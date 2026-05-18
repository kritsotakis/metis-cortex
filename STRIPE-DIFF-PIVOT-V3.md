# Stripe Diff — Pivot v3

**Status:** Planning writeup. Nothing executed against Stripe yet. Peter reviews → greenlight → Code applies via Stripe API.
**Revised 2026-05-18 after Cowork partial review + Code's full convention cross-check** — see "Convention fixes applied" section at bottom for diff against v1 of this doc.
**Currency:** AUD (locked per Peter 2026-05-18 — Sydney trades + AU accountants are year-1 TAM). All `price.create` calls pass `currency: 'aud'` explicitly.
**Founding rate:** archived, not deleted (keeps closer-tool available for legacy outreach prospects).
**Brand convention** (per `~/.claude/memory/stripe-brand-convention.md`, Model B full-descriptor mode): every product tagged with full 5-key metadata schema:
```json
{
  "business": "metis_cortex",
  "brand": "Metis Cortex",
  "statement_descriptor_suffix": "METIS",
  "legal_entity": "Kritsotakis Family Trust",
  "abn": "45984876899"
}
```
Plus `tax_code: "txcd_10000000"` (General Services — matches account-wide convention; not over-engineering per-product tax codes).

---

## Existing state (as of 2026-05-09)

Stripe account: `acct_1Qi7qr2nwvvosadL` (shared trust account, all 5 businesses).

| Product | Product ID | Price | Price ID | Status |
|---|---|---|---|---|
| Setup Fee | `prod_UU7Xw8XuMlkD1W` | A$1,500 one-time | `price_1TV9Jo2nwvvosadLTkBGJXDj` | Active default |
| AI Receptionist (Zoe) — Standard | `prod_UU7XyC7hIX9jIu` | A$1,200/mo | `price_1TV9Jw2nwvvosadLXDCrFp1i` | Active default |
| AI Receptionist (Zoe) — Founding | (same product) | A$800/mo cap=5 | `price_1TV9K12nwvvosadLZcdlSFgC` | Active alt |

---

## Target state (after v3 pivot)

### Existing products — rename + reprice

**1. `prod_UU7Xw8XuMlkD1W` (Setup Fee)**

| Action | Detail |
|---|---|
| Rename | "AI Receptionist — Setup" (drop Trades Grand Slam tie — same product invoiced at A$1,500 legacy or A$5,000 v3, descriptor must be generic) |
| Keep `statement_descriptor` | `METIS SETUP` (matches convention line 79, unchanged from May 9 product creation) |
| Update `description` | "One-time install fee for AI Receptionist (Zoe). Includes voice agent setup, custom script tuning, calendar/CRM integration, and 30-day post-launch tuning window." |
| Add new price | A$5,000 one-time, **explicit `currency: 'aud'`**, label `receptionist-setup-aud-5000` |
| Set new default | the new A$5,000 price |
| Archive old price | `price_1TV9Jo2nwvvosadLTkBGJXDj` (A$1,500) — stays attached, available for grandfathered clients |

**2. `prod_UU7XyC7hIX9jIu` (AI Receptionist Zoe)**

| Action | Detail |
|---|---|
| Rename | "AI Receptionist — Monthly (Zoe)" |
| Keep `statement_descriptor` | `METIS RECEPTION` (matches convention line 79, unchanged from May 9 product creation) |
| Update `description` | "Monthly subscription for AI Receptionist (Zoe). Includes ~500 minutes of agent time + monitoring + monthly tuning call." |
| Add new price | A$1,500/mo recurring, **explicit `currency: 'aud'`**, label `receptionist-monthly-aud-1500` |
| Set new default | the new A$1,500/mo price |
| Archive old prices | `price_1TV9Jw2nwvvosadLXDCrFp1i` (A$1,200), `price_1TV9K12nwvvosadLZcdlSFgC` (A$800 founding) — both stay attached, available for legacy clients |

### New products — create

**3. AI Strategy & Audit**

| Field | Value |
|---|---|
| Name | "AI Strategy & Audit" |
| `statement_descriptor` | `METIS AUDIT` |
| `description` | "Two-week paid engagement: business shadowing, opportunity register, 90-day automation roadmap. PDF + 30-min Loom walkthrough delivered." |
| `metadata` | `business=metis_cortex`, `brand=Metis Cortex`, `statement_descriptor_suffix=METIS`, `legal_entity=Kritsotakis Family Trust`, `abn=45984876899`, `offer=ai_audit`, `tax_code=txcd_10000000` |
| Prices | A$2,000 (Lite), A$3,500 (Standard, **default**), A$5,000 (Deep) — all one-time, **explicit `currency: 'aud'`** |

**4. Workflow Automation — Setup**

| Field | Value |
|---|---|
| Name | "Workflow Automation — Setup" |
| `statement_descriptor` | `METIS WORKFLOW` (14 chars — matches convention pattern of plain brand-product descriptor; Stripe disambiguates Setup vs Monthly by product ID on invoices) |
| `description` | "One-time build fee for n8n/Make workflow automation. 1–5 workflows depending on tier." |
| `metadata` | `business=metis_cortex`, `brand=Metis Cortex`, `statement_descriptor_suffix=METIS`, `legal_entity=Kritsotakis Family Trust`, `abn=45984876899`, `offer=workflow_automation`, `tax_code=txcd_10000000` |
| Prices | A$3,000 (1 workflow), A$5,000 (2–3 workflows, **default**), A$10,000 (5+ workflows) — all one-time, **explicit `currency: 'aud'`** |

**5. Workflow Automation — Monthly**

| Field | Value |
|---|---|
| Name | "Workflow Automation — Monthly" |
| `statement_descriptor` | `METIS WORKFLOW` |
| `description` | "Monthly retainer for n8n/Make workflow hosting, monitoring, tweaks. Required for workflows built by Metis." |
| `metadata` | `business=metis_cortex`, `brand=Metis Cortex`, `statement_descriptor_suffix=METIS`, `legal_entity=Kritsotakis Family Trust`, `abn=45984876899`, `offer=workflow_automation`, `tax_code=txcd_10000000` |
| Prices | A$300/mo (Light), A$500/mo (Standard, **default**), A$1,000/mo (Heavy) — all recurring, **explicit `currency: 'aud'`** |

### Retrofit existing products — add missing metadata

The May 9 product creation only set 3 of the 5 convention-required metadata fields (`business`, `legal_entity`, `abn`). Add the missing 2 to both existing products as part of this diff execution:

| Product | Add to metadata |
|---|---|
| `prod_UU7Xw8XuMlkD1W` (Setup) | `brand: "Metis Cortex"`, `statement_descriptor_suffix: "METIS"` |
| `prod_UU7XyC7hIX9jIu` (Monthly) | `brand: "Metis Cortex"`, `statement_descriptor_suffix: "METIS"` |

Convention compliance: full 5-key schema across all 5 products after this diff lands.

### Held — do not build yet

These wait until first sale in each line, then we build the product at the agreed price.

- Website (Astro + Cloudflare) — A$5K / A$10K / A$15K setup + A$200–500/mo
- Marketing Automation — A$3K / A$5K / A$7K + A$500–1.5K/mo
- Custom AI Build — A$10K+ setup + variable monthly

Holding because: each is a 0-paying-client product line. Building Stripe SKUs ahead of demand creates premature catalogue complexity. We add them the moment a verbal yes lands at a defined price.

---

## Audit-to-build credit mechanics

Per `metis-ai-audit-offer.md`: 50% of audit fee credits toward any build over A$5K booked within 90 days.

**Implementation:** Stripe coupon, one per audit client, expires 90 days, applies to any Receptionist/Workflow invoice of A$5K+.

| Audit price | Credit | Coupon code pattern |
|---|---|---|
| A$2,000 (Lite) | A$1,000 off | `AUDIT-CREDIT-{CLIENT_SLUG}-1000` |
| A$3,500 (Standard) | A$1,750 off | `AUDIT-CREDIT-{CLIENT_SLUG}-1750` |
| A$5,000 (Deep) | A$2,500 off | `AUDIT-CREDIT-{CLIENT_SLUG}-2500` |

Coupons issued manually after audit signature; not auto-generated. Reason: forces a sales touchpoint when the audit closes — "here's your credit code, the next conversation is the build pitch."

---

## Refund reserve

Per `metis-trades-grand-slam.md`: hold 15% of every Grand Slam invoice in a separate guarantee reserve until 91 days post-install.

**Implementation:** not a Stripe feature — accounting only. Bookkeeping pattern:
- On every Grand Slam invoice (setup + monthly), transfer 15% to a separate Xero account `Metis Cortex — Guarantee Reserve` (liability account).
- Release to revenue at day 91 post-install if no claim filed.
- If claim filed, refund 2× the client's paid total from this account (with general account topping up the gap).

Code does not need to do anything for this — it's bookkeeping. Flagged here so it doesn't get forgotten.

---

## Migration plan for existing clients

There are no signed Metis Cortex clients today. No grandfathering required. All existing SKUs can be archived without notice.

If a legacy outreach prospect (Aaron / Stella / Helen / Brooke / Arthur) comes back and says yes to the old A$800 founding rate before the v3 pivot is announced, we can still close them on the legacy price — the archived `price_1TV9K12nwvvosadLZcdlSFgC` is still active for new subscriptions, it just isn't the default.

---

## Execution steps (Code, when greenlit)

1. Verify Stripe account access (use existing trust account `acct_1Qi7qr2nwvvosadL`).
2. Update `prod_UU7Xw8XuMlkD1W` per section 1 above. Add new price. Set new default. Archive old price.
3. Update `prod_UU7XyC7hIX9jIu` per section 2 above. Add new price. Set new default. Archive old prices.
4. Create AI Audit product + 3 prices per section 3. Set Standard as default.
5. Create Workflow Automation Setup product + 3 prices per section 4. Set Standard as default.
6. Create Workflow Automation Monthly product + 3 prices per section 5. Set Standard as default.
7. Update `src/lib/site.ts` `PRICING` constants to reflect new defaults (when new Astro repo is scaffolded — Code doesn't touch this until repo lands).
8. Confirm in STATUS.md Decision Log.

Total Stripe work: ~30 minutes API-side. No live customer impact (zero active subscriptions).

---

*Doc owner: Code. Created 2026-05-18 per pivot v3 greenlight. Awaiting Peter's "ship it" before any live Stripe changes.*

---

## Convention fixes applied (v1 → v2, 2026-05-18 later)

Cowork did a partial review of v1 of this doc (couldn't read `~/.claude/memory/stripe-brand-convention.md` — outside their scope). Code did the full cross-check against the convention and applied 6 fixes:

| # | v1 (original) | v2 (current) | Why |
|---|---|---|---|
| 1 | Setup descriptor: `METIS RECEPT SETUP` | `METIS SETUP` | Convention line 79 uses `METIS SETUP` for the Setup product since May 9; consistency. Setup product is generic (legacy A$1,500 + new A$5,000 both invoice from same product), so descriptor must not tie to Grand Slam. |
| 2 | Monthly descriptor: `METIS RECEPT` | `METIS RECEPTION` | Convention line 79 has `METIS RECEPTION` for the Receptionist product since May 9; using the existing live descriptor avoids accidental rename of in-flight charges. |
| 3 | Workflow Setup descriptor: `METIS WORKFLOW SETUP` | `METIS WORKFLOW` | Convention pattern is brand-product, not brand-product-flavour. Stripe disambiguates Setup vs Monthly by product ID on invoices; no need to bake distinction into descriptor. |
| 4 | New products' metadata: 5 keys (`business`, `legal_entity`, `abn`, `offer`, `tax_code`) | 7 keys (added `brand: "Metis Cortex"` + `statement_descriptor_suffix: "METIS"`) | Convention lines 35–48 require all 5 brands carry `brand` + `statement_descriptor_suffix` for Xero pass-through / forward-compat scenarios where suffix-mode is the only available path. |
| 5 | Setup product description tied to Trades Grand Slam | Generic "AI Receptionist setup" description | Same product invoices both legacy A$1,500 and new A$5,000. Description must reflect that, not be Grand-Slam-specific. |
| 6 | Currency implicit | Explicit `currency: 'aud'` on every `price.create` call | Convention line 79 says "AUD only" for Metis Cortex; pass explicitly so it's never inferred from account default. |

**Plus a new "Retrofit existing products" subsection** — the 2 May 9 products (`prod_UU7Xw8XuMlkD1W` Setup, `prod_UU7XyC7hIX9jIu` Monthly) were created with only 3 of 5 convention-required metadata keys. This diff execution adds the missing `brand` + `statement_descriptor_suffix` to both, bringing all 5 products into full convention compliance in one pass.

**Cowork's other concerns:**
- Tax code `txcd_20030000` (Professional/Consulting) vs `txcd_10000000` (General Services) for the Audit product → **stayed with General Services** per convention line 7 ("Tax code `txcd_10000000`" account-wide); both are 10% GST in AU, code differs only for cross-border tax classification.
- Price-level metadata (vs product-level) → **skipped**; convention doesn't require it, retrofit cheap if needed later.

Diff now convention-compliant. Ready for execution on Peter's `ship stripe diff` greenlight.
