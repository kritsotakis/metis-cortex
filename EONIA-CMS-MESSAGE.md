# Eonia CMS Confirmation — Message Templates

> **For:** Peter to send to the Eonia clinical team
> **Author:** Cowork, executing Task 5 of `COWORK-INFRASTRUCTURE-SETUP.md`
> **Synced into repo:** Claude Code, 2026-05-06
> **Why:** The Eonia Frontline install pack needs the actual clinical management system name (Cliniko, Pabau, Halaxy, etc.) to spec the booking webhook. Until confirmed, Day 1 of the Eonia install is blocked.

---

## Message 1 — initial CMS confirmation

Send this to whoever runs the day-to-day at Eonia (the lead therapist, the clinic manager, or whoever manages bookings).

**Channel:** WhatsApp / SMS / email — whatever's normal. Keep it casual.

```
Quick admin question — what clinical management system are we using at Eonia?
(Cliniko, Pabau, Halaxy, Timely, Fresha, Phorest, or something else.)

Need to confirm for an integration we're scoping for the front desk.
```

That's it. One question, friendly tone, no lead-up. Lets them give a one-word answer.

## Message 2 — follow-up once CMS confirmed

Once you have the CMS name, send this same person:

```
Cheers. Last one — who's got admin access if we need to generate an API
key down the track? Don't need it now, just want to know who to ping.
```

This pre-positions the API key request without making it feel like the admin person needs to do anything today.

## What Cowork does with the answer

When you forward the answer back, I'll:

1. Update `eonia-frontline-pilot-pack.md` — replace the generic "[CMS NAME]" placeholders in the webhook spec with the actual system. Each CMS has a different API shape:
   - **Cliniko** — REST API, well-documented, Australian-built (likely the answer)
   - **Pabau** — UK-based, GraphQL API, common in aesthetic clinics
   - **Halaxy** — Australian, has API but more limited
   - **Timely** — NZ-built, REST API, common in beauty/wellness
   - **Fresha** — UK, very common in beauty, more limited integration support
   - **Phorest** — Irish, salon/spa focus, well-supported API
2. Update `~/.claude/memory/active-projects.md` — Eonia Frontline install row from "CMS confirmation pending" to "CMS confirmed: [name]"
3. Add a TODO entry: "Generate Eonia [CMS] API key" — to fire on Eonia install Day 1, not before
4. Note the admin contact in memory so we know who to ping when the install actually starts

## Likely answer (so you know what to expect)

For a Sydney aesthetic clinic in 2026, the three most likely answers in order are:

1. **Cliniko** — the Australian default for allied health and aesthetic clinics. ~60% likelihood.
2. **Pabau** — popular specifically in aesthetic/cosmetic. ~20% likelihood.
3. **Timely** — popular in beauty/wellness more broadly. ~10% likelihood.

If the answer is anything outside these three, that's fine — the Frontline install adapts. Just need to know what we're integrating with.

## Timing

Send Message 1 today or tomorrow. No rush — the Eonia Frontline install kicks off in parallel with DSK once DSK Day 7 is clean. We need the CMS name by then.
