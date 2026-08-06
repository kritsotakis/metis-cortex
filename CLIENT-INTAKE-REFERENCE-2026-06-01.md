# Metis — AU Family-Law Client Intake Reference

**Date:** 2026-06-01
**Purpose:** the canonical source-of-truth for the Metis client-side document inventory generator. Every matter-type template (T1 DPO stay, T2 change of assessment, T3 parenting, T4 property, T5 initial consult prep) reads from this doc to generate its checklist.
**Sources:** AU family-law procedure knowledge + Peter's DPO matter source material (`~/Desktop/child-support-stay-order/`) + the "no-holes" build spec in `~/Desktop/metis-cortex-app/CLAUDE.md` (compliance artefacts + Sewell v Zelden file-note elements + family-law process gates) + LPUL ss.174-178 + ASCR rr.9-12 + post-2024 parenting + post-June-2025 codified four-step property reforms.

This is what every AU family-law client needs to supply their solicitor. Phase 1 Metis (DPO matter) needs to support the T1 subset; the rest get built incrementally.

---

## Universal intake (every matter, regardless of type)

These are required for the solicitor to take on ANY family-law matter and comply with professional obligations.

### 1. Client identification + verification (LPUL + ASCR + AUSTRAC if applicable)

- **Primary photo ID** — Australian driver's licence OR passport (with photo, date of birth, address)
- **Secondary ID** — Medicare card OR utility bill OR bank statement (address match)
- **Date of birth + current residential address** — for conflict check + court documents
- **Australian citizenship / residency status** — affects jurisdiction + court fee waivers
- **Spouse/de facto partner's full name + DOB + last known address** — for opposing-party conflict check
- **Any children's full names + DOBs** — for conflict + capacity (children's lawyer if matter requires)

### 2. Contact + accessibility

- **Phone, email, postal address** — primary + alternate
- **Emergency contact** — non-party
- **Language preferences + interpreter need** — if English isn't first language
- **Accessibility needs** — hearing, vision, mobility, mental capacity considerations
- **Safe contact method** — important in FV matters (don't send mail to a shared address)

### 3. Conflict-check inputs (ASCR rr.10-12)

- **Spouse/de facto party's full name + any previous names** — including maiden, married, business names
- **Any business names the client OR opposing party has traded under** — sole trader, company, partnership
- **Any prior solicitors used by either party** — particularly in this or related matters
- **Family members on either side who may have a legal interest** — children, parents, siblings

### 4. Costs disclosure inputs (LPUL s174 — the basis the solicitor will use to set their fees)

This is what the solicitor needs to PROVIDE the disclosure; the client needs to RECEIVE + understand it. But to be set:
- **Funding source** — own funds / family loan / litigation funding / Legal Aid grant / pro bono
- **Capacity to pay** — solo earner / dual income / unemployed / on benefit
- **Realistic complexity signals** — multi-asset, multi-jurisdiction, FV, high-conflict (drives the estimate)

### 5. Engagement context

- **Previous legal representation in this matter** — who, when, why ended (privileged but flag-able)
- **Any current proceedings or pending applications** — FCFCOA, Magistrates Court, Services Australia, etc.
- **Time-critical deadlines** — court dates, statutory windows, response deadlines, FV protection order expiry
- **Capacity for proceedings** — health, mental state, sobriety (affects ability to instruct + give evidence)

### 6. Family-violence screening (mandatory at intake per FLA + Lighthouse where available)

Even where FV isn't the matter, intake must screen for it because it shifts process (FDR exemption, pre-action steps, parenting framework):
- **Any AVO / DVO / FVO / IVO** — current or expired, against whom, by whom
- **Any police involvement** — incidents reported, even if no charges
- **Any safety concerns about contact with the opposing party** — for solicitor's own safety + client's
- **Any children present during incidents** — affects parenting matters materially

---

## A. Divorce (formal — divorce application under FLA s48)

**What the solicitor needs from the client:**

| Item | Why | Source |
|---|---|---|
| Marriage certificate (original or certified copy) | Required to file divorce application; foundational evidence | State births/deaths/marriages registry |
| Date of separation | s48 requires 12+ months separation; date is contested issue | Client memory; supporting evidence below |
| If separated under one roof: evidence | s48 still satisfied but needs proof — separate rooms, finances, social, sexual | Affidavit from third party (family member, neighbour) + bank statements showing separate accounts + Centrelink letters if benefits changed |
| Children's birth certificates (under 18) | s55A — court must be satisfied proper arrangements for children | State BDM |
| Statement of proper arrangements for any children under 18 | Schools, residence, contact, financial support | Client statement |
| If marriage less than 2 years: counselling certificate OR exemption | s44(1B) — must attend marriage counselling OR get court leave | Marriage counsellor (Relationships Australia etc.) |
| Service evidence | Spouse must be served if Sole Application; affidavit of service | Process server |

---

## B. Parenting orders (post-2024 FLA reforms — current s60CC best-interests framework)

The 2024 reforms (effective 6 May 2024) **removed the s61DA Equal Shared Parental Responsibility presumption + s65DAA equal-time requirement**. Current s60CC is a simplified best-interests test. The intake must support this.

| Item | Why | Source |
|---|---|---|
| Children's full names, DOBs, school enrolment | Foundation | BDM + school enrolment forms |
| Children's Medicare numbers + GP details | Health-related parenting decisions | Medicare card + GP receipts |
| Current parenting arrangement (formal or informal) | What the court is being asked to change OR ratify | Client diary + any written agreement |
| **Section 60I FDR certificate** (or exemption proof) | **Mandatory pre-filing in most parenting matters** — FDR practitioner must certify attempted mediation OR issue exemption (FV, urgency, child abuse, jurisdictional, etc.) | FDR practitioner (Relationships Australia, Family Relationship Centre, accredited private FDRP) |
| Pre-action procedure compliance | FCFCOA Practice Direction — Genuine Steps before filing | Solicitor-client correspondence + FDR attempts |
| Family violence history | s4AB definition + FV affects best-interests + may exempt FDR | Police records, AVOs, hospital records, photos, messages |
| Children's voice — independent children's lawyer indicators | Older children + high-conflict matters | Family Consultant report referrals |
| Schools' contact details + attendance records | Care arrangements + relocation issues | School admin office |
| Childcare arrangements + costs | Splitting child support + care % calc | Childcare provider statements |
| Medical / counselling / therapy history for children | Best-interests + risk factors | GP, paediatrician, child psychologist |
| Communication history with other parent (text, email, app like 2houses) | Co-parenting capacity + concerning conduct evidence | Phone exports + 2houses log + email archives |
| Photos / videos relevant to parenting | Drug use, conditions, FV — proportionate and contextualised | Camera roll + cloud storage |
| Any incident diary maintained | Contemporaneous record of handover issues, missed contact | Client diary |
| Drug / alcohol / criminal history of either party (if alleged) | Best-interests risk factors | Court records, police reports (subpoena route) |
| Travel documents for children (passports) | Hague Convention + relocation matters | Family vault |
| Cultural / religious / Indigenous status | Special best-interests considerations | Client statement |

---

## C. Property settlement (post-June-2025 codified four-step under FLA Part VIII)

The 2025 reforms (effective 10 June 2025) **codified the four-step process + introduced "economic effect of family violence" as a relevant consideration + new disclosure duty s71B (married) / s90RI (de facto) + companion-animals framework**. The four steps are: (1) identify pool, (2) assess contributions, (3) assess future needs, (4) just and equitable.

**The full + frank disclosure duty is ongoing, undertaking-backed, and breach triggers contempt/costs.** This drives the document list — anything material to the asset pool must be disclosed.

### Asset pool — what's in (every category, with documentation)

| Asset class | Documents required | Source |
|---|---|---|
| **Real property — primary residence** | Title search, contract of purchase, mortgage statement (current + 12mo), valuation report (formal or sworn estimate), property tax + rates notices, insurance policy | LPI / LRS state registries, lender, valuer |
| **Real property — investment properties** | Same as above PLUS rental income statements + agent management agreement + depreciation schedule | Above + property manager |
| **Real property — overseas** | Foreign title + valuation + tax obligations + any caveats | Foreign jurisdiction |
| **Bank accounts** | **ALL** accounts (sole + joint + offshore) — 12-24 months of statements, balances at separation + balances at trial date | Bank (automatable via Basiq once Phase 2 ships) |
| **Term deposits + savings** | Statements + maturity dates + interest | Bank |
| **Credit cards + personal loans** | Statements showing limits + balances + interest rate + payment history | Lenders |
| **Superannuation** | Member statements (current + historical), Total Super Balance, beneficiary nomination, Defined Benefit valuations (specialist actuary required), SMSF trust deed + financials | Super fund / SMSF accountant |
| **Vehicles** | Registration, loan/lease documents, fair-market valuation (Redbook OR sworn) | RTA equivalents, lender |
| **Shares + managed funds** | Holdings statement, CHESS sponsorship details, transaction history, cost base, recent valuations | Broker / share registry / fund |
| **Cryptocurrency** | Wallet exports, exchange statements, transaction history, current valuation (date-specific) | Exchanges, hardware wallet exports, blockchain explorer |
| **Cash + jewellery + collectibles** | Valuation reports + insurance schedule | Insurance company + sworn statement |
| **Business interests (sole trader)** | BAS lodgements, P&L, balance sheet, accountant's valuation | Accountant |
| **Business interests (company)** | ASIC extract, shareholdings, company financials (audited if available), Directors' loans, valuation report | ASIC Connect + accountant |
| **Business interests (partnership)** | Partnership agreement, financials, partner ledger | Accountant |
| **Trust interests** | Trust deed, schedule of beneficiaries, distribution history (5+ years), trust financials, appointor + trustee details — **disclosure required even if discretionary beneficiary** (Peter's Kritsotakis Family Trust case) | Trustee accountant |
| **Inheritance — received or expected** | Estate documents, will (if probated or copy if living testator), executor contact | Solicitor handling estate |
| **Gifts received during marriage** | Gift letters or evidence + cash receipts + treatment (loan vs gift) | Donor + bank records |
| **Loans from parents (informal)** | Loan agreements OR pattern of payments + parent statement | Parent + bank records |
| **Insurance — cash surrender value** | Life policies + whole-of-life + investment-linked | Insurance company |
| **Tax refunds + ATO debts** | NOAs + ATO portal screenshots | myGov ATO (manual download) |
| **Centrelink debts / overpayments** | Centrelink statements | myGov Services Australia |

### Income evidence (all sources, both parties — used for ATI history + child support + future-needs assessment)

| Item | Detail | Source |
|---|---|---|
| **Notices of Assessment** | 5+ years minimum — more if matter has CGT events, business income volatility, child-support assessment dispute (Peter's matter needed 7 NOAs 2018-19 to 2024-25) | myGov ATO (manual) |
| **Recent pay slips** | Last 3-6 months | Employer / payroll |
| **Employment contract** | Current + any termination/redundancy | Employer |
| **Centrelink statements** | If receiving any benefits | myGov |
| **Workers compensation** | Payment summaries + ongoing entitlement letters | Insurer (Peter's matter — he's on WC) |
| **Investment income** | Dividend statements, distribution reports | Brokers, fund managers, share registries |
| **Business income** | BAS, P&L, accountant's letter for the most recent FY | Accountant |
| **Rental income** | Agent statements, depreciation schedules | Property manager |
| **Capital gains events** | CGT schedule + supporting docs (sale contract, cost base evidence) | Accountant + records |

### Liabilities (every debt, both parties)

| Item | Detail | Source |
|---|---|---|
| **Mortgages** | All — including reverse mortgages, lines of credit | Lender |
| **Personal loans** | Including HELP/HECS, family loans, BNPL accounts | Lenders |
| **Credit cards** | All cards, all parties | Lenders |
| **Tax debts** | ATO portal | myGov |
| **Centrelink debts** | Services Australia portal | myGov |
| **Child support debts** | CSAOnline | myGov |
| **Bankruptcy / insolvency** | AFSA records if relevant | AFSA |
| **Guarantor obligations** | Any guarantees signed (e.g., for parents, business partners) | Bank + private records |
| **Litigation pending** | Any unrelated claims against either party | Court records |

### Pre-relationship + post-separation evidence (contributions step)

| Item | Why |
|---|---|
| Asset position at start of cohabitation OR marriage | Initial contributions — affects step 2 of the four-step |
| Asset position at date of separation | Sets the "starting point" for adjustments |
| Asset position at current date | Distinguishes post-separation contributions / dissipations (Peter's matter — Tempe sale + alleged FTX dissipation) |
| Any property acquired post-separation | Particularly important; may or may not be in the pool |
| Any inheritances received post-separation | Can be excluded OR included depending on context |
| Any debts incurred post-separation | Same — characterisation matters |
| **Dissipation narrative + dollar particulars** | Where one party has reduced the pool — must be specific (Peter's Tempe net proceeds breakdown is the textbook case — Para 23B v3 in the redline) |

### Family-violence economic effect (NEW under 2025 reforms)

- Loss of income from FV-related disability / absence
- Costs incurred for safety (relocation, security, legal)
- Career disruption attributable to FV
- Impacts on workforce participation

### Companion animals (NEW under 2025 reforms)

- Documentation of ownership / care
- Veterinary records
- Adoption / purchase records

---

## D. Spousal maintenance

In addition to property documents (need-and-capacity is the test):

| Item | Why |
|---|---|
| **Detailed budget** — actual current spending across all categories | Establishes needs |
| **Earning capacity evidence** — qualifications, employment history, age, health, child-care responsibilities | Establishes capacity OR lack |
| **Re-training plans + costs** | If transitioning back to workforce |
| **Health conditions + medical reports** | Affects earning capacity |
| **Childcare cost evidence** | Affects ability to work |
| **Other party's earning capacity** | Same evidence as for them |

---

## E. Child support (administrative — Services Australia process)

| Item | Why | Source |
|---|---|---|
| **Current care arrangement (% nights with each parent)** | Drives formula calculation | Client diary + parenting orders if any |
| **Both parents' NOAs (5+ years)** | ATI history drives the assessment | myGov ATO |
| **Current income evidence (both parties if known)** | Same | Payslips + Centrelink + BAS |
| **Special expenses** | Children's medical, schooling, disability — affects change-of-assessment | Receipts |
| **Services Australia correspondence** | Any prior assessments, change-of-assessment outcomes, agreements | CSAOnline (manual) |
| **Banking records around payment dates** | Evidence of paid / received / arrears | Bank (Basiq Phase 2) |

---

## F. Child support court (DPO / s.111C stay / departure / s.116B / s.117 special circumstances)

**This is Peter's matter — the T1 template.** Specific requirements beyond E:

| Item | Why | Notes from Peter's DPO matter |
|---|---|---|
| **All Services Australia correspondence in the matter** | Foundation of the application | Peter pulled 18 PDFs from CSAOnline — manual export |
| **DPO copy** (s.72D — issued under CSRC Act) | Establishes existence + terms of the order being challenged | Peter doesn't have copy; covering letter requested it + FOI fallback |
| **Income/ATI history showing distortion** | Justifies stay — that current assessment is unfair given income reality | Peter: 7 NOAs needed (2018-19 to 2024-25) showing one-off 2019-20 CGT spike from Tempe sale |
| **One-off income event documentation** | If matter turns on CGT event / inheritance / redundancy / one-off windfall | Peter: Tempe sale contract + CGT schedule + net proceeds breakdown |
| **Current income evidence** | Workers comp, business income, etc. — what payer is actually earning now | Peter: WC payment summary @ $1,680/wk gross since Jan 2024 + DSK income TBD |
| **Bankruptcy status** | Relevant if affects ability to pay or asset pool | Peter: AFSA petition pending |
| **Travel necessity (if DPO lift sought)** | Why travel is needed — work, family, medical | Peter's matter: hardship-based |
| **Proposed interim payment evidence** | What payer can realistically pay during stay (key per Critique F4 — must be defensible) | Peter: 50% net DSK income (rewritten from $50/week which read as contempt) |
| **Prior change-of-assessment applications** | Procedural history — rejection reasons | Peter: April 2025 Reason 8A application rejected for s.98C 18-month limit |
| **Trust interests (full disclosure)** | Even if discretionary beneficiary | Peter: Kritsotakis Family Trust disclosure required — caught by Critique E7 |

---

## G. Family violence / AVO

| Item | Why | Source |
|---|---|---|
| **Police event numbers + reports** | Foundational evidence | NSW Police (Information Access Unit), client copies |
| **Hospital / medical records (FV-related injuries)** | Independent corroboration | Hospital records request |
| **GP / counsellor / psychologist records** | Pattern of harm, mental health impacts | Treating practitioner |
| **Photos of injuries (date-stamped if possible)** | Direct evidence | Camera roll + cloud |
| **Photos of property damage** | Same | Same |
| **Text / email / social media messages** | Threats, controlling conduct, coercive control evidence | Phone exports + email + screenshots |
| **Witness statements** | Family, friends, neighbours who saw / heard incidents | Witness contact + statements |
| **Audio / video recordings (where lawfully obtained)** | NSW SDA 2007 strict — only lawful recordings | Client files |
| **Existing AVO / DVO / IVO / FVO** | Current orders | Local Court |
| **Safety plan + risk assessment** | If from DV service / Lighthouse / police | DV service |
| **Children's exposure evidence** | If parenting matter linked | Above sources |

---

## H. Consent orders

| Item | Why |
|---|---|
| **Draft agreement** | The substance to formalise |
| **All parenting evidence (per C)** if parenting orders | Underlying documentation for review |
| **All property evidence (per D)** if property orders | Same |
| **Both parties' financial disclosure** | Court must be satisfied orders are just and equitable |
| **Independent legal advice certificates** | Particularly for BFAs / consent orders without solicitor on each side |

---

## I. Mediation / FDR prep

| Item | Why |
|---|---|
| Full property + parenting disclosure (per C and D above) | FDR negotiates on this basis |
| Realistic best-case + worst-case + walkaway positions | Strategy |
| Children's voices documented (if applicable) | Parenting decisions |
| Time-cost-emotional-cost realistic estimate of litigation alternative | Negotiation leverage / inverse |

---

## J. International / Hague / relocation

| Item | Why |
|---|---|
| Passports + visa status of all parties | Jurisdictional + return-order capacity |
| Foreign court orders (apostilled or certified) | Recognition + enforcement |
| Habitual residence evidence | Hague Convention test |
| Travel history (entry/exit records) | Same |
| Proposed relocation plan (job, school, housing) | Best-interests evaluation |

---

## K. Binding Financial Agreement (s90B/C/D or s90UB/UC/UD)

| Item | Why |
|---|---|
| Complete asset + income disclosure (per C/D) | s90G validity — both parties' full disclosure required |
| Independent legal advice (each party, separate solicitors) | s90G validity gate |
| Signed BFA document | Foundation |
| Solicitor's certificate of advice for each party | s90G validity gate |
| Reason for BFA (pre-marriage / during / post-separation) | Determines which provision applies |

---

## The "no-holes" compliance artefacts (every matter, regardless of type)

These are the artefacts the solicitor produces — the client doesn't supply them, but the client must SIGN/RECEIVE them. Metis tracks their state so the matter doesn't stall.

| Artefact | Statutory base | Risk if missing |
|---|---|---|
| **Costs disclosure** | LPUL s174 | s178 voids costs agreement + blocks fee recovery — the highest-risk gap |
| **Costs agreement / retainer** | LPUL s180 | Same |
| **Engagement / confirming letter** | Professional practice | Scope ambiguity → conflict + scope creep |
| **Conflict-check record** | ASCR rr.10-12 | Disciplinary + breach of fiduciary |
| **Client identification + verification record** | LPUL + AUSTRAC if money-handling | Same |

And the 10-element file note (per Sewell v Zelden [2010] NSWSC 1180):
- Date / time / duration
- Everyone present + capacity
- Client's account
- Advice given (substance)
- Options presented
- 🔴 **Risks warned of**
- 🔴 **Client's response, especially decision NOT to follow advice**
- Instructions received
- Next steps + owner + timeframe
- Costs discussed

The two 🔴 elements are the ones that decide negligence/complaint outcomes — Metis client side surfaces these to the client BEFORE the conference so the solicitor doesn't have to extract them under pressure.

---

## Family-law process gates (Metis must detect + flag)

These don't add documents; they trigger procedural requirements:

| Gate | Why |
|---|---|
| **s60I / FDR certificate** | Required before parenting filing in FCFCOA (some exemptions — FV, urgency, child abuse) |
| **Pre-action genuine steps** | FCFCOA Practice Direction |
| **Family violence screening (s4AB + Lighthouse)** | Every matter, especially parenting — affects FDR exemption, FV economic-effect adjustment, safety planning |
| **Full + frank financial disclosure** (s71B married / s90RI de facto) | Ongoing duty — undertaking-backed, breach = contempt/costs |
| **Time limits** | 12 months post-divorce (married property), 2 years post-separation (de facto property) |
| **Urgency triggers** | FV protection orders, child recovery, urgent property (Mareva-equivalent), DPO blocking travel |

---

## Matter × Phase build mapping (what Metis supports when)

| Matter | Phase 1 (DPO prototype) | Phase 2 (post-first-paying-firm) | Phase 3 (Year 2) |
|---|---|---|---|
| F. DPO / s.111C stay (T1) | ✅ **Full template** — Peter's matter | + Basiq banking auto + voice channel + multi-tenancy | — |
| E. Child support administrative (T2) | partial — depends on T1 overlap | ✅ Full template | — |
| C. Parenting orders (T3) | — | ✅ Full template | + Lighthouse + FCFCOA forms |
| D. Property settlement (T4) | — | ✅ Full template (lighter) | ✅ Full + business valuations + super splitting |
| Initial-consult prep (T5 — matter-agnostic, just gather everything) | — | ✅ Universal template | — |
| A. Divorce | — | — | ✅ Year 2 |
| B. Separation (informal) | — | — | ✅ Year 2 |
| G. FV / AVO | — | partial (referral only — too sensitive) | ✅ With specialised safety architecture |
| H. Consent orders | — | — | ✅ |
| I. Mediation / FDR prep | — | — | ✅ |
| J. International / Hague | — | — | Year 3 |
| K. BFA | — | — | Year 3 |

---

## What this means for Phase 1 (Metis-for-Peter / DPO matter)

The T1 (DPO stay) template needs to gather, organise, draft, and matter-pack:

**Section F intake (DPO-specific)** — already documented above.

Cross-cutting Universal intake:
- Peter has done his own ID + contact + conflict (no opposing solicitor)
- Peter is self-represented — costs disclosure isn't applicable (no fee being charged to him)
- Engagement context is documented in REDLINE + STATUS
- FV screening — not applicable to this matter (no FV alleged either way)

**The 5 outstanding pre-requisites** mapped to intake categories:
1. **DSK income lodgement (ATO)** — Section C income (own business income) + Section F current income evidence
2. **SA written confirmation** — Section F services Australia correspondence
3. **DPO copy** — Section F DPO copy
4. **Tempe net proceeds breakdown** — Section C asset pool + Section C pre-relationship/post-separation evidence + Section F one-off income event documentation
5. **Trust register figures** — Section C asset pool / trust interests + Section F trust interests (full disclosure)

Phase 1 build supports each of these via:
- Guided walkthrough to retrieve (myGov ATO, Services Australia, ASIC Connect)
- Manual upload + OCR for paper/scanned docs
- Conversational follow-up to fill gaps Metis identifies
- Automatic re-generation of affidavit Paras 19, 24(a), 16, 23B v3, 23C as inputs arrive
- Adversarial-critique re-run after each material update
- Matter Pack export at end (FCFCOA-ready)

This doc IS the spec input for the Phase 1 document inventory generator.

---

## What's still needed (next iteration)

1. **Per-jurisdiction recording-law map** for the voice channel (NSW done; VIC/QLD/SA/WA/ACT/TAS for national Phase 3)
2. **Family violence safety modes** — special UI + retention policy when FV is flagged (Phase 2 minimum)
3. **Mature checklist updates** as 2025 reforms case law develops (six-monthly review cadence)
4. **Validation against an actual solicitor's intake form** — best done as part of the Mom-Test conversations (ask each cohort A solicitor: "what do you ask new clients to bring? Anything we missed?")

---

*This document supersedes the document-inventory sketch in METIS-CLIENT-WORKFLOW-SPEC.md Stage 2; that spec should reference this doc rather than duplicate it.*
