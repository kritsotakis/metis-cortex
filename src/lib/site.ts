export const SITE = {
  url: "https://metiscortex.au",
  name: "Metis Cortex",
  shortName: "Metis",
  title:
    "Metis Cortex — AI systems for Sydney service businesses, built by an operator",
  description:
    "We build AI receptionists, workflow automation, and operational audits for service businesses — and we're running them on our own four businesses first. Six years enterprise IT (MCSE / Cisco / Citrix). 21 years running a restaurant. Sydney, AUD. Honest pricing, no lock-in, one offer per engagement.",
  tagline: "We build the AI we wish we'd had at the restaurant.",
  locale: "en_AU",
} as const;

export const CONTACT = {
  primaryEmail: "peter@kritsotakis.com.au",
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

/* PRICING — v3 (2026-05-18). Setup A$5,000 + Monthly A$1,500 reflects the
 * pivot pricing per STRIPE-DIFF-PIVOT-V3.md. Founding A$800 archived (kept
 * accessible in Stripe as legacy closer-tool for original outreach prospects). */
export const PRICING = {
  setupAud: 5000,
  monthlyAud: 1500,
  auditLiteAud: 2000,
  auditStandardAud: 3500,
  auditDeepAud: 5000,
  workflowSetupAud: 3000,
  workflowMonthlyAud: 500,
  /* Legacy — superseded by v3 pivot but archived for grandfathering */
  legacySetupAud: 1500,
  legacyStandardMonthlyAud: 1200,
  legacyFoundingMonthlyAud: 800,
} as const;

export function bookingHref(): string {
  if (BOOKING.calendlyUrl) return BOOKING.calendlyUrl;
  return `mailto:${contactEmail()}?subject=Metis%20Cortex%20demo`;
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
