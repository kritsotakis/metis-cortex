# Phase 1 Sprint Kickoff — Metis Client (DPO Co-Pilot)

**Sprint start:** Monday 2026-06-02 morning · **Sprint end target:** Friday 2026-06-19 (~2.5 weeks) · **First user:** Peter (DPO matter) · **No third-party users until Phase 0 lawyer gate clears**

## Goal in one line

Ship a working user-supervised co-pilot that helps Peter finish his FCFCOA s.111C stay application this sprint, producing the artefacts that double as the Metis client-side product prototype.

## Why this scope

- Peter's child support harassment is creating real-time pressure → his matter must move this sprint
- The DPO matter is the literal source material for matter-template T1 (per CLIENT-INTAKE-REFERENCE-2026-06-01.md Section F)
- Building it as a real product for Peter (rather than a one-off automation) means the work compounds into the Phase 2 multi-tenant launch
- Zero third-party UPL exposure during build (Peter is the user) — Phase 0 lawyer gate doesn't block this sprint, only blocks public launch

## What ships in Phase 1

### M1 — Co-pilot browser automation runtime (~4-5 days)

- Chrome extension OR Playwright-supervised session pattern (decision Monday morning — extension preferred per the AUTOMATION-RESEARCH doc)
- Per-action audit log (every click, every download, with timestamp)
- Visible action narration in a side panel ("clicking Lodgments… downloading 2019-20 NOA… filing under Annexure C")
- Stop / undo controls
- Hard rails: NEVER auto-click form submits, payments, change-of-detail requests, or anything irreversible — surface for client confirmation
- Source-system adapters (Phase 1 set): myGov + ATO + CSAOnline + Commonwealth Courts Portal + ASIC Connect + AFSA

### M2 — DPO matter template engine (~3-4 days)

- T1 template per CLIENT-INTAKE-REFERENCE-2026-06-01.md Section F — fully spec'd, just needs to be coded
- Workflow state machine: triage → inventory → retrieve → process → critique → matter pack
- Reads document inventory from CLIENT-INTAKE-REFERENCE-2026-06-01.md as canonical source-of-truth
- Generates the 5 pre-requisite checklist for Peter's matter (DSK BAS, SA written confirmation, DPO copy, Tempe net proceeds, trust register figures)
- Per-pre-requisite: knows the source system, the retrieval method, the input format, and which affidavit paragraph(s) get updated

### M3 — Conversational interface (~3-4 days)

- Text-only for Phase 1 (voice deferred to Phase 2)
- React app (extending the existing Manus React/Vite/Tailwind codebase)
- Single page with chat + status panel + document panel
- LLM routing: Gemini Flash for fast classification, Claude Sonnet for drafting + critique passes
- UPL safe-harbour rails baked into system prompts (DRAFT watermarks, lawyer-flag forks, no opinion sentences without authority citation)

### M4 — Document processing pipeline (~3-4 days)

- PDF text extraction (text-layer) + Apple Vision OCR fallback (scanned) — same pattern Claude used on the original DPO matter (verified working)
- Structured field extraction from OCR'd PDFs via LLM (matter-type-aware prompts)
- Document classification → annexure assignment
- Encrypted-at-rest storage (R2 / local FS for single-user Phase 1)
- PII redaction-for-display in chat UI

### M5 — Adversarial critique re-runner (~2 days)

- Already specified in METIS-CLIENT-WORKFLOW-SPEC.md Stage 10 + proven during the original DPO redline pass
- Independent agent (different model, different system prompt) reviews assembled material
- Outputs the same structure as REDLINE-DPO-2026-05-27.md (F-numbered fixes)
- Auto-runs after each material input arrives + on-demand

### M6 — Matter Pack PDF generator (~2 days)

- Single PDF assembly: triage summary + document inventory + chronology + annexure schedule with cross-references + affidavit drafts + cover letters + adversarial-critique findings + open questions for solicitor
- Re-uses the python-docx pipeline from the original DPO matter (`filled/02_affidavit_FILLED.docx` etc.)
- Adds a PDF combine step that produces a JP-appointment-ready bundle

## What does NOT ship in Phase 1

- Banking via CDR (Basiq) — Phase 2
- Voice channel (Deepgram + Twilio) — Phase 2
- Multi-tenancy — Phase 2 (Peter is the only user in Phase 1)
- Email / cloud-storage OAuth adapters — Phase 2
- Other matter templates (T2-T5) — Phase 2-3
- B2C consumer surface at meetiris.au — decided 2026-05-31 NOT to do this; single-brand Metis Cortex only

## Monday morning — first 90 minutes

1. **Read the existing Manus codebase** (`~/Desktop/metis-cortex-app/`) for: existing legal knowledge base (already current-law per 2026-05-29 commit 6910a66), AustLII integration, LLM routing, React app structure
2. **Decide Chrome extension vs Playwright supervised session** for the co-pilot runtime — extension is preferred per AUTOMATION-RESEARCH doc but the existing app architecture may push us one way or the other
3. **Set up the M1 skeleton** — repo branch, basic extension manifest OR Playwright runner stub, action log data structure
4. **Run the FIRST co-pilot session against Peter's DPO matter** by end of day Monday — pick the easiest pre-requisite (probably AFSA bankruptcy status check) as the smoke test

## End-of-sprint demo (Fri 2026-06-19)

The demo is Peter's own matter being closed:
- All 5 outstanding pre-requisites done via the co-pilot
- Affidavit Paras 19, 24(a), 16, 23B v3, 23C regenerated and current
- Adversarial-critique pass passes ≥80% of the previous REDLINE findings (re-run on the updated material)
- Matter Pack PDF generated, JP-appointment-ready
- Peter books the JP appointment for the following week

The demo is also the validation: if the co-pilot pattern works for the most demanding possible user (Peter, with full domain knowledge, on a real urgent matter), it works for the next 10 founding clients.

## Phase 0 gate — runs in PARALLEL during the sprint (does NOT block Phase 1 for Peter, DOES block any third-party launch)

- Sydney legaltech lawyer 30-min consult — UPL safe-harbour + ToS interpretation for myGov + ATO + Services Australia co-pilot pattern. ~A$300-500. Peter books Monday or Tuesday.
- Lawcover initial conversation — PI position on Metis-assisted client work. Free intro call. Peter books.
- Output: a Phase-2-launch-readiness checklist saying what we can and can't promise to third-party clients

## After Phase 1 ships — Phase 2 kickoff window

- ~End June 2026
- Triggered by: Phase 1 demo passes + Phase 0 lawyer gate clears
- ~6-8 weeks per the AUTOMATION-RESEARCH doc
- Adds CDR banking (Basiq partner), voice channel, multi-tenancy, email/cloud adapters
- First founding clients onboard mid-August 2026

## Risks tracked

| Risk | Probability | Mitigation |
|---|---|---|
| ToS interpretation pushes back on co-pilot pattern for myGov / ATO / SA | medium | Phase 0 lawyer review explicitly asks this; fallback to step-by-step guided walkthrough |
| Chrome extension complexity > expected | medium | Pivot to Playwright supervised session by Tuesday EOD if extension is fighting back |
| Peter's bandwidth across 5 businesses + court matter | high | Sprint scope is intentionally narrow (T1 only, no third-party features); each milestone independently shippable |
| Legal knowledge base requires updates during the sprint as 2025-reform case law develops | low | Six-monthly review cadence per CLIENT-INTAKE-REFERENCE-2026-06-01.md; out of scope this sprint |
| Adversarial critique misses something material | medium | Run the critique on Peter's matter — he can spot what's missing better than anyone (he wrote it the first time around) |

## What's in the repo + ready for the sprint

- `~/Desktop/metis-cortex-app/` — Manus-built React + tRPC + Express + MySQL app, already migrated off Manus, legal knowledge base current to post-2024 parenting + post-June-2025 codified four-step
- `~/Desktop/child-support-stay-order/` — Peter's DPO matter source material (drafts, prior-application, REDLINE, PAIR.md) — Phase 1 first integration target
- `~/Desktop/metis-cortex/METIS-CLIENT-WORKFLOW-SPEC.md` — 12-stage workflow spec
- `~/Desktop/metis-cortex/CLIENT-INTAKE-REFERENCE-2026-06-01.md` — canonical document inventory by matter type
- `~/Desktop/metis-cortex/METIS-CLIENT-AUTOMATION-RESEARCH-2026-05-31.md` — co-pilot architecture + regulatory architecture
- `~/Desktop/metis-cortex/COMPETITIVE-TEARDOWN-2026-05-30.md` — what we're differentiating against
- `~/Desktop/metis-cortex/STATUS.md` — single source of truth for state + decisions

## Monday checklist (Peter)

- [ ] Confirm sprint start (this doc)
- [ ] Book Sydney legaltech lawyer consult (~A$300-500, 30 min, this week)
- [ ] Book Lawcover intro call (free, this week)
- [ ] Block 30 min Monday morning for co-pilot kickoff session
- [ ] Have myGov credentials ready (you log in, Metis drives)

## Monday checklist (Code / Claude)

- [ ] Read existing app codebase (`~/Desktop/metis-cortex-app/`) end-to-end
- [ ] Make Chrome-extension-vs-Playwright decision
- [ ] Set up M1 skeleton
- [ ] Run first co-pilot session on AFSA bankruptcy check as smoke test
- [ ] PAIR.md update at child-support-stay-order with sprint kickoff entry

---

*This document IS the sprint plan. Daily progress logged to STATUS decision log + PAIR.md at `~/Desktop/child-support-stay-order/`. Demo Friday 2026-06-19.*
