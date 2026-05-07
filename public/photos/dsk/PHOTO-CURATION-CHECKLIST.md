# DSK Photo Curation Checklist

> **For:** Peter, to dig through DSK Jobber attachments + iPhone Photos and surface candidates
> **Author:** Cowork, executing Task 4 of `COWORK-INFRASTRUCTURE-SETUP.md`
> **Synced into repo:** Claude Code, 2026-05-06
> **Drop candidates here:** `~/Desktop/metis-cortex/public/photos/dsk/`
> **Final picked photos move to:** `~/Desktop/metis-cortex/public/photos/dsk/final/`

---

## Why we're doing this

The Metis Cortex site looks much stronger with real DSK photos than with stock or AI-generated imagery. Authenticity converts; stock photography signals "another agency." You have ~20K Jobber records and a personal photo library — the right photos exist, we just need to find them.

## What I need from you (~30 min)

Dig through:
- **Jobber attachments** — filter recent jobs (last 12 months), look at "before/after" attachments and worksite photos
- **iPhone Photos** — search for terms: DSK, cleaning, van, Mosman, Bondi, strata, pre-sale, end-of-lease
- **Any team WhatsApp groups** where the cleaners post job photos
- **Your camera roll** if you've taken site photos personally

Drop candidates into this folder: `~/Desktop/metis-cortex/public/photos/dsk/`

Naming convention as you save them:
- `01-hero-candidate-1.jpg`, `01-hero-candidate-2.jpg` ... — Hero background candidates (wide shots)
- `02-casestudy-candidate-1.jpg`, etc. — DSK case study primary photos
- `03-equipment-candidate-1.jpg`, etc. — Decorative shots of vans, gear, team
- `04-founder-candidate-1.jpg`, etc. — You at a worksite (Phase 2)
- `05-second-property-candidate-1.jpg`, etc. — Optional second case study slot

Aim for **8–12 candidates total** across all five slots. I'll triage down to **5 final picks** (one per slot).

## What I'm looking for in each slot

| Slot | Use | Specs | What makes a winner |
|---|---|---|---|
| **1. Hero background** | Sits behind the navy gradient on the homepage hero, very subtle | Wide horizontal, **2400×1200 minimum** | Cleaner mid-job at a Sydney property exterior. Ideally with a DSK van visible. Wide enough that it survives a heavy navy overlay. The composition should leave the right two-thirds clear (text sits there). |
| **2. DSK case study primary** | Anchor photo for the case study strip | Square or 4:3, **1600×1200 minimum** | The DSK team standing in front of a finished property. Or a striking before/after pair (if before/after, both shots should be from the same angle). Property looks polished, team looks competent. |
| **3. Decorative — equipment / van / team** | Small accent images in "What's Included" or footer | Any aspect, **1200×900 minimum** | Real DSK gear, branded van, team in DSK uniform. Doesn't have to be a hero composition — just professional. |
| **4. Founder strip (Phase 2)** | "About" page, post-launch | Wide, **2000×1100 minimum** | You at a DSK job site. Candid, not posed. You wearing whatever you wear when you actually work. Something that says "I run this" not "I had a headshot taken." |
| **5. Second case study (optional)** | Different property type for visual variety | 4:3, **1600×1200 minimum** | A different property type from slot 2 — if slot 2 is residential pre-sale, slot 5 could be a strata building exterior or an end-of-lease unit |

## Hard filtering rules — don't even submit a photo that breaks these

- ❌ **No customer faces.** Privacy. If a customer is in frame, it's out — don't submit and don't try to mask them yourself, just skip the photo.
- ❌ **No license plate close-ups** of the DSK van or any other vehicle. Privacy + legal.
- ❌ **No identifiable interior shots of luxury homes.** Security risk for the customer. Exterior shots of houses are fine; their letterbox or street number close-ups are not.
- ❌ **No low-resolution photos.** Minimum 1600px on the long edge. If it looks like a thumbnail, skip it.
- ❌ **Nothing blurry.** "Action shot of cleaner in motion" with motion blur on the cleaner is fine; out-of-focus shots are not.
- ❌ **Nothing older than 12 months.** DSK branding evolves; use current-era photos only.
- ❌ **No JPEG artefacts visible at fit-screen size.** If the file's been compressed too many times, skip it.
- ❌ **No filters / heavy edits.** No Instagram filters, no AI enhancements, no over-saturation. Natural-looking only.

## Soft preferences — picks that score higher

- ✅ Sydney landmarks / neighbourhoods visible in background — adds local credibility
- ✅ DSK van in shot (without licence plates close-up)
- ✅ Team in matching DSK uniform
- ✅ Natural daylight — beats fluorescent indoor every time
- ✅ Australian-coded settings (eucalypts, blue sky, Sydney sandstone, etc. — anything that reads as not-American)
- ✅ Action over posed — cleaner mid-mop > cleaner standing with broom

## What Cowork does after you drop the candidates

Once you've added 8–12 candidate files to the folder:

1. Inspect each one against the filtering rules and the slot-specific specs
2. Pick **the top 1 per slot** (5 final photos)
3. Move the picked files to `public/photos/dsk/final/` with renamed canonical files:
   - `hero-bg.jpg`
   - `casestudy-primary.jpg`
   - `equipment-decorative.jpg`
   - `founder-worksite.jpg`
   - `casestudy-secondary.jpg`
4. Run them through `pngquant` / `imagemin` to optimise file sizes (typically 30–60% reduction with no visible quality loss)
5. Generate accessible alt text for each — one specific descriptive sentence per photo, saved in `public/photos/dsk/final/alts.json`:
   ```json
   {
     "hero-bg.jpg": "DSK team finishing a pre-sale clean at a Mosman home, late afternoon light",
     "casestudy-primary.jpg": "DSK technician completing a deep clean on a Bondi unit's kitchen",
     ...
   }
   ```
6. Tell Code which paths to wire into the Hero, CaseStudy, and decorative components
7. The remaining 3–7 unused candidates stay in the parent `public/photos/dsk/` directory marked as "future use" — useful for blog posts, vertical landing pages in Phase 3, etc.

## What this unblocks

This isn't critical-path for site launch — the site can ship with placeholder photos and we swap them in later. But the case study strip + hero look 10x more credible with real DSK photos before the first cold-email batch goes out, so the right time to do this is **after Cloudflare migration is live and before the first 50 cold emails go**.
