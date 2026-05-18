# Stripe Dashboard Runbook — V3 Pivot Diff

**Goal:** Apply STRIPE-DIFF-PIVOT-V3.md (v2 with 6 convention fixes) to the shared trust Stripe account `acct_1Qi7qr2nwvvosadL` manually via the Stripe Dashboard. ~30 min total.

**Why manual:** Stripe MCP auth shimming hung; not worth more time debugging. Dashboard clicks are deterministic and zero customer impact (zero active subscriptions).

**Open dashboard:** https://dashboard.stripe.com/products
**Live mode only.** Make sure the toggle in the top-left is set to **Live**, not Test.

---

## Pre-flight check (60 seconds)

Before touching anything:

1. Top-left toggle reads **"Live mode"** (NOT "Test mode")
2. Top-right account selector reads **Kritsotakis Family Trust** (or just shows the account — only one account here)
3. Visit `https://dashboard.stripe.com/products` — you should see 3 products from May 9:
   - **Setup Fee** — A$1,500
   - **AI Receptionist (Zoe)** — A$1,200/mo (Standard) + A$800/mo (Founding)

If those 3 products are NOT visible, STOP — wrong account or wrong mode.

---

## Task 1 — Update existing Setup Fee product (~3 min)

Click on **Setup Fee** in the products list.

### 1a. Rename product
- Click the product name "Setup Fee" at the top → edit → change to: **`AI Receptionist — Setup`**
- Click **Save**

### 1b. Update description
- Find the **Description** field → replace with:
  > One-time install fee for AI Receptionist (Zoe). Includes voice agent setup, custom script tuning, calendar/CRM integration, and 30-day post-launch tuning window.
- Save

### 1c. Add missing metadata
- Scroll to **Metadata** section → click **Add metadata** → add these two rows:
  - Key: `brand` · Value: `Metis Cortex`
  - Key: `statement_descriptor_suffix` · Value: `METIS`
- Existing metadata (`business=metis_cortex`, `legal_entity=Kritsotakis Family Trust`, `abn=45984876899`) stays as-is
- Save

### 1d. Add new A$5,000 price
- Find the **Pricing** section (lower on the page)
- Click **+ Add another price**
- Configure:
  - Pricing model: **One-time**
  - Amount: **5000.00** AUD
  - (No tax — Stripe Tax handles inclusive/exclusive at checkout per account settings)
- Save

### 1e. Set A$5,000 as default
- Find the new A$5,000 price in the list → click the **⋯ menu** on the right → **Make default**

### 1f. Archive the old A$1,500 price (keep accessible)
- Find the old A$1,500 price → click **⋯ menu** → **Archive price**
- Confirms it's removed from default checkout but stays attached to the product for legacy clients

### 1g. Verify statement descriptor stays as `METIS SETUP`
- Find **Statement descriptor** field — should still read `METIS SETUP` (no change needed)
- If it shows something different, edit to `METIS SETUP` and save

✅ Task 1 done.

---

## Task 2 — Update existing AI Receptionist (Zoe) product (~3 min)

Go back to **Products** → click **AI Receptionist (Zoe)**

### 2a. Rename product
- Change product name to: **`AI Receptionist — Monthly (Zoe)`**
- Save

### 2b. Add missing metadata
- Add the same 2 metadata rows:
  - `brand` · `Metis Cortex`
  - `statement_descriptor_suffix` · `METIS`
- Save

### 2c. Add new A$1,500/mo price
- **+ Add another price**
- Configure:
  - Pricing model: **Recurring**
  - Billing period: **Monthly**
  - Amount: **1500.00** AUD
- Save

### 2d. Set A$1,500/mo as default
- New price → **⋯ menu** → **Make default**

### 2e. Archive the old A$1,200/mo Standard price
- Old A$1,200/mo → **⋯ menu** → **Archive price**

### 2f. Archive the old A$800/mo Founding price
- A$800/mo Founding → **⋯ menu** → **Archive price**
- (Both archived prices stay attached and can still be used for legacy/grandfathered clients — just not default checkout)

### 2g. Verify statement descriptor stays as `METIS RECEPTION`
- Should read `METIS RECEPTION` (no change needed; was set May 9)

✅ Task 2 done.

---

## Task 3 — Create new AI Strategy & Audit product (~6 min)

Click **Products** → top-right **+ Add product**

### 3a. Product details
- Name: **`AI Strategy & Audit`**
- Description:
  > Two-week paid engagement: business shadowing, opportunity register, 90-day automation roadmap. PDF + 30-min Loom walkthrough delivered.
- Image: skip
- Tax code: **General — Services** (or `txcd_10000000` if Stripe lets you paste a code)
- Statement descriptor: **`METIS AUDIT`**

### 3b. Pricing — create 3 one-time prices

**Price 1 — Lite:**
- Pricing model: **One-time**
- Amount: **2000.00** AUD
- Save

After product is created, click into it again and **+ Add another price**:

**Price 2 — Standard (set this as default):**
- Pricing model: **One-time**
- Amount: **3500.00** AUD
- Save
- Then **⋯ menu** on the A$3,500 price → **Make default**

**Price 3 — Deep:**
- Pricing model: **One-time**
- Amount: **5000.00** AUD
- Save

### 3c. Add metadata (full 5-key schema + 1 offer-specific)
- Scroll to Metadata → add 6 rows:
  - `business` · `metis_cortex`
  - `brand` · `Metis Cortex`
  - `statement_descriptor_suffix` · `METIS`
  - `legal_entity` · `Kritsotakis Family Trust`
  - `abn` · `45984876899`
  - `offer` · `ai_audit`
- Save

✅ Task 3 done.

---

## Task 4 — Create new Workflow Automation Setup product (~5 min)

**Products** → **+ Add product**

### 4a. Product details
- Name: **`Workflow Automation — Setup`**
- Description:
  > One-time build fee for n8n/Make workflow automation. 1–5 workflows depending on tier.
- Tax code: **General — Services**
- Statement descriptor: **`METIS WORKFLOW`**

### 4b. Pricing — 3 one-time prices
- A$3,000 one-time (1 workflow)
- A$5,000 one-time (2–3 workflows) → **Make default**
- A$10,000 one-time (5+ workflows)

### 4c. Metadata (6 rows, same pattern)
- `business` · `metis_cortex`
- `brand` · `Metis Cortex`
- `statement_descriptor_suffix` · `METIS`
- `legal_entity` · `Kritsotakis Family Trust`
- `abn` · `45984876899`
- `offer` · `workflow_automation`

✅ Task 4 done.

---

## Task 5 — Create new Workflow Automation Monthly product (~5 min)

**Products** → **+ Add product**

### 5a. Product details
- Name: **`Workflow Automation — Monthly`**
- Description:
  > Monthly retainer for n8n/Make workflow hosting, monitoring, tweaks. Required for workflows built by Metis.
- Tax code: **General — Services**
- Statement descriptor: **`METIS WORKFLOW`** (same as Setup product — Stripe disambiguates by product ID on invoices)

### 5b. Pricing — 3 recurring monthly prices
- A$300/mo recurring (Light)
- A$500/mo recurring (Standard) → **Make default**
- A$1,000/mo recurring (Heavy)

### 5c. Metadata (same 6 rows as Task 4)

✅ Task 5 done.

---

## Post-flight verification (2 min)

Open https://dashboard.stripe.com/products in a fresh tab. You should see **5 products total**:

| # | Product | Default price | Other prices |
|---|---|---|---|
| 1 | AI Receptionist — Setup | A$5,000 one-time | A$1,500 archived |
| 2 | AI Receptionist — Monthly (Zoe) | A$1,500/mo | A$1,200/mo archived · A$800/mo archived |
| 3 | AI Strategy & Audit | A$3,500 one-time | A$2,000 + A$5,000 |
| 4 | Workflow Automation — Setup | A$5,000 one-time | A$3,000 + A$10,000 |
| 5 | Workflow Automation — Monthly | A$500/mo | A$300/mo + A$1,000/mo |

**Quick checks on each:**
- Click each product → scroll to Metadata → confirm 5 keys present: `business`, `brand`, `statement_descriptor_suffix`, `legal_entity`, `abn` (plus `offer` on the 3 new products)
- Confirm statement descriptors: `METIS SETUP`, `METIS RECEPTION`, `METIS AUDIT`, `METIS WORKFLOW` × 2
- Confirm archived prices still appear in the list (greyed out / labeled "Archived"), proving legacy paths preserved

---

## After completion

Send Code a one-line confirmation: **`stripe diff applied`** — Code will:
1. Update STATUS.md (move Stripe row from In Flight → Done This Sprint)
2. Update PAIR.md log entry for Cowork visibility
3. Mirror STATUS to memory

That closes the v3 pivot Stripe workstream. Remaining v3 items waiting: accountant call (tomorrow), `.ai` domain (next week, optional defensive).

---

## If anything looks off

Common pitfalls:

- **Forgot to set new default price** → product page shows old price as primary. Fix: click new price ⋯ → Make default.
- **Archived too aggressively** → if you accidentally archive a NEW price before setting it as default, just unarchive it (⋯ menu has Unarchive).
- **Metadata typo** → keys are case-sensitive. `business` not `Business`. `statement_descriptor_suffix` not `Statement_Descriptor_Suffix`.
- **Tax code missing** → leave as default if the picker doesn't have "General — Services" exactly. Stripe Tax handles AU GST account-wide regardless.

**Roll-forward principle:** none of these can damage live customers since there are zero active subscriptions. If something looks wrong, fix forward — don't try to revert.

---

*Doc owner: Code. Created 2026-05-19 as a fallback for MCP auth issues. Equivalent to STRIPE-DIFF-PIVOT-V3.md v2 in execution outcome.*
