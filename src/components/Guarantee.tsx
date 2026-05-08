import { CTAButton } from "./CTAButton";

export function Guarantee() {
  return (
    <section id="guarantee" className="bg-ink text-bone py-28 sm:py-36">
      <div className="mx-auto max-w-4xl px-6 text-center sm:px-10">
        <p className="mb-6 text-xs uppercase tracking-[0.22em] text-gold">
          The guarantee
        </p>
        <p className="font-display text-[clamp(2.25rem,5vw,4rem)] leading-[1.1] tracking-tight text-bone">
          If Metis Cortex doesn&rsquo;t book at least{" "}
          <span className="italic text-gold-soft">5 extra appointments</span>{" "}
          in month one, you get a full refund of the setup fee.
        </p>
        <p className="mt-8 text-base text-bone/70">
          No paperwork. No questions.
        </p>

        <div className="mt-12 flex justify-center">
          <CTAButton>Book a 10-minute demo</CTAButton>
        </div>
      </div>
    </section>
  );
}
