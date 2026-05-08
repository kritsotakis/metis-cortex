# How Metis Cortex Works

> **Plain-English explanation of the business model, customer journey, and unit economics.**
> Written for: Peter's own mental model, family/partners asking "what is this thing", lawyer/accountant context, and future hires.
> Last updated: 2026-05-07

---

## In one sentence

Metis Cortex configures proven AI tools (Retell + GoHighLevel + Twilio) on Australian service businesses' phones in 14 days, charges A$1,500 setup + A$600/month, and refunds the setup fee if it doesn't book the customer at least 5 extra appointments in their first month.

The moat is being a Sydney operator who runs four service businesses himself (DSK Property Cleaning, Eonia Aesthetic Clinic, HydraLab, and Exit Code), so the operator-to-operator credibility transfer is real — not consultancy, not theory.

> **Phase 2 product expansion (locked 2026-05-08):** After customer-discovery with Belle Property Manly identified "finding buyers" as the #1 real estate pain — not "answering questions" — a higher-ARPU upsell layer was added: **Frontline Outbound** (AI database activation). See `FRONTLINE-OUTBOUND-SPEC.md` for the full spec. The three-tier stack is summarised in the "Three-tier product stack" section below.

---

## Three-tier product stack

The Metis Cortex product is now structured as three SKUs, sold separately or as a bundle. Customers can start at Tier 1 (Frontline base) and upgrade to Tier 2 + 3 once value is proven.

| Tier | Product | What it does | Pricing | Customer pain |
|---|---|---|---|---|
| **Tier 1** | **Frontline base** | Inbound AI receptionist — answers calls, qualifies leads, books appointments | A$1,500 setup + A$600/mo | "We miss too many calls" |
| **Tier 2** | **Frontline Knowledge** | Per-asset Q&A on inbound calls — Zoe knows your specific listings / properties / customers in detail | +A$300/asset/mo | "Our staff waste hours answering basic questions" |
| **Tier 3** | **Frontline Outbound** | AI database activation — Zoe makes outbound matching calls against your existing customer/inquirer database based on configurable triggers | A$1,500–5,000/mo per business depending on volume | "We can't generate enough new bookings / sales" |

**Pricing example — boutique real estate agency with 5 active listings + 3,000 buyer database:**

- Tier 1 base: A$600/mo
- Tier 2 (5 listings × A$300): A$1,500/mo
- Tier 3 outbound buyer activation: A$3,000/mo
- **Total: A$5,100/mo per agency**

10 such agencies on the full bundle = A$51,000/mo MRR. That's a real business in one vertical alone.

**Pricing example — mid-size dental practice (2,500 patients):**

- Tier 1 base: A$600/mo
- Tier 2 not applicable (no per-asset knowledge needed)
- Tier 3 outbound recall + insurance year-end activation: A$1,500/mo
- **Total: A$2,100/mo per practice**

ROI math for the dental example: 500 additional appointments/year × A$250 avg = A$125,000 recovered revenue against A$25,200 annual cost. ~5× ROI.

**Pricing example — DSK-style cleaning business:**

- Tier 1 base: A$600/mo
- Tier 2 not applicable
- Tier 3 outbound re-engagement of dormant one-off customers: A$800–1,200/mo
- **Total: A$1,400–1,800/mo per business**

---

## Why three tiers, not one

Three observations from customer-discovery work:

1. **Customer pain isn't uniform.** Belle Manly's pain is "finding buyers" (Tier 3). A clinic owner's pain is "missed calls" (Tier 1). A real estate office manager's pain is "agents wasting time on Q&A" (Tier 2). Sell what they actually need, not a one-size-fits-all bundle.
2. **Tier 1 is the wedge — Tier 3 is the engine.** Tier 1 gets you in the door at A$600/mo, low risk, easy to demo, easy to install. Once installed and trusted, Tier 3 is where the business owner actually pays — because Tier 3 generates revenue, not saves cost.
3. **Pricing scales with value.** Tier 1 is defensive (cost reduction) so willingness-to-pay is capped. Tier 3 is offensive (revenue generation) so willingness-to-pay scales with the customer's revenue uplift. A real estate agency that converts ONE extra sale per quarter from Zoe-sourced calls (A$30K–80K commission) doesn't blink at A$3K/mo.

---

## The customer journey, end to end

### 1. Lead arrives (3 realistic sources)

- **Warm intro** — someone in the founder's LinkedIn network DMs about a missed-call problem
- **LinkedIn case study post** — DSK pilot results land on the Metis Cortex company page; a tradie or clinic owner comments or DMs
- **Cold email reply** — one of the 50 Sydney prospects in the prospect list replies "interested, send more"

For a path-(i) leveraged-boutique business, expect **3–5 demos per week** at steady state. Not 30. This is a craft business, not a funnel business.

### 2. Demo gets booked via Calendly (10 minutes)

Prospect picks a slot, gets a custom confirmation email, arrives at the call.

The demo isn't a slide pitch. The founder dials a real Twilio test number and **Zoe** (the AI receptionist persona) answers live while the prospect listens. She qualifies a fake call ("I need a pre-sale clean for a 4-bed in Mosman"), books a slot, sends an SMS confirmation. The 10 minutes break down:

- 4 min — actual product working live on the phone
- 4 min — what it costs, how the install works, the refund guarantee
- 2 min — questions

Roughly **30–50% of demos close** at this stage. The prospect just heard the product working, so there's no "but does it actually work?" doubt to overcome.

### 3. Prospect pays via Stripe

A$1,500 setup + A$600/month recurring. They put a card in. Auto-charges monthly going forward. Onboarding email 1 fires immediately.

### 4. The 14-day install (the actual work)

Day-by-day inside an install:

| Day | Phase | What happens |
|---|---|---|
| 1–3 | Provisioning | Twilio Australian local number provisioned; GoHighLevel sub-account spun up; client's calendar synced |
| 4–5 | Voice prompt build | Zoe's voice prompt written with the client's actual services, pricing, escalation rules — the most custom part of every install |
| 6–7 | CRM connection | Zoe connected to the client's CRM (Jobber / ServiceM8 / Cliniko / Pabau) so bookings flow back automatically |
| 8–10 | Internal QA | 5 internal test calls covering normal, urgent, reschedule, complaint, and after-hours scenarios |
| 11–12 | Soft launch | Client's existing number forwards to Zoe ONLY for missed calls / after-hours. Client stays in control during business hours |
| 13 | Shadow mode | 24-hour test: Zoe takes everything, founder monitors every call recording before bed |
| 14 | Go live | Zoe is the front line. Client's mobile is the human escalation when she can't handle something |

**Founder time per install: ~15–25 hours.** Not 80. Most of it is configuring tools, not coding.

### 5. Day 14 onwards — Frontline is live

The client's existing business number now forwards permanently to Zoe's Twilio number.

When the phone rings:
- **Zoe picks up within 30 seconds** (always, no lunch break, no after-hours gap)
- She qualifies, captures the address and details, books into the calendar
- The booking lands in the client's CRM automatically
- Client gets an SMS notification of the new booking

When something weird happens (angry customer, large quote, request for a service they don't offer):
- Zoe escalates → fires SMS to the client immediately with a transcript snippet
- Client calls back within their committed window

**Founder's ongoing role per client: ~2–3 hours/month** — checking call recordings, tuning the prompt when something doesn't work, occasional escalation triage.

### 6. Day 28 — first metrics report email

The client receives a single email with:

- Total inbound calls Zoe handled
- Conversion rate (enquiry → booked job)
- Estimated revenue from those bookings
- After-hours calls captured (the pure-recovery number)
- Comparison vs. baseline week before install

Three outcomes from there:

- **Default — auto-renew** at A$600/month, no action needed
- **Underdelivered** — refund the A$1,500 install fee per the guarantee, client cancels
- **Strong fit** — client asks "what else can you do?" and gets upsold to Reception or Handbook (Phase 2 products)

Realistic split at scale: ~70% renew, ~15% upsell, ~15% refund.

---

## Unit economics — per client, per month

| Line | Amount |
|---|---|
| Revenue (recurring) | A$600/month |
| Retell AI (voice usage) | -A$80 |
| GoHighLevel (CRM + workflow) | -A$148 |
| Twilio (number + call usage) | -A$15 |
| **Gross margin (recurring)** | **~A$357/month per client** |

Plus a **A$1,500 setup fee** as one-off (almost pure margin — costs ~A$50 in setup credits).

---

## What it looks like at scale

| Active clients | Monthly recurring revenue | Monthly costs | Monthly net | Founder hours/month on installs + maintenance |
|---|---|---|---|---|
| 5 | A$3,000 | A$1,215 | A$1,785 | ~30 hr |
| 10 | A$6,000 | A$2,430 | A$3,570 | ~45 hr |
| 20 | A$12,000 | A$4,860 | A$7,140 | ~80 hr (hire becomes necessary) |
| 30 | A$18,000 | A$7,290 | A$10,710 | ~120 hr (full team mode) |

Plus install fees on the way up — at 30 active clients the business has collected ~A$45,000 in install fees over the climb.

---

## The realistic 12-month shape

| Period | What happens |
|---|---|
| **Months 1–3** | Install Frontline on DSK + Eonia + HydraLab as case studies (free, own businesses). Zero external clients. Three vertical case studies in hand. |
| **Months 4–6** | First 3–5 paying external clients via warm intro from LinkedIn network. ~A$1,800–3,000 MRR + A$4,500–7,500 in install fees. |
| **Months 7–9** | 6–10 paying clients. ~A$3,600–6,000 MRR. Install bottleneck starts to bite — first hire decision. |
| **Months 10–12** | 10–15 paying clients. ~A$5,000–9,000 MRR. Year 1 done. |

**Year 1 revenue projection: A$50,000–80,000** (recurring + install fees combined). Real money. Not life-changing on its own — but compounds into Year 2 (A$120,000–180,000 projected) without any new strategy work, just continued execution.

Plus the **indirect uplift** on DSK + Eonia + HydraLab from running the same systems internally — probably another A$30,000–60,000 of recovered revenue across those three businesses, since they all stop leaking missed calls.

---

## What's actually hard about it

**Acquisition is the bottleneck.** Getting in front of qualified service-business owners is harder than the install or the tech. The first 5 clients are the hardest — once 3 case studies (DSK + Eonia + HydraLab + 3 paying) exist, referrals start working.

**Founder is the bottleneck on installs** until a hire happens. At 8–10 clients, doing every install solo + running the rest of the businesses isn't sustainable. First operations hire is needed around month 7–9.

**Churn risk** — every client who refunds is a public bad story if they're vocal. The refund guarantee protects legally but doesn't prevent reputation damage. First 5 clients especially — pick them carefully. Don't take a client whose missed-call number is too low; they won't see the lift and they'll churn loud.

---

## What's actually easy about it

**The tech is solved.** Retell + GoHighLevel + Twilio is a 2026 production-grade stack. Nothing being invented — proven tools being configured for businesses who don't know how to do it themselves.

**The pitch is concrete.** "Stop missing calls" + live demo + refund guarantee. No abstract "AI transformation" sales motion. Prospect hears it work or they don't.

**Founder is already the customer.** DSK is the dogfood. Every external install is a repeat of an internal install that already happened. Clients can't gaslight the founder about how their business works — he runs four of them.

---

## How this fits in the broader portfolio

| Business | Role | Path |
|---|---|---|
| **Exit Code** | Venture-scale software bet — anonymous brand, indicators + course, scalable digital product | path (ii) — chase scale |
| **Metis Cortex** | Leveraged boutique + AI ops layer for the other businesses | path (i) — leveraged boutique |
| **DSK** | Cash-cow service business + Frontline case study #1 | cash flow + reference customer |
| **Eonia** | Clinic + Frontline case study #2 (different vertical) | cash flow + reference customer |
| **HydraLab** | Chemistry R&D + custom AI workflow case study #3 | IP play + reference customer |

Two strategic bets at once (Exit Code = path ii, Metis Cortex = path i) doesn't overload one operator because they have very different rhythms — Exit Code is asynchronous content + product work, Metis Cortex is synchronous client work. They don't compete for the same hours of the day.

---

## The discipline rules that keep this on path (i) without sliding off

These were locked when the strategy was set on 2026-05-06. Holding to them prevents the boutique from accidentally becoming a consultancy:

1. **Charge for outcomes, not hours.** Productized service from day one. The moment "$200/hour" gets quoted once, it's a consultancy forever.
2. **Refuse bespoke beyond a tight feature set.** Customer asks for a custom Salesforce integration? "We install Frontline. We don't build custom integrations — here's a Zapier template." Saying no is what makes it productize-able later.
3. **Document obsessively.** Every install, every prompt, every workflow, every call recording (with consent). Building the dataset for a SaaS layer two years out, even if not productizing now.
4. **Build observability into every install.** Real-time dashboard showing calls answered, bookings made, recovered revenue. That dashboard becomes the SaaS UI in path (ii).
5. **Track cost-to-serve per account ruthlessly.** When the data shows one segment (e.g. Sydney med spas) converts at 80% with low support load, that's the SaaS-able beachhead.
6. **Identify and protect the proprietary layer early.** The vertical-specific prompt library, the missed-call recovery scoring algorithm, whatever it turns out to be. The day it appears, it's the wedge that makes path (ii) defensible.

The trap to refuse on sight: **don't take the A$20,000 bespoke install for one big client.** Looks like easy revenue. It's the single fastest way to kill path (ii) — six months of customization that doesn't generalize burns the runway and the case study rights and the founder's time.

---

## What's NOT in scope for Frontline base launch (deferred to later phases)

- **Frontline Knowledge (Tier 2)** — per-asset Q&A on inbound calls. Phase 2 SKU, build after at least 1 paying Tier 1 client. Spec implicit in `FRONTLINE-OUTBOUND-SPEC.md` and earlier strategy notes.
- **Frontline Outbound (Tier 3)** — AI database activation. Phase 2 SKU, build after at least 1 paying Tier 1 client. Full spec in `FRONTLINE-OUTBOUND-SPEC.md` (locked 2026-05-08 from Belle Property Manly customer-discovery conversation).
- **AI Opportunity Audit** — Phase 2 product (~A$500), sold to installed Frontline clients to identify additional AI opportunities in their business
- **Custom implementation services** (knowledge bots, marketing automation, custom workflows) — Phase 3, sold direct to installed accounts at A$3K–15K per project or A$1.5K–3K/mo retainer
- **Vertical-specific landing pages** (`/cleaners`, `/clinics`, `/tradies`, etc.) — Phase 3, only after 10 paying clients
- **Customer portal / dashboard** — Phase 4, only after 25 paying clients
- **International expansion** — Phase 4+, AU only for the first 12 months minimum

**Discipline rule (locked 2026-05-08):** Frontline base must have at least 1 paying external client before any work begins on Tier 2 or Tier 3. This rule exists to prevent strategic ADHD — the customer-discovery insights that produced the three-tier stack are valuable, but they must not delay the Tier 1 launch.

---

## Reference

Detail on each component lives in:

- `dsk-frontline-pilot-pack.md` — full DSK install playbook
- `eonia-frontline-pilot-pack.md` — full Eonia install playbook (clinic-adapted)
- `SALES-PREP-PACKAGE.md` — 10-min demo flow + 10 objection responses + 5 pricing rebuttals
- `ONBOARDING-EMAIL-SEQUENCE.md` — Day 1 / 3 / 7 / 14 customer onboarding emails
- `PILOT-CAPTURE-KIT.md` — 11-screenshot checklist + Day 28 metrics report email template
- `LINKEDIN-COMPANY-PAGE-COPY.md` + `LINKEDIN-FIRST-100-OUTREACH.md` + `LINKEDIN-FIRST-POST-DRAFT.md` — LinkedIn launch materials
- `COLD-EMAIL-V1-PROSPECTS.md` — 26 Sydney prospects + Apollo handoff for the remaining 24
- `THERAPIST-LAWYER-SHORTLIST.md` — three Sydney HR lawyers vetted for the Eonia therapist hire that frees up Peter's clinical hours for Frontline pilots
- `STATUS.md` — canonical state file, updated each session
