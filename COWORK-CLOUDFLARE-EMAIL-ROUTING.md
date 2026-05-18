# Cowork brief — Cloudflare Email Routing for `info@metiscortex.au`

> **For:** Cowork (you drive; only escalate to Peter on a specific blocker)
> **Authored by:** Claude Code, 2026-05-10 (revised — was previously addressed to Peter; corrected per Peter's directive that briefs default to Cowork, not him)
> **Goal:** Stand up Cloudflare Email Routing so `info@metiscortex.au` forwards to `peter@kritsotakis.com.au`. Live site already says `info@metiscortex.au` everywhere — without this, every prospect email bounces.
> **Trigger phrase on completion:** `email routing live`

---

## State of play

- ✅ Site live at https://metiscortex.au with `info@metiscortex.au` referenced in Footer, JSON-LD schema, /privacy contact line, 404 page, Hero phone CTA fallback
- ✅ Cloudflare zone for `metiscortex.au` already exists in Peter's account (`peter@kritsotakis.com.au`); zone is on Cloudflare nameservers (active green)
- ✅ Site config in repo at `src/lib/site.ts` already has `CONTACT.brandEmail = "info@metiscortex.au"` — every component pulls from this one constant
- ❌ No MX records for `metiscortex.au` yet — `info@metiscortex.au` bounces today
- ❌ No routing rule configured

**Cost:** $0 forever. Cloudflare Email Routing is free on the standard plan.

---

## Execution rule

**Cowork attempts via Kapture first. Escalate to Peter ONLY on a specific, named blocker** (e.g. "Cloudflare login screen demands the 6-digit 2FA code from Peter's phone — cannot proceed without him") — not pre-emptively, and not as the default path. Peter is busy and explicitly does not want to be the executor for clicks the agents can drive.

If Kapture's session has cookies for `dash.cloudflare.com` from a prior session, the run completes end-to-end. If it doesn't, you'll hit the login screen — that's the moment to escalate, with the precise URL + step Peter needs to unblock.

---

## What Cowork does

### 1. Open Cloudflare dashboard via Kapture

```
URL: https://dash.cloudflare.com/
```

If logged in → continue. If not → check whether Kapture can complete the email/password step (Peter's credentials may be in the password manager Kapture has access to). Hard 2FA prompt = escalation point (see "Escalation script" below).

### 2. Navigate to the metiscortex.au zone's Email Routing

- Sidebar → **Websites** → click `metiscortex.au`
- Zone sidebar → **Email** (sometimes labelled **Email Routing**; use the in-zone search if not visible)
- Click **Get started** — Cloudflare auto-adds 3 MX records + 1 SPF TXT record to DNS (~30 sec, success banner appears)

### 3. Configure the custom-address rule

- **Routing rules** tab → **Custom address**
- **Custom address:** `info@metiscortex.au`
- **Action:** Send to an email
- **Destination:** `peter@kritsotakis.com.au`
- **Save**

Cloudflare emails `peter@kritsotakis.com.au` a destination-verification link. **Peter must click that link** — this is the one part you can't drive (the link is in his inbox, behind his auth). Tell him in PAIR.md exactly what to look for ("subject: Verify your email address with Cloudflare; sender: noreply@notify.cloudflare.com") and set `Peter action needed: yes` only for this single step.

### 4. Verify MX records propagated

```bash
dig MX metiscortex.au +short
```

Expected:
```
1 route1.mx.cloudflare.net.
2 route2.mx.cloudflare.net.
3 route3.mx.cloudflare.net.
```

### 5. Verify SPF record

```bash
dig TXT metiscortex.au +short | grep -i spf
```

Expected: TXT containing `v=spf1 include:_spf.mx.cloudflare.net ~all` (or Cloudflare's recommended SPF).

### 6. Send a verification email

From any external account Cowork has access to → `info@metiscortex.au`. Body: *"Cowork verification of info@ forwarding — please confirm this lands in your peter@kritsotakis.com.au inbox."* Wait ~30 sec and confirm Peter received it (one ping in PAIR.md is fine; don't make him watch the inbox).

### 7. Update STATUS.md

Append to **Done This Sprint**:

> 2026-05-10 — `info@metiscortex.au` Cloudflare Email Routing live. MX + SPF records auto-provisioned by Cloudflare. Forward verified by external test send → peter@kritsotakis.com.au. Footer + JSON-LD + /privacy + 404 + Hero phone CTA fallback all already pull from `CONTACT.brandEmail` in `src/lib/site.ts` — no code changes required. Cowork (Kapture-driven setup + verify) + Peter (single destination-verification click).

Close in **Open Loops**:
- "🔴 SET UP CLOUDFLARE EMAIL ROUTING for info@metiscortex.au"
- Bounce-risk on info@ closed

Mirror to `~/.claude/memory/metis-cortex-status.md` (Code will sync if filesystem write to that path is out of Cowork's scope).

### 8. Post to PAIR.md

```
### YYYY-MM-DD HH:MM — cowork → code
**Did:** Email routing for info@metiscortex.au verified live. MX + SPF records propagated. External test send delivered to Peter.
**Need from you:** nothing — fyi only. CONTACT.brandEmail already flipped to info@metiscortex.au in commit 6b695b5; Code-side wiring is complete.
**Status:** 🟢 done
```

---

## Escalation script (only if Kapture genuinely can't proceed)

Set `Peter action needed: yes` in PAIR.md AND tell him in chat. Use this template:

> **Blocker:** <one specific thing — e.g. "Cloudflare 2FA prompt; Kapture session has no TOTP for your account">
> **What I need from you (60 sec):** <the smallest possible action — e.g. "open https://dash.cloudflare.com, complete 2FA, then reply 'logged in' so Cowork resumes">
> **Why you specifically:** <2FA on your phone | card | signature | etc.>

Don't escalate the whole 9-step procedure. Escalate only the unblock.

---

## What Cowork must NOT do

- **Do not** route the whole task to Peter as a "9-step procedure for him" — try Kapture first.
- **Do not** modify the `metiscortex.au` zone's existing DNS records (the A records pointing at Cloudflare Pages must stay untouched). Email Routing only ADDS MX + SPF.
- **Do not** declare the task done without the test send arriving in Peter's kritsotakis inbox. MX propagation is one thing; deliverability is another.
- **Do not** modify any code in the repo. Code-side work is complete.

---

## Confirmation Cowork posts back

After all checks pass:

```
✅ Email routing live for info@metiscortex.au.
   Verified:
   - MX records: route1/route2/route3.mx.cloudflare.net (dig confirmed)
   - SPF record: v=spf1 include:_spf.mx.cloudflare.net ~all
   - External test send from <Cowork's verification email> delivered to peter@kritsotakis.com.au at HH:MM
   STATUS.md updated, memory mirror flagged for Code.
   PAIR.md notification posted.
   info@ bounce-risk closed.
```

If escalation was needed:

```
⚠️ Email routing partial — Peter unblock required.
   Reached: <step number/name>
   Blocker: <specific>
   Posted to PAIR.md with `Peter action needed: yes`
   Will resume on his confirmation.
```

---

## Reference

- [STATUS.md](STATUS.md) — canonical state
- [COWORK-PARALLEL-TRACKS.md](COWORK-PARALLEL-TRACKS.md) — broader queue (Calendly, LinkedIn, ASIC, etc.)
- [SETUP-CHECKLIST-FREE.md](SETUP-CHECKLIST-FREE.md) — $0 setup checklist; this task is item #1 of 6 free tasks
- `src/lib/site.ts` — `CONTACT.brandEmail` already set to `info@metiscortex.au`; no code change needed when forwarding goes live
