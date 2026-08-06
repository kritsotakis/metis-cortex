# Metis — Red-Team Note: live-law grounding vs the UPL line (2026-06-26)

**Context.** A hard, *out-of-domain* legal question (an Australian financial-services / AFSL
regulatory assessment of EXIT CODE's "v2 gated execution" feature) was used to test the Metis
engine. Two passes were run: (A) answer from model memory; (B) answer after **retrieving the
actual law** (s766C / s766B / s911A from AustLII via the live browser, plus ASIC RG 36). This note
captures what the test proved — both the capability and the danger — so it feeds the build.

---

## 1. What live-law retrieval fixed (the moat working)

| Dimension | Memory pass (A) | Live-law pass (B) |
|---|---|---|
| Core call | "arranging ≈ dealing, ~75% confident" | Same call, **~80%**, anchored to verbatim s766C(2) |
| Key correction | "trader does it themselves" treated loosely | **s766C(3) read exactly**: the "deals on their own behalf" exemption protects the *trader*, NOT the *arranger*; s766C(3A) confirms acting *for another* ≠ "own behalf". This sharpened the verdict and removed a soft spot. |
| Carve-out hunt | generic "no execution-only exemption" | Pinned to the **actual s766C(2) text** ("unless … financial product advice") + flagged **s766C(7) → reg 7.6.01** as the only place a real carve-out could live |
| Cheapest path | "become a CAR / broker structure" (described) | Mapped to the **literal statutory exemptions**: s911A(2)(a) representative + s911A(2)(b) intermediary authorisation |

**Lesson:** retrieving primary law didn't just add citations — it **changed a substantive
conclusion** (the s766C(3) point) and raised calibrated confidence. Grounding > memory. This is the
Metis thesis (AustLII-live + current-law cognition) demonstrated on a cold, hard problem.

---

## 2. The red-team finding (the danger)

**Even with the law correct, the engine produced ADVICE-SHAPED output:** a verdict ("v2 needs a
licence, ~80%"), a **recommended** path, and a **ranked** option table with cost/time.

That is exactly the line Metis's architecture is designed **not** to cross. Under the product's own
UPL safe-harbour (see `METIS-CLIENT-WORKFLOW-SPEC.md`): organise/draft/flag = OK; **recommend /
opine on merits / "you should do X" / rank options as a recommendation = NEVER.** The raw model
will cross that line by default unless the **product hard-rails it**.

Second danger: the question was **financial-services law — entirely outside Metis's family-law
domain** — and the model answered confidently anyway. A Metis that answers AFSL questions is
"generic legal AI", which is both the positioning the external reviews told us to avoid and a
liability vector (out-of-domain = no current-law tuning, no consent/UPL scaffolding).

---

## 3. Build implications (locked)

1. **Live-law retrieval is the moat — invest in it.** AustLII + ASIC/Austlii grounding measurably
   beats memory. Keep it; widen coverage *within* family law (current statutes + recent cases).
2. **Guardrails must be SYSTEM-ENFORCED, not left to model discretion.** The model is happy to
   recommend; the system must stop it. Required gates:
   - **Advice-shape detector** — block/reframe output containing recommendations, merit opinions,
     "you should", ranked-recommendation tables, or a confidence-scored verdict on what to *do*.
   - **DRAFT watermark + "this is a legal call → confirm with your solicitor"** interrupts on every
     strategic fork (already specced — this test shows why it can't be optional).
3. **Domain lock.** Metis must **refuse/redirect out-of-domain** queries (anything not AU family
   law). An out-of-domain question should hit a hard "Metis only assists with Australian family-law
   matters" guard, not a confident answer.
4. **Calibrated-confidence + "what a lawyer must confirm" is good and should be retained** — the
   test produced an honest uncertainty list; that pattern is safe and should be a standard output
   block (it *defers* rather than *advises*).

**One-line takeaway:** *Live-law grounding strengthens the engine and raises the UPL stakes at the
same time. The retrieval is the moat; the rails that stop it recommending are the product.*

---

*Filed 2026-06-26 by Code. Source provisions retrieved live: [s766C](https://www5.austlii.edu.au/au/legis/cth/consol_act/ca2001172/s766c.html) · [s766B](https://www5.austlii.edu.au/au/legis/cth/consol_act/ca2001172/s766b.html) · [s911A](https://www5.austlii.edu.au/au/legis/cth/consol_act/ca2001172/s911a.html) · ASIC RG 36.*
