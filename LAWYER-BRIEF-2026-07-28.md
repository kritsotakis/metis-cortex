# Metis — brief for legal review

**Prepared:** 28 July 2026
**For:** a practising Australian solicitor (family law and/or legal-practice regulation)
**Purpose:** one specific question — *which parts of this can be offered to other people, and on what conditions?*

This is not a request for a general risk assessment. The tool exists, it works, and
one invited user has access. What's needed is a line drawn in a place we can build to.

---

## 1. The single question

Metis does, for its builder's own matter, considerably more than it currently
offers to anyone else. That gap is deliberate — it was drawn conservatively out
of caution, not analysis — and we now want it drawn correctly.

**What it currently offers a user:**

| Capability | Status |
|---|---|
| Document checklist per matter type, with why each item matters and where to get it | Live |
| Document upload, PDF text extraction, tracking what's held vs outstanding | Live |
| Q&A that explains process and terminology, refuses advice | Live |
| A "summary for your first appointment" form — user's own words into labelled fields | Live |
| Export: an inventory pack listing what's held and what's outstanding | Live |

**What it has produced for the builder's own (self-represented) matter, via a
general-purpose AI assistant rather than this product:**

- An initiating application and a 27-paragraph affidavit
- Cover letters, an FOI request, a substantive response to a statutory body
- Analysis of a medical report and a work-capacity decision
- An adversarial critique that identified five material problems in his own drafts

**The question:** how much of the second list can be offered to a third party,
and under what supervision model?

---

## 2. Why we think the line is not where our disclaimers assumed

We found *Van der Feltz* [2017] WASC 2 — a conviction for advertising to assist
self-represented litigants to complete applications and draft affidavits. As we
read it, the court considered that stating one is not a lawyer *"did not affect
the nature of the work."* The Victorian Legal Services Board has published to
similar effect regarding disclaimers.

We have also seen the distinction framed as: **completing blanks in a form is
clerical; producing a document from a body of facts, having analysed its legal
effect, is legal practice.**

If that is right, then:

- The checklist, the explanations and the "user writes their own answers into
  labelled fields" form are likely on the safe side.
- Generating an affidavit from a user's documents is likely not — **and no
  disclaimer changes that.**

**We would like this confirmed or corrected.** Our disclaimers are currently
doing work we may be wrong to ask of them.

---

## 3. The model we would like assessed

Not "AI advises the public". Rather:

> Metis prepares drafts. **A solicitor reviews and adopts them.** The solicitor
> is the one practising law; Metis is a drafting tool used under supervision —
> the position a paralegal or junior occupies.

Questions on that model:

1. Does supervised sign-off resolve the concern in §2, or does the *preparation*
   remain the problem regardless of who signs?
2. What would make the review genuine rather than a rubber stamp — and what
   record of it would you want to exist? We can build whatever is needed
   (surfacing what the AI was uncertain about, an audit trail of what changed).
3. Would a professional indemnity insurer accept AI-prepared work reviewed this
   way? Is this a conversation to have with Lawcover before building further?
4. Is there a defensible middle tier — research and explanation to anyone,
   drafting only where a solicitor is engaged?

---

## 4. Court AI rules — please confirm we've read these correctly

The FCFCOA issued a **Practice Direction on the use of artificial intelligence
on 29 May 2026** which, as we read it, applies to self-represented litigants and
not only practitioners: the filer remains responsible, and AI-assisted material
must be verified before filing.

Separately, in *Helmold & Mariya (No 2)* [2025] FedCFamC1A 163 a
self-represented litigant appears to have been penalised over fabricated
authorities.

**What we have done in response:** Metis now refuses to produce any case
citation at all — including ones it would get right — on the reasoning that a
user who cannot verify a citation cannot distinguish a correct one from a
fabrication. The Practice Direction is disclosed in the user agreement.

**Questions:** is that response proportionate, or over-corrected? And does
inputting matter material into an overseas AI provider raise an issue under
Part XIVB or otherwise that we should be handling differently?

---

## 4A. User-supervised browser automation — a separate question we need answered

We want Metis to help clients retrieve their own documents from myGov, ATO
online services, Child Support online and the Commonwealth Courts Portal. None
of these offer any public API for individuals; that appears to be deliberate.

We see two patterns with, we think, very different risk profiles:

1. **Unattended robotic access** — our system holds the client's credentials and
   logs in by itself. We assume this breaches those services' terms and we are
   **not** proposing it.
2. **User-supervised co-pilot** — the client logs in themselves and completes
   any 2FA, then, while watching, allows Metis to drive navigation in their own
   browser session: locate the right pages, download the right documents. Every
   action is logged and narrated, the client can stop at any point, and anything
   irreversible (submitting a form, changing a detail, making a payment) is
   never automated.

**Questions:**

1. Is pattern 2 meaningfully distinct from pattern 1 for the purposes of these
   services' terms of use, and of the Commonwealth computer-offence provisions?
   Our working view is that an AI assisting a logged-in, present, supervising
   user is closer to assistive technology than to robotic access — but that is
   our view, not advice, and we would rather be told we are wrong now.
2. Does it matter which of these implementations we choose — a browser
   extension running in the client's own browser, versus a browser embedded in
   our application?
3. If the answer is that we should not do this at all, our fallback is
   step-by-step written instructions and the client downloading and uploading
   the documents themselves. We are content with that outcome; we would just
   like to know.

Banking is a separate case: the Consumer Data Right provides a regulated path,
which we would use via an accredited sponsor rather than seeking accreditation
ourselves.

---

## 5. Documents we would like reviewed

Two categories, with different urgency.

**A. Client-facing, in use now (one invited user):**
1. Client agreement / disclaimer shown before any access — *is this doing what
   we think it is?*
2. The document checklists (parenting, child-support stay, first-appointment) —
   *is anything here advice rather than information?*
3. The exported matter pack — *the export is arguably the point of exposure; is
   its framing right?*

**B. Solicitor-facing, built but NOT in use, pending this review:**
4. Costs disclosure (LPUL s174/s178) generator
5. Costs agreement / engagement letter (s180) generator

On 4 and 5 we have deliberately **not** drafted the four s174 client-rights
statements — the output carries a visible `[LAWYER TO CONFIRM EXACT WORDING]`
placeholder, on the basis that visibly incomplete is safer than plausibly wrong.
Given s178 (a non-compliant disclosure voids the costs agreement and blocks
recovery), we would rather you wrote that wording than checked ours.

---

## 6. What we are not asking

- Not asking whether to build it. It's built.
- Not asking for a general risk register.
- Not asking you to approve the software.

We're asking where the line sits, so we can build up to it and stop.

---

## 7. Current posture, for context

- One user, personally known to the builder, who has accepted the agreement terms.
- Not open to the public. Sign-in is invitation-only.
- Hosted in Sydney; AI processing occurs overseas and this is disclosed.
- Publicly, the solicitor-facing product is marked "coming soon" precisely
  because of the items in §5B.
- No fees charged to anyone.

---

## Appendix — available on request

- The 11 drafts referred to in §1, from the builder's own matter
- The adversarial critique and the five issues it raised
- The full client agreement text
- A live walkthrough of the tool
