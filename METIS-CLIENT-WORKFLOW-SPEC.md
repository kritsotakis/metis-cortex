# Metis Client — Workflow Specification

**Date:** 2026-05-30 (single-brand naming decision 2026-05-31 — client-facing surface is "Metis" inside Metis Cortex; no separate sub-brand)
**Source material:** Peter Kritsotakis's three rounds in AU family law (divorce, child/family matters, current FCFCOA DPO stay application). The DPO matter at `~/Desktop/child-support-stay-order/` is the **prototype** — every workflow stage below maps to something Claude actually did during that matter.
**Status:** Working spec. NOT a build go-ahead. Build is gated behind solicitor-side Mom-Test signal (`MOM-TEST-SCRIPT-V2-2026-05-30.md`) AND a multi-source competitive scan of AU client-side family-law tools.

## The client-facing interface is **Metis** — conversational AI inside Metis Cortex

**Decision 2026-05-31 (final, supersedes the "Iris" naming proposed earlier same day):** the client-facing surface is a conversational AI named simply **Metis** — the short form of the parent brand. Text + voice channels. The 12-stage workflow below becomes the *back-end logic* Metis (the client-facing surface) executes; the *interface* is dialogue, not a form.

**Naming hierarchy (locked):**
- **Metis Cortex** = the full platform / product / company. Used in marketing, sales, solicitor-facing UI, contracts, legal docs.
- **Metis** (short form) = the client-facing assistance feature. Used when referring to the client's interaction surface. *"Have your client talk to Metis before our conference."*
- **No separate sub-brand** for the client-facing AI. Earlier proposals (Iris, Zoe, Athena) all rejected in favour of single-brand discipline — one brand to build/market/defend, no Year-2 spin-out overhead, no domain cluster to register, no fragmentation risk.

**Why conversational over form-based:**
- Family-law clients at the worst point of their life don't navigate workflow apps; they will talk to a patient AI that asks one question at a time
- It's how Claude actually helped Peter on the DPO matter — conversation, not a form
- Chat layer is the cheapest UI to build (wraps existing back-end)
- Voice channel falls out naturally (clients who can't sit at a laptop)
- UPL guardrails are *easier* in conversation (Metis can naturally interrupt with *"this next call is a legal question — I'll flag it for your solicitor"*)

---

## Why this exists

Three rounds of AU family-law process (divorce, child/family matters, DPO + s.111C stay) demonstrated that the *client side* of a family-law matter carries a documentation burden that's roughly equal to — and often higher than — the solicitor's drafting burden. The client has to:

- Find, retrieve, and organize documents from at least 6 separate systems (myGov/ATO, CSAOnline/Services Australia, bank/super portals, email archives, paper files, court portals)
- Build a defensible chronology that crosses tax years, custody changes, and procedural milestones
- Disclose assets they barely understand (trusts, bankruptcy interests, shareholdings, super splits)
- Make strategic decisions (stay-only vs interlocutory, settlement vs litigation) without legal training
- Resist the urge to draft narrative paragraphs that self-incriminate, support the opposing party's case, or invite contempt findings

Most clients don't do this well. **The ones who do, do it the way Claude did it for Peter on the DPO matter.** That workflow is the product.

Metis Client is the client-facing extension of Metis Cortex: same underlying engine (Australian legal cognition, AustLII research, AU data residency, family-law-current-law discipline), different surface and different safe-harbour architecture for an unqualified user.

---

## Positioning vs. the solicitor-side product

| | Metis Cortex (solicitor) | Metis Client (client / pre-engagement / self-rep) |
|---|---|---|
| **Primary user** | Admitted legal practitioner | Family-law client or self-rep litigant |
| **Trigger event** | Client conference / consult | Client receives a letter, notice, change of assessment, court date, or DPO |
| **Core JTBD** | "Capture the conference and draft the file note + brief + proposal before I leave the room" | "Help me find what I need, organize it the way a court expects, and walk into the solicitor's office (or the registry) with a matter pack the lawyer can immediately use" |
| **Output** | File note, case brief, client proposal, client portal | Document inventory, chronology, annexure schedule, draft affidavit, asset/liability schedule, cover letters, adversarial-critique pass, solicitor-handoff package |
| **UPL posture** | Tool for admitted practitioner — lawyer reviews everything | Tool for unqualified user — every output flags strategic decisions back to lawyer; never tells client what to do |
| **Pricing** | A$600-1,500/mo per solicitor (founding rate) | Per-matter (A$199-499 one-off) OR free + solicitor-referred bundle |
| **Distribution** | Direct sales to NSW family-law sole/micro | Two-sided: (a) solicitor referral ("get your docs in order before our consult"), (b) self-rep direct via FCFCOA registry / Legal Aid NSW referral / community legal centre referral |

**Strategic framing:** Metis isn't "AI for solicitors" — it sits in the middle, between the client preparing the matter and the solicitor recording the conference. The matter flows through it. That two-sided architecture is the long-term defensible moat, but only after the solicitor side validates.

---

## The 12-stage client workflow (mapped from the DPO matter)

Each stage corresponds to something Claude actually produced in `~/Desktop/child-support-stay-order/`. The stage number, the artefact, and the file path are the proof.

### Stage 1 — Matter triage + jurisdiction lock

**What happens:** Client describes their situation in plain language. Metis Client identifies the matter family (divorce, parenting, property, child support, DPO/CGT, change of assessment, FV/AVO, urgency triggers) and the correct procedural framework (FCFCOA initiating application, Services Australia administrative process, mediation/FDR, etc.).

**DPO prototype proof:** Peter described the inflated 2019-20 ATI driven by the Tempe sale + the DPO blocking travel + the rejected Reason 8A change of assessment. Claude triaged to: "FCFCOA Sydney application for s.111C *Child Support (Registration and Collection) Act 1988* stay order with DPO lift as ancillary."

**UPL gate:** Metis Client *suggests* the framework, *flags alternatives*, and *recommends a Legal Aid duty-lawyer / community legal centre consult* before final commitment to a procedural path. Never makes the strategic call alone.

### Stage 2 — Document inventory generation

**What happens:** Based on matter type, Metis Client generates the exact document checklist needed. Categorised by source system (myGov/ATO, CSAOnline, bank, email, paper, court portal) with retrieval instructions per source.

**DPO prototype proof:** `drafts/00_FILL_IN_CHECKLIST.md` — 8 categories: income/tax figures (6 Notices of Assessment + 2019-20 CGT component), party addresses, care arrangement change date, SA written rejection, DPO copy, CRN, proposed interim rate, occupation line.

**Differentiator:** the checklist is *matter-specific* (DPO stay needs ATI history + DPO copy + CRN; parenting matter needs school enrolments + Medicare records + s60I/FDR certificate; property matter needs disclosure schedule + bank statements + super splits). One checklist template per matter family.

### Stage 3 — Document retrieval assistance

**What happens:** Step-by-step guides for pulling documents from each source (with screenshots / video walkthroughs):
- myGov → ATO → Tax → Lodgments → download N years of Notices of Assessment
- CSAOnline → Activity History → download all correspondence
- MyGov → Centrelink/Services Australia → letters
- Bank portals → date-range statement export
- ScreenshotsApple/Mail.app → email export to PDF

**DPO prototype proof:** Peter pulled 18 prior-application PDFs from CSAOnline. Claude organised the workflow — what to download, what to save, where to drop.

### Stage 4 — Document extraction + OCR

**What happens:** Text-layer PDFs are extracted; scanned PDFs are OCR'd. Output is structured (date, sender, recipient, subject, content type).

**DPO prototype proof:** Of 18 PDFs, 11 had text layer (PDFKit extract), 7 were scanned (Vision OCR). Output saved to `prior-application/extracted/`.

**Tech:** macOS PDFKit + Vision works for the prototype. For production, Apple Vision / Google Vision / Azure Cognitive Services. AU data residency = mandatory.

### Stage 5 — Annexure schedule construction

**What happens:** Documents categorised into a court-expected annexure scheme (Annexures A, B, C... K). Each annexure has a label, a description, and cross-references to the affidavit paragraphs that cite it.

**DPO prototype proof:** Annexures A-K in `drafts/02_affidavit.md` annexure schedule. Each one cross-references the body paragraphs (e.g. Annexure C = 7 Notices of Assessment, cited in paras 11 + 12(a)-(e)).

**UPL gate:** Metis Client constructs the *physical* annexure schedule; whether each document is *evidentially admissible* and whether the *cross-references survive cross-examination* is a solicitor question, flagged in the output.

### Stage 6 — Chronology generation

**What happens:** Date-ordered timeline of every relevant fact + every document. Surfaces gaps (missing periods), conflicts (date discrepancies between documents), and statutory windows (12-month post-divorce property limitation, 2-year de facto limit, 18-month change-of-assessment limit).

**DPO prototype proof:** The affidavit's chronological structure across Sections D (the 2019-20 financial year + Tempe sale), E (procedural history), F (current financial circumstances), G (reasons for delay), H (hardship).

### Stage 7 — Asset / liability schedule (property matters)

**What happens:** Auto-builds a draft schedule from bank statements, super statements, real-property records, vehicle registrations. Flags missing entries (trusts, shareholdings, partially-paid shares, loans receivable/payable).

**DPO prototype proof:** Peter's Kritsotakis Family Trust beneficial interest + Kritsotakis Investments Pty Ltd 100 partially-paid ordinary shares + $80K Jim/Karren loan = three asset entries that nearly didn't make it onto the financial statement. Critique item E7 caught it.

**UPL gate:** the *categorisation* (trust = discretionary beneficiary vs controlling capacity; shares = partially-paid vs fully-paid; loan = recoverable vs gift) is a legal question. Metis Client surfaces the entries + the categorisation options + the consequences of each; the client + solicitor pick.

### Stage 8 — Draft affidavit / draft application drafting

**What happens:** Structured paragraphs cross-referenced to annexures. Section-by-section scaffold (parties → existing orders → current circumstances → procedural history → financial circumstances → reasons for delay → hardship → matter to be stayed → service → relief sought). Matter-specific templates per matter family.

**DPO prototype proof:** `drafts/02_affidavit.md` — 27-paragraph affidavit, 11 sections, full annexure schedule, jurat block. `drafts/01_initiating_application_CONTENT.md` — 5 orders sought. `drafts/03_covering_letter_services_australia.md` + `drafts/04_cover_letter_urgency.md`.

**UPL gate:** every paragraph marked **DRAFT — FOR REVIEW BY YOUR SOLICITOR**. Every strategic choice (Order 3 wording, s.111C vs s.112 framing, dissipation narrative wording) flagged with "this is the trade-off — pick with your lawyer" call-outs.

### Stage 9 — Cover letter generation

**What happens:** Cover letters to Services Australia, FCFCOA registry, opposing party, solicitor.

**DPO prototype proof:** 3 cover letters drafted (`drafts/03_*.md`, `drafts/04_*.md`, `drafts/05_*.md`).

### Stage 10 — Adversarial-critique pass

**What happens:** Independent AI agent (different model, different system prompt) reads the entire pack and writes the case for the **opposing party**. Surfaces:
- Counter-arguments the opposing solicitor will raise (ranked)
- Paragraph-by-paragraph weakness audit
- Self-incrimination risks
- Contempt-headline risks (e.g. Peter's $50/week proposed payment looked like contempt)
- Compliance landmines (undisclosed trust, hearsay basis for jurisdiction, undeclared income admissions)
- Strategic exposures
- Credibility risks
- Recommended fixes numbered W1-WN

**DPO prototype proof:** `reference/adversarial_critique.md` (320 lines). Surfaced 30+ items, 5 of which were 🔴 CRITICAL and produced the `REDLINE-DPO-2026-05-27.md` rework.

**This is the single most valuable thing Metis Client can do for a client.** Most clients arrive at a solicitor's office with a narrative they've polished in their head; the solicitor's first 30 minutes is undoing the parts that hurt the case. The adversarial-critique pass surfaces those parts to the client *before* the solicitor sees them, so the consult starts from a stronger position.

**UPL gate:** the critique is framed as *"things to discuss with your solicitor before they're surprised"* — not as *"do these things."* Strategic choices stay with the lawyer.

### Stage 11 — Strategy options surface

**What happens:** For every fork in the matter, the client is shown:
- The options (e.g. stay-only vs s.112 leave-up-front)
- The trade-offs in plain language
- Which choice is most consistent with the documentation gathered
- The flagged recommendation that this is a *legal* call, not a documentation call

**DPO prototype proof:** Peter chose stay-only (s.111C alone, no s.112 leave up front) on Services Australia's direction. Claude documented the choice + the alternative + the reasoning, but never made the call.

### Stage 12 — Solicitor handoff package (the Matter Pack)

**What happens:** Single PDF (or shared portal link) the client brings to the first solicitor consult containing:
1. Triage summary (matter type + procedural framework + urgency)
2. Document inventory (what's gathered, what's pending, source per document)
3. Chronology
4. Asset/liability schedule (if property matter)
5. Annexure schedule with cross-references
6. Draft affidavit / application (marked DRAFT — FOR YOUR REVIEW)
7. Cover letters
8. Adversarial-critique findings
9. Strategy options + the client's tentative call (and why)
10. Open questions the client wants the solicitor to answer

**The pitch to solicitors becomes:** "a Metis-prepared client arrives with their matter already structured into the 12-stage pack. Your first consult goes from 'what's happening?' to 'here's my read on what they've done, and here's the plan' in 15 minutes instead of 90."

**The pitch to clients becomes:** "you walk into the solicitor's office with the matter pack instead of a shoebox. The first 30 minutes you would have spent describing your situation are now the 30 minutes the solicitor spends planning your case."

---

## Matter-type templates (Year-1 minimum viable set)

Each template is a specialisation of the 12 stages — different document inventory, different affidavit scaffold, different critique heuristics.

| Template | Matter family | Primary statute / process | Build priority |
|---|---|---|---|
| **T1 — Child support stay (s.111C)** | DPO + inflated assessment | CSRC Act s.111C + s.72D | 🥇 First — Peter's DPO matter is the literal prototype |
| **T2 — Change of assessment** | Reason 8A / 8B / 1-10 grounds | CSA Act Part 6A | 🥈 Second — Peter went through this in 2025 |
| **T3 — Parenting orders** | Care arrangements + best-interests | FLA s60CC (post-2024) + s60I FDR cert | 🥉 Third — covers majority of family-law matters |
| **T4 — Property settlement** | Asset pool / four-step | FLA Part VIII (post-June-2025 codified four-step) | Fourth — overlaps with T1 disclosure work |
| **T5 — Initial consult prep (matter-agnostic)** | "I have a first appointment Friday, what should I bring?" | Universal | Fifth — low-cost, high-volume entry point |

Templates T6+ (divorce filing, FV/AVO support, recovery orders, child abduction) deferred to Year-2.

---

## UPL safe-harbour architecture (what the AI says vs. never says)

This is the hardest part of the build. Get this wrong and the product is an Unauthorised Legal Practice claim away from extinction.

| Allowed | Not allowed |
|---|---|
| "The DPO is issued under s.72D of the CSRC Act." | "Section 72D means you can definitely lift the DPO with a stay order." |
| "Here are the documents that affidavits in similar matters typically attach." | "These documents will be sufficient for your matter." |
| "The opposing party's solicitor is likely to argue X (here's why)." | "You should respond to X by saying Y." |
| "These figures don't reconcile across documents — discuss with your solicitor." | "The reconciliation should be done by Z." |
| "This paragraph creates a self-incrimination risk because…" | "Remove this paragraph." |
| "A duty-lawyer consult through Legal Aid NSW is available at 1800 451 784." | (Refer them to a *specific* lawyer Metis benefits from referring to.) |

**Mandatory output gates:**
1. **Every document carries a "DRAFT — FOR REVIEW BY YOUR SOLICITOR" watermark.**
2. **Strategic decision points** trigger an explicit "this is a legal call, not a documentation call — book a duty-lawyer consult before finalising" interruption.
3. **No prediction of outcomes.** Metis Client never says "you will win" / "you will lose" / "this is likely to succeed."
4. **No representation in proceedings.** Metis Client doesn't draft anything that purports to be a *final* legal document; only DRAFTs.
5. **Automatic disclaimer in every export:** Metis Client is a document-organisation tool. It is not a law firm and does not provide legal advice. Strategic and substantive legal decisions require a qualified solicitor.

**Pre-launch legal sign-off required:**
- A Sydney privacy/legaltech lawyer reviews the UPL architecture before public launch
- Engagement with Lawcover (PI insurance) to understand how Metis Client output is treated in disciplinary / negligence proceedings
- Map the safe-harbour against Legal Profession Uniform Law (NSW) ss.10-11 (definition of legal practice) + Australian Solicitors' Conduct Rules

---

## Integration with the solicitor side

The two products share one back-end. The matter flows:

```
Client opens matter on Metis Client
     ↓
12-stage workflow produces Matter Pack
     ↓
Client books solicitor consult
     ↓
Solicitor opens client's matter on Metis Cortex
     ↓
Conference recorded (with consent) — Metis Cortex captures
     ↓
File note + case brief + proposal drafted
     ↓
Client receives via the same portal
     ↓
Client uses Metis Client for any document gathering during the matter
     ↓
Solicitor uses Metis Cortex for every subsequent conference
```

**Same client portal, same matter ID, same audit trail.** This is the architectural reason client-side isn't a separate product — it's the *client view* of the matter that Metis Cortex already supports (existing `ClientPortal.tsx` + `clientPortalTokens` + `portalDocuments` + `actionItems` + `portalMessages` tables per the Manus handoff).

---

## What's reusable from the existing app (built by Manus, on disk now)

- `client/src/pages/ClientPortal.tsx` — client-facing matter portal
- `clientPortalTokens` table — single-use passwordless client access
- `portalDocuments` table — document upload + management
- `actionItems` table — task tracking with deadlines
- `portalMessages` table — secure in-app messaging
- `caseMilestones` table — matter timeline
- `legalKnowledge.ts` — Australian statutes + cases (already current-law for family law per 2026-05-29 commit 6910a66)
- `austlii.ts` — live AustLII search
- Magic-link auth — already replaces Manus OAuth (Cowork-Code work 2026-05-28)
- Deepgram transcription — already configured (for the few interview-style document-source elicitations)

**What needs to be built net-new (for Year-1 MVP T1 template):**
- Document inventory checklist generator (matter-type → checklist mapping)
- Source-system retrieval guide (per-source step-by-step playbooks)
- PDF text extraction + OCR pipeline (existing app has Whisper audio transcription; doesn't have PDF OCR yet)
- Annexure schedule builder (UI for drag-drop categorisation)
- Chronology generator (timeline from document metadata + content)
- Adversarial-critique agent (different model, different system prompt, dedicated UPL safe-harbour rails)
- Matter Pack PDF export (templated single-document output)

**Estimate:** 4-6 weeks of focused build for T1 (DPO stay) MVP, assuming the solicitor-side validation gate has cleared. Less if Peter's DPO matter artefacts become the seed data (they should).

---

## Build sequencing (gated)

### Phase 0 — Validate (NOW)
- ✅ **Multi-source competitive scan complete (2026-05-30)** — see "Competitive landscape" section below
- Add the "Metis-prepared client" probe to Mom-Test pack v2 → ask solicitors directly whether they'd refer prospects to Metis Client, or whether they'd see it as a threat
- Confirm UPL architecture with a Sydney privacy/legaltech lawyer (30-min consult, ~A$300-500) before *any* public claim about client-side

### Phase 1 — Build narrow (Q1 after solicitor wedge proves)
- T1 (DPO stay) MVP only
- Use Peter's DPO matter as the seed data + the first end-to-end test
- 5 self-rep DPO-affected clients (Legal Aid NSW referral network is the natural recruiting channel) as Phase 1 beta
- KPI: 5 of 5 produce a Matter Pack that a Legal Aid duty-lawyer rates "usable" or better in a 30-min review

### Phase 2 — Expand (Q2-Q3)
- T2 (change of assessment) + T3 (parenting orders) + T5 (initial consult prep)
- Solicitor referral channel opens (every Metis Cortex solicitor gets a referral link)

### Phase 3 — Two-sided scale (Q4+)
- T4 (property settlement)
- Community legal centre + Legal Aid NSW partnership conversations
- Self-rep volume play

---

## Competitive landscape (verified 2026-05-30 — multi-source scan)

Three direct candidates checked. None occupy the same wedge as Metis Client. The two that exist are *complementary* (Amica) or *adjacent on the wrong side* (Settify, solicitor-facing).

### Amica (amica.gov.au)

- **Operator:** National Legal Aid + Portable (Australian Government-backed)
- **Cost:** Free
- **Traction:** 17,000+ matters registered · 8,000+ asset divisions · 2,000+ parenting/property agreements · "$80M+ saved the courts in out-of-court agreements"
- **What it does:** DIY self-help for *amicable* separating couples. Produces an *agreement* (parenting arrangements + property division)
- **What it explicitly DOESN'T do (verbatim from site):** "**not suitable for contested separations or family violence situations**"
- **Excluded matter types:** child support (DPO, change of assessment, stay orders, s.111C), contested orders, FV/coercive control, anything needing a court document instead of an agreement
- **Verdict:** Amica is the *funnel-out* for Metis Client, not the competitor. The honest move is to *recommend Amica first* in onboarding: "If your separation is amicable, try amica.gov.au — free, government-backed, 17,000+ matters. Metis Client is for everything Amica can't help with."

### Settify (settify.com)

- **Operator:** Settify, private
- **Cost:** Not published
- **Geographic scope:** International (AU/CA/UK/US)
- **What it does:** "Client intake systems for law firms" — the solicitor's firm uses Settify to streamline intake; clients fill out forms during intake under the firm's brand
- **What it doesn't do:** independent client-side document organisation, affidavit drafting, chronology generation, matter packs for self-rep, child-support-specific, AU-statute-current-law
- **Verdict:** Settify is solicitor-facing infrastructure. It's not the same product. It might be a future *integration partner* (Metis pushes the Matter Pack into a Settify-using firm's intake) but not a competitor

### Legal Aid NSW

- **What it provides:** Paper PDFs (Factsheets 3 + 4 for child-support stays), phone line (1800 451 784 Child Support Service), duty-lawyer service
- **Digital tooling:** None. Verified during Peter's DPO matter (`factsheets/` folder in source) and again 2026-05-30
- **Verdict:** Not a competitor — they are the *referral source*. Phase 2 partnership conversation is the natural play

### Other candidates checked or considered

- **Lex Protocol** (lex-protocol.com) — already in the solicitor-side teardown; post-event dictation for lawyers. Not client-side.
- **Sortifyd / divorce-property tools** — Phase 2 scan; not direct DPO/child-support overlap
- **LawAdvisor** — generic legal-services platform, not family-law-document-organisation
- **Penda** — family violence app, different angle (safety planning), not document organisation
- **Hello Sky / Open Family Law** — Phase 2 scan; deferred

### Strategic implication

**Metis Client's defensible client-side wedge is the matters Amica excludes by design:**
- ❌ Amica = *amicable* property + parenting agreements → ✅ Metis Client = *contested* matters
- ❌ Amica = excludes family violence → ✅ Metis Client = FV-safe document workflow (with appropriate safety modes)
- ❌ Amica = no child support / no DPO / no stay applications → ✅ Metis Client = exactly these matters
- ❌ Amica = produces an *agreement* → ✅ Metis Client = produces a *matter pack* + affidavits + applications + adversarial-critique

**Honest positioning that holds up:** *"For matters Amica can't help with. Where Amica produces an agreement to keep you out of court, Metis Client produces the matter pack for when court is unavoidable."*

This is NOT "first to market" (Amica beat us by years and is free). This IS "first to the specific harder matters Amica explicitly excludes." Different claim, defensible.

---

## Risks (managed, not avoided)

| Risk | Severity | Management |
|---|---|---|
| **UPL exposure** — AI advising unrepresented client = potential criminal offence | 🔴 critical | Phase 0 lawyer sign-off + every-output safe-harbour rails + mandatory duty-lawyer consult triggers at strategic forks |
| **Solicitor channel poison** — Mom-Test reveals solicitors see Metis-prepared clients as a threat to their first-30-min framing control | 🔴 critical | Mom-Test probe before build; if signal is bad, defer client-side to Phase 3 or partner with one solicitor cohort directly |
| **Pivot reflex** — building client-side becomes the excuse not to close the solicitor wedge | 🟡 high | Phase 0 only until solicitor first paying customer signs; explicit gate in STATUS |
| **Multi-source claim repeated** — "no one does client-side" said before checking | 🟡 high | Mandatory competitive scan in Phase 0 before any positioning claim |
| **Self-rep data security** — clients uploading divorce evidence, FV records, financial disclosures, medical records | 🔴 critical | AES-256 + AU data residency + zero-knowledge encryption at rest + automatic deletion 90 days post-matter-close + opt-in retention |
| **Founder bandwidth** — Peter running 5 businesses + child support matter + Metis Cortex solicitor side + now Metis Client | 🟡 high | Strict Phase 0 / Phase 1 gates; no parallel build until solicitor pays |

---

## Open questions (need decision before Phase 1)

1. **Branding** — is it "Metis Client" as a sub-brand, or unified as just "Metis" with client + solicitor surfaces?
2. **Pricing** — per-matter one-off (A$199-499) or free + solicitor-referred bundle? Both? Decision affects unit economics + sales motion.
3. **Self-rep vs solicitor-referred default** — which is the primary acquisition channel for Phase 1? (Recommendation: solicitor-referred first, because it doesn't fight the solicitor wedge.)
4. **The DPO matter** — does Peter's actual DPO matter become Test Case #1 (anonymised), or does that conflict with the matter still being live?
5. **Lawcover engagement** — proactively or reactively? Manus recommended proactive on the solicitor side; same logic doubles for client side.

---

## What to do next

1. **Run the multi-source competitive scan** on AU client-side family-law tools (1-2 hrs)
2. **Add the "Metis-prepared client" probe to Mom-Test v3** (15 min — patch the existing v2 doc)
3. **Update STATUS** with the dual-track Year-1 decision (gated, not committed) and the founder-three-rounds context
4. **Sleep on it** — this is a strategic expansion; the decision should hold up after 24 hours, not just the moment of "yes let's go"

---

*Source matter: `~/Desktop/child-support-stay-order/` — every workflow stage above has a real artefact in that folder. Read the artefacts to verify the spec isn't speculation; this is what actually happened.*
