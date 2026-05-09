export const SITE = {
  url: "https://metiscortex.au",
  name: "Metis Cortex",
  shortName: "Metis",
  title: "Metis Cortex — 100% answered. Or your money back.",
  description:
    "We install an AI receptionist on your business in 14 days. Zoe picks up every missed call within 60 seconds, qualifies the lead, books the appointment. A$1,500 setup, A$1,200/mo (A$800/mo founding rate for first 5 case study clients). 100% answered or your money back; live in 14 days or we waive the setup fee.",
  locale: "en_AU",
} as const;

export const CONTACT = {
  primaryEmail: "peter@kritsotakis.com.au",
  /* brandEmail flipped to info@metiscortex.au 2026-05-09 per Peter — email
   * forwarding being set up via Cloudflare Email Routing imminently.
   * Until forwarding is live, mail to info@ will bounce; that's an
   * accepted short window. */
  brandEmail: "info@metiscortex.au" as string | null,
  brandEmailTarget: "info@metiscortex.au",
  phoneE164: "+61414885366",
  phoneDisplay: "0414 885 366",
} as const;

export const SOCIAL = {
  linkedinPersonal: "https://www.linkedin.com/in/peterkritsotakis/",
  linkedinCompany: null as string | null,
} as const;

export const BOOKING = {
  calendlyUrl: null as string | null,
  fallbackHref: "mailto:peter@kritsotakis.com.au?subject=Metis%20Cortex%20demo",
} as const;

export const LEGAL = {
  trustName: "Kritsotakis Family Trust",
  abn: "45 984 876 899",
  trusteeName: "Kritsotakis Investments Pty Ltd",
  trusteeAcn: "153 844 136",
  trusteeAbn: "58 153 844 136",
  asicBusinessName: "Metis Cortex",
  asicRegistrationDate: "9 May 2026" as string | null,
  asicNextRenewalDate: "9 May 2027",
} as const;

export const PRICING = {
  setupAud: 1500,
  monthlyAud: 1200,
  foundingMonthlyAud: 800,
  foundingClientCap: 5,
  guaranteePercentHandled: 100,
  guaranteeHoursSaved: 10,
  guaranteeWindowDays: 30,
  installDays: 14,
} as const;

export const OFFER = {
  name: "The 14-Day Receptionist Install",
} as const;

export function bookingHref(): string {
  return BOOKING.calendlyUrl ?? BOOKING.fallbackHref;
}

export function contactEmail(): string {
  return CONTACT.brandEmail ?? CONTACT.primaryEmail;
}

export function asicLine(): string {
  if (LEGAL.asicRegistrationDate) {
    return `ASIC business name: ${LEGAL.asicBusinessName} (registered ${LEGAL.asicRegistrationDate})`;
  }
  return "ASIC business name registration pending";
}

export function priceFormatAud(amount: number): string {
  return `A$${amount.toLocaleString("en-AU")}`;
}
