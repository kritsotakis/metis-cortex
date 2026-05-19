# AR Recovery — How It Actually Works

**Show her if she asks "how does it work technically?" — but don't lead with this.**

Most accountants don't care about the plumbing. They care about: does it run on its own, do they have control, is their data safe.

---

## The flow in plain English

```
1. Your Xero account
   └─ exports aged AR every morning at 6am
       │
       ▼
2. Metis Cortex engine
   ├─ matches every overdue invoice to a "tier" (T+7, T+14, T+21, T+30, T+45, T+60+)
   ├─ checks the "do not chase" list (VIPs, friends, payment plans)
   ├─ picks the right email/SMS template for the tier + client segment
   └─ drafts the chase comm in your firm's voice
       │
       ▼
3. Your firm's outbox
   ├─ email goes via your existing Outlook/Gmail (or via Brevo if you prefer)
   ├─ SMS goes via Twilio with your firm's name as sender
   └─ every send carries a one-tap payment link (Stripe / EzyCollect / your processor)
       │
       ▼
4. Client receives the chase
   ├─ pays via link → marked PAID in Xero automatically
   ├─ replies to email → flagged in your inbox for personal handling
   └─ ignores it → escalates to next tier in 7 days
       │
       ▼
5. Your dashboard
   ├─ live aged AR (drops as clients pay)
   ├─ per-client status: chased / responded / paid / escalated
   ├─ weekly summary email to you every Monday at 8am
   └─ phone-task auto-created in your CRM for T+30 cases (you call the hard ones)
```

---

## What's underneath (only mention if she asks)

| Component | Service |
|---|---|
| Workflow engine | n8n (self-hosted on Cloudflare) |
| Xero integration | Official Xero API (read-only on contacts + invoices, no write access) |
| Email sending | Brevo (or your existing tool if preferred) |
| SMS sending | Twilio with AU number |
| Dashboard | GoHighLevel (your dedicated tenant) |
| Templates | Drafted in your voice during kickoff, approved by you before live |
| Payment links | Stripe / EzyCollect / your existing processor |
| Data storage | Australian-hosted (Cloudflare AU region) |

---

## What she controls (this is the trust question)

✅ Every email template approved by her before going live
✅ "Do not chase" list — VIPs, friends, sensitive cases — entirely her call
✅ Schedule — she can pause anytime (e.g. EOFY rush, family emergency)
✅ Tone — formal / warm / direct, segmented per client tier
✅ Data — Australian-hosted; she can export everything; we delete on request

---

## What we DON'T do (the boundaries)

❌ We don't store her client tax data — only contact info + invoice metadata (amount + age + status)
❌ We don't write to Xero (read-only API) — invoices marked PAID by Xero, not us
❌ We don't give tax advice — comms are payment-chase only
❌ We don't replace her — she handles the hard conversations, the tricky clients, the strategic decisions
❌ We don't train AI models on her client data — never. Australian Privacy Act compliant.

---

## The sketch (if she wants a napkin version)

```
Xero  →  Tier logic  →  Templates  →  Email/SMS  →  Client pays
                              ↑                          │
                              │                          ▼
                         Her approval            Xero auto-updates
                                                        │
                                                        ▼
                                                  Dashboard
```

That's the whole product. Six boxes. One workflow. One vertical.

---

*Plain English wins. Pull this up only if she asks.*
