# 01 — Context, scope and requirements

## The organisation (fictional)

**Kestrel Pay Ltd** is a 140-person payment software vendor in Malta. It builds and hosts a card-processing platform for acquiring banks and payment institutions in the EU. Its customers connect through a REST API, and the **Refunds & Card Lookup API** is the service this case looks at.

The case starts when I join as **Information Security Officer** and the Head of Engineering asks three things of me:

1. Bring security into the SDLC before the next PCI assessment.
2. Show where the real risk sits in the code we ship.
3. Get audit-ready evidence that doesn't depend on screenshots taken the night before.

## Scope of this engagement

| In scope | Out of scope |
|---|---|
| Refunds & Card Lookup API source code, dependencies and CI pipeline | Card-present / terminal software |
| The SDLC that produces it: design, code review, testing, release | Data-centre physical controls (the hosting provider's responsibility) |
| Logs and data stores the API writes to | Corporate IT (email, laptops) |

## Requirements the work is measured against

| Source | Why it applies | What it drives here |
|---|---|---|
| **PCI DSS v4.0.1** | The platform stores, processes and transmits cardholder data | Req 3 (protect stored data, no SAD after authorisation), Req 6 (secure development, 6.2.4 attack prevention, 6.3 vulnerability management), Req 11 (testing) |
| **PCI Software Security Framework** — Secure Software Standard and Secure SLC Standard | Kestrel sells payment software to other regulated entities | Secure design, sensitive-data protection, a documented and evidenced secure lifecycle |
| **ISO/IEC 27001:2022** | Kestrel's ISMS is certified | A.8.25 secure development lifecycle, A.8.26 application security requirements, A.8.27 secure architecture, A.8.28 secure coding, A.8.29 security testing, A.8.8 technical vulnerabilities |
| **DORA (EU 2022/2554)** | Kestrel is an ICT third-party provider to financial entities, which push DORA contract terms down to it | Testing, incident notification support, audit rights in contracts |
| **GDPR** | Cardholder names are personal data | Data minimisation, security of processing (Art. 32) |
| **OWASP Top 10 / ASVS** | The engineering team's working vocabulary | Findings are written in OWASP terms so developers act on them |

> The SSF documents are being revised: the Secure Software Standard is now at v2.0 and a Secure SLC v2.0 draft has been out for comment. I cite the control areas here, not requirement numbers. A real engagement would confirm the version the assessor will use.

## Stakeholders I'd work with

Head of Engineering (sponsor) · API team lead and developers · DevOps · QA · Compliance Officer · the external QSA and SSF assessor · the pen test vendor.
