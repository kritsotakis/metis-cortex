# Metis Cortex — External Review Brief V2 (for Manus · Gemini · ChatGPT · Cowork)

**From:** Peter Kritsotakis
**Date:** 2026-06-01 (Monday evening, Sydney AEST)
**Supersedes:** [V1 brief 2026-05-29](./METIS-CORTEX-EXTERNAL-REVIEW-BRIEF.md). You can read V1 if you want full context, but this V2 is self-contained.
**Live site:** https://metiscortex.au

**Ask:** Two days ago you (the four of you collectively) gave me a sharp set of pressure-tests. I'm sending **Tuesday afternoon outreach to 6 NSW family-law Accredited Specialists**, and before I do, I want one more pass against the artifacts that have changed since V1. Be sceptical. Tell me what's off. Rank your top 3 concerns.

---

## What's changed since V1 (the 2026-05-29 brief)

### Direction confirmed, no further pivot

- **Single brand only.** I rejected my own "Iris" sub-brand idea last night after exploring it. Metis Cortex is the platform; "Metis" is the short form for the client-facing AI feature inside it. No separate domain (`meetiris.au` not registered). No spin-out.
- **Lane discipline locked.** Metis-side sessions are read-only against the live DPO matter folder; legal substance stays in the parallel child-support-stay sessions. I overstepped this lane Saturday night writing legal-content drafts into the matter folder and got correctly pushed back — corrected, banners on the offending drafts, memory rule locked, dashboard fixed.

### New artifacts since V1 review

All in `~/Desktop/metis-cortex/`:

1. **[`FOUNDING-FIRMS-OFFER-V1.md`](./FOUNDING-FIRMS-OFFER-V1.md)** — the Hormozi-rebuilt offer doc. Standalone Year-1 value stack of A$48,680+ vs A$8,400 paid (5.8× value-to-price). Structure C tiered pricing (Solo A$700/mo / Practice A$1,800/mo / Firm A$3,500/mo, locked for life). Two-headed guarantee. Real scarcity reason-why (5 firms × 10 hrs/mo founder = 50 hrs/mo cap). Honest "what we won't do" list. **This is what I'm sending Tuesday afternoon to 6 prospects.**

2. **[`WEEK-1-MOM-TEST-SEND-LIST-2026-06-01.md`](./WEEK-1-MOM-TEST-SEND-LIST-2026-06-01.md)** — 28-firm staged list filtered to top 7 (Accredited Specialist × Solo/Practice tier), site-verified tonight: 5 Solo + 2 Practice with channel breakdown. One firm (Southern Waters Legal) had a suspended domain and was removed → 6 firms remaining for Tuesday send.

3. **[`PHASE-1-SPRINT-KICKOFF-MONDAY.md`](./PHASE-1-SPRINT-KICKOFF-MONDAY.md)** — concrete sprint plan for the actual co-pilot build. 2-3 weeks. Uses my own live DPO matter as the test fixture (with appropriate lane discipline).

4. **[`METIS-CLIENT-AUTOMATION-RESEARCH-2026-05-31.md`](./METIS-CLIENT-AUTOMATION-RESEARCH-2026-05-31.md)** — corrected source-system matrix. The honest revision: **user-supervised co-pilot is viable** for ATO/CSAOnline/court portals (the pattern I personally proved last week with Claude driving authenticated sessions while I watched). Not "guided walkthrough only" as I initially over-conservatively framed. Banking via Basiq partner (A$0.50/user/mo) for the regulated CDR path.

5. **[`CLIENT-INTAKE-REFERENCE-2026-06-01.md`](./CLIENT-INTAKE-REFERENCE-2026-06-01.md)** — canonical AU family-law intake reference. Universal intake (LPUL ID + ASCR conflict + costs disclosure + mandatory FV screening) + 11 matter types with document tables + compliance artefacts (LPUL s174/s178 + Sewell v Zelden 10-element file note) + process gates (s60I FDR / pre-action / s71B/s90RI disclosure / time limits / urgency triggers).

6. **[`Metis Toolkit v0.1`](./prototypes/)** — 5 working CLI tools (matter_dashboard.py / consistency_checker.py / intake.py / four_doc_check.py / `metis` wrapper). Pattern-based, deterministic, sub-second. **I'm using these on my own live DPO matter right now** as the prototype validation. The 4-doc consistency checker is the slice the parallel DPO session explicitly asked for as "product-validation in real conditions."

### Site updates since V1

- **Site v2.1** deployed at metiscortex.au — Founder section with the 3-act story (6 yrs enterprise IT → 21 yrs Limani Seafood → 3 rounds of AU family law as the client), A$700/mo founding rate published in the Founding Firms program section.
- **Site v2.2** also deployed — added "For clients" section with early-access capture form. Honest amica.gov.au funnel-out ("For amicable separations, try amica.gov.au — it's free and government-backed. For everything they exclude, Metis is for you").

### What V1 said vs what I did

| V1 reviewer said | What I did |
|---|---|
| ChatGPT: moat is family-law cognition not transcription | Threaded into competitive teardown + offer doc; not commodified |
| Gemini: consent is NSW criminal compliance + subpoena trap | Added "Step 1: Walk the client through consent" to How-It-Works on site; consent workflow is the #1 product gate in Phase 1 build plan |
| Gemini: drop costs-disclosure feature | Removed from active product surface; deferred to Phase 3 IF demanded by paying customers |
| Manus: Smokeball Archie + AI Legal Assistant + Law Brief AI are the real competitors | Live competitive scan run Saturday; Law Brief AI verified doing the live-conference motion now in QLD; positioning shifted to "depth differentiators on top of contested space" not "uncontested wedge"; Amica framed as funnel-out for amicable matters |
| Cowork: founder credential is the unfakeable part | Founder section on site + medium-form founder copy threaded into outreach + offer doc opens with operator credentials |
| Cowork: don't claim "no one does this" | Multi-source rule locked in memory; current claim is narrower: "AustLII-live + family-law-current-law + audit-grade consent — uncontested as a combination" (verified) |

---

## The 6 questions for V2 (be sharp)

### Question 1 — The Hormozi-rebuilt offer

[`FOUNDING-FIRMS-OFFER-V1.md`](./FOUNDING-FIRMS-OFFER-V1.md) is what 6 Accredited Specialists will receive Tuesday afternoon. Read it cold.

- Does the value stack ring true or read as inflated? (A$48,680+ standalone vs A$8,400 paid = 5.8x)
- Is the two-headed guarantee structure asymmetrically expensive enough to be credible vs Law Brief AI's 90-day refund?
- Is the scarcity reason-why ("5 firms × 10 hrs/mo Peter = 50 hrs/mo cap") believable, or does it read as manufactured?
- Is "Standard rate locked for the LIFE of your account, never raises" too generous (caps revenue ceiling) or correct positioning for founding firms specifically?
- What objection from a sceptical Accredited Specialist haven't I pre-answered?

### Question 2 — Pricing structure inconsistency I'm sleeping on

- **Site v2.1 (deployed):** A$700/mo per solicitor, **pure per-seat**. A 3-person practice reads A$2,100/mo on the site.
- **Offer doc V1 (sending Tuesday):** **Structure C tiered** — Solo A$700, Practice A$1,800 flat, Firm A$3,500 flat. A 3-person practice reads A$1,800/mo in the email.

Two different prices for the same 3-person practice depending on where they look. Which is right?

- Structure C (tiered) is the only transparent per-firm pricing in the AU legaltech competitive set (verified Sat — AI Legal Assistant publishes 9 price points; Smokeball publishes per-seat 4 tiers; LEAP gates pricing; Law Brief AI uses "less than 2 billable hours per month").
- Should I patch the site Tuesday morning to "From A$700/mo per solicitor (per-firm tiered for 2+)"?
- Or keep the simpler per-seat anchor on site + let offer doc explain the tiered structure in the conversation?

### Question 3 — The send list

[`WEEK-1-MOM-TEST-SEND-LIST-2026-06-01.md`](./WEEK-1-MOM-TEST-SEND-LIST-2026-06-01.md) is the 6 (after site-verification removed Southern Waters Legal).

- Is the ranking sensible? (5 Solo Accredited Specialists before 1 Practice tier)
- The send sequence (Mon AM email × 4, Mon PM LinkedIn × 1, Tue phone × 2) was written for Mon — now Tuesday afternoon — is the channel mix still right?
- Pass threshold: 2-of-6 booking the 15-min call = strong; 1-of-6 = workable; 0-of-6 = revisit before Cohort B. Calibrated correctly?
- Is there a smarter way to think about replacing the removed Southern Waters slot — Cohort B substitution now or hold for next week?

### Question 4 — The lane discipline correction

I overstepped my own discipline Saturday night writing legal-content drafts into the live DPO matter folder. The parallel child-support-stay session correctly pushed back. Banners added to the offending drafts; memory rule locked; dashboard fixed. **Question: do you see any concerns with the "Metis reads matter folder, DPO session writes legal substance" split as a stable long-term operating pattern, or does it create new failure modes I'm not seeing?**

### Question 5 — Metis Toolkit v0.1 product slices

Five working tools in `~/Desktop/metis-cortex/prototypes/`:
- `matter_dashboard.py` (state-at-a-glance HTML)
- `consistency_checker.py` (all-fact cross-doc check, 729 facts / 148 distinct values on my matter)
- `intake.py` (PDF → categorise + extract + file)
- `four_doc_check.py` (structured 4-doc reconciliation across SA Response + FCFCOA Affidavit + Financial Statement + Bankruptcy SoA — 0 drift, 2 consistent, 19 single-source, 20 absent on my matter tonight)
- `metis` (CLI wrapper)

These are sub-second pattern-based tools I can run on my own matter NOW. Phase 1 sprint builds the production version with conversational interface + co-pilot browser automation.

- **Which slice would you prioritise extending next?** The DPO session called the 4-doc reconciliation "the highest-pain item" — I've shipped baseline; LLM-enhanced paraphrase detection ($327k ↔ $327,016) is the next leg.
- **Is there a slice I should have built instead?** Deadline cascade? Stakeholder follow-up registry? Auto DOCX regen?

### Question 6 — What have I missed entirely?

Same V1 question, asked again 60 hours later with everything above in context. The point is to surface things V1 missed because the artifacts didn't exist then.

---

## The honest stance

I'm not asking whether to send Tuesday — I am sending Tuesday afternoon. I want one more sceptical pass to:

1. **Catch any line in the offer doc I shouldn't say to a 25-year Accredited Specialist** (e.g. credibility-undercutting hyperbole, math that doesn't add up, scarcity that reads as manufactured)
2. **Resolve the site vs offer doc pricing inconsistency** with input from people who've seen both
3. **Pressure-test the lane discipline** with the kind of distance the parallel session can't give
4. **Surface anything I've missed** that's quietly load-bearing

Rank your top 3 concerns. Be specific. Tell me what you'd change before Tuesday afternoon.

---

## What V1 said that I'm holding to

- Validate before building more (10 Mom-Test interviews before compliance engine build) — still on
- Costs disclosure stays out of the active product surface
- Founder-credential lived experience is the unfakeable part — leaned into hard (site Founder section + offer doc opening + outreach opener)
- Mom-Test discipline applies to the Tuesday call (no pitch, ask about past behaviour, "what would you have to know to record?" not "would you record?")
- Pricing is a market question not a cost question (verified 93% gross margin headroom)
- Independent build, no acquisition pitches, supplement-not-partner positioning — locked in memory
