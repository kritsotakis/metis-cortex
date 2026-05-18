# V3 Honest Copy — Hero + About + Service Strip

**Status:** Draft 2026-05-18. Replaces the receptionist-only Hormozi copy ("100% answered. Or your money back.") with v3 agency positioning + operator-credibility-without-false-case-study-claims.
**Constraint:** Must be defensible to "where else have you done this?" question. Currently: zero external case studies live; 1 accountant pilot pending; 4 internal businesses being built (DSK, Eonia, HydraLab, restaurant past). Copy below assumes that reality.
**Target file:** `src/components/Hero.tsx` + `src/app/page.tsx` + Footer. No tech rebuild — surgical copy patches to existing Next.js codebase.

---

## Hero — three variants to pick from

### Variant A — Operator-led, sober (recommended)

**Eyebrow (small caps above headline):**
AI systems for service businesses

**Headline (Cormorant, large):**
Built by an operator who's running it on his own businesses first.

**Subhead (Inter, lighter):**
I'm Peter — a Microsoft systems engineer turned 21-year restaurant operator, now building four service businesses. I built Metis Cortex because I needed it for my own operations first. We do AI receptionists, workflow automation, and operational audits for service businesses across Sydney.

**Primary CTA:** Book a 15-min intro call
**Secondary CTA:** See the service menu →

---

### Variant B — Three-act lead (more punchy, less safe)

**Eyebrow:**
AI systems for service businesses

**Headline:**
Six years building enterprise IT. Twenty-one years running a restaurant. Four businesses in flight. One AI agency.

**Subhead:**
That's the resume. Metis Cortex is what I'm building because every operator I know — including me — is bleeding time on phone calls, chasing unpaid invoices, and answering the same client questions 50 times a week. We fix that, with AI agents that actually know your business.

**Primary CTA:** Book a 15-min intro call
**Secondary CTA:** See the service menu →

---

### Variant C — Problem-led, founder hidden until later (safest, weakest differentiator)

**Eyebrow:**
AI systems for service businesses

**Headline:**
Stop bleeding hours to the phone, the inbox, and the chase.

**Subhead:**
AI receptionists, workflow automation, and operational audits — built by an operator who's installing it on his own service businesses first, before selling it to yours.

**Primary CTA:** Book a 15-min intro call
**Secondary CTA:** See the service menu →

---

## About — anchor the operator credibility (200 words, replaces any existing About)

**Section heading:** Built by an operator. Tested on his own businesses first.

**Body:**

Most AI agencies are slide decks plus a $200 ChatGPT wrapper. Metis Cortex is built by someone who's run real operations for thirty years.

I'm Peter Kritsotakis. Before this, I spent six years as a Microsoft systems engineer (MCSE, Cisco, Citrix) building enterprise infrastructure. Then I ran Limani Seafood Restaurant in Narrabeen for 21 years — overnight kitchen, weekend rush, the works. Sold it in 2025.

Today I'm building four service businesses under the Kritsotakis Family Trust: a Sydney cleaning brand (DSK), an aesthetic clinic (Eonia), a chemical manufacturing operation (HydraLab), and a trading-discipline software venture. Metis Cortex is what I'm building to solve the operational problems I keep hitting in those four — phone calls I can't answer, invoices I can't chase, repeat client questions I shouldn't be typing.

The agency is in its first month. We have one external pilot in flight (an accountant in Sydney). Everything we sell, we use ourselves first. If you want to be one of the first external installs in your vertical — at pilot terms — let's talk.

— Peter

---

## Service strip — 6 service lines, non-link list

Replaces the "WhatsIncluded" 7-item Hormozi value stack on the existing site.

**Section heading:** What we build for service businesses

| Service | Headline | One-liner |
|---|---|---|
| **AI Strategy & Audit** | Where are you bleeding time? | Two-week paid audit. We map your workflows, find 2–3 automation opportunities, and hand you a 90-day roadmap with ROI per opportunity. From A$2,000. |
| **AI Receptionist (Zoe)** | Answer every call. Even at 11pm. | Voice agent that handles overflow + after-hours calls, books into your CRM, and texts the caller with confirmation. From A$5,000 setup + A$1,500/mo. |
| **Workflow Automation** | Stop copy-pasting between tools. | n8n / Make builds connecting your Xero, Jobber, ServiceM8, Brevo, Slack. From A$3,000. |
| **Marketing Automation** | Wake up the list you already have. | Brevo / Mailchimp flows: welcome, nurture, post-purchase, win-back. From A$3,000 + A$500/mo. |
| **Website (Astro / Cloudflare)** | Fast, cheap, SEO-ready. | Static site on Cloudflare. The same architecture we run on our own businesses. From A$5,000 + A$200/mo. |
| **Custom AI Build** | When the off-the-shelf options have run out. | Bespoke agents, RAG systems, document processors, internal copilots. From A$10,000. |

**Below the table — one line:**
*One offer per engagement until we've earned the right to expand. No 18-month "platform" promises.*

---

## Footer — drop overstated claims

**Old (existing site, to remove):**
- "Built for Sydney service operators across cleaning, restaurant, real estate, dental, beauty — case studies forthcoming"
- Any reference to Eonia / HydraLab / Limani as "case studies"
- Founding-rate scarcity messaging ("5 founding spots left")

**New (replace with):**
- ASIC business name: Metis Cortex (registered 9 May 2026)
- ABN: 45 984 876 899 (Kritsotakis Family Trust)
- Email: info@metiscortex.au
- Service area: Sydney + AU (remote engagements available)
- Operating as: Kritsotakis Family Trust trading as Metis Cortex

---

## What to drop from the existing site

Surgical deletions (no rebuild, no rewrite — just remove these sections/lines):

1. **Hero** — the "100% answered. Or your money back." anchor + bronze underline.
2. **Guarantee section** — both stacked guarantees (100% missed calls + 10hrs saved / 14-day install or setup waived). Replace with the Audit's mini-guarantee + Grand Slam's 2× refund only on `/audit` and `/grand-slam` pages, NOT on homepage.
3. **CostOfMissedCalls** — entire section (talks about "21 years of operating four businesses" — kept the credibility line is OK; the rest implies operational data we don't have).
4. **WhatsIncluded** — replace with the 6-service strip above.
5. **ClosingCTA** — "Your next missed call is at 7pm tonight" copy is receptionist-only. Replace with generic "Book a 15-min intro call."
6. **FAQ entries about Sophiie / AiDial / Chime** — keep one differentiator FAQ, drop the rest (over-defensive vs competitors not relevant to agency positioning).
7. **DSKCaseStudy import comment-out** stays as-is — no DSK numbers yet, don't surface.

---

## What to KEEP from existing site

The good shipped work that carries through unchanged:

- Cormorant Garamond + Inter typography
- Ink #0F203F / Bone #F5F1EA / Bronze #B07843 palette
- "One bronze accent per composition" brand rule
- Manus PNG lockups (already in `public/brand/`)
- Privacy policy (`/privacy` — AU Privacy Act 1988 compliant, Manus-reviewed)
- 404 page (`/not-found`)
- Calendly + Plausible + LinkedIn placeholders in `src/lib/site.ts` (still need session-bound clicks from Peter to populate, queue still hot)
- Footer ASIC + ABN line
- `info@metiscortex.au` email routing

---

## Implementation plan

When Peter says "ship copy patches":

1. **Hero.tsx** — replace headline/subhead with Variant A (or selected variant)
2. **page.tsx** — remove `<CostOfMissedCalls />`, replace `<WhatsIncluded />` with new `<ServiceStrip />` component (or just inline since the data is small), update `<ClosingCTA />` copy
3. **New `<AboutOperator />` component** — drop in below Hero, above ServiceStrip. ~80 lines.
4. **`<Guarantee />` component** — delete from homepage; preserve content for `/audit` + `/grand-slam` landing pages (those land separately).
5. **`<FAQ />` component** — prune to 3-4 questions max, drop competitor-specific entries.
6. **Footer.tsx** — strip founding-rate fine print + case-study language; keep ASIC + ABN + email.

Estimated time: ~90 min surgical edits. Single commit. Cloudflare Pages auto-deploys on push to `main`.

---

## Decision needed from Peter

1. **Pick a Hero variant** — A (recommended), B, or C. Or "blend A+B" — I can mix.
2. **Confirm operator-credibility-only positioning** — drop all "4 case studies" framing from sales materials, accept "1 external pilot pending" honest claim?
3. **`ship copy patches`** — Code executes the implementation plan above.
4. **Founder bio length** — 200 words (above) feels right for the About section, but happy to cut to 100 if you want it punchier.

Doc owner: Code. Created 2026-05-18 after Peter shared 3-act background (MCSE/Cisco/Citrix → restaurant → 4-business founder) + flagged DSK/Eonia/HydraLab as not-yet-operational. Ready for Peter's variant pick + ship greenlight.
