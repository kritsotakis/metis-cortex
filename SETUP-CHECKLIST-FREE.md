# Metis Cortex — $0 Setup Checklist

> Everything below is **free** — no card details charged today. Each step is self-contained and reversible. Recommended order top-to-bottom; pick any starting point.
>
> **Total time if you knock all seven out in one sitting:** ~2 hours.

---

## 1. Cloudflare Email Routing — `info@metiscortex.au`

**Why this first:** the live site already says `info@metiscortex.au`. Until forwarding is live, mail to that address bounces and leads disappear. **5 minutes, $0 forever.**

### Steps

1. Open https://dash.cloudflare.com → log in as **peter@kritsotakis.com.au**
2. In the left sidebar, click **Websites** → click **`metiscortex.au`** (the zone)
3. In that zone's left sidebar, click **Email** (under "Routing" — if it's not there, click **Email Routing** in the search bar at top)
4. Click the **Get started** button. Cloudflare adds 3 MX records + 1 SPF TXT record to your DNS automatically (takes ~30 seconds — you'll see a success banner).
5. Click **Routing rules** (top tab) → click **Custom address**
6. Configure the rule:
   - **Custom address:** `info@metiscortex.au`
   - **Action:** Send to an email
   - **Destination:** `peter@kritsotakis.com.au`
   - Save
7. Cloudflare will email **peter@kritsotakis.com.au** with a verification link. **Click that link** to confirm the destination.
8. **Test:** open your phone's email, send a test from any address (e.g. your personal Gmail) → `info@metiscortex.au`. Should land in your kritsotakis inbox within ~30 seconds.

### Verify

```
Reply: "email routing live"
```

---

## 2. Calendly — free plan, demo URL

**Why:** the site's "Book a 15-min demo" button currently mailto-falls-back. Once Calendly URL exists, it goes to a real bookable demo flow. **15 min, $0 forever** (free tier covers our 1-event-type use case).

### Steps

1. Go to https://calendly.com → click **Sign up free** (top right)
2. Sign up with **peter@kritsotakis.com.au** (or `peter@metiscortex.au` if Cloudflare Email Routing is already done)
3. After verification, Calendly asks you to set up your first event:
   - **Event type:** One-on-One
   - **Name:** `Metis Cortex demo — 15 min`
   - **Description:** `Live demo of Zoe answering a real call. We'll dial a test number, you hear her qualify a fake lead and book it. Three minutes of demo, the rest is your questions.`
   - **Location:** Google Meet (Calendly auto-creates the link) OR Zoom
   - **Duration:** 15 minutes
   - **Date range:** Rolling 30 days
   - **Available hours:** Mon–Fri 09:00–17:00 AEST (or whatever fits your calendar)
   - **Buffer:** 15 min before, 15 min after
   - **Min notice:** 4 hours before booking
4. Add **invitee questions** (these route to Zoe's qualification — important for the sales prep):
   - "What's your business and where are you based?" (required)
   - "How many calls/messages a week are you missing?" (required)
   - "What's the biggest bottleneck — answering, follow-up, or database activation?" (required)
5. **Confirmation page:** copy/paste the body from [Desktop/metis-cortex/CALENDLY-CONFIRMATION-EMAIL.md](Desktop/metis-cortex/CALENDLY-CONFIRMATION-EMAIL.md)
6. Save and copy the public URL (looks like `https://calendly.com/peter-kritsotakis/metis-cortex-demo` or similar)

### Verify

```
Reply with: "Calendly URL: <paste the URL>"
```

When you reply, I'll flip the site config — every "Book a 15-min demo" button on the site stops mailto-falling-back and starts pointing at your Calendly. One-line site change.

---

## 3. Twilio — account signup (no number purchase yet)

**Why:** verify your business now so when you start DSK pilot Day 1, the only step left is "buy a number" ($1/mo) — saves 30 min of business-verification waiting on Day 1 itself. **10 min, $0 today.**

### Steps

1. Go to https://www.twilio.com/try-twilio → click **Sign up**
2. Sign up with **peter@kritsotakis.com.au**
3. Twilio verifies your phone number via SMS — enter `0414 885 366`
4. After login, you'll be asked: "What do you want to do with Twilio?" → pick **Voice** → "I'll let you know later" for everything else
5. Skip the credit card prompt for now (you can add it later when you actually buy a number)
6. **Important:** complete the **business verification** flow:
   - Twilio dashboard → **Account** → **General Settings** → **Business Profile** (or similar)
   - Submit ABN 45 984 876 899 + business name "Metis Cortex" (registered with ASIC 9 May 2026)
   - Approval takes 1–3 business days. Without it you can't send SMS in Australia.

### Verify

```
Reply: "Twilio account ready"
```

(No URL to share — account is account-only at this stage.)

---

## 4. Retell AI — account signup (no credits yet)

**Why:** Retell is where Zoe lives. Same as Twilio — verify and onboard now so DSK Day 1 just needs credits added. **10 min, $0 today.**

### Steps

1. Go to https://www.retellai.com → click **Get Started** or **Sign Up**
2. Sign up with **peter@kritsotakis.com.au**
3. Retell asks for use-case: **Inbound voice agent for SMB receptionist**
4. Skip card / credits step for now — you can add credits when ready to install on DSK
5. Browse the dashboard:
   - **Agents** → see template agents (don't build one yet)
   - **Voices** → preview Australian female voices (you'll pick one for Zoe later — try `aura-2-australian-female` or similar)
6. Bookmark the docs at https://docs.retellai.com — you'll reference these during DSK install

### Verify

```
Reply: "Retell account ready"
```

---

## 5. Stripe — account + ABN verification

**Why:** required to take payment when DSK pilot completes + first paying client signs. No fees until first transaction. **30 min** because Australian business verification asks for ABN + bank docs.

### Steps

1. Go to https://dashboard.stripe.com/register → click **Sign up**
2. Sign up with **peter@kritsotakis.com.au**
3. Country: **Australia**
4. Business type: **Company / Trust**
5. Business details:
   - Legal entity name: **Kritsotakis Family Trust**
   - ABN: **45 984 876 899**
   - Trading name: **Metis Cortex**
   - ASIC business name registration: **Metis Cortex (registered 9 May 2026)**
   - Address: your business address (likely the trust's registered address — Belrose, NSW per the ASIC registration)
6. Bank account: link your business bank account (Westpac/CommBank/etc.)
7. Identity verification: Stripe asks for a director's ID — submit Karren's (she's the sole director of Kritsotakis Investments Pty Ltd which is the corporate trustee). You can also list yourself as a beneficial owner via the trust's records.
8. Wait for Stripe approval (typically 1–3 business days)

### Verify

```
Reply: "Stripe verified"
```

---

## 6. Plausible Analytics — 30-day free trial

**Why:** privacy-respecting analytics, no cookie banner needed (matches our /privacy page commitments). **5 min, free for 30 days, €9/mo after if you keep it.**

### Steps

1. Go to https://plausible.io → click **Start free trial**
2. Sign up with **peter@kritsotakis.com.au**
3. After verification, click **Add a site**:
   - Domain: `metiscortex.au` (no www, no protocol)
   - Timezone: **Australia/Sydney**
4. Plausible shows you a snippet like:
   ```html
   <script defer data-domain="metiscortex.au" src="https://plausible.io/js/script.js"></script>
   ```
   **Don't paste this anywhere yourself** — once you reply with the trigger phrase below, I'll add it to `src/app/layout.tsx` in one commit.
5. Optional: in dashboard **Settings → Visibility**, set the dashboard to **Anyone with the link** — lets me + Cowork verify pageviews without logging in. Keep the URL private.

### Verify

```
Reply: "Plausible site ready" (and the dashboard URL if you made it public)
```

I add the script to layout.tsx, push, Cloudflare deploys ~2 min, first pageview lands in your dashboard.

---

## 7. LinkedIn Company Page — Metis Cortex

**Why:** brand presence + first-100 outreach unlock + lets you tag Metis Cortex on personal posts. Assets and copy already in repo. **30 min, $0.**

### Steps

1. Make sure you're logged into LinkedIn as **Peter Kritsotakis**
2. Top nav → **Work** dropdown (right side, near your photo) → **Create a Company Page**
3. Choose page type: **Company** (NOT Showcase, NOT Educational, NOT Small Business)
4. Page identity:
   - **Name:** `Metis Cortex`
   - **LinkedIn URL:** `linkedin.com/company/metis-cortex` (try this; if taken, try `metiscortex` or `metiscortex-au`)
   - **Website:** `https://metiscortex.au`
   - **Industry:** `Business Consulting and Services`
   - **Company size:** `1–10 employees`
   - **Company type:** `Privately held`
   - **Tagline:** *"AI receptionist for Australian service businesses. 14-day install. 100% answered or your money back."* (or whatever's in [LINKEDIN-COMPANY-PAGE-COPY.md](Desktop/metis-cortex/LINKEDIN-COMPANY-PAGE-COPY.md))
5. Upload **logo**:
   - File: [Desktop/metis-cortex/public/brand/social/linkedin-company-logo.png](Desktop/metis-cortex/public/brand/social/linkedin-company-logo.png) (or `linkedin-company-square.png` if that's what's in the folder)
6. Upload **cover image**:
   - File: [Desktop/metis-cortex/public/brand/social/linkedin-company-cover.png](Desktop/metis-cortex/public/brand/social/linkedin-company-cover.png) (1128×191)
7. Paste **About** copy from [Desktop/metis-cortex/LINKEDIN-COMPANY-PAGE-COPY.md](Desktop/metis-cortex/LINKEDIN-COMPANY-PAGE-COPY.md) (full About block)
8. Add **Specialities** (max 20) — paste from same doc
9. Save + Publish
10. **Update your personal profile**:
    - Add experience: `Founder, Metis Cortex` — link to the new company page
    - Update headline: paste the personal headline line from the copy doc

### Verify

```
Reply: "LinkedIn page: <URL>"
```

I'll flip `SOCIAL.linkedinCompany` in [Desktop/metis-cortex/src/lib/site.ts](Desktop/metis-cortex/src/lib/site.ts) — Footer link relabels from "LinkedIn (founder)" to "LinkedIn", JSON-LD `sameAs` schema auto-populates with the company URL.

---

## What's deliberately NOT on this list (paid items, hold for DSK Day 1)

| Tool | Cost | Why hold |
|---|---|---|
| GoHighLevel Starter | A$148/mo | Required to deliver Zoe; no point until you actually start DSK pilot |
| Twilio AU phone number | A$1/mo + usage | Same |
| Retell credits | A$25–50 minimum | Same |
| Google Workspace | A$12/mo per user | Optional — you can keep using personal Gmail until you have a team |

**Total ongoing $0 cost after this checklist:** A$0/mo (Plausible bills you ~A$15/mo after the 30-day trial — if you don't want it, cancel before day 30).

---

## Reply formats — the 7 trigger phrases

When you complete each task, reply with the exact phrase. Each one fires a specific Code-side update.

| Task | Trigger phrase | What it fires |
|---|---|---|
| 1 | `email routing live` | Verifies email path; closes the bounce-risk loop |
| 2 | `Calendly URL: <paste>` | Code flips `BOOKING.calendlyUrl` in site config; CTAs go live |
| 3 | `Twilio account ready` | STATUS log; nothing on the site |
| 4 | `Retell account ready` | STATUS log; nothing on the site |
| 5 | `Stripe verified` | STATUS log; ready for first paid subscription |
| 6 | `Plausible site ready` | Code adds tracker script to layout.tsx; deploys |
| 7 | `LinkedIn page: <URL>` | Code flips `SOCIAL.linkedinCompany`; Footer + JSON-LD update |

---

## After you finish all 7 — what's left to spend money on (when ready)

To start the DSK pilot Day 1 and actually take a real call with Zoe, you'll need (~A$200 first-week spend):

1. **GoHighLevel** — sign up Starter $97 USD/mo (~A$148/mo)
2. **Twilio AU local number** — $1 USD/mo (~A$2/mo)
3. **Retell credits** — minimum $25–50 USD load (~A$40–80)

That's the line where Metis Cortex stops being a marketing site and becomes a real business. The 7 tasks above get you everything-except-that for $0.
