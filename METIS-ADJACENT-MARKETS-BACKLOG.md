# Metis — adjacent markets and third-party access (backlog, not now)

**Logged 2026-08-07.** Captured so it isn't lost, deliberately NOT scheduled.

**The gate on all of it:** Metis has zero paying customers, and the standing
decision in STATUS is *no more feature-building until 10 strangers pay*. Every
hour generalising the product is an hour not spent finding out whether anyone
pays for the specific thing. Revisit this file after that gate clears, or when
a paying customer asks for one of these by name.

---

## The observation (Justinas, via Peter, 2026-08-07)

Metis's underlying shape is generic: **one coordinator, many contributors, a
document checklist with deadlines and consequences.** That describes far more
than a parenting matter.

Named candidates:
- **Project managers on large jobs** — subcontractors, certifiers, councils,
  variations, defect reports
- **Real estate agents** — coordinating client, trades, solicitor, broker,
  strata manager through a settlement

---

## Why not now — the moat argument

What makes Metis defensible in law is exactly what does **not** transfer: the
LPUL s174/s178 compliance work, the *Sewell v Zelden* file-note fields, the UPL
rails, the practice-area templates, and the lawyer review being pursued. Strip
those out and the product is a checklist with uploads, competing with
Monday.com and Asana on their own ground with none of that advantage.

---

## The nearer adjacency, if this is pursued: CONVEYANCING

From `KONSTAN-LAWYERS-TEARDOWN-2026-08-07.md` — conveyancing is:
- an actual Konstan practice area (so a real first customer exists)
- extremely document-heavy (contract, s10.7 certificate, strata report, ID)
- LEAP-native, which fits the integration already in development
- **structurally the same thing Justinas described** — a client coordinating
  with an agent, a broker, a solicitor and a strata manager

It reaches the real-estate adjacency *through* the legal market rather than
abandoning it, and keeps the compliance credibility intact. If any of this gets
built, build this one first.

---

## ✅ The exception — THIRD-PARTY UPLOAD IS NOT IN THIS BACKLOG

Peter raised "let a third party such as an accountant upload documents" in the
same conversation. **That is not an adjacent-market feature — it is a missing
piece of the family-law product that already exists**, and should be built for
the current market:

- Property settlements require **full and frank financial disclosure**
  (s71B married / s90RI de facto). Those documents routinely sit with the
  client's **accountant**, not the client.
- Same shape: payslips from an employer, statements from a bank, a super fund.
- Today the checklist says "get your tax returns" and the client is a courier.

**The infrastructure already exists.** `server/phoneUpload.ts` implements a
signed, 15-minute, matter-scoped, **write-only** upload token for the
phone-camera handoff, which re-checks ownership at redemption. "Email this link
to your accountant" is the same primitive with different delivery — days, not
weeks.

Three requirements, all already modelled by the phone flow:
1. **Write-only.** The third party uploads and can never read the matter. An
   accountant must not see the client's family-violence documents.
2. **Client authorises each invite.** Not the solicitor acting unilaterally.
3. **Attributed and audited.** Every upload records who supplied it — now
   possible since `server/audit.ts` exists (2026-08-07).

Sequencing note: this overlaps the **solicitor-invites-their-client bridge**
(issue B1 in `METIS-ISSUE-REGISTER-2026-08-07.md`, the top-ten technical gap —
the client and solicitor sides are still separate data models). Both are
"someone other than the account owner contributes to a matter". Design the
permission model **once**, for both, rather than twice.
