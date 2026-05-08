# Metis Cortex — Launch Site

One-page launch site for **Metis Cortex**, the Speed-to-Lead AI receptionist.

- Stack: Next.js 16 (App Router) · React 19 · Tailwind CSS v4 · TypeScript
- Hosting target: Vercel free tier
- Primary domain: `metiscortex.au`

## Local development

```bash
npm install
npm run dev
```

Then open http://localhost:3000.

## Wiring before launch

Search and replace these placeholders before going live:

| Placeholder | Where | Replace with |
|---|---|---|
| `https://calendly.com/peter-kritsotakis/metis-cortex-demo` | `src/components/CTAButton.tsx` | Real Calendly link |
| `ASIC business name registration pending` | `src/components/Footer.tsx` | ASIC business name registration number once issued |
| Pilot stat dashes (`—`) | `src/components/DSKCaseStudy.tsx` | Real DSK 14-day pilot numbers |
| LinkedIn URL | `src/components/Footer.tsx` | Confirm slug |

## Deploy to Vercel (free tier)

1. Push to GitHub: `gh repo create metis-cortex --private --source . --remote origin --push`
2. Import the repo at vercel.com/new — it auto-detects Next.js, no config needed
3. In Vercel → Project → Settings → Domains, add `metiscortex.au`
4. Vercel gives you the DNS records to set. In GoDaddy DNS for `metiscortex.au`:
   - **A** record on `@` → `76.76.21.21`
   - **CNAME** on `www` → `cname.vercel-dns.com`
5. HTTPS provisions automatically within ~10 min
6. No env vars required for v1

**Hosting cost:** $0 on Vercel free tier (100 GB bandwidth/month, way more than this site needs).

Static rendering, edge-rendered OG image, no client-side JS beyond the native `<details>` accordion. Lighthouse target 95+ on all four axes.

## Structure

```
src/
├── app/
│   ├── layout.tsx           ← fonts, metadata, JSON-LD
│   ├── page.tsx             ← composes the 9 sections
│   ├── globals.css          ← Tailwind v4 theme tokens
│   ├── opengraph-image.tsx  ← edge-rendered OG (1200×630)
│   ├── twitter-image.tsx    ← re-exports OG
│   ├── sitemap.ts
│   └── robots.ts
└── components/
    ├── Hero.tsx
    ├── CostOfMissedCalls.tsx
    ├── WhatsIncluded.tsx
    ├── DSKCaseStudy.tsx
    ├── HowItWorks.tsx
    ├── Guarantee.tsx
    ├── FAQ.tsx
    ├── ClosingCTA.tsx
    ├── Footer.tsx
    └── CTAButton.tsx
```

## Brand tokens

Defined as CSS custom properties in `src/app/globals.css`:

- `bg-ink` / `text-ink` — deep navy `#0e1e2e`
- `bg-bone` / `text-bone` — bone white `#f5f1ea`
- `bg-gold` / `text-gold` — oxidised bronze `#b07843`
- `font-display` — Cormorant Garamond (H1 + section headings)
- Default body — Inter

## What's NOT in v1 (deferred per brief)

- About page / Greek mythology storytelling
- Reception or Handbook SKUs
- Vertical landing pages
- Blog, customer login, dashboard, pricing tiers

These return in Phase 2 (after 5 paying clients) and Phase 3 (after 20).
