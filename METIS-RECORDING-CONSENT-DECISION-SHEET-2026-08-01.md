# Metis Cortex — recording consent: decision sheet for legal review

**Prepared:** 1 August 2026
**Status:** Questions only. No recording workflow exists yet and none will be built until these are
answered — this document is deliberately not a design for approval, it's the input a design needs.

---

## Context

The solicitor-side product is meant to record a client conference (with consent), transcribe it, and
draft a file note, case brief, and client proposal from it. **None of this is built yet.** The
conference-capture UI exists in skeleton form, but the actual recording mechanism, the consent
mechanism, and the retention/deletion logic for what's captured have not been implemented. We're
asking these questions before building any of it, not reviewing a workflow that already exists.

Two things already on the record from the 28 July brief, restated here because they bear directly on
these questions:

- The **FCFCOA Practice Direction on AI (29 May 2026)**, as we read it, applies to self-represented
  litigants as well as practitioners, requires verification and accountability for AI-assisted
  material, and prohibits AI recording/transcription devices in **court proceedings** specifically.
- We have not yet confirmed how the NSW Surveillance Devices Act's consent requirements interact with
  a solicitor-conducted client conference specifically, as distinct from the FCFCOA's own rules.

---

## 1. Who must consent, and how is consent captured

**The question:** Every participant in a conference, or only the client? Does the solicitor's own
participation need separate consent, or is that implicit in them running the meeting? If a third party
joins (a support person, an interpreter, a colleague), do they need to consent too, and does the
meeting need to pause until they do?

**How captured:** a checkbox before recording starts, a verbal statement captured in the recording
itself, a signed form beforehand, or some combination — and what evidentiary weight does each carry if
consent is later disputed?

---

## 2. Whether consent must be renewed each conference

**The question:** if the same client has multiple conferences over the life of a matter, does consent
need to be re-obtained every time, or does a standing consent (e.g., given once at retainer) cover the
whole matter? Does anything change if a conference is rescheduled, or if a different solicitor at the
same firm conducts a later session?

---

## 3. Withdrawal and refusal handling

**The question:** if a client refuses to consent, or withdraws consent mid-conference, what has to
happen technically — does recording stop immediately, does anything already captured get discarded, or
retained but flagged as non-consensual and unusable? What does the solicitor need to be able to do in
that moment (a clear, fast "stop and delete" action), and what does the system need to guarantee about
that action actually being irreversible?

---

## 4. Recording, transcript, and audio retention/deletion

**The question:** how long should the raw audio be kept after a transcript is generated — deleted
immediately once transcribed, kept for the life of the matter, kept for a fixed period? Does the
transcript itself have different retention rules than the audio? Who can request deletion (client,
solicitor, both), and does a professional obligation to retain file records for a minimum period
override a client's deletion request?

---

## 5. Third-party transcription and overseas disclosure

**The question:** transcription would run through Deepgram (not currently configured or active — see
the subprocessor register). What needs to be disclosed to the client about that specific third party
before a conference is recorded, separately from the general privacy policy? Does the answer change
depending on where Deepgram processes the audio, and if so, what do we need to find out from them
before this can be answered?

---

## 6. Privilege / confidentiality wording

**The question:** what should the consent language itself say about legal professional privilege — does
recording the conference create any risk to privilege that needs to be disclosed or waived explicitly,
and is there specific wording that protects privilege that we should be using rather than drafting
ourselves?

---

## 7. Prohibited settings, including court proceedings

**The question:** beyond the FCFCOA's own prohibition on AI recording in court proceedings, what other
settings should this feature refuse to operate in — mediation or FDR sessions, family consultant or
expert conferences, anything else? Should the product technically prevent recording in these contexts
(and if so, how would it know it's in one), or is this purely a matter of solicitor training and
policy?

---

## 8. Required audit evidence

**The question:** what record of consent should exist after the fact, and for how long — a timestamp
and checkbox state, the actual consent statement captured in the recording, a separate signed
document? What would you want to be able to point to if a client later disputed that they'd consented?

---

## What we're asking for

Not a drafted policy. Not a workflow to approve. Answers to the eight questions above, in whatever form
is useful — even "this needs case-by-case judgment, don't build a single fixed workflow for it" is a
real, usable answer. Once we have that, the actual recording-consent mechanism gets designed and built
against it, and *that* implementation comes back for review before it's used on any real conference.
