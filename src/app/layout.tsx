import type { Metadata } from "next";
import { Cormorant_Garamond, Inter } from "next/font/google";
import "./globals.css";
import { CONTACT, LEGAL, PRICING, SITE, SOCIAL, contactEmail } from "@/lib/site";

const cormorant = Cormorant_Garamond({
  variable: "--font-cormorant",
  subsets: ["latin"],
  weight: ["500", "600", "700"],
  display: "swap",
});

const inter = Inter({
  variable: "--font-inter",
  subsets: ["latin"],
  display: "swap",
});

export const metadata: Metadata = {
  metadataBase: new URL(SITE.url),
  title: SITE.title,
  description: SITE.description,
  alternates: { canonical: "/" },
  openGraph: {
    type: "website",
    url: SITE.url,
    siteName: SITE.name,
    title: SITE.title,
    description: SITE.description,
    locale: SITE.locale,
    images: [
      {
        url: "/og.png",
        width: 1200,
        height: 630,
        alt: SITE.title,
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: SITE.title,
    description: SITE.description,
    images: ["/og.png"],
  },
  robots: { index: true, follow: true },
};

const sameAs = [SOCIAL.linkedinCompany, SOCIAL.linkedinPersonal].filter(
  (v): v is string => Boolean(v),
);

const localBusinessJsonLd = {
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  name: SITE.name,
  description: SITE.description,
  url: SITE.url,
  email: contactEmail(),
  telephone: CONTACT.phoneE164,
  priceRange: `A$${PRICING.setupAud.toLocaleString()} setup + A$${PRICING.monthlyAud}/month`,
  areaServed: { "@type": "City", name: "Sydney" },
  address: {
    "@type": "PostalAddress",
    addressLocality: "Sydney",
    addressRegion: "NSW",
    addressCountry: "AU",
  },
  ...(sameAs.length > 0 ? { sameAs } : {}),
  parentOrganization: {
    "@type": "Organization",
    name: LEGAL.trustName,
    taxID: LEGAL.abn,
    legalName: `${LEGAL.trustName} (Trustee: ${LEGAL.trusteeName}, ACN ${LEGAL.trusteeAcn})`,
  },
  makesOffer: {
    "@type": "Offer",
    name: "Metis Cortex Receptionist",
    priceSpecification: {
      "@type": "UnitPriceSpecification",
      price: String(PRICING.setupAud),
      priceCurrency: "AUD",
      unitText: "setup",
    },
  },
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en-AU" className={`${cormorant.variable} ${inter.variable}`}>
      <body className="bg-bone text-ink">
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify(localBusinessJsonLd),
          }}
        />
        {children}
      </body>
    </html>
  );
}
