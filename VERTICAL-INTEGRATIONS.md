# Metis Cortex — Vertical Integrations Map

**Purpose.** When Zoe (Retell AI agent) takes a call for a Metis Cortex customer, she must (a) read availability, (b) write a booking, (c) push lead/contact data into the customer's CRM. This document maps the dominant booking / CRM / practice-management platforms in 6 AU SMB verticals so we know which integrations to build first.

**Stack assumed.** Retell AI (voice) → GoHighLevel (orchestration + CRM) → customer's vertical platform via API/webhook/Zapier/Make. Twilio underneath for telephony.

**Legend.**
- API: Yes / Limited (gated/partner) / No / Unverified
- Webhook: Yes / No / Polling-only
- Zapier / Make: Native / Beta / via Webhooks / None
- GHL native: Yes / No (most are No — GHL leans on its own calendar + Zapier/webhooks)
- AU prevalence: Small / Medium / Large
- Complexity: 1 (trivial Zapier) → 5 (custom OAuth + write API + edge cases)

---

## 1. Hospitality (restaurants, cafes, bars)

| Platform | API | Webhook | Zapier | GHL native | AU prevalence | Complexity | Notes |
|---|---|---|---|---|---|---|---|
| **SevenRooms** | Limited (partner-provisioned) | Yes | via Webhooks | No | Medium-Large (premium venues) | 4 | OAuth2; must request creds + webhook setup via SevenRooms rep. `api-docs.sevenrooms.com` is gated. |
| **NowBookIt** | Unverified — check at sales call | Unverified | None apparent | No | **Large in AU/NZ** (11k+ venues) | 4 | Lightspeed/Square/Impact Data partners only; no public dev portal found. |
| **ResDiary** | Yes (partner portal) | Yes | via Webhooks | No | Medium-Large (AU pubs, multi-venue) | 3 | Separate API creds via support; webhook-first design — good fit for Zoe write-backs. |
| **OpenTable** | Limited (affiliate-gated, 3-4 wk approval) | Yes (for partners) | via Webhooks | No | Medium (skewed to CBD/fine dining) | 5 | Application required; restricts who can write reservations. Hard for sub-10-client agency to access. |
| **Tock** (Squarespace) | Limited | Limited | via Webhooks | No | Small in AU | 4 | Squarespace-owned since 2021; primarily widget/embed. Direct API gated. |
| **Mr Yum / me&u** | Limited (POS partner) | Likely (via partner) | None apparent | No | Medium (QR ordering, not bookings) | 5 | Ordering platform — not really a booking system. Skip unless customer specifically needs order capture. |
| **Quandoo** | Yes (Partner API, public docs) | Yes | via Webhooks | No | Small-Medium (more EU than AU) | 3 | Widget / direct / portal tiers. Direct integration requires Joint DPA. |

**AU hospitality verdict.** Build **ResDiary** first (open partner API + webhooks, big AU footprint), then **SevenRooms** (premium venues that pay). NowBookIt is the dark horse — huge AU footprint but no obvious public API; needs a sales-call discovery before quoting.

---

## 2. Real estate (boutique agencies, property mgmt)

| Platform | API | Webhook | Zapier | GHL native | AU prevalence | Complexity | Notes |
|---|---|---|---|---|---|---|---|
| **VaultRE / MRI Vault** | Yes (`docs.api.vaultre.com.au`) | Yes | via Webhooks | No | **Large** (market leader AU/NZ) | 3 | "Open API-first"; 380+ integrations live. Must register as accredited partner. |
| **Box+Dice / MRI Box and Dice** | Yes (Apiary docs) | Limited | via Webhooks | No | Large (1,100+ AU offices) | 3 | Now MRI-owned. Apiary docs at `websiteboxdiceapi.docs.apiary.io`. |
| **Eagle Software / MRI Eagle** | Yes (limited public docs) | Unverified | None apparent | No | Medium | 4 | Cloud CRM; integrates with IRE, Realworks, REI Forms Live. Contact for keys. |
| **Realhub / Realbase** | Yes (`api-docs.realhub.com.au`) | Likely | via Webhooks | No | Medium-Large (campaign/marketing side) | 3 | Two auth modes (API key + user OAuth). More marketing/listings than CRM. |
| **Inspect Real Estate (Reapit Lettings)** | Yes (XML feed + integration partners) | Limited | None apparent | No | Large (rentals/inspections) | 4 | Communicates via XML feeds + integrator partnerships. Booking inspections is the high-value Zoe use case. |
| **Zenu** | Unverified — check at sales call | Unverified | Unverified | No | Small | 4 | Limited public footprint; ask in sales call. |

**AU real-estate verdict.** **VaultRE** is the must-have integration — most market share, cleanest docs. **Inspect Real Estate** is highest-value because Zoe scheduling rental inspections solves a real, daily, voice-driven workflow. **Box+Dice** rounds out the top three.

---

## 3. Healthcare (medical / dental / allied health)

| Platform | API | Webhook | Zapier | GHL native | AU prevalence | Complexity | Notes |
|---|---|---|---|---|---|---|---|
| **Cliniko** | Yes (`docs.api.cliniko.com`) | **No native webhooks** (poll only) | Not native (APIANT, Pabbly) | No | **Large** (allied health AU) | 3 | 200 req/min/user rate limit. No webhooks → must poll for changes. Native Zapier missing as of 2025. |
| **Pabau** | Yes (open API + dev programme) | Yes | Native | No | Medium AU (UK/global strong) | 2 | Best-in-class for our use-case. Read/write appointments, patient, invoice. Native Zapier + Make. |
| **Halaxy** | Yes (FHIR-based) | Limited | via Webhooks | No | Medium-Large (allied health AU) | 4 | **Costs 150 credits/mth** to use API; FHIR standard adds learning curve. |
| **Best Practice (Bp Premier)** | Yes (FHIR via Halo Connect) | Limited | via Webhooks | No | **Very Large** (70%+ of AU GPs) | 5 | FHIR facade is partner-only; SQL Passthrough also available via Halo Connect. Heavy compliance. |
| **Praktika** (dental) | Limited (widget + key for online booking) | Unverified | None | No | Medium (AU dental) | 3 | API key for online booking slots; minimal docs. AU-built, AU-only. |
| **Power Diary / Zanda** | **No public API** | No | None native | No | Medium-Large (allied health) | 5 | Confirmed no API; integrations only via pre-built partners (Stripe, Tyro, Mailchimp). Effectively un-integrable. Mark as blocker on sales calls. |
| **Nookal** | Yes (key-based) | Unverified | via Webhooks | No | Medium (AU allied health) | 3 | Practice manager enables API; common with form/ehr partners. |
| **Genie Solutions / Gentu** | Yes (Genie Partner API, FHIR, read-only mostly) | Unverified | None native | No | Large (specialist medical AU) | 4 | Magentus-owned. Read access today; write coming. Specialist focus (OB/GYN, ortho, derm). |

**AU healthcare verdict.** **Pabau** wins on integration ease (and is the natural Eonia fit). **Cliniko** wins on AU SMB volume — but the lack of webhooks means we'll burn cycles polling. **Power Diary / Zanda customers cannot be served by Zoe** without manual workarounds — qualify out at sales. Bp Premier is huge but is enterprise-grade integration via Halo Connect — not suitable for a 1-10-client agency.

---

## 4. Beauty / aesthetic (clinics, salons, spas)

| Platform | API | Webhook | Zapier | GHL native | AU prevalence | Complexity | Notes |
|---|---|---|---|---|---|---|---|
| **Timely** | Yes (REST, partner gated) | Limited | Native (basic) | No | **Large** AU (salon/spa) | 3 | NZ-AU origin, very common. Public dev docs sparse — request via support. |
| **Fresha** | Limited (data connectors + partner) | Limited | None native | No | **Very Large** (70k+ merchants global; AU strong) | 4 | Free for merchants → adoption huge; but partner API access tightly controlled. Several scraping APIs exist (Apify) — not a real integration path. |
| **Mindbody** | Yes (Public API v6 + Webhooks API) | **Yes (full webhooks API)** | Native | No | Medium-Large (fitness/wellness AU) | 2 | **Best-in-class API.** Webhooks deliver near-real-time events with retry. Use this as the gold-standard reference integration. |
| **Phorest** | Yes (REST, no webhooks — poll) | **No** | via Webhooks (polled) | No | Small-Medium AU | 3 | Email `api-requests@phorest.com` for access. Use `updated_at` to poll for changes. |
| **Pabau** | (see Healthcare row) | Yes | Native | No | Medium AU (medi-aesthetic) | 2 | Same platform as healthcare; doubles for aesthetic clinics like Eonia. |

**AU beauty verdict.** **Mindbody** is the easiest integration (full webhooks + Zapier native). **Timely** and **Fresha** have the AU footprint but gated API access — both need sales-call discovery to confirm tier. **Pabau** is the cleanest medi-aesthetic play (and our own Eonia precedent).

---

## 5. Cleaning / trades / field service

| Platform | API | Webhook | Zapier | GHL native | AU prevalence | Complexity | Notes |
|---|---|---|---|---|---|---|---|
| **Jobber** | Yes (GraphQL + webhooks, HMAC-signed) | Yes | **Native (premium)** | No | Large (AU/NZ tradies) | 2 | Webhooks must respond <1s + idempotent + HMAC verify. Triggers: New Client/Quote/Invoice/Job. Excellent for Zoe. |
| **ServiceM8** | Yes (`developer.servicem8.com`) | Yes (`api.servicem8.com/webhook_subscriptions`) | **Native** | No | **Very Large in AU** (DSK uses it) | 2 | OAuth add-on flow. Triggers: Job Created/Completed, Client Created. JSON POST, must return 200. |
| **Tradify** | **No public API** (per GetApp) | No | None native | No | Medium AU/NZ | 5 | Xero/MYOB sync only. Effectively un-integrable for booking — qualify out at sales. |
| **AroFlo** | Yes (paired with simPRO via Blackball middleware) | Limited | via Webhooks | No | Medium AU | 4 | Less public docs; integrations typically via partners. |
| **simPRO** | Yes (`developer.simprogroup.com`) | Yes (System → Setup → API → Webhook Subscriptions) | via Webhooks | No | Large (AU enterprise trades) | 3 | OAuth 1.0 (older); JSON-RPC/XML-RPC. Skewed to larger trades businesses, not 1-truck cleaners. |

**AU field-service verdict.** **ServiceM8** is the highest-priority build — biggest AU SMB cleaning/trades footprint, full webhook API, Native Zapier. **Jobber** is second (premium Zapier integration, modern GraphQL). Tradify customers are a no-go without a manual workaround.

---

## 6. Professional services (law, accounting, consulting)

| Platform | API | Webhook | Zapier | GHL native | AU prevalence | Complexity | Notes |
|---|---|---|---|---|---|---|---|
| **Clio** | Yes (`docs.developers.clio.com` v4) | Yes | **Native** | No | Medium AU (Manage + Grow) | 2 | Two products: Clio Manage (matters) + Clio Grow (intake). Grow is the natural Zoe target — new-matter creation. |
| **Smokeball** | Yes (partner API; trust-account aware) | Limited | None native | No | **Large AU** (legal practice mgmt) | 4 | AU-tailored, trust accounting compliance. API access via partner program. AI Assistant integration recently launched. |
| **Xero Practice Manager** | Yes (`developer.xero.com`) | Limited | via Xero Zapier (limited) | No | **Very Large AU** (silver+ Xero partners) | 3 | Same OAuth/auth as Xero. Free for Xero silver+ partners → very high accountant penetration in AU. |
| **FYI Docs** | Yes (Xero-pulling) | Limited | None native | No | Medium AU (Xero-heavy firms) | 3 | Document-management focus; uses XPM API key + MS365. Less suited for live booking. |
| **Karbon** | Yes (REST) | Yes | Native | No | Medium AU (growing) | 2 | Modern API, native Zapier. Strong for accountant lead-intake / new-client onboarding via Zoe. |

**AU prof-services verdict.** **Clio** + **Karbon** are the two cleanest builds (native Zapier, modern APIs). **Xero Practice Manager** has by far the largest AU accountant footprint but the API is lower-fidelity for live booking — better for capturing client/contact data than scheduling. **Smokeball** is the highest-revenue opportunity (large AU legal market) but partner-gated.

---

## Priority recommendation — first 8 integrations to build

Ranked by **AU SMB market share × ease of integration**. Build in this order; each one unlocks a defensible vertical for Metis Cortex.

| Rank | Platform | Vertical | Why first | Build effort |
|---|---|---|---|---|
| 1 | **ServiceM8** | Cleaning / trades | Massive AU SMB footprint, native Zapier + webhooks, Peter has insider knowledge via DSK. | 1-2 days |
| 2 | **Jobber** | Cleaning / trades | Premium Zapier native, modern GraphQL + HMAC webhooks, big NZ/AU base. | 1-2 days |
| 3 | **Cliniko** | Healthcare (allied) | Largest AU allied-health installed base. No webhooks → must poll, but doable. | 3-4 days |
| 4 | **Pabau** | Beauty + medi-aesthetic | Best-in-class API/webhook/Zapier; matches Eonia precedent → reuse work. | 1-2 days |
| 5 | **Mindbody** | Beauty / fitness / wellness | Gold-standard webhooks API + native Zapier. Reference architecture for the others. | 1-2 days |
| 6 | **VaultRE** | Real estate | Market leader AU/NZ, partner API, 380+ live integrations prove the model. | 2-3 days |
| 7 | **ResDiary** | Hospitality | Open partner API + webhooks; biggest AU restaurant footprint with usable docs. | 2-3 days |
| 8 | **Clio (Grow)** | Legal | Native Zapier, modern v4 API; new-matter intake is the perfect Zoe job. | 1-2 days |

**Skip / qualify-out at sales:**
- **Power Diary / Zanda** — no API, no webhooks
- **Tradify** — no public API
- **OpenTable** — affiliate gate is too slow (3-4 wk approval) for pilot agency stage
- **Best Practice (Bp Premier)** — FHIR via Halo Connect is enterprise-grade, not 1-10-client friendly

**Sales-call discovery items** (mark "Unverified" — confirm with prospect): NowBookIt, Mr Yum, Zenu, Eagle Software, Praktika, Nookal, Tock, AroFlo, Smokeball, FYI Docs.

---

## Architectural note for Peter

Across all 6 verticals, **none of these platforms have a native GoHighLevel integration**. That means for every customer, Zoe → GHL is the easy half; **GHL → vertical-platform is the integration we're actually selling**. Three patterns will cover ~80% of cases:

1. **Native Zapier path** (ServiceM8, Jobber, Mindbody, Clio, Pabau, Karbon) — fastest, but Zapier costs scale per-task. Use for low-volume customers.
2. **Webhook + Make.com / n8n path** (ResDiary, SevenRooms, Jobber, simPRO, VaultRE) — flat-rate hosting, scales better. Use for medium+ volume.
3. **Custom OAuth + REST polling** (Cliniko, Phorest, Halaxy, Smokeball, Bp Premier) — engineering build, only justified at higher MRR tiers.

Pricing should reflect pattern: Zapier-tier customers can be on the lower plan; webhook/n8n customers mid-tier; custom OAuth customers are premium-tier.

---

*Sources: SevenRooms api-docs.sevenrooms.com · NowBookIt nowbookit.com · ResDiary resdiary.com docs · OpenTable platform.opentable.com · Tock exploretock.com · Quandoo docs.quandoo.com · VaultRE docs.api.vaultre.com.au · Box+Dice websiteboxdiceapi.docs.apiary.io · Realhub api-docs.realhub.com.au · Inspect Real Estate inspectrealestate.com.au · Cliniko docs.api.cliniko.com · Halaxy support.halaxy.com · Best Practice haloconnect.io · Praktika praktika.com.au · Power Diary keragon.com/integrations/powerdiary · Nookal nookal.com · Genie docs.geniesolutions.io · Pabau pabau.com/integrations · Timely gettimely.com · Fresha fresha.com · Mindbody developers.mindbodyonline.com · Phorest developer.phorest.com · Jobber getjobber.com · ServiceM8 developer.servicem8.com · Tradify getapp.com · simPRO developer.simprogroup.com · Clio docs.developers.clio.com · Smokeball smokeball.com.au · Xero PM developer.xero.com · FYI fyi.app · Karbon karbonhq.com.*
