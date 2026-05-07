# Metis Cortex — Customer Onboarding Email Sequence

> **For:** Peter (and the Brevo / Resend / MailerLite drip platform once chosen)
> **Trigger sequence:** Stripe payment success → Day 1 instant → Day 3 → Day 7 → Day 14 → end of sequence (Day 28 metrics report is a separate workflow)
> **Author:** Cowork, executing Task 11 of the 2026-05-06 brief; combined into single doc by Code

---

# Onboarding Email 1 — Day 1 (instant after payment)

> **Trigger:** Stripe (or whatever processor) payment success webhook → fire this email immediately
> **From:** peter@kritsotakis.com.au (move to peter@metiscortex.au once Google Workspace is set up post-Phase-2)
> **Reply-to:** peter@kritsotakis.com.au
> **Author:** Cowork, executing Task 11 (1/4) of the 2026-05-06 brief

---

## Subject

```
Welcome to Metis Cortex — what happens next
```

(46 characters; preview-friendly; sets clear expectation that there's actionable information.)

## Preview text (90 chars max)

```
The 14-day clock just started. Here's what we'll do, what you'll need, and when.
```

(81 characters; sets the structure of the email; no fluff.)

## Body

```
Hi {{first_name}},

Payment confirmed. Your install starts today.

Here's how the next 14 days work:

  Days 1–3 — I configure GoHighLevel for {{business_name}}, provision a
             Sydney-local number for Zoe to answer on, and connect Twilio.
  Days 4–7 — I build Zoe's voice prompt for your business and connect
             her to your existing calendar/CRM.
  Days 8–10 — Test calls. We dial in tone, qualify-and-book flow, and
              the handoff to your team for unusual cases.
  Day 11–13 — Soft launch. Zoe answers after-hours and missed calls only.
              You stay on the front line during the day so we can fine-tune.
  Day 14 — Full go-live. Zoe is the primary; you're the human escalation.

To start the build, I need three things from you in the next 48 hours:

  1. Your existing business phone number (the one ringing now)
  2. Your business hours — when Zoe books, vs. when she just takes a message
  3. Your top 3 service types and your standard pricing for each

Reply to this email with those, or grab a 15-minute call with me here:
{{kickoff_call_link}}

Anything off? Reply to this email — I read every one personally.

Peter Kritsotakis
Metis Cortex
metiscortex.au
```

**Word count:** 196. Under 200-word ceiling.
**Action:** ONE — reply with the three onboarding items, OR book the kickoff call.
**Tone check:** operator-led, day-by-day clarity, no marketing fluff, signed by Peter personally.

---

## Variables to merge

| Token | Source |
|---|---|
| `{{first_name}}` | Stripe customer first name |
| `{{business_name}}` | The trading name they paid under |
| `{{kickoff_call_link}}` | A second Calendly event type ("Metis Cortex Kickoff Call — 15 min") created during Task 1 |

If `{{kickoff_call_link}}` doesn't exist yet, fall back to `peter@kritsotakis.com.au` and have them email instead. Make the kickoff Calendly link a Phase 2 nice-to-have; it's not blocking.

## Out of scope for this email

- ❌ A welcome video — defer until you have one recorded
- ❌ Branded HTML — plain text + sensible line breaks renders fine across all clients
- ❌ Multiple CTAs — one path forward only
- ❌ Refund-guarantee restatement — they already saw it on the homepage and the booking confirmation; restating in email 1 reads as defensive

---

# Onboarding Email 2 — Day 3

> **Trigger:** 72 hours after the Day 1 welcome email (skip if customer hasn't replied to email 1 — chase manually instead)
> **From:** peter@kritsotakis.com.au
> **Reply-to:** peter@kritsotakis.com.au
> **Author:** Cowork, executing Task 11 (2/4) of the 2026-05-06 brief

---

## Subject

```
Building Zoe for {{business_name}}
```

(Variable; reads ~38 characters with a typical business name. Personalised + specific.)

## Preview text

```
Three updates from the past 72 hours, plus one thing I need from you this week.
```

(80 characters; signals progress + frames the ask.)

## Body

```
Hi {{first_name}},

Quick update on the build for {{business_name}}.

What's done:

  ✓ Sydney-local number provisioned via Twilio: {{twilio_number}}
  ✓ GoHighLevel sub-account configured, your calendar synced
  ✓ Voice prompt for Zoe drafted — first version ready for review

What I'm working on this week:

  → Connecting Zoe to {{their_crm}} so booked jobs flow back automatically
  → Tuning her tone — Australian female voice, warm but efficient,
    no "robotic call centre" feel
  → Building the qualifying questions specific to your service mix

One thing I need from you this week:

A 60-second voice memo of you answering a typical inbound enquiry —
the way you'd talk to a real customer. Doesn't need to be polished;
it's just a tone reference for Zoe so she sounds like your business,
not a generic AI voice.

Either reply to this email with the audio attached, or text it to
0423 668 766 — whichever's easier.

Anything come up? Reply directly — I read every one.

Peter
Metis Cortex
```

**Word count:** 178. Under ceiling.
**Action:** ONE — record and send a 60-second voice memo as tone reference.
**Tone check:** progress-led, specific deliverables, single ask framed as low-effort.

---

## Variables to merge

| Token | Source |
|---|---|
| `{{first_name}}` | Stripe customer first name |
| `{{business_name}}` | Trading name |
| `{{twilio_number}}` | The actual provisioned AU local number, captured during install Day 2 |
| `{{their_crm}}` | What they told you in email-1 reply (Jobber / ServiceM8 / Cliniko / "manual"/etc.) |

If they haven't told you their CRM yet, replace with *"your existing booking system"* and chase via separate email.

## Out of scope for this email

- ❌ A demo video of Zoe in action — too early; she's still being tuned
- ❌ Sending the voice prompt for review — overwhelming at Day 3; save for Day 7
- ❌ Asking for testimonial expectations — too early to reference outcomes

## Edge case

**If the customer hasn't replied to Email 1's questions:** don't send Email 2 yet. Email is failing. Pick up the phone and call them. Day 3 silence is a very early churn signal — fix it human-to-human, not by sending a second template.

---

# Onboarding Email 3 — Day 7 (midpoint)

> **Trigger:** Day 7 of the install, regardless of whether earlier emails were responded to (if not responded, escalate to phone first — but still send this email so the cadence stays predictable)
> **From:** peter@kritsotakis.com.au
> **Reply-to:** peter@kritsotakis.com.au
> **Author:** Cowork, executing Task 11 (3/4) of the 2026-05-06 brief

---

## Subject

```
Halfway there — test calls this week
```

(36 characters; sets expectation that this email is action-heavy without being overwhelming.)

## Preview text

```
Zoe answers her first test calls in the next 48 hours. Here's what to listen for.
```

(81 characters; concrete + signals to keep reading.)

## Body

```
Hi {{first_name}},

Day 7 of the install. We're halfway. Here's where things sit and what
this week looks like.

Done so far:

  ✓ Voice prompt finalised — Zoe answers in an Australian female voice,
    warm and efficient
  ✓ Calendar + CRM connected — bookings flow automatically into
    {{their_crm}}
  ✓ Five qualify-and-book scenarios scripted (new quote, existing
    client, reschedule, complaint, after-hours)

This week:

  → Tuesday/Wednesday — I run 5 internal test calls on Zoe to check
    every scenario passes. I'll share the recordings with you.
  → Thursday — your turn to listen and flag anything that doesn't sound
    like {{business_name}}. We adjust before going live.
  → Friday — we forward your existing number to Zoe ONLY for missed
    calls and after-hours. You stay on the front line during the day.

What to listen for in the test recordings:

  - Does her tone match how you'd talk to a customer?
  - Are the qualifying questions in the right order for your service?
  - Does the booking time confirm clearly (date, time, address)?
  - When she escalates to me, does the handoff feel natural?

If something's off, reply to this email or call 0423 668 766. Better
to fix in test than at go-live.

Refund guarantee reminder: if Zoe doesn't book at least 5 extra
appointments in your first month live, you get the full $1,500 install
back. No paperwork. That's why I want test calls clean before we ship.

Peter
Metis Cortex
```

**Word count:** 256. **Over the 200-word ceiling — keep this one slightly longer because Day 7 is the highest-information moment of the install.**
**Action:** ONE — listen to test recordings, flag anything off.
**Tone check:** confident, specific, includes the refund-guarantee restatement justified by the moment ("better to fix in test than at go-live").

---

## Variables to merge

| Token | Source |
|---|---|
| `{{first_name}}` | Stripe customer first name |
| `{{business_name}}` | Trading name |
| `{{their_crm}}` | What they confirmed in earlier emails — Jobber / ServiceM8 / Cliniko etc. |

## Out of scope for this email

- ❌ Asking them for a testimonial — way too early; this is mid-install
- ❌ Pitching add-on services (Reception, Handbook) — strict no in Phase 1; comes later via the Audit upsell
- ❌ Sharing their data publicly / asking permission to use them as a case study — defer until the Day-30 metrics report

## Edge case

**If they're behind on their part (still no voice memo, no answers to qualifying-question variations) by Day 7:** the email still goes out, but you also pick up the phone. Day 7 silence on the customer side means the Day 14 launch is at risk. Do not let it slip silently.

## Refund-guarantee placement note

The guarantee gets restated here — and only here — in the onboarding sequence. Restating it on Day 1 reads as defensive. Restating it on Day 14 reads as undermining the launch. Restating it at Day 7 reads as confident: "we're committing to make this work, and we've put real money behind it." That's the only place it earns its keep in the sequence.

---

# Onboarding Email 4 — Day 14 (go-live)

> **Trigger:** Day 14 of the install, sent at 9:00 AEST the morning Frontline goes primary
> **From:** peter@kritsotakis.com.au
> **Reply-to:** peter@kritsotakis.com.au
> **Author:** Cowork, executing Task 11 (4/4) of the 2026-05-06 brief

---

## Subject

```
Frontline is live for {{business_name}}
```

(Variable; reads ~38 characters with a typical business name. The most important word is "live" — it lands in inbox preview as a status confirmation, not a question.)

## Preview text

```
Zoe is now answering. What to do in the first 24 hours, and when your report lands.
```

(87 characters; immediate orientation.)

## Body

```
Hi {{first_name}},

Frontline is live.

As of 9am today, Zoe is answering every call to {{forwarded_number}}.
You're now the human escalation, not the front line.

What happens in the first 24 hours:

  - Every inbound call: Zoe picks up within 30 seconds, qualifies, books.
  - Every booking: lands in {{their_crm}} automatically + you get an SMS.
  - Every escalation (rare): you get a priority SMS + the call recording.
  - Every after-hours call: handled — no backlog when you start tomorrow.

What to do today:

  1. Make a couple of test calls to {{forwarded_number}} — verify Zoe
     sounds right and the booking lands.
  2. Watch your phone for the first real call alert. The first one is
     always the most exciting.
  3. Don't second-guess Zoe in the first week. If something feels off,
     flag it to me and I'll adjust the prompt — don't intercept calls
     unless it's a real emergency.

What lands in 14 days:

Day 28 — your month-one metrics report. I'll send a single email with:

  - Total inbound calls Zoe handled
  - Conversion rate (enquiry → booked job)
  - Estimated revenue from those bookings
  - After-hours calls captured (the pure-recovery number)
  - Comparison vs. baseline week before install

If those numbers don't show 5 extra booked appointments minimum, the
$1,500 install fee comes straight back to you — no paperwork.

Anything weird in the first 24 hours? Reply to this email or call
0423 668 766. I'm watching the system closely for the first week.

Peter
Metis Cortex
metiscortex.au
```

**Word count:** 232. Slightly over 200 but justified — this is the go-live moment and clarity beats brevity.
**Action:** ONE — make a couple of test calls, then trust the system.
**Tone check:** confident-not-cocky, specific 24h playbook, refund guarantee gets one final mention (this time as a deliverable, not a defence).

---

## Variables to merge

| Token | Source |
|---|---|
| `{{first_name}}` | Stripe customer first name |
| `{{business_name}}` | Trading name |
| `{{forwarded_number}}` | Their existing business number (the one Zoe forwards from). Use this not the Twilio number — that's the back-end; they care about THEIR number now reaching Zoe. |
| `{{their_crm}}` | Confirmed CRM — Jobber / ServiceM8 / Cliniko / etc. |

## Out of scope for this email

- ❌ Asking for a Google review / public testimonial — way too early; needs the Day 28 numbers first
- ❌ Pitching the Audit upsell — Phase 2 product; doesn't exist publicly yet
- ❌ Asking them to refer other businesses — fair game on Day 30 once the metrics report lands and proves the value

## What happens after Email 4

The onboarding sequence ends here. The next scheduled customer touchpoint is the **Day-28 metrics report email** — separate template, drafted later as part of the customer-success workflow. That email is the one that decides whether they:
- Stay on for month 2 (default — auto-renew)
- Add Reception/Handbook upsells (Phase 2 — earned right)
- Refer another operator (the highest-value outcome)
- Refund (the explicit fall-back the guarantee promised)

## Edge case

**If Day 14 launches with major issues** (Zoe failing on real calls, integration broken, etc.):
- Don't send this email automatically. The "Frontline is live" subject line lands as a lie if the system isn't working.
- Hold the email. Fix the issue. Send it the day Frontline is genuinely stable, regardless of calendar day.
- The 14-day clock can flex — the customer would rather get a working system on Day 16 than a broken one on Day 14. Communicate the slip directly via phone, not via the template sequence.
