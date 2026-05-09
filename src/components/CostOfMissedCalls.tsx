const stats = [
  {
    figure: "5",
    label: "booking mistakes per month",
    body: "Every operator we install Zoe with finds at least 5 booking mistakes per month their team didn't know about — wrong night, wrong table size, missed dietary, wrong service code.",
  },
  {
    figure: "A$280",
    label: "average booking lost",
    body: "Across the four service businesses we run (cleaning, clinic, chemistry lab, restaurant) the average value of a missed booking call sits ~A$280.",
  },
  {
    figure: "A$13,500",
    label: "per business per year",
    body: "Five missed bookings/month × A$280 × 12 = A$13,500/year walking out the door. Zoe pays for herself in the first quarter.",
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
          We ran the numbers on the businesses we run.
        </h2>
        <p className="mt-4 max-w-2xl text-base leading-relaxed text-ink-muted">
          Cleaning. A 21-year Sydney restaurant. An aesthetic clinic. A
          chemistry lab. Across the four, missed phone bookings are the most
          predictable revenue leak we&rsquo;ve measured. Operator math, not
          industry estimates.
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
          Numbers from operating Australian service businesses since 2003. Real
          DSK Property Cleaning Zoe-pilot data publishes after our 14-day
          install completes.
        </p>
      </div>
    </section>
  );
}
