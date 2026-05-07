# Cowork brief — Tasks 14–15 (sales prep + pilot capture)

> **For:** Cowork
> **Authored by:** Claude Code, 2026-05-06 14:30
> **Companion briefs:** Tasks 1–13 already delivered. This adds 2 more aimed at the next 2-week window.

---

## Context — what's coming up that needs Cowork drafts ready

In the next 2 weeks the following milestones land:

1. **First Calendly demo books** (the moment Peter publishes the URL)
2. **DSK Frontline pilot Day 28 — metrics report needs to fire** (the email that decides whether the customer renews / refunds / refers)
3. **First LinkedIn case-study post** (LinkedIn first-post template already drafted, needs the DSK pilot data slotted in)

Two of those need pre-drafted content Cowork can produce now. **Don't pre-build past these — anything Phase-2-or-later is premature.**

---

## Two new tasks

| Task | Why now | Cowork time |
|---|---|---|
| 14. Sales prep package (demo flow + objection handling + pricing rebuttals) | First demo lands the moment Calendly goes live. Peter will wing it without prep, or use a real script with prep. Genuine quality difference. | 90 min |
| 15. Pilot data capture kit (screenshot checklist + Day 28 metrics report email) | The DSK pilot ends in ~2 weeks. The case study writes from screenshots + the metrics report email. Both need to exist before Day 28. | 45 min |

**Total: ~2 hours 15 min Cowork time. Both deliverable as paste-ready docs.**

---

## Task 14 — Sales prep package

**Why:** Peter takes the demos personally — no SDR, no sales team. Each demo is 10 minutes of his time and the difference between booked and lost. A prepped script + objection responses make every demo close higher.

**Deliverable:** Single doc `metis-cortex-sales-prep-package.md` with three sections:

### Section 1 — Demo flow (the 10-minute script)

A second-by-second breakdown of the 10-min demo Peter runs:

- **Minute 0:00–1:00** — opening, set frame, read their pre-call answers from Calendly (the missed-call number they wrote in)
- **Minute 1:00–4:00** — live demo: Peter dials a Twilio test number, Zoe answers, qualifies a fake "I need a pre-sale clean for a 4-bed in Mosman," books, sends SMS confirmation. Prospect hears the actual product. **No slides.**
- **Minute 4:00–6:00** — translate what they just heard into their business: *"For your [vertical], the script changes but the structure is identical. Here's how it'd handle [their specific pre-call answer]."*
- **Minute 6:00–8:00** — pricing + guarantee + 14-day install. Plain numbers, no fancy framing. *"$1,500 setup, $600/month, refund if it doesn't book 5 extra in month one."*
- **Minute 8:00–9:00** — invite questions. Whatever they ask, the answer is short.
- **Minute 9:00–10:00** — close. Three options:
   1. Book the 14-day install now (Stripe link)
   2. Get them to send 1-2 of their typical inbound enquiry recordings so the next call is custom-tailored
   3. Send a 30-min reschedule for after they've discussed with a partner / team

**Tone notes for the script:**
- Operator-to-operator, no sales-y "amazing tool" language
- Peter says "I" not "we" — solo founder, owned product
- If a prospect is high-energy, match. If they're considered/quiet, slow down. Don't push.
- If they go silent after the demo, *let them*. Quiet means they're calculating. Don't fill the silence.

### Section 2 — Objection handling (10 most likely)

For each objection, give: **(a)** the underlying concern Peter should hear, **(b)** the 1-2 sentence response, **(c)** the bridge that gets back to closing.

Cover at minimum these 10:

1. *"It'll sound robotic / customers will hate AI"* — concern: brand reputation
2. *"$600/month is a lot"* — concern: ROI / cash flow
3. *"What if it screws up a real customer call?"* — concern: customer experience / liability
4. *"Are you locking me into a contract?"* — concern: flexibility
5. *"My phone system is non-standard / VoIP / weird"* — concern: technical complexity
6. *"I want to wait until you have more case studies"* — concern: risk aversion
7. *"My missed-call problem isn't that bad"* — concern: prioritisation / urgency
8. *"What integrates with [their CRM]?"* — concern: tech fit
9. *"How is this different from [Sophiie / Chime / cheaper competitor]?"* — concern: comparative shopping
10. *"I need to think about it / talk to my partner"* — concern: deferral

For each, the response must be:
- Honest (no over-promising)
- Specific (not vague)
- Brief (under 30 words spoken)

### Section 3 — Pricing rebuttals (5 specific scenarios)

For each, the script Peter says when they push back:

1. **"Can you do it for $X less?"** — specific number, holding the line
2. **"What if I just buy the setup, skip the monthly?"** — won't work, but here's what's available
3. **"What about a 6-month commitment for a discount?"** — counter-offer or hold
4. **"Pay me when it works, refund if not"** — they want pure performance pricing — Peter's already doing this via the refund guarantee, frame correctly
5. **"Can you give me 14 days free to test?"** — equivalent to skipping payment, here's the refund guarantee instead

Each pricing rebuttal must:
- Hold price (no discount before 5 paying clients exist — discounting too early sets a floor)
- Frame the refund guarantee as the actual concession Peter's already making
- Walk-away script if they truly won't pay $1,500 + $600/month — a referral to a self-serve cheaper tool is a graceful exit

**Save:** `metis-cortex-sales-prep-package.md` in your outputs.

**Timebox:** 90 min.

---

## Task 15 — Pilot data capture kit

**Why:** The DSK pilot completes in ~2 weeks. The case study (and the cold email batch that fires after it) is built from specific screenshots + a metrics report email. Without a checklist, Peter scrambles on Day 28 to grab the right screens. With it, the case study writes itself.

**Deliverable:** Single doc `metis-cortex-pilot-capture-kit.md` with two sections:

### Section 1 — Screenshot checklist (Day 28 capture playbook)

Specific list of what to capture from where, in what state, at what time:

**From GoHighLevel:**
1. Call log — past 14 days, filtered to "answered by Zoe"
2. Conversation transcripts — pick 3 representative ones (1 normal quote, 1 after-hours, 1 reschedule)
3. Pipeline view showing opportunities created in the 14-day window
4. SMS log showing the booking confirmations sent

**From Jobber (DSK's CRM):**
1. Job list — all jobs created by Zoe-via-webhook in 14 days
2. Revenue summary for those jobs (sum of quoted values)
3. Calendar week-view showing the 14-day install + post-install booking density

**From Twilio:**
1. Call detail records (CDR) showing inbound call counts + answered-within-30-seconds %
2. The actual phone number assigned to Zoe (for the case study reference)

**From Retell:**
1. Agent dashboard showing total calls handled, average call duration, escalation rate
2. The agent's voice prompt config (for the case study "what we built" section)

**Format every screenshot:**
- Date-stamped (visible in the screenshot OS clock)
- Clean window, no other apps visible behind
- Save to `~/Desktop/metis-cortex/public/photos/dsk/pilot-evidence/` (Code creates this directory)
- Naming: `pilot-{source}-{description}-2026-MM-DD.png`

**Privacy filtering:**
- Customer names blurred / redacted in transcripts
- Phone numbers other than DSK's own redacted
- Any home addresses redacted
- Anonymise everything except DSK itself — DSK is the customer here, all other parties get masked

### Section 2 — Day 28 metrics report email template

**Trigger:** Day 28 of the install (14 days after Day 14 go-live), sent at 09:00 AEST

**Recipient:** the customer (Peter for the DSK pilot, but template-ready for all future clients)

**Purpose:** This is the highest-stakes email in the entire customer lifecycle. It either retains them (default — auto-renew), upsells them to Reception/Handbook (Phase 2), or triggers the refund. Tone is decisive.

**Structure:**

- Subject: *"Your month-one Frontline report — {{business_name}}"*
- Preview: 1 line
- Body:
   - Headline number first — total inbound calls handled by Zoe in 28 days
   - 4 numbers: bookings created, conversion rate, recovered revenue (from after-hours + missed-window calls), escalations to human
   - Comparison vs. baseline week before install (this is what makes the case study real)
   - One specific moment that surprised even Peter — the "story" beat that humanises the numbers
   - Decision menu — three options framed neutrally:
     1. Auto-renew ($600 charged to card on Day 30, no action needed)
     2. Add Reception SKU as upsell (link to scope call) — *only mention this if 5+ extra bookings landed*
     3. Refund of $1,500 install + cancellation if month one didn't deliver — link to refund form
   - Signed Peter Kritsotakis personally

**Tone:**
- Confident, not boastful
- If the numbers are great, let them speak — don't gild them with adjectives
- If the numbers are mixed, lead with the strongest ones and address the misses head-on
- If the numbers don't hit 5 extra bookings, don't pretend they did — fire the refund link clearly

**Variables:**

| Token | Source |
|---|---|
| `{{business_name}}` | Trading name |
| `{{first_name}}` | Stripe customer first name |
| `{{call_count}}` | From GHL call log |
| `{{booking_count}}` | From Jobber / GHL pipeline |
| `{{conversion_rate}}` | Calculated |
| `{{recovered_revenue}}` | Sum from Jobber jobs in 14-day post-install window — baseline week |
| `{{after_hours_count}}` | Filtered call count, 7pm-7am window |
| `{{baseline_metric}}` | Pre-install week's missed-call count |

**Word count ceiling:** 400 words (longer than onboarding sequence because this email carries decision weight; brevity here reads as dismissive).

**Save:** `metis-cortex-pilot-capture-kit.md`. Code syncs into repo as `PILOT-CAPTURE-KIT.md`.

**Timebox:** 45 min total (20 min screenshot checklist + 25 min metrics report email).

---

## What Cowork must NOT do

- **No fictional case study numbers.** Wait for real DSK pilot data. Templates use `{{tokens}}`, never invented placeholders that look real.
- **No demo videos / recordings.** Out of scope. Peter does live demos.
- **No Reception or Handbook SKU pricing.** Phase 2 product, doesn't exist publicly yet, don't fabricate.
- **No "what if the pilot fails entirely" doomsday email.** The Day 28 email handles all three outcomes (renew / upsell / refund) gracefully — no separate doom version needed.
- **No multi-language.** English only, AU market only.
- **No code edits.** Code's lane.

---

## Sequencing

Tasks 14 and 15 are independent. Recommended order: **14 first** (longer + higher near-term leverage; Calendly goes live before pilot ends).

---

## Confirmation Cowork posts back

```
✅ Task 14 — Sales prep package at metis-cortex-sales-prep-package.md
            (demo flow + 10 objections + 5 pricing rebuttals)
✅ Task 15 — Pilot data capture kit at metis-cortex-pilot-capture-kit.md
            (screenshot checklist + Day 28 metrics report email template)
```

Then Code syncs into the repo and the queue closes for now. Cowork is in genuine standby until Peter's gates clear.
