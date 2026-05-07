const steps = [
  {
    n: "01",
    title: "30-minute scoping call",
    body: "Book this week. We learn your business, your call patterns, and the one thing you most need answered after hours.",
  },
  {
    n: "02",
    title: "14-day install",
    body: "We configure the voice agent, the CRM, the calendar, the number, and the scripts. You approve. You do nothing else.",
  },
  {
    n: "03",
    title: "Month-one report",
    body: "You see the lift in answered calls, booked appointments, and recovered revenue — or we refund the setup fee.",
  },
];

export function HowItWorks() {
  return (
    <section className="bg-bone-soft py-24 sm:py-32">
      <div className="mx-auto max-w-6xl px-6 sm:px-10">
        <p className="mb-4 text-xs uppercase tracking-[0.22em] text-gold">
          How it works
        </p>
        <h2 className="font-display max-w-3xl text-4xl leading-tight tracking-tight text-ink sm:text-5xl">
          Three steps. Two weeks. One number to watch.
        </h2>

        <ol className="mt-16 grid gap-px overflow-hidden rounded-2xl bg-ink/10 sm:grid-cols-3">
          {steps.map((step) => (
            <li
              key={step.n}
              className="flex flex-col gap-6 bg-bone-soft p-10"
            >
              <span className="font-display text-5xl text-gold">{step.n}</span>
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
