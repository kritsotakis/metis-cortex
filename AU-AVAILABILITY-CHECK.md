# Metis Cortex SaaS Stack — Australian Availability Check

**Date verified:** 2026-05-08
**Verifier:** Claude Code (research subagent)
**Scope:** 7 vendors — Retell AI, GoHighLevel, Twilio, NotebookLM, Cliniko, Pabau, Halaxy

---

## 1. TL;DR

**Twilio, Cliniko, and Halaxy are clean AU plays — Twilio has full AU regulatory tooling, Cliniko hosts in AWS Sydney with Australian Privacy Principles compliance, Halaxy is AU-built and free to start.** Retell AI and GoHighLevel both work in Australia today but route everything through US infrastructure with USD billing — Retell stores all PII in US AWS with no AU residency option, and GoHighLevel requires ABN-based A2P registration via its Twilio sub-account with prices in USD. **No outright blockers, but the US-hosted tools (Retell, GHL, NotebookLM) all need a Privacy Act 1988 disclosure to clinic clients before processing patient data — that is the real operational warning.**

---

## 2. Per-Tool Verdict Table

| Tool | AU signup | AU phone numbers | Data residency | AUD billing | Key gotcha | Verdict |
|---|---|---|---|---|---|---|
| **Retell AI** | Self-serve, no waitlist | NO native — must BYO via Twilio/Telnyx SIP | US only (AWS, no AU/EU regions) | USD only | No AU-accent voice list published; PII stored in US | ⚠️ Works, but US-hosted |
| **GoHighLevel** | Self-serve | Yes via LC Phone (Twilio under hood); ABN required for A2P | US (no AU residency option documented) | USD pricing; AU SMS ~$0.0515/seg (≈6.5x US) | A2P uses ABN not ACN; carrier vetting 24-72h | ⚠️ Works, USD only |
| **Twilio** | Self-serve | Yes — local, mobile, toll-free; ASIC docs + ABN required | Global; AU region available for some products | USD by default; AUD invoicing for some accounts (confirm at signup) | KYC update rolling out late May 2026; identity proof needed for local numbers | ✅ AU-ready |
| **NotebookLM** | Self-serve via any Google account | N/A | Google Cloud (no AU-only region for free/Plus) | USD via Google AI Pro / Workspace | Personal account uploads MAY be reviewed if you give thumbs-up/down feedback; Workspace accounts protected | ⚠️ Use Workspace acc only for clinic data |
| **Cliniko** | 30-day free trial, no card | N/A (clinic software, not telephony) | AU — AWS Sydney region | USD list price (was AUD historically — confirm at checkout) | None material — Australian Privacy Principles aligned | ✅ AU-native |
| **Pabau** | Self-serve | N/A | Not publicly disclosed for AU | USD pricing on .com site | UK HQ; AU support timezone unclear; data residency unverified | ⚠️ Confirm hosting at signup |
| **Halaxy** | Free, instant, no card | Optional add-on dedicated practice phone | AU (bank-grade encryption, AU-based) | AUD (AU-built platform) | Free core; pay-per-use credits for SMS/telehealth/AI Scribe | ✅ AU-native |

---

## 3. The 3 Things Peter Needs to Know Before Signing Up

### 3.1 Retell AI ships every voice call through US AWS — disclose this to clinic clients
Retell's compliance page states all PII is stored and processed in US AWS, with **no EU or AU regional option**. They are SOC 2 Type 2 + HIPAA + GDPR compliant, but make zero mention of Privacy Act 1988 or APP. For Eonia-style clinics handling health data, this means: (a) update the clinic's privacy policy to disclose offshore voice processing, (b) get explicit patient consent for voice AI handling, (c) plan latency budget — Sydney→US-West round trip adds ~150-200ms, which is borderline for sub-second voice AI conversational feel. Retell does NOT provision +61 numbers natively — you must bring your own Twilio/Telnyx number via SIP trunk.

### 3.2 GoHighLevel A2P registration in Australia uses ABN, not ACN — and SMS to AU mobiles costs ~6.5x US rates
The platform supports AU phone numbers (LC Phone, which is Twilio under the hood). Registration requires the **ABN** (not the ACN), and the standard A2P brand vetting is 24-72h with carrier review. Critical pricing watch-out: SMS to AU numbers is ~$0.0515 per segment vs ~$0.0079 for US — at 1,000 SMS/month per clinic that's ~AUD$80/mo just on SMS, before voice or platform fees. All GHL pricing is USD; Stripe BECS Direct Debit is supported for the agency's own subscription billing.

### 3.3 NotebookLM is fine in Australia — but use a Workspace account, not a personal one, for any clinic data
NotebookLM is available in Australia today on any Google account (free tier: 100 notebooks, 50 sources/notebook, 3 audio overviews/day; Plus at $7.99 USD/month doubles limits). Per Google's published policy: **personal account** uploads are not used for model training BUT thumbs-up/down feedback may be reviewed by trained humans (with account de-identification). **Google Workspace / Workspace for Education** accounts have stronger protection — uploads, queries and responses are never reviewed and never used for training, regardless of feedback. Recommendation: provision NotebookLM under the Metis Cortex Google Workspace tenant, not Peter's personal Gmail, before uploading any clinic SOPs or client documents.

---

## 4. AU-Native Alternatives (where they exist)

| US tool | AU-built / AU-native alternative | Notes |
|---|---|---|
| **Retell AI** (voice agent) | **VoiceFlow ANZ partners**, **Sestek** (TR but APAC region), **Bolna** (in Retell ecosystem). No direct AU-built voice-agent platform of equivalent maturity as of May 2026 — most AU clinics route to Retell/Vapi/Bland with disclosure. | Gap in market — no AU equivalent yet |
| **GoHighLevel** (CRM/workflow) | **HubSpot APAC** (hosted in Australia tier available on Enterprise), **ActiveCampaign** (US but with AU billing), **Keap** (US). Closer to AU-native: **Lead Forensics ANZ**, **Maropost** (Toronto/Sydney). | No drop-in AU GHL clone exists |
| **Twilio** | **MessageMedia** (Melbourne-based, AU-native, ABN-aware A2P, AUD billing), **ClickSend** (Sydney, AU-native), **SMSGlobal** (Melbourne). All three offer AU local + mobile numbers and AUD invoicing. | MessageMedia is the closest Twilio peer for AU |
| **NotebookLM** | **Anthropic Claude Projects** (US-hosted but enterprise tier supports regional residency), **Microsoft Copilot for M365** (AU tenant available via Microsoft 365 Enterprise) | No AU-native equivalent |
| **Cliniko** | Already AU-native (Melbourne HQ) | Baseline |
| **Pabau** | **Cliniko**, **Halaxy**, **Power Diary** (AU), **Coreplus** (AU) | Multiple AU alternatives |
| **Halaxy** | Already AU-native (Melbourne HQ, free tier) | Baseline |

---

## 5. Sources (all fetched 2026-05-08)

- Retell AI compliance documentation — https://docs.retellai.com/general/compliance
- Retell AI phone-number provisioning guide — https://www.retellai.com/blog/how-to-buy-an-ai-phone-number-a-guide-on-your-options-and-providers
- Retell AI community: data residency clarification thread — https://community.retellai.com/t/request-for-clarification-on-data-residency-regional-hosting-and-enterprise-plan/2424
- Retell AI privacy policy — https://www.retellai.com/legal/privacy-policy
- GoHighLevel AU phone-number purchasing — https://help.gohighlevel.com/support/solutions/articles/155000003226-how-to-purchase-a-phone-number-in-a-sub-account
- GoHighLevel A2P 10DLC brand approval (incl. ABN guidance) — https://help.gohighlevel.com/support/solutions/articles/155000000508-a2p-10dlc-brand-approval-best-practices
- GoHighLevel LC Phone pricing — https://help.gohighlevel.com/support/solutions/articles/48001223556-lc-phone-pricing-billing-guide
- GoHighLevel Australia adoption + BECS billing — https://ghlcentral.com/gohighlevel-australia/
- Twilio Australia regulatory guidelines — https://www.twilio.com/en-us/guidelines/au/regulatory
- Twilio AU voice pricing — https://www.twilio.com/en-us/voice/pricing/au
- Twilio AU SMS pricing — https://www.twilio.com/en-us/sms/pricing/au
- Twilio AU phone-number terms — https://www.twilio.com/en-us/legal/service-country-specific-terms/au-phone-numbers
- NotebookLM plans page — https://notebooklm.google/plans
- NotebookLM privacy & terms (Google Help) — https://support.google.com/notebooklm/answer/17004255
- Cliniko pricing — https://www.cliniko.com/pricing/
- Cliniko security (AWS Sydney hosting) — https://www.cliniko.com/security/
- Cliniko Australian Privacy Principles compliance guide — https://help.cliniko.com/en/articles/4274054-how-cliniko-helps-you-comply-with-the-australian-privacy-principles
- Pabau pricing — https://pabau.com/pricing/
- Pabau AU EMR market guide — https://pabau.com/blog/top-10-emr-software-in-australia-2026-guide
- Halaxy pricing (AU) — https://www.halaxy.com/pricing/au
- Halaxy security — https://www.halaxy.com/article/security
- AWS Australia data privacy — https://aws.amazon.com/compliance/australia-data-privacy/

---

**Items marked "Unverified — confirm at signup":**
- Pabau exact AU data-residency location (UK HQ, APAC expansion stated but no public AU data-centre disclosure)
- Cliniko's current display currency at AU billing checkout (historically AUD; current public list shows USD)
- Retell AI Australian-accent voice catalogue (providers ElevenLabs/Cartesia/Deepgram/MiniMax all have AU voices, but Retell publishes no consolidated AU-voice list — verify in dashboard at signup)
- Twilio AU local-number verification SLA (digital verification post-submission stated; no published time SLA — community reports 1-5 business days)
- GoHighLevel AUD billing for the platform fee (USD confirmed; AUD invoicing not documented)
