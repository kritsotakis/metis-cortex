# Metis Cortex — Code Session Brief

**For:** Claude Code (new Metis Cortex session)
**From:** Peter Kritsotakis
**Date:** 2026-05-21 (Sydney)
**Status:** Pre-build. Committed direction. Brand fully repositioned from prior history.

> **First action:** read this brief end-to-end, then read `~/.claude/CLAUDE.md` (global protocol). Then propose your starting plan in chat. Do NOT carry over assumptions from prior Metis Cortex v1-v8 framings (hospitality consulting, agency, receptionist) — those are dead. This is a clean repositioning.

---

## Quick context

**Metis Cortex is being repositioned to an AI trading research platform.** Standalone brand, standalone product, standalone regulatory posture. It pairs conceptually with Peter's EXIT CODE business (trading discipline software) but is architecturally separate.

**Why separate, not folded into EXIT CODE:** EXIT CODE operates under strict editorial/legal posture — purely educational content, no real-time market intelligence, no actionable signals. Adding a scanner that identifies trade setups would break those gates and put EXIT CODE's brand at risk. Cleaner architecture: keep EXIT CODE as the discipline framework brand, Metis Cortex as the research/scanner brand. Two complementary brands, two separate risk profiles, no contamination.

**The prior Metis Cortex v1-v8 history** (hospitality consulting, agency, receptionist variations) is dead. The brand's ASIC registration + Cloudflare DNS infrastructure are being repurposed to the trading-research direction. Do not re-evaluate the prior framings; they are archived.

---

## Business identity (locked)

| Field | Value |
|---|---|
| Business name | **Metis Cortex** (already ASIC registered 9 May 2026) |
| Entity | Kritsotakis Family Trust (ABN 45 984 876 899) — same trust as DSK / EXIT CODE / Komiti / HydraLab |
| Primary domain | metiscortex.au (already registered, currently shows coming-soon placeholder) |
| Defensive domain | metiscortex.ai (TBD — consider registering as defensive hold) |
| Brand email | info@metiscortex.au (already routing via Google Workspace) |
| Stripe | Existing products in shared trust Stripe account `acct_1Qi7qr2nwvvosadL` — will need repositioning |
| Memory mirror | `~/.claude/memory/metis-cortex-status.md` (already exists, needs full rewrite for new direction) |
| PAIR.md location | `~/Desktop/metis-cortex/PAIR.md` (exists from prior history — needs reset header) |
| Notion page ID | `35de39f4-1f45-8175-be25-eb43e510311c` (already created) |

---

## Product spec

### One-line pitch

> **Metis Cortex — AI trading research platform. Identifies pattern setups across markets. Pairs with disciplined execution frameworks (like EXIT CODE) so traders can focus on judgment, not chart-scanning.**

### Buyer

Active retail/prosumer traders who:
- Already use TradingView, ThinkOrSwim, or similar charting platforms
- Trade 5-50+ times per month across crypto + forex + equities
- Pay A$50-300/mo for some combination of tools, indicators, communities, courses
- Are technically literate (comfortable with API keys, technical analysis terminology, risk management concepts)
- Value research/identification tools over alert-spam services
- Understand AI outputs are research material, not actionable recommendations

### v1 product scope (start narrow, expand later)

**v1 = AI Pattern Scanner ONLY across 2 asset classes (crypto + forex).** Equities deferred to v2 because of differing regulatory posture across jurisdictions.

1. **AI pattern recognition engine**
   - Identifies common technical setup patterns across multiple timeframes (4H / Daily / Weekly initially)
   - Pattern library: momentum, mean reversion, breakout, breakdown, support/resistance, trend continuation, divergence
   - Quality scoring per finding (A/B/C confluence)
   - Educational tag on every output describing the pattern type + technical criteria

2. **Subscriber dashboard**
   - Daily research digest (top 5-10 highest-quality findings per session)
   - Filterable by market / timeframe / pattern type / quality grade
   - Click-through to chart visualization
   - Subscriber can mark items as "reviewed" / "interesting" / "skipped" (personal journaling)

3. **TradingView Pine Script overlay** (subscriber-gated)
   - Visual markers on user's own TradingView charts
   - Pattern type label on each marker
   - No "buy/sell" labels — purely descriptive ("Momentum continuation setup, 4H, Grade A")

4. **Email research digest**
   - Daily morning email with top findings
   - Educational context for each finding
   - No direct execution call-to-action

**NOT in v1:**
- ❌ ASX or other equities markets (deferred to v2 once regulatory posture is settled)
- ❌ Push notifications / SMS / Telegram alerts (escalates posture from research → time-sensitive recommendation)
- ❌ Auto-trading or order execution (entirely different product category)
- ❌ Specific position sizing or stop-loss recommendations
- ❌ Performance "track record" claims or back-tested return projections
- ❌ Copy-trading or social trading features

---

## Pricing structure

Three-tier subscription:

| Tier | Price | What's included |
|---|---|---|
| Standard | A$49/mo | Daily digest, top 5 findings, Pine overlay (basic) |
| Pro | A$129/mo | All findings (15-25/day), all asset classes in scope, advanced filters |
| Elite | A$349/mo | Pro + monthly research review call + early access to new pattern types |

**Founding rate:** First 50 paying subscribers get A$29/mo locked-in indefinitely for the Standard tier. Promoted as "founding research members."

**Pricing rationale:**
- A$49 Standard is high enough to filter for serious traders, low enough to overcome cold-start friction
- A$129 Pro is the volume play (target tier)
- A$349 Elite captures high-engagement users + creates direct feedback loop via monthly calls
- No A$499+ tier — keeps positioning research-focused, not "premium signal service"

---

## Tech stack

**Recommended foundation: GoHighLevel (GHL) for subscriber-facing layer + custom Python for scanner engine.** This cuts build time materially by skipping auth/CRM/billing/portal infrastructure.

**Metis Cortex gets its own dedicated GHL Agency Starter account (~A$150/mo).** No shared infrastructure with any other Kritsotakis business — Komiti is architecturally separate, EXIT CODE is architecturally separate. Total operational separation: clean subscriber data, clean billing trail, clean audit trail, isolated risk profile (important given trading-research category posture).

| Layer | Tool | Notes |
|---|---|---|
| Subscriber CRM + portal + auth + billing | **GoHighLevel** (dedicated Metis Cortex account) | White-labelled to metiscortex.au branding |
| Email + SMS digest delivery | GHL native + workflows | Daily digest pushed via GHL automations |
| Sign-up funnel | GHL funnel builder | Faster than custom Next.js for v1 |
| Workflow automation | GHL workflows | Trigger emails/notifications on new findings |
| Market data ingestion | Binance API (crypto) + OANDA or similar (forex) | Multi-source for redundancy |
| Historical data + backtest | Tiingo, Polygon, or similar | For pattern validation |
| Pattern recognition engine | Custom Python + Claude for context | TA-Lib for indicators + LLM for nuance |
| Scanner orchestration | Cloudflare Workers + Cron Triggers | Runs separately from GHL (dedicated Metis Cortex infrastructure) |
| GHL ↔ scanner integration | Webhook (scanner → GHL custom field → workflow trigger) | Clean separation of concerns |
| Pine Script overlay | TradingView publishing | Subscriber-only access via TradingView's input-field gating (under Metis Cortex TradingView account, separate from any EXIT CODE accounts) |
| Payments | Stripe via GHL native integration | Uses trust account `acct_1Qi7qr2nwvvosadL` with Metis Cortex-tagged products (per existing brand convention) |

**Build time impact:**
- **Without GHL:** 12-16 weeks officially (4-9 months realistic per reviewer analysis)
- **With GHL foundation:** 4-8 weeks for v1 MVP — skip building auth/CRM/billing/portal entirely

**Why GHL is the right call here:**
- Peter already familiar (same stack referenced in Komiti brief as multi-tenant option)
- Battle-tested for solo operators running SaaS-like subscriptions
- Native white-label + custom domain support
- Removes the lowest-leverage build work (auth, portal, billing) so you focus on the actual moat (scanner accuracy)

**Tradeoffs to acknowledge:**
- ~A$450/mo platform cost regardless of subscriber count (breakeven ~10 subscribers)
- GHL UX is marketing-agency-flavoured, not pure-SaaS-product feel
- Vendor lock-in to GHL pricing/availability
- White-labelling helps but doesn't perfectly hide GHL aesthetic

**Alternative if GHL doesn't fit:** Custom Next.js on Cloudflare Pages + Memberstack auth + Stripe Subscriptions. Same stack as existing metiscortex.au site. 12-16 week build instead of 4-8.

**NOT considered:** Metis Cortex as a GHL-reseller agency — that would land back in the saturated AI agency space the reviewers warned against. Different brand, different conversation.

---

## Locked constraints (NOT up for debate)

- Brand: **Metis Cortex** (already ASIC registered, reusing existing infrastructure)
- Entity: Kritsotakis Family Trust (ABN 45 984 876 899)
- v1 = Crypto + Forex only (equities deferred)
- AUD pricing year 1, global expansion year 2
- Solo operator + AI leverage (no team hires until 100+ paying subs)
- Subscription model — NOT trade-copy, NOT auto-trading, NOT managed accounts
- Research/educational framing on all outputs — never specific "buy/sell" calls
- **Architecturally separate from EXIT CODE** — different brand, different posture, no cross-contamination

---

## Realistic expectations (the honest version per prior 4-reviewer feedback)

This is the hardest market Peter has explored across all his ventures. Reviewers were unanimous on these structural challenges:

1. **Hard market.** AI trading research / signal category has 50+ existing players. Cold-start customer acquisition is challenging without an existing audience.

2. **Regulatory posture is real.** AU regulatory framework around financial information services is strict. Required Day 1:
   - Clear research-not-advice framing throughout
   - "Educational research only, not financial advice" disclaimer on every output
   - Standard Terms of Service explicitly disclaiming responsibility for trade outcomes
   - Privacy Policy compliant with AU Privacy Act 1988
   - Professional indemnity insurance specific to information services (not Peter's existing business insurance)
   - Recommend operating with `info@metiscortex.au` as primary contact, with formal customer support channel separate from Peter's personal/DSK/Komiti channels

3. **Build complexity is higher than nominal estimate.** Market data reliability + pattern accuracy + false-positive reduction are ongoing tuning work, not "build once and forget" SaaS. Plan for 4-9 months to MVP that's reliable enough to charge for.

4. **Customer psychology in this category is volatile.** Subscribers churn fast after market drawdowns. Retention requires strong educational framework, not just accuracy claims.

5. **Distribution requires sustained content output.** Pine Script publication on TradingView is the only realistic organic discovery channel for solo operators. Requires consistent script updates + educational TradingView posts.

6. **Solo-operator capacity reality:** Peter has 4 other ventures (DSK, Eonia, HydraLab, EXIT CODE) plus the new Komiti commitment. Adding Metis Cortex makes 6 active ventures against ~60 hrs/week realistic capacity. Something will be neglected.

These constraints are not deal-breakers but they ARE real. Code should treat them as design constraints, not problems to argue away.

---

## 90-day execution plan

**Weeks 1-2: Foundation reset**
- Reset metiscortex.au site copy from current "coming-soon placeholder" to trading-research positioning
- Update STATUS.md to reflect new direction (full rewrite of existing file — strip all prior hospitality/agency framings)
- Reset PAIR.md header with new project state
- Update Notion page to match
- Set up Terms of Service + Privacy Policy + research-disclaimer framework
- Apply for PI insurance quote (information services / research SaaS)
- Define core pattern library scope (10-15 patterns for v1)

**Weeks 3-6: Data pipeline + pattern engine v0.1**
- Set up market data ingestion (crypto first — simpler API access)
- Build pattern recognition pipeline for 3 highest-priority patterns (momentum continuation, mean reversion, breakout)
- Run historical backtesting to validate pattern detection accuracy
- Build internal dashboard for QA review of detections

**Weeks 7-10: Subscriber product MVP**
- Build subscriber Next.js portal on Cloudflare Pages
- Subscriber auth + Stripe subscription
- Daily digest email pipeline
- Pine Script overlay (basic version) published to TradingView
- Subscriber-gated access via TradingView's input field gating

**Weeks 11-14: Closed beta**
- Recruit 20 closed-beta users (mix of EXIT CODE customer list + Peter's trading network)
- Free 30-day access in exchange for structured feedback
- Daily digest emails active
- Pattern accuracy tuning based on beta feedback
- Refine false-positive reduction logic

**Weeks 15+: Public launch (likely Month 4-5 realistic)**
- Open paid subscriptions
- Founding rate A$29/mo for first 50 standard subscribers
- TradingView Pine Script publication for organic discovery
- Email blast to EXIT CODE customer list (cross-promotion, with clear separation that this is a distinct brand)
- Q1 conservative target: 30 paying subscribers = A$1,500-4,000 MRR

---

## Distribution strategy

**Phase 1 (Weeks 7-14, closed beta):** Curated invite-only access. Quality > volume. 20 beta users provides enough signal-quality feedback to refine v1.

**Phase 2 (Month 4-6, public launch):**
- TradingView Pine Script publication — primary organic discovery
- Educational content under Peter's name (or anonymous brand — TBD)
- EXIT CODE customer list cross-promotion (with clear brand separation)
- Trading community presence (Reddit, Twitter, niche Discords) — sustained content output required

**Phase 3 (Month 6-12):**
- Affiliate program for established trading educators
- Selective podcast appearances
- Paid acquisition tests only after organic shows >2% conversion rate

**NOT in scope:** Influencer marketing, copy-trading platforms, performance leaderboards, public track-record claims.

---

## Legal / compliance posture (Day 1 essentials)

**Required Day 1 setup:**

1. **Professional indemnity insurance** specific to information services / research SaaS (Peter's existing business insurance does NOT cover this category)
2. **Terms of Service** explicitly stating:
   - All output is research / educational material
   - Not financial advice, not personalised recommendations
   - Subscriber acknowledges full responsibility for all trading decisions
   - No guarantees of accuracy, performance, or outcomes
3. **Privacy Policy** compliant with AU Privacy Act 1988
4. **Research disclaimer on every output:**
   - Email digests
   - Pine Script overlay labels
   - Dashboard findings
   - Sample wording: "Educational research material — not financial advice. Independently verify all information before making any trading decision."
5. **Customer support boundaries:**
   - No 1:1 trade discussion in customer support
   - No "should I buy/sell X?" responses
   - Support sticks to product usage + technical issues only
6. **Data retention policy** — clearly stated how long subscriber data + research history is retained

These are operational design constraints, not problems to circumvent. Build them in from Day 1.

---

## What's NOT in scope (intentional scope discipline)

- ❌ Trading bot software or auto-execution
- ❌ Managed accounts / discretionary trading services
- ❌ Equities markets in v1 (deferred to v2)
- ❌ Push/SMS/Telegram alerts in v1 (too time-sensitive — escalates posture)
- ❌ Performance track-record claims or returns marketing
- ❌ Copy-trading or trade-following features
- ❌ Influencer-style branding (sustained anonymous-or-low-profile brand, not founder-personality marketing)
- ❌ EXIT CODE bundling at the product level (architecturally separate brands)

---

## First concrete actions (Code's first session output)

When Peter says `start metis cortex build`:

1. **Audit existing Metis Cortex infrastructure** — STATUS.md / PAIR.md / Notion / Stripe products / domain / DNS / repo
2. **Identify what needs reset** vs what can be reused (most of the prior hospitality-positioning content needs archiving)
3. **Check Stripe products** — likely need to deactivate old hospitality-tier products + create new trading-research subscription products
4. **Verify metiscortex.au DNS + Cloudflare Pages** still healthy
5. **Update STATUS.md** to reflect new direction (full rewrite — strip prior framings)
6. **Mirror STATUS.md to `~/.claude/memory/metis-cortex-status.md`**
7. **Reset PAIR.md header** for new project state
8. **Propose v1 build sequence in chat** for Peter to greenlight before coding starts

Peter will then say either:
- `greenlight: reset infrastructure` → Code proceeds with cleanup
- `greenlight: start pattern engine` → Code begins technical build
- `wait` → Peter handles something manually first
- Push back on something in the brief

---

## Session protocol (follow Peter's locked global pattern)

Per `~/.claude/CLAUDE.md`:

- **STATUS file structure (locked):** State (3-line summary) · In Flight · Done This Sprint · Open Loops · Trigger Phrases (reactive) · Next Live Trigger · Decision Log (append-only) · Reference docs
- **Mirror STATUS to 3 locations:** `~/Desktop/metis-cortex/STATUS.md` + `~/.claude/memory/metis-cortex-status.md` + Notion page `35de39f4-1f45-8175-be25-eb43e510311c`
- **PAIR.md is the Code↔Cowork channel** — talk to Cowork via the file, not by routing through Peter
- **Lane discipline:** Code does repo edits, git, deploys, build/test, file system, local dev. Cowork does docs, browser automation, dashboard config, research/lookups.
- **Skill Scan Declaration** required before spawning generic agents on triggered tasks.

---

## Files / artifacts to reference

| File | Purpose |
|---|---|
| `~/Desktop/metis-cortex/METIS-CORTEX-CODE-SESSION-BRIEF.md` | This brief — canonical reference |
| `~/Desktop/metis-cortex/METIS-CORTEX-V2-TRADING-SIGNALS-BRIEF-2026-05-21.md` | Original founding brief sent to reviewers |
| `~/Desktop/metis-cortex/STATUS.md` | Existing STATUS — needs reset to new direction |
| `~/Desktop/metis-cortex/PAIR.md` | Existing PAIR — header needs reset, log preserved as history |
| `~/Desktop/komiti/KOMITI-CODE-SESSION-BRIEF.md` | Sister venture brief — different brand, different posture |
| `~/.claude/CLAUDE.md` | Global protocol |
| `~/.claude/memory/businesses.md` | Cross-venture context |
| `~/.claude/memory/notion-sync.md` | Notion sync protocol |
| `~/.claude/memory/stripe-brand-convention.md` | Brand convention for shared trust Stripe account |
| `~/Desktop/exit-code/STATUS.md` | EXIT CODE state — sister brand, architecturally separate |

---

## What success looks like at end of Code session 1

Code's first session should produce:

1. ✅ Audit of existing Metis Cortex infrastructure (what to reset, what to reuse)
2. ✅ STATUS.md fully rewritten to reflect new trading-research direction
3. ✅ Memory mirror updated at `~/.claude/memory/metis-cortex-status.md`
4. ✅ PAIR.md header reset (log history preserved)
5. ✅ Stripe products audit (which to archive, which to create new)
6. ✅ Initial build sequence proposed in chat for Peter's greenlight

NOT in session 1:
- ❌ Don't actually rebuild the site yet (wait for Peter's greenlight)
- ❌ Don't deactivate Stripe products yet (audit first, decide together)
- ❌ Don't start pattern engine build (wait for foundation reset + greenlight)

---

## Honest context Peter wants Code to know

- Peter is committed to BOTH Komiti AND Metis Cortex as parallel ventures. Komiti is the primary financial bet (faster cash, lower regulatory risk). Metis Cortex is the longer-arc bet (higher ceiling, harder market).
- Capacity is the binding constraint — 6 active ventures against ~60 hrs/week realistic capacity. Code should optimise build for solo-operator-with-AI-leverage workflow, not for "perfect build."
- Architectural separation from EXIT CODE is intentional. The EXIT CODE editorial posture (pure educational, no real-time market intelligence) must be preserved.
- Prior Metis Cortex history (v1-v8 hospitality/agency framings) is dead. Brand + ASIC infrastructure are being repurposed, not the product direction. Strip all prior framings from STATUS.md.
- This is the hardest single market Peter has entered. Code should design for realistic 4-9 month timeline to MVP that earns its first paying customer — not the optimistic 12-16 week nominal estimate.

---

*Brief generated 2026-05-21 by Claude (Anthropic) at Peter's request. Canonical reference doc for the Metis Cortex repositioning. Last updated 2026-05-21 by Code in the originating session that produced both this and the Komiti brief.*