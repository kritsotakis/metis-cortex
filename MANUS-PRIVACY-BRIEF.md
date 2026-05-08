# Brief for Manus — Metis Cortex privacy policy review

> **Purpose:** Review the draft privacy policy for the Metis Cortex marketing site. The policy is live at https://metiscortex.au/privacy. We need a second set of eyes before treating it as final — both legal-correctness and operator-readability.
>
> **Author:** Peter Kritsotakis (peter@kritsotakis.com.au) · Sydney, Australia · 2026-05-09
> **Site:** https://metiscortex.au

---

## Context

**The business:** Metis Cortex installs an AI receptionist (Zoe) on Australian SMBs. Single founder + own-business pilots (DSK Property Cleaning + Eonia) before external sales. Pre-product-market-fit, ~0 paying external clients.

**Operating entity:** Kritsotakis Family Trust (ABN 45 984 876 899). Sydney, NSW. Trustee: Kritsotakis Investments Pty Ltd (ACN 153 844 136).

**Why we wrote a privacy policy:** The site collects personal information (name, email, phone, business name, qualifying-question answers) when someone books a demo via Calendly. The policy is referenced in the footer of every page. **Australian Privacy Act 1988** + **APPs (Australian Privacy Principles)** apply.

**Where the policy lives in the codebase:** [src/app/privacy/page.tsx](src/app/privacy/page.tsx) — a Next.js page. The full text is the focus of this review.

**Current status:** Draft, deployed as a placeholder so the footer link doesn't 404. Not yet treated as final. Awaiting your review before locking.

---

## Data flow we're describing

What we collect (or will collect):
1. **Booking enquiries** via Calendly: name, email, phone, business name, three qualifying-question answers.
2. **Email correspondence** to peter@kritsotakis.com.au or hello@metiscortex.au (forward in flight).
3. **Server logs** via Cloudflare: IP, user agent, request path, timestamp.
4. **Pilot/customer data:** call transcripts (via Retell AI), lead notes (in GoHighLevel), billing details (Stripe — future), CRM integration credentials.
5. **Future analytics:** Plausible (privacy-respecting, cookieless) — wired this week.

Third-party processors:
- **Calendly** (US) — booking storage
- **Cloudflare** (global edge with Sydney POP) — hosting, DNS, security, future Email Routing
- **Google Workspace** (US) — email and docs (provisioning in flight)
- **Retell AI** (US, future) — AI voice agent
- **GoHighLevel** (US, future) — CRM and workflows
- **Twilio** (US/AU, future) — telephony numbers
- **Plausible** (EU, future) — pageview analytics, no cookies
- **Stripe** (US/AU, future) — billing

We don't sell data, share for advertising, or use it to train third-party AI models without explicit consent.

---

## Specific questions we want you to interrogate

### 1. Notifiable Data Breaches (NDB) scheme coverage

Section 6 of the policy mentions: *"If a data breach happens that is likely to cause serious harm, we will notify you and the Office of the Australian Information Commissioner (OAIC) as required by the Notifiable Data Breaches scheme."*

**Does this language meet the threshold?** The NDB scheme has specific assessment timeframes (30-day max), specific notification content requirements, and specific obligations around what triggers a notifiable breach. Is one sentence enough, or do we need:
- An explicit statement of our breach response process
- Reference to the 30-day assessment window
- Reference to "remedial action" attempts before notification
- A privacy contact officer role

**The risk we're trying to size:** if a breach happens and the OAIC reviews our policy, does this clause shield us or expose us?

### 2. Liability exposure on specific phrasings

Some statements we've made:
- *"We do not sell your information, share it for advertising, or use it to train third-party AI models without your specific consent."*
- *"We choose providers we believe meet a reasonable standard of security and contractual protection."*
- *"We use reputable hosting and SaaS providers, encrypted connections (HTTPS/TLS), strong passwords, and two-factor authentication on accounts that hold personal information."*

**Are any of these statements creating provable claims that we then have to live up to?** For example:
- "We do not sell your information" — if a future business pivot involves data licensing, are we boxed in?
- "Reasonable standard of security" — if a third party (Calendly, Cloudflare) is breached, do we have a contractual liability beyond what they owe us?
- "Two-factor authentication on accounts that hold personal information" — if a single account (e.g. a bookkeeper's Gmail) doesn't have 2FA, is that a policy violation?

**What we want from you:** flag clauses where the language is too tight or imprecise — anywhere we should soften, qualify, or add "to the extent reasonable" hedges without sounding sketchy.

### 3. Biometric voice data — the gap we know about

The policy doesn't currently address voice recordings. But:
- **Retell AI** records every call Zoe takes — the customer's voice is captured.
- **Calendly** doesn't capture voice but a Demo call we run on Zoom or Google Meet would.
- **Voice biometrics are arguably "sensitive information"** under APP 3 — higher consent threshold than ordinary personal information.

We currently have no clause addressing:
- Whether call audio is retained, and for how long
- Whether voice data is used to train any model (we don't, but should explicitly say)
- Customer rights to delete voice recordings
- Whether the AI agent (Zoe) discloses to the caller that they're being recorded — Australian state law (NSW Surveillance Devices Act, similar in other states) generally requires consent

**What we want from you:** is this a real gap or are we over-thinking it? If it's a real gap, what's the minimum clause set that closes it?

### 4. Children's data — age threshold

The policy currently says: *"We do not knowingly collect information from anyone under 18."*

**Two issues:**
- The Privacy Act doesn't define a specific age. Some operators use 16. Others use 13 (US influence — COPPA).
- Our actual ICP is owner-operators of SMBs — likely all 25+. The under-18 clause is boilerplate. Do we need it at all?

**What we want from you:** is "18" the right threshold for an Australian B2B SaaS, or should we drop the clause entirely since there's zero realistic risk?

### 5. Operator readability

This is a B2B policy aimed at owner-operators of small Australian service businesses — not lawyers, not procurement teams. They'll skim it for one minute and ask "what does this mean for me?"

**What we want from you:** read it as a Sydney cleaning business owner. Where does it lose you? Where does it sound like SaaS legalese? Where could plain English replace defensive boilerplate?

### 6. The clause we forgot

What's the obvious clause we've omitted that another set of eyes catches? A few possibilities to rule in or out:
- **Cross-border data transfer** — we mention overseas storage (section 4) but is it sufficient under APP 8.1?
- **Data subject access rights** — section 8 covers this; is it enough?
- **Consent withdrawal mechanism** — implicit in section 8; should it be explicit?
- **Third-party-data clause** — if a customer sends us a list of *their* customers (CRM upload), what obligations do we take on?
- **Marketing communications** — we'll send onboarding emails; is the consent flow + opt-out adequately described?
- **Cookies + analytics** — section 7 currently soft on this. Plausible doesn't use cookies; Cloudflare does for security. Need to be more specific?

---

## What we want from you

A pragmatic review, not a legal opinion. Specifically:

1. **The clause that's actually risky.** Out of everything we've written, what's the single sentence most likely to bite us if challenged?
2. **The gap that's actually risky.** Out of everything we've omitted, what's the single missing clause most likely to cause regulator action or customer complaint?
3. **The operator-readability fix.** One concrete rewrite suggestion for a section that currently reads like SaaS boilerplate.
4. **Specifically: voice biometrics.** Yes-or-no — do we need to add a clause? If yes, draft the minimum text.
5. **Verdict.** Is this draft fit for purpose for a pre-PMF AU B2B SaaS at our scale, or do we need a lawyer pass before locking it?

---

## Reference

| Doc | What |
|---|---|
| [src/app/privacy/page.tsx](src/app/privacy/page.tsx) | The actual policy (the focus of the review) |
| [STATUS.md](STATUS.md) | Canonical state — In Flight, Done, Open Loops |
| [MANUS-BUSINESS-BRIEF.md](MANUS-BUSINESS-BRIEF.md) | Companion brief for business plan review |
| Australian Privacy Act 1988 | https://www.legislation.gov.au/Details/C2014C00076 |
| OAIC privacy guidelines | https://www.oaic.gov.au/privacy/privacy-guidance-for-organisations-and-government-agencies |
