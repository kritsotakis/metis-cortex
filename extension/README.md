# Metis Companion — browser extension

Saves a document you're looking at straight into a Metis matter, against the
right checklist item.

## What problem it solves

Getting one document into Metis today: find it on the agency site → download →
switch tabs → click upload → hunt through your Downloads folder → pick which
checklist item it belongs to. A parenting matter has seventeen items.

With this: pick the matter once, download the document as normal, done.

## What it does and doesn't do

**Does:** re-fetch a file you downloaded and send it to Metis; file it against a
checklist item and tick it off; extract the text so Metis can read it.

**Doesn't:** sign in for you, browse on its own, or touch a page you didn't
open. It is armed one download at a time, and stays silent otherwise.

That restraint is deliberate. Whether a tool may drive a logged-in session on
myGov or the ATO is an open legal question — see §4A of the lawyer brief — and
nothing here depends on the answer.

## Install (unpacked, for personal use)

1. Chrome → `chrome://extensions`
2. Turn on **Developer mode** (top right)
3. **Load unpacked** → select this `extension/` folder
4. Copy the **ID** Chrome assigns it

Then tell the server that ID is allowed, and restart it:

```
METIS_EXTENSION_ID=<the id chrome gave you>
```

Without that variable the extension's requests are refused — cross-origin
access is off by default rather than open to every installed extension.

### Which server it talks to

It works this out itself. On opening, it checks the local dev server and the
live one, prefers whichever is running and signed in, and shows which it chose
at the top of the popup with a link to switch. Nothing to configure.

## Using it

1. Sign in to Metis in a normal tab (the extension uses that session).
2. Click the extension icon, choose the matter and — optionally — the checklist
   item the document belongs to.
3. **Arm — save my next download**, then download the document as you normally
   would. A green tick on the icon means it landed.
4. Or **Save the page I'm on now**, for a PDF already open on screen.

Attaching to a checklist item marks it confirmed, because you chose it while
looking at the document. That's a stronger assertion than the filename matching
the web app does — and it's still your assertion, not Metis's guess.

## Permissions, and why each is needed

- `downloads` — to notice when you've downloaded something
- `storage` — remembers which matter you selected
- `activeTab` / `scripting` — reads the URL of the tab you're on for "save this
  page"
- Host access to Metis itself — to send the file
- `optional_host_permissions` — granted per-site by you, only when a capture
  needs to re-fetch from that site. Nothing is requested up front.

## Known limits

- A file only comes back if its URL is still fetchable with your session. Some
  sites generate one-time download links; if a capture fails, download the file
  and upload it through the web app instead.
- Scans and images are stored but not readable — Metis will say so rather than
  pretend.
- Not published to the Chrome Web Store. Unpacked, personal use.
