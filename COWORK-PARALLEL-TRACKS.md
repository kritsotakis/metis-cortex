# Cowork brief — Parallel tracks: Calendly + Email forward + LinkedIn + ASIC watch

> **For:** Cowork
> **Authored by:** Claude Code, 2026-05-08
> **Goal:** Knock out the four no-code-required tasks that unlock first-booking infrastructure, inbound email, and brand presence. Site is live at https://metiscortex.au — these tasks build the surrounding sales surface.

---

## State of play (read this before briefing Peter)

- ✅ Site live at https://metiscortex.au + https://www.metiscortex.au (SSL, auto-deploy)
- ✅ Brand bundle at `public/brand/` (logos, social kit, brand guide)
- ✅ Copy decks ready: [LINKEDIN-COMPANY-PAGE-COPY.md](LINKEDIN-COMPANY-PAGE-COPY.md), [LINKEDIN-FIRST-POST-DRAFT.md](LINKEDIN-FIRST-POST-DRAFT.md), [LINKEDIN-FIRST-100-OUTREACH.md](LINKEDIN-FIRST-100-OUTREACH.md)
- ✅ Calendly confirmation email + onboarding sequence ready: [CALENDLY-CONFIRMATION-EMAIL.md](CALENDLY-CONFIRMATION-EMAIL.md), [ONBOARDING-EMAIL-SEQUENCE.md](ONBOARDING-EMAIL-SEQUENCE.md)
- ⏸️ ASIC business name registration paid 2026-05-08, registration number arrives in 1–2 business days
- ⏸️ claude.ai/design refining logos in parallel — do not touch `public/brand/` until those land

---

## The auth wall (re-confirmed pattern)

Same as Cloudflare + GoDaddy in prior tasks: **kapture is a separate session from Peter's logged-in Chrome.** Calendly, GoDaddy email management, LinkedIn — all session-bound auth. **Peter drives the clicks. You drive the prep + verification + STATUS update.**

Don't waste cycles trying to drive Calendly's UI or LinkedIn's setup wizard from your sandbox. Brief Peter precisely so he can execute in one sitting.

---

## Task A — Calendly demo URL (15 min, Peter's browser)

### Brief Peter with this verbatim

> **Goal:** A bookable URL like `calendly.com/metiscortex/demo` that lands prospects in your calendar with the right pre-call questions and the confirmation email we drafted.
>
> **Steps:**
> 1. calendly.com → sign in with **peter@kritsotakis.com.au** (or create account if first time — free tier is fine)
> 2. **Account settings → Branding** → upload `public/brand/social/linkedin-company-square.png` as profile photo (or any 400×400 mark from `public/brand/`)
> 3. **Account settings → Account name** → set to `Metis Cortex` (this becomes the URL slug if you let it)
> 4. **+ Create → One-on-One** event:
>    - Event name: `Metis Cortex demo — 20 min`
>    - Location: Google Meet (or Zoom, your call)
>    - Duration: 20 minutes
>    - Date range: Rolling 30 days
>    - Available hours: pick what suits — recommend Mon–Fri 09:00–17:00 AEST
>    - Buffer: 15 min before, 15 min after
>    - Min notice: 4 hours
> 5. **Invitee questions** — add these three:
>    - "What's your business and where are you based?" (required)
>    - "How many calls/messages a week are you missing?" (required)
>    - "What's the biggest bottleneck right now — answering, follow-up, or database activation?" (required)
> 6. **Confirmation page** → paste the body from [CALENDLY-CONFIRMATION-EMAIL.md](CALENDLY-CONFIRMATION-EMAIL.md) into the custom confirmation message
> 7. **Workflows → + New** → "Send no-show follow-up" → trigger 24h after no-show → paste no-show template from same file
> 8. **Save + copy the public URL** (looks like `https://calendly.com/metiscortex/demo` or `https://calendly.com/metiscortex-au/demo`)
> 9. Reply with: `Calendly URL: <paste>`

### What you (Cowork) do after Peter posts the URL

1. **Verify the URL loads:**
   ```bash
   curl -sIo /dev/null -w "Calendly: HTTP %{http_code}\n" <URL>
   # Expected: 200 (or 301 redirect to 200)
   ```

2. **Smoke-test the booking flow:** open `<URL>` in kapture, confirm the three invitee questions render, confirm the brand mark shows on the booking page. (The auth wall doesn't prevent VIEWING a public Calendly link.)

3. **Flag Code to wire it in:** post in PAIR.md:
   ```
   ### YYYY-MM-DD HH:MM — cowork → code
   **Did:** Calendly URL verified live: <URL>
   **Need from you:** Replace placeholder href in src/components/CTAButton.tsx with this URL. Same commit batch as Footer email update if both land same day.
   **Status:** ⏸️ waiting-on-pair
   ```

4. **Update STATUS.md** — Done This Sprint:
   > 2026-05-08 — Calendly demo URL live: `<URL>` — 20-min event, 3 qualifying questions, branded confirmation email, no-show workflow. Peter (clicks) + Cowork (verify + STATUS).

   Close in Open Loops: "Calendly demo URL setup pending"

   Mirror to `~/.claude/memory/metis-cortex-status.md` (Code will sync if you can't write there).

---

## Task B — GoDaddy `hello@metiscortex.au` email forward (10 min, Peter's browser)

### Brief Peter with this verbatim

> **Goal:** Inbound emails to `hello@metiscortex.au` forward to `peter@kritsotakis.com.au` so prospects who skip Calendly can still reach you.
>
> **Steps:**
> 1. godaddy.com → sign in → **My Products** → find **`metiscortex.au`**
> 2. Look for **Email & Office** OR **Email Forwarding** OR **Workspace Email** (GoDaddy moves this around — try all three)
> 3. If GoDaddy shows "free email forwarding included with domain": **Set up forwarding**
>    - Forward from: `hello@metiscortex.au`
>    - Forward to: `peter@kritsotakis.com.au`
>    - Save
> 4. If GoDaddy says "email forwarding requires Microsoft 365 paid plan": **stop and tell me** — we'll use Cloudflare Email Routing instead (free, requires DNS records I'll add)
> 5. Test from your phone: send an email to `hello@metiscortex.au` from any other address. Should land in `peter@kritsotakis.com.au` within 5 min.
> 6. Reply with one of:
>    - `Email forward live` (it worked)
>    - `GoDaddy wants paid plan — switch to Cloudflare` (we'll pivot)

### What you (Cowork) do after Peter posts result

**If `Email forward live`:**

1. **Verify deliverability** — ask Peter to send a test from any external address; confirm receipt.
2. **Check MX records weren't broken:**
   ```bash
   dig MX metiscortex.au +short
   # Expected: GoDaddy MX records (mailstore1.secureserver.net + smtp.secureserver.net) OR Cloudflare's depending on path
   ```
3. **Flag Code to wire in:**
   ```
   ### YYYY-MM-DD HH:MM — cowork → code
   **Did:** Email forward verified live: hello@metiscortex.au → peter@kritsotakis.com.au
   **Need from you:** Update src/components/Footer.tsx — replace any placeholder email/contact text with `hello@metiscortex.au` mailto link.
   **Status:** ⏸️ waiting-on-pair
   ```
4. **STATUS.md update** — Done This Sprint:
   > 2026-05-08 — `hello@metiscortex.au` forwards to `peter@kritsotakis.com.au` (GoDaddy email forwarding). Verified by external test send. Peter (clicks) + Cowork (verify + STATUS).

**If `GoDaddy wants paid plan — switch to Cloudflare`:**

Tell Peter:
> Switching to Cloudflare Email Routing (free, runs at the DNS layer):
> 1. dash.cloudflare.com → metiscortex.au zone → **Email** (left sidebar)
> 2. **Get started** → Cloudflare adds 3 MX records + 1 TXT (SPF) automatically
> 3. **Routing rules → Custom address** → from `hello@metiscortex.au` → to `peter@kritsotakis.com.au`
> 4. **Verify destination** — Cloudflare emails peter@kritsotakis.com.au, click confirm
> 5. Send test from external address → should land

Then run the same verification + STATUS update path as the GoDaddy success case.

---

## Task C — LinkedIn company page (30 min, Peter's browser)

### Brief Peter with this verbatim

> **Goal:** A live LinkedIn company page for Metis Cortex with brand assets, copy, and a Founder profile linking back. This unblocks the first-100 outreach plan.
>
> **Pre-flight (don't skip):** copy in [LINKEDIN-COMPANY-PAGE-COPY.md](LINKEDIN-COMPANY-PAGE-COPY.md), assets in [public/brand/social/](public/brand/social/) — specifically:
> - **Logo:** `public/brand/social/linkedin-company-square.png` (400×400)
> - **Cover image:** `public/brand/social/linkedin-company-cover.png` (1128×191)
>
> **Steps:**
> 1. linkedin.com → top nav **Work** menu → **Create a Company Page** → choose **Company** (NOT Showcase, Educational, or Small Business — we want the standard Company entity)
> 2. **Page identity:**
>    - Name: `Metis Cortex`
>    - LinkedIn public URL: `linkedin.com/company/metis-cortex` (if taken try `metiscortex` or `metiscortex-au`)
>    - Website: `https://metiscortex.au`
>    - Industry: `Business Consulting and Services`
>    - Company size: `1-10 employees`
>    - Company type: `Privately held`
>    - Tagline: paste from LINKEDIN-COMPANY-PAGE-COPY.md "Tagline" section
> 3. **Logo + cover:** upload both files from `public/brand/social/`
> 4. **About section:** paste full "About" block from LINKEDIN-COMPANY-PAGE-COPY.md
> 5. **Specialities** (max 20): paste from doc
> 6. **Save + Publish**
> 7. **Update your personal profile** (peter@kritsotakis.com.au LinkedIn):
>    - Add experience: "Founder, Metis Cortex" — link to the new company page
>    - Update headline: paste from LINKEDIN-COMPANY-PAGE-COPY.md "Personal headline" section
> 8. Reply with: `LinkedIn page live: <URL>`

### What you (Cowork) do after Peter posts URL

1. **Verify page is public:**
   ```bash
   curl -sIo /dev/null -w "LinkedIn page: HTTP %{http_code}\n" <URL>
   # Expected: 200
   ```

2. **Open in kapture, sanity-check rendering:** logo crisp at 400×400, cover not stretched/cropped weirdly, About copy renders without truncation (LinkedIn truncates at ~300 chars in preview — confirm the hook line is in the first 300 chars).

3. **Flag back to Peter what to do next:**
   > Page live, looks clean. Three follow-on actions when you're ready (no rush, can wait until after DSK pilot Day 28 data lands):
   > - Pin the first post (template in LINKEDIN-FIRST-POST-DRAFT.md) — wait for real DSK pilot numbers before publishing
   > - Run first-100 outreach (plan in LINKEDIN-FIRST-100-OUTREACH.md) — gated on DSK pilot data
   > - Apollo enrichment (26→50) — gated on DSK pilot data per STATUS

4. **STATUS.md update** — Done This Sprint:
   > 2026-05-08 — LinkedIn company page live: `<URL>` — branded logo + cover, About copy from LINKEDIN-COMPANY-PAGE-COPY.md, Peter's profile updated with Founder role. First post + outreach campaign held until DSK pilot Day 28 data lands. Peter (clicks) + Cowork (verify + STATUS).

   Close in Open Loops: "LinkedIn company page launch"

---

## Task D — ASIC business name registration number watch (passive)

### What this is

ASIC paid 2026-05-08 for business name registration. Number arrives via email to peter@kritsotakis.com.au within 1–2 business days. Once it lands, it needs to appear in:

- Website footer (legal/compliance)
- LinkedIn company page (Specialities → also valid in description)
- Email signatures
- Any future invoices/quotes

### Brief Peter

> When the ASIC email lands with the registration number, just forward it or paste the number in chat with `ASIC reg number: <number>`. We'll handle wiring it into Footer.tsx + LinkedIn + signatures.

### What you (Cowork) do when Peter posts the number

1. **Don't change LinkedIn yet** unless Peter's personal profile already shows it — let Peter paste it once into chat, then both Code + Cowork act in parallel.

2. **Flag to Code via PAIR.md:**
   ```
   ### YYYY-MM-DD HH:MM — cowork → code
   **Did:** ASIC reg number received: <number>
   **Need from you:** Add to src/components/Footer.tsx fine print — `ABN 45 984 876 899 · Business name: Metis Cortex (ASIC reg <number>)` — same commit batch as Calendly + email Footer updates if all three land same day.
   **Status:** ⏸️ waiting-on-pair
   ```

3. **Update LinkedIn About section** — append "ASIC business name registration <number>" to the About copy. (Peter does the click; you brief.)

4. **STATUS.md update** — Done This Sprint:
   > YYYY-MM-DD — ASIC business name registration number received: `<number>`. Wired into Footer + LinkedIn About. Peter (forwarded) + Code (Footer commit) + Cowork (LinkedIn brief + STATUS).

   Close in Open Loops: "ASIC registration number pending"

---

## Order of operations

These four tasks are independent — Peter can do them in any order. Recommended sequence based on speed-to-value:

1. **Task B (email forward)** — 10 min, unblocks any "the website doesn't have a contact email" friction
2. **Task A (Calendly)** — 15 min, unblocks first booking
3. **Task C (LinkedIn)** — 30 min, brand presence (no urgency until DSK pilot data)
4. **Task D (ASIC)** — passive, fires when email lands

If Peter wants to batch into one sitting, that's ~55 min total.

---

## What Cowork must NOT do

- **Do not** drive Calendly / GoDaddy / LinkedIn UIs via kapture for any session-bound action (sign-in, settings changes, page creation). Auth wall is permanent.
- **Do not** modify `public/brand/` files — claude.ai/design is iterating on logos in parallel; their output supersedes anything you'd touch.
- **Do not** commit to the repo. Code owns the repo edits. You flag changes via PAIR.md.
- **Do not** publish the LinkedIn first post or run outreach yet — gated on DSK pilot Day 28 data per STATUS Open Loops.
- **Do not** declare a task done without the verification step (curl check, kapture render check, or external test send).

---

## Confirmation Cowork posts back per task

```
✅ Task <A|B|C|D> done. <one-line outcome>.
   Verified: <list of checks that passed>
   PAIR.md flagged Code: <yes — for Footer/CTAButton wiring | n/a>
   STATUS.md updated, memory mirror flagged for Code.
```

If a task fails or hits an unexpected wall:

```
⚠️ Task <X> blocked. <what Peter tried>.
   Surfacing to Peter:
   - <specific failure>
   - <recommended fix or pivot>
   STATUS.md NOT yet updated.
```

---

## Reference

- [STATUS.md](STATUS.md) — canonical state
- [CALENDLY-CONFIRMATION-EMAIL.md](CALENDLY-CONFIRMATION-EMAIL.md) — Task A confirmation copy
- [LINKEDIN-COMPANY-PAGE-COPY.md](LINKEDIN-COMPANY-PAGE-COPY.md) — Task C page copy
- [LINKEDIN-FIRST-POST-DRAFT.md](LINKEDIN-FIRST-POST-DRAFT.md) — Task C follow-on (held)
- [LINKEDIN-FIRST-100-OUTREACH.md](LINKEDIN-FIRST-100-OUTREACH.md) — Task C follow-on (held)
- [COWORK-CUSTOM-DOMAIN-ATTACH.md](COWORK-CUSTOM-DOMAIN-ATTACH.md) — precedent for auth-wall + verification pattern
- [PAIR.md](PAIR.md) — live Code↔Cowork channel
