import { CTAButton } from "./CTAButton";
import { CONTACT } from "@/lib/site";

export function Hero() {
  return (
    <section className="relative overflow-hidden bg-ink text-bone">
      <header className="relative mx-auto flex max-w-6xl items-center justify-between px-6 pt-8 sm:px-10">
        <a
          href="#"
          aria-label="Metis Cortex"
          className="inline-flex items-center gap-3 text-bone transition-opacity hover:opacity-85"
        >
          <img
            src="/brand/metiscortex-mark.png"
            alt=""
            className="h-16 w-16"
          />
          <img
            src="/brand/metiscortex-wordmark-tight.svg"
            alt="Metis Cortex"
            className="h-10 w-auto"
          />
        </a>
        <nav
          aria-label="Primary"
          className="hidden items-center gap-7 text-sm uppercase tracking-[0.16em] text-bone/65 sm:flex"
        >
          <a href="#how-it-works" className="hover:text-bone">How we work</a>
          <a href="#services" className="hover:text-bone">What we build</a>
          <a href="#about" className="hover:text-bone">About</a>
        </nav>
      </header>

      <div className="relative mx-auto max-w-6xl px-6 pt-20 pb-28 sm:px-10 sm:pt-28 sm:pb-36">
        <p className="mb-6 inline-flex items-center gap-3 text-xs uppercase tracking-[0.22em] text-bone/55">
          <span className="h-px w-8 bg-bone/30" />
          Sydney AI agency — built by a 30-year operator
        </p>

        <h1 className="font-display text-[clamp(2.75rem,6.5vw,6rem)] font-semibold leading-[0.98] tracking-[0.02em] text-bone">
          We&rsquo;re using this on{" "}
          <span className="mc-bronze-underline-hero">our own</span> businesses
          first.
          <br />
          <span className="mc-italic-display text-bone/85">
            Then we build it for yours.
          </span>
        </h1>

        <p className="mt-10 max-w-2xl text-lg leading-relaxed text-bone/80 sm:text-xl">
          I&rsquo;m Peter. Six years building enterprise IT (MCSE / Cisco /
          Citrix), 21 years running Limani Seafood in Narrabeen, now building
          four service businesses of my own. Every system we sell — AI
          receptionists, workflow automation, operational audits — is running on
          one of those four first.{" "}
          <span className="text-bone">
            By the time it lands in yours, the bugs are out.
          </span>
        </p>

        <div className="mt-12 flex flex-wrap items-center gap-6">
          <CTAButton accent="none">Book a 15-min operator call</CTAButton>
          <a
            href="#services"
            className="text-sm uppercase tracking-[0.18em] text-bone/70 hover:text-bone"
          >
            See what we build →
          </a>
        </div>

        <p className="mt-6">
          <a
            href="/audit-checklist"
            className="inline-flex items-center gap-2 text-base text-bone/70 underline-offset-4 hover:text-bone hover:underline"
          >
            Or grab the 7-question operations audit checklist ↓
          </a>
        </p>

        <p className="mt-10 text-sm italic leading-relaxed text-bone/60">
          &ldquo;We build the AI we wish we&rsquo;d had at the
          restaurant.&rdquo;
        </p>

        <p className="mt-10 text-xs uppercase tracking-[0.16em] text-bone/45">
          Or call directly · {CONTACT.phoneDisplay}
        </p>
      </div>
    </section>
  );
}
