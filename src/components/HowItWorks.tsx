const steps = [
  {
    n: "01",
    title: "Book a 15-min operator call",
    body: "No SDR. You're talking to the person who'll build it. We'll find out where you're bleeding time and tell you, straight, whether we can help.",
  },
  {
    n: "02",
    title: "2-week paid audit + 90-day roadmap",
    body: "Business shadowing, opportunity register, ROI per opportunity. From A$2,000. 50% of the audit fee credits to any build over A$5,000 booked within 90 days.",
  },
  {
    n: "03",
    title: "Install one system. Prove ROI. Expand.",
    body: "One offer per engagement until we've earned the right to expand. No 18-month 'platform' promises. You keep ownership of every system we build.",
  },
];

export function HowItWorks() {
  return (
    <section id="how-it-works" className="bg-bone-soft py-24 sm:py-32">
      <div className="mx-auto max-w-6xl px-6 sm:px-10">
        <p className="mb-4 text-xs uppercase tracking-[0.22em] text-bronze">
          How we work
        </p>
        <h2 className="font-display max-w-3xl text-4xl leading-tight tracking-tight text-ink sm:text-5xl">
          Three steps. One offer at a time. No platform lock-in.
        </h2>

        <ol className="mt-16 grid gap-px overflow-hidden rounded-lg bg-ink/10 sm:grid-cols-3">
          {steps.map((step) => (
            <li
              key={step.n}
              className="flex flex-col gap-6 bg-bone-soft p-10"
            >
              <span className="font-display text-5xl text-ink/50">{step.n}</span>
              <h3 className="font-display text-2xl text-ink">{step.title}</h3>
              <p className="text-base leading-relaxed text-ink-soft">
                {step.body}
              </p>
            </li>
          ))}
        </ol>
      </div>
    </section>
  );
}
