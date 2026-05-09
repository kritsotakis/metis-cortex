import { CTAButton } from "./CTAButton";
import { PRICING, priceFormatAud } from "@/lib/site";

export function ClosingCTA() {
  return (
    <section className="relative overflow-hidden bg-ink text-bone py-28 sm:py-36">
      <div className="relative mx-auto max-w-5xl px-6 text-center sm:px-10">
        <p className="mb-6 text-xs uppercase tracking-[0.22em] text-bronze">
          Founding rate · {PRICING.foundingClientCap} spots
        </p>

        <p className="font-display text-[clamp(2.5rem,6vw,5rem)] leading-[1.05] tracking-tight">
          Your next missed call is at 7pm tonight.
          <br />
          Want it booked by 7:01?
        </p>

        <p className="mt-10 mx-auto max-w-2xl text-base leading-relaxed text-bone/75">
          One slot per vertical — cleaning, restaurant, real estate, dental,
          beauty. After the first {PRICING.foundingClientCap}, standard rate.
          15-minute demo, no pitch deck.
        </p>

        <div className="mt-12 flex justify-center">
          <CTAButton>Hear Zoe — book the demo</CTAButton>
        </div>
      </div>
    </section>
  );
}
