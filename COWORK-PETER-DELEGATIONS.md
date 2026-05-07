# Cowork brief — Peter delegations

> **For:** Cowork
> **Authored by:** Claude Code, 2026-05-07
> **Why this brief:** Most pending action items previously gated on Peter can be delegated to Cowork now that filesystem access + browser-driving are live. This brief separates **Peter-only** items (security, signing, personal relationships) from **Cowork-executable** items (browser config, API calls, drafting + sending).

---

## What stays with Peter (truly only him, ~5 min total)

These are not delegable — security, personal relationships, signing.

| # | Action | Why Peter only | Time |
|---|---|---|---|
| **P1** | Rotate Cloudflare password | Password generation should happen in Peter's password manager and the new password should never leave it. Cowork must NOT touch this. | 3 min |
| **P2** | Enable 2FA on Cloudflare via authenticator app on his phone | 2FA seed lives on his physical device. Save recovery codes in 1Password. | 2 min |
| **P3** | Send 1-line WhatsApp/SMS to the Eonia clinical team asking which CMS they use (Cliniko / Pabau / Halaxy / Timely / Fresha / Phorest / other) | Existing relationship; should come from Peter's number, not a generic Cowork email. Message text in `EONIA-CMS-MESSAGE.md`. | 30 sec |
| **P4** | Sign any legal document that comes back from the lawyer engagement (term sheet finalisation, employer agreement) | Legally binding signature must be Peter's. Cowork does NOT sign on his behalf. | varies |
| **P5** | Confirm the GitHub repo creation step (one of Path A / Path B below) | Peter chooses path; Cowork executes the chosen one. | 1 min decision |

**Total Peter time: ~6 min.**

---

## What Cowork takes over (everything else)

The remaining items Peter has been gated on can all be Cowork-executed now. Tasks 1–5 below are the pre-launch unblock chain.

### Task 1 — GitHub repo creation

Peter chooses one of two paths in P5 above. Cowork executes the chosen path.

**Path A — `gh` CLI (faster).** If `gh auth status` shows Peter authenticated locally:

```bash
cd ~/Desktop/metis-cortex
gh auth status   # verify
gh repo create kritsotakis/metis-cortex --private --source . --remote origin
```

**Path B — browser.** If `gh` CLI not authenticated:

1. github.com → top-right `+` → New repository
2. Owner: confirm with Peter (default: `kritsotakis`)
3. Name: `metis-cortex`
4. **Private**
5. Do NOT init with README, .gitignore, or license (local repo already has them)
6. Create repository
7. Copy the HTTPS URL

Then in either path, run:

```bash
cd ~/Desktop/metis-cortex
git remote add origin <HTTPS_URL>   # Path B only — Path A handles this
```

**Deliverable:** repo URL captured + first commit ready to push (committed locally but unpushed). Pause here until Peter confirms Cloudflare P1+P2 are done. Pushing code that ties to a compromised Cloudflare account is the same security risk as never rotating.

**Timebox:** 5 min.

### Task 2 — Commit + push the migration

Once Peter confirms P1 + P2 (Cloudflare password rotated + 2FA enabled):

```bash
cd ~/Desktop/metis-cortex
git add -A
git status   # sanity check — confirm no .env or secrets staged
git commit -m "$(cat <<'EOF'
feat: brand bundle v3, static export, full content suite

- Manus brand bundle v3 (favicons, lockups, mark variants, social kit, brand guide PDF)
- Hero + Footer brand mark inline (40x40, navy + transparent variants, optimised PNGs)
- AI agent persona renamed Mia → Zoe (Greek for "life")
- next.config.ts: output: export, images.unoptimized, trailingSlash
- layout.tsx: openGraph + twitter metadata reference static /og.png
- Removed dynamic OG endpoints (opengraph-image.tsx, twitter-image.tsx)
- Added 15 customer-facing content docs (LinkedIn, sales prep, onboarding, pilot capture, etc.)

Co-Authored-By: Cowork <noreply@cowork>
EOF
)"
git push -u origin main   # or master — match the branch name
```

**Sanity check before push:** confirm `git diff --cached` doesn't include any of: `.env`, `.env.local`, `secrets.json`, anything matching `*key*` or `*token*` patterns. The repo should not contain credentials.

**Deliverable:** commit SHA + push successful + GitHub repo shows the code.

**Timebox:** 3 min.

### Task 3 — Cloudflare Pages → Connect to Git

In the Cloudflare dashboard (Cowork drives the browser if Peter has shared the session):

1. **Workers & Pages** → **Create application** → **Pages** tab → **Connect to Git**
2. Authorize Cloudflare to access GitHub if prompted → select the `metis-cortex` repo
3. Build settings:
   - **Project name:** `metis-cortex`
   - **Production branch:** `main` (or `master`)
   - **Framework preset:** **Next.js (Static HTML Export)** — IMPORTANT, not the regular "Next.js" preset
   - **Build command:** `npm run build`
   - **Build output directory:** `out`
   - **Root directory:** `/`
   - **Environment variables:** none (Node defaults to LTS in Cloudflare's CI, side-stepping Peter's local Node 25 issue)
4. **Save and Deploy**
5. Wait ~90 sec for first build. If the build fails, surface the build log error before continuing.
6. Once green, capture the `.pages.dev` preview URL.

**Deliverable:** Pages project deployed at `metis-cortex.pages.dev` (or whatever Cloudflare assigns). Smoke-test by curling the preview URL — should return HTTP 200 + render the Metis Cortex hero.

**Timebox:** 10 min.

### Task 4 — Add custom domain `metiscortex.au`

1. In the Pages project → **Custom domains** → **Set up a custom domain**
2. Enter `metiscortex.au` → Cloudflare will detect the zone (already added) and configure CNAME automatically
3. SSL/TLS mode: **Full (Strict)** — Cloudflare manages SSL end-to-end, Pages serves over HTTPS
4. The Vercel A records currently in the zone get auto-replaced when the custom domain attaches. No manual cleanup needed.

**Deliverable:** `https://metiscortex.au` resolves to the Pages deployment with HTTPS green.

**Timebox:** 5 min.

### Task 5 — GoDaddy nameserver swap

For both `metiscortex.au` AND `exitcode.trade`:

1. Log into GoDaddy → **My Products** → domains list
2. For each domain → **DNS** → **Nameservers** → **Change** → **I'll use my own nameservers**
3. Paste:
   - `emerie.ns.cloudflare.com`
   - `jimmy.ns.cloudflare.com`
4. Save. Wait up to 24h for propagation.

**Verification (24h later):**

```bash
dig +short NS metiscortex.au
dig +short NS exitcode.trade
```

Both should return Cloudflare nameservers.

**Deliverable:** nameserver swap complete, propagation in flight.

**Timebox:** 5 min execute + ≤24h wait.

---

### Task 6 — Calendly demo URL

(Independent of the Cloudflare chain — can run in parallel.)

1. Log into Peter's Calendly (`peter@kritsotakis.com.au`)
2. Create new Event Type: **"Metis Cortex Demo — 10 min"**
3. Configure per `CALENDLY-CONFIRMATION-EMAIL.md` instructions (already in repo):
   - Duration: 10 min
   - Availability: Mon–Fri 09:00–18:00 AEST
   - Calendar sync: Peter's primary Google Calendar
   - Buffer: 15 min before/after
   - Cap: 4 demos/day
   - Pre-call questions (2 required, free text per the existing doc)
4. **Notifications → Confirmation email → Customise** → paste the body from `CALENDLY-CONFIRMATION-EMAIL.md`
5. **Notifications → Cancellation/no-show notification** → paste the no-show template from same doc
6. Capture the public URL — likely `https://calendly.com/peter-kritsotakis/metis-cortex-demo`

**Self-test:** book a demo using a throwaway email, verify:
- Custom confirmation email lands (the one Cowork drafted)
- Event appears in Peter's Google Calendar
- Pre-call questions captured
- 1-hour-before reminder schedules

**Deliverable:** Calendly URL pasted to Peter + Code. Code updates `CTAButton.tsx` line 5 in next commit batch.

**Timebox:** 15 min.

### Task 7 — GoDaddy `hello@metiscortex.au` email forwarding

1. GoDaddy → My Products → `metiscortex.au` → **Email & Office** → **Email Forwarding**
2. Set up forwards:
   - `hello@metiscortex.au` → `peter@kritsotakis.com.au`
   - `peter@metiscortex.au` → `peter@kritsotakis.com.au`
3. Confirm GoDaddy auto-adds the MX records to DNS

**Important:** when Task 5 (nameserver swap) propagates, the MX records need to be migrated from GoDaddy DNS to Cloudflare DNS. Cowork: **capture the MX values BEFORE the nameserver swap**, then re-add them in Cloudflare DNS panel post-propagation. Otherwise the email forwarding breaks.

**Self-test:** send an email from a different address to `hello@metiscortex.au`, confirm it lands in `peter@kritsotakis.com.au` within 5 min.

**Deliverable:** email forward live + MX records migrated to Cloudflare.

**Timebox:** 10 min execute + ≤24h wait for nameserver propagation.

### Task 8 — LinkedIn company page execute

Cowork drives Peter's LinkedIn session (if Peter has shared it via browser-passthrough).

1. linkedin.com → top nav **Work** dropdown → **Create a Company Page** → **Small business**
2. Paste copy from `LINKEDIN-COMPANY-PAGE-COPY.md` (in repo) into the wizard fields
3. Logo: upload `~/Desktop/metis-cortex/public/brand/social/linkedin-company-logo.png` (300×300, Manus-rendered)
4. Cover banner: upload `~/Desktop/metis-cortex/public/brand/social/linkedin-company-cover.png` (1128×191)
5. Add specialties list from the doc
6. Set Peter as **Page Admin**
7. **Publish**
8. On Peter's personal LinkedIn profile → add "Metis Cortex" as a current position (links page to profile)

**Deliverable:** LinkedIn company page URL captured.

**Don't post yet.** Per `LINKEDIN-FIRST-100-OUTREACH.md`, the first 7 days are invite-only (50–100 follower invites from Peter's network), no posts until DSK pilot Day 28 data lands.

**Timebox:** 30 min.

### Task 9 — Apollo prospect enrichment (26 → 50 + verified emails)

Cowork has the Apollo plugin (`apollo:prospect`).

1. Read `COLD-EMAIL-V1-PROSPECTS.md` — 26 starter rows + Apollo handoff brief at the bottom
2. Run `/prospect` in Cowork with the ICP brief from that doc
3. Expected output: ~24 additional prospects + verified emails for the 26 existing rows + LinkedIn URLs + confidence scores
4. Update `COLD-EMAIL-V1-PROSPECTS.md` with the enriched data
5. Update `STATUS.md` Open Loop #11 from "Apollo enrichment pending" → "Done — 50 verified rows, awaiting DSK pilot Day 28 to send"

**Critical rule:** DO NOT send any cold emails until DSK pilot Day 28 numbers are real. Empty case-study placeholders sink cold emails.

**Deliverable:** enriched prospect file + STATUS update.

**Timebox:** 15 min.

### Task 10 — Engage one lawyer for the term sheet review

1. Read `THERAPIST-LAWYER-SHORTLIST.md` — three firms (LegalVision / Sprintlaw / Coutts Legal) with email template
2. Send the email from the doc to all three in parallel from `peter@kritsotakis.com.au` — Cowork drafts and sends, Peter on the From line
3. When responses come back (likely within 1–2 business days), evaluate per the criteria in the doc:
   - Specialisation confirmation (Beauty Award + casual + profit-share)
   - Fee within A$300–600 band
   - Turnaround under 5 business days
   - Communication style
4. Pick the strongest fit, paste-trigger to Peter: *"Engaged [firm], turnaround [date]"*
5. Code (or Peter) updates `STATUS.md` Open Loop #10 → "Engaged [firm]"
6. When the lawyer's notes come back, Cowork integrates the changes into `eonia-therapist-engagement-termsheet.md` → mark term sheet "Reviewed by [firm], [date]"

**Important:** Cowork is the messenger and integrator. Peter is the signatory — he reads the lawyer's notes himself before signing anything.

**Timebox:** 5 min send + 5 days wait + 30 min integration after notes return.

---

## Sequencing — what unblocks what

```
Phase A (Peter, parallel, ~6 min):
  P1 Cloudflare password rotated
  P2 2FA enabled
  P3 Eonia CMS one-liner sent
  P5 GitHub repo path chosen

Phase B (Cowork, sequential, ~15 min):
  Task 1 → GitHub repo created
  Task 2 → commit + push (gated on Phase A complete)

Phase C (Cowork, parallel with B once code is in GitHub, ~25 min):
  Task 3 → Cloudflare Pages connect
  Task 4 → custom domain
  Task 5 → GoDaddy nameserver swap (24h propagation in background)

Phase D (Cowork, parallel with anything, ~70 min total):
  Task 6 → Calendly setup
  Task 7 → GoDaddy email forward (capture MX before Task 5 nameserver swap)
  Task 8 → LinkedIn company page execute
  Task 9 → Apollo enrichment
  Task 10 → Lawyer outreach (5 min send, then async)

Phase E (Peter, varies):
  P4 Sign lawyer-reviewed term sheet when notes return
```

**Critical ordering rule:** Task 7 (email forward) must capture MX records BEFORE Task 5 (nameserver swap) propagates, or email breaks.

---

## What Cowork must NOT do

- **Do NOT rotate the Cloudflare password.** Peter only.
- **Do NOT enable 2FA on Peter's behalf.** Authenticator seed is on his device.
- **Do NOT sign anything legally binding** — even if Peter is busy.
- **Do NOT push to any GitHub remote other than `kritsotakis/metis-cortex`** (or the username Peter confirms).
- **Do NOT commit `.env`, `.env.local`, secrets, or API tokens** to the repo. Pre-push diff check enforces this.
- **Do NOT send any cold emails** until DSK pilot Day 28 data is real.
- **Do NOT post on LinkedIn** until DSK pilot Day 28 data is real.
- **Do NOT make any pricing changes** to the homepage or pricing pages. Brand-spec locked.
- **Do NOT make architectural decisions** (e.g. "let's use Vercel instead", "let's add Tailwind plugin X"). Surface to Peter.

---

## STATUS file update on completion

After each task lands, update `~/Desktop/metis-cortex/STATUS.md`:

- Move the task from **In Flight** to **Done This Sprint**
- Close the corresponding **Open Loop**
- Add a Decision Log entry if anything material was decided
- Mirror to `~/.claude/memory/metis-cortex-status.md`:
  ```bash
  cp ~/Desktop/metis-cortex/STATUS.md ~/.claude/memory/metis-cortex-status.md
  ```

---

## Confirmation Cowork posts back

After each task:

```
✅ Task X — <one line of what landed>
   Verified: <one curl/check that proves it works>
   STATUS: updated, mirrored to memory
```

After all tasks:

```
✅ Site live at https://metiscortex.au
✅ Calendly demo URL: <URL>
✅ hello@metiscortex.au → peter@kritsotakis.com.au forward live
✅ LinkedIn company page: <URL>
✅ Apollo prospect list at 50 verified rows
✅ Lawyer engaged: <firm>, term sheet review turnaround <date>
✅ STATUS reflects everything
```

Then Peter has only Phase E (sign the lawyer-reviewed term sheet) and Phase F (run the DSK pilot through Day 28) left.
