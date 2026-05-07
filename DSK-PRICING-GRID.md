# DSK Pricing Grid — for Zoe (Retell agent)

> **For:** the Retell voice agent prompt + knowledge base, and Peter as a single source of truth
> **Author:** Cowork, executing Task 13 of the 2026-05-06 brief
> **Sources:** dsk.au/pre-sale-cleaning, dsk.au/end-of-lease, dsk.au/strata-maintenance, dsk.au/offers, dsk.au home, dsk.au/mothers-day-999 (excluded — promotional)
> **Eventual home:** `~/Desktop/metis-cortex/DSK-PRICING-GRID.md`
> **Status:** Draft v1 — needs Peter to confirm the inconsistencies flagged at the bottom before this becomes the source of truth Zoe quotes from.

---

## ⚠️ Inconsistencies for Peter to resolve before Zoe ships

These need a yes/no from Peter before the prompt is finalised:

1. **Pre-sale schema.org JSON-LD price = $890** but the visible site copy says "From $2,500 interior + exterior / From $1,650 exterior only." The $890 is almost certainly stale metadata. Either remove it from the page's JSON-LD (preferred) or update it to $1,650 to match the visible exterior-only entry price. Right now Google may be indexing $890 as the headline rich-snippet price — that hurts conversion.
2. **Builders Clean page returns 404** at `dsk.au/builders-clean/`. Is "builders clean" still a service or folded into pre-sale? If still a service, what's the price? If folded in, Zoe shouldn't reference it as a separate offering.
3. **Suburb pricing modifier** — the visible site says "Fixed quotes within 24 hours" with no suburb tier visible publicly. Confirm: does DSK actually charge differently for Mosman vs Newtown vs Bondi, or is it a flat-rate-by-property-size model with the visit cost effectively the same? **Default assumption in this grid: no suburb modifier; quotes are property-size-driven.** Override if wrong.
4. **Strata schema.org JSON-LD has no `offers` block** with pricing. The visible page lists tiered weekly/monthly pricing. Update the schema for SEO consistency.

---

## Service × Property Size — full grid

### 1. Pre-Sale Cleaning (interior + exterior)

| Property size | Interior + exterior price | Exterior only price | Notes |
|---|---|---|---|
| 1-bed unit | Quoted individually | Quoted individually | Below standard 3-bed minimum — call out for custom quote |
| 2-bed unit | Quoted individually | Quoted individually | Below standard 3-bed — custom quote |
| 3-bed home (standard) | **From $2,500** | **From $1,650** | DSK's published "standard" benchmark |
| 4-bed home | From $2,500 — quoted individually for size | From $1,650 — quoted individually | Larger than standard, expect upward adjustment |
| 5+ bed home | Quoted individually | Quoted individually | Custom quote always |
| Townhouse | Quoted individually | Quoted individually | Custom quote |

**Turnaround:** 48 hours from booking to clean
**Quote:** fixed price emailed within 24 hours of enquiry
**Coverage:** Northern Beaches, North Shore, Eastern Suburbs

---

### 2. End of Lease Cleaning (bond-back guarantee)

| Property type | Price |
|---|---|
| Apartment / unit | **From $440** |
| House | **From $660** |

**Bond-back guarantee:** if the property manager flags issues during inspection, DSK returns and cleans the flagged areas at no cost. Tenant must notify DSK within 24 hours of inspection.

**Note on size scaling:** end-of-lease pricing scales with the property — $440 / $660 are floor prices. A 4-bed house will be quoted higher than a 3-bed.

---

### 3. Strata Cleaning & Maintenance

| Building tier | Unit count | Per weekly visit | Per month indicative |
|---|---|---|---|
| **Small** | Up to 20 units | From $350 | ~$1,400 |
| **Medium** | 21–60 units | From $650 | ~$2,600 |
| **Large / Portfolio** | 60+ units | Custom quote | Volume discounts available |

**Service agreement structure:**
- Standard 12-month service agreement with locked monthly pricing
- Annual CPI-linked review at renewal
- Transparent variation process for one-off works
- 60-day termination-for-cause clause
- Optional 24-month agreement with 5% rate hold (no annual CPI uplift)
- Includes written reports

---

### 4. Add-Ons (any service)

| Add-on | Price |
|---|---|
| Oven deep clean | **+$80** |
| Carpet steam clean | **+$120** |
| Window cleaning (exterior) | **+$150** |
| Gutter clear | **+$180** |
| Pressure wash driveway | **+$250** |

---

### 5. Suburb Modifier

**Default policy: no suburb modifier.** DSK quotes by property size + service type. The pricing above applies across all served suburbs in:
- Northern Beaches
- North Shore
- Eastern Suburbs

> If Peter confirms a suburb modifier exists, replace this section with the actual rules. Until confirmed, Zoe quotes flat-rate by property-size + service-type.

---

### 6. Excluded — promotional pricing (DO NOT QUOTE)

The Mother's Day "Full External House Clean" pricing — $999 single storey / $1,299 double storey / $1,499 triple storey — **expires 11 May 2026**. After that date:
- Bookings close Sat 9 May 2026 OR at 15 homes (whichever first)
- Zoe must NEVER quote these prices for new enquiries received after 9 May
- If a caller asks specifically about the Mother's Day deal post-9-May, Zoe responds: *"That special's wrapped up for this year. Happy to quote you the standard exterior clean — Peter will email a fixed price within 24 hours."*

---

## What Zoe should NEVER quote (escalate to Peter)

Hard rules in the agent prompt:

| Scenario | Zoe response |
|---|---|
| **Post-fire / post-flood / post-water-damage clean** | "That's a specialised job. I'll flag it with Peter directly — he'll call you within 2 hours." |
| **Hoarding situations** | "We do handle these, but they need a personal walkthrough. Peter will call you back within 2 hours to scope it." |
| **Biohazard / crime-scene / deceased estate post-trauma** | "We don't quote these on the phone. Peter will call you back within 2 hours." |
| **Same-day service (within 4 hours of call)** | "Let me check with Peter — same-day jobs need his approval. He'll call you in the next 30 minutes." |
| **Booking value exceeds $5,000** | "Quotes over $5,000 go through Peter directly. He'll call you back within 2 hours with a fixed price." |
| **Caller is outside the service area** (anything south of the harbour bridge except Eastern Suburbs, anything west of Inner West, etc.) | "We're focused on the Northern Beaches, North Shore, and Eastern Suburbs. Happy to recommend a trusted operator in your area — let me grab Peter to call you back with a name." |
| **Strata building manager wants a quote on the spot** | "Strata quotes need a free site inspection — that's how we lock the right number. Let me get one in your diary this week." |
| **Caller asks for a price below floor pricing** ("can you do a 4-bed for $1,500?") | "Our pricing is fixed and reflects what it actually costs to do the work properly. I can't go below the published rates, but Peter can talk you through what's included if you'd like to chat with him." |

---

## Retell-prompt-ready YAML block

Drop this into the agent's knowledge base or system prompt:

```yaml
dsk_pricing:
  service_area:
    - Northern Beaches
    - North Shore
    - Eastern Suburbs

  contact:
    phone: "0423 668 766"
    business_name: "DSK Property Cleaning"
    insurance: "$20M public liability"
    police_checked: true
    directly_employed_team: true

  pre_sale_cleaning:
    standard_3_bed_interior_exterior: 2500
    standard_3_bed_exterior_only: 1650
    smaller_or_larger: "quoted individually"
    turnaround_hours: 48
    quote_response_hours: 24

  end_of_lease:
    apartment_unit_from: 440
    house_from: 660
    bond_back_guarantee: true
    bond_back_notification_window_hours: 24

  strata:
    small_building:
      units: "up to 20"
      weekly_visit_from: 350
      monthly_indicative: 1400
    medium_building:
      units: "21-60"
      weekly_visit_from: 650
      monthly_indicative: 2600
    large_portfolio:
      units: "60+"
      pricing: "custom_quote"
    agreement_term_months: 12
    annual_cpi_review: true
    termination_for_cause_days: 60
    extended_24_month_rate_hold_pct: 5

  addons:
    oven_deep_clean: 80
    carpet_steam_clean: 120
    window_cleaning_exterior: 150
    gutter_clear: 180
    pressure_wash_driveway: 250

  do_not_quote_escalate_to_peter:
    - post_fire_water_damage
    - hoarding
    - biohazard_crime_scene_deceased_estate
    - same_day_within_4_hours
    - booking_value_over_5000
    - outside_service_area
    - strata_on_the_spot_quote
    - below_floor_pricing
    - mothers_day_pricing_post_11_may_2026

  promotional_pricing_excluded_after_2026_05_11:
    name: "Mother's Day Special — Full External House Clean"
    single_storey: 999
    double_storey: 1299
    triple_storey: 1499
    valid_until: "2026-05-11"
    booking_closes: "2026-05-09 OR 15 bookings"
```

---

## Retell-prompt-ready JSON block

Same data, JSON form, for direct paste into Retell's system prompt JSON variables:

```json
{
  "dsk_pricing": {
    "service_area": ["Northern Beaches", "North Shore", "Eastern Suburbs"],
    "contact": {
      "phone": "0423 668 766",
      "business_name": "DSK Property Cleaning",
      "insurance": "$20M public liability",
      "police_checked": true,
      "directly_employed_team": true
    },
    "pre_sale_cleaning": {
      "standard_3_bed_interior_exterior": 2500,
      "standard_3_bed_exterior_only": 1650,
      "smaller_or_larger": "quoted individually",
      "turnaround_hours": 48,
      "quote_response_hours": 24
    },
    "end_of_lease": {
      "apartment_unit_from": 440,
      "house_from": 660,
      "bond_back_guarantee": true,
      "bond_back_notification_window_hours": 24
    },
    "strata": {
      "small_building": {
        "units": "up to 20",
        "weekly_visit_from": 350,
        "monthly_indicative": 1400
      },
      "medium_building": {
        "units": "21-60",
        "weekly_visit_from": 650,
        "monthly_indicative": 2600
      },
      "large_portfolio": {
        "units": "60+",
        "pricing": "custom_quote"
      },
      "agreement_term_months": 12,
      "annual_cpi_review": true,
      "termination_for_cause_days": 60,
      "extended_24_month_rate_hold_pct": 5
    },
    "addons": {
      "oven_deep_clean": 80,
      "carpet_steam_clean": 120,
      "window_cleaning_exterior": 150,
      "gutter_clear": 180,
      "pressure_wash_driveway": 250
    }
  }
}
```

---

## Sample Zoe responses (for the prompt's few-shot examples)

```
Caller: "How much for a pre-sale clean on a 3-bedroom house in Mosman?"
Zoe: "For a standard 3-bedroom home, our pre-sale clean is from $2,500
     for interior plus exterior, or from $1,650 if you only need the
     exterior. Peter will email a fixed price within 24 hours once we
     know a couple of details — would you like me to set that up now?"

Caller: "And if I want the oven cleaned too?"
Zoe: "Easy — that's an $80 add-on. I'll note it on the quote so it's
     included from the start."

Caller: "I've got a 5-bedroom house in Vaucluse, what's that going to run?"
Zoe: "For larger homes we quote individually rather than the standard
     rate, so I'll capture the details and Peter will email you a fixed
     price within 24 hours. Address and a couple of property details
     and we're set."

Caller: "What about an end-of-lease clean for a 2-bedroom apartment?"
Zoe: "End-of-lease pricing for apartments starts at $440 with our
     bond-back guarantee — if the property manager flags anything during
     inspection, we come back and re-clean those areas at no cost.
     Peter will confirm the fixed price within 24 hours."

Caller: "We're a 35-unit strata block in Bondi Junction looking at
        weekly cleaning."
Zoe: "Perfect — that's our medium-building tier, weekly visits from
     $650, around $2,600 a month. We'd want to do a free site
     inspection first to lock the exact number, and the standard
     agreement is 12 months with annual CPI review. When suits for
     the inspection?"

Caller: "I had a flood in my kitchen last night, can you clean it tomorrow?"
Zoe: "Post-water-damage cleans need Peter to scope directly — too many
     variables to quote on the phone. Let me grab your address and
     phone, he'll call you back within 2 hours."

Caller: "Will you do a 4-bed pre-sale for $1,500?"
Zoe: "Our pricing is fixed and reflects what it actually costs to do
     the work to the standard your agent will expect. I can't go below
     the published rate. Peter's happy to walk you through what's
     included if you'd like to chat with him directly."
```

---

## What NOT to put in Zoe's prompt

- ❌ The promotional Mother's Day pricing (expires 9 May)
- ❌ Specific suburb-by-suburb pricing (no public confirmation that suburbs differ)
- ❌ The schema.org $890 figure (it's stale metadata, not a real price)
- ❌ Builders Clean specifics (page is 404 — confirm with Peter if still offered)
- ❌ Any rate that isn't on this grid — when in doubt, escalate to Peter

---

## Cowork done

Grid extracted from public DSK pages, cross-checked across 5 source pages, structured for both human reference and machine prompt-injection. Inconsistencies flagged for Peter to resolve before the agent ships. Once Peter answers the four bullet points at the top, this becomes Zoe's pricing source of truth — and updates flow into the Retell knowledge base block.

Sources:
- [dsk.au — pre-sale cleaning](https://dsk.au/pre-sale-cleaning/)
- [dsk.au — end of lease](https://dsk.au/end-of-lease/)
- [dsk.au — strata maintenance](https://dsk.au/strata-maintenance/)
- [dsk.au — offers](https://dsk.au/offers/)
- [dsk.au — Mother's Day special (promotional, excluded)](https://dsk.au/mothers-day-999/)
