# Stark Industries — case study profile

The guided project's organisation. Lessons 10 to 16 build an ISMS for it
clause by clause, so this file is the single source of truth for who they are.
Stated facts stay separate from my assumptions, same convention as the Oscorp
profile.

**Status:** established at module 12, lesson 9.

## What the brief states

| Attribute | Value |
| --- | --- |
| Name | Stark Industries Inc. |
| Location | New York City, New York, USA |
| Product | SaaS platform offering marketing automation tools for small businesses |
| Hosting | Amazon AWS |
| ISMS scope | The development, deployment and management of the Stark Industries platform — strictly the newly developed SaaS application |
| Driver | Prospective clients require ISO 27001 certification as a condition of procurement |
| Target | ISO/IEC 27001:2022 certification |
| Stated data position | The application does **not** store personally identifiable information — it collects marketing data and provides marketing insights |

### People

| Role | Name |
| --- | --- |
| CEO | Tony Stark |
| Information Security Manager | Happy Hogan |
| Information Security Analyst | James Rhodes |
| Software Developer | Natalia Romanoff |
| IT Infrastructure Engineer | Maria Hill |
| Cyber Security GRC Analyst | me |

**Interested parties named:** Information Security Manager, Information Security
Analyst, IT Infrastructure Engineer, Software Developer, and Amazon AWS.

**My role:** hired by the Information Security Manager to build the ISMS and get
the organisation certified.

## Not yet stated

Headcount beyond the six named · revenue and funding stage · client base and
whether any clients are outside the US · what data the platform actually
processes on behalf of clients · whether there is an office or the team is remote
· existing policies, if any · existing security tooling · other AWS or SaaS
suppliers · whether the company has ever had an incident.

## My working assumptions

Flagged as mine. To be revised as the project states facts.

| Assumption | Reasoning | Confidence |
| --- | --- | --- |
| The platform processes personal data belonging to Stark's *clients* | Marketing automation for small businesses normally involves contact lists, email addresses and behavioural data. "No PII" most plausibly means no PII about Stark's own end users, not that the platform is personal-data-free | **Medium–high, and worth challenging** |
| Stark is a processor, not a controller, for client data | Standard SaaS position | Medium |
| The team is small enough that segregation of duties will be a live problem | Six named people covering dev, infrastructure, security and leadership | High |
| No existing ISMS or formal policy set | The brief says build from scratch | High |
| Clients are primarily US small businesses | Stated market, no international mention | Low — not stated |

## Things to establish early

- **Does the platform process personal data on behalf of clients?** This changes
  control selection, exclusion justifications, and whether GDPR can reach Stark
  through EU-based clients
- **Who performs the internal audit** (clause 9.2) if I am the person who built
  the ISMS
- **The AWS shared responsibility boundary** — what Stark is responsible for
  versus what AWS covers, which drives several Annex A exclusions
