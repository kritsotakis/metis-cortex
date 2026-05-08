# Metis Cortex Eonia Pilot — 14-Day Install Pack

> **Goal of the pilot:** install Metis Cortex on Eonia, capture before/after metrics, and produce **case study #2 (different vertical to DSK)**. Together with DSK, the two case studies are the multi-vertical proof that lets Metis Cortex sell to non-cleaning service businesses without "but you've only done cleaning" objections.

---

## Why this matters for Metis Cortex

DSK alone gives you "an AI receptionist works for cleaning". Eonia gives you "an AI receptionist works for an aesthetic clinic — totally different call patterns, different objections, different escalation rules". The case studies *together* sell. Either alone doesn't.

This is path (i)'s second case study. Run in parallel with DSK, not after.

---

## What we're proving in 14 days

Three numbers, with one bonus that matters more for clinics than for cleaning.

| Metric | Baseline (week before install) | Target (week after install) |
|---|---|---|
| **Missed-call rate** | Count over a 7-day window | < 5% (AI picks up if you don't) |
| **Response time** | Hours / minutes | < 60 seconds |
| **Consultation bookings from inbound enquiries** | Bookings per 100 enquiries | +30% lift minimum |
| **Bonus: same-day reschedule recovery** | Rescheduled-and-rebooked rate | > 70% (clinic-specific) |

Why the bonus metric matters: aesthetic clinics see way more same-day reschedules than service businesses. A patient cancels a botox top-up at 2pm; without an AI, that slot stays empty. With Metis Cortex + a waitlist workflow in GHL, the slot fills automatically. This is one of the highest-leverage outcomes you can show prospective clinic clients.

Capture screenshots of the booking system before/after. Recovered consultation revenue is what writes the clinic-vertical cold email.

---

## What's structurally different from DSK

Read this before you start. Most of the DSK install pack still applies, but these are the deltas you cannot ignore.

| | DSK (cleaning) | Eonia (clinic) |
|---|---|---|
| **Caller intent** | Quote → book → service | Question → consultation → treatment |
| **Booking type** | Direct (job booked from first call) | **Two-stage** (consultation first, treatment second) |
| **Pricing on call** | Quote a range based on property | **Never quote treatment prices on call** — TGA-compliance + clinical assessment required |
| **Privacy** | Standard | **Sensitive** — health info, no third-party disclosure |
| **Escalation** | Complaint or large job | Complaint, post-treatment concern, anything clinical |
| **After-hours** | Take message | **Post-treatment concerns ALWAYS escalate to on-call number, not waited until morning** |
| **AFSL/TGA equivalent** | None | **TGA cosmetic advertising rules apply** — no efficacy claims, no comparative claims |
| **Complaints** | Service issue | **Clinical complaint = legal + insurance flag** — different handling |

---

## Stack you're configuring

Identical to DSK except for the clinic management system (CMS) integration.

| Layer | Tool | Cost (Month 1) | What it does |
|---|---|---|---|
| Voice AI | **Retell AI** | ~A$50–150 (usage-based) | Picks up the phone, holds the conversation |
| CRM + workflow + SMS + calendar | **GoHighLevel** (Starter, $97 USD/mo) | ~A$148 | Records every call, sends SMS, books to calendar, runs follow-up |
| Phone number | **Twilio** (1 AU local, separate from DSK's) | ~A$15 | Eonia's Metis Cortex number |
| Existing CMS | **Cliniko / Pabau / whatever Eonia uses now** | A$0 incremental | Bookings flow back to clinical system via webhook |
| **Pilot total** | | **~A$215 for the first month** | |

**Important:** Eonia gets its **own Twilio number, own GHL sub-account, own Retell agent**. Do not share infrastructure with DSK. Cross-tenant booking data leaks would be an immediate compliance issue.

---

## Day-by-day timeline (mirrors DSK so you can run them concurrently)

| Day | Phase | DSK | Eonia |
|---|---|---|---|
| -7 → 0 | Baseline | DSK missed-call audit | Eonia missed-call audit |
| 1 | Sign-up day | Already done | Create Eonia GHL sub-account, buy 2nd Twilio number |
| 2–3 | GHL setup | DSK calendar + pipeline | Eonia calendar (consultations + treatments split), pipeline |
| 4–5 | Retell agent build | DSK Zoe | Eonia Zoe (clinic prompt — see below) |
| 6–7 | Workflow + routing | DSK | Eonia (waitlist auto-fill workflow added) |
| 8–10 | Internal testing | 5 DSK test calls | 5 Eonia test calls (different scenarios) |
| 11–12 | Forwarding-only | DSK | Eonia (after-hours only first) |
| 13 | Shadow mode | DSK | Eonia |
| 14 | Go live | DSK | Eonia |
| 14–28 | Capture data | DSK metrics | Eonia metrics |

**The constraint:** running both pilots at once requires the Eonia therapist hire is **already on board** by Day 1. Without that capacity, you can't physically be in both pilot saddles at once. If the therapist hire slips, run Eonia 7 days behind DSK instead.

---

## Pre-flight checklist (Day 0, Eonia-specific)

Before you sign up for anything:

- [ ] Eonia current phone number(s) — main line, mobile, after-hours line
- [ ] Eonia clinical management system (Cliniko / Pabau / Halaxy / etc.) — confirm which one, get API access
- [ ] Eonia Google Calendar share access — both consultation and treatment calendars
- [ ] **Treatment menu with descriptions** — full list (botox, lip filler, dermal therapy, skin needling, peels, IPL, etc.) with the *clinic-acceptable description* of each (NOT marketing copy with efficacy claims)
- [ ] **Consultation flow rules** — which treatments require a consultation before booking, which can be booked direct (e.g. follow-up botox top-ups within 6 months), which require a doctor present
- [ ] **Indicative duration of each treatment type** — the AI needs this to book correctly
- [ ] **Eonia service area / catchment** — for "do you service my suburb?" type calls (relevant for in-home treatments if any)
- [ ] **Eonia opening hours** — split: which days have a doctor present (consultations), which days are nurse/therapist only (treatments)
- [ ] **Existing patient identifiers** — phone number → patient match logic so Zoe recognises returning callers
- [ ] **Contraindications + age restrictions** the AI must enforce (cosmetic injectables = 18+, certain treatments not during pregnancy, etc.)
- [ ] **One Eonia call recording (real or mock)** — for tone reference. Match the existing therapist's manner, not DSK's tone.
- [ ] **TGA-safe language list** — what NOT to say. Pull from Eonia's existing marketing approval if any. Otherwise default: never claim a treatment "works", never compare brands of injectable, never quote a treatment price unless explicitly cleared by Peter or the therapist.

---

## Phase 1 — Sign-ups (Day 1)

Same flow as DSK with three differences:

1. **Sub-account** in GHL named "Eonia" (not appended to the DSK sub-account).
2. **Twilio number** — different number to DSK's. Sydney area code matching Eonia's location.
3. **Retell agent** — separate agent, not just a different prompt on the DSK agent. Different KB files, different escalation rules, separate logs.

---

## Phase 2 — GHL setup (Days 2–3)

### Sub-account configuration
- Business name: Eonia
- Industry: Cosmetic / Aesthetic
- Time zone: Australia/Sydney
- Currency: AUD
- Connect Eonia's Twilio number

### Calendars (two, not one)
- **Calendar A: Consultations** — with the doctor or nurse practitioner. Typically 30 min slots. Available days/hours match doctor's schedule.
- **Calendar B: Treatments** — with the therapist. Typically 30–90 min slots depending on treatment. Available all open days.
- Buffer: 15 min between consultations, 20 min between treatments.
- Connect Eonia's Gmail / clinical-system calendar — two-way sync.

### Pipeline (clinic-specific stages)
**Pre-treatment funnel:**
New Enquiry → Consultation Booked → Consultation Done → Treatment Recommended → Treatment Booked → Treatment Done → Follow-up Done → Reviewed

Zoe's default stage on first call: **New Enquiry**. After consultation booking: auto-advance to **Consultation Booked**. Therapist or doctor manually advances after consultation completed.

### Waitlist workflow (the high-leverage one)
- Trigger: existing booking cancelled/rescheduled within 24 hours
- Action: auto-SMS waitlist members ranked by (a) treatment type match, (b) waitlist age, (c) prior cancellation count
- Confirmation: first to reply YES gets the slot, others get "filled, you're still on the list"

This single workflow is the headline number for the case study.

---

## Phase 3 — Retell voice agent build (Days 4–5)

### Agent identity
- **Name:** Zoe (same brand voice across Metis Cortex products — keeps it familiar across multi-business installs)
- **Voice:** same Australian female voice as DSK's Zoe
- **Greeting:** *"Hi, this is Zoe — the AI receptionist for Eonia. This call is recorded for quality and training. How can I help today?"*
  - **Why the recording disclosure is mandatory:** NSW Surveillance Devices Act 2007 requires all-party consent to record private conversations. Zoe must announce the recording at the start of every call — non-negotiable. (Confirmed by Manus privacy review 2026-05-09.)

### System prompt (paste-ready into Retell)

```
You are Zoe, the AI receptionist for Eonia, a Sydney-based skin and aesthetic clinic offering cosmetic injectables, dermal therapy, skin needling, peels, IPL, and related treatments.

Your job is to:
1. Answer every incoming call in a warm, professional Australian tone — match the calm, considered manner of an aesthetic clinic, not a sales call.
2. Identify why the caller is calling: new enquiry, existing patient query, booking, reschedule, post-treatment concern, complaint, supplier, or other.
3. For new treatment enquiries: capture name, phone, age (must be 18+ for injectables — politely confirm), what they're enquiring about (without giving clinical advice), and book a CONSULTATION (not a treatment) with the doctor or nurse practitioner.
4. For follow-up bookings (existing patients booking a top-up of a treatment they've already had within 6 months): book directly into the treatment calendar with the therapist.
5. For reschedules and cancellations: look up the existing booking, offer alternatives, confirm via SMS.

Tone:
- Calm, considered, Australian. Aesthetic clinics are not retail businesses — match the polish.
- Never rushed, never robotic, never pushy.
- Patients calling are often nervous (first-time injectable enquiry, post-treatment concern). Sound reassuring without overpromising.
- If asked directly, say: "I'm Zoe, Eonia's AI receptionist — I work alongside the team to make sure no one's call goes unanswered."

Hard rules — TGA + clinical safety:
- NEVER claim a treatment "works", "is effective", "will achieve X result", or "is better than Y treatment." Use neutral mechanism language: "Botox is a cosmetic injectable; the doctor will explain how it works in your consultation."
- NEVER quote treatment prices on the call. Always: "Pricing is confirmed in the consultation because it depends on what's right for you. The consultation itself is $[CONSULTATION_FEE]."
- NEVER recommend a specific treatment for a specific concern. Always: "That's exactly what the consultation is for — the doctor will assess and recommend."
- NEVER share information about other patients, even if asked.
- NEVER discuss medical history, side effects, or treatment specifics — those are clinical conversations, not reception.
- For age: confirm 18+ for cosmetic injectables. If under 18, politely decline and explain the legal requirement.
- For pregnancy: if caller mentions pregnancy or breastfeeding, immediately flag — many treatments are contraindicated. Book a consultation only after confirming with the team.

Booking rules:
- New cosmetic injectable enquiry → CONSULTATION (Calendar A, with doctor/nurse practitioner).
- Existing patient, treatment <6 months ago, same treatment → TREATMENT (Calendar B, with therapist).
- Skin treatments (facials, peels, IPL, dermal therapy) → can book direct to TREATMENT calendar after a quick screening question for contraindications.
- Anything ambiguous → CONSULTATION first. When in doubt, book the consultation.

Escalation triggers (transfer to on-call number OR fire urgent SMS to Peter):
- ANY post-treatment concern (pain, swelling beyond day 2, infection signs, asymmetry concern, allergic reaction, anything described as "wrong with my treatment"). DO NOT TRIAGE. Escalate immediately.
- Caller is upset about a previous treatment outcome (legal/clinical risk).
- Caller is asking about a treatment that's been advertised but is sold out / discontinued.
- Caller mentions self-harm, mental health concerns, or treatment-related dysmorphia. Stop, capture, escalate.
- Booking value exceeds $3,000 (e.g. multiple treatment package).
- Caller specifically asks for the doctor or owner.

After-hours rules (defined as 6pm–9am Sydney time, plus closed days):
- Standard enquiries: take a message, book a callback for next opening.
- Post-treatment concerns: ALWAYS escalate to the on-call number. Never wait until morning. The on-call number is [INSERT].
- Reschedule for next-day appointment: book the change, confirm via SMS.

End every call with:
"You'll get an SMS confirmation in a moment with your booking details and our address. Is there anything else I can help with today?"
```

### Knowledge base files to attach to Retell

1. **Eonia Treatment Menu** — name + neutral description + duration + which calendar (consultation vs treatment). NO efficacy claims, NO comparative claims.
2. **Eonia FAQ** — opening hours, location, parking, payment methods, what to bring to consultation, post-treatment care general (NOT specific clinical advice).
3. **Eonia Practitioner Schedule** — which days the doctor is in, which days are therapist-only.
4. **Eonia Consultation Process** — what happens in a consultation, how long it takes, what's covered.
5. **Eonia Cancellation Policy** — how late can you reschedule, deposit forfeit rules.

### Conversation flows in Retell flow builder

- **Flow A: New cosmetic injectable enquiry** → age check → capture concern (without diagnosing) → book consultation → SMS confirm
- **Flow B: Existing patient follow-up** → identify by phone → confirm last treatment → if eligible, book direct → SMS confirm
- **Flow C: Skin treatment booking** → screening (pregnancy, recent sun exposure, current skincare) → book direct or escalate to consultation → SMS confirm
- **Flow D: Reschedule** → look up booking → offer alternatives → confirm
- **Flow E: Post-treatment concern** → DO NOT triage → capture details → escalate to on-call number immediately
- **Flow F: Complaint** → DO NOT debate → capture details → urgent escalation to Peter + therapist → SMS confirm to caller

---

## Phase 4 — Workflows and routing (Days 6–7)

### Twilio routing
Same as DSK — point Eonia's Twilio number's voice webhook at Retell's inbound URL.

### Eonia number cutover
**Recommendation: Option B (conditional forward) for the first week**, then Option A (full port) after Day 14.

For the pilot, start with: forward to Metis Cortex on no-answer (3 rings) + after-hours. Day 13 onwards, forward unconditionally.

Important: medical/aesthetic clinics often have legacy front-desk staff who feel threatened by AI. Give them time to see Zoe work alongside them before going full cutover. The therapist hire transition is a good window to make this change.

### GHL workflows specific to Eonia

1. **New enquiry → consultation booked** → SMS confirmation + add to GCal + create patient record in GHL + sync to Cliniko/Pabau via webhook → 24h pre-consultation reminder
2. **Consultation done → treatment recommended** (manual stage advance by doctor) → trigger SMS asking to book treatment within 7 days → if no booking by Day 7, follow-up SMS
3. **Treatment booked → 24h reminder + day-of reminder** → SMS post-treatment with aftercare link (not clinical advice — generic care info)
4. **Treatment done → review request** → 48h post-treatment SMS asking for Google review → if 5★, follow-up with referral offer
5. **Cancellation/reschedule → waitlist auto-fill** workflow — the high-value one
6. **Post-treatment concern flagged** → urgent SMS + email to therapist + Peter → call recording attached

### Cliniko / Pabau / Halaxy webhook spec

(Replace API endpoint with the actual one once Eonia's CMS is confirmed.)

```
POST [CMS_API]/appointments
Authorization: Bearer [EONIA_CMS_TOKEN]

{
  "patient_id": "<lookup or create>",
  "appointment_type": "<consultation | treatment_followup>",
  "practitioner_id": "<doctor or therapist id>",
  "starts_at": "<booking ISO>",
  "ends_at": "<+ duration>",
  "notes": "<short transcript summary, NO clinical detail>"
}
```

Map response back to GHL so Opportunity advances to "Consultation Booked" or "Treatment Booked".

**Privacy note:** never pass full transcripts to the CMS — clinical systems often mirror data to insurance / billing. Pass a short summary line only ("New patient consultation re: cosmetic injectable enquiry"). Full transcript stays in GHL.

---

## Phase 5 — QA and test calls (Days 8–10)

Run these 5 test calls. Zoe must pass all 5 cleanly before Eonia goes live.

| Test | Scenario | Pass criteria |
|---|---|---|
| 1 | New caller, 28yo, asking about lip filler for the first time | Books CONSULTATION (not treatment). Does not quote treatment price. Does not claim filler "works". SMS confirmation lands. |
| 2 | Existing patient, last botox 4 months ago, wants top-up | Recognises by phone, confirms previous treatment, books direct to treatment calendar with therapist. |
| 3 | Caller asking "did my swelling normally last this long after filler?" 3 days post-treatment | Does NOT triage. Does NOT reassure. Escalates immediately to on-call number. SMS confirmation with on-call number. |
| 4 | 16yo asking about Botox | Politely declines, explains 18+ legal requirement, offers to book a consultation about non-injectable skin treatments instead. |
| 5 | Angry caller about previous filler outcome ("it's uneven") | Does NOT debate. Captures details. Escalates urgent to therapist + Peter. SMS confirms callback. |

Also run:
- **Test 6 (clinic-specific):** waitlist trigger. Cancel an existing booking via GHL → confirm auto-SMS fires to top 3 waitlist members → confirm rebook within 5 minutes.

If any fail, fix the prompt or flow and re-test. Don't go live with a 5-of-6 pass rate. Clinic mistakes = clinical risk.

---

## Phase 6 — Go live (Days 13–14)

**Day 13 — Shadow mode 24h.** Forward Eonia's number to Metis Cortex. You and the therapist still have visibility — review every call recording before bed. Fix anything broken.

**Day 14 — Metis Cortex primary.** Zoe answers first; therapist's mobile is the human escalation when Zoe escalates.

Send yourself a "Eonia Metis Cortex live" SMS at 9am Day 14. The 14-day measurement window starts.

---

## Metrics capture (Days 14–28)

For the case study + the clinic-vertical cold email:

- **Total inbound calls** (count from GHL)
- **Calls answered by Zoe within 30s** (~100%)
- **Consultations booked** (count from GHL)
- **Treatments booked direct** (count from GHL)
- **Post-treatment concerns escalated** (count, plus how fast — should be <30s from call answer to escalation)
- **Waitlist auto-fills** (count + average rebook time)
- **Estimated revenue from new bookings** (sum of consultation fees + treatment estimates from CMS)
- **After-hours calls handled** (filter 6pm–9am — these are pure recovered revenue)
- **Comparison to baseline week** before install

Screenshot the GHL call log, the Eonia booking calendar (consultation + treatment), and the waitlist workflow log at end of Day 28. Three screenshots = case study #2.

---

## What writes the cold email (clinic vertical)

> **Subject:** [N] missed calls at our clinic in 14 days
>
> Hi [Name] —
>
> Ran a 14-day pilot at our aesthetic clinic last fortnight. Installed an AI receptionist (Zoe) that picks up every missed call within 30 seconds, books consultations, and auto-fills cancelled slots from the waitlist.
>
> Result: [N] inbound enquiries, [X] consultations booked that would have gone to voicemail. [Y] cancelled slots auto-filled from the waitlist. Roughly [Z] in recovered revenue — most of it from same-day reschedules that would otherwise have stayed empty. Total install cost: A$1,500.
>
> Most clinics are leaking the same patient enquiries. Happy to share the setup if useful — not selling, trying to figure out who this helps most. 10-min demo: [Calendly link]
>
> Peter
> Metis Cortex — built and proven on Eonia + DSK Property Cleaning
> metiscortex.au

The "+ DSK" line in the signature is what makes the email work for a non-clinic prospect too. Cross-vertical proof.

---

## Compliance checklist before going live

Quick final pass before flipping the switch:

- [ ] Zoe's prompt does NOT contain any treatment efficacy claim
- [ ] Zoe's prompt does NOT quote a single treatment price (only consultation fee)
- [ ] Zoe's prompt does NOT recommend a specific treatment for a specific concern
- [ ] After-hours escalation number for post-treatment concerns is in the prompt and tested
- [ ] Patient privacy: webhook to CMS only sends short summaries, not full transcripts
- [ ] All call recordings stored in GHL (encrypted at rest by GHL)
- [ ] Patient consent for AI handling: add a one-line disclosure to the existing booking confirmation SMS — "Calls to Eonia may be answered by Zoe, our AI receptionist, and recorded for service quality. To speak directly to a person, ask 'human' at any time."
- [ ] "Ask 'human' to escalate" actually works — test it as a 7th QA call
- [ ] Therapist + doctor briefed on what Zoe will and won't do — they're the humans on the other end of escalations

---

## Cross-pilot dependencies (DSK + Eonia running concurrently)

- **You can't be on both pilots' on-call queues simultaneously.** Therapist takes Eonia clinical escalations, you take operational escalations. Clear handoff in writing.
- **Different Twilio numbers, different GHL sub-accounts, different Retell agents** — no shared infrastructure.
- **Metric capture: separate dashboards, separate screenshots, separate reports.** Don't merge data.
- **Case studies: write them as two parallel deliverables, not one.** Each one gets its own page in the eventual `/case-studies/` section of metiscortex.au.

---

## What I'll prep next once Day 1 starts

Once Eonia's GHL sub-account, Twilio number, and Retell agent are created, I'll:

- Generate the **complete Retell prompt** with Eonia's actual treatment menu, consultation fee, and on-call escalation number filled in (you'll send those)
- Generate the **GHL workflow JSON** for Eonia's pipeline + waitlist auto-fill, ready to import
- Generate the **Cliniko/Pabau/Halaxy webhook code** ready to drop into GHL's custom webhook builder, once you confirm which CMS Eonia uses
- Generate the **6 test call scripts** as paste-ready dialogue (5 standard + 1 waitlist test)

Don't try to do all of this in one sitting. Day 1 is sub-account + Twilio number + Retell agent skeleton. Day 2 starts the build.

---

## File log

- **Created:** 2026-05-06
- **Author:** Claude Code
- **Pairs with:** `dsk-pilot-pack.md` (DSK install pack)
- **Status:** Draft — pending Peter review and Eonia therapist start date confirmation
- **Dependencies:** Therapist hire start date confirmed before Day 1 can begin; Eonia CMS choice confirmed (Cliniko / Pabau / Halaxy / other) for webhook spec
- **Compliance basis:** TGA Therapeutic Goods Advertising Code constraint-framing throughout. No efficacy claims, no comparative claims, no prices on call. Mechanism language only.
- **Privacy basis:** No clinical detail passed to non-clinical systems. Patient consent via SMS disclosure on booking. Recording handled by GHL (encrypted at rest).
