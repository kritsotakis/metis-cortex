const before = [
  { label: "Missed calls / week", value: "—" },
  { label: "Avg response time", value: "—" },
];

const after = [
  { label: "Missed calls / week", value: "0" },
  { label: "Avg response time", value: "60 sec" },
  { label: "Booking lift", value: "—" },
  { label: "Recovered revenue", value: "—" },
];

export function DSKCaseStudy() {
  return (
    <section className="bg-ink text-bone py-24 sm:py-32">
      <div className="mx-auto max-w-6xl px-6 sm:px-10">
        <p className="mb-4 text-xs uppercase tracking-[0.22em] text-bronze">
          Case study — DSK Property Cleaning
        </p>
        <h2 className="font-display max-w-3xl text-4xl leading-tight tracking-tight sm:text-5xl">
          We installed Metis Cortex on our own cleaning business first.
        </h2>
        <p className="mt-6 max-w-2xl text-base leading-relaxed text-bone/70">
          DSK is a Sydney property cleaning company doing pre-sale and strata
          work. We pointed Metis Cortex at it before we ever sold it to anyone
          else. The numbers below are from the 14-day pilot — final figures
          land week of completion.
        </p>

        <div className="mt-16 grid gap-8 lg:grid-cols-2">
          <div className="rounded-lg border border-bone/15 p-10">
            <p className="text-xs uppercase tracking-[0.18em] text-bone/50">
              Before
            </p>
            <dl className="mt-6 space-y-5">
              {before.map((row) => (
                <div
                  key={row.label}
                  className="flex items-baseline justify-between gap-6 border-b border-bone/10 pb-4 last:border-0"
                >
                  <dt className="text-bone/70">{row.label}</dt>
                  <dd className="font-display text-3xl text-bone">
                    {row.value}
                  </dd>
                </div>
              ))}
            </dl>
          </div>

          <div className="rounded-lg bg-bone text-ink p-10">
            <p className="text-xs uppercase tracking-[0.18em] text-bronze">
              After
            </p>
            <dl className="mt-6 space-y-5">
              {after.map((row) => (
                <div
                  key={row.label}
                  className="flex items-baseline justify-between gap-6 border-b border-ink/10 pb-4 last:border-0"
                >
                  <dt className="text-ink-muted">{row.label}</dt>
                  <dd className="font-display text-3xl text-ink">
                    {row.value}
                  </dd>
                </div>
              ))}
            </dl>
          </div>
        </div>

        <p className="mt-10 text-sm text-bone/50">
          Pilot data placeholder — replace with real figures from week-of-completion report.
        </p>
      </div>
    </section>
  );
}
