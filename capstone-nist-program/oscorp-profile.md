# Oscorp — client profile

The course's running case-study organisation. Every practical assessment from
module 2 onwards builds on it, so this file is the single source of truth for who
Oscorp is. Facts get added as the course states them; my own assumptions are
marked as assumptions and stay marked until the course confirms or contradicts
them.

**Status:** thin. Established in module 1, lesson 4.

## What the course has stated

| Attribute | Value | Source |
| --- | --- | --- |
| Name | Oscorp | Mod 01 L4 |
| Sector | Bioengineering scientific research | Mod 01 L4 |
| CEO and founder | Norman Osborn | Mod 01 L4 |
| Engagement | I'm a consultant at a Big 4 firm; Oscorp is my first client | Mod 01 L4 |
| Stated driver | A confidential project the CEO is planning | Mod 01 L4 |
| Stated goal | "Pass all cyber security legal and compliance regulations" | Mod 01 L4 |

## Not yet stated

Size and headcount · jurisdictions of operation · legal entity structure ·
revenue · listed or private · what data is actually held · IT estate and cloud
footprint · existing security team, if any · existing certifications · supplier
base · whether it takes payments · whether it runs human trials.

Most of these are needed before any assessment means anything. I'd expect the
course to fill some in as the practicals arrive.

## My working assumptions

Flagged as mine, not the course's. To be revised as facts land.

| Assumption | Reasoning | Confidence |
| --- | --- | --- |
| Research IP is the crown-jewel asset | A bioengineering firm's value is its research; the CEO's stated driver is a confidential project | High |
| Confidentiality outweighs availability and integrity | Same reasoning — though integrity of research data matters more than the CEO's framing suggests | Medium |
| Likely holds health or human-subject data | Bioengineering research commonly involves clinical or genetic data; not stated | Medium |
| Australian context | The course's compliance examples lead with the Australian Privacy Act and CPS 234, and the lesson's HQ render shows a riverside CBD skyline that reads Australian | Low — inference from the course's examples and its set dressing, not a stated fact. Confirm before it changes any assessment |
| Not a payments business | No retail or card-handling activity mentioned | Medium |

## Applicability analysis

The client's goal is to pass *all* regulations. That isn't how compliance works,
so this is my read on what would actually be triggered. Each entry names the
trigger rather than the regulation, because the trigger is what decides.

| Regime | Trigger | Likely applies to Oscorp? |
| --- | --- | --- |
| Privacy law (general) | Holding personal information about identifiable individuals | **Yes** — at minimum employee data; likely research subject data too |
| GDPR | Offering goods/services to, or monitoring, people in the EU; or an EU establishment | **Unknown** — depends on where research subjects and staff are |
| Australian Privacy Act | Being an APP entity operating in Australia | **Unknown** — depends on the jurisdiction question above |
| Health/genetic data rules | Handling health or genetic information, which most privacy regimes treat as a special category | **Likely** — and this is the highest-consequence gap if true |
| PCI DSS | Storing, processing or transmitting cardholder data | **Probably not** — no payment activity indicated |
| CPS 234 | Being an APRA-regulated entity (banking, insurance, superannuation) | **No** — Oscorp is not a financial institution |
| ISO 27001 | Not a law; a voluntary certifiable standard | **Optional** — a choice, not an obligation. Worth separating from the legal items when reporting to the CEO |
| Research/biosafety regulation | Sector-specific rules on research conduct and dual-use material | **Likely, and outside my scope** — flag to the client rather than assess |

## Questions I'd ask at the first meeting

1. What data do you hold, about whom, and in which countries do those people live?
2. Where does the research data physically sit, and who administers it?
3. Does the confidential project have different access rules from everything else — and who can grant an exception to them?
4. Is there an existing security function, or is this the first engagement?
5. Which of your obligations are contractual (grant conditions, research partners, customers) rather than statutory? These usually bite sooner and get overlooked.
6. Who owns risk decisions when the CEO is the data owner?

## Notes

- The CEO is simultaneously the sponsor, the crown-jewel data owner, and the
  person most likely to want an exception. Any access model for the confidential
  project has to hold against its own sponsor.
- "Pass all regulations" should be reframed with the client early. The
  applicability analysis above is the deliverable that does it.
