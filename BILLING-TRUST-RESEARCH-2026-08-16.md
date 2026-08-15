# Billing & trust — primary-source research (2026-08-16)

Two questions Peter wanted answered before showing John/Konstan: (1) does the Metis billing model match how a suburban NSW family-law firm bills? (2) does a per-matter trust ledger mirror earn its keep next to LEAP's?

## 1. Billing — findings and what changed in Metis

- **6-minute units are the NSW norm, not law.** Law Society NSW precedent *Disclosure and Costs Agreement*: "Our charges are structured in 6 minute units. For example, the time charged for an attendance of up to 6 minutes will be 1 unit and the time charged for an attendance between 6 and 12 minutes will be 2 units." Real firms (ClearPath Navigating Family Law, Bathurst; PGG Legal) use the identical wording. Rounding is up to the next unit.
- **A minimum unit is chargeable only if disclosed.** LS Costs Guidebook 6th ed. 2.5.1: "if charges are to be levied on a minimum unit of time basis, this should be made clear to the client in the disclosure document or costs agreement. If this has not been done, then the law practice will only be able to charge for the actual time spent." LPUL s 172 (fair and reasonable) is the assessor's hook against padded units.
- **Rates are per fee-earner by seniority.** The LS precedent tables Partner / Senior Associate / Solicitor. Suburban NSW family firms 2025–26: Rafton (Penrith/Parramatta) $500–$700/h ex GST; PGG $750; Jameson Law guide $450–$750; paralegals ~$250. Legal Aid NSW Cth family rate $195/h (7 Apr 2025) and AG panel $336.23/h are regulated comparators, not private rates.
- **Fixed fees are standard for discrete work.** Consort Family Law: divorce (sole) $2,000, consent orders (property) $5,000, BFA from $6,000; Rafton: divorce $1,650, consent orders $4,400; Kate Austin: consent orders from $4,730.
- **Itemised bill content** (Guidebook Oct 2024, 2.4.7): date; description; practitioner names; duration; amount. LPUL s 187 (30-day request / 21-day comply), s 192 (client-rights notice must accompany the bill — statutory content, kept as [LAWYER TO CONFIRM] in Metis), s 188 (signed/nominated principal), s 191 (no charge for preparing bills), s 194 (no recovery until 30 days), s 198 (12-month assessment).
- **LEAP fee model** (LEAP AU help + leap.build API): unit length, per-staff billing rate, activity/task code, billable status. `POST /api/v2/fees` takes MatterGUID, WorkDoneByStaffGUID, TaskCodeGUID, TransactionDate, SecondsPerUnit, FeeUnits, RatePerHour, CalculationMode (0 hourly / 1 fixed), BillingDescription, BillingMode, ExternalURL/ExternalJSON. Access via LEAP Developer Console + Marketplace pre-approval.

**Changed in Metis (v145):** per-solicitor rate card; billing unit setting (default 360s rounded up; 60s = actual time) with the Guidebook caveat shown; actual minutes stored beside units; fixed-fee lines; activity codes; LEAP-shaped export (JSON rows in the /api/v2/fees shape + CSV).

**Open for John/Konstan:** which unit and rounding their agreement discloses; whether API push into LEAP is wanted (needs Marketplace onboarding) or CSV suffices; whether they run one rate or a seniority table.

## 2. Trust — findings and what changed in Metis

- **A per-matter trust ledger is a "trust record"** — LPUL s 128 (definition includes "trust ledger accounts", "records of monthly reconciliations"), s 147 (permanent form; must "at all times disclose the true position"; 7 years after last entry or matter finalisation, whichever is later; backups included).
- **Computerised systems must meet LPUGR rr 38–41**: month-end copies that "cannot be modified afterwards" (r 38(5)); chronological file-maintenance log (r 39); system "not capable of accepting … a transaction resulting in a debit balance" without a permanent exception report, no deletion of non-zero ledgers, no in-place amendment, sequential page numbering, mandatory fields (r 40); monthly off-site backups (r 41). Ledger per person per matter, balance after every entry, entries within 5 working days (r 47); monthly three-way reconciliation within 15 working days (r 48).
- **External examination is annual** (LPUL s 155); the LS External Examiner Checklist 2026 tests uncertified software line by line against rr 38–41 and short-circuits for Law Society **certified** software. LEAP is on the certified list. LEAP already shows a per-matter ledger (Trust Funds tab; Trust Ledger Report).
- **Overdrawn ledger = breach** — LPUL s 148 (500 penalty units / 5 years); LSJ Aug 2025: "Overdrawing a client's trust ledger is a breach, even by $1"; s 154 requires irregularities to be reported.
- **Common findings**: late reconciliations, stale adjusting items, dormant balances, overdrawn ledgers, unauthorised withdrawals — all inside the certified system's workflow.

**Decision:** an uncertified mirror ledger in Metis is a liability (drift = s 147(2)(b) problem; duplicate of what LEAP already provides). **Removed** in v145; the billing page points to the certified trust system. Nothing trust-shaped will be rebuilt unless a LEAP read-only feed becomes available and even then only as "as reported by LEAP at [time] — not a trust record".

Sources fetched (not from memory): legislation.nsw.gov.au LPUL + LPUGR consolidated text (via WA official mirror where NSW 403'd), lawsociety.com.au (precedent costs agreement, Costs Guidebook, EE Checklist 2026, certified-software list, FAQ 2020, EE Update 2020), lsj.com.au (Feb 2024, Aug 2025), leap.build API reference, LEAP AU help centre, firm websites named above.
