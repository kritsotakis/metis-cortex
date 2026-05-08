# Metis Cortex — Design Brief for claude.ai/design

> **For:** Peter to paste into a fresh claude.ai chat (or use as the system context for a Claude artifact session) when designing collateral.
> **Last updated:** 2026-05-08
> **Site:** https://metiscortex.au (live)

---

## How to use this brief

Copy everything between the `---` rulers below. Paste it as the **first message** in a new claude.ai/design session. Then describe the specific asset you want designed (pitch deck slide, one-pager, social graphic, etc.). Claude will produce on-brand artifacts.

If you can attach files: also attach `public/brand/metiscortex-brand-guide.pdf` and the relevant logo SVGs from `public/brand/`. They give Claude the visual reference.

---

## ── PASTE EVERYTHING BELOW INTO claude.ai/design ──

# Metis Cortex — Brand context for Claude

You are designing collateral for **Metis Cortex**, an Australian-founded productised AI services business. Read this entire brief before producing any artifact. Match the voice, visual direction, and product framing precisely.

## What the business is

**Metis Cortex** installs AI receptionists ("Metis Cortex") on Australian service businesses. The AI persona is named **Zoe** (Greek for "life" — the meaning is not surfaced on customer-facing copy). She picks up every missed call within 60 seconds, qualifies the lead, and books the appointment.

**Product stack:**

| Tier | Product | Pricing | What it does |
|---|---|---|---|
| 1 | **Metis Cortex** | A$1,500 setup + A$600/mo | Inbound AI receptionist. Stops missed calls. |
| 2 | **Metis Cortex Knowledge** | +A$300/asset/mo | Per-asset Q&A — Zoe answers detailed questions about specific listings/customers. |
| 3 | **Metis Cortex Outbound** | A$1,500–5,000/mo | AI database activation — Zoe makes outbound matching calls against the customer's existing CRM database. |

**Refund guarantee:** If Metis Cortex doesn't book at least 5 extra appointments in month one, full refund of the install fee. No paperwork.

**The dogfood:** Built and proven on the founder's own cleaning business (DSK Property Cleaning) before being sold externally. The founder runs four service businesses — DSK, Eonia, HydraLab (chemistry R&D), Exit Code (trading software). Operator-to-operator credibility is the core moat.

## Who the customer is

Australian service businesses with phone-driven leads:

- **Property cleaning** (start vertical — DSK is case study)
- **Trades** (plumbers, electricians, builders, painters)
- **Boutique real estate agencies** (independent, not Belle/Ray White corporate)
- **Aesthetic clinics** (boutique only, Eonia is case study #2)
- **Dental / allied health** (single-location practices)

Common shape: 1-10 employees, owner-operator decision-maker, A$50K–500K/month revenue, phone is the lead acquisition channel, currently leaking missed calls to voicemail.

**Year 1: Sydney metro only.** Year 2: Australia-wide. Year 3+: international.

## Voice and tone

**Direct, plain English, Australian, anti-hype. Operator-to-operator.**

- ✅ *"Stop missing calls. $1,500 installed in 14 days. Refund if it doesn't work."*
- ✅ *"Your next missed call is at 7pm tonight. Want it booked by 7:01?"*
- ✅ *"Built and proven on DSK Property Cleaning."*
- ❌ *"Revolutionising engagement through transformative AI."*
- ❌ *"Empowering businesses with cutting-edge intelligence."*
- ❌ *"AI brain layer"*, *"Greek goddess"*, anatomical references to cortex/brain
- ❌ *"Excited to announce"*, *"Stoked to share"*, corporate launch tone

Numbers over adjectives. Specific over vague. *"48 hours"* not *"fast turnaround"*. *"5 extra appointments"* not *"meaningful uplift"*.

## Visual direction

**Premium but operational. Stripe meets a Sydney workshop.**

### Colour palette (locked)

| Role | Hex | Usage |
|---|---|---|
| Primary — Ink Navy | `#0e1e2e` | Backgrounds, body text on light surfaces, primary UI elements |
| Secondary — Bone Cream | `#f5f1ea` | Text on dark surfaces, light backgrounds, cards |
| Accent — Bronze | `#b07843` | Single-detail moments only — one accent per composition. Never as background fill. |

The bronze accent rule is critical: ONE bronze element per composition, used to draw the eye. Multiple bronze elements dilute the brand.

### Typography (locked)

| Role | Typeface | Weight | Usage |
|---|---|---|---|
| Display / Headings | Cormorant Garamond | 600 (SemiBold) | Logo wordmark, page headings, hero text |
| Body / UI | Inter | 400 (Regular) | Body copy, navigation, buttons, captions |

Display headings use **+6 letter-spacing**. The "CORTEX" subline of the logo uses **+12 letter-spacing**.

Fallback chains:
- Display: `'Cormorant Garamond', 'Tiempos Headline', 'GT Sectra', Georgia, serif`
- Body: `'Inter', 'IBM Plex Sans', -apple-system, Helvetica, sans-serif`

### Logo

The mark is a **brain-coral motif** rendered as cream linework on dark navy, with a single bronze accent line. The wordmark "METIS CORTEX" sits beneath, with METIS in serif (large) and CORTEX in sans (smaller, wider tracking).

**Asset paths in repo:**
- `public/brand/metiscortex-mark.svg` — mark only, dark variant
- `public/brand/metiscortex-mark-on-light.svg` — mark for light backgrounds
- `public/brand/metiscortex-mark-transparent.png` — transparent PNG for compositing
- `public/brand/metiscortex-wordmark.svg` — wordmark only, dark variant
- `public/brand/metiscortex-wordmark-on-light.svg` — wordmark for light backgrounds
- `public/brand/metiscortex-horizontal-lockup.svg` / `-on-light.svg` — full lockup
- `public/brand/metiscortex-stacked-lockup.svg` / `-on-light.svg` — stacked variant
- `public/brand/logo-mark-128.png` — 128px navy-bg, used in Hero header
- `public/brand/logo-mark-transparent-128.png` — 128px transparent, used in Footer
- `public/icons/favicon-{16,32,48,64,128,256,512,1024}.png` — favicon ladder

### Photography

**Real Australian service businesses at work** — tradies, cleaners, vans, ute trays, phones ringing. NOT stock photography. NOT AI-generated synthetic photos. NOT glass office buildings.

If photography isn't available, use abstract geometric compositions in the brand palette rather than stock or AI-generated imagery. The brief is firm: synthetic photography is forbidden.

### What to avoid

- ❌ Tech-blue (`#0066FF` and similar)
- ❌ Neon AI greens
- ❌ Generic SaaS purple
- ❌ Greek-key patterns, marble columns, togas, classical motifs
- ❌ Robot iconography
- ❌ Glitchy AI / cyberpunk aesthetics
- ❌ 3D embossing, glow effects, drop shadows on the mark
- ❌ Recolouring the mark in non-brand colours
- ❌ Setting "METIS" in sans-serif or "CORTEX" in serif (typographic hierarchy is intentional)
- ❌ Multiple bronze accents per composition

## Layout and composition rules

**Stacked lockup spacing:** mark centred above wordmark. Clear space around the lockup equals the height of the "CORTEX" text block on all sides.

**Horizontal lockup spacing:** mark left-aligned, wordmark right of mark. Horizontal gap between mark and text equals 0.5× mark width. Clear space on all sides equals mark height × 0.25.

**Minimum size:** horizontal lockup must not render below 120px wide. Below that threshold, use mark-only.

**Negative space matters.** Premium-but-operational brands use generous whitespace. Don't fill every pixel.

## The headline / hero patterns

When designing collateral, the headline pattern is one of:

1. **Direct command:** *"Stop missing calls."*
2. **Scenario hook:** *"Your next missed call is at 7pm tonight. Want it booked by 7:01?"*
3. **Result-led:** *"14 days. A$1,500. AI receptionist on your phone."*
4. **Trust line:** *"Built and proven on DSK Property Cleaning. Australian-owned."*

The **refund guarantee** is the single strongest piece of copy in any composition that needs a closer:

> *"If Metis Cortex doesn't book at least 5 extra appointments in month one, you get a full refund of the setup fee. No paperwork. No questions."*

## Three-line founder positioning

When credibility needs to be established (cold email, founder bio, about section):

> Peter Kritsotakis runs four Sydney service businesses — DSK Property Cleaning, Eonia, HydraLab chemistry, Exit Code trading software. Metis Cortex was built to fix the missed-call problem on his own businesses first. Operator-to-operator, not consultant-to-client.

## Scope rules for any artifact

- All copy is for **Australian English** (use AUD, "boot" not "trunk", spelling like "centre" "colour" "favour")
- Australian Privacy Act + Spam Act apply to any cold-outreach collateral
- TGA Therapeutic Goods Advertising Code applies to anything mentioning Eonia (no efficacy claims, no comparative claims, no prices for cosmetic treatments)
- Phase 1 launch is Metis Cortex ONLY publicly. Knowledge and Outbound are referenced only on internal/sales docs, not the public homepage.
- ASIC business name registration is paid as of 2026-05-08, registration number pending. Footer copy currently says "registration pending" — replace with actual number when issued.

---

## ── END OF PASTE ──

# Specific design tasks worth running through claude.ai/design

Once the brief above is in claude.ai/design, here are the priority artifacts to commission. Listed in order of business impact.

## Tier 1 — Use these in the next 4 weeks

### 1. Sales pitch deck (10–12 slides)

**Purpose:** Used in demos with prospects who want context before deciding. Sent as PDF after a demo as a leave-behind.

**Structure:**

1. Title slide — Metis Cortex wordmark, "Stop missing calls."
2. The problem — service businesses miss 30–40% of inbound calls
3. The cost — A$380 per missed call, 87% of leads who don't reach you in 60 seconds book a competitor
4. The product — Metis Cortex: AI receptionist, 14-day install
5. How it works — three steps, screenshots of Zoe answering a call
6. Pricing + guarantee — A$1,500 + A$600/mo, refund if doesn't book 5 extra
7. Case study — DSK Property Cleaning (with placeholder for real numbers post-Day 28)
8. Who it's for — service business verticals
9. What's NOT in scope — what we don't do (sets boundaries, builds trust)
10. The team — operator-to-operator positioning
11. Next step — book a demo at metiscortex.au or scope call
12. Thank you — clean closing slide

**Format:** PDF, 16:9 aspect ratio, embeddable HTML version for screen-share demos.

### 2. One-page sales sheet (PDF)

**Purpose:** Single-page leave-behind for in-person sales meetings (Peter does in-person visits to DSK strata clients, real estate agencies). Also as a download-after-demo.

**Structure:** Front side: hero + problem + solution + pricing + guarantee + book-demo CTA. Back side: how it works (3 steps) + DSK case study + integration logos (Jobber, ServiceM8, GoHighLevel, Cliniko) + contact details.

**Format:** A4 portrait PDF, double-sided, 250gsm matte print spec (Officeworks compatible).

### 3. LinkedIn post graphic templates (5 variants)

**Purpose:** When the DSK pilot Day 28 data lands, Peter posts the case study on the Metis Cortex LinkedIn company page. The post needs supporting graphics that drop into Cowork's existing post template (`LINKEDIN-FIRST-POST-DRAFT.md`).

**Variants:**

1. **Number-led** — large bronze number (e.g. "27 calls recovered") on navy bg, small wordmark bottom-right
2. **Before/After** — split-screen comparison of missed-calls metric, navy left / cream right
3. **Quote card** — single sentence quote ("Built on DSK first") with attribution
4. **Feature list** — checklist of what Metis Cortex does, clean Inter, single bronze checkmark accent
5. **Schedule a demo** — soft CTA card, Calendly URL

**Format:** 1080×1080 (square) for in-feed, 1080×1350 (4:5) for max feed real estate.

## Tier 2 — Use these when scaling (~2–6 months out)

### 4. Vertical-specific landing page templates

When the cold-email batch fires (Day 28 of DSK pilot), some prospects will land on `metiscortex.au` and need vertical-specific framing. Phase 3 of the strategy includes:

- `/cleaners` — DSK-led case study, cleaning-vertical objections
- `/tradies` — plumber/electrician case studies, missed-call-equals-lost-job math
- `/real-estate` — boutique buyer's agent + outbound buyer-activation pitch (Phase 2 product)
- `/clinics` — Eonia case study, TGA-compliant copy
- `/dental` — recall-rate uplift maths

Each is a single landing page with the same structural skeleton, vertical-specific stats and proof points.

### 5. Email signature designs (3 variants)

For Peter's outbound emails — sales follow-ups, lawyer engagements, partnership outreach. Three variants:

1. Minimal — text only, brand colours
2. With small logo lockup
3. With 1-line CTA ("Book a 10-min demo")

### 6. Demo recording cover art

When Peter records his first demo screen-share for prospects who can't book live, the recording needs intro/outro slides. Three slides total: intro card, mid-roll product shot, outro with CTA.

## Tier 3 — Use these when proven product-market fit (Phase 2+)

### 7. Reception SKU page design

Phase 2 product (Metis Cortex Knowledge) — a dedicated page once the SKU exists in production.

### 8. Metis Cortex Outbound product page

Phase 2 product per `OUTBOUND-SPEC.md` — needed when at least 1 paying client exists on Outbound.

### 9. Customer portal mockups

Phase 4 product per `HOW-IT-WORKS.md` deferred-scope list — only after 25 paying clients.

---

## Working files in this repo

When Peter uses claude.ai/design, attach the relevant ones:

- **Brand guide PDF** (visual reference): `public/brand/metiscortex-brand-guide.pdf`
- **Logo SVGs** (for trace/embed): everything in `public/brand/`
- **Social platform sizes** (existing renders for reference): `public/brand/social/*.png`
- **Existing site code** (for layout patterns): `src/components/Hero.tsx`, `src/components/Footer.tsx`
- **Tailwind tokens** (for hex/typography reuse): `src/app/globals.css`
- **Brand discipline rules** (text reference): `HOW-IT-WORKS.md` discipline rules section + `OUTBOUND-SPEC.md` "what NOT" sections

## Process notes for claude.ai/design

- **Iterate small, ship clean.** Don't ask for "the whole pitch deck" in one prompt. Run slide-by-slide and integrate.
- **Demand restraint.** Claude artifacts can over-design. The brand is restrained. If an artifact has 4 colours instead of 3, push back.
- **Test at 16×16 / 32×32 sizes.** Anything that doesn't read at favicon size doesn't read at Twitter avatar size either.
- **AU compliance check on every cold-outreach piece.** Anti-Spam Act language, opt-out path, identifying info.

## What this brief does NOT cover

- Trademark / IP protection (separate playbook in `eonia-pilot-pack.md` and Exit Code IP work)
- Legal review of any specific claims (lawyer engaged separately for term sheet, see `THERAPIST-LAWYER-SHORTLIST.md`)
- Regulatory copy for clinics/medical (TGA review needed for Eonia-specific content)
- A/B testing methodology (separate Cowork brief if needed)
