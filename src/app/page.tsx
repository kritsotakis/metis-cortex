import { Hero } from "@/components/Hero";
import { WhatStopsBleeding } from "@/components/WhatStopsBleeding";
import { HowItWorks } from "@/components/HowItWorks";
import { ServiceStrip } from "@/components/ServiceStrip";
import { AboutOperator } from "@/components/AboutOperator";
import { FAQ } from "@/components/FAQ";
import { ClosingCTA } from "@/components/ClosingCTA";
import { Footer } from "@/components/Footer";

export default function Home() {
  return (
    <main>
      <Hero />
      <WhatStopsBleeding />
      <HowItWorks />
      <ServiceStrip />
      <AboutOperator />
      <FAQ />
      <ClosingCTA />
      <Footer />
    </main>
  );
}
