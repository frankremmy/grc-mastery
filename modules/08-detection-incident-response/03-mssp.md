# Managed security service provider (MSSP)

> Module 08, lesson 3. Buying detection as a service, and why "we use an MSSP"
> tells you almost nothing on its own.

## Summary

SIEMs are expensive and demand experienced analysts to configure, tune and watch
them around the clock. Small and mid-sized businesses can't resource that, and the
cost is hard to justify. Even large organisations struggle to recruit and retain
experienced analysts.

**MSSPs** — managed security service providers — exist because of that gap.
Specialist firms selling security services, most notably monitoring. They can host
the SIEM, receive your logs, build detection use cases, generate alerts, and
depending on the contract, respond to incidents. For a smaller organisation that's
a sensible answer: pay specialists rather than run an expensive platform you don't
know how to operate.

**And then the caution**, which is the substance of the lesson. It's rare to find
an MSSP doing the job as promised. They look good on paper, and the gaps appear as
soon as you ask difficult questions.

### The cautionary tale

A mid-sized financial services organisation, during a maturity assessment, reported
that a "fantastic" MSSP handled all their monitoring. In a meeting with that MSSP,
asked how much log data they ingested, the representative didn't know and needed to
check with his team. **Two weeks later the answer came back: they had no logs at
all**, because the client had never managed to send them.

The organisation had paid substantial money for two and a half years for a
monitoring service that was never delivered. Security there was run by a head of
IT without deep security knowledge — which is how something like this survives
undetected.

The lesson drawn: **don't trust what the client tells you; validate the claims.**

### How to assess an MSSP arrangement

**1. Logs.** Have all the client's logs actually been onboarded into the MSSP's
SIEM? This establishes how much visibility they have over the environment they
claim to monitor. Ask first.

**2. Detection use cases.** Are they aligned to an industry framework? How often
are they reviewed? And — the point that's easy to miss — **is the client actively
involved?** The MSSP is paid to monitor, but needs constant input from the business
to know whether what it detects is even relevant.

**3. Response.** Assess the process for responding to alerts. Two contract models:

- **MSSP responds to everything**, reporting back what was detected and handled.
  Here you validate the communication: does the business see the alerts, do the two
  parties talk?
- **MSSP responds to some tiers only** — the more common model. Incidents are
  prioritised P1, P2, P3. The MSSP typically handles P3 — lower importance, higher
  volume, straightforward. P1 and P2 shouldn't be frequent, and get escalated to
  the business, where experienced analysts respond.

**4. Alert volume, as a diagnostic.** How many alerts per day?

- 500 or 5,000 — an unmanageable volume; response isn't effective.
- One or two — not enough detection.
- The useful answer sits between. Then take a **sample** of incidents and examine
  what was generated and how it was handled.

Using an MSSP doesn't mean an organisation has good detection and response. Validate,
look deeper, and never accept "everything's fine because we use an MSSP."

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| MSSP | Outsourced security monitoring and services | The realistic answer for organisations that can't staff a SOC |
| Log onboarding | Whether the client's logs actually reach the provider | The first question, and where the worst failures hide |
| Client involvement | Business input on what matters and what's normal | Without it the MSSP detects generically, not relevantly |
| Response model | Who handles which incidents under the contract | Determines where the gap sits when something serious happens |
| P1 / P2 / P3 | Incident priority tiers | The usual split point between provider and client |
| Alert volume | Alerts per day as a health indicator | Too many means no response; too few means no detection |
| Sampling | Examining actual incidents and their handling | Evidence, rather than a description of the process |
| Validating claims | Checking rather than accepting what the client reports | The professional habit this lesson is really teaching |

## Where this shows up in a real job

The cautionary tale is recognisable in structure even at much smaller scale: a
service is paid for, both sides assume the other is handling something, and nobody
checks until someone asks a specific question. Backups configured years ago that
never ran, a monitoring integration that broke after a migration — same shape, same
reason nobody noticed.

The "head of IT running security" detail also matters and it's the part I'd expect
to encounter most often. Smaller organisations frequently have a capable generalist
holding security alongside everything else, and the gap isn't competence — it's
that nobody in the room knows which question to ask.

I haven't worked with an MSSP or assessed one, so this is a framework I'd apply
rather than experience I can claim.

## My take

The two-and-a-half-year story earns its place because of **how cheap the discovery
was**. One question — how much log data are you ingesting — exposed a complete
service failure. It took two weeks only because nobody at the provider knew the
answer, which is itself the finding. That's the real lesson about assessment
technique: the question that reveals most is often the most basic one, and the
reason it goes unasked is that everyone assumes it was answered long ago.

Three things:

**Outsourcing moves the work, not the accountability.** The client remained
responsible for its own security throughout those two and a half years. A contract
transfers activity; it doesn't transfer the consequence of that activity not
happening. That's worth stating plainly to a client who believes the MSSP "handles
security" — and it's the same structure as module 3's point that consultants doing
first-line work are still inside the organisation.

**The alert-volume diagnostic is excellent because it fails in both directions.**
Most metrics only warn about one failure mode. Here, a high number means nobody can
respond and a low number means nothing is being detected — so no answer is
comfortable, and the client has to explain their number rather than present it. I'd
pair it with the report-rate thinking from module 6: volume plus what proportion
was investigated plus what proportion led to action.

**Client involvement is the gap nobody contracts for.** An MSSP knows attack
patterns; it doesn't know that your finance team always runs large exports on the
last Friday of the month, or that the research group legitimately works at 3am
before a submission. Without that context, detection is generic — tuned to what
attacks look like in general rather than what abnormal looks like here. So "how
often do you meet your MSSP and what do you tell them" is a better question than it
sounds, and an arrangement with no regular contact is producing alerts about a
business nobody described.

One thing to add to the assessment list: **what happens when the relationship
ends.** Logs sitting in a provider's SIEM, use cases built in their tenant, and
incident history in their ticketing system are all things a client may not be able
to take with them. Worth asking early, because it's a dependency the client usually
hasn't considered and it's cheaper to fix in the contract than at exit.
