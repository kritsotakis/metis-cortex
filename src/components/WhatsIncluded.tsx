import { OFFER, PRICING, priceFormatAud } from "@/lib/site";

const stack: { title: string; detail: string; value: string }[] = [
  {
    title: "AI receptionist on your existing number, 24/7",
    detail:
      "Zoe picks up every inbound within 60 seconds. After-hours, overflow, missed calls — covered.",
    value: "Worth A$4,000/mo (cost of a junior FT receptionist)",
  },
  {
    title: "14-day done-for-you setup",
    detail:
      "No IT work on your side. We install, configure, and tune. You answer five questions and approve the script.",
    value: "Worth A$5,000 (typical AI agency build)",
  },
  {
    title: "Custom voice trained on your existing call recordings",
    detail:
      "Same vocabulary, same tone, same bracket of jobs. Zoe sounds like your business.",
    value: "Worth A$2,000 (one-off)",
  },
  {
    title: "CRM + calendar integration",
    detail:
      "Direct write to Jobber, ServiceM8, GoHighLevel, Cliniko, SevenRooms, NowBookIt, or Google Calendar. No copy-paste.",
    value: "Worth A$1,500 (one-off)",
  },
  {
    title: "Monthly prompt + workflow tuning",
    detail:
      "One prompt update + one workflow tweak per month included. Pricing change, new service, new policy — handled.",
    value: "Worth A$500/mo (consultant retainer)",
  },
  {
    title: "Real-time call transcription + lead routing",
    detail:
      "Every call transcribed, tagged, and routed. You see what Zoe handled before you reply.",
    value: "Worth A$300/mo",
  },
  {
    title: "Australian-owned support, business hours",
    detail:
      "Mon–Fri AEST. Email + SMS. We answer. No offshore ticket queue.",
    value: "Worth A$200/mo",
  },
];

export function WhatsIncluded() {
  return (
    <section className="bg-bone py-24 sm:py-32">
      <div className="mx-auto max-w-6xl px-6 sm:px-10">
        <div className="grid gap-16 lg:grid-cols-[1fr_1.4fr] lg:gap-24">
          <div>
            <p className="mb-4 text-xs uppercase tracking-[0.22em] text-gold">
              What you get
            </p>
            <h2 className="font-display text-4xl leading-tight tracking-tight text-ink sm:text-5xl">
              {OFFER.name}.
            </h2>
            <p className="mt-6 text-base leading-relaxed text-ink-muted">
              Built on Retell AI for voice, GoHighLevel for CRM and workflow,
              Twilio for numbers. We configure all of it.
            </p>
            <p className="mt-8 text-sm text-ink-muted">
              <span className="font-medium text-ink">Total stack value:</span>{" "}
              A$8,500 setup + A$5,000/mo
            </p>
            <p className="mt-2 text-sm text-ink-muted">
              <span className="font-medium text-ink">Your investment:</span>{" "}
              {priceFormatAud(PRICING.setupAud)} setup +{" "}
              {priceFormatAud(PRICING.monthlyAud)}/mo
            </p>
            <p className="mt-2 text-sm text-gold">
              {priceFormatAud(PRICING.foundingMonthlyAud)}/mo founding rate for
              first {PRICING.foundingClientCap} case-study clients
            </p>
          </div>

          <ul className="divide-y divide-ink/10 border-y border-ink/10">
            {stack.map((item, i) => (
              <li
                key={item.title}
                className="grid grid-cols-[auto_1fr] items-start gap-6 py-6"
              >
                <span className="font-display text-2xl text-gold">
                  {String(i + 1).padStart(2, "0")}
                </span>
                <div>
                  <p className="text-lg leading-snug text-ink">
                    {item.title}
                  </p>
                  <p className="mt-2 text-sm leading-relaxed text-ink-muted">
                    {item.detail}
                  </p>
                  <p className="mt-2 text-xs uppercase tracking-[0.14em] text-ink-muted/80">
                    {item.value}
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
