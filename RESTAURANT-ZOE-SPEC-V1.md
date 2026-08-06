# Restaurant Zoe — Product Spec v1

**Direction locked 2026-05-20.** Supersedes all prior Metis Cortex direction (Path A receptionist, Path B vertical receptionist, Path C accountant AR-chase, Path D Sophiie-implementation-partner, micro-SaaS pivot, all variations).

---

## One-line product

**Restaurant Zoe** — AI receptionist built specifically for AU restaurants, with deep menu/dietary intelligence and native integration with restaurant booking systems (NowBookIt first).

## Why this wins

1. **Sophiie is not in restaurants.** Their Industries page targets tradies + salons. Restaurant-specific workflows aren't on their roadmap. The vertical is uncontested by the dominant horizontal player.
2. **Restaurant booking systems are integration moats.** NowBookIt / SevenRooms / ResDiary / OpenTable have vertical-specific data structures and partner-tier API gates. Once Metis ships the NowBookIt integration, Sophiie can't easily clone without ground-up work.
3. **Menu + dietary intelligence is the actual product moat.** A generic AI receptionist saying "let me transfer you to staff" when someone asks "is the carbonara gluten-free?" is a dead product. Restaurant Zoe knows: every dish, every allergen (GF/DF/V/VG/nuts/shellfish), modifications available, deposit policies, no-show rules, kids' menu, BYO rules, parking, dress code. Deep, structured, queryable.
4. **Operator credibility:** Peter Kritsotakis ran Limani Seafood Restaurant in Narrabeen for 21 years. Sells to restaurant owners as "the agency that knows what your floor manager deals with at 7:30pm Saturday with a 6-top no-show and a celiac walk-in." Unbeatable on trust by definition.
5. **Warm market access:** Limani's old supplier network + Northern Beaches restaurant cluster + Sydney hospitality contacts = real path to first 5-10 paying customers without cold outreach.

## Buyer profile

**Primary ICP:** AU mid-tier restaurants doing A$1-5M annual revenue (50-200 covers/night), independent or small group (1-5 locations), already paying for a booking platform (NowBookIt / SevenRooms / ResDiary). Reservations volume high enough that missed calls = real lost bookings (5+ missed calls/week minimum).

**Sydney focus initially:** Northern Beaches + Inner West + Eastern Suburbs. Peter's network density highest here.

**NOT the buyer:** chains, QSR/fast-food, takeaway-only, 20-cover small operations (too cheap to justify A$600/mo).

## Pricing (initial — subject to revision after first 3 installs)

- **Setup:** A$2,500 one-time (includes menu ingestion, booking system integration, voice tuning, 14-day install)
- **Monthly:** A$600/mo (covers Zoe agent time, ongoing tuning, support)
- **High-volume tier:** A$1,000/mo for 200+ covers/night (more agent minutes, more integration depth)

Premium positioning. Restaurants paying for AI Zoe are higher-end operations that already understand "saving 2 walk-aways/week = A$2-5K monthly recovered revenue >> A$600/mo cost."

Target MRR at 25 paying restaurants × A$600/mo = **A$15K MRR within 12 months.**

## Core features (MVP, first paying customer)

| Feature | Description |
|---|---|
| **Inbound voice answer** | Zoe picks up every call within 60sec. Greets in restaurant's voice. NSW Surveillance Devices Act recording disclosure. |
| **Menu intelligence** | Structured menu DB ingested from PDF/web. Answers dish-by-dish queries with allergen + dietary flags + price + descriptions. |
| **Dietary requirement handling** | "I'm celiac, what's safe?" → answers with confidence + offers chef confirmation for kitchen-prepared items. |
| **Reservation booking** | Direct write to NowBookIt for table reservations. Captures size, time, dietary notes, deposit requirement. |
| **Reservation modification** | Read existing booking, reschedule, modify covers, cancel per restaurant's policy. |
| **FAQ handling** | Hours, location, parking, dress code, BYO, kids' menu, function bookings, gift vouchers. Restaurant-specific. |
| **Escalation to staff** | When Zoe can't handle (private functions over X size, complaints, specific chef questions) → SMS forward to manager with summary. |
| **Daily ops report** | Email summary every morning: calls handled, bookings made, FAQs answered, escalations, anomalies. |

## Integrations (sequenced)

| Phase | Platform | Why |
|---|---|---|
| **MVP** | NowBookIt | AU-built, common in mid-tier Sydney restaurants, more accessible API access than enterprise platforms |
| Month 4-6 | SevenRooms | High-end venues; partner-tier API; opens premium Sydney CBD/Eastern Suburbs market |
| Month 6-9 | ResDiary | Enterprise; needed for hat-rated venues; partner certification process |
| Month 9-12 | OpenTable | Global; gating heavy; revisit when 20+ AU restaurants signed |
| Future | Square for Restaurants / Lightspeed POS | If venue uses POS-based booking instead of dedicated platform |

## Technical architecture

| Layer | Stack |
|---|---|
| Voice agent | Retell AI (existing decision — bundles voice + RAG + Twilio) |
| Telephony | Twilio (AU number, inbound forwarding from restaurant's existing line) |
| Menu DB | Postgres (or Airtable for MVP) — structured menu + allergen flags |
| Menu ingestion | Claude-powered PDF → JSON pipeline (one-shot at setup, manual updates monthly) |
| Booking write | NowBookIt API (verify partner access requirement) |
| Restaurant CRM | GoHighLevel sub-account (one per restaurant) |
| Hosting | Cloudflare Workers for orchestration |

Estimated build time to first paying customer: **3 months solo + Code AI leverage.**

## 12-month plan

| Month | Move | Target |
|---|---|---|
| 0-1 | Restaurant Zoe MVP build. NowBookIt API access. Menu ingestion pipeline. First voice agent. | Spec → working prototype |
| 1-2 | Install on 1-2 friendly Sydney restaurants from Peter's network. Pilot free or A$500 token. | First installs |
| 2-3 | Tune voice, integrations, menu Q&A from real call data. Document install playbook. | 3 case studies |
| 3-6 | First paying restaurants at A$2,500 + A$600/mo. Target: 5 paying clients = A$3K MRR. | A$3K MRR |
| 6-9 | Add SevenRooms integration. Open Eastern Suburbs / CBD market. | 12 paying clients ≈ A$7.2K MRR |
| 9-12 | Add ResDiary or expand to NSW regional/Melbourne. Refine pricing tiers. | 25 paying clients ≈ A$15K MRR |
| 12+ | Expand AU-wide. Consider second vertical (medspas? — Eonia synergy). | A$25K+ MRR |

## What dies

These prior directions are explicitly superseded:

- ❌ Path A — horizontal AI receptionist for trades (Sophiie's market, closed)
- ❌ Path C — DFY workflow automation for AU accountants (Sophiie's invoice chase ate the wedge)
- ❌ Path D — Sophiie-implementation-partner for tradies (services-heavy, not subscription)
- ❌ Hybrid (Lite + Pro ladder) — defer indefinitely
- ❌ "Speed to Lead" v1 framing — saturated globally
- ❌ Micro-SaaS pivot to AR-chase only — wedge dead
- ❌ Trades Grand Slam offer with 2× refund — receptionist play, dead

## What carries over

- ✅ Metis Cortex brand + ASIC registration
- ✅ Kritsotakis Family Trust entity + ABN
- ✅ metiscortex.au domain (currently coming-soon — stays so until 3 restaurant installs land)
- ✅ Brand assets (Cormorant + Inter, ink/bronze/bone palette, Manus PNGs)
- ✅ Zoe persona/name
- ✅ NSW Surveillance Devices Act recording disclosure greeting
- ✅ Privacy Policy (Manus-reviewed, AU Privacy Act 1988 compliant)
- ✅ Stripe trust account (`acct_1Qi7qr2nwvvosadL`) — pricing SKUs will be rebuilt for restaurant tier

## Open questions / risks

1. **NowBookIt API access** — need to verify partner-tier API is accessible. Worst case: requires direct partnership application + 4-6 weeks approval.
2. **Restaurant price sensitivity** — A$600/mo is significant for mid-tier restaurants. Need to validate with first 2-3 conversations that this is defensible.
3. **Customer Terms of Service** — same lawyer pass needed before Client #3 (chain-of-consent for NSW Surveillance Devices Act recording, ~A$300-600 budget).
4. **Sophiie expansion risk** — they could add restaurants to their Industries page in 6-12 months. Metis needs 5+ case studies + brand presence in Sydney restaurants before that window closes.
5. **Restaurant churn** — hospitality has 60% 5-year close rate. Build for higher churn than typical SaaS.

## First moves (week 1)

1. Verify NowBookIt API partner access — direct outreach to their partnerships team
2. Identify 5 Sydney restaurants in Peter's network for discovery conversations (NOT pitches yet)
3. Map menu ingestion pipeline architecture
4. Build Limani-style sample restaurant in dev (test menu DB + booking integration with Peter's institutional knowledge)

---

*Owner: Peter Kritsotakis. Spec generated 2026-05-20 (Sydney) after 12+ strategic reframes locked into single direction. No more pivots until 3 restaurant installs land or 90 days of execution data invalidates the spec.*
