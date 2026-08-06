# METIS CORTEX — CONSOLIDATED ISSUE & RISK REGISTER (as at 2026-08-07)

Compiled from: STATUS.md (last ~10 entries), METIS-REDTEAM-LIVE-LAW-2026-06-26.md,
METIS-INCIDENT-RESPONSE-PLAN-2026-08-01.md, METIS-PUBLIC-CLAIMS-VERIFICATION-2026-08-01.md,
METIS-RECORDING-CONSENT-DECISION-SHEET-2026-08-01.md, METIS-SUBPROCESSOR-REGISTER-2026-08-01.md,
METIS-LAWYER-REVIEW-PACK-2026-08-01.md, app/CLAUDE.md, plus a codebase TODO/placeholder sweep.

Severity: **BLOCKER** = blocks real-client/real-firm use · HIGH · MED · LOW.
Status: open / mitigated / accepted-risk / closed-residual.

## A. Legal / Compliance

| # | Issue | Sev | Status |
|---|---|---|---|
| A1 | **s174 costs-disclosure wording not lawyer-reviewed** — the four client-rights statements are a literal `[LAWYER TO CONFIRM EXACT WORDING]` placeholder (`app/server/routers/consultation.ts:691`); no reviewer engaged (John meeting Mon 2026-08-10 is the live path) | BLOCKER | open |
| A2 | **s178 exposure** — non-compliant disclosure voids the costs agreement and blocks fee recovery; artefact unreviewed | HIGH | open (DRAFT banner + placeholder mitigate) |
| A3 | **s180 costs agreement** — unknown whether any part is prescribed statutory text; open question to reviewer | HIGH | open |
| A4 | **Case brief is the closest artefact to independent legal analysis (UPL)** — "not ready even under supervision" is a live possible reviewer answer | HIGH | open |
| A5 | **UPL: raw model produces advice-shaped output by default** — rails (`enforceRails()` + domain lock) survived adversarial tests, but rails are the product, not the model | HIGH | mitigated client-side; standing design constraint |
| A6 | **Recording consent: all 8 decision-sheet questions unanswered** (who consents, renewal, withdrawal/deletion, retention, Deepgram disclosure, privilege, prohibited settings, audit evidence) | BLOCKER (for recording) | open |
| A7 | **NSW SDA consent gate must never be automated** — human-click gate in place; policy recorded after one blocked attempt | MED | mitigated |
| A8 | **FCFCOA AI Practice Direction (29 May 2026)** — interaction with client conferences under NSW SDA unconfirmed | HIGH | open |
| A9 | **ToS / privacy policy never had a lawyer pass** (launch gate 4) | BLOCKER | open |
| A10 | **AU data-residency formal pass not done** (gate 3) — Sydney hosting in practice, but Anthropic processes matter content in the US; Resend stores email data in the US | BLOCKER | open |
| A11 | **APP compliance is "aligned with", not reviewed** — no formal Privacy Act review; NDB threshold judgment needs a real legal read | MED | open, hedged on-site |
| A12 | Client-ID data-minimisation call (no doc number/copy stored) unconfirmed by a lawyer | MED | open |
| A13 | Conflict-check record adequacy (ASCR rr10–12) unconfirmed by a lawyer | MED | open |
| A14 | Legaltech UPL/ToS review lane for the browser co-pilot concept never engaged (co-pilot unbuilt) | MED | open |
| A15 | **LEAP claims discipline** — nothing may be claimed as "integrates with LEAP"; paid reviewer ≠ "mutual client" | MED | mitigated (rules written into Monday doc + video) |
| A16 | Privacy Act small-business exemption removal (Dec 2026) — watch item | LOW | monitor |

## B. Technical / Product

| # | Issue | Sev | Status |
|---|---|---|---|
| B1 | **Client and solicitor sides are two separate, unbridged data models** — same real-world matter has no shared record. (Peter's solicitor-invites-client feature = the fix.) | HIGH | open |
| B2 | **No real conference has ever been recorded through the product** — pipeline proven only on pasted/synthetic transcripts | HIGH | open |
| B3 | **LEAP integration not built; registration stalled** — reply drafted, held for Monday PM; needs Peter's manual 4-word edit | HIGH | open |
| B4 | Deepgram configured but consent-gated; real audio untouched | MED | mitigated |
| B5 | Capabilities video says "Meaty" in 4 lines — do not send externally until re-rendered. Blocked on a new ElevenLabs `sk_` key (legacy hex keys are now rejected by their API). Video content is otherwise still accurate — verified 2026-08-07 that nothing in the narration was made false by the security work or the origin-story correction. | MED | open |
| B6 | Website-facing 60–90s client video cut not made | LOW | open |
| B7 | app/CLAUDE.md stale storage claim ("R2 in production" — actually local Fly volume + R2 backup) | LOW | open (doc drift) |
| B8 | No solicitor billing (deliberate; sales-led grants) — becomes work at firm #2 | LOW | accepted-risk |
| B9 | n08 narration "seventy seconds" nit — FIXED 2026-08-07 (claim cut from audio) | LOW | closed |
| B10 | HANDOFF-METIS.md listed the DSK phone number on the Metis owner line | LOW | **fixed 2026-08-07** |
| B11 | 5th outreach letter (Family Mediation NSW) never got the de-AI pass | LOW | open |
| B12 | Dormant Gemini fallback path with no key — update register if switched on | LOW | accepted-risk |

## C. Business / Operational

| # | Issue | Sev | Status |
|---|---|---|---|
| C1 | **PI insurance not in force** (gate 2); no cyber insurance or breach retainer either | BLOCKER | open |
| C2 | **Zero paying strangers, zero solicitor customers** — validation never run; standing decision: no more feature-building until 10 strangers pay | HIGH | open |
| C3 | **Single-founder / key-person risk** — Peter is the entire detection, response and continuity plan | HIGH | open |
| C4 | **John relationship is the critical path; he hates AI for legal work** — lead with refusals; video risky for him specifically; he is also the LEAP unlock | HIGH | mitigated (Monday doc) |
| C5 | **STATUS record reliability** — wrong twice about outreach state (Simon "SENT"; LEAP "not started"). Check Mail before trusting the log | MED | open (recurring process risk) |
| C6 | Outreach was cold-email-first (just failed with John); reworked call-first; DSK number found in signatures and fixed | MED | mitigated |
| C7 | Google Search Console — **claim was WRONG. Verified 2026-08-07: sitemap had already been submitted 4 Aug (Success, 30 pages). Domain property now added, ownership auto-verified via Cloudflare, sitemap resubmitted → 46 pages.** | MED | **closed 2026-08-07** |
| C8 | Socials stuck at Peter's final clicks; never automate Meta/LinkedIn (account restriction) | LOW | constraint accepted |
| C9 | Refunds honoured manually via Stripe dashboard | LOW | accepted-risk |
| C10 | No trademark registration (decision recorded: skip for now) | LOW | accepted-risk |
| C11 | STATUS structural sections frozen at 2026-06-18 while dated entries carry state | LOW | open (hygiene) |

## D. Data / Security

| # | Issue | Sev | Status |
|---|---|---|---|
| D1 | **No automated breach/intrusion detection, no monitoring** — one person checking manually; incident plan never rehearsed | HIGH | open |
| D2 | **No independent security audit or pen test** — disclosed, but real for a product holding family-violence and children's data | HIGH | open |
| D3 | **Subprocessor DPAs unconfirmed across the board** — Fly DPA TBC; Anthropic DPA TBC + **no ZDR (~30-day US retention of matter content)**; Resend TBC; register unpublished | HIGH | open |
| D4 | **PARTLY CLOSED 2026-08-07.** The extracted *text* of every document is now app-layer encrypted (AES-256-GCM), as are transcripts, case briefs, legal issues, proposals, chat and portal messages. The document **bytes** on the volume remain protected only by platform disk encryption. | MED | partly mitigated; residual disclosed |
| D5 | Single-machine local volume — mitigated by measured restore test (RTO ~30s, RPO ≤24h) + verified daily R2 mirror | MED | mitigated |
| D6 | HISTORY: storage writes on ephemeral FS for ~2 months (fixed 1 Aug, data recovered byte-verified) | MED | closed-residual |
| D7 | HISTORY: public pages exposed a real person's matter/claim numbers (fixed same day); public-claims pass not yet recurring practice | MED | closed-residual |
| D8 | Cross-tenant leak class bit twice — now tenancy-in-SQL everywhere, adversarially tested, test-pinned incl. the ZIP route | MED | mitigated |
| D9 | ElevenLabs key exposed in transcript (twice) — rotation forced anyway (legacy keys rejected); new sk_ key awaited | MED | open |
| D10 | Anthropic processes sensitive matter content in the US under standard retention — disclosed; no regional option confirmed | MED | open / disclosed |
| D11 | Auth perimeter (magic-link + ALLOWED_EMAILS + DEV_AUTH double-flag) solid but never externally audited | LOW | accepted-risk |

---

## Top 10 by severity

1. **A1/A2 — s174 wording + lawyer review of the five artefacts** (BLOCKER): the single gate that unlocks the solicitor side. Monday's ask.
2. **C1 — PI + cyber insurance not in force** (BLOCKER).
3. **A9 — ToS/privacy lawyer pass** (BLOCKER).
4. **A10 — AU data-residency formal pass** (BLOCKER): overseas AI processing is the hard part, not the Sydney hosting.
5. **A6/A8 — recording-consent decisions entirely open** (BLOCKER for recording).
6. **D3 — DPA/ZDR gap across subprocessors** (HIGH): most concrete paperwork hole under the stated privacy posture.
7. **B2 — no real conference ever run through the product** (HIGH).
8. **B1 — unbridged client/solicitor data models** (HIGH): Peter's invite-your-client feature is the fix.
9. **C3 + D1/D2 — single founder, no monitoring, no audit** (HIGH).
10. **C2 — zero customers** (HIGH): every risk above is carried for a product no stranger has paid for; Monday is simultaneously validation, lawyer-review and LEAP paths.

Cross-cutting: honest-disclosure discipline is strong, but **record reliability (C5) and doc drift (B7) have each failed more than once** — treat as a standing risk, not isolated slips.
