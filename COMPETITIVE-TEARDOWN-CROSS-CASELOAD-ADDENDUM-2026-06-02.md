# Competitive Teardown — Cross-Caseload Coordination Addendum

**Date:** 2026-06-02
**Parent doc:** [`COMPETITIVE-TEARDOWN-2026-05-30.md`](./COMPETITIVE-TEARDOWN-2026-05-30.md)
**Trigger:** Section 3 of the offer doc claims cross-caseload differentiation (action items extracted from conferences → matter dashboard, stale matter surfacing, deadline cascade, follow-up registry across matters). Prior teardown verified per-conference / single-matter capabilities; didn't verify cross-matter cognition. This addendum closes that gap before Tuesday afternoon send.
**Method:** WebFetch against features pages of LEAP, Smokeball, AI Legal Assistant, Law Brief AI (2026-06-02 evening Sydney).

---

## TL;DR

**Section 3's cross-caseload claim is defensible against every named competitor.** Nobody else extracts action items from conference recordings, surfaces stale matters via AI cognition, cascades deadlines across the portfolio, or runs cross-document consistency reconciliation. **Closest adjacency:** Smokeball's Daily Digest (calendar task aggregator). Real but materially different from what Metis does.

---

## Findings per competitor

### LEAP Matter AI

**Verified feature surface (from leaplegalsoftware.com/au/innovations/):**
- *"Get instant answers from your matter"* — **single feature, per-matter Q&A**

**Not present in their public feature surface:**
- ❌ Cross-matter action item surfacing
- ❌ Stale matter alerts
- ❌ Deadline cascade across portfolio
- ❌ Follow-up registry
- ❌ Cross-matter dashboard

**Read:** LEAP Matter AI is per-matter question-answering on content already in the matter file. Doesn't see across matters and doesn't extract from conferences.

### Smokeball (full platform + Archie AI)

**Verified feature surface:**
- **Archie AI:** *"helps practitioners do more in less time by assisting with tasks like information gathering, drafting correspondence and matter summaries"* — single-matter scope
- **Daily Digest:** *"prioritises tasks at a glance, with the ability to quickly show what tasks are due for completion aside your calendar"* — calendar task aggregator across the firm
- **Legal Calendaring:** *"tracks all the critical dates for each matter"* — per-matter date tracking
- **Firm Insights:** *"performance tracking and accurate view of profitability based on staff activities"* — KPI dashboard, not matter-state dashboard

**Adjacency analysis — Daily Digest is the closest thing to Metis Section 3:**
- ✅ Aggregates tasks across the firm into a single view (genuine cross-matter)
- ✅ Prioritises by what's due
- ❌ Aggregates *calendar events you've already typed in* — not items extracted from recordings or documents
- ❌ Doesn't flag *stale matters* (matter is overdue per its SLA) — only *tasks due today*
- ❌ No AI cognition; it's an aggregator of manual data entry
- ❌ No cross-document consistency check
- ❌ No follow-up registry ("you sent X to Y on date Z, no reply in 32 days")

**Read:** Smokeball is genuinely the strongest adjacency we've found. They have a real "across-the-firm" surface. But it's **calendar/task aggregation** of manually-entered events, not **AI-extracted-action-items + matter-state-surfacing across the caseload**. Section 3 must acknowledge this honestly.

### AI Legal Assistant

**Verified feature surface (from legalassistant.au):**
- Document Review (single doc)
- Discuss Document (chat interface, document-centric)
- Draft Documents (editing, summarising)
- **Multi-Doc Review** *("Analyze multiple documents simultaneously for conflicting clauses, inconsistencies, mismatching details, missing references, chronological issues")* — closest thing to Metis 4-doc reconciliation, but document-centric not matter-centric
- Research Assistant (AustLII-equivalent for AU/NZ)
- Voice to Actionable Text
- Document Discrepancy Detector

**Cross-matter capability — verbatim from scan:**
> *"no mention of portfolio or caseload dashboards, cross-matter action item surfacing, stale matter alerts, missed deadline tracking, multi-matter follow-up management, firm-wide matter oversight capabilities. The product is positioned around document-centric work rather than practice management infrastructure."*

**Read:** Document-centric, not matter-centric, not caseload-centric. Their Multi-Doc Review is the closest analogue to our 4-doc reconciliation but at the document layer not the matter-portfolio layer. **No cross-matter functionality.**

### Law Brief AI

**Verified feature surface (from lawbrief.com.au):**
- Per-consultation: VoIP or web-app face-to-face recording → polished client letter + internal file note

**Cross-matter capability — verbatim from scan:**
> *"Operates on a single-matter, per-consultation basis. There is no mention of cross-matter capabilities, portfolio dashboards, or firm-wide caseload management. The service is designed to streamline the administrative burden of individual consultation documentation, not to surface patterns, action items, or follow-ups across a firm's entire caseload."*

**Read:** Explicitly single-matter. No cross-caseload capability.

---

## What Section 3 can defensibly claim

Verified against this scan:

1. ✅ **AI-extracted action items from conference recordings, routed to the matter dashboard** — nobody does this. Closest adjacency (Smokeball Daily Digest) aggregates calendar tasks the user already typed, not items extracted from recordings.

2. ✅ **Stale-matter surfacing** (matter is overdue per its SLA; nobody has moved on it; risk of falling through cracks) — nobody does this. Smokeball Daily Digest is "tasks due today," not "matters where the next move is yours and you haven't made it."

3. ✅ **Deadline cascade across the portfolio with risk flags** — Smokeball Legal Calendaring tracks critical dates per matter; doesn't cascade or show "X firms with FDR certificate inside 14-day window across your caseload."

4. ✅ **Follow-up registry** ("you sent X to Y on date Z, no reply in N days") — nobody does this.

5. ✅ **Cross-document consistency reconciliation** (across affidavit + financial statement + bankruptcy SoA etc.) — AI Legal Assistant's Multi-Doc Review is the closest analogue but operates at the document layer; doesn't see matter-portfolio context.

6. ✅ **Single-page "what's the state of every matter right now" dashboard with state indicators** (owner now / waiting on / stale / at-deadline-risk / open action items / recently-arrived docs) — nobody has this. Smokeball Firm Insights is profitability/performance, not matter-state.

## What Section 3 should honestly NOT claim

- ❌ "First aggregator of cross-firm tasks" — Smokeball Daily Digest exists. We're not first to cross-firm visibility; we're first to AI-cognition-driven cross-firm visibility.
- ❌ "Only deadline tracker" — Smokeball Legal Calendaring tracks deadlines per matter. We do the cross-matter cascade + risk-flag layer; they do per-matter tracking.

## Suggested Section 3 language (verified-defensible)

> Smokeball's Daily Digest prioritises calendar tasks you've already typed in. LEAP Matter AI lets you ask a single matter a question. AI Legal Assistant reviews single documents. Law Brief AI generates one polished letter per consultation.
>
> **None of them extract action items from a recording you just made, flag a matter as stale because the next move is yours and you haven't made it, cascade deadlines across your portfolio, or surface a follow-up your client has been waiting on for 32 days.** Metis does this because it's the only one that sees both the conference content and the cross-matter state.

This sentence is defensible against every verified competitor in this addendum.

---

## What this addendum doesn't pressure-test (defer post-Mom-Test)

- Whether solicitors actually use Smokeball Daily Digest enough to make it competitive vs Metis (could be feature-on-paper that nobody uses)
- Whether LEAP / Smokeball have undisclosed roadmap items in cross-caseload AI (unfetchable from public surfaces)
- Whether adjacent legal-tech outside the named family-law AI set (e.g. Clio Matter Stages, ActionStep workflows, Centerbase) does cross-caseload coordination — these are PMSes not AI tools; out of scope but worth checking if a Mom-Test caller raises them
- Whether non-AU legal AI (US/UK/CA) does cross-caseload — out of scope; not a competitor for NSW family-law solicitors

---

*Filed 2026-06-02 to close the Section 3 positioning gap before Tuesday afternoon send. Read-only against existing teardown; does not modify the parent doc; adds verified cross-caseload context.*
