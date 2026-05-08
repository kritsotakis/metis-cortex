# Calendly Confirmation Email + No-Show Follow-up

> **For:** Peter to paste into Calendly → Notifications → Customise (Confirmation email + Cancellation/no-show notification)
> **Author:** Cowork, executing Task 10 of the 2026-05-06 brief
> **Eventual home:** `~/Desktop/metis-cortex/CALENDLY-CONFIRMATION-EMAIL.md`

---

## How to install in Calendly

1. Calendly → your account → **Event Types** → **"Metis Cortex Demo — 10 min"**
2. **Notifications** tab → **Confirmation email** → **Customise**
3. Paste the subject + body below into the relevant fields
4. **Calendar invite** stays as Calendly's default (don't customise — it's reliable, doesn't need branding)
5. **Reminder** — Calendly's default 1-hour-before email + SMS is fine; no customisation needed
6. **Cancellation/no-show notification** → Customise → paste the no-show template

Calendly auto-injects the booking time, calendar link, and reschedule link as merge tags. Don't hard-code those.

---

## Confirmation email — sent the moment they book

### Subject

```
Your Metis Cortex demo — {{event_date}}, {{event_time}}
```

(Calendly merges `{{event_date}}` and `{{event_time}}` automatically. Format will read like *"Your Metis Cortex demo — Wed 14 May, 10:00 AM"*.)

### Preview text (Calendly: "Email preview text" field, 90 chars max)

```
10 minutes. We'll show you Zoe answering a real test call. No deck, no slide pitch.
```

(89 characters, opens with the duration anchor, ends with the differentiation against typical agency demos.)

### Body

```
Hi {{invitee_first_name}},

Booked. {{event_date}} at {{event_time}} — that's in your calendar now.

Here's what the 10 minutes look like:

I'll dial a live test number with our AI receptionist (Zoe) on the other end.
You'll hear her pick up, qualify a lead, and book a job in real time. Then
we'll talk pricing, the 14-day install, and the refund guarantee. That's it —
no deck, no slide pitch.

One ask before we talk: have your current weekly missed-call number roughly
in mind. Even a guess is fine. We'll work backward from that to whether
Metis Cortex makes sense for your business or doesn't.

If you need to reschedule: {{reschedule_url}}

Talk soon,

Peter Kritsotakis
Metis Cortex
metiscortex.au
```

**Word count:** 142 words. Under the 200-word ceiling.
**Tone check:** operator-to-operator, no jargon, one specific pre-call ask, anti-deck differentiation, founder name signed at the bottom (not "the Metis Cortex team").

---

## No-show follow-up — sent 24h after a missed demo

### How to install

Calendly → **Notifications** → **Cancellation / no-show notification** → **Customise**

OR set up a separate Calendly Workflow:
- Trigger: **Event ended** (and they didn't attend — Calendly tracks this if you mark them as no-show, or use Zoom/Meet attendance integration)
- Send: **24 hours after**
- Email body: below

### Subject

```
Missed you — happy to reschedule
```

(28 chars, no exclamation, no judgement. Tone signals "stuff happens, no drama".)

### Preview text

```
Friday afternoons get away from all of us. Happy to find a new slot whenever works.
```

(82 chars, normalises the no-show, removes any guilt loop.)

### Body

```
Hi {{invitee_first_name}},

Looks like {{event_date}} got away from you. Happens — no drama on this end.

Metis Cortex's still here whenever you want the 10 minutes. AI receptionist
installed on your business in 14 days, A$1,500 setup, refund if it doesn't
book 5 extra jobs in month one.

Reschedule whenever it suits: {{scheduling_url}}

Peter
Metis Cortex
```

**Word count:** 56 words. Brief on purpose — long no-show emails read as desperate. Reschedule link is the only action.
**Tone check:** zero guilt, zero "I noticed you didn't…" framing, the offer-restatement is one line, signed Peter not Peter Kritsotakis (more casual on a follow-up).

---

## Calendar invite block (default — don't customise)

Calendly's default calendar invite already includes:
- Event name (matches Calendly Event Type name)
- Date / time
- Join link (Zoom / Google Meet / phone — whichever you configured)
- "Reschedule / Cancel" links

**Don't customise this.** Calendar clients (Google, Outlook, Apple) render Calendly's default invite cleanly. Custom HTML in calendar invites breaks across half of mail clients.

---

## What to do if a prospect replies to the confirmation email

If they reply to the confirmation (asking a question, sending context, etc.):

- **Reply within 2 business hours.** Demo bookings have the highest cancel rate in the 24h between booking and the call — fast follow-up cuts cancellation by ~30%.
- **Match their length.** If they sent 3 lines, send 3 lines. If they sent a paragraph, you can send a paragraph.
- **Don't pre-pitch.** They've already decided to demo — the demo IS the pitch. Anything you write before the call eats into the 10 minutes' job.
- **Common questions and short answers:**
  - *"Will this work with [their CRM]?"* → "Yes — covers Jobber, ServiceM8, GoHighLevel, Cliniko, anything with a webhook. Show you live on the call."
  - *"What's the catch?"* → "If it doesn't book 5 extra jobs in month one, full refund of the install. That's the catch we've taken on. Quick demo and you'll see why I'm comfortable doing it."
  - *"Are you the founder?"* → "Yes — and I run a Sydney cleaning company (DSK) where we built this on ourselves first. That's why I take the calls."

---

## Out of scope for v1

- ❌ Branded HTML email templates (plain text or Calendly's default styling is fine)
- ❌ Customising the calendar invite (Calendly default is fine)
- ❌ A multi-step nurture for prospects who book but cancel before the call (no volume yet)
- ❌ Translating into other languages (English only, AU market only)
- ❌ Adding video preview thumbnails to the email body (no demo video exists yet)

---

## Done criteria

These two emails replace Calendly's defaults the moment Peter sets them up. Both are paste-ready. Total Peter setup time: ~5 minutes inside Calendly.
