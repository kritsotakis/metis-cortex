/**
 * Metis Companion — service worker.
 *
 * Watches for downloads and, when one looks like a document, offers to file it
 * into the matter the user has selected. It never navigates, never logs in, and
 * never touches a page the user hasn't opened themselves.
 *
 * The one clever bit: rather than trying to read the finished file off disk
 * (which MV3 can't do without file:// access), it re-fetches the download's own
 * URL from the extension context. Because the request carries the site's
 * cookies, an authenticated PDF from myGov or the ATO comes back fine — the
 * same bytes the browser just saved, without ever reading the filesystem.
 */

const STATE_KEY = "metisTarget";

/** Where Metis lives. Localhost first so a dev build doesn't hit production. */
async function apiBase() {
  const { metisBase } = await chrome.storage.local.get("metisBase");
  return metisBase || "https://metis-cortex.fly.dev";
}

async function getTarget() {
  const state = await chrome.storage.local.get(STATE_KEY);
  return state[STATE_KEY] || null;
}

function looksLikeDocument(item) {
  const name = (item.filename || "").toLowerCase();
  const mime = (item.mime || "").toLowerCase();
  if (mime.includes("pdf") || mime.includes("word") || mime.startsWith("image/")) return true;
  return /\.(pdf|docx?|jpe?g|png|webp|txt|md)$/.test(name);
}

/** Toast via the badge — a notification permission isn't worth it for this. */
async function flash(text, color) {
  await chrome.action.setBadgeBackgroundColor({ color });
  await chrome.action.setBadgeText({ text });
  setTimeout(() => chrome.action.setBadgeText({ text: "" }), 4000);
}

async function captureFromUrl({ url, filename, matterId, itemKey }) {
  // Re-fetch in the extension context; cookies for the originating site ride
  // along, which is what makes an authenticated agency PDF retrievable.
  const res = await fetch(url, { credentials: "include" });
  if (!res.ok) throw new Error(`Couldn't fetch the file (${res.status})`);
  const blob = await res.blob();

  const form = new FormData();
  form.append("file", blob, filename || "document.pdf");
  form.append("matterId", String(matterId));
  if (itemKey) form.append("itemKey", itemKey);
  form.append("fileName", filename || "document.pdf");

  const base = await apiBase();
  const up = await fetch(`${base}/api/extension/capture`, {
    method: "POST",
    body: form,
    credentials: "include",
  });
  if (!up.ok) {
    const body = await up.json().catch(() => ({}));
    throw new Error(body.error || `Metis rejected it (${up.status})`);
  }
  return up.json();
}

chrome.downloads.onCreated.addListener(async item => {
  try {
    const target = await getTarget();
    // Only act when the user has explicitly armed a matter. Silence otherwise —
    // an extension that grabs every download you make is not a good neighbour.
    if (!target?.armed || !target.matterId) return;
    if (!looksLikeDocument(item)) return;

    const result = await captureFromUrl({
      url: item.finalUrl || item.url,
      filename: (item.filename || "").split(/[\\/]/).pop(),
      matterId: target.matterId,
      itemKey: target.itemKey,
    });

    await chrome.storage.local.set({
      lastCapture: {
        at: Date.now(),
        fileName: result.fileName,
        matterTitle: result.matterTitle,
        attachedTo: result.attachedTo,
        extractionStatus: result.extractionStatus,
      },
    });
    await flash("✓", "#1a7f5a");

    // One-shot by default: after a capture, disarm. Filing a document against
    // the wrong checklist item is tedious to unpick, and silently hoovering up
    // every subsequent download is worse than making the user click again.
    if (!target.keepArmed) {
      await chrome.storage.local.set({ [STATE_KEY]: { ...target, armed: false } });
    }
  } catch (err) {
    console.error("[Metis] capture failed:", err);
    await chrome.storage.local.set({ lastError: { at: Date.now(), message: String(err.message || err) } });
    await flash("!", "#b3261e");
  }
});

// Lets the popup capture the current tab directly, for a PDF already on screen
// rather than one being downloaded.
chrome.runtime.onMessage.addListener((msg, _sender, sendResponse) => {
  if (msg?.type !== "CAPTURE_URL") return;
  captureFromUrl(msg.payload)
    .then(result => sendResponse({ ok: true, result }))
    .catch(err => sendResponse({ ok: false, error: String(err.message || err) }));
  return true; // async
});
