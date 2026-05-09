import { OFFER, PRICING, priceFormatAud } from "@/lib/site";

const stack: { title: string; detail: string }[] = [
  {
    title: "AI receptionist on your existing number, 24/7",
    detail:
      "Zoe picks up every inbound within 60 seconds. After-hours, overflow, missed calls — covered.",
  },
  {
    title: "14-day done-for-you setup",
    detail:
      "No IT work on your side. We install, configure, and tune. You answer five questions and approve the script.",
  },
  {
    title: "Custom voice trained on your existing call recordings",
    detail:
      "Same vocabulary, same tone, same bracket of jobs. Zoe sounds like your business.",
  },
  {
    title: "CRM + calendar integration",
    detail:
      "Direct write to Jobber, ServiceM8, GoHighLevel, Cliniko, SevenRooms, NowBookIt, or Google Calendar. No copy-paste.",
  },
  {
    title: "Monthly prompt + workflow tuning",
    detail:
      "One prompt update + one workflow tweak per month included. Pricing change, new service, new policy — handled.",
  },
  {
    title: "Real-time call transcription + lead routing",
    detail:
      "Every call transcribed, tagged, and routed. You see what Zoe handled before you reply.",
  },
  {
    title: "Australian-owned support, business hours",
    detail:
      "Mon–Fri AEST. Email + SMS. We answer. No offshore ticket queue.",
  },
];

export function WhatsIncluded() {
  return (
    <section id="pricing" className="bg-bone py-24 sm:py-32">
      <div className="mx-auto max-w-6xl px-6 sm:px-10">
        <div className="grid gap-16 lg:grid-cols-[1fr_1.4fr] lg:gap-24">
          <div>
            <p className="mb-4 text-xs uppercase tracking-[0.22em] text-bronze">
              What&rsquo;s included
            </p>
            <h2 className="font-display text-4xl leading-tight tracking-tight text-ink sm:text-5xl">
              {OFFER.name}.
            </h2>
            <p className="mt-6 text-base leading-relaxed text-ink-muted">
              Everything below installs in {PRICING.installDays} days for{" "}
              {priceFormatAud(PRICING.setupAud)} +{" "}
              {priceFormatAud(PRICING.monthlyAud)}/mo. The {PRICING.installDays}{" "}
              days is the value — that&rsquo;s how long it takes to train Zoe
              on your menu, services, and edge cases. Not configurable AI you
              fill in yourself. Installed AI we configure for you.
            </p>
            <p className="mt-6 text-sm text-ink-muted">
              {priceFormatAud(PRICING.foundingMonthlyAud)}/mo founding rate for
              the first {PRICING.foundingClientCap} case-study clients — one
              slot per vertical.
            </p>
          </div>

          <ul className="divide-y divide-ink/10 border-y border-ink/10">
            {stack.map((item, i) => (
              <li
                key={item.title}
                className="grid grid-cols-[auto_1fr] items-start gap-6 py-6"
              >
                <span className="font-display text-2xl text-ink/50">
                  {String(i + 1).padStart(2, "0")}
                </span>
                <div>
                  <p className="text-lg leading-snug text-ink">
                    {item.title}
                  </p>
                  <p className="mt-2 text-sm leading-relaxed text-ink-muted">
                    {item.detail}
                  </p>
                </div>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </section>
  );
}
