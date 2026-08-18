# DPO lessons → Metis: assessment and build recommendation
**Written:** 18 Aug 2026, ~23:45 · **Input:** `LESSONS-FROM-THE-DPO-MATTER-2026-08-18.md` (field report, objection lodged tonight, receipt 19674587) + `~/.claude/skills/legal-filing-check/SKILL.md` · **Method:** each of the eight §4 implications checked against the actual codebase (`server/keyDates.ts`, `courtForms.ts`, `matterTemplates.ts`, `matterPack.ts`, `routers/metis.ts`, `routers/consultation.ts`, `Home.tsx`), not against memory of it.

Treating the field report as primary evidence, as asked. Where it says "already exists", I checked; two of the three "already built" assumptions in the brief are only partly true.

---

## 1. The eight implications vs what Metis does today

| # | Implication | Status | What actually exists / what's missing |
|---|---|---|---|
| 1 | **Consistency scan across the pack** | **Not built** | Nothing reads across documents. The pack export is inventory-only (by design — `matterPack.ts` says so). No figure/date/name extraction, no cross-reference. |
| 2 | **Adversarial + editorial pre-lodgement review** | **Not built** | The only "review" step is the guided-form export banner ("written by the client, not a lawyer"). No adversarial read, no relief-ladder prompt, no editorial pass. |
| 3 | **Provenance on every figure/date** | **Not built** | Documents can be *linked* to checklist items (`matterChecklistLinks`), which is item-level provenance. But form answers, key dates and chat claims carry no "which document, which page". Documents don't even carry page-level text offsets. |
| 4 | **Client-input fields the assistant refuses to guess** | **Partly built** | The UPL line holds: `enforceRails()` blocks advice-shaped output; court forms are client-typed with a "written by the client" export banner; `lawyerGate` fields exist. **But** nothing stops Ask Metis from *suggesting* a dollar figure or frequency if asked "what should I put?" — the rails catch advice, not invented facts. The refusal-with-reason ("this is something you attest to; I format, you supply") is not a coded behaviour. |
| 5 | **"Lodge-anyway" date before the deadline** | **Partly built** | Key-dates tracker exists (`keyDates.ts`, `matterKeyDates`) with passed/soon(≤30d)/ok. There is no second, earlier, user-set "act by" date, and "soon" is a colour, not a nudge. Cheapest item on the list. |
| 6 | **Reviewer-not-editor for the solicitor bridge** | **Already built** | The bridge (`matterShares`, v170–172) is exactly this shape: the solicitor sees and *copies*; never writes into the client's file. Nothing to do. |
| 7 | **Template guidance against backdating** | **Not built** | Zero hits for backdating/reconstruction anywhere in templates, forms or guides. The one guide mention ("isn't backdated") is about aged-care funding, unrelated. |
| 8 | **"What changed since you last saw this" for the solicitor** | **Not built** | The bridge shows the client's current document list; no version history, no diff, no "new since your last visit". |

Honest tally: **1 built, 2 partly, 5 not built.** The brief's instinct that "several may already exist" is right for the bridge and half-right for key dates and the UPL line.

---

## 2. What to build, in what order

Peter's instinct is the top three (consistency scan, adversarial review, provenance). I mostly agree, but the **order and shape** should change, for two evidence-based reasons:

**(a) Provenance is a prerequisite for the consistency scan, not a sibling.** A scan that says "your affidavit says $34k and your objection says $50k" is only useful if it can also say *which is sourced* — otherwise it flags a conflict and can't rank it. §1.2 of the report is the mechanism by which §1.1's conflicts got resolved (ledger beat recollection). Build provenance first, thin.

**(b) The cheapest, most-evidenced items should ship this week, before the big ones.** #5 (lodge-anyway date) and #7 (backdating guidance) are hours of work each, both directly evidenced, and both are the kind of thing a stressed self-represented person is most tempted into. There's no reason they wait behind a multi-week feature.

### Recommended order

**Wave 0 — this week, small (≈1 day total)**
- **#5 Lodge-anyway date.** Add an optional `actByAt` to `matterKeyDates`, defaulting to 7 days before any hard deadline; the checklist/dashboard nudge treats *that* as the real date; copy explains why ("professional review improves a document; the deadline is jurisdictional"). Also surface it in the solicitor's key-dates view.
- **#7 Backdating guidance.** One paragraph in every acknowledgment / statutory-declaration / statement template and the relevant guides: *dated today about past events — fine; framed as written earlier — never, even if it would help.* Plus a rails check: if the user asks Ask Metis to "date this as of [past date]", refuse and explain.
- **#4 completion.** Extend `enforceRails()` (or a sibling `refuseToAttest()`) with the fact-invention case: when asked to supply a figure/frequency/date the user will attest to, the assistant declines and asks for the real number, saying why. Pin with a rails test.

**Wave 1 — provenance, thin (≈1 week)**
- Store page-level text for extracted documents (they already have `extractedText`; add page boundaries).
- Any figure/date the user enters into a court form or key date can be **linked to a document + page** ("where did this come from?"), reusing the checklist-link pattern. Optional at first; the pack shows a ✅ source or "unsourced" per figure.
- Ask Metis, when it quotes a figure from a document, cites file + page (it already reads the docs; this is a prompt + output-format change).

**Wave 2 — consistency scan (≈2 weeks, the real feature)**
- Extract candidate facts (money, dates, names, case numbers) from every document in the matter + form answers.
- Cluster by entity; flag disagreements ("$33,998.88 in the loan exhibit vs $34,000 in your form answer"; "father: James in doc A, Dimitrios in doc B").
- Present as a *pre-export report* — the pack won't say "consistent", it will say "we found N places where documents disagree; here they are". Honesty rule: this is a suggestion list, not a verdict.
- No competitor does this. It is the DPO matter's single biggest lesson (§1.1).

**Wave 3 — adversarial + editorial review (≈1–2 weeks, but the UPL design is the hard part)**
- Two model passes over a draft the user is about to lodge: **adversarial** ("read this as the other side — what does it hand them? what's missing — relief ladder, non-recurrence argument?") and **editorial** (uncorroborated claims, tense drift, attachments list vs attachments, tone).
- **This is the one that needs care on the client side.** "What does this paragraph hand the other side" is a hair from legal advice. Two safe framings: (i) ship it on the **solicitor side first** — a solicitor reviewing a client's pack gets the adversarial read; that's professional support, squarely inside the line; (ii) on the client side, restrict output to *questions* ("have you considered how paragraph 3 reads to a decision-maker?") and mechanical findings (unsourced figure, uncorroborated claim, missing alternative ask), never "remove this". Recommend (i) first, then (ii) once the wording has been through the same lawyer review the templates need.

**Wave 4 — bridge diff (#8, ≈3 days)** — snapshot the shared document list per solicitor visit; show "new/changed since [date]". Cheap once Wave 1 exists.

### Push-back on the instinct
Ship the small ones first, and put adversarial review on the **solicitor side** before the client side. The report itself says the adversarial pass is what turned a "narrow but not defeat" objection into a good one — but it also says John's judgement was the load-bearing review. Give the adversarial tool to John. It's the strongest possible version of "the pack lets a solicitor review rather than build" (§1.8), and it doesn't strain the UPL line.

---

## 3. Section 5 vs the homepage and pitch — anything overclaiming?

Checked `Home.tsx`, `publicChat.ts` system prompt, and the office-manager pack. Verdict: **the honesty rails hold; two soft spots.**

**Holds:**
- Explicit trust tile: *"Not a substitute for a lawyer … does not give legal advice … built to make the lawyer you see more useful, not to replace them."* That is §5.1, verbatim in spirit.
- Solicitor section frames the tool as "a second chair", with the FRL check scoped honestly ("State law, sections and case law flagged for the solicitor to verify").
- Nothing says Metis "knows the law". Guides are primary-source verified; the public chat is told it gives no advice and cites no cases.

**Soft spots (worth tightening, not urgent):**
1. Hero line: *"Metis tells you which documents your kind of matter actually needs."* Defensible (it's a checklist by matter type), but "tells you" is a knowing-verb. Consider "shows you the list of documents matters like yours usually need". Small.
2. Solicitor section: *"has the file note, case brief and client proposal drafted before the client leaves the room."* True of the software, but paired with the DPO evidence it should carry the qualifier the whole report is about — *drafted for the solicitor to review*, not drafted full stop. Add "for your review" and it's exactly right.
3. Office-manager pack §1 ("the paralegal a suburban firm can't hire") — fine, and §5.1's "make his hour count" framing should be added as a sentence, since it's now evidenced.

**The §6 homepage line** ("A real matter, run this way, was reviewed by a solicitor for $1,100 who said 'very happy — just remove the drafting notes'") is true and usable — with two cautions: (a) it's the founder's own matter, so say so or it reads as a customer testimonial; (b) don't put a dollar figure next to "solicitor" in a way that implies a Metis price. Suggested wording: *"The founder ran his own matter this way. The solicitor who reviewed the pack said 'very happy — just remove the drafting notes.' The pack did the organising; the solicitor did the judging."*

---

## 4. The skill's seven rules — product behaviour or Claude skill?

| Rule | Verdict |
|---|---|
| 1. Never fill in a fact the client attests to | **Product behaviour.** It's the UPL line *and* good paralegal practice — belongs in `enforceRails`, not in a skill only Peter's Claude reads. (Wave 0.) |
| 2. Ledger beats recollection; verify on the document's face | **Product behaviour, partially.** Provenance (Wave 1) is the product form. "Verify on the face" becomes a nudge when a date is entered without a linked page. |
| 3. No reconstructed/backdated documents | **Product behaviour.** Template guidance + a rails refusal (Wave 0). |
| 4. Deadline first, fallback date set | **Product behaviour.** Lodge-anyway date (Wave 0). |
| 5. One story everywhere | **Product behaviour.** The consistency scan *is* this rule (Wave 2). |
| 6. Unresolved characterisations stay unresolved | **Product behaviour, light.** A per-matter "open questions" list that blocks the export banner from saying "ready" — but doesn't block export. Cheap; fold into Wave 2. |
| 7. One session in control | **Already the product's shape** (bridge = reviewer-not-editor). Nothing to add. |

**Pre-lodgement checklist:** the mechanical steps — placeholder scan (`[`, `TBC`, `&nbsp;`, `INSERT`), attachments-list-vs-attached reconciliation, render check of the produced PDF — are trivially product features and should be the first thing Wave 2's report runs before any model is involved. The judgement steps (adversarial, editorial) are Wave 3.

**What stays a skill:** the *operating discipline* for an AI running a live matter end-to-end (session control, when to escalate, how to absorb a cross-check). That's Peter's working method, not a product surface — Metis's users don't run matters through Claude Code.

---

## 5. Not doing / explicitly parked
- Not putting client-side adversarial review live before lawyer review of its wording. It's the highest-value and highest-UPL-risk item; sequencing it behind the solicitor-side version is deliberate.
- Not touching the family-law-only framing anywhere — §5.3 is right that the method is general, and the product is already multi-area.
