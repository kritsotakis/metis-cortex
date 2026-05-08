export const SITE = {
  url: "https://metiscortex.au",
  name: "Metis Cortex",
  title: "Metis Cortex — Stop missing calls.",
  description:
    "We install an AI receptionist on your business in 14 days. It picks up every missed call within 60 seconds, qualifies the lead, and books the appointment. A$1,500 setup, A$600/month. Refund guarantee.",
  locale: "en_AU",
} as const;

export const CONTACT = {
  primaryEmail: "peter@kritsotakis.com.au",
  brandEmail: null as string | null,
  phoneE164: "+61423668766",
  phoneDisplay: "0423 668 766",
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
  asicRegistrationNumber: null as string | null,
} as const;

export const PRICING = {
  setupAud: 1500,
  monthlyAud: 600,
  guaranteeBookings: 5,
  guaranteeWindowDays: 30,
} as const;

export function bookingHref(): string {
  return BOOKING.calendlyUrl ?? BOOKING.fallbackHref;
}

export function contactEmail(): string {
  return CONTACT.brandEmail ?? CONTACT.primaryEmail;
}

export function asicLine(): string {
  if (LEGAL.asicRegistrationNumber) {
    return `ASIC business name: ${LEGAL.asicBusinessName} (reg ${LEGAL.asicRegistrationNumber})`;
  }
  return "ASIC business name registration pending";
}
