import { CTAButton } from "./CTAButton";

export function AboutOperator() {
  return (
    <section id="about" className="bg-bone-soft py-24 sm:py-32">
      <div className="mx-auto max-w-4xl px-6 sm:px-10">
        <p className="mb-4 text-xs uppercase tracking-[0.22em] text-bronze">
          About
        </p>
        <h2 className="font-display max-w-3xl text-4xl leading-tight tracking-tight text-ink sm:text-5xl">
          Built by an operator. Tested on his own businesses first.
        </h2>

        <div className="mt-12 space-y-7 text-lg leading-relaxed text-ink-soft">
          <p>
            In my last year running Limani Seafood Restaurant, we missed 40+
            calls a week. I&rsquo;d spent six years before that building
            enterprise phone systems for banks. And I couldn&rsquo;t fix my own
            restaurant&rsquo;s phone.
          </p>

          <p className="text-ink">
            That gap —{" "}
            <em>
              I know how to build this, but the tools haven&rsquo;t existed at a
              price service businesses can pay
            </em>{" "}
            — is why Metis Cortex exists.
          </p>

          <p>
            You don&rsquo;t need another agency pitching slides. You need
            someone who&rsquo;s been in your seat. I built this because I
            needed it for my own businesses first. I&rsquo;m Peter Kritsotakis.
          </p>

          <p className="text-base text-ink-muted">
            Background: Microsoft systems engineer (MCP / MCSA / MCSE), Cisco
            engineer, Citrix engineer · Limani Seafood Narrabeen 2004–2025 ·
            currently building Detailing Solutions Krew (cleaning), Eonia
            Omorfia (aesthetic clinic), HydraLab (chemical manufacturing), and
            a trading-discipline software venture. All four are early-stage.
            Metis Cortex is what I&rsquo;m installing on each of them as I
            scale them.
          </p>

          <p>
            The agency is in its first month. We have one external pilot in
            flight — a Sydney accountant — and we&rsquo;re not pretending
            otherwise. Everything we sell, we use ourselves first. If you want
            to be one of the first external installs in your vertical — at
            pilot terms — let&rsquo;s talk.
          </p>

          <p className="font-display text-2xl text-ink">— Peter</p>
        </div>

        <div className="mt-12">
          <CTAButton surface="bone">Book a 15-min operator call</CTAButton>
        </div>
      </div>
    </section>
  );
}
