import { CTAButton } from "./CTAButton";

export function ClosingCTA() {
  return (
    <section className="relative overflow-hidden bg-ink text-bone py-28 sm:py-36">
      <div
        aria-hidden="true"
        className="pointer-events-none absolute inset-0 opacity-[0.07]"
        style={{
          backgroundImage:
            "radial-gradient(circle at 70% 30%, #b07843 0%, transparent 55%)",
        }}
      />
      <div className="relative mx-auto max-w-5xl px-6 text-center sm:px-10">
        <p className="font-display text-[clamp(2.5rem,6vw,5rem)] leading-[1.05] tracking-tight">
          Your next missed call is at{" "}
          <span className="italic text-gold-soft">7pm tonight.</span>
          <br />
          Want it booked by 7:01?
        </p>
        <div className="mt-12 flex justify-center">
          <CTAButton>Book a 10-minute demo</CTAButton>
        </div>
      </div>
    </section>
  );
}
