# Frank Remmy — GRC Portfolio

Governance, risk and compliance work built while completing the **Cyber Security
GRC Mastery** course and its **ISO 27001 Lead Auditor** track.

I'm a support engineer moving into security. Most of what GRC produces — risk
registers, control assessments, policies, programme roadmaps — never shows up in
a CTF writeup, so this repo is where that work lives in the open. Every
deliverable is my own answer, written **before** I saw the course solution, and
where a solution exists I've recorded where I agreed with it, where I didn't, and
why.

Longer write-ups go on [frankremmy.com](https://frankremmy.com).

---

## Start here

The five pieces that best show how I work.

| | Artefact | What it shows |
| --- | --- | --- |
| 1 | **[NIST CSF assessment](deliverables/capstone-oscorp-nist-assessment.xlsx) and [three-year security programme](deliverables/capstone-oscorp-security-program.md)** | 98 controls scored against interview notes, a roadmap sequenced by dependency rather than severity, and a line-by-line comparison with the model answer |
| 2 | **[Enterprise incident response plan](deliverables/08-oscorp-incident-response-plan.md)** ([Word](deliverables/08-oscorp-incident-response-plan.docx)) | A plan built on ENISA's incident management guide, with NIS2 Article 23 and GDPR notification timelines — rebuilt from an Australian template once I saw the jurisdiction was wrong |
| 3 | **[FAIR calculator](deliverables/11-fair-calculator.xlsx) and [phishing risk quantification](deliverables/11-oscorp-phishing-quantification.md)** | My own FAIR model, with secondary loss modelled properly and a sensitivity sheet; puts a security investment's break-even at an 18% risk reduction |
| 4 | **[Third-party supplier assessment](deliverables/09-horizon-labs-assessment.md)** | Reading a SaaS supplier's questionnaire for what it actually evidences, and what the client's own questionnaire forgot to ask |
| 5 | **[ISO 27001 ISMS build — Stark Industries](modules/12-iso27001-lead-auditor/stark-industries-profile.md)** *(in progress)* | Building an ISMS clause by clause, including the [risk assessment, treatment and SoA work](modules/12-iso27001-lead-auditor/12-clause-6.md) and the inconsistencies between them an auditor would find |

---

## Case studies

### Oscorp — running client engagement

A bioengineering and pharmaceutical research firm with a marketed medicine,
research IP as its crown jewel, and no security function. Most module
assessments build on it. Client profile: [`oscorp-profile.md`](capstone-nist-program/oscorp-profile.md).

| Artefact | Area | Status |
| --- | --- | --- |
| [CIA triad assessment](deliverables/02-cia-triad-assessment.md) | Risk | My answer |
| [Audit programme](deliverables/03-oscorp-audit-program.md) | Audit | My answer |
| [Asset management process and CMDB design](deliverables/04-oscorp-asset-management.md) | Asset management | Compared with solution |
| [IAM recommendations](deliverables/05-oscorp-iam-assessment.md) | Identity and access | Compared with solution |
| [Simulated phishing platform evaluation](deliverables/06-oscorp-phishing-platform.md) | Awareness | Compared with solution |
| [Insider threat programme](deliverables/07-oscorp-insider-threat-program.md) | Data security | Compared with solution |
| [Incident response plan](deliverables/08-oscorp-incident-response-plan.md) | Detection and response | My answer |
| [Vulnerability management recommendations](deliverables/10-oscorp-vulnerability-management.md) | Vulnerability management | My answer |
| [FAIR phishing quantification](deliverables/11-oscorp-phishing-quantification.md) | Risk quantification | Self-directed |
| [NIST CSF assessment](deliverables/capstone-oscorp-nist-assessment.xlsx) · [Programme and roadmap](deliverables/capstone-oscorp-security-program.md) | Capstone | Compared with solution |

### Horizon Labs — Oscorp's SaaS supplier

| Artefact | Area | Status |
| --- | --- | --- |
| [Supplier security assessment](deliverables/09-horizon-labs-assessment.md) | Third-party risk | Compared with solution |

### Stark Industries — ISO 27001 guided project *(in progress)*

A small New York SaaS company seeking certification for one product. Profile:
[`stark-industries-profile.md`](modules/12-iso27001-lead-auditor/stark-industries-profile.md).
Notes so far cover [scope](modules/12-iso27001-lead-auditor/10-clause-4.md),
[leadership](modules/12-iso27001-lead-auditor/11-clause-5.md) and
[planning](modules/12-iso27001-lead-auditor/12-clause-6.md). My own ISMS document
set will follow in `deliverables/`.

### Standalone case studies

| Artefact | Organisation | Area | Based on |
| --- | --- | --- | --- |
| [Risk assessment and register](deliverables/02-risk-assessment-wayne.md) ([CSV](deliverables/02-wayne-risk-register.csv)) | Wayne Enterprises | Risk | Course scenario |
| [Three lines of defence case study](deliverables/03-3lod-case-study.md) | Foresight Group Holdings | Audit and governance | Published risk report |
| [Security awareness programme case study](deliverables/06-awareness-case-study.md) | Kentucky Wesleyan College | Awareness | Published programme plan |

Source documents are linked from each case study rather than copied here.

---

## How I work

- **Answer first, compare second.** My response goes in before I see the model
  answer. The comparison records disagreements as well as gaps — a repo of
  transcribed solutions would show nothing.
- **Assumptions are labelled.** Where a case study doesn't state something, I say
  what I assumed and how confident I am, so a reader knows which conclusions to
  challenge.
- **My own tools.** The FAIR calculator, risk register and asset register
  templates are built from scratch rather than copied from course files.
- **Jurisdiction matters.** I'm based in Malta, so where it changes the answer I
  work from EU obligations — GDPR, NIS2, DORA — rather than defaulting to US or
  Australian ones.

---

## Course progress

| # | Module | Notes | Practical | Case study |
| --- | --- | :---: | :---: | :---: |
| 01 | [Introduction to GRC](modules/01-introduction-to-grc/) | ☑ | — | — |
| 02 | [Risk Management](modules/02-risk-management/) | ☑ | ☑ | ☑ |
| 03 | [Audit](modules/03-audit/) | ☑ | ☑ | ☑ |
| 04 | [Asset Management](modules/04-asset-management/) | ☑ | ☑ | — |
| 05 | [Identity and Access Management](modules/05-iam/) | ☑ | ☑ | — |
| 06 | [Security Education and Awareness](modules/06-security-awareness/) | ☑ | ☑ | ☑ |
| 07 | [Data Security and DLP](modules/07-data-security-dlp/) | ☑ | ☑ | — |
| 08 | [Detection and Incident Response](modules/08-detection-incident-response/) | ☑ | ☑ | ☐ |
| 09 | [Third-Party Risk Management](modules/09-tprm/) | ☑ | ☑ | — |
| 10 | [Pentest and Vulnerability Management](modules/10-pentest-vuln-management/) | ☑ | ☑ | — |
| 11 | [Cyber Risk Quantification](modules/11-risk-quantification/) | ☑ | ☑ | — |
| 12 | [ISO 27001 Lead Auditor](modules/12-iso27001-lead-auditor/) | ◐ | ◐ | ☐ |
| — | [Capstone: NIST CSF Program](capstone-nist-program/) | ☑ | ☑ | — |

☑ complete · ◐ in progress · ☐ not started · — not applicable

Each module folder has its own README indexing the lesson notes. Notes follow
one format: summary, key concepts, where it shows up in a real job, and my take.

---

## Repository layout

```
deliverables/            finished artefacts — start here
capstone-nist-program/   NIST CSF capstone notes and the Oscorp client profile
modules/NN-slug/         lesson notes, one file per lesson, indexed by the
                         module README
templates/               reusable blanks: risk register, asset register, audit
                         programme, TPRM questionnaire, lesson notes
reference/               public-domain NIST material used across modules
```

## Frameworks and concepts

NIST CSF · NIST SP 800-53 · ISO/IEC 27001:2022 and 27002 · ISO 31000 · FAIR ·
ENISA incident management · NIS2 · GDPR · MITRE ATT&CK · OWASP · three lines of
defence · CIA triad

## A note on scope

These are my own notes and my own answers. No course videos, slides, templates or
solution files are reproduced here, and the ISO standard's text isn't either —
both are paid products. See [CONTRIBUTING.md](CONTRIBUTING.md) for the rules I
hold the repo to.
