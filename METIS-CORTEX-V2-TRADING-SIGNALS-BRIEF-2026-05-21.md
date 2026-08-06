# Metis Cortex v2 — Strategic Direction Brief (Repositioning)

**For:** Gemini + ChatGPT + Manus + Cowork (clean-slate validation)
**From:** Peter Kritsotakis
**Date:** 2026-05-21 (Sydney)
**Decision under review:** Repurpose **Metis Cortex** from "AI consulting / hospitality" → **AI trading signals platform paired with EXIT CODE**?

---

## Pretext

I've spent 2 weeks running strategic analysis on Metis Cortex. After 9+ reframes, the lateral-thinking exercise surfaced a SEPARATE business (Komiti — NSW strata SaaS) that's now committed as its own venture (separate brief).

That freed Metis Cortex to be REPOSITIONED to a use that actually fits the brand:

- **Metis** = Greek titan of wisdom, strategy, counsel — exactly the right metaphor for trading
- **Cortex** = neural intelligence, pattern recognition — exactly the right metaphor for AI trade signal detection
- **EXIT CODE** = my existing trading-discipline software brand (Pine Script indicators + AI-voiceover course)

The repurposed pitch: Metis Cortex = AI signal identification ("when/what to trade") + EXIT CODE = trader discipline ("how to behave inside the trade and exit"). Two complementary products in one trading family.

I want you to pressure-test this clean-slate. The Metis Cortex brand + ASIC business name already exist; I'm not building from zero — I'm repurposing existing infrastructure to a product line that genuinely fits.

---

## My asset profile

**Background:**
- 6 years enterprise IT engineer (early 2000s)
- 21 years operating Limani Seafood Restaurant
- Currently building 5 ventures: DSK (cleaning), Eonia (clinic, pre-launch), HydraLab (chemistry), EXIT CODE (trading software), Komiti (NSW strata SaaS)
- Active trader personally — built EXIT CODE as anonymous discipline brand because I lived the trader-behaviour problem firsthand
- Sydney-based, solo operator, ~25-30 hrs/week max per venture

**Specific to Metis Cortex's commercial fit:**
- **EXIT CODE exists as a working product** with Pine Script indicators + course (9 modules, 45 lessons)
- I'm an actual trader with deep understanding of what signal services get wrong (too many alerts, no context, no discipline framework, churn-driven SaaS)
- Pine Script integration capability via EXIT CODE foundation
- Greek mythology brand family (Metis + Eonia + EXIT CODE's Operator Zero) signals a coherent operator-led intelligence brand

---

## What Metis Cortex v2 is

### One-line pitch

> **Metis Cortex — AI-identified trade setups for active traders. Pairs with EXIT CODE's discipline framework so you actually trade them properly.**

### Buyer

Active retail/prosumer traders:
- Trading 5-50+ times/month
- Already using TradingView (4M+ active subscribers globally)
- Pay A$50-300/mo for some combination of: signal services, indicators, courses, community
- Frustrated with high-noise signal services that flood Telegram/Discord with low-quality alerts
- Comfortable with technical analysis, want AI as an edge not as a crutch

**Initial market segmentation:**
- **Tier 1:** AU/NZ active retail traders trading ASX equities + crypto + forex
- **Tier 2 (month 6+):** Global TradingView users (English-speaking)
- **Tier 3:** EXIT CODE customer base (existing warm channel)

### Product (what the SaaS actually does)

**Core signal engine:**
1. **AI pattern recognition** across multiple timeframes (4H + Daily + Weekly) — momentum + mean reversion + breakout + breakdown setups
2. **Setup quality scoring** — each signal rated A/B/C based on confluence (technical + volume + market context + correlation)
3. **EXIT CODE integration** — every Metis Cortex signal flagged with corresponding EXIT CODE discipline rule (e.g., "B-grade momentum long: max 0.5R position, EXIT CODE Rule 7 applies")
4. **Multi-market coverage** — ASX 200 equities, top 50 cryptocurrencies, major forex pairs, ASX 200 indices
5. **Daily setup digest** — morning email with 3-5 highest-quality setups + risk parameters + EXIT CODE notes
6. **Alert system** — push notifications + Telegram for time-sensitive setups
7. **Pine Script overlay** — visual signal markers directly in TradingView (subscriber Pine indicator)

**NOT in scope:**
- Auto-trading / order execution
- Custom strategy backtesting
- News-driven event alerts
- Crypto leverage signals (regulatory + ethics)
- Penny stock or low-cap signals

### Pricing

- **A$79/mo standard** — daily signal digest, top 5 setups, Pine overlay
- **A$199/mo pro** — real-time alerts, all setups (15+/day), full EXIT CODE integration
- **A$499/mo elite** — pro + monthly 1:1 review call + EXIT CODE course included (bundled value)
- **EXIT CODE customers get 30% discount** (warm-channel incentive)

### Economics (Month 12 target)

| Tier mix | Subscribers | MRR |
|---|---|---|
| 150 standard × A$79 | A$11,850 | |
| 50 pro × A$199 | A$9,950 | |
| 10 elite × A$499 | A$4,990 | |
| **Total: 210 subs** | | **A$26,790/mo** |

**Sits inside Peter's A$15-30K MRR target window. Higher ceiling than Komiti's strata model because crypto+ASX trader market is larger than NSW strata.**

### Cost stack (per subscriber, AUD)

- Claude API tokens (signal generation): ~A$3-5/mo
- Market data feeds (ASX + crypto + forex): ~A$2-3/mo
- Stripe processing: ~A$2-6/mo
- Email + push delivery: ~A$0.50/mo
- **Per-subscriber COGS: ~A$8-15/mo**
- **Gross margin at A$79/mo standard: ~85%**
- **Gross margin at A$199/mo pro: ~92%**

### Tech stack (build complexity is the real risk)

- **Market data ingestion:** Alpaca + Tiingo + Polygon (or Yahoo for MVP) + Binance API (crypto)
- **Pattern recognition:** Claude API for context + custom Python signal engine + technical indicators library (ta-lib)
- **Backtesting + quality validation:** Backtrader / Vectorbt
- **Subscriber app:** Web app (Next.js) + iOS/Android push via Expo + Telegram bot
- **Pine Script overlay:** TradingView-published Pine indicator (auth-gated to subscribers)
- **Backend:** Cloudflare Workers / Hetzner VPS + Postgres

**Build time solo: 12-16 weeks for MVP.** Significantly longer than Komiti's 6-10 weeks because trading signal accuracy + market data reliability are hard problems.

---

## EXIT CODE × Metis Cortex integration

The differentiation play. Most signal services just spam alerts. Metis Cortex bundles every signal with:

1. **Position-sizing recommendation** based on EXIT CODE risk framework
2. **Discipline tag** — "This signal triggers EXIT CODE Rule 12 (mean reversion entry rules)"
3. **Exit framework reminder** — built-in stops + targets aligned to EXIT CODE methodology
4. **Behavioural pre-commit** — subscriber checks an "I will follow my exit plan" box before alert resolves

**Pitch:** "Signal services tell you when to enter. We tell you when to enter AND how to behave once you're in. Pairs with EXIT CODE."

This is the single defensible angle vs the 50+ other AI signal services flooding the market.

---

## 90-day execution plan

**Weeks 1–4: MVP build (technical heavy)**
- Build core signal engine (1 timeframe, ASX equities only) — proof of concept
- Backtest on 18 months of historical ASX data — must show >55% win rate before launch
- Build Pine Script overlay for TradingView
- Set up subscription billing (Stripe Payment Links)
- Email digest template

**Weeks 5–8: Closed beta**
- 10-20 EXIT CODE customers get free 30-day access in exchange for feedback + signal quality reporting
- Daily signal digest email starts going out
- Weekly tuning calls with beta users
- Refine signal quality + reduce false positive rate

**Weeks 9–12: Public launch**
- Open paid subscriptions at A$79/standard, A$199/pro, A$499/elite
- EXIT CODE customer email blast (30% discount code)
- ProductHunt / Indie Hackers launch
- TradingView script publication for organic discovery
- Q1 target: 30 paying subscribers = A$3,000-4,000 MRR

**Month 4+:** Add crypto coverage, expand to forex, add Telegram alerts, refine quality scoring.

---

## What's locked in (NOT up for debate)

- Brand name: Metis Cortex (already ASIC registered)
- Entity: Kritsotakis Family Trust (ABN 45 984 876 899)
- AUD pricing (year 1 AU-focused, expand globally year 2)
- EXIT CODE integration as core differentiator (NOT standalone signals)
- ASX + crypto + forex (NOT penny stocks, NOT options)
- Solo operator + AI leverage (no team hires until 100 paying subs)
- Subscription model — NOT trade copy services, NOT auto-trading

---

## What I need from you (pressure-test)

**1. Is the AI trading signals market actually buyable from a solo operator?** The market has 50+ existing competitors (TrendSpider, Trade Ideas, Benzinga, TraderLion, etc.). Is there room for a new entrant — or am I about to spend 4 months building MVP for a saturated market?

**2. Is "Metis Cortex + EXIT CODE bundle" a genuinely defensible positioning?** Most signal services are pure-signal. Does adding "discipline framework integration" actually differentiate, or is it complexity buyers don't want?

**3. Is the 6-figure-views-per-month TradingView community a realistic distribution channel?** Pine Script publication can get organic discovery — but most published scripts get drowned. Is this distribution real or aspirational?

**4. What's the regulatory exposure?** ASIC has tightened rules around "trade recommendations" and "financial advice" in 2025-2026. Do I need an AFSL? Can I get away with "educational signals, not advice"? What's the liability if a subscriber loses money following Metis Cortex signals?

**5. Is the 12-16 week build realistic, or am I underestimating?** Signal accuracy is genuinely hard. Market data reliability is genuinely hard. What's the most likely thing to break or take 3x longer than planned?

**6. Pricing — is A$79/standard / A$199/pro / A$499/elite right for AU retail traders?** Or should it be lower-volume / higher-priced? US-style pricing (US$30-100/mo) vs premium AU positioning?

**7. The Komiti vs Metis Cortex v2 tradeoff:** I'm committing to BOTH businesses but Komiti has lower technical risk (SaaS automation) and faster cash. Metis Cortex v2 has higher ceiling but longer build + signal accuracy risk. If you could only fund one — which?

**8. The $10K bet question:** If you had to bet $10K of your own money on Metis Cortex v2 hitting 200 paying subscribers within 12 months — what's the single biggest yes/no determinant?

---

## How to respond

Structure your response as:

1. **One-paragraph honest verdict** — is this market entry survivable as a solo operator?
2. **Strongest argument FOR** the Metis Cortex v2 reposition
3. **Strongest argument AGAINST** — what makes you think I should skip this
4. **Your $10K bet variable** — the single biggest yes/no determinant
5. **The one thing you'd change about the plan** — specific, actionable
6. **The blind spot you think I have** — direct

Be brutally honest. The Komiti commitment is locked; whether Metis Cortex v2 is the second venture or gets parked is genuinely on the table.

---

## Files for context (available on request)

- This brief (`METIS-CORTEX-V2-TRADING-SIGNALS-BRIEF-2026-05-21.md`)
- EXIT CODE current state — anonymous brand, Pine Script indicators + 9-module course
- Sister brief: `KOMITI-EXTERNAL-REVIEW-BRIEF-2026-05-21.md` (the other committed business)

---

*Brief generated 2026-05-21 by Claude (Anthropic) at Peter's request. Peter is committing to Komiti (separate brief) and considering Metis Cortex v2 (this brief) as second venture. Reviewers asked to provide standalone validation of the trading signals reposition, not to compare against earlier Metis Cortex v1-v8 hospitality/agency framings.*
