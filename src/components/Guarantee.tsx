import { CTAButton } from "./CTAButton";
import { PRICING, priceFormatAud } from "@/lib/site";

export function Guarantee() {
  return (
    <section id="guarantee" className="bg-ink text-bone py-28 sm:py-36">
      <div className="mx-auto max-w-4xl px-6 text-center sm:px-10">
        <p className="mb-6 text-xs uppercase tracking-[0.22em] text-gold">
          The guarantees
        </p>

        <p className="font-display text-[clamp(2rem,4vw,3rem)] leading-[1.15] tracking-tight text-bone">
          If Zoe doesn&rsquo;t handle{" "}
          <span className="mc-bronze-underline">
            {PRICING.guaranteePercentHandled}% of your missed calls
          </span>{" "}
          and save your team at least {PRICING.guaranteeHoursSaved} hours of
          phone time in the first {PRICING.guaranteeWindowDays} days,{" "}
          <span className="mc-italic-display text-gold-soft">
            full refund of the setup fee.
          </span>
        </p>

        <hr className="mc-rule-on-ink mx-auto my-12 w-24" />

        <p className="font-display text-[clamp(1.75rem,3vw,2.5rem)] leading-[1.2] tracking-tight text-bone/90">
          If we don&rsquo;t go live in{" "}
          <span className="mc-bronze-underline">
            {PRICING.installDays} days
          </span>
          ,{" "}
          <span className="mc-italic-display text-gold-soft">
            we waive the {priceFormatAud(PRICING.setupAud)} setup fee.
          </span>
        </p>

        <p className="mt-10 text-base text-bone/65">
          No paperwork. No questions.
        </p>

        <div className="mt-12 flex justify-center">
          <CTAButton>Book a 15-min demo</CTAButton>
        </div>
      </div>
    </section>
  );
}
