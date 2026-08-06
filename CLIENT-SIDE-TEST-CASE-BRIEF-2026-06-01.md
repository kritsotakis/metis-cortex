# Metis Cortex — Client-Side Test Case Brief

**From:** Peter (via the child-support-stay Code chat)
**To:** Metis Cortex code chat
**Date:** 2026-06-01
**Purpose:** Use Peter's own live multi-stream legal/financial matter as a test case to prototype the client-side of Metis Cortex.

> **Read once cold.** This brief is self-contained — you don't need the child-support-stay PAIR.md, but it's at `~/Desktop/child-support-stay-order/PAIR.md` if you want to look at the live coordination model in action.

---

## Why this is a useful test case

Metis Cortex's Pro tier is "done-for-you workflow automation for AU professional services." The accountant niche is the wedge. Accountants run **complex, multi-stakeholder, multi-deadline, multi-document matters for clients** — usually for tax, sometimes spanning ATO + bankruptcy + court + counsellor + ex-spouse + multiple businesses.

Peter has, right now, one of these matters playing out in real life — and it has the exact same shape as what an accountant client of Metis would manage:

- **4 parallel proceedings**, each with its own decision-maker
- **4 sets of documents** that must tell ONE consistent story
- **Hard deadlines** with cascading downstream consequences if missed
- **3 external professional stakeholders** (counsellor, accountant, ex-spouse via SA process)
- **Personal AND business financial disclosure** with high accuracy requirements

The matter is messy enough that nothing pre-built handles it. It's already being run via a 2-agent (Code + Cowork) workflow with a shared PAIR.md coordination log. **That working pattern is the prototype Metis can extract from.**

---

## Peter's situation in one paragraph

Peter is subject to a **Departure Prohibition Order** issued by Services Australia (Child Support) on 23 December 2024 because of child-support arrears. The arrears were calculated on a 2019-20 Adjusted Taxable Income that was inflated by a one-off capital gain from selling an investment property. His ordinary earning capacity is roughly $100k–$150k/year; the spike year was $327k. He lodged a Change of Assessment with Services Australia in April 2025 — they refused to consider periods more than 18 months old (s.98C limit) and directed him to obtain a court order. He is **self-represented**, preparing a Federal Circuit and Family Court of Australia (FCFCOA) application for s.112 leave + s.111C stay + DPO challenge. In parallel he is preparing a bankruptcy petition with his Wesley Mission financial counsellor. And as of 1 June 2026, his ex-partner has filed her *own* Change of Assessment against him (Reason 8B — earning capacity) with a 14-day response window. Plus there's been a recent restructure of family business interests to his mother because an undischarged bankrupt can't be a company director.

---

## The four parallel workflow streams

| # | Stream | Decision-maker | Document | Deadline |
|---|---|---|---|---|
| 1 | **FCFCOA stay + s.112 leave application** | Federal Court (Sydney Registry) | Initiating Application + Affidavit + Financial Statement + Financial Questionnaire + Annexures + Urgency Cover Letter | Self-imposed ASAP (DPO blocking overseas travel) |
| 2 | **Response to Sarah's Change of Assessment** | Services Australia (Child Support) | Written response + 6 months bank statements + Workcover details + P&L/balance sheet/depreciation for current + last 2 FY for all entities | **15 June 2026** (hard) |
| 3 | **Bankruptcy petition (debtor's)** | AFSA | Statement of Affairs + supporting docs | "A couple of months away" — being prepared by Alice Russell (Wesley) |
| 4 | **Administrative DPO revocation request** | Services Australia (Child Support Registrar) | Letter requesting s.72I revocation or s.72L DAC | Lodge concurrent with FCFCOA filing |

**Critical constraint:** the financial disclosure in all four streams must be consistent. Inconsistency = catastrophic credibility damage in any one of them, AND potential perjury/clawback exposure.

---

## The artifacts being managed (current state)

A working folder at `~/Desktop/child-support-stay-order/`:

```
PAIR.md                        — live coordination log (Code↔Cowork, 25 entries, auto-rendered header)
REDLINE-DPO-2026-05-27.md      — 6-item rework redline awaiting per-item Peter decisions
COWORK-BRIEF.md                — execution brief for the Cowork agent
prior-application/             — 20+ source PDFs from CSAOnline + ATO + Services Australia letters
  extracted/                   — text-extracted versions (Swift PDFKit + macOS Vision OCR)
  sa_documents_received_*.md   — synthesised fact extracts from incoming SA letters
  sa_sarah_coa_application_*.md — extract + analysis of Sarah's COA application
drafts/
  00_FILL_IN_CHECKLIST.md
  01_initiating_application_CONTENT.md   — content for FCFCOA Initiating Application
  02_affidavit.md                        — ~30-paragraph affidavit (current state on disk)
  03_covering_letter_services_australia.md
  04_cover_letter_urgency.md             — paragraph-numbered urgency letter (PD 3.25(b))
  05_email_alice_russell_bankruptcy_transfer.md  — email to financial counsellor
  06_sa_response_to_sarah_coa_2026-06-15.md      — (to be created)
filled/                        — DOCX files generated by Cowork from drafts/ via build_docs.py
annexures/                     — bundled supporting documents, alphabetised A through K
reference/
  supporting_research_*.md     — s.111C statutory text, DPO/DAC framework, case law
  procedure_and_urgency.md     — FCFCOA practice directions, urgent listing pathway
  case_law_research.md         — Gyselman, Aldridge & Keaton, Yathopoulos (verified status logged)
  adversarial_critique.md      — full 320-line "Sarah's lawyer" gap-audit
forms/                         — blank FCFCOA forms (Initiating App, Affidavit, FS, FQ)
factsheets/                    — Legal Aid NSW Factsheets 3 + 4 (for reference, not Legal Aid involvement)
```

That's the state of a single matter. About **45+ files**, including documents that the client (Peter) created, documents he received, draft work products, generated DOCX, research, and structured analyses.

---

## The coordination model that's actually working

Peter runs two AI agents in parallel:
- **Code** (Claude Code) — handles file edits, document drafting, legal research, agent spawning, source-truth markdown
- **Cowork** (Claude.ai Desktop with filesystem access) — handles DOCX generation, browser tasks (currently Control Chrome MCP since Kapture was uninstalled), email drafting, professional-service-style document polishing, calling out the human stakeholders (the accountant, Alice from Wesley, JPs)

They coordinate via an **append-only PAIR.md** in the matter folder. Latest entry's `Status` flag (🟢 done / 🟡 working / ⏸️ waiting-on-pair / 🔴 need-peter) tells the next agent (or Peter) where the ball is. An auto-rendered header at the top of PAIR.md gives a "what's the state right now" view: owner, blocked count, action queue, last touched, stale items.

Peter is NOT the message bus between the two agents. He only steps in when `🔴 need-peter` — for facts only he knows, decisions only he can make, or signatures only he can give.

**This pattern is the thing.** Replace "Peter" with "the accountant's client," replace "Code/Cowork" with "the accountant + Metis automation," and you have the Metis Cortex client-side experience.

---

## What's been working

- **Single source-of-truth folder** (matter on disk) that any session can land in cold and pick up from
- **Auto-rendered PAIR.md header** that shows state at a glance — "owner now," "stale," action queue, total entries
- **Append-only log** with structured Status flags — never lose context, never edit history
- **Markdown drafts as source-of-truth**; DOCX as generated artifact (build_docs.py) — easy to diff, easy to QA
- **Structured fact-extract files** for incoming letters (each new letter from SA gets a `_received_*.md` extract with verbatim quotes + analysis)
- **Cross-document consistency check** is currently a manual reconciliation (4-doc matrix) — this is the painful bit, see below
- **Adversarial-critique pre-filing audit** — playing the other side's lawyer to find weaknesses; output structured as critique items F4 / F14 / F16 etc., then redlined → drafts updated
- **Skill scan + PRE-TASK SCAN** discipline — every non-trivial task starts with declaration of matched skills + research gaps + plan, visible to the principal

---

## What's painful (the actual problems Metis client-side could solve)

1. **Cross-document consistency.** Four streams, ~10 documents, dozens of factual claims that must align. Currently a manual reconciliation. Drift happens silently. An automated "Sarah's QLD property — appears in 2 of 4 documents, should it be in all 4?" or "your 2019-20 ATI is stated as $327,016 in draft A and $327k in draft B — consistent" would prevent late-stage credibility damage.

2. **Multi-deadline cognitive load.** 15 June (SA response), ASAP-but-discretionary (FCFCOA filing), "a couple of months" (bankruptcy), parallel (DPO admin request). A unified timeline view with cascading "if you slip X, Y also slips" would be valuable.

3. **External stakeholder loop closure.** Email to Alice (financial counsellor), brief to accountant, request to Services Australia, process server engagement, JP appointment. Each is a separate communication that needs follow-up. Each has its own "I'm waiting on their answer to question X" state. Currently tracked ad hoc in PAIR.md prose. A structured "waiting-on" registry would help.

4. **Incoming document intake.** Every time Services Australia posts a letter, Peter scans it and emails it to himself, then drops it in `prior-application/`. The Code session then OCRs it, extracts facts, structures them, files an analysis. A client-facing "upload here, we handle the rest" pipeline would compress that loop.

5. **Status communication for the principal.** Peter wants to know: "what's the state of my matter right now, what's blocking, what do I have to do." The PAIR.md auto-header gives this at a glance for him — but the lift for a non-technical client would be a friendly portal view of the same data.

6. **Versioned drafts + DOCX regeneration.** Markdown → DOCX via build_docs.py works, but every time the markdown changes, someone has to regenerate the DOCX. Auto-regenerate-on-save (or on PAIR.md state transition) would close that gap.

---

## Test-case framing for Metis client-side

Treat Peter as the prototypical Metis client. He is:
- A small-business owner / sole trader
- With a complex personal matter that an accountant would touch (tax, business structures, bankruptcy, trust restructuring, ATO compliance)
- AND a complex non-tax-but-financial matter (family court, child support, DPO) that an accountant *also* gets dragged into
- Self-represented in the legal proceedings, professionally-counselled on the financial side

The Metis Pro service for this client would be:
- Centralised matter intake + document repository
- Automated cross-doc consistency checking (the highest-value automation here)
- Multi-deadline tracking dashboard
- External-stakeholder follow-up automation (auto-nudge the accountant, log Alice's responses, track JP/process server)
- Versioned source-of-truth drafts with auto-generated polished outputs
- Status communication layer (the "what's the state of my matter" view)

The Lite tier could be a stripped-down version: secure document upload + structured intake form + status dashboard + basic deadline reminders. No bespoke draft generation; that's the Pro upsell trigger.

---

## What to prototype against this case

Concrete things Metis code could build that Peter could test immediately on his real matter:

1. **Matter dashboard** that reads the on-disk folder (PAIR.md + drafts/ + annexures/) and renders a client-portal view: streams, deadlines, action items, recent activity
2. **Document consistency checker** — read the 4 streams' drafts, extract key claims (income figures, asset list, dates, party details), flag inconsistencies
3. **Deadline cascade visualisation** — show what slips if any individual deadline slips
4. **Incoming-document intake endpoint** — upload-a-scan → OCR → structured extract → file in the right folder + log to PAIR.md
5. **Stakeholder follow-up registry** — "you sent X to Y on date Z, no reply for N days; nudge?"
6. **Auto DOCX regeneration on markdown commit**

Each of those is a discrete prototype that delivers value on its own. If even ONE of them works for Peter's matter, that's product validation: it would obviously help an accountant client managing their own messy multi-stream tax/structure/compliance matter.

---

## How to use this brief

- **Don't try to solve Peter's legal matter** from this brief — Code + Cowork are handling that in the child-support-stay session.
- **Treat the matter as a fixture.** It's a live, real, complex client-side workflow. Anything Metis prototypes against it gets tested in real conditions immediately.
- **Pick a slice.** Don't try to build all of it. Pick the highest-value single thing (probably the matter dashboard OR the consistency checker) and prototype that against the existing on-disk matter folder.
- **Read `~/Desktop/child-support-stay-order/PAIR.md`** if you want to see the live coordination log — it shows what good two-agent coordination looks like in practice and is the closest existing thing to what Metis Pro tier would offer.

---

## Files referenced

- `~/Desktop/child-support-stay-order/PAIR.md` — live coordination log, auto-rendered header
- `~/Desktop/child-support-stay-order/drafts/*.md` — current draft state
- `~/Desktop/child-support-stay-order/prior-application/sa_*.md` — fact extracts from incoming letters
- `~/Desktop/child-support-stay-order/reference/adversarial_critique.md` — gap audit
- `~/Desktop/child-support-stay-order/REDLINE-DPO-2026-05-27.md` — redline of rework items awaiting Peter's decisions
