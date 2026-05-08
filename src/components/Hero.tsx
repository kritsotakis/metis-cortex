import { CTAButton } from "./CTAButton";
import { OFFER, PRICING, priceFormatAud } from "@/lib/site";

export function Hero() {
  return (
    <section className="relative overflow-hidden bg-ink text-bone">
      <header className="relative mx-auto flex max-w-6xl items-center justify-between px-6 pt-8 sm:px-10">
        <a
          href="#"
          aria-label="Metis Cortex"
          className="inline-flex items-center gap-4 text-bone transition-opacity hover:opacity-85"
        >
          <img
            src="/brand/metiscortex-mark-transparent.png"
            alt=""
            className="h-16 w-16"
          />
          <img
            src="/brand/metiscortex-wordmark-tight.svg"
            alt="Metis Cortex"
            className="h-14 w-auto"
          />
        </a>
        <nav
          aria-label="Primary"
          className="hidden items-center gap-7 text-sm uppercase tracking-[0.16em] text-bone/65 sm:flex"
        >
          <a href="#how-it-works" className="hover:text-bone">How it works</a>
          <a href="#pricing" className="hover:text-bone">Pricing</a>
          <a href="#guarantee" className="hover:text-bone">The guarantees</a>
        </nav>
      </header>

      <div className="relative mx-auto max-w-6xl px-6 pt-20 pb-28 sm:px-10 sm:pt-28 sm:pb-36">
        <p className="mb-6 inline-flex items-center gap-3 text-xs uppercase tracking-[0.22em] text-bone/55">
          <span className="h-px w-8 bg-bone/30" />
          {OFFER.name}
        </p>

        <h1 className="font-display text-[clamp(3.5rem,9vw,8.25rem)] font-semibold leading-[0.96] tracking-[0.02em] text-bone">
          <span className="mc-bronze-underline-hero">100% answered.</span>
          <br />
          <span className="mc-italic-display text-bone/85">
            Or your money back.
          </span>
        </h1>

        <p className="mt-10 max-w-2xl text-lg leading-relaxed text-bone/80 sm:text-xl">
          Stop missing calls. We install Zoe — your AI receptionist — on your
          existing number in {PRICING.installDays} days. She picks up every
          inbound within 60 seconds, qualifies the lead, books the appointment,
          and writes it into your calendar and CRM.
        </p>

        <p className="mt-6 max-w-2xl text-base leading-relaxed text-bone/65">
          {priceFormatAud(PRICING.setupAud)} setup +{" "}
          {priceFormatAud(PRICING.monthlyAud)}/mo standard.{" "}
          <span className="text-bone">
            Founding rate {priceFormatAud(PRICING.foundingMonthlyAud)}/mo
          </span>{" "}
          for the first {PRICING.foundingClientCap} case-study clients
          (cleaning, restaurant, real estate, dental, beauty — one slot per
          vertical).
        </p>

        <div className="mt-12 flex flex-wrap items-center gap-6">
          <CTAButton>Book a 15-min demo</CTAButton>
          <a
            href="#guarantee"
            className="text-sm uppercase tracking-[0.18em] text-bone/70 hover:text-bone"
          >
            See the guarantees
          </a>
        </div>

        <aside className="mt-16 max-w-2xl rounded-lg bg-bone/[0.04] backdrop-blur-sm p-5 sm:p-6">
          <div className="grid grid-cols-[60px_1fr_auto] items-center gap-5 py-2 text-sm">
            <span className="font-mono text-xs tracking-wider text-bone/45">
              19:04
            </span>
            <span className="text-bone/85">
              Inbound · 0412 ••• 311
            </span>
            <span className="text-[11px] uppercase tracking-[0.16em] text-bone/65">
              Answered · 4s
            </span>
          </div>
          <div className="grid grid-cols-[60px_1fr_auto] items-center gap-5 border-t border-bone/10 py-2 text-sm">
            <span className="font-mono text-xs tracking-wider text-bone/45">
              19:04
            </span>
            <span className="text-bone/85">
              Booked · Thu 7:30pm · table for 4, peanut allergy noted
            </span>
            <span className="text-[11px] uppercase tracking-[0.16em] text-bone/55">
              Confirmed
            </span>
          </div>
        </aside>

        <p className="mt-10 text-sm text-bone/55">
          Built and proven on DSK Property Cleaning — our own Sydney cleaning
          business. Founder ran Limani Seafood Restaurant in Narrabeen for 21
          years. Australian-owned.
        </p>
      </div>
    </section>
  );
}
