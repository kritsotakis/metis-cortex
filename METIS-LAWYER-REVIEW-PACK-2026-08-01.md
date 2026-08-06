# Metis — solicitor-side compliance artefacts: lawyer review pack

**Prepared:** 1 August 2026
**For:** the same reviewer as [LAWYER-BRIEF-2026-07-28.md](LAWYER-BRIEF-2026-07-28.md) (or another practising
Australian solicitor / legal-practice regulation specialist)
**Purpose:** a structured sign-off pack for five specific artefacts, so review produces a decision on
each one — approved, approved with changes, or reworked — not just general commentary.

This is the practical companion to the 28 July brief, which asked open scoping questions (where does
the UPL line sit, does supervision resolve it). This document instead shows you **exactly what the
system generates**, verbatim, for the five things flagged there as "built but NOT in use, pending
review." Nothing here has been shown to a real client. Nothing generates without a solicitor manually
triggering it, and every generated document carries a hard-coded **"DRAFT — wording not
lawyer-reviewed, do not send to a client"** banner in the interface, not just a badge.

---

## How to use this document

Each of the five sections below has the same structure: what it is, exactly what gets generated
(the real prompt sent to the AI, or — for the two non-AI items — exactly what's recorded), what's
already been deliberately left unfinished and why, and a sign-off block.

For each item, please mark one:

> ☐ **Approved as-is** — safe to use once the other launch gates (PI insurance, data residency) clear
> ☐ **Approved with the changes noted below**
> ☐ **Not yet safe to use** — see notes

A summary table is at the end so you can fill in one line per item without re-reading if that's faster.

---

## 1. Costs disclosure (LPUL s174 / s178)

**What it is:** After a consultation, the solicitor enters the fee basis and a fee estimate range. The
system drafts the surrounding disclosure document. The solicitor sets every number; the AI never
sets or suggests a fee.

**Threshold logic applied** (per the app's own prior research against s174): estimate ≤$750 → no
disclosure technically required, but one is generated anyway for the file; $750–$3,000 → standard/
short-form; >$3,000 → full disclosure. This is computed from the solicitor-entered upper estimate.

**The exact prompt sent to the AI** (solicitor-entered values shown as placeholders):

> Draft a Legal Profession Uniform Law (LPUL) s174 costs disclosure document for an Australian
> family-law matter. Disclosure tier: `{NONE / STANDARD / FULL}`.
>
> Client: `{client name}`
> Matter: `{matter description}`
> Basis of costs (solicitor-supplied, do not alter the substance): `{solicitor's entered text}`
> Total estimate (ex GST/disbursements, solicitor-supplied, do not alter): `${low} - ${high}`
>
> Structure the document with clear headings: Basis of Costs, Estimate, and Your Rights. For the
> "Your Rights" section, do NOT write the actual statutory wording yourself — instead insert exactly
> this placeholder text, verbatim, as its own paragraph: "[LAWYER TO CONFIRM EXACT WORDING: the
> four s174 client-rights statements]". Keep the basis-of-costs and estimate sections professional
> and specific to the figures given — those parts are safe to draft in full since they're structural,
> not prescribed statutory text.

**Deliberately not drafted:** the four s174 client-rights statements. The output always contains the
literal placeholder `[LAWYER TO CONFIRM EXACT WORDING: the four s174 client-rights statements]`
instead of invented wording — on the basis that visibly incomplete is safer than plausibly wrong.
**This is the one piece of exact wording we'd like you to write**, rather than review — given s178
(a non-compliant disclosure voids the costs agreement and blocks fee recovery), we don't want to be
the ones drafting statutory rights language.

**What the solicitor sees in the interface, every time, before the document:**

> **DRAFT — wording not lawyer-reviewed.** Do not send to a client. A non-compliant disclosure voids
> the costs agreement and blocks fee recovery (LPUL s178).

**Sign-off:**
> ☐ Approved as-is · ☐ Approved with changes (below) · ☐ Not yet safe
>
> The four s174 rights statements (if you're willing to provide the exact wording here, we'll wire it
> in as a fixed, versioned block rather than AI-generated text):
>
> _______________________________________________________________
>
> Other changes needed:
>
> _______________________________________________________________

---

## 2. Costs agreement / engagement letter (LPUL s180)

**What it is:** The solicitor enters the scope of engagement and fee basis; the system drafts the
surrounding retainer/engagement letter structure.

**The exact prompt sent to the AI:**

> Draft a costs agreement / retainer (Legal Profession Uniform Law s180), functioning also as the
> engagement/confirming letter, for an Australian family-law matter.
>
> Client: `{client name}`
> Scope of engagement (solicitor-supplied, do not alter the substance): `{solicitor's entered text}`
> Basis of costs (solicitor-supplied, do not alter the substance): `{solicitor's entered text}`
>
> Structure with clear headings: Scope of Engagement, Basis of Costs, Termination, and Client
> Acknowledgement. Keep it professional and specific to what's supplied. This is a draft for
> solicitor review before use.

**What the solicitor sees in the interface, every time, before the document:**

> **DRAFT — wording not lawyer-reviewed.** Do not send to a client.

**Known gap:** unlike the costs disclosure, this prompt doesn't currently instruct the model to avoid
any specific prescribed statutory language — the four headings (Scope, Basis, Termination,
Acknowledgement) are ones we judged as structural rather than containing prescribed text. **Please
tell us if any part of an s180 agreement needs the same placeholder treatment as the s174 rights
statements.**

**Sign-off:**
> ☐ Approved as-is · ☐ Approved with changes (below) · ☐ Not yet safe
>
> Does any part of this need a "do not draft, insert placeholder" instruction like item 1?
>
> _______________________________________________________________
>
> Other changes needed:
>
> _______________________________________________________________

---

## 3. Case brief (post-conference)

**What it is:** After a consultation, the system drafts a structured brief from the transcript and
identified legal issues — for the solicitor's own working file, not client-facing.

**Why it's built as structured JSON, not free prose:** *Sewell v Zelden* [2010] NSWSC 1180 identifies
two fields that decide negligence/complaint outcomes — the risks warned of, and the client's response
(especially any decision not to follow advice). We made these mandatory schema fields the model
cannot silently omit, rather than sections inside a wall of prose it could skip.

**The exact prompt sent to the AI** (transcript and issues are the real consultation content):

> You are an expert Australian solicitor. Based on the consultation transcript and identified legal
> issues, create a structured case brief.
>
> Client consultation transcript: `{transcript}`
> Identified legal issues: `{issue list}`
> Relevant law: `{research findings}`
>
> Use Australian legal terminology and reference specific Australian legislation and case law.
>
> You MUST populate every field, including risksWarned and clientResponse. If the transcript
> genuinely contains no record of a risk being warned of, or no client response to advice being
> given, say exactly that ("Not recorded in this consultation — confirm with the file note") rather
> than leaving the field vague or omitting it — a missing negligence-critical field must be visibly
> missing, never silently absent.

**Schema fields forced on every generation:** Client Overview · Legal Issues Identified · Relevant
Law · Preliminary Assessment · **Risks Warned Of** · **Client's Response** · Recommended Next Steps.
If the model can't populate `risksWarned` or `clientResponse` from the transcript, the field is
filled with a visible fallback (`⚠️ Not recorded — confirm with the file note.`) rather than left
blank or omitted — verified with real transcripts containing and lacking this content.

**Known limitation:** this drafts research and legal-issue framing from a live transcript — closer to
independent legal analysis than the costs documents above, which only structure solicitor-supplied
numbers. **This is probably the item where your read on the UPL question in the 28 July brief matters
most** — we'd treat "not ready to use even under supervision" as a real answer, not a setback.

**Sign-off:**
> ☐ Approved as-is · ☐ Approved with changes (below) · ☐ Not yet safe
>
> Notes:
>
> _______________________________________________________________

---

## 4. Conflict check (ASCR rr10–12)

**What it is:** A plain factual record, captured as step 3 of the intake wizard before a consultation
starts. **No AI involved — nothing generated, nothing to review for wording**, only whether the
record captures what it should.

**What's recorded:**
- Names of the other party/parties involved
- Outcome: **Clear** / **Conflict identified** / **Needs review**
- Free-text notes (optional)
- Timestamp, and the solicitor who recorded it

**What's NOT recorded:** any narrative beyond the above — this is designed as a discrete, dated,
retained record, not a full conflict-search report.

**Sign-off:**
> ☐ Captures what's needed · ☐ Needs additional fields (below) · ☐ Not adequate
>
> Fields to add or change:
>
> _______________________________________________________________

---

## 5. Client identification / verification

**What it is:** Also step 3 of the intake wizard. A plain factual record that an ID document was
sighted — **no AI, nothing generated.**

**What's recorded:**
- Document type sighted (free text, e.g. "Driver licence")
- Whether it was sighted (yes/no)
- Free-text notes (optional)
- Timestamp, and the solicitor who recorded it

**Deliberate design choice — please confirm this is the right call:** we do **not** record the
document *number*, an image of the document, or any other identifying detail from it — only that a
document of a given type was sighted, and when. This was a data-minimisation decision (recording
*that* a check happened, dated and retained, satisfies "discrete, dated, retained" without creating a
new sensitive-data-at-rest liability by storing the ID number or a copy itself). **If regulatory
practice actually expects the document number or a copy retained, tell us and we'll add it** — right
now we've erred toward collecting less, not more.

**Sign-off:**
> ☐ This level of detail is adequate · ☐ More detail needed (below) · ☐ Not adequate
>
> What else needs to be captured:
>
> _______________________________________________________________

---

## Summary table

| # | Artefact | AI-generated? | Approved as-is | Approved with changes | Not yet safe |
|---|---|---|---|---|---|
| 1 | Costs disclosure (s174) | Yes — structure only, rights statements placeheld | ☐ | ☐ | ☐ |
| 2 | Costs agreement (s180) | Yes — structure only | ☐ | ☐ | ☐ |
| 3 | Case brief | Yes — from transcript | ☐ | ☐ | ☐ |
| 4 | Conflict check | No — factual record | ☐ | ☐ | ☐ |
| 5 | Client ID/verification | No — factual record | ☐ | ☐ | ☐ |

---

## What we're not asking here

Same as the 28 July brief: not asking whether to build these — they're built. Not asking for a
general risk register. Asking specifically: for each of the five, is it safe to put in front of a
real solicitor and a real client, and if not yet, precisely what has to change.

## Current posture, for context

- None of these five items are live. The solicitor-side product is publicly marked "coming soon."
- No fees charged to anyone; no real client data has passed through any of the five.
- Hosted in Sydney; AI processing (Anthropic Claude) occurs overseas and is disclosed in the
  [privacy policy](https://metiscortex.au/privacy) and [safety page](https://metiscortex.au/metis/safety).
- The other launch gates — professional indemnity cover, a formal AU data-residency review — are
  tracked separately and aren't part of what's being asked of you here.

## Appendix — available on request

- A live walkthrough of any of the five flows
- The full costs-disclosure/agreement generation code (`server/routers/consultation.ts`)
- The `matterTemplates.ts` / `legalKnowledge.ts` sources the case brief and client-side checklists
  draw on, if useful background
