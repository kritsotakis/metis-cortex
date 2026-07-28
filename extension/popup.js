/**
 * Popup: choose a matter and (optionally) a checklist item, then either arm the
 * next download or capture the page currently open.
 *
 * "Arm" rather than "always on" is deliberate. An extension that silently
 * uploads every download you make is a bad neighbour, and filing something
 * against the wrong checklist item is annoying to unpick.
 *
 * Server selection is automatic and visible in the UI. The first version asked
 * the user to paste JavaScript into the service-worker console to point it at a
 * local server — which is an unreasonable thing to ask of anyone, and which the
 * first person to try it understandably pasted into a search box instead.
 */

const STATE_KEY = "metisTarget";
const PRODUCTION = "https://metis-cortex.fly.dev";
const LOCAL = "http://localhost:3000";

const $ = id => document.getElementById(id);

function setStatus(msg, kind) {
  const el = $("status");
  el.className = `status ${kind}`;
  el.textContent = msg;
}

/** Does this server answer, and are we signed in to it? */
async function probe(base) {
  try {
    const res = await fetch(`${base}/api/extension/targets`, {
      credentials: "include",
      signal: AbortSignal.timeout(2500),
    });
    if (res.ok) return { base, state: "ready", data: await res.json() };
    if (res.status === 401) return { base, state: "signed-out" };
    return null;
  } catch {
    return null;
  }
}

/**
 * Prefer whichever server is actually running and signed in. A dev server on
 * localhost means that's the one being worked on, so it wins when both answer.
 */
async function resolveServer() {
  const saved = (await chrome.storage.local.get("metisBase")).metisBase;
  if (saved) {
    const r = await probe(saved);
    if (r) return r;
    // Saved server has gone away — fall through and look again rather than
    // stranding the user on a dead address.
  }
  const [local, prod] = await Promise.all([probe(LOCAL), probe(PRODUCTION)]);
  const chosen =
    (local?.state === "ready" && local) ||
    (prod?.state === "ready" && prod) ||
    local ||
    prod;
  if (chosen) await chrome.storage.local.set({ metisBase: chosen.base });
  return chosen;
}

function renderServerLine(base, onSwitch) {
  const other = base === LOCAL ? PRODUCTION : LOCAL;
  const label = base === LOCAL ? "local dev server" : "metiscortex (live)";
  const otherLabel = other === LOCAL ? "local dev server" : "live server";
  $("server").innerHTML =
    `Connected to the <strong>${label}</strong> — ` +
    `<a href="#" id="switchServer">use the ${otherLabel} instead</a>`;
  $("switchServer").onclick = async e => {
    e.preventDefault();
    await chrome.storage.local.set({ metisBase: other });
    onSwitch();
  };
}

async function load() {
  $("main").style.display = "none";
  $("signedOut").style.display = "none";
  $("server").textContent = "Looking for Metis…";

  const found = await resolveServer();

  if (!found) {
    $("signedOut").style.display = "block";
    $("signedOutMsg").textContent =
      "Couldn't reach Metis — is the app running?";
    $("openMetis").onclick = () => chrome.tabs.create({ url: PRODUCTION + "/metis" });
    $("server").innerHTML =
      `Tried the local dev server and the live one. ` +
      `<a href="#" id="retry">Try again</a>`;
    $("retry").onclick = e => { e.preventDefault(); load(); };
    return;
  }

  renderServerLine(found.base, load);

  if (found.state === "signed-out") {
    $("signedOut").style.display = "block";
    $("signedOutMsg").textContent = "You're not signed in to Metis.";
    $("openMetis").onclick = () => chrome.tabs.create({ url: found.base + "/metis" });
    return;
  }

  const targets = found.data.targets || [];
  if (!targets.length) {
    $("signedOut").style.display = "block";
    $("signedOutMsg").textContent = "No matters yet — set one up in Metis first.";
    $("openMetis").onclick = () => chrome.tabs.create({ url: found.base + "/metis" });
    return;
  }

  $("main").style.display = "block";

  const matterSel = $("matter");
  matterSel.innerHTML = targets.map(t => `<option value="${t.id}">${t.title}</option>`).join("");

  function renderItems() {
    const t = targets.find(x => String(x.id) === matterSel.value);
    $("item").innerHTML =
      `<option value="">— just add it to the matter —</option>` +
      (t?.items || []).map(i => `<option value="${i.key}">${i.name}</option>`).join("");
  }
  matterSel.onchange = renderItems;
  renderItems();

  const saved = (await chrome.storage.local.get(STATE_KEY))[STATE_KEY];
  if (saved?.matterId && targets.some(t => t.id === saved.matterId)) {
    matterSel.value = String(saved.matterId);
    renderItems();
    if (saved.itemKey) $("item").value = saved.itemKey;
    if (saved.armed) $("armedNote").style.display = "block";
  }

  $("arm").onclick = async () => {
    await chrome.storage.local.set({
      [STATE_KEY]: {
        matterId: Number(matterSel.value),
        itemKey: $("item").value || null,
        armed: true,
      },
    });
    $("armedNote").style.display = "block";
    setStatus("Ready. Your next download will be saved.", "ok");
  };

  $("capturePage").onclick = async () => {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    if (!tab?.url || !/^https?:/.test(tab.url)) {
      setStatus("This page can't be saved.", "err");
      return;
    }
    setStatus("Saving…", "ok");
    chrome.runtime.sendMessage(
      {
        type: "CAPTURE_URL",
        payload: {
          url: tab.url,
          filename: (tab.title || "page").replace(/[^\w.-]+/g, "-").slice(0, 80) + ".pdf",
          matterId: Number(matterSel.value),
          itemKey: $("item").value || null,
        },
      },
      resp => {
        if (resp?.ok) {
          const r = resp.result;
          setStatus(
            `Saved to "${r.matterTitle}"` +
              (r.extractionStatus === "needs_ocr" ? " — but Metis can't read inside it." : ""),
            "ok",
          );
        } else {
          setStatus(resp?.error || "That didn't work.", "err");
        }
      },
    );
  };

  const { lastCapture, lastError } = await chrome.storage.local.get(["lastCapture", "lastError"]);
  if (lastCapture && Date.now() - lastCapture.at < 60_000) {
    setStatus(
      `Saved "${lastCapture.fileName}" to ${lastCapture.matterTitle}` +
        (lastCapture.attachedTo ? " and ticked it off." : "."),
      "ok",
    );
  } else if (lastError && Date.now() - lastError.at < 60_000) {
    setStatus(lastError.message, "err");
  }
}

load();
