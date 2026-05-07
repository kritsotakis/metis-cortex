import { CTAButton } from "./CTAButton";

export function Hero() {
  return (
    <section className="relative overflow-hidden bg-ink text-bone">
      <div
        aria-hidden="true"
        className="pointer-events-none absolute inset-0 opacity-[0.08]"
        style={{
          backgroundImage:
            "radial-gradient(circle at 20% 0%, #b07843 0%, transparent 45%), radial-gradient(circle at 80% 100%, #b07843 0%, transparent 50%)",
        }}
      />
      <header className="relative mx-auto flex max-w-6xl items-center justify-between px-6 pt-8 sm:px-10">
        <a
          href="#"
          aria-label="Metis Cortex"
          className="flex items-center gap-3 transition-opacity hover:opacity-80"
        >
          <img
            src="/brand/logo-mark-128.png"
            alt=""
            width={40}
            height={40}
            className="h-10 w-10 rounded"
          />
          <span className="font-display text-2xl font-medium tracking-tight text-bone">
            Metis<span aria-hidden="true" className="mx-1 text-gold">·</span>Cortex
          </span>
        </a>
        <a
          href="#guarantee"
          className="hidden text-sm uppercase tracking-[0.18em] text-bone/70 hover:text-bone sm:block"
        >
          The Guarantee
        </a>
      </header>

      <div className="relative mx-auto max-w-6xl px-6 pt-20 pb-28 sm:px-10 sm:pt-28 sm:pb-36">
        <p className="mb-6 inline-flex items-center gap-3 text-xs uppercase tracking-[0.22em] text-gold">
          <span className="h-px w-8 bg-gold" />
          Speed-to-Lead, installed in 14 days
        </p>

        <h1 className="font-display text-[clamp(3.5rem,9vw,7rem)] font-semibold leading-[0.95] tracking-tight text-bone">
          Stop missing
          <br />
          <span className="italic text-gold-soft">calls.</span>
        </h1>

        <p className="mt-10 max-w-2xl text-lg leading-relaxed text-bone/80 sm:text-xl">
          We install an AI receptionist on your business in 14 days. It picks
          up every missed call and new enquiry within 60 seconds, qualifies the
          lead, and books the appointment.{" "}
          <span className="text-bone">A$1,500 setup, A$600/month.</span> If we
          don&rsquo;t book you 5 extra appointments in month one, full refund.
        </p>

        <div className="mt-12 flex flex-wrap items-center gap-6">
          <CTAButton>Book a 10-minute demo</CTAButton>
          <p className="text-sm text-bone/60">
            Built on DSK Property Cleaning — our own Sydney cleaning business.
            Australian-owned.
          </p>
        </div>
      </div>
    </section>
  );
}
