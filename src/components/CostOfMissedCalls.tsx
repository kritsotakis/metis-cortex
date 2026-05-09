const stats = [
  {
    figure: "5",
    label: "booking mistakes per month",
    body: "Across the four businesses we run, every team has at least 5 booking mistakes a month they don't know about — wrong night, wrong table size, missed dietary, wrong service code.",
  },
  {
    figure: "A$280",
    label: "average value at risk per mistake",
    body: "Cleaning, clinic, chemistry lab and a 21-year restaurant. The average revenue at risk per mistake — cancellation, no-show, wrong-night chaos — sits ~A$280.",
  },
  {
    figure: "A$16,800",
    label: "per business per year",
    body: "5 × A$280 × 12 = A$16,800/year per business in recoverable revenue leak. Across four businesses that's real money. Zoe is built to catch all five.",
  },
];

export function CostOfMissedCalls() {
  return (
    <section className="bg-bone-soft py-24 sm:py-32">
      <div className="mx-auto max-w-6xl px-6 sm:px-10">
        <p className="mb-4 text-xs uppercase tracking-[0.22em] text-bronze">
          The cost of missed calls
        </p>
        <h2 className="font-display max-w-3xl text-4xl leading-tight tracking-tight text-ink sm:text-5xl">
          21 years of operating four businesses taught us where the leak is.
        </h2>
        <p className="mt-4 max-w-2xl text-base leading-relaxed text-ink-muted">
          Cleaning. A Sydney restaurant we ran for 21 years. An aesthetic
          clinic. A chemistry lab. The most predictable revenue leak across
          all four is what happens to the phone bookings the team thinks they
          got right.
        </p>

        <div className="mt-16 grid gap-px overflow-hidden rounded-lg bg-ink/10 sm:grid-cols-3">
          {stats.map((s) => (
            <div key={s.label} className="bg-bone-soft p-8 sm:p-10">
              <p className="font-display text-6xl text-ink">{s.figure}</p>
              <p className="mt-2 text-sm uppercase tracking-[0.16em] text-ink-muted">
                {s.label}
              </p>
              <p className="mt-6 text-base leading-relaxed text-ink-soft">
                {s.body}
              </p>
            </div>
          ))}
        </div>

        <p className="mt-8 max-w-3xl text-xs leading-relaxed text-ink-muted">
          Operator estimates from running Australian service businesses since
          2003. Real DSK Property Cleaning Zoe-pilot data publishes after our
          14-day install completes.
        </p>
      </div>
    </section>
  );
}
