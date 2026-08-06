# Metis (Client-Facing) — Automated Document Retrieval Research + Phased Build Plan

**Date:** 2026-05-31
**Source material:** Peter's DPO matter (`~/Desktop/child-support-stay-order/`) as the concrete test case + 2026-05-31 multi-source competitive scan of AU CDR data platforms + AU regulatory architecture knowledge (Privacy Act 1988, CDR, TPB, AUSTRAC, NSW SDA 2007).
**Scope:** how Metis (client-facing surface) actually pulls documents from banks, ATO, Services Australia, court portals, super funds, and email/cloud — phased so Phase 1 ships in 2-3 weeks (your DPO matter), Phase 2 ships after first paying customer (banking auto), Phase 3 is Year 2.

---

## The vision (in three sentences)

A separating Australian — or any family-law client — opens Metis from a referral link. They have a conversation; Metis identifies the matter type, lists what documents will be needed, and offers each source three options: *"I'll pull it for you,"* *"I'll walk you through it,"* or *"upload it yourself."* By the end of the conversation Metis has a chronologically-organised, annexure-numbered, court-expected Matter Pack ready to hand to their solicitor — built from documents the client never had to organise.

---

## The five-stage client experience (what the user actually sees)

### Stage 1 — Triage conversation (~10 minutes, text + voice)

Client describes situation in plain language. Metis identifies:
- Matter type (divorce / parenting / property / child support / DPO / FV-AVO / mixed)
- Urgency triggers (FV risk, DPO blocking travel, FCFCOA hearing date, statutory window closing)
- Procedural framework (FCFCOA initiating application / Services Australia administrative / mediation/FDR / change of assessment / etc.)
- Jurisdiction (NSW / VIC / QLD / etc. — affects recording law + state-specific procedure)
- Whether to recommend [Amica](https://amica.gov.au) instead (if matter is amicable, both parties agree, no FV)

**Output:** matter type locked, framework chosen, document inventory generated (Stage 2 list).

### Stage 2 — Document inventory + retrieval plan (~5 minutes)

Metis generates the matter-specific document list and asks for each: *"how do you want this retrieved?"*

For each source, three options:
- **🟢 Connect automatically** (where regulated path exists — banking via CDR)
- **🟡 I'll walk you through it** (guided screen-by-screen for myGov / CSAOnline / court portals)
- **🔵 I'll upload it myself** (always available fallback)

### Stage 3 — Automated + guided retrieval (~30 minutes spread over a week, async)

Client connects banking (real-time via CDR partner), follows walkthroughs for myGov + CSAOnline (does this in their own time, Metis polls for new docs), uploads scanned letters from the kitchen drawer. Metis OCRs everything, extracts structured fields, categorises into annexures, surfaces gaps + asks follow-up questions.

### Stage 4 — Adversarial-critique pass + strategy options surfacing (~15 minutes)

Same as the existing 12-stage workflow Stage 10-11. Metis runs an independent agent over the assembled documents + draft affidavit, flags compliance landmines (self-incrimination, hearsay, undisclosed assets, contempt risk), surfaces strategy options at each fork ("stay-only vs s.112 leave — here's the trade-off, this needs your solicitor's call").

### Stage 5 — Matter Pack handoff to solicitor

Single PDF (or shared portal link). Client books solicitor consult; solicitor receives the Matter Pack the day before; first consult opens at "here's my read on what they've done, and here's the plan" instead of "what's happening?"

---

## CORRECTION 2026-06-01 — "guided walkthrough" understated the automation surface

Peter pushed back on the earlier "no API = manual only" framing. He's right. During his own DPO matter, Claude drove an authenticated browser session (myGov ATO + CSAOnline) on his behalf while he watched — pulling 18 PDFs from CSAOnline, navigating ATO lodgments, OCR'ing the downloads. That's not "guided walkthrough" — that's **user-supervised co-pilot automation**, and it's materially different from the unattended robotic access that ToS clauses target.

**Two automation patterns, very different legal/risk profiles:**

1. **Unattended robotic access** — third-party system holds credentials, logs in alone, scrapes data. This is what myGov / ATO / Services Australia ToS prohibit. ❌
2. **User-supervised co-pilot** — user logs in themselves (handles 2FA, accepts ToS), session is then driven by an AI in real-time with the user watching, with stop/undo controls + audit log of every action. ✅ This is the pattern that worked on the DPO matter.

When the user is authenticated, present, and supervising, the AI is acting *as* the user — closer to assistive technology than robotic access. ToS clauses targeting "automated means" aim at credential-holding bots running unattended, not at AI helping a logged-in user navigate.

**Implementation patterns (Phase 1 picks Option A — same as what Claude used on the DPO):**
- **A — Browser extension** — client installs Metis extension; logs into myGov/etc. normally; clicks "let Metis help" → extension drives navigation in their tab. Lowest ToS risk (it's their browser, their session). **Phase 1 pick.**
- **B — Embedded supervised session** — Metis app embeds a Playwright-style browser; client logs in within Metis; Metis drives in the same session. Lowest friction but client trust may be lower.
- **C — Screen-recorded co-pilot** — client screen-shares; Metis suggests + auto-clicks in real-time. Highest transparency but technical setup friction.

**Hard rails on co-pilot (non-negotiable):**
- Per-action audit log (every click, every download)
- Visible action narration ("downloading 2019-20 NOA… filing under Annexure C")
- Stop / undo at any step
- Anything irreversible (form submissions, payments, change-of-detail requests) is NEVER auto-clicked — surfaced for client to confirm

**Phase 0 gate addition:** the Sydney legaltech lawyer brief now specifically asks about user-supervised browser automation against myGov + ATO + Services Australia ToS — not just CDR + UPL. Whoever reviews this needs to confirm the co-pilot pattern is legally distinct from prohibited robotic access. The honest fallback if they say no = revert to guided walkthroughs for those three sources only.

---

## Source-system matrix (what we need, from where, how we get it) — CORRECTED

The architecture has to be honest about which sources are automatable and which aren't. Some have regulated data-sharing paths; most don't — but many that don't have APIs ARE still drivable via user-supervised co-pilot automation (above).

| Source | What we need | Automatable today? | Path |
|---|---|---|---|
| **Banking (4 big + 100+ smaller AU banks)** | 12-24 months of statements, transaction history, balances, joint account distinction | ✅ **YES** | Consumer Data Right (CDR), via Basiq or Frollo as sponsoring ADR — A$0.50/user/mo at Basiq verified |
| **ATO / myGov (tax)** | Notices of Assessment (5+ years), tax returns, CGT schedules, super balances, PAYG summaries | ❌ NO public API | 🟢 **User-supervised co-pilot** (after client auth) — same pattern Claude used on Peter's DPO matter |
| **Services Australia / CSAOnline** | Child support assessments, change-of-assessment letters, DPO notices, prior-application history | ❌ NO public API | 🟢 **User-supervised co-pilot** (after client auth) — exactly what pulled Peter's 18 prior-application PDFs |
| **Commonwealth Courts Portal (FCFCOA)** | Existing court orders, case file history, prior applications | ❌ NO public API | 🟢 **User-supervised co-pilot** (after client auth) |
| **Super funds** | Statements, balances, splits, beneficiary nominations | ⚠️ **Partial** | Some funds have APIs (rare); CDR Super in scope but not yet live as of 2026; guided walkthrough for now |
| **Property records (NSW LRS, VIC Land Use Victoria etc.)** | Title searches, mortgage discharges, sale contracts | ⚠️ **Paid per-search APIs** | InfoTrack, GlobalX, SAI Global — paid commercial APIs, A$15-30/search. Defer to Phase 3 |
| **Insurance (CDR Insurance — pending)** | Policies + claims for relevant assets | ❌ **Not yet live** | Manual until CDR expands |
| **Email archives (Gmail, Outlook, iCloud)** | Correspondence with opposing party, prior solicitors, employer letters | ✅ **OAuth APIs** | Gmail API + Microsoft Graph + iCloud Mail (limited) — read-only with consent; search for specific senders/keywords |
| **Cloud storage (Dropbox, Google Drive, OneDrive)** | Scanned letters, photos of paper documents | ✅ **OAuth APIs** | Standard OAuth flows |
| **ASIC (company + trust register)** | Company extracts, current organisation roles | ⚠️ **Paid search** | ASIC Connect — paid per-search (A$9-44). Phase 2 |
| **Centrelink / Medicare** | Benefit letters, statements (relevant for parenting matters) | ❌ NO public API | 🟢 **User-supervised co-pilot** (after myGov auth) |
| **Vehicle / RTA records** | Vehicle ownership, debt-secured-by-vehicle | ⚠️ **State-by-state** | Defer to Phase 3 |
| **Phone records (Telstra, Optus, etc.)** | Call/SMS history (relevant for FV matters, claimed contact patterns) | ⚠️ **Account holder only** | Guided walkthrough through telco self-service portal |
| **Photos / paper documents at home** | Anything physical (letters, court orders, marriage certificate, kids' birth certificates) | ✅ **Direct upload** | Camera + OCR + auto-categorisation in conversation |

**Read:** banking is the only category with a clean regulated automation path. ATO + Services Australia + court portals are guided-walkthrough-only by structural design — no API, deliberate. The play is **hybrid**: automate where regulation allows (banking, OAuth-accessible email/cloud), guide where it doesn't, accept upload as fallback always.

---

## Technical architecture (four layers)

```
┌─────────────────────────────────────────────────────────────────┐
│  Layer 4 — Conversational AI surface ("Metis")                  │
│  - Text chat + voice (Deepgram + GPT/Claude/Gemini routing)     │
│  - Single-page React app + mobile web                           │
│  - UPL safe-harbour rails (DRAFT watermarks, lawyer-flag forks) │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Layer 3 — Matter orchestration (the 12-stage workflow engine)  │
│  - Matter triage + framework selection                          │
│  - Document inventory generator (matter-type → checklist)        │
│  - Chronology builder + annexure schedule constructor            │
│  - Asset/liability schedule (for property matters)              │
│  - Adversarial-critique runner                                  │
│  - Matter Pack PDF generator                                    │
│  - Workflow state machine (Drizzle ORM + MySQL on Railway)      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Layer 2 — Source adapters (per-source-system integrations)     │
│  - banking-cdr-adapter (Basiq client)                           │
│  - email-oauth-adapter (Gmail API + MS Graph + iCloud)          │
│  - cloud-storage-adapter (Dropbox + GDrive + OneDrive OAuth)    │
│  - manual-upload-adapter (file upload + camera capture)         │
│  - guided-walkthrough-runner (step-by-step instruction engine   │
│    for myGov / CSAOnline / court portals — generates dynamic    │
│    instructions per source, polls for upload completion)        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Layer 1 — Document processing pipeline                          │
│  - OCR (Apple Vision / Google Vision — AU region)               │
│  - Structured field extraction (LLM)                            │
│  - Document classification (matter-type-aware)                  │
│  - PII detection + redaction-for-display                        │
│  - Encrypted-at-rest storage (R2 with AU residency)             │
└─────────────────────────────────────────────────────────────────┘
```

**Existing app already has:** Layer 1 partial (Deepgram audio; PDF OCR would be new), Layer 3 partial (the legal knowledge base + AustLII + LLM routing), Layer 4 partial (React UI exists, needs conversational adaptation). Layer 2 is largely net-new.

**Net-new build effort for Phase 1 (Metis-for-Peter on the DPO matter):**
- Layer 1 PDF OCR pipeline: ~3 days (re-use Apple Vision pattern from DPO matter)
- Layer 2 manual-upload-adapter + guided-walkthrough-runner for myGov + CSAOnline: ~5 days
- Layer 3 matter-orchestration for DPO-stay template only: ~5 days
- Layer 4 conversational interface (text-only, voice deferred to Phase 2): ~5 days
- Adversarial-critique agent integration: ~2 days
- Total: **~2.5-3 weeks of focused work**

---

## Regulatory architecture (what's allowed, what isn't)

### Consumer Data Right (CDR)

- **Banking** is fully live (since 2020). Any business pulling consumer banking data is regulated.
- **Two paths to compliance:**
  - **Become an Accredited Data Recipient (ADR)** — direct accreditation, A$30-100K + 3-6 months + ongoing compliance (security audits, governance, reporting). Not viable for Phase 1-2.
  - **Use a sponsoring ADR** — partner with a CDR-accredited platform (Basiq is the dominant one in AU; Frollo is the alternative). They handle accreditation, security, consent flows; you build on their SDK.
- **Verified Basiq pricing:** A$0.50/user/month (banking data) + A$0.25/user/month (data enrichment) + platform access fee. At 1,000 clients = A$750-1,000/mo. **Negligible vs the per-matter revenue.**
- **CDR Super, Insurance, Telco:** in scope, partially activated, not fully live as of 2026. Watch but don't depend on.

### ATO / myGov

- **No public API for individuals.** Period.
- **Tax Practitioners Board (TPB)** registered software (Xero, MYOB, etc.) can access via Tax Practitioners SBR — but that requires the user to be a registered tax agent. **Metis is not a tax agent and shouldn't become one.**
- **The Metis client-side path is guided walkthrough** — "log into myGov, navigate to ATO, click Lodgments, download PDF, upload here." Metis polls for upload completion + extracts.
- **Avoid TPB exposure:** Metis must NEVER advise on tax positions, recompute ATIs, or interpret tax notices beyond "this document is your 2019-20 Notice of Assessment showing ATI of $X." Anything more = tax advice = TPB registration requirement. Hard rail.

### Services Australia (Centrelink, Medicare, Child Support)

- **No public API.** Manual myGov access only.
- **Guided walkthrough** — same pattern as ATO.
- **DPO copies + change-of-assessment letters:** Metis can draft the request letter for the client to send to Services Australia. Cannot auto-submit.

### Tax Practitioners Board

- Don't trigger. Stay in document gathering + organisation. Never provide tax positions, recompute, or advise.

### AUSTRAC

- Not triggered by document gathering. Would be triggered if Metis became a designated service provider (handling money, KYC verification for regulated purposes). Not in scope.

### Privacy Act 1988 + APPs

- **APP 1** — Privacy policy: required + must specifically address CDR data handling
- **APP 5** — Notification at collection: built into every conversation prompt
- **APP 8** — Cross-border disclosure: requires AU-region LLM processing (Vertex AI Sydney or Bedrock Sydney). US-region inference = APP 8 disclosure required (and is a deal-breaker for many solicitors).
- **APP 11** — Security: encrypted at rest (AES-256), TLS 1.3, role-based access, audit logs
- **APP 12-13** — Access + correction: clients can download/delete their data anytime

### NSW Surveillance Devices Act 2007

- Already addressed for the conference-recording side (Metis Cortex solicitor product)
- For Metis client side: not directly applicable (no recording involved in document gathering). But if voice channel is used for client conversation, same all-party-consent rules apply.

### Legal Profession Uniform Law (LPUL) — UPL

- **The biggest exposure.** Metis client side could be argued to constitute unauthorised legal practice if it advises on the matter.
- **Architecture for safe-harbour:**
  - Document organisation = NOT legal practice (admin work, anyone can do it)
  - Draft generation with mandatory "FOR REVIEW BY YOUR SOLICITOR" watermarks = NOT legal practice (draft assistance, like a paralegal could provide)
  - Strategic decision flagging WITHOUT advice ("this is a legal call — discuss with your solicitor") = NOT legal practice
  - Predictions of outcomes / "you should…" / "you will win" = LEGAL PRACTICE — never do
- **Sydney legaltech lawyer review** before launch (~A$300-500 30-min consult) — non-negotiable Phase 0 gate

---

## Phase 1 — Metis-for-Peter (your DPO matter, 2-3 weeks)

**Goal:** finish your own DPO matter (the 5 hard pre-requisites are still pending) using a Phase 1 prototype, in a way that doubles as the first working build.

**Scope (narrow):**

- Text conversational interface (no voice yet)
- One matter template: T1 — DPO stay
- One automated source: nothing (Phase 1 is manual-upload + guided-walkthrough only — keeps the regulatory complexity at zero)
- One client: you
- One target output: the witnessed-ready Matter Pack for your FCFCOA application

**What it builds:**

1. **Conversational triage** — you say "FCFCOA s.111C stay order, NSW, child support" → it triages, pulls up the 5 pending pre-requisites from where REDLINE-DPO-2026-05-27.md lives
2. **Document upload + OCR** — drag-drop 18 prior-application PDFs → it extracts text + categorises into annexures A-K
3. **Guided walkthroughs** for the remaining steps:
   - ATO: "go to myGov → ATO → Lodgments → download 6 NOAs, drop them here" → it extracts ATIs
   - DPO copy: "draft email to Services Australia + alternative FOI request letter" → ready to send
   - Tempe net proceeds: "go to your accountant + Wesley → ask for breakdown of $1,283K sale proceeds" → fillable form
   - Trust register: ASIC search (paid, you pay manually) → enter figures
4. **Adversarial-critique** pass over the assembled material (your REDLINE-DPO-2026-05-27.md already has 6 critical items + others; Metis re-runs the critique on the rework)
5. **Matter Pack export** — single PDF for JP appointment

**Build cost:** ~2.5-3 weeks Peter + Claude. No CDR. No partners. No regulatory work. No third-party clients = zero UPL exposure (you're the user).

**What you walk away with:**
- Your DPO matter actually finished + filed
- A working Metis prototype tested against the most demanding possible user (you)
- Anonymisable as Reference Case #1
- Source data for the future Phase 2 design

**Out of scope for Phase 1:**
- Banking automation (Phase 2)
- Voice channel (Phase 2)
- Multi-tenancy (Phase 2)
- Other matter types (Phase 2/3)
- B2C consumer surface (Year 2)

---

## Phase 2 — First paying customer + Basiq banking + voice (Q3-Q4 2026)

**Triggered by:** first Metis Cortex founding firm signs the pilot + 30-day green signal.

**Scope additions:**

1. **CDR banking via Basiq** — Phase 2 build (~3-4 weeks):
   - Basiq SDK integration
   - Consent flow (CDR consent dashboard required)
   - Bank statement parsing → asset/liability schedule auto-populate
   - Per-transaction categorisation (helps property settlement matters)
   - Pricing: A$0.50/client/mo + Basiq platform fee — passed through or absorbed into firm's per-matter cost (negligible)

2. **Email + cloud storage OAuth adapters** (~1-2 weeks):
   - Gmail / Outlook / iCloud Mail read-only access
   - Keyword search (e.g., "opposing party name" + "your previous solicitor's name") to extract relevant correspondence
   - Dropbox / Google Drive / OneDrive for scanned-document pulls

3. **Voice channel for client conversation** (~1-2 weeks):
   - Deepgram for transcription (already wired for the solicitor side)
   - Twilio for the phone-call channel
   - Same UPL rails as text

4. **Multi-tenancy** (~1 week):
   - Firm sees their referred clients' matters
   - Client portal scoped to firm + client
   - Audit log per matter

5. **Sydney legaltech lawyer review** of UPL safe-harbour architecture (~A$300-500, 1-week timeline)

6. **Lawcover engagement** for PI position on Metis-assisted work (joint call with first paying firm, no cost)

**Phase 2 total effort:** ~6-8 weeks. Lands ~Q3 2026 assuming Phase 1 ships end of June.

---

## Phase 3 — Year 2 expansion (Q1 2027+)

Triggered by: 5 founding firms paying + 6 months retention.

- T2 (change of assessment), T3 (parenting), T4 (property), T5 (initial consult prep) matter templates
- Property records integration (InfoTrack / GlobalX paid APIs)
- ASIC Connect integration
- CDR Super when fully live
- Telco data when CDR Telco activates
- Consumer-direct surface (currently parked per single-brand decision; revisit if signal warrants)

---

## What Peter's DPO matter looks like running through Metis tonight (concrete walkthrough)

Take the 5 hard pre-requisites you have outstanding. Walk through how Phase 1 Metis would handle each.

**Pre-requisite 1: Lodge DSK income with ATO**

Today: you have to remember to do it; calculate; lodge BAS or income disclosure; remember to update affidavit Paras 19 + 24(a) after.

In Metis Phase 1:
- Conversation: *"the redline says you need to lodge DSK income before swearing. Let's do that now. Have you decided BAS or income disclosure?"*
- You: *"BAS, last 12 months"*
- Metis: *"OK, go to myGov → ATO → Activity Statements → Lodge a BAS. When you've submitted, take a screenshot of the confirmation page and drop it here. I'll annexure it as 'K' and update Para 19 + Para 24(a) of your affidavit to the compliance statement with the lodgement date."*
- You do it. Drop the screenshot. Metis updates the affidavit MD + regenerates the DOCX.

**Pre-requisite 2: SA written confirmation that stay order is required**

Today: you have to email Services Australia, possibly FOI, get a response, parse it.

In Metis Phase 1:
- Metis drafts the SA email + alternative FOI request letter, both ready to send
- *"Send the SA email first. If you get a written response in 7 days, drop it here and I'll annexure it as 'E' and tighten Para 16 to remove the hearsay language. If no response, send the FOI request — also ready to send."*

**Pre-requisite 3: DPO copy**

Same pattern. Metis drafts the request to Services Australia. You send. Metis polls for upload.

**Pre-requisite 4: Tempe sale net proceeds breakdown**

Today: you have to contact your accountant + Wesley, get the figures, type them in.

In Metis Phase 1:
- Metis generates a fillable form with the categories from the REDLINE (mortgage / commission / settlement / FTX $200K / FX margin / residual)
- You fill it from your accountant's email reply
- Metis updates Para 23B v3 with the dollar breakdown

**Pre-requisite 5: Trust share register figures**

Today: you have to do an ASIC search (paid) + reconstruct from memory.

In Metis Phase 1:
- Metis instructs the ASIC Connect search (paid by you, A$9-44)
- You upload the extract
- Metis extracts: Kritsotakis Investments Pty Ltd, sole director Karren, you = 100 partially-paid ordinary shares
- Metis updates Para 23C + Financial Statement section

**End state:** all 5 pre-requisites done in a few hours of conversation across a week of async work. Affidavit + initiating application + cover letter DOCXs all regenerated. JP appointment safe to book. Matter Pack ready for filing.

**This is the prototype. It also closes your DPO matter.**

---

## Open questions + research gaps (what wasn't verified tonight)

1. **Basiq sponsoring-ADR specifics** — pricing page didn't clarify whether Metis would need its own CDR accreditation or can ride on Basiq's. Direct call with Basiq sales = A$0, 30 min, the answer
2. **Frollo as alternative** — site returned 404; comparable pricing + sponsoring model worth verifying
3. **CDR Super activation timeline** — pending activation; affects when super statements can be automated
4. **Sydney legaltech lawyer recommendation** — name + 30-min consult booking. Phase 0 gate item.
5. **Lawcover position on AI-assisted client work** — separate engagement; could be joint call with first paying firm
6. **MyGov ToS** — quick read to confirm guided walkthroughs are ToS-compliant (browser direction is fine; account credential collection is not, and Metis never asks for them)
7. **State-by-state surveillance device variations** — confirmed NSW (5yr / 500 penalty units, all-party consent); VIC/QLD/SA/WA/ACT/TAS need confirmation if voice channel goes national in Phase 2

---

## Recommendation + next concrete step

**Build the Phase 1 prototype for your DPO matter. Use that to close out the matter AND produce the first working version of the client-facing Metis. ~2.5-3 weeks. Zero regulatory exposure. Highest-leverage path.**

**Order of work, if you greenlight:**

1. Spend tomorrow (Sunday) reading this doc + sleeping on whether Phase 1 scope is right
2. If yes: Monday morning I scope the actual Phase 1 sprint (specific tickets, file structure, integration points with the existing Manus codebase) and we start Tuesday
3. By end of Week 3 (~mid-June): your DPO matter is filed, Metis prototype is working, you have something to demo on Mom-Test calls that's *actually built* rather than mocked
4. Mom-Test send happens AFTER Phase 1 prototype exists (~mid-to-late June), so every conversation has a real demo to show, not slides

**This delays the Mom-Test send by ~2-3 weeks** vs the "send Monday" plan. Real trade-off. But: every Mom-Test call lands harder when the answer to "show me how it works" is "let me share my screen" instead of "here's the spec." And it closes your DPO matter in the same window.

Alternative: send Mom-Test Monday with current site + slides; build Phase 1 in parallel. Riskier (split focus) but preserves the early outreach window.

Your call. Sleep on it.
