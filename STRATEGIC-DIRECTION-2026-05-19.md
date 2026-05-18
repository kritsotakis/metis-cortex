# Strategic Direction Memo — 2026-05-19

**For:** Peter Kritsotakis
**Authored by:** Code, synthesised from 4-agent parallel research (pricing-strategy + competitive-landscape + mom-test + hundred-million-offers)
**Status:** Decision-ready. Site is dropped to coming-soon while direction firms up.

---

## The strategic finding

**The horizontal AI receptionist market closed for new entrants between May 8 and May 19.** Three things shifted:

1. **Sophiie is A$300/mo, not A$450/mo.** Stale data. They have 175+ customers, partnership channel via Tradiespace, fast-shipping (multi-channel inbox + Android app in ~3 weeks).
2. **Trillet + CallMate (Solve8) launched at A$49/mo.** Below Sophiie. Collapsed the price floor.
3. **Healthengine "Helen" went national for AU GPs.** Integrated with Best Practice + MedicalDirector Pracsoft. GP vertical now closed entirely.

**Implication:** competing horizontally with Sophiie at any price point — even a clever metered-overage wedge — is a brand + volume war a new entrant can't win in 12 months. The reprice we were considering (A$2,500 + A$750/mo) would pattern-match Valory (existing struggling player) and lose on volume vs Sophiie.

**Source:** `~/Desktop/metis-cortex/COMPETITIVE-LANDSCAPE-2026-05-19.md` (Agent 2 refresh, 11 days after baseline)

---

## The three paths considered

| | Path A — Horizontal AI receptionist | Path B — Vertical AI receptionist | Path C — DFY workflow automation |
|---|---|---|---|
| **Position** | Compete with Sophiie on done-for-you + metered pricing | Pick ONE vertical (aesthetic / boutique law / allied health) and own end-to-end | Sell workflow automation (AR-chase, EOFY, AI client-comms) to AU professional services, starting with accountants |
| **First client path** | Cold outreach to Sydney trades | Cold outreach to vertical of choice | Warm: tomorrow's accountant call |
| **Case study path** | DSK pilot data (DSK has no calls — see Open Loop) | Eonia (not launched) | Accountant pilot Day 90 numbers |
| **Differentiation** | Done-for-you + metered overage — weak vs Sophiie's brand | Compliance-baked-in for AHPRA / LPA verticals — defensible | Operator + IT background fits accountant buyer perfectly |
| **Sophiie threat** | Direct competition, you lose | Sophiie weak in compliance verticals — you can win | Sophiie not in this market — no overlap |
| **12-month MRR target ($15-30K)** | Need 30-50 retail clients — too aggressive for solo | Need 15-20 vertical clients at premium pricing — realistic | Need 10-15 accountant clients at A$750 retainer — realistic + warm referral compounding |
| **Risk profile** | High — brand war + customer service team needed | Medium — vertical specialisation requires niche expertise | Low — proven model (consultancy → SaaS), warm path through accountant |

---

## My recommendation

**Path C as primary direction. Path B as natural expansion in months 6-12.**

Concretely: stop trying to lead with AI receptionist. Lead with **done-for-you workflow automation for Australian accountants**. AI receptionist (Zoe) becomes a future Tier 2 product within a vertical-specific suite once the accountant case study lands.

**Why C wins:**

1. **You have a warm path tomorrow.** Your accountant already has the three pains (capacity / AR / phone calls). She'll likely say yes to a free 90-day pilot if you run the Mom Test discipline properly.
2. **Accountants buy from operators, not agencies.** Your 6 years enterprise IT + 21 years restaurant + 30 years operating background is the ideal credibility profile for an accounting practice owner. AI receptionist buyers care about voice quality and brand; accountant buyers care about whether you understand business systems. That's literally you.
3. **Sophiie isn't in this market.** Accountant workflow automation is fragmented, undermarketed, and high-willingness-to-pay (typical accounting firm spends A$2-5K/mo on practice management + tools — A$750/mo for AR-chase that recovers A$10K+/yr is rounding error).
4. **Referral physics are strong.** Accountants talk to other accountants. One happy pilot → 2 warm intros → 4 cold leads → 1 second client. Compound growth pattern.
5. **Margins are better than receptionist.** No voice minutes. COGS per client drops to ~A$50/mo. Margin at A$750/mo ≈ 93%.

---

## 12-month operating plan

| Month | Move | Outcome |
|---|---|---|
| **0 (tomorrow)** | Accountant call. Mom Test brief in hand. AR-chase pilot pitched. | Yes / no. Likely yes. |
| **1-2** | Build AR-chase workflow in her practice (n8n + Brevo + Xero integration + email/SMS templates in her voice). | Real install, real data. |
| **3 (Day 90)** | Capture numbers, testimonial, 2 referrals. | **Case study #1.** Real, defensible. |
| **4-6** | Pitch 2 referred accountants. Standardise install playbook. A$2,500 setup + A$500-750/mo retainer. | 1-2 paid signs. |
| **6-9** | Add EOFY workflow + AI client-comms as upsells to first 2 clients. Stack revenue per client to A$1,000+/mo. | Per-client revenue grows. |
| **9-12** | 8-12 retainer clients × A$750 avg = **A$6-9K MRR.** | On track for A$15K MRR by month 15. |
| **12-18** | Expand to second vertical (boutique law OR allied health). Use accountant playbook as template. | Vertical compounding. |

---

## What this means for the site

**Today:** dropped to coming-soon placeholder. Hidden from search engines (`robots: noindex`). Email link only. Brand visible (mark + wordmark), no claims, no pricing, no positioning that commits to direction.

**After tomorrow's call:**
- If she says yes → I rewrite the site over the next week as **"Done-for-you automation for Australian accountants. Built by a 30-year operator."** Single vertical, single message, accountant-pilot as the hero case study (with her permission). Trades Grand Slam shelved entirely.
- If she says no → reassess. Possibly pivot to a different vertical / different prospect. But she's unlikely to say no — pain is named, relationship is warm.

---

## What's on hold

- **AI receptionist (Zoe) flagship positioning** — parked. Becomes Tier 2 product within a vertical suite later, or dropped entirely.
- **Trades Grand Slam offer** — parked. Vertical specialisation supersedes.
- **Founding-rate scarcity copy + "4 case studies" overclaim** — already killed.
- **`.ai` domain registration** — still optional/defensive, no urgency.
- **Stripe v3 pivot diff (STRIPE-DIFF-PIVOT-V3.md + STRIPE-DASHBOARD-RUNBOOK.md)** — needs revisiting. New pricing structure (workflow automation, not receptionist) means the Stripe SKUs need a different set: AI Audit + Workflow Setup + Workflow Monthly with vertical-specific pricing. Don't apply the existing diff. We'll redo it after Path C is validated.
- **Trades Grand Slam attribution mechanism spec** — preserved in chat output (Agent 4). If we ever return to Path A or B, the spec is ready to ship. Not relevant for Path C.

---

## What's locked in

- **Brand:** Metis Cortex (ASIC registered 9 May 2026, ABN 45 984 876 899 under Kritsotakis Family Trust)
- **Domain:** metiscortex.au (live, .ai optional defensive)
- **Visual identity:** Cormorant + Inter typography, ink/bronze/bone palette, Manus PNG lockups
- **Email:** info@metiscortex.au (Google Workspace, MX live, SPF still pending fix)
- **Privacy policy:** AU Privacy Act 1988 compliant draft, Manus-reviewed
- **Stack:** Retell + Twilio + Claude + GHL + n8n (validated COGS per Agent 1)

---

## The hard truth

The "best you can" version of Metis Cortex isn't the version trying to be everything for every service business. It's the version that picks ONE vertical you can dominate by being the operator-credible specialist. Accountants first. Then law. Then allied health. Vertical expansion, not horizontal soup.

Your competitor isn't Sophiie. Your competitor is the accountant down the road who's still doing BAS chase in Outlook. Metis becomes the firm that takes that off her plate.

That's where you win. Tomorrow's call is step one.

---

*This memo supersedes the v3 pivot positioning (May 17-18) which assumed a horizontal AI agency could compete in the AI receptionist market. New competitive data invalidates that assumption. Path C reorients toward Peter's actual market advantage.*
