import { CTAButton } from "./CTAButton";

export function ClosingCTA() {
  return (
    <section className="relative overflow-hidden bg-ink text-bone py-28 sm:py-36">
      <div className="relative mx-auto max-w-5xl px-6 text-center sm:px-10">
        <p className="mb-6 text-xs uppercase tracking-[0.22em] text-bronze">
          Operator-led, dogfood-tested
        </p>

        <p className="font-display text-[clamp(2.5rem,6vw,5rem)] leading-[1.05] tracking-tight">
          We build the AI we wish we&rsquo;d had
          <br />
          <span className="mc-italic-display text-bone/85">
            at the restaurant.
          </span>
        </p>

        <p className="mt-10 mx-auto max-w-2xl text-base leading-relaxed text-bone/75">
          Sydney AI agency. Six years building enterprise IT before that, 21
          years running a restaurant. We use everything we sell on our own
          businesses first. If you want one of the first external installs in
          your vertical — at pilot terms — book a 15-min call.
        </p>

        <div className="mt-12 flex justify-center">
          <CTAButton>Book a 15-min operator call</CTAButton>
        </div>
      </div>
    </section>
  );
}
