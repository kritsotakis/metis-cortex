# Cowork brief — Metis Cortex Infrastructure Setup

> **Owner:** Peter Kritsotakis
> **Assigned:** Cowork
> **Companion brief:** `COWORK-CLOUDFLARE-MIGRATION.md` — runs in parallel, no conflicts
> **Authored by:** Claude Code, 2026-05-06

---

## Goal in one sentence

Stand up the supporting infrastructure that lets Metis Cortex actually convert a demo (Calendly + mailbox), positions it for warm-intro selling on LinkedIn, and unblocks the Eonia install + therapist hire decisions — so when the site goes live, the operational pieces don't lag behind it.

## Six tasks, parallel tracks, total ~3 hours of Cowork time + ~45 min of Peter time

| Task | Track | Cowork time | Peter time | Blocks ship? |
|---|---|---|---|---|
| 1. Calendly demo URL | A — Infra | 15 min | 5 min review | YES — placeholder in code |
| 2. `hello@metiscortex.au` mailbox | A — Infra | 10 min | 5 min auth | YES — for any demo follow-up |
| 3. LinkedIn company page | B — Presence | 20 min prep | 30 min execute | NO — but blocks warm-intro selling |
| 4. DSK photo curation | B — Presence | 30 min triage | — | NO — site can ship without |
| 5. Eonia CMS confirmation | C — Pilot prep | 10 min | 5 min ask | Blocks Eonia install only |
| 6. Lawyer referral research | C — Pilot prep | 45 min | — | Blocks therapist hire only |

Run tracks A and B in parallel, hold C until tracks A and B done.

---

## Task 1 — Calendly demo URL

**Why:** `CTAButton.tsx` line 5 currently hardcodes `https://calendly.com/peter-kritsotakis/metis-cortex-demo` as a placeholder. Until that's a real URL, every CTA on the homepage is broken.

**Confirm with Peter first:**
- Does he have an existing Calendly account on `peter@kritsotakis.com.au`? If yes, use it. If no, confirm that account email and password manager entry before creating new.

**Steps (Cowork executes after Peter confirms account access):**

1. Login to Calendly
2. Create new Event Type: **"Metis Cortex Demo — 10 min"**
   - Duration: 10 min
   - Availability: Mon–Fri, 09:00–18:00 AEST (Australia/Sydney timezone)
   - Calendar sync: Peter's primary Google Calendar (peter@kritsotakis.com.au)
   - Buffer: 15 min before/after
   - Cap per day: 4 demos max (don't burn Peter's day on demos that don't convert)
   - Rolling availability window: 14 days out
3. Add 2 pre-call questions (visible to Peter before the call, helps qualify):
   - **"What kind of service business do you run?"** (required, free text)
   - **"What's your current missed-call problem in one sentence?"** (required, free text)
4. Set confirmation email subject: *"Your Metis Cortex demo is booked."* — match the brand voice.
5. Set reminder: 1 hour before via SMS to caller (if they provide phone) and email
6. Get the public URL — likely `https://calendly.com/peter-kritsotakis/metis-cortex-demo` if available, else whatever Calendly assigns
7. Test: book a demo yourself (use a throwaway email), confirm:
   - Email confirmation lands
   - Event appears in Peter's Google Calendar
   - Pre-call questions captured
   - Reminder schedules

**Deliverable:** Paste the live Calendly URL back to Peter + Claude Code. Claude Code updates `CTAButton.tsx` line 5 in the same commit batch as the Manus brand integration.

**Timebox:** 15 min Cowork + 5 min Peter to test the flow.

---

## Task 2 — `hello@metiscortex.au` mailbox

**Why:** When a prospect emails after a demo, "peter@kritsotakis.com.au" looks personal/scrappy. "hello@metiscortex.au" looks like a real business. Cheap credibility upgrade.

**Decision: GoDaddy email forwarding (free) vs. Google Workspace (~A$15/user/mo)**

For path-(i) boutique, **GoDaddy email forwarding is sufficient for v1**. Free, takes 5 min. Upgrade to Google Workspace later when:
- Peter wants outbound emails to come *from* `hello@metiscortex.au` (forwarding is inbound-only)
- He needs multiple mailboxes
- He needs Google Drive/Docs collaboration tied to the domain

**Steps (Cowork executes):**

1. Login to GoDaddy → My Products → `metiscortex.au` → **Email & Office**
2. **Email Forwarding** → Set up a forward
3. Create forwards:
   - `hello@metiscortex.au` → `peter@kritsotakis.com.au`
   - `peter@metiscortex.au` → `peter@kritsotakis.com.au`
4. **DNS verification:** GoDaddy adds MX records automatically when forwarding is enabled. Confirm MX records appear in DNS panel.
5. Test: send an email from a different account to `hello@metiscortex.au`, confirm it lands in `peter@kritsotakis.com.au` within 5 minutes.

**Note for the Cloudflare migration brief:** If `metiscortex.au` DNS is moved to Cloudflare (per Cloudflare brief Phase 2.2 Option A), the MX records must be migrated to Cloudflare's DNS panel manually. Cowork: when DNS migration happens, capture the MX records first, then re-add them in Cloudflare.

**Deliverable:** Confirmation email log + tell Peter the forward is live. Claude Code updates `Footer.tsx` line 26+ to add `hello@metiscortex.au` as the primary contact (currently shows `peter@kritsotakis.com.au`).

**Timebox:** 10 min Cowork + 5 min Peter for GoDaddy auth (if Cowork doesn't have access).

---

## Task 3 — LinkedIn company page

**Why:** Path-(i) selling is warm-intro via LinkedIn. Peter posts from his personal profile, but every post needs to tag a company page that prospects can click through to. Without a company page, the brand can't accumulate followers, can't run sponsored content, and looks unprofessional in DM signatures.

**Cowork prep (can do this without Peter's auth):**

Draft the page content. Save to `~/Desktop/metis-cortex/LINKEDIN-COMPANY-PAGE-COPY.md`:

```markdown
# Metis Cortex — LinkedIn Company Page Copy

**Page name:** Metis Cortex
**Tagline (max 120 chars):** Speed-to-Lead AI receptionists installed in 14 days. Sydney-built. Australian-owned.
**Industry:** Business Consulting and Services
**Company size:** 1–10 employees
**Headquarters:** Sydney, NSW, Australia
**Founded:** 2026
**Specialties:** AI, Speed-to-Lead, Customer Service Automation, AI Receptionist, Service Business Operations

**About section (max 2,000 chars):**
Metis Cortex installs AI receptionists on Australian service businesses.

We pick up every missed call within 60 seconds, qualify the lead, and book the appointment — so service businesses stop leaking enquiries to voicemail.

Metis Cortex, our flagship product, installs in 14 days. A$1,500 setup, A$600/month, month-to-month. If it doesn't book at least 5 extra appointments in month one, full refund.

Built and proven on our own cleaning business (DSK Property Cleaning) before we ever sold it externally.

Sydney-built. Australian-owned. Operator-to-operator.

For service businesses doing $50K–$500K/month with phone-driven leads — cleaners, tradies, real estate agents, dental practices, aesthetic clinics, allied health.

Book a 10-minute demo: [Calendly URL once Task 1 complete]

**Logo:** Use the placeholder simple "M + bronze dot" icon at 300×300 PNG until Manus brand bundle delivers. Cowork: render `~/Desktop/metis-cortex/src/app/icon.svg` to PNG at 300×300 using `npx svgexport src/app/icon.svg /tmp/linkedin-logo.png 300:300` — provide the PNG to Peter.

**Cover banner (1128×191):** Hold until Manus delivers `02_linkedin_company_cover_1128x191.png`. Until then, leave blank or use a flat navy `#0e1e2e` colour fill.
```

**Then Peter executes (browser-only, ~30 min):**

1. linkedin.com → top nav "Work" → **Create a Company Page** → **Small business**
2. Paste the content above into the relevant fields
3. Upload the placeholder logo (from `/tmp/linkedin-logo.png`)
4. Set Peter as **Admin** under Page Settings
5. Publish the page
6. Add "Metis Cortex" as a current position to Peter's personal profile (links the two)
7. Send the page URL back to Cowork

**Deliverable:** LinkedIn company page URL.

**Timebox:** 20 min Cowork prep + 30 min Peter execute.

---

## Task 4 — DSK photo curation

**Why:** The site's Hero and DSK Case Study sections will look much stronger with real DSK photos than with stock or AI-generated imagery. Peter has 20K Jobber records — there are good photos in there.

**Cowork's role: define the criteria + help triage. Peter's role: dig and pick.**

**Photo criteria — Cowork tells Peter to look for these specific shots:**

| Slot | Use | Spec | Where to look |
|---|---|---|---|
| 1 | **Hero background** (subtle, behind navy gradient) | Wide horizontal, 2400×1200 minimum, action shot of cleaner mid-job at a Sydney property exterior — ideally with DSK van visible | Recent jobs (last 6 months), Jobber attachments, Peter's iPhone Photos |
| 2 | **DSK Case Study primary photo** | Square or 4:3, 1600×1200, the DSK team with a finished property in the background OR a striking before/after pair | Same |
| 3 | **Metis Cortex / "What's Included" decorative** | Anything showing real professional cleaning equipment, vans, or the team in uniform | Same |
| 4 | **About / Founder strip (Phase 2)** | Wide shot of Peter at a DSK job site, candid not posed | Personal photo library |
| 5 | **Optional second case study slot** | 4:3, a different property type (strata building exterior or pre-sale completed home) | Same |

**Filtering rules (Cowork enforces, Peter picks):**

- **No customer faces** — privacy. If a customer is in frame, mask or skip.
- **No license plate close-ups** — privacy / legal.
- **No interior shots of identifiable luxury homes** — security risk for the customer.
- **High resolution only** — minimum 1600px on the long edge.
- **JPEG, well-lit, not blurry** — if it looks like an iPhone snap from a tradie's shoulder, skip it.
- **Recent enough that the DSK branding is current** — last 12 months only.

**Steps:**

1. Cowork creates `~/Desktop/metis-cortex/public/photos/dsk/` directory
2. Cowork creates a triage doc `PHOTO-CURATION-CHECKLIST.md` in that folder with the table above
3. Peter spends 30 min digging through Jobber + Photos.app and drops candidates in the folder, named `01-hero-candidate-1.jpg`, `01-hero-candidate-2.jpg`, etc.
4. Once 8–12 candidates are dropped, Cowork triages — picks the top 1 per slot (5 final photos), moves them to `public/photos/dsk/final/`, marks the rest as candidates for future use.
5. Cowork captures alt text for each picked photo (1 sentence each, descriptive for accessibility).

**Deliverable:** 5 picked photos in `public/photos/dsk/final/` + alt text in a JSON file.

**Timebox:** 30 min Cowork triage + 30 min Peter dig.

---

## Task 5 — Eonia CMS confirmation

**Why:** The Eonia install pack (`eonia-pilot-pack.md`) specifies a webhook to Eonia's clinical management system. The webhook spec varies by system (Cliniko, Pabau, Halaxy each have different APIs). Without this confirmation, Day 1 of the Eonia install can't start.

**Steps:**

1. Cowork drafts a 1-line message for Peter to send to the Eonia team:
   > "Quick admin question — what clinical management system are we using? (Cliniko, Pabau, Halaxy, or something else.) Need to confirm for an integration we're scoping."
2. Peter sends, gets the answer
3. Cowork captures the answer + asks the second question:
   > "Great. Who has admin access to generate an API key when we need one?"
4. Cowork updates `eonia-pilot-pack.md` Phase 2/4 sections with the actual CMS name + sets a TODO for API key once therapist install Day 1 starts
5. Cowork updates `~/.claude/memory/active-projects.md` Eonia install row to reflect CMS confirmed

**Deliverable:** CMS name confirmed in writing in the pilot pack + active-projects.md.

**Timebox:** 10 min Cowork + 5 min Peter to send/relay the message.

---

## Task 6 — Lawyer referral research for therapist term sheet

**Why:** The therapist term sheet (`eonia-therapist-engagement-termsheet.md`) needs lawyer review before signing. Peter doesn't have a relationship with a small-business HR lawyer in Sydney. Cowork's job: find 3 candidates, get quotes, hand off to Peter for the call.

**Selection criteria:**

- **Sydney-based** (NSW law applies, time zone overlap matters)
- **Specialises in small-business employment law** — ideally with experience in:
  - Beauty Industry Award 2020
  - Casual employment + profit-share bonus arrangements
  - Sham contracting risk assessment
  - Corporate trustee signing authority (Pty Ltd as trustee for trust)
- **Fixed-fee for 1-hour review** preferred over hourly billing
- **Budget: A$300–600 for a 1-hour review** including written notes
- **Reachable by phone or email within 1 business day**

**Sources to check:**

1. **Lawyer referral services:**
   - Law Society of NSW Find A Lawyer: https://www.lawsociety.com.au/findalawyer
   - LegalVision (online, fixed-fee) — usually around A$400–600 for review
   - LawTap (fixed-fee specialist marketplace)
2. **Specialist small-business HR firms in Sydney:**
   - Search: "small business employment lawyer Sydney"
   - Filter by reviews, response time, fee transparency
3. **Existing networks:**
   - Ask Peter: does his accountant have a lawyer referral? (Most accountants do.)
   - Ask Peter: any business owner in his network used a small-business HR lawyer?

**Steps:**

1. Cowork researches and produces a shortlist of **3 lawyers/firms** with:
   - Name, firm, contact (email + phone)
   - Quote for 1-hour review of a casual-employee + profit-share term sheet
   - Specialisation match (Beauty Industry Award? Profit-share? Sham contracting?)
   - Earliest available date for the call
   - Why this one made the shortlist (1 sentence)
2. Cowork drafts a 4-line email Peter can send to all 3 in parallel:
   > Subject: Term sheet review — small business hire, NSW
   >
   > Hi [name],
   >
   > I'm a Sydney-based business owner about to hire a beauty therapist for my aesthetic clinic on a casual + profit-share basis. I have a draft term sheet I'd like reviewed for sham-contracting risk, Award classification, and the profit-share clause specifically.
   >
   > Can you confirm fixed fee for 1-hour review with written notes, and the earliest you could turn it around?
   >
   > Peter Kritsotakis
3. Peter sends to all 3, picks based on response speed + quote
4. Cowork updates the active-projects.md row when one is engaged

**Deliverable:** Shortlist doc at `~/Desktop/metis-cortex/THERAPIST-TERMSHEET-LAWYER-SHORTLIST.md` with 3 candidates + the email template.

**Timebox:** 45 min Cowork research + 10 min Peter send.

---

## What Cowork must NOT do

- **Do NOT touch any code in `~/Desktop/metis-cortex/src/`** — that's Claude Code's lane. Only `public/photos/dsk/` and the new doc files in repo root are Cowork's scope.
- **Do NOT push to GitHub** — Claude Code coordinates the push schedule via the Cloudflare migration brief.
- **Do NOT create LinkedIn personal posts yet** — the company page exists first, then Peter posts strategically. Don't auto-post.
- **Do NOT engage lawyers, sign anything, or make commitments on Peter's behalf** — Cowork's job is research + shortlist + draft email. Peter sends and decides.
- **Do NOT register any additional domains** without Peter's written approval. The defensive `.com` registration was discussed but not authorised — leave it.
- **Do NOT migrate DNS to Cloudflare in this brief** — that's the Cloudflare migration brief's Phase 2. Coordinate with that brief, don't pre-empt it.
- **Do NOT mark any task "Final" until Peter explicitly confirms** the deliverable works (e.g. test demo booking actually lands in his calendar; test email actually forwards).

## Out of scope for v1 (defer)

- Twitter/X profile (defer until 1 paying client)
- YouTube channel (defer until first product demo video script exists)
- Google Business Profile listing (defer — Sydney-only HQ doesn't need GBP for the boutique selling motion)
- Facebook / Instagram (wrong channels for B2B service-business sales)
- `metiscortex.com` defensive registration (do this when convenient — A$15 task, low priority)
- Newsletter signup (no newsletter content strategy yet — defer to Phase 2)

## Sequencing — what unblocks what

```
Phase A (parallel):
  Task 1 (Calendly) ──┐
  Task 2 (Mailbox) ───┼──→ Site launch unblocks
  Task 3 (LinkedIn) ──┘    (Cloudflare migration handles the deploy)

Phase B (after A):
  Task 4 (DSK photos) ──→ Site visual polish (post-launch ok)
  Task 5 (Eonia CMS) ──→ Eonia install Day 1 unblocks
  Task 6 (Lawyer)    ──→ Therapist hire unblocks
```

Tasks 1, 2, 3 are the v1 ship-supporting infrastructure. Tasks 4, 5, 6 are pilot/install prep.

## Total timebox

| Phase | Cowork | Peter |
|---|---|---|
| Phase A (Tasks 1–3) | 45 min | 40 min |
| Phase B (Tasks 4–6) | 1h 25min | 35 min |
| **Total** | **~2h 10min** | **~1h 15min** |

If total exceeds 3 hours of Cowork time, stop and surface why.

## Final confirmation Cowork posts back when each task lands

```
✅ Task 1 — Calendly URL: <URL>
✅ Task 2 — hello@metiscortex.au forwards to peter@kritsotakis.com.au, MX records: <list>
✅ Task 3 — LinkedIn company page: <URL>, Peter set as admin
✅ Task 4 — 5 DSK photos in public/photos/dsk/final/, alt text in alts.json
✅ Task 5 — Eonia uses <CMS name>, API admin: <person>
✅ Task 6 — Lawyer shortlist at THERAPIST-TERMSHEET-LAWYER-SHORTLIST.md, email template ready
```

Then update `~/.claude/memory/active-projects.md` Metis Cortex / Eonia rows to reflect each completion.

And append to `~/.claude/memory/recent-activity.md` a new dated entry per the session-end protocol.
