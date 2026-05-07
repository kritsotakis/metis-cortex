import type { Metadata } from "next";
import { Cormorant_Garamond, Inter } from "next/font/google";
import "./globals.css";

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

const SITE_URL = "https://metiscortex.au";
const TITLE = "Metis Cortex — Stop missing calls.";
const DESCRIPTION =
  "We install an AI receptionist on your business in 14 days. It picks up every missed call within 60 seconds, qualifies the lead, and books the appointment. A$1,500 setup, A$600/month. Refund guarantee.";

export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  title: TITLE,
  description: DESCRIPTION,
  alternates: { canonical: "/" },
  openGraph: {
    type: "website",
    url: SITE_URL,
    siteName: "Metis Cortex",
    title: TITLE,
    description: DESCRIPTION,
    locale: "en_AU",
    images: [
      {
        url: "/og.png",
        width: 1200,
        height: 630,
        alt: "Metis Cortex — Stop missing calls.",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: TITLE,
    description: DESCRIPTION,
    images: ["/og.png"],
  },
  robots: { index: true, follow: true },
};

const localBusinessJsonLd = {
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  name: "Metis Cortex",
  description: DESCRIPTION,
  url: SITE_URL,
  email: "peter@kritsotakis.com.au",
  telephone: "+61423668766",
  priceRange: "A$1,500 setup + A$600/month",
  areaServed: { "@type": "City", name: "Sydney" },
  address: {
    "@type": "PostalAddress",
    addressLocality: "Sydney",
    addressRegion: "NSW",
    addressCountry: "AU",
  },
  parentOrganization: {
    "@type": "Organization",
    name: "Kritsotakis Family Trust",
    taxID: "45 984 876 899",
    legalName:
      "Kritsotakis Family Trust (Trustee: Kritsotakis Investments Pty Ltd, ACN 153 844 136)",
  },
  makesOffer: {
    "@type": "Offer",
    name: "Frontline — AI Receptionist",
    priceSpecification: {
      "@type": "UnitPriceSpecification",
      price: "1500",
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
