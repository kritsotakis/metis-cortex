# Metis Cortex — Vertical-Specific Objection Handling

> **For:** Peter, before any vertical-targeted demo
> **Purpose:** 25 vertical-specific objections layered on the 10 generics in `SALES-PREP-PACKAGE.md`
> **Voice:** AU English, operator-to-operator, no SaaS jargon
> **Updated:** 2026-05-08

---

## TL;DR — three universals

**#1 "I tried an AI receptionist and it was rubbish"** — validate, don't argue.
> *"Same — tested the lot before I built mine. Failure mode's identical: real question lands, AI flounders. Break isn't the voice tech, it's that no one builds it for you. Mine takes 14 days because I'm doing the build, not you."*

**#2 "It'll sound like a robot and customers will hate it"**
> *"Want to hear her? I'll dial the test number now, you tell me when she sounds like a robot. If she does, I owe you the call."*

**#3 "We already have someone answering the phone"**
> *"Zoe doesn't replace your front desk. She picks up calls they can't get to. After 6pm, Sundays, while Sarah's on lunch, while the phone rings four times during a quote. That's where the missed-call dollars live."*

---

## 1. Restaurant / Cafe

40-80 seat venue, owner-operator. SevenRooms/NowBookIt/Resy/OpenTable. Phone rings during service. 5-12% margins. Has seen Slang.ai in a competitor venue.

---

**Objection #1 — "I'm not paying $1,200/mo for something Slang or NowBookIt's AI does for $300"**

Underlying concern: price-anchoring. They've seen Slang.ai at A$399/mo per location and we look 3x more expensive at first glance.

Response: *"Slang's a phone bot — pre-recorded answers, single use case. NowBookIt's AI is a reporting tool, not a receptionist. Mine's built for you, trained on your menu, your covers, your voice. If $300 of pre-recorded did the job, you'd already have it."*

Bridge: *"What's actually killing your phones — bookings, takeaway orders, special requests, dietary questions, or all four?"*

Proof point: Tier 2 Knowledge per-asset Q&A (menu, allergens, wine, dietary, parking) is A$300 each, opt-in only. Slang doesn't separate that.

---

**Objection #2 — "When I was at Limani we knew every regular by name. AI can't do that."**

Underlying concern: lost personal touch — the thing that makes hospitality hospitality.

Response: *"Twenty-one years at Limani — same instinct. Regulars don't ring at 2pm to book Saturday — they walk past, wave, message me direct. The 2pm caller is the punter trying six places. Zoe handles him so your front-of-house has bandwidth for the regular at 6."*

Bridge: *"What percentage of your phone bookings are first-timers vs regulars, roughly?"*

Proof point: Zoe pushes caller history into your booking system — regulars land tagged so the team sees it. Not a replacement; a buffer for the strangers.

---

**Objection #3 — "Friday night is mayhem — what happens when she gets a 14-top with five dietaries?"**

Underlying concern: edge cases during peak. They're imagining the disaster scenario.

Response: *"She doesn't try. Over 8 pax, three+ dietaries, anything weird — Zoe takes the details, says 'I'll have the manager call back within the hour' and texts you the transcript. Same as a competent host who knows when to escalate."*

Bridge: *"What does your current best front-of-house person do with a 14-top dietary call right now?"*

Proof point: Built-in escalation — Zoe SMS-fires the operator within 60 seconds of any flagged call. Tested on QA Day 8-10.

---

**Objection #4 — "Restaurants are 5% margin. I can't carry $1,200/month if it doesn't pay back fast."**

Underlying concern: cash flow. Hospo margins are razor-thin and they've been burned by tech that promised payback and didn't deliver.

Response: *"Average cover at 60 seats is ~A$70. Recover four hung-up bookings a month — $280 plus alcohol, roughly square. Recover ten, you're up. 30-day refund means month one is on me — if she doesn't move the needle by week four, you're whole."*

Bridge: *"What's your average spend per cover, and roughly how many calls do you reckon ring out unanswered Friday-Saturday?"*

Proof point: Stacked guarantee — full refund if Zoe doesn't handle 100% of missed calls + save 10 hours in 30 days. Founding-rate A$800/mo tightens the maths further.

---

**Objection #5 — "I run SevenRooms / NowBookIt — does it actually plug in or is it another tab?"**

Underlying concern: tech stack pain. They've already got booking software they paid for and won't tolerate another disconnected system.

Response: *"Plugs in. SevenRooms, NowBookIt, OpenTable, Resy — Zoe books straight into the diary you already use, dietary fields and party-size logic included. No Metis Cortex tab. Your floor staff see bookings where they see them now."*

Bridge: *"Which one are you running, and what's the worst part of it for you right now?"*

Proof point: SevenRooms, NowBookIt, Resy, OpenTable all on the integration list per `HOW-IT-WORKS.md`. Integration build is in the 14 days, not a phase-2 upsell.

---

## 2. Boutique Real Estate

3-8 agents, principal-operator, $1M-$5M stock. One missed $2.5M vendor = $60K-$100K commission walking. "Personal service" is the brand. Vault RE / Box+Dice / Agentbox.

---

**Objection #6 — "If a $2M vendor rings and gets an AI, I've lost the listing before I open my mouth"**

Underlying concern: first impressions on high-value transactions. The vendor judges the agency in 30 seconds.

Response: *"Same instinct. So Zoe doesn't run on vendor calls during business hours — your mobile takes those. She catches the 7pm Sunday after the open home, the buyer-agent enquiry that lands while you're at a listing presentation. The calls you ran out on are the ones she saves."*

Bridge: *"What's your typical response time to a Saturday-afternoon enquiry right now?"*

Proof point: Business-hours / after-hours routing built into the 14-day install. Same logic on DSK triaging strata vs residential pre-sale.

---

**Objection #7 — "Buyer's agents will sniff out an AI in two seconds and use it against me"**

Underlying concern: peer-credibility. Buyer's agents are sophisticated and the principal doesn't want to look amateur to them.

Response: *"Built the escalation for exactly that. Zoe captures the property, takes the brief, says 'principal will call you back inside an hour' — then SMS-fires you with the transcript. Buyer's agents never get a full AI conversation. They get a fast-handoff receptionist who never drops their request."*

Bridge: *"How many buyer's-agent calls would you say you take in a week vs miss?"*

Proof point: Trigger-word escalation — "buyer's agent", "advocate", "off-market" all flag immediately. Tunable in the monthly prompt update inside A$1,200/mo.

---

**Objection #8 — "My agents own their phones — I can't force them to forward calls to some AI"**

Underlying concern: organisational politics. Agents are independent contractors and won't accept anything that touches their personal mobile.

Response: *"Don't. Run Zoe on the office line and the listing-board number — that's where orphan calls come in. Each agent keeps their personal mobile. Zoe just stops the office number ringing out at 6:30pm when no one's there to grab it."*

Bridge: *"What number do you put on your for-sale boards — agent direct, or the office?"*

Proof point: Twilio forwards from your existing office line, not the agents'. No phone-system surgery on the agent end.

---

**Objection #9 — "We're a relationships business. AI doesn't build relationships."**

Underlying concern: brand identity. Boutique RE sells personal service as the differentiator and AI feels like the opposite of that.

Response: *"Relationships are built at the open home, the listing pres, the auction. Zoe's job is to make sure no one trying to start a relationship bounces to voicemail. The relationship still happens — you just don't lose the front door."*

Bridge: *"How many enquiries from your last open home turned into actual conversations vs ones that went cold?"*

Proof point: Tier 2 Knowledge per-listing recall — Zoe knows your 5 active listings (price guide, inspection times, contract terms). Adds to the relationship; doesn't replace it.

---

**Objection #10 — "I deal with stuff under FIRB / off-market / vendor confidentiality. AI handling that is a legal exposure."**

Underlying concern: compliance and confidentiality. Real estate has specific disclosure rules and they don't want a bot accidentally divulging vendor info.

Response: *"Zoe never volunteers off-market detail. She captures the enquiry and passes it to you — doesn't quote prices on confidential listings, doesn't confirm vendor names, doesn't discuss FIRB. Caller pushes, she escalates. Disclosure decisions stay yours."*

Bridge: *"What's the most sensitive enquiry you've had to handle in the last month? Walk me through what should happen if that ring came in at 8pm."*

Proof point: Prompt-locked information boundaries — configured Day 4-5 of the install (the most custom part per `HOW-IT-WORKS.md`). QA-tested across five scenarios on Day 8-10.

---

## 3. Dental Practice

1-3 chair owner-operator. Recall = lifeblood (6-monthly cycles). HICAPS / fund-cover queries dominate phones. Privacy Act + state Health Records obligations.

---

**Objection #11 — "If your AI gives a patient dental advice and they get hurt, who's wearing it?"**

Underlying concern: malpractice exposure. There's a documented US case where a receptionist gave dental advice and the practice got sued. They're imagining that scenario with an AI.

Response: *"Zoe never gives clinical advice. Locked to triage only — book, reschedule, take details, escalate. Caller asks 'is this an abscess', her line is 'I can't diagnose over the phone, but I can get you in today. What time suits?' Same boundary your front desk should already have."*

Bridge: *"What's your current process when a caller describes pain on the phone?"*

Proof point: "No clinical advice" boundary locked at install Day 4-5. QA-tested Day 8-10 with "urgent" and "complaint" scenarios. Every call recorded — auditable trail if anything ever surfaces.

---

**Objection #12 — "Patient data — phones — Privacy Act. Where does this sit?"**

Underlying concern: privacy compliance. AU dental practices fall under the Privacy Act 1988 + state health records acts. They want to know data handling specifically.

Response: *"All call data sits on Australian infrastructure — Twilio AU, GHL AU residency. Recordings 90 days unless you ask longer. Patients hear 'this call may be recorded' at the start, same as your bank. I send you the data-handling spec in writing before install — your indemnity insurer will want to see it."*

Bridge: *"Does your current phone system record calls today, or is this the first time you'd have audio?"*

Proof point: AU-hosted stack per `HOW-IT-WORKS.md` — Twilio AU + GHL AU sub-account. Spec sendable before any payment.

---

**Objection #13 — "Recall calls are how we keep the chair full. If she screws those up I'm dead."**

Underlying concern: business-critical workflow. Dental P&L hinges on recall conversion. They don't want this experiment running on the most important call category.

Response: *"Don't run her on recall outbound. Tier 1 is inbound-only — catches missed calls, books new patients, fills cancellations from your waitlist. Recall outbound is a separate decision down the track, after 60 days on safer ground."*

Bridge: *"What's your current recall conversion — is it the limiter, or is it new-patient capture?"*

Proof point: Tier 3 Outbound is parked per `HOW-IT-WORKS.md`. Tier 1 is inbound-only. Recall stays under your team. Outbound revisited only after 60+ days of proven inbound.

---

**Objection #14 — "She has to handle HICAPS / private health fund queries — half my calls are 'is this covered?'"**

Underlying concern: insurance complexity. Patients ask about gap fees, item codes, fund coverage — and getting it wrong creates billing fights.

Response: *"Zoe captures the fund, captures the item code if they know it, books the consult, says 'we'll confirm exact gap at the appointment.' Never quotes a final number — that depends on items billed on the day. Exactly what your front desk should say. She just doesn't make exceptions when it's busy."*

Bridge: *"What's the standard line your front desk uses when someone asks about cover?"*

Proof point: Tier 2 Knowledge — insurance is one of four dental categories in `HOW-IT-WORKS.md` (treatment Q&A, insurance, recall, dietary). A$300/mo each, opt-in after Tier 1 is proven.

---

**Objection #15 — "My patients are 60+. They'll know it's AI in three seconds and tell me about it."**

Underlying concern: demographic mismatch. University of Sydney research shows 65+ Australians are uncomfortable with AI phone calls. They've seen the comments online.

Response: *"Some will. So Zoe identifies as 'the receptionist' or 'an automated booking assistant for the practice' — your call. Honesty kills the surprise. Patients who hate it ask for a human; her line is 'no worries, I'll have someone call you back inside the hour.' You lose nothing — they were going to voicemail anyway."*

Bridge: *"What percentage of your patient base would you say is 65+?"*

Proof point: Configurable identity at install Day 4-5 — assistant or receptionist intro, owner's call. Tuned during install based on your patient mix.

---

## 4. Aesthetic Clinic / Beauty

1-2 practitioner clinic (RN or doctor). Injectables, hydrafacials, laser, skin. AHPRA Sept 2025 guidelines: in-person/video consult before any injectable, no async prescribing, S4 brand names blocked.

---

**Objection #16 — "AHPRA says I have to do an in-person or video consult before any injectable. Your AI can't book a 'botox appointment' — it's illegal."**

Underlying concern: regulatory exposure. The Sept 2025 AHPRA guidelines are explicit and they don't want an AI booking flow that breaches them.

Response: *"Correct — and Zoe's prompt is built for that. She books a consultation, never a treatment. Phrasing's 'I can get you in for an initial consult with [practitioner] — that's where suitability gets assessed, treatment appointments are booked from there.' Two-stage funnel, AHPRA-compliant by design."*

Bridge: *"How are you currently triaging the 'how much for botox' phone calls?"*

Proof point: "Consult first, treatment second" prompt logic locked Day 4-5. Mirrors AHPRA Sept 2025 language. Auditable in install handover.

---

**Objection #17 — "TGA rules mean I can't advertise prescription products by name. Will your bot say 'Botox' on a phone call?"**

Underlying concern: TGA advertising compliance. S4 prescription medicines (incl. cosmetic injectables) cannot be advertised to consumers by name. A bot saying "Botox is $X per unit" is a breach.

Response: *"No. Zoe's prompt blocks brand names and prices. Caller says 'how much for Botox', her line is 'I can't quote treatment names or prices over the phone — TGA rule. I can book you a consult where the practitioner can talk through options.' Compliant version of what your front desk should already say."*

Bridge: *"Does your current website have the same compliance lock, or is your phone the only exposed point?"*

Proof point: S4 brand names blocked at prompt level — generic terms only. QA-tested Day 8-10 with the "price-shopping injectable caller" scenario.

---

**Objection #18 — "My patients pay $800-$3,000 a visit. They expect concierge, not a bot."**

Underlying concern: high-end patient expectation. The clinic positions on premium service and a robot answering feels downmarket.

Response: *"Premium clinics run Zoe on after-hours overflow — the 7pm Sunday, the lunchtime ring while reception's on a consult. Business hours, your front desk owns the phone. Patient experience doesn't change; the after-hours enquiry just stops disappearing into voicemail."*

Bridge: *"What hours do you currently have a human picking up the phone?"*

Proof point: Daytime → your line, after-hours → Zoe. Same architecture running on Eonia (Peter's clinic). Beauty founding slot open.

---

**Objection #19 — "Insurance and AHPRA reviews are nightmare fuel. If she misrepresents a treatment outcome, that's my registration."**

Underlying concern: practitioner registration risk. AHPRA can suspend practitioner registration for misleading claims about cosmetic outcomes — and they've been actively prosecuting since the 2025 guidelines.

Response: *"She doesn't represent outcomes. Prompt blocks any 'will this work for me' answer — redirects to the consult every time. Line is 'outcomes vary by patient, the practitioner needs to assess in person.' Same answer your nurse should give. She just gives it 100% of the time."*

Bridge: *"How do you currently handle the 'will Botox fix this' phone call when you're not on the floor?"*

Proof point: Outcome-claim block in install prompt. 90-day call recording = AHPRA audit trail. Worked through on Eonia install (Case Study #2).

---

**Objection #20 — "Under-18 cosmetic rules with 7-day cooling-off — I'm not letting a bot near that workflow."**

Underlying concern: minor-patient safety. AHPRA's 7-day cooling-off period for under-18s is enforced and any process error triggers AHPRA notification.

Response: *"Zoe doesn't book minors at all. Her screening line is 'are you 18 or over' — if no, captures details and escalates immediately, no booking made. Every under-18 enquiry goes to your team direct, cooling-off paperwork stays with the practitioner."*

Bridge: *"How often do you actually take under-18 cosmetic enquiries — is it 1 a week, 1 a month?"*

Proof point: Hard age gate at install Day 4-5. No booking logic for under-18s — escalation only. Mirrors AHPRA Sept 2025 minors section.

---

## 5. Cleaning / Trades

1-5 vehicle service, owner-on-tools. AU tradies lose ~A$42K/yr to missed calls. Likely tried Sophiie/Johnni/TransferToAI and quit because the install never finished. ServiceM8/Jobber/Simpro.

---

**Objection #21 — "I tried Sophiie / Johnni / TransferToAI and it never went live properly"**

Underlying concern: been-burned cynicism. They paid $99-$300, spent 30 hours configuring, gave up.

Response: *"Same story I've heard ten times. Reason it didn't go live is no one was building it for you. Self-serve is cheap because it doesn't include a human. Mine includes 14 days of me building, testing, going live. Miss the 14 days and the A$1,500 setup fee is waived."*

Bridge: *"Which one did you try, and what's the part where it actually fell over for you?"*

Proof point: Stacked guarantee #2 — install in 14 days or setup fee waived. Day-by-day playbook in `HOW-IT-WORKS.md`. 15-25 founder hours per install — Peter's, not yours.

---

**Objection #22 — "If she quotes wrong on a job and I have to honour it, I lose money"**

Underlying concern: pricing exposure. They've heard horror stories about AI quoting jobs at the wrong price.

Response: *"Zoe doesn't quote final price. Captures scope — bedrooms, condition, suburb, urgency — gives a starting-from range or 'I'll have [you] confirm by SMS within the hour.' At DSK we run starting-from only. Final quote happens when you call back from the ute."*

Bridge: *"How are you handling pricing on the phone right now — full quote, ballpark, or 'I'll come look first'?"*

Proof point: At DSK we measured 10 missed-call recoveries/month × A$300 = A$3,000/mo recovered (`HOW-IT-WORKS.md`). "Starting from" + SMS-back, not on-call hard quotes.

---

**Objection #23 — "Half my callers don't speak English well. She'll never cope with a strong accent."**

Underlying concern: real-world Australian phone traffic. Tradies take calls from migrant homeowners, strata managers with thick accents, etc. They've heard early voice AI butcher these calls.

Response: *"2026 voice models handle accents better than most humans on a Friday arvo. Where she struggles, the prompt's tuned to ask once 'sorry — could you say that again?' Still can't get it, she escalates with 'I'll have someone call you back inside an hour.' She doesn't mishear and book a job at the wrong address."*

Bridge: *"What suburb's most of your work in?"*

Proof point: Retell voice model trained on AU speech + escalation fallback for low-confidence audio. QA-tested across accent variability.

---

**Objection #24 — "I'm on ServiceM8 — does it actually drop the job in, or is it another inbox to check?"**

Underlying concern: existing-stack pain. ServiceM8 is the centre of their world; anything that doesn't push into it is friction.

Response: *"Pushes straight into ServiceM8 as a job card — caller's details, address, scope, recording attached. Your dispatcher sees it like any other booking. No second inbox. Same on Jobber and Simpro."*

Bridge: *"What does your dispatcher do with a missed call right now — call back, SMS, leave it?"*

Proof point: ServiceM8 + Jobber + Simpro all on the integration list in `HOW-IT-WORKS.md`. CRM connection happens install Days 6-7. DSK runs the same architecture.

---

**Objection #25 — "I'm a one-man-band. $1,200/month is a lot when I'm doing $250K turnover."**

Underlying concern: small-business cash flow. Sole-trader cleaner or sparkie at the bottom of the ICP can't carry the price.

Response: *"At $250K, maths is tighter. Founding rate's A$800/mo for life if your vertical's open — cleaning's gone to DSK. Honest answer: under 8-10 missed calls a week, you're too small for this right now. Count your missed calls this week, text me Friday. Under 5, skip it. Over 8, maths flips."*

Bridge: *"Want me to send a 60-second audit template — text me your numbers Friday and I'll tell you yes or no, no pitch?"*

Proof point: Walk-away discipline per `SALES-PREP-PACKAGE.md` — don't take a client whose missed-call number is too low. Honesty preserves the relationship; half come back in 6 months.

---

## The "I tested 5 AI receptionists" universal opener

For any prospect who has tried Sophiie, AiDial, Chime, Smith.ai or TransferToAI. First move after "anything else worth knowing?".

**30-word version**
> *"Tested every one I could find before I built mine — Sophiie, Chime, Smith.ai, the lot. Same failure every time: real question lands, AI flounders. Mine's done-for-you, not config-it-yourself."*

**60-word version**
> *"Yeah — same story. Tested Sophiie, AiDial, Chime, Smith.ai, TransferToAI. Failure mode's identical: nice voice, then a real question lands and the AI has nothing. Reason isn't the tech — voice is solved. Reason is no one builds it for you. They sell software with a config screen. Mine's 14 days of me building it, no config screen on your end."*

**90-word version**
> *"Tested seven of them. Sophiie, Chime, Johnni, Smith.ai, TransferToAI, Hooroo, AiDial. Each one took a real call from a fake job, each one fell apart inside two minutes. Voice was fine. The break was always the same: prompt's generic, no one built it for the actual business, edge case lands and there's nothing behind the voice. So I built mine the opposite — 14-day install, I do the build, I train her on your call recordings, and I refund the setup if she doesn't deliver in 30 days. That's the only difference that matters."*

---

## Vertical-specific demo flows (what Peter dials live)

3 min product + 1 min dialling, mirroring the prospect's vertical.

**Restaurant** — *"Booking for six Saturday 7:30, one gluten-free, one vegetarian. Got anything that works?"* → Zoe captures party + dietaries, confirms, SMS lands, logs to SevenRooms / NowBookIt.

**Boutique RE (buyer's agent)** — *"Buyer's agent on the 4-bed in Mosman — can the principal call back this afternoon? My buyer's keen."* → Zoe captures + escalates within 60 seconds. SMS fires to Peter's phone in front of the prospect.

**Dental (fund query)** — *"HCF top hospital, want to book a check-up and clean. What's the gap on items 012 and 114?"* → Zoe books, gives the compliant non-quote ('we'll confirm at the appointment'), no clinical advice.

**Aesthetic clinic** — *"After Botox in my forehead. What's it cost, anything Wednesday?"* → Zoe books a consult, not a treatment. No price. No S4 brand name. AHPRA-compliant two-stage funnel.

**Cleaning / trade** — *"Need a pre-sale clean for a 4-bed in North Bondi by Friday."* → Zoe captures scope, gives starting-from range only, commits to SMS hard quote within the hour, pushes to ServiceM8 as a job card.

---

## Sources

Research conducted 2026-05-08.

**AHPRA / TGA / AU regulatory:**
[AHPRA Sept 2025 guidelines](https://www.ahpra.gov.au/News/2025-09-02-New-guidelines-for-cosmetic-procedures.aspx) · [AHPRA June 2025 announcement](https://www.ahpra.gov.au/News/2025-06-03-New-cosmetic-procedure-guidelines.aspx) · [AHPRA performing non-surgical](https://www.ahpra.gov.au/Resources/Cosmetic-surgery-hub/Cosmetic-procedure-guidelines.aspx) · [Clayton Utz](https://www.claytonutz.com/insights/2025/june/navigating-the-2025-ahpra-guidelines-on-cosmetic-procedures-heres-what-you-need-to-know) · [Lexology](https://www.lexology.com/library/detail.aspx?g=4083bcb8-a330-42eb-a25c-376408df4b92) · [The Conversation](https://theconversation.com/new-rules-for-cosmetic-injectables-aim-to-make-the-industry-safer-will-they-work-257898) · [ABA TGA Compliance](https://australianbeautyassociation.org/tga-compliance-made-simple-a-guide-for-beauty-salons/) · [Aesthetic Medical Practitioner — S4](https://aestheticmedicalpractitioner.com.au/features/cosmetic-practice/s4-cosmetic-injectables-confusion-re-buying-and-storage/)

**Dental / patient privacy:**
[CDA — AI in dentistry HIPAA risks](https://www.cda.org/newsroom/endorsed-services/ai-in-dentistry-what-are-the-hipaa-violation-risks/) · [MedPro — Answering Machine Lawsuit](https://medprodental.com/practice-more-safely/how-a-dental-offices-receptionist-and-answering-machine-led-to-a-lawsuit) · [Valory AU dental](https://www.valory.com.au/resources/ai-receptionist-for-dental-practices) · [Arini recall rate](https://www.arini.ai/blog/improve-patient-retention-recall-rate-dental-clinics) · [DentalAIAssist HIPAA Guide](https://dentalaiassist.com/blog/ai-receptionists-and-hipaa-complete-guide-to-security-privacy-and-compliance/)

**Restaurant:**
[Slang AI](https://www.slang.ai/) · [Yelp ROI AI answering](https://business.yelp.com/resources/articles/ai-answering-services/?domain=restaurants) · [Hostie after-hours AI](https://hostie.ai/resources/after-hours-ai-for-restaurant-reservations-auto-confirm-setup) · [Backofhouse — Human Touch](https://backofhouse.io/resources/let-ai-handle-your-restaurant-phones-without-losing-the-human-touch) · [SevenRooms AI](https://sevenrooms.com/platform/artificial-intelligence/) · [NowBookIt AI Insights](https://www.nowbookit.com/tools-and-tips/now-book-it-insights-restaurant-reporting/) · [ALM 10 Best 2026](https://almcorp.com/blog/best-ai-receptionist-products-2026/)

**Real estate:**
[Phonely RE](https://www.phonely.ai/industries/real-estate-agents-ai-answering-service) · [Voice.ai property mgmt](https://voice.ai/hub/ai-voice-agents/best-answering-service-for-property-management/) · [Crescendo conversational AI](https://www.crescendo.ai/blog/conversational-ai-for-real-estate)

**Cleaning / trades:**
[Virtual Reception AU](https://www.virtualreception.com.au/blog/5-proven-ways-missed-calls-lose-jobs-for-trades-businesses/) · [Allclean — $80K/yr](https://allclean.app/blog/missed-calls-cost-cleaning-businesses) · [Sophiie trades](https://www.sophiie.ai/industries/trades) · [Yes AI tradies](https://yesai.au/ai-for-tradies/) · [Get Fully Booked AU](https://getfullybooked.au/post/ai-answering-service-australia) · [TransferToAI 11 Best AU](https://transfertoai.com/blog/best-ai-answering-services-australia) · [Cleverize AU](https://www.cleverize.ai/blog/australian-ai-receptionist) · [Whirlpool Forum](https://forums.whirlpool.net.au/archive/1865154)
