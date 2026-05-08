# Metis Cortex Outbound — Product Specification

> **Status: PARKED 2026-05-09** per Manus business review — regulatory risk (ACMA Do Not Call register, July 2026 mandatory AI disclosure rules) plus discipline rule (no Tier 3 work until 1 paying Tier 1 client). Spec preserved for future revisit. **Do not build, do not market, do not list publicly.**
>
> **Original status:** DRAFT — Phase 2 product. Do NOT build until Metis Cortex has at least 1 paying external client.
> **Author:** Claude Code, 2026-05-08
> **Trigger event:** Belle Property Manly conversation 2026-05-08 — agency stated their #1 pain is "finding buyers" not "missing calls"
> **Parked:** 2026-05-09 (Manus review)
> **Last updated:** 2026-05-09

---

## TL;DR

Metis Cortex Outbound is the **revenue-generating** counterpart to Metis Cortex (Inbound). Same Zoe persona, opposite direction.

Where Metis Cortex **answers** calls coming in, Outbound **makes** calls going out — to a business's existing customer/inquirer database, matched against a re-engagement trigger.

| | Metis Cortex (Inbound) | Metis Cortex Outbound |
|---|---|---|
| **Direction** | Answers calls | Makes calls |
| **Job to be done** | Stop missing calls | Activate dormant database |
| **Customer pain** | "We miss leads" | "We can't find enough buyers / patients / customers" |
| **Pricing logic** | Cost reduction (defensive) | Revenue generation (offensive) |
| **ARPU ceiling** | A$600/mo | A$2K–5K/mo |
| **Switching cost** | Low (forward a phone) | High (CRM integration) |
| **Vertical fit** | All target verticals | All target verticals — even better fit because each vertical has clear triggers |

**This is likely the SaaS-able layer of the Metis Cortex product stack.** Metis Cortex is the wedge to get into accounts. Outbound is the upsell that generates 3–5× the ARPU and creates real switching costs.

---

## The customer-discovery moment

On 2026-05-08, Peter spoke with Belle Property Manly and asked: *"What's your biggest issue at the moment?"*

They did NOT say:
- "We miss too many calls"
- "Buyers ask too many questions about listings"

They DID say:
- **"Finding buyers."**

That's the foundational signal. Real estate agents don't lack inbound; they lack matched buyers for the listings they have. The dormant asset is the buyer database — thousands of past inquirers, open-home attendees, "tell me about the next one" leads — that nobody systematically works because it's too time-consuming for human agents.

This pattern repeats across every target vertical. The product addresses the pattern.

---

## The pattern

```
Dormant database  +  Re-engagement trigger  =  Outbound matching call
─────────────────    ─────────────────────     ─────────────────────────
Past customers /     Time-based, cycle-based,    Zoe identifies the right
inquirers /          or event-based signal       person to call at the right
patients in CRM      that this person should     moment, makes the call,
                     hear from us NOW            books the action, hands
                                                 hot leads to the human
```

Three components:

1. **The database** — already exists in every target business. Sitting in their CRM (AgentBox, Cliniko, Jobber, Dentally, etc.) doing nothing.
2. **The trigger** — vertical-specific, but always one of: time-based (X months since last visit), cycle-based (treatment plan due), event-based (new listing, rate change, equipment age threshold).
3. **The call** — Zoe places it, identifies herself as AI working with the business, states the matched value, books the action.

---

## Vertical fit matrix

| Vertical | Database asset | Trigger | Per-call ceiling value | Estimated ARPU |
|---|---|---|---|---|
| **Real estate (residential boutique)** | Past inquirers + open-home attendees from CRM (AgentBox / Domain CRM / Vault / Box+Dice) | New listing matches buyer's saved criteria (price band, suburb, beds, type) | A$30K–80K commission per converted sale | **A$2,000–5,000/mo** per agency |
| **Dental practices** | Patient list with last-visit dates from Dentally / Praktika / Oasis / D4W | 6-month checkup due; treatment plan unfinished; insurance year-end approaching | A$200 hygienist → A$3K crown → A$8K orthodontic | **A$1,500–2,500/mo** per practice |
| **Aesthetic clinics** | Treatment-cycle patient data from Cliniko / Pabau | Botox 4 months out, filler 6–12 months out, IPL series due, lapsed patients | A$500–2K per session | **A$1,500–3,000/mo** per clinic |
| **Trades (plumber/electrician/builder)** | Past customers + equipment-age data from Jobber / ServiceM8 | Hot water 10–15yr replacement, gas safety annual, drain preventative, electrical safety | A$200 service → A$2.5K replacement | **A$1,000–2,500/mo** per business |
| **Cleaning (DSK)** | 20K Jobber records, mostly dormant one-off customers | 6-month post-job re-engagement, seasonal triggers, address-based (property sale → target new owner) | A$400–2.5K | **A$800–1,500/mo** per business |
| **Mortgage brokers** | Past clients + market data | Rate cycle change, fixed-term roll-off, equity threshold for next property | A$3K–6K commission per refinance | **A$2,000–4,000/mo** per broker |
| **Optometrists** | Patient list + 2-year glasses cycle | Annual exam due, glasses prescription anniversary | A$300–800 per visit | **A$1,000–1,800/mo** per practice |
| **Allied health** (physio, chiro, podiatry) | Treatment plan dropouts | "You had 3 sessions left, want to book?" | A$120–200 per session | **A$1,000–2,000/mo** per practice |
| **Personal trainers / gyms** | Lapsed member list | Time-based comeback offers | A$50–200/mo recurring | **A$800–1,500/mo** per business |
| **Solar installers** | Old quote requests, dormant leads | Rebate change, seasonal interest, energy-bill spikes | A$10K–15K install | **A$1,500–3,000/mo** per installer |

**Pattern observation:** the higher the per-conversion value (real estate, mortgage, solar), the higher the willingness to pay. The more recurring the conversion (gyms, allied health), the more volume-driven the model.

---

## Reference scenario — dental practice ROI math

Mid-size Sydney dental practice with 2,500 active patients:

**Without Outbound:**
- Standard recall protocol = SMS reminder 1 week before 6-month due
- Industry benchmark rebook rate = ~50%
- Result: 1,250 patients rebook out of 2,500 due. 1,250 patients drop out.

**With Outbound:**
- Zoe calls each patient when 6-month due. Conversational, handles objections ("I'm too busy," "it's too expensive," "let me check my diary"), offers alternative times.
- Rebook rate target = ~70%
- Result: 1,750 patients rebook. 500 additional appointments.

**The dollar math:**
- 500 additional appointments × A$250 avg = **A$125,000/year recovered revenue**
- Outbound cost: A$1,500/mo × 12 = A$18,000/year
- Net to practice: A$107,000/year
- **ROI: ~7×**

**Insurance year-end is the killer use case for dental.** Patients have unused dental insurance benefits expiring December 31. AI calls every patient with unused benefits in November-December. Conversion is high because "use it or lose it" creates real urgency. December alone could justify the year's spend.

---

## Architecture

### Components

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  CRM (per client)         Trigger Engine        Voice Layer     │
│  ─────────────────        ────────────────      ──────────────  │
│  - AgentBox API           - Time-based rules    - Twilio        │
│  - Cliniko API            - Cycle-based rules   - Retell agent  │
│  - Jobber API             - Event-based hooks   - Australian    │
│  - Dentally API           - Match scoring         voice config  │
│  - Domain CRM             - Priority queueing                   │
│  - Vault / Box+Dice                                             │
│       ↓                          ↓                    ↓         │
│       └──────────────────────────┴────────────────────┘         │
│                                  ↓                              │
│                      ┌───────────────────────┐                  │
│                      │  Outbound Orchestrator │                  │
│                      │  - When to call        │                  │
│                      │  - Which person        │                  │
│                      │  - What script         │                  │
│                      │  - Compliance gates    │                  │
│                      │  - Audit logging       │                  │
│                      └───────────────────────┘                  │
│                                  ↓                              │
│              ┌────────────────────┴────────────────────┐        │
│              ↓                                         ↓        │
│     ┌──────────────┐                          ┌──────────────┐  │
│     │ Hot lead     │                          │ Cold / no-   │  │
│     │ → warm-      │                          │ answer →     │  │
│     │   transfer   │                          │ SMS + email  │  │
│     │   to agent   │                          │ nurture      │  │
│     └──────────────┘                          └──────────────┘  │
│              ↓                                         ↓        │
│              └────────────────────┬────────────────────┘        │
│                                   ↓                             │
│                        ┌──────────────────────┐                 │
│                        │  Reporting Dashboard  │                 │
│                        │  - Calls made         │                 │
│                        │  - Reach rate         │                 │
│                        │  - Booking rate       │                 │
│                        │  - Revenue attributed │                 │
│                        └──────────────────────┘                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### CRM integration matrix (priority order)

| CRM | Vertical | Why this priority | API quality |
|---|---|---|---|
| **AgentBox** | Real estate (Australia residential dominant) | First integration — Belle Property and most boutique agencies use it | Solid REST API |
| **Cliniko** | Allied health, aesthetic clinics, dental (Australian default) | Second integration — covers Eonia + most Sydney clinics | Solid REST API, well-documented |
| **Jobber** | Cleaning, trades | Third — DSK is on Jobber, plus most Sydney tradies | Solid GraphQL API |
| **Dentally / Praktika** | Dental specifically | Fourth — dental-specific layer, separate from Cliniko | Variable |
| **Domain CRM / REA Group APIs** | Real estate (alternative to AgentBox) | Fifth — needed for some agencies that don't use AgentBox | Variable |
| **Vault / Box+Dice** | Real estate (alternative) | Sixth — niche but real | Limited |
| **Pabau / Halaxy** | Aesthetic / allied health alternatives | Seventh — if Eonia turns out to use one of these | Variable |

**Build order:** AgentBox first (Belle Manly demand), then Cliniko (Eonia + general clinic market), then Jobber (DSK + trades). Three integrations cover ~80% of target clients.

### Trigger types

**Time-based:**
- "Call this customer because it's been X months since their last visit/transaction"
- Examples: 6-month dental checkup, annual eye exam, 12-month hot water service

**Cycle-based:**
- "Call this customer because their treatment cycle / product life is at the trigger point"
- Examples: Botox 3-4 months post-injection, IPL course gap, 10-year hot water replacement window

**Event-based:**
- "Call this customer because something happened that makes this moment relevant"
- Examples: New real estate listing matching their criteria, interest rate change matching mortgage refinance threshold, end-of-financial-year approaching for accounting clients

### Compliance layer (mandatory before any outbound calls)

- **Privacy Act 1988 (Cth)** — calling people from a CRM database means using their personal data. Each business has consent terms in their privacy policy; verify before enrolling them.
- **Spam Act 2003 (Cth)** — "spam" includes voice calls. Existing customer relationship is a defence; cold/unsolicited calls without consent are not.
- **Do Not Call Register Act 2006 (Cth)** — DNCR check before every outbound call. Free API. Mandatory.
- **AI disclosure** — at the start of every call: *"Hi, this is Zoe — I'm an AI assistant working with [Business Name]..."*. Multiple Australian state regulations are tightening this.
- **Recording consent** — calls recorded under the standard "this call may be recorded" notice; Australian states differ on one-party vs two-party consent (NSW = one-party, VIC = two-party).
- **Opt-out path** — every call has a clear way to say "don't call me again." Honored within 5 business days per Spam Act.
- **Audit trail** — every call logged with timestamp, recipient, script used, outcome, opt-outs received. Defensive against regulatory complaints.

This is harder than Metis Cortex but well-trodden territory; existing voice AI platforms (Retell, Air, Vapi) have compliance hooks.

---

## Pricing model

Three options to test. Pick based on customer feedback in the validation phase.

### Option A — Flat retainer

| Tier | Description | Price |
|---|---|---|
| **Outbound Starter** | Up to 200 outbound calls/mo | A$1,500/mo |
| **Outbound Pro** | Up to 1,000 outbound calls/mo | A$3,000/mo |
| **Outbound Enterprise** | Unlimited calls, multiple triggers, multiple users | A$5,000/mo |

Setup fee A$2,500 one-off (CRM integration + trigger config + script tuning).

**Pro:** predictable, simple to bill, easy to forecast.
**Con:** doesn't scale with customer success — if Zoe drives A$50K of new revenue, you still get A$3K.

### Option B — Per-conversion (revenue share)

| Component | Calculation |
|---|---|
| **Setup fee** | A$2,500 one-off |
| **Monthly base** | A$500/mo (covers infrastructure) |
| **Per-conversion fee** | 5–10% of revenue from Zoe-sourced bookings, OR % of commission for real estate |

**Pro:** aligns incentives perfectly, scales with customer success.
**Con:** harder to bill cleanly, requires conversion attribution infrastructure (which calls led to which bookings led to which sales), customers may dispute attribution.

### Option C — Per-call

| Component | Calculation |
|---|---|
| **Setup fee** | A$2,500 one-off |
| **Per-call fee** | A$2–3 per call attempt + A$5–10 per successful conversation |

**Pro:** transparent, scales with usage, no attribution disputes.
**Con:** customers may try to game it (limit which lists you're allowed to call), and cost per call drives price-sensitive negotiation.

**Recommendation: Option A (flat retainer) for v1.** Simplest to sell, easiest to bill, customer can predict their cost. Test Option B in Year 2 once you have conversion data to back the % rate.

---

## Build phases

**Strict prerequisite: do NOT begin Phase 1 of Outbound build until Metis Cortex has at least 1 paying external client.** This rule exists to prevent strategic ADHD. Customer revenue on the base product is the gate.

### Phase 0 — Validation (concurrent with Metis Cortex launch)

**Cost: ~A$0. Time: 2 weeks of customer conversations.**

- Talk to 5 boutique real estate agencies (Belle Manly + 4 others)
- Talk to 3 dental practices
- Talk to 2 aesthetic clinics
- Validate: would they pay A$1,500–3,000/mo for outbound database activation? What CRM are they on? What triggers matter most?
- **Outcome gate:** at least 3 conversations result in "yes, I'd pay A$X/month for that." Without 3 confirmed willingness-to-pay statements, do not proceed to Phase 1.

### Phase 1 — Single-vertical MVP (real estate, AgentBox)

**Cost: ~A$5K in dev time + Twilio/Retell credits. Time: 6–8 weeks.**

- One CRM integration: AgentBox
- One trigger type: new listing → match buyer criteria → outbound call
- One vertical: residential real estate
- One pilot customer: ideally Belle Manly, otherwise the strongest from Phase 0 conversations
- **Outcome gate:** pilot customer reports at least 1 booked inspection from a Zoe-initiated call. Without that proof, don't expand.

### Phase 2 — Vertical expansion + second CRM

**Cost: ~A$10K dev + integration. Time: 8 weeks after Phase 1.**

- Second CRM integration: Cliniko
- Two new triggers: dental recall (time-based), aesthetic treatment cycle (cycle-based)
- Pilot customers: 1 dental practice + 1 aesthetic clinic
- **Outcome gate:** ROI math validated for both new pilots. ARPU model confirmed.

### Phase 3 — Productize + scale

**Cost: ~A$20K dev. Time: 12 weeks after Phase 2.**

- Third CRM integration: Jobber (covers DSK + trades)
- Self-serve trigger configuration UI
- Reporting dashboard with conversion attribution
- Onboarding playbook (~5-day install per customer instead of 14)
- **Outcome gate:** 5 paying Outbound customers, retention >85% at 3 months, ROI clearly documented.

### Phase 4 — Beachhead vertical dominance

**Cost: ongoing. Time: 12 months after Phase 3.**

- Pick 1 vertical you've gone deepest in (likely real estate)
- Build vertical-specific features competitors can't match (e.g. listing-document Q&A, agent commission attribution)
- Aim for 30+ paying Outbound clients in that vertical alone
- **Outcome gate:** A$50K+ MRR from one vertical. Decision point: stay vertical-deep, or expand horizontal?

---

## Success metrics

Track from Phase 1 onwards:

| Metric | Target | Why |
|---|---|---|
| **Outbound calls made** | Volume tracking | Capacity and pipeline measurement |
| **Reach rate** (calls answered or returned) | >40% | Below this = bad lead list or wrong time-of-day |
| **Conversation rate** (calls that become a real conversation) | >25% of reach | Below this = Zoe's opening is wrong |
| **Booking conversion rate** (conversations → booked appointment/inspection) | >15% | Below this = wrong audience or weak pitch |
| **Revenue attribution per call** | A$50–500 depending on vertical | Direct dollar value generated |
| **Customer ROI** | >3× monthly fee | Below this = customer churns |
| **Customer retention at 6 months** | >85% | Below this = product doesn't deliver sustainably |

---

## What this is NOT

To preserve scope discipline:

- ❌ NOT a generic outbound dialer (Air.ai, Bland.ai do that — generic, no integrations, no vertical understanding)
- ❌ NOT a CRM replacement (works with the CRM the business already uses)
- ❌ NOT a sales SDR replacement for prospecting NEW customers (operates against the EXISTING database — that's the wedge)
- ❌ NOT a marketing automation platform (no email-blast, no funnel-build, just outbound voice with smart targeting)
- ❌ NOT for clinics with privacy concerns until AU-residency RAG infrastructure is in place
- ❌ NOT a feature of Metis Cortex — it's a separate SKU with separate pricing, separate install playbook, separate value prop

---

## Risks

1. **Outbound calls have higher hang-up rate than inbound.** Even with good targeting, ~30-40% of calls will get hung up on within 10 seconds. Plan for it.
2. **Compliance is harder than inbound.** DNCR + Privacy + Spam + state-specific recording rules. Get this wrong = fines + reputation damage.
3. **CRM integrations are messy.** Every CRM has quirks. Plan for 2x estimated dev time on each integration.
4. **Customers may resist their data being processed by AI** — needs clear data processing agreement (DPA) at signup, AU-residency assurance, audit-trail access.
5. **Real estate agents may resist losing the relationship moment.** "Cold buyer pickup" is part of an agent's craft. Sell it as augmentation not replacement: hot leads still go to the human, Zoe handles the database mining the agent doesn't have time for.
6. **Conversion attribution disputes.** Customers will challenge "did Zoe really cause that booking?" Build robust attribution from day 1.
7. **Voice AI hallucinations on outbound.** Worse than inbound because the recipient didn't initiate — they're already skeptical. Strict quote-only mode needed.
8. **Strategic ADHD.** Building Outbound before Metis Cortex has paying clients is the single biggest risk. Discipline gate locked.

---

## Decision gates before any code

Before Phase 1 starts, all five must be true:

- [ ] Metis Cortex has at least 1 paying external client
- [ ] At least 3 customer conversations in target verticals have produced "yes, I'd pay A$X/month for that"
- [ ] Belle Property Manly (or another real estate agency) has signed a letter of intent or paid setup fee for the v1 pilot
- [ ] CRM API access confirmed working with AgentBox sandbox account
- [ ] Compliance review completed by an Australian privacy/spam-law lawyer (~A$1,000 budget)

Without all five, do not write code. Build conviction first.

---

## How this updates the broader Metis Cortex strategy

This product reframes the company:

**Before this spec was written:**
Metis Cortex = AI receptionist installer for Australian service businesses. Path-(i) leveraged boutique. ARPU ceiling A$600/mo per client. Year 1 revenue projection A$50–80K.

**After this spec:**
Metis Cortex = AI database activation for Australian service businesses, with inbound receptionist as the wedge. Path-(i) base + path-(i+) Outbound layer. ARPU ceiling A$5,000/mo per client. Year 1 revenue projection unchanged (A$50–80K) because Outbound doesn't ship until Metis Cortex has paying clients. Year 2 revenue projection upgraded to A$300–600K with Outbound layer landing 3–5× the ARPU per client.

The product stack becomes:

| Tier | Product | When it ships |
|---|---|---|
| Tier 0 | **Metis Cortex Triage** (inverse of Metis Cortex — politely declines new business, routes existing) | Phase 2, after Outbound is live |
| Tier 1 | **Metis Cortex** (inbound AI receptionist) | NOW (the launch product) |
| Tier 2 | **Metis Cortex Knowledge** (per-asset Q&A on inbound) | Phase 2, with Outbound |
| Tier 3 | **Metis Cortex Outbound** (database activation) | After 1 paying Metis Cortex client |

---

## Reference

- Belle Property Manly conversation 2026-05-08 (the trigger event)
- `HOW-IT-WORKS.md` — base business model (will be updated to reflect three-tier stack)
- `dsk-pilot-pack.md` — Metis Cortex install for DSK
- `eonia-pilot-pack.md` — Metis Cortex install for Eonia
- `COLD-EMAIL-V1-PROSPECTS.md` — 26 verified Sydney prospects, useful for Outbound validation conversations
- `STATUS.md` — canonical state
