# Metis Cortex — Pilot Data Capture Kit

> **For:** Peter, on Day 28 of the DSK pilot (and every paying client thereafter)
> **Author:** Cowork, executing Task 15 of the 2026-05-06 14:30 brief
> **Eventual home:** `~/Desktop/metis-cortex/PILOT-CAPTURE-KIT.md`
> **Trigger:** the morning of Day 28, before the metrics-report email goes out

---

## Why this kit exists

Day 28 of the pilot is the highest-leverage moment in the entire customer lifecycle. Three things happen on the same day:

1. The customer receives the month-one metrics report (deciding renew / upsell / refund)
2. Peter captures the screenshots that become the public case study
3. The cold-email batch fires (referencing those screenshots and that report)

Without a checklist, Peter scrambles on Day 28 to find the right screens. Two valuable things slip — either the case study is weaker, or the report email is delayed. With this kit, both happen the same morning, on autopilot.

---

## Section 1 — Day 28 screenshot checklist

### Capture sequence (do in this order, takes ~30 minutes)

#### From GoHighLevel (4 screenshots)

| # | What | Where in GHL | Notes |
|---|---|---|---|
| 1 | **Call log — past 14 days** | Conversations → Calls → filter "Date: last 14 days" → filter "Direction: Inbound" → filter "Answered by: Zoe agent" | Sort by date descending. Capture the count visible at the top. |
| 2 | **3 representative conversation transcripts** | Click into individual conversations → screenshot the call summary + transcript | Pick: one normal new-quote, one after-hours (filter by 7pm–7am), one reschedule. **Customer name + phone number redacted in screenshot.** |
| 3 | **Pipeline view — opportunities created in 14d** | Pipelines → DSK pipeline → filter "Created in last 14 days" → "Source: Zoe" | Show the count + the funnel breakdown (New Enquiry → Qualified → Booked) |
| 4 | **SMS log — booking confirmations sent** | Conversations → SMS → filter "Sent by automation: Booking confirmation" → last 14 days | Count visible at top. Redact customer phone numbers. |

#### From Jobber (3 screenshots)

| # | What | Where in Jobber | Notes |
|---|---|---|---|
| 5 | **Job list — created by Zoe webhook in 14d** | Jobs → filter "Date created: last 14 days" → filter by tag "Zoe-booked" or by source field | Show the count + the list. **Customer names + addresses redacted.** |
| 6 | **Revenue summary** | Reports → Revenue → date range "last 14 days" → filter to Zoe-sourced jobs | Should show total quoted value of those jobs. This is the recovered-revenue number. |
| 7 | **Calendar week-view** | Calendar → week view → screenshot a representative week post-install | Showing booking density. Don't show customer names; the visual story is the volume of slots filled, not who. |

#### From Twilio (2 screenshots)

| # | What | Where in Twilio | Notes |
|---|---|---|---|
| 8 | **Call detail records** | Phone Numbers → Manage → click your AU number → Logs → Calls → date range last 14 days | Show: total inbound, % answered within 30 seconds (this is Zoe's response-time proof point) |
| 9 | **The Twilio number assigned to Zoe** | Phone Numbers → Manage → list view → screenshot showing the Sydney-local number | This is what shows up in the case study. *"02 XXXX XXXX answers in 27 seconds, 24/7."* |

#### From Retell (2 screenshots)

| # | What | Where in Retell | Notes |
|---|---|---|---|
| 10 | **Agent dashboard — call stats** | Agents → "Zoe" → Analytics tab → last 14 days | Total calls, average duration, escalation rate, customer satisfaction proxy if available |
| 11 | **Voice prompt config** | Agents → "Zoe" → Configuration tab → screenshot the system prompt section | This is the "what we built" proof for the case study. **Don't include any DSK-specific pricing data in the public version of this screenshot — pricing is a competitive asset; show it only with PRICING REDACTED placeholder.** |

### File handling

**Save location:** `~/Desktop/metis-cortex/public/photos/dsk/pilot-evidence/`

(Code creates the directory. Cowork can prep this when filesystem access lands.)

**Naming convention:**

```
pilot-{source}-{description}-2026-MM-DD.png
```

Examples:

- `pilot-ghl-call-log-2026-05-21.png`
- `pilot-ghl-transcript-after-hours-redacted-2026-05-21.png`
- `pilot-jobber-revenue-summary-2026-05-21.png`
- `pilot-twilio-call-records-2026-05-21.png`
- `pilot-retell-dashboard-2026-05-21.png`

**Capture quality rules:**

- ✅ Browser zoomed to 100% before screenshot (text legible)
- ✅ OS clock visible in the corner — date-stamps the evidence
- ✅ Window clean, no other apps stacked behind
- ✅ Use `Cmd+Shift+4` then space-bar then click the window — captures cleanly without desktop clutter
- ✅ Save as PNG, not JPEG (text stays crisp)

### Privacy redaction (MANDATORY before any screenshot leaves your machine)

Use the macOS Preview annotation tools or Pixelmator to mask:

- ❌ **Customer first + last names** — replace with "Customer A", "Customer B" etc.
- ❌ **Customer phone numbers** — black-bar across all but the area code
- ❌ **Customer street addresses** — black-bar street number + name; suburb + state OK to leave visible
- ❌ **Email addresses other than DSK's own** — black-bar
- ❌ **Any personally-identifiable health information** (relevant for Eonia pilot, not DSK) — full redaction
- ✅ **DSK's own data is fine to show** — DSK is the customer in this case study, the consenting party
- ✅ **Aggregate counts and totals are fine** — no individual identification

**Don't crop tightly to just the number.** Leave the surrounding interface visible — that's how the screenshot reads as authentic. Tight crops read as fabricated.

### Two-pass capture

**First pass — capture everything:** all 11 screenshots, raw, no redaction. Save to `pilot-evidence/raw/`. These are your private internal record.

**Second pass — redact for public use:** copy each screenshot to `pilot-evidence/redacted/`, redact per the rules above. These are what go into the case study, the LinkedIn post, the cold email, the homepage testimonial strip.

**Never publish a raw-pass screenshot.** Even one slip on customer-name redaction is the kind of thing that ends up screenshotted and shared as a privacy fail.

---

## Section 2 — Day 28 metrics report email template

### About this email

This is the most important email in the entire customer lifecycle. It either:
- **Auto-renews them** (default — most likely outcome if numbers are good)
- **Triggers the upsell to Reception/Handbook** (only if 5+ extra bookings landed — the upsell needs the data to back it)
- **Triggers the refund** (if month one didn't deliver)

The same template handles all three outcomes. Tone: confident. Numbers do the work; adjectives don't.

### Trigger and timing

- **When:** Day 28 of the install (14 days after Day 14 go-live), 09:00 AEST
- **From:** peter@kritsotakis.com.au
- **Reply-to:** peter@kritsotakis.com.au
- **For Stripe-managed billing:** Day 28 is two days before auto-renewal on Day 30. This window gives the customer time to act on the refund option if they want to. Don't compress to Day 29 — too much pressure.

### Subject

```
Your month-one Metis Cortex report — {{business_name}}
```

(Variable; ~50 chars with a typical business name. "Report" frames it as data not pitch.)

### Preview text (90 chars max)

```
{{call_count}} calls handled. {{booking_count}} bookings. Here's what month one delivered.
```

(85 characters; numbers in the preview = open rate doubles vs. soft framing.)

### Body

```
Hi {{first_name}},

Day 28 of Metis Cortex at {{business_name}}. The numbers below are the
real results from Zoe over the past 28 days.

The headline:

  → {{call_count}} inbound calls handled by Zoe
  → {{booking_count}} bookings created
  → {{conversion_rate}}% enquiry-to-booking conversion
  → A${{recovered_revenue}} in recovered revenue
  → {{after_hours_count}} after-hours calls captured
    (these would have hit voicemail before)
  → {{escalation_count}} escalations to me (the rare cases that
    needed human judgment)

Compared to your baseline week before install — you were missing
{{baseline_metric}} calls/week. This month you missed close to zero.

The one that surprised even me: {{surprise_moment}}

Where this lands:

  Option 1 — Auto-renew. {{next_charge_amount}} charges to your card
             on Day 30. No action needed. Most clients pick this
             when month one delivers.

  Option 2 — Add Reception or Handbook. Both are upsells we built
             after Metis Cortex that share the same Zoe install. Reply
             to this email with "tell me more" and I'll send a
             10-min walkthrough.
             {{ Only show this option block if booking_count >= 5 }}

  Option 3 — Refund. The guarantee was 5 extra bookings in month one;
             Zoe delivered {{booking_count}}.
             {{ if booking_count >= 5 }}
               You're whole regardless of what you pick.
             {{ else }}
               You hit the refund threshold. Reply with "refund"
               and I send the form. Full $1,500 back to your card
               within 7 days. Zoe stays live for the rest of the
               month at no charge.
             {{ endif }}

You don't need to reply unless you want to change something — auto-renew
is the default. If anything's confusing or off, reply to this email and
I'll come back to you the same day.

Peter Kritsotakis
Metis Cortex
metiscortex.au
```

**Word count:** approximately 290 words with all variables filled in.
**Tone check:** numbers in priority order, refund mentioned by name with the actual delivered booking count, no hedging if it underdelivered.

### Variable summary

| Token | Source | Notes |
|---|---|---|
| `{{first_name}}` | Stripe customer first name | |
| `{{business_name}}` | Trading name | |
| `{{call_count}}` | GHL call log filter | All inbound, last 28 days |
| `{{booking_count}}` | Jobber + GHL pipeline | Jobs created from Zoe-source enquiries |
| `{{conversion_rate}}` | calculated `(booking_count / call_count) × 100` | Round to nearest whole percent |
| `{{recovered_revenue}}` | Jobber revenue summary | Sum of quoted values for the 28-day post-install window minus baseline week (if applicable) |
| `{{after_hours_count}}` | Twilio CDR filter 7pm–7am | The pure-recovery number — these calls would have hit voicemail |
| `{{escalation_count}}` | GHL escalation log | Times Zoe handed off to Peter |
| `{{baseline_metric}}` | DSK pre-install measurement | Captured during pilot Day -7 to Day 0 |
| `{{surprise_moment}}` | Peter manually fills in | One specific example from the 28 days. E.g., *"the Mosman pre-sale that came in at 7:42pm on a Sunday — Zoe quoted A$2,500, qualified, booked Monday morning before I even saw the missed call."* |
| `{{next_charge_amount}}` | Stripe subscription | Usually `A$600` for Metis Cortex-only |

### Rendering rules

The template uses inline conditional blocks (`{{ if booking_count >= 5 }}` etc.). When sending:

- If `booking_count >= 5` (success path) — include all three options as written, but the Refund block reads *"You're whole regardless of what you pick."*
- If `booking_count < 5` (refund path) — Option 2 (Reception/Handbook upsell) is **removed entirely**. Don't pitch upsells when month one underdelivered. The Refund block reads as the active recommendation.

If your email tooling doesn't support inline conditionals, fork two versions of the template — one for ≥5 bookings, one for <5. Same body otherwise.

### What you DON'T put in this email

- ❌ Adjectives like "amazing," "incredible," "blown away" — undermines the data
- ❌ A separate "what's next" CTA block — the three options are the CTA
- ❌ Ask for a Google review — too early; ask separately on Day 35 if Option 1 was selected
- ❌ Ask for a referral — same, Day 35
- ❌ Reception/Handbook upsell if `booking_count < 5` — actively harmful
- ❌ Apology language if numbers underdelivered — own it once at the top, then fire the refund link cleanly. Apologising more than once reads as desperation.

### Sending discipline

- Send 09:00 AEST sharp. Tuesday/Wednesday/Thursday only — Mondays they're catching up; Fridays they're winding down.
- Don't BCC anyone internally. The customer should believe this email is one-to-one (which it is).
- If they reply within 24h with a question, respond same-day. Day 28 + 24h is when retention is decided in practice.

### What happens after Day 28

- **Day 30:** Stripe auto-renew fires (if Option 1 selected — which is the default if no reply received)
- **Day 35:** soft-touch follow-up — *"how's Zoe going in week 5?"* — either ask for a Google review (if all good) or surface any rough spots before they fester
- **Day 60:** the Audit upsell becomes live (the $500 paid AI Opportunity Audit) — separate template, drafted later
- **Day 90:** referral ask, framed as *"three operators in your network who'd benefit"*

This email is the gate to all of that. If month-one numbers are good and this email lands cleanly, the rest of the lifecycle is mechanical.

---

## Done criteria

The kit covers everything Peter needs on Day 28 morning, in the order he needs it. Capture the screenshots first (private record + redacted public version), then send the metrics report email by 09:00, then post the LinkedIn case study (template already drafted in `LINKEDIN-FIRST-POST-DRAFT.md`), then fire the cold email batch (prospects already drafted in `COLD-EMAIL-V1-PROSPECTS.md`). Day 28 becomes a 2-hour orchestrated routine, not a scramble.

When the DSK pilot completes, this kit's first deployment writes the foundation case study. Every subsequent client install reuses the same Day-28 routine with their data in the variable slots. The kit pays for itself on the first deployment and compounds from there.
