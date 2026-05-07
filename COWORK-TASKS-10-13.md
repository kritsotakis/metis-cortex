# Cowork brief — Tasks 10–13 (productive work during holding pattern)

> **For:** Cowork
> **Authored by:** Claude Code, 2026-05-06 13:50
> **Companion briefs:** `COWORK-CLOUDFLARE-MIGRATION.md`, `COWORK-INFRASTRUCTURE-SETUP.md`, `COWORK-STATUS-SYNC-2026-05-06.md`

---

## Context — what's changed since the last status sync

**1. Cloudflare zones added (by another agent / Peter directly).** Cloudflare account now has 2 zones: `exitcode.trade` + `metiscortex.au`. DSK stays on GoDaddy. The Cloudflare side of the migration is partially set up — when you eventually execute Phase 2 of `COWORK-CLOUDFLARE-MIGRATION.md`, you do NOT need to "Add a Site" — go straight to adding `metiscortex.au` as a custom domain in the Pages project.

**2. Vercel A records will appear in Cloudflare DNS** for `metiscortex.au` — these are stale from a May-4 Vercel deployment and will be replaced automatically when you add the custom domain in Pages. No manual DNS cleanup needed before migration.

**3. SSL mode for `metiscortex.au` should be Full Strict** (Cloudflare manages SSL end-to-end with Pages). Don't follow the earlier "Full not Full Strict" advice — that was given assuming Vercel hosting. We're going Cloudflare Pages.

**4. Eonia domain correction:** the correct domain is `eonia.au`, NOT `eoniaclinic.com.au`. Code has updated `~/.claude/CLAUDE.md` and `~/.claude/memory/businesses.md`. Update your own session memory accordingly. Use `eonia.au` in all future references.

**5. Standing gates still active:**
- Cloudflare Phase 0 (password rotated + 2FA + GitHub repo) — needed before Phase 1
- Filesystem access to `~/Desktop/metis-cortex` — Code keeps syncing your outputs
- Eonia CMS, lawyer engagement, Calendly, GoDaddy email — Peter auth required

---

## Four new tasks — all are draft-only, no auth/filesystem needed

These ship deliverables you can produce in your current state. Each is timeboxed and serves a real downstream need.

| Task | Why it matters | Cowork time |
|---|---|---|
| 10. Demo follow-up email template | The moment a prospect books via Calendly, every minute without a confirmation email signals amateur-hour. Needs to exist before Calendly goes live. | 30 min |
| 11. Customer onboarding email sequence (4 emails) | Once first paying client signs, they receive Day 1 / Day 3 / Day 7 / Day 14 emails. These exist or they don't — no halfway. | 90 min |
| 12. First LinkedIn post draft (case-study template) | Lands the moment DSK pilot Day 28 data is real. Pre-drafted with placeholders so Peter's only edit is filling in real numbers. | 30 min |
| 13. DSK pricing grid extraction | The Retell agent prompt (Phase 3 of DSK pilot) requires DSK's actual pricing for Zoe to quote correctly. Extract from existing DSK pages so it's ready when install Day 4 hits. | 60 min |

**Total: ~3.5 hours of Cowork time. All deliverable as paste-ready docs in your output folder, then Code syncs into the repo.**

---

## Task 10 — Demo follow-up email template

**Why:** When a prospect books via Calendly, three things happen automatically (Calendly's defaults): they get a calendar invite, an event reminder 1 hour before, and a confirmation email at the moment of booking. We want a *custom* confirmation email instead of Calendly's default — branded, specific, primes them for the demo. This is set up inside Calendly under Notifications → Confirmation email → Customise.

**Deliverable:** A single template at `metis-cortex-calendly-confirmation-email.md` covering:

1. **Subject line** — must read in inbox preview. Suggested direction: *"Your Metis Cortex demo — [Day], [Time]"*
2. **Preview text** — 1 line, 90 chars max, gives the recipient a reason to open
3. **Email body** — short (under 200 words). Structure:
   - Confirmation of booking + add-to-calendar link (Calendly auto-injects this)
   - 2 sentences on what to expect from the 10-min call (Peter walks them through Frontline live, shows Zoe answering a real test call, talks pricing + guarantee)
   - **One specific pre-call ask:** "Have your current weekly missed-call number roughly in mind — even a guess is fine. We'll work backward from that to whether Frontline makes sense for you."
   - Reschedule link (Calendly auto-injects)
   - Footer: Peter Kritsotakis / Metis Cortex / metiscortex.au
4. **Tone:** Operator-to-operator. No salesy language. No "I'm so excited." Match the brand voice on the homepage.

**Plus a no-show follow-up template** (sends 24h after a missed demo, Calendly Notifications → Cancellation/no-show notification):

- Subject: *"Missed you — happy to reschedule"*
- Body: 4 lines. Acknowledge they didn't make it (no judgement), one-line reminder of what Frontline is, reschedule link, sign-off.

**Save:** `~/Library/Application Support/Claude/...your-outputs.../metis-cortex-calendly-confirmation-email.md`. Code will sync into repo as `CALENDLY-CONFIRMATION-EMAIL.md`.

**Timebox:** 30 min.

---

## Task 11 — Customer onboarding email sequence (4 emails)

**Why:** When the first paying client signs (Day 1 of their 14-day install), they enter a sequence that keeps them informed without overloading you. Predictable comms = high CSAT. Confused, silent installs = early churn.

**Deliverable:** 4 separate email templates, sent on a schedule from the moment payment processes:

| # | Send when | Subject | Purpose |
|---|---|---|---|
| 1 | Day 1 — instant after payment | *"Welcome to Metis Cortex — what happens next"* | Confirm payment, set expectation for the 14-day install, list what we'll need from them in week 1 (their existing phone number, business hours, top 3 service types, current CRM if any), introduce Peter as their point of contact |
| 2 | Day 3 | *"Building Zoe for [their business]"* | Update on progress — Retell agent configured, Twilio number provisioned, voice prompt drafted. Include 1 specific item they need to action this week (review the voice prompt draft, send a sample call recording for tone, etc.) |
| 3 | Day 7 — midpoint | *"Halfway there — test calls this week"* | Progress check, run them through what test calls will look like, what they should listen for, what's normal vs concerning. Reinforce the 5-extra-bookings refund guarantee |
| 4 | Day 14 — go-live | *"Frontline is live for [their business]"* | Confirmation that Zoe is now answering their phone, what to do in the first 24h, how to escalate, when they'll receive the month-1 metrics report |

**For each email:**

- Subject + preview text + 200-word max body
- Tone: same operator-to-operator brand voice as the rest
- One clear action per email — never zero, never two
- Include a clear "Reply to this email if anything's off" line at the bottom of every one (replies route to peter@kritsotakis.com.au or hello@metiscortex.au once that's live)

**Out of scope for v1:**

- Branded HTML templates (plain text or minimal HTML — no email-design rabbit hole)
- Drip platform integration (these go into whatever sends the emails — Brevo, Resend, MailerLite — pick later. For now, deliver the templates.)
- A/B subject line testing (no sample size for that yet)

**Save:** 4 files at `metis-cortex-onboarding-email-{1,2,3,4}.md` in your outputs. Code syncs into repo as `ONBOARDING-EMAIL-SEQUENCE.md` (combined doc) when filesystem access is available.

**Timebox:** 90 min total (~22 min per email).

---

## Task 12 — First LinkedIn post draft (DSK case study template)

**Why:** The first post the Metis Cortex LinkedIn company page makes shapes the algorithm's read of the brand for the next 12 months. It needs to be the DSK case study — not a "we're launching" post. We pre-draft it now with placeholders, so the moment Day 28 data lands, Peter does a 5-min find-and-replace and posts.

**Deliverable:** `metis-cortex-linkedin-first-post-template.md` with:

1. **The post itself** — under 1,300 chars (LinkedIn's truncate point). Structure:
   - Hook in the first 2 lines (the truncate point) — must be a number or a specific tension. Example direction: *"14 days ago I installed an AI receptionist on my own cleaning business. Here's what happened to the missed calls."*
   - Before/after snapshot — 4 numbers max, formatted clean
   - One sentence on the surprising thing (a specific moment from the pilot — a recovered after-hours call that was a real $X job, etc. — placeholder for now)
   - The brand pitch — single line, no hard sell, ends with "10-min demo in the comments"
   - Hashtags: 3 max, all small-business / Australia / AI relevant. Big-list spam tags hurt reach.

2. **Three subject-line variants of the hook** — the first 2 lines are 80% of the work. Give Peter 3 options to A/B in his head before posting.

3. **The reply-comment-with-Calendly-link template** — LinkedIn algorithm penalises external links in the post body but not in comments. The first comment is where the demo link goes. Pre-drafted as a 2-line follow-up Peter posts immediately after the main post lands.

4. **Engagement-prompt suggestions** — Peter messages 5–10 of the closest people he invited to follow the page (Tier C from `LINKEDIN-FIRST-100-OUTREACH.md`) within 30 min of posting, asking them to leave a substantive comment (not just a like). Algorithm-juicing is allowed when comments are real. Give Peter a 3-line template message for that ask.

**Save:** `metis-cortex-linkedin-first-post-template.md` in outputs. Synced into repo as `LINKEDIN-FIRST-POST-DRAFT.md`.

**Timebox:** 30 min.

---

## Task 13 — DSK pricing grid extraction

**Why:** The Retell voice agent (Zoe) needs DSK's actual pricing to quote correctly during inbound calls. Phase 3 of the DSK pilot pack lists this as a Day 4-5 deliverable — but the data already exists across DSK's existing site pages. Extract it now so it's ready in clean tabular form when the Retell prompt is being filled in.

**Sources:**

- DSK pricing pages: `dsk.au/pre-sale/`, `dsk.au/strata/`, `dsk.au/services/`, `dsk.au/offers/`
- DSK suburb pages (24 × 4 = 96 pages, all live) — pricing references appear in some
- DSK Mother's Day landing pages — current promotional pricing in `/mothers-day-999/` etc.
- Recent active-projects.md updates capture the pricing bump (Interior+Exterior $1,650 → $2,500)

**Deliverable:** `metis-cortex-dsk-pricing-grid.md` containing:

1. **Service × Property size matrix** — for each service type (pre-sale clean, end-of-lease, builders clean, strata maintenance, exterior-only, kitchen deep clean, bathroom deep clean), a price range by property size (1-bed unit, 2-bed unit, 3-bed townhouse, 4-bed house, 5+ bed home, strata block tier-1 / tier-2 / tier-3).
2. **Suburb modifier** — if pricing differs by suburb (which it likely does for some — Mosman vs Bondi vs Newtown), capture the modifier.
3. **Add-on pricing** — oven clean, carpet clean, window interior, garage, gardening (since gardening is removed from pre-sale, capture the standalone price), etc.
4. **What Zoe should NEVER quote** — anything outside the grid, anything unusual (post-fire, hoarding situations, biohazard) — flagged for Peter callback.
5. **Format:** Both human-readable Markdown table AND a Retell-prompt-ready JSON or YAML block so it can be dropped straight into the agent's knowledge base.

**Filtering rules:**

- Pull only **current** pricing — anything Mother's Day-tagged (MD2026 markers per active-projects.md) expires May 11; don't include in the permanent grid
- Cross-check pricing across multiple pages — flag any inconsistencies for Peter to resolve before this becomes the source of truth
- Strata pricing was reframed to "12-month service agreement with locked pricing" per the strata contract pivot — reflect that

**Save:** `metis-cortex-dsk-pricing-grid.md`. Code syncs into repo as `DSK-PRICING-GRID.md`.

**Timebox:** 60 min.

---

## Sequencing

```
All four tasks parallelise — no inter-dependencies.
Recommended Cowork order: Task 12 (quick) → Task 10 (quick) → Task 13 (research-heavy) → Task 11 (longest, save for last)
```

You can start any of them right now. None require auth. None require filesystem access.

---

## What Cowork must NOT do

- **No emails actually sent.** All four tasks are draft-only. Peter sends manually after review.
- **No LinkedIn posts published.** Task 12 is draft-only. Peter posts when DSK data lands.
- **No code edits.** Code's lane.
- **No git pushes.** Coordinated via Cloudflare brief.
- **Don't backfill Tasks 7/8/9** — they're already synced into repo. Reference them but don't redo them.
- **Don't speculate about Vercel** — we're Cloudflare Pages, decided. Move on.

---

## Confirmation Cowork posts back

```
✅ Task 10 — Calendly confirmation email + no-show follow-up at metis-cortex-calendly-confirmation-email.md
✅ Task 11 — Onboarding email sequence (Day 1/3/7/14) at metis-cortex-onboarding-email-{1,2,3,4}.md
✅ Task 12 — LinkedIn first-post template + 3 hook variants + comment+message scripts at metis-cortex-linkedin-first-post-template.md
✅ Task 13 — DSK pricing grid + Retell-ready JSON block at metis-cortex-dsk-pricing-grid.md
```

Then Code syncs into the repo and updates memory.
