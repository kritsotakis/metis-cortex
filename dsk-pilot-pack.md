# Metis Cortex DSK Pilot — 14-Day Install Pack

> **Goal of the pilot:** install Metis Cortex on DSK Property Cleaning, capture before/after metrics, and produce **case study #1** that drives the first 5 paying Metis Cortex clients (path-(i) leveraged boutique, warm-intro selling, NOT cold outbound).

---

## What we're proving in 14 days

Three numbers.

| Metric | Baseline (week before install) | Target (week after install) |
|---|---|---|
| **Missed-call rate** | Count over a 7-day window | < 5% (AI picks up if you don't) |
| **Average response time** | Hours / minutes | < 60 seconds |
| **Bookings from inbound enquiries** | Bookings per 100 enquiries | +30% lift minimum |

Capture screenshots of the Jobber dashboard before and after. The recovered revenue number is what writes the cold email.

---

## Stack you're configuring

| Layer | Tool | Cost (Month 1) | What it does |
|---|---|---|---|
| Voice AI | **Retell AI** | ~A$50–150 (usage-based) | Picks up the phone, holds the conversation, books the appointment |
| CRM + workflow + SMS + calendar | **GoHighLevel** (Starter, $97 USD/mo for the pilot) | ~A$148 | Records every call, sends SMS, books to calendar, runs follow-up |
| Phone number | **Twilio** (1 AU local number) | ~A$15 | The actual number Metis Cortex answers on |
| Existing CRM | **Jobber** (DSK already pays) | A$0 incremental | Bookings flow back to Jobber via webhook |
| **Pilot total** | | **~A$215 for the first month** | |

Accounts needed at:
- retellai.com (sign up, fund $100 USD credit)
- gohighlevel.com (Starter plan, 14-day free trial covers the pilot)
- twilio.com (provision 1 AU local number)
- Jobber API access (already have this; grab API key from settings)

---

## Day-by-day timeline

| Day | Phase | What happens |
|---|---|---|
| -7 → 0 | **Baseline** | Track DSK missed calls and response times. No changes yet. |
| 1 | **Sign-up day** | Create Retell, GHL, Twilio accounts. Buy AU number. |
| 2–3 | **GHL setup** | Sub-account configured, snapshot loaded, calendar synced |
| 4–5 | **Retell agent build** | Voice prompt configured, knowledge base loaded |
| 6–7 | **Workflow + routing** | GHL workflows wired, Twilio routing set, Jobber webhook tested |
| 8–10 | **Internal testing** | 5 scripted test calls, fix everything that breaks |
| 11–12 | **Live with forwarding only** | DSK number forwards to Metis Cortex only when missed; you still answer when available |
| 13 | **Soft launch** | 24-hour shadow mode — Metis Cortex takes everything, you monitor |
| 14 | **Go live** | Metis Cortex is the primary — it picks up first, you're the human escalation |
| 14–28 | **Capture data** | Track the three metrics. Screenshot weekly. |

---

## Pre-flight checklist (Day 0)

Before signing up for anything:

- [ ] DSK current phone number (the one ringing now)
- [ ] DSK Jobber API key (Settings → Integrations → API)
- [ ] DSK Google Calendar share access for the booking calendar
- [ ] List of DSK service types and standard prices (pre-sale clean, end-of-lease, builders clean, strata, etc.)
- [ ] DSK service area (suburbs DSK actually services)
- [ ] DSK availability hours (when Metis Cortex books vs. when it just takes a message)
- [ ] DSK quote variables — what does the AI need to ask to give a price (sqm? bedrooms? garage? rooms? oven? carpet?)
- [ ] One DSK call recording (real or mock) — to feed the AI as a tone reference
- [ ] Email + SMS template you currently send after a quote — Metis Cortex will copy that voice

Have all the above in one place before Day 1.

---

## Phase 1 — Sign-ups and accounts (Day 1)

**Retell AI:**
1. Sign up at retellai.com
2. Top up $100 USD credit (covers ~15 hours of voice agent calls)
3. Note your API key for later

**GoHighLevel:**
1. Sign up for the Starter plan ($97 USD/mo) — 14-day free trial, but enter card so it doesn't pause mid-pilot
2. Create a sub-account named "DSK Property Cleaning"
3. Skip onboarding wizard — we're loading a custom snapshot

**Twilio:**
1. Sign up, verify, fund $20 USD
2. Phone Numbers → Buy a Number → Australia → Sydney area code
3. Buy 1 number (~A$1.50/mo + usage)
4. Enable Voice + SMS on it

**Jobber API:**
1. Settings → Integrations → API Access → Generate token
2. Save the token securely

---

## Phase 2 — GHL setup (Days 2–3)

**Sub-account configuration:**
- Business name: DSK Property Cleaning
- Industry: Cleaning Services
- Time zone: Australia/Sydney
- Currency: AUD
- Connect Twilio number: paste the AU local number you bought

**Calendar:**
- Create calendar: "DSK Bookings"
- Set business hours: matches DSK's actual availability
- Buffer between bookings: 30 mins
- Connect Google Calendar (Peter's or DSK's Gmail) for two-way sync

**Pipeline:**
- Stages: New Enquiry → Qualified → Quote Sent → Booked → Job Done → Reviewed
- Default to "New Enquiry" when AI captures a lead

**Workflows (filled in Phase 3):**
- Inbound call → AI answers → captures lead
- Booking confirmed → SMS confirmation
- 24h before job → SMS reminder
- Job done → SMS asking for review

---

## Phase 3 — Retell voice agent build (Days 4–5)

This is the heart of Metis Cortex. The AI's behaviour lives here.

### Agent identity
- **Name:** Zoe (warm, neutral Australian female name)
- **Voice:** Retell's `aura-2-australian-female` (or closest equivalent at install date)
- **Greeting:** *"Hi, this is Zoe — the AI receptionist for DSK Property Cleaning. This call is recorded for quality and training. How can I help?"*
  - **Why the recording disclosure is mandatory:** NSW Surveillance Devices Act 2007 requires all-party consent to record private conversations. Zoe must announce the recording at the start of every call — non-negotiable. (Confirmed by Manus privacy review 2026-05-09.)

### System prompt (paste-ready into Retell)

```
You are Zoe, the AI receptionist for DSK Property Cleaning, a Sydney-based premium property cleaning company specialising in pre-sale cleans, end-of-lease cleans, builders cleans, and strata maintenance.

Your job is to:
1. Answer every incoming call in a warm, professional Australian tone
2. Identify why the caller is calling (new quote, existing booking, complaint, supplier, etc.)
3. For new quote requests: capture name, phone, address (suburb minimum), property type, service type, urgency, square footage or number of bedrooms, and any special requirements (carpet, oven, garage, post-renovation dust, etc.)
4. Quote a price range based on the pricing rules below
5. If they want to proceed, book them into the calendar at a time that works
6. Confirm via SMS at the end of the call

Tone:
- Warm, professional, Australian. Not corporate. Not robotic.
- Conversational, but efficient. Don't ramble.
- If the caller is rushed or stressed (e.g., end-of-lease emergency), match that energy and prioritise booking speed over upsell.
- Never claim to be human if asked directly. Say: "I'm Zoe, DSK's AI receptionist — I work alongside Peter and the team to make sure no one waits on hold."

Pricing rules:
[INSERT DSK STANDARD PRICING HERE — service type × property size grid]

Hard rules:
- Never quote outside the pricing grid. If unusual, capture details and say "Peter will call you back within 2 hours with a quote."
- Never accept a booking outside DSK service area: [INSERT SUBURBS LIST]
- For complaints: don't try to resolve. Say "I'm flagging this with Peter directly. He'll be in touch within 1 hour." Then trigger the urgent-callback workflow.
- For after-hours calls (defined as 7pm–7am Sydney time): take the message, book a callback for first thing next morning, send SMS confirmation.

Escalation triggers (transfer to human OR trigger urgent SMS to Peter):
- Caller asks specifically for Peter
- Caller is irate or threatening to leave a bad review
- Booking value exceeds $5,000
- Booking requires same-day service (within 4 hours)

End every call with:
"You'll get an SMS confirmation in a moment with the details and our team's number. Anything else I can help with today?"
```

### Knowledge base files to attach

Upload to Retell:
1. **DSK Pricing Grid** — service × property size × suburb → price range (Peter to fill in actual numbers)
2. **DSK FAQ** — opening hours, what's included in a pre-sale clean vs end-of-lease, do we move furniture, do we use eco products, etc.
3. **DSK Service Area** — list of suburbs you actually service
4. **DSK Process** — quote → confirm → clean → done → review

### Conversation flows (configure in Retell's flow builder)

- **Flow A: New quote** → capture details → quote → book → SMS confirm
- **Flow B: Existing client** → identify by phone number → "Hi [Name], lovely to hear from you again, what can I help with?"
- **Flow C: Reschedule** → look up booking → offer alternative slots → confirm
- **Flow D: Complaint** → capture details → urgent escalation to Peter → SMS confirm to caller

---

## Phase 4 — Workflows and routing (Days 6–7)

### Twilio routing

Configure your Twilio AU number's voice webhook to point at Retell's inbound number-forward URL (Retell will give you the exact URL when you create the agent).

### DSK number → Metis Cortex cutover

Two ways to cut DSK's existing number over to Metis Cortex. Pick one:

**Option A — Number port (cleanest, ~3–5 days lead time):**
Port the existing DSK number from its current carrier to Twilio. Once ported, all existing customers calling the same number get Metis Cortex. Recommended for the long-term.

**Option B — Conditional call forward (Day 1, no porting):**
Set DSK's existing number to forward to the Twilio number under three conditions:
- Always (Metis Cortex answers everything; you still see the call in GHL and can grab it)
- On no-answer after 3 rings
- After hours (7pm–7am)

For the pilot, **start with Option B "after-hours + no-answer"** so you stay in control while you build trust in the system. By Day 14, switch to "always" and let Metis Cortex take the front line.

### GHL workflows to wire up

1. **New inbound call** → create Contact if new → create Opportunity in "New Enquiry" → trigger Retell agent → log call recording + transcript on the Opportunity
2. **Booking confirmed by Zoe** → SMS confirmation to caller → add booking to GHL calendar → fire Jobber webhook to create job
3. **24h before booking** → SMS reminder to caller
4. **Job marked complete in Jobber** → trigger SMS asking for Google review → if 5★ posted, SMS thank-you with referral offer
5. **Escalation triggered** → urgent SMS + email to Peter with caller info, transcript snippet, callback time

### Jobber webhook spec

When Zoe books a job, GHL fires this to Jobber's API to create the job:

```
POST https://api.getjobber.com/api/graphql
Authorization: Bearer [DSK_JOBBER_TOKEN]

mutation {
  createJob(input: {
    clientId: "<lookup or create>",
    title: "<service type>",
    instructions: "<full transcript summary>",
    startAt: "<booking ISO datetime>",
    endAt: "<+ estimated duration>",
    location: { address1: "<address>", city: "<suburb>", postal: "<postcode>", region: "NSW" }
  }) {
    job { id }
    userErrors { message }
  }
}
```

Map Jobber's response back to GHL so the Opportunity moves to "Booked" stage.

---

## Phase 5 — QA and test calls (Days 8–10)

Before going live, run these 5 test calls. Zoe must pass all 5 cleanly.

| Test | Scenario | Pass criteria |
|---|---|---|
| 1 | Standard pre-sale clean, 4-bed house, Mosman | Books correctly, quotes within range, SMS confirmation lands |
| 2 | Urgent end-of-lease, 2-bed unit, Bondi, this weekend | Recognises urgency, doesn't waste time on small talk, books fastest available |
| 3 | Strata enquiry, weekly common-area clean, Surry Hills | Captures details, escalates to Peter (strata is a contract sale, not a one-off) |
| 4 | Existing client calling about an upcoming booking | Recognises by phone, doesn't ask for name, handles reschedule |
| 5 | Angry customer about poor previous job | Doesn't try to resolve, captures complaint, fires urgent escalation to Peter |

If any fail, fix the prompt or flow and re-test. Don't go live with a 4-out-of-5 pass rate.

---

## Phase 6 — Go live (Day 13–14)

**Day 13 — Shadow mode for 24 hours.** Forward DSK's number to Metis Cortex, but you also still pick up your mobile if able. Listen to every call recording before bed. Fix anything broken.

**Day 14 — Metis Cortex is primary.** Metis Cortex answers first; your mobile is the human escalation when Zoe escalates.

Send yourself a "Metis Cortex went live" SMS at 9am Day 14. From this moment, the 14-day measurement window starts.

---

## Metrics capture (Days 14–28)

For the case study and the cold email:

- **Total inbound calls** (count from GHL)
- **Calls answered by Zoe within 30 seconds** (should be ~100%)
- **Calls that resulted in a booked job** (count from Jobber)
- **Estimated revenue from those bookings** (sum of Jobber job values)
- **After-hours calls answered** (filter by 7pm–7am — these are the pure recovered revenue, since they would have been missed otherwise)
- **Comparison to baseline week** before install

Screenshot the GHL call log, the Jobber job list, and a calendar week-view at the end of Day 28. These three screenshots become the case study.

---

## What writes the cold email

After the 14-day measurement window, fill in this template with the real numbers:

> **Subject:** [N] missed calls at DSK in 14 days
>
> Hi [Name] —
>
> Ran a 14-day pilot on my own cleaning company last fortnight. Installed an AI receptionist (Zoe) that picks up every missed call within 30 seconds and books the job.
>
> Result: [N] inbound enquiries, [X] booked jobs that would have gone to voicemail. Roughly [Y] in recovered revenue. Total install cost (one-off): A$1,500.
>
> Most Sydney property and service businesses are leaking the same leads. Happy to share the setup if useful — not selling, just trying to figure out who this helps most. 10-min demo: [Calendly link]
>
> Peter
> Metis Cortex — built and proven on DSK
> metiscortex.au

That's the asset that drives the first 5 clients. Everything between now and that email is groundwork.

---

## What I'll prep next

Once you've started Day 1 (signed up for accounts, bought the Twilio number), I'll:
- Generate the **complete Retell prompt** with DSK's actual pricing grid filled in (you'll send me the numbers)
- Generate the **GHL workflow JSON** ready to import
- Generate the **Jobber webhook code** ready to drop into GHL's custom webhook builder
- Generate the **5 test call scripts** as paste-ready dialogue

Don't try to do all of this in one sitting. Day 1 is just sign-ups. Day 2 starts the build.

---

## File log

- **Created:** 2026-05-06 (saved as `.md` from earlier paste)
- **Author:** Peter (original) + Claude Code (formatted)
- **Pairs with:** `eonia-pilot-pack.md` (Eonia install pack — case study #2)
- **Status:** Active — used as template for Eonia + future verticals
- **Dependencies:** DSK pricing grid + service area + Jobber API key + call-recording reference must be captured at Pre-flight (Day 0) before Day 1 sign-ups begin
