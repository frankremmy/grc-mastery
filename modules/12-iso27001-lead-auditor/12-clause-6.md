# Clause 6 — planning

> Module 12, lesson 12. _The longest clause: risk assessment, risk treatment, the
> Statement of Applicability, and the objectives that make the ISMS measurable._

## How clause 6 breaks down

| Requirement | What it needs | Document? |
| --- | --- | --- |
| 6.1.1 General | Address risks and opportunities | No separate document |
| 6.1.2 Risk assessment | A defined, documented assessment process | **Risk Assessment Process** |
| 6.1.3 Risk treatment | A treatment process, a treatment plan, and the SoA | **Risk Treatment Process and Plan**, **SoA** |
| 6.2 Objectives | Measurable information security objectives | **ISMS Objectives** |
| 6.3 Planning of changes | Changes to the ISMS made in a planned way | No separate document — handled by change management |

This is where most of the time goes, and the lesson is candid about why.

## 6.1.2 — the risk assessment process

ISO doesn't mandate a methodology. NIST and others publish risk frameworks, and
an organisation may already have its own, but the standard doesn't require any of
them. What it *does* require is that the process contains specific elements:

- **Risk acceptance criteria**, and criteria for performing assessments
- Assessments that produce **consistent, valid and comparable results**
- Risks identified in terms of **loss of confidentiality, integrity and
  availability**
- **Risk owners** identified
- Consequences and **likelihood** assessed, and a **risk level** determined
- Risks **evaluated** against the criteria and **prioritised**
- The process **retained as documented information**

**The process designed for Stark has six steps:** asset identification; threat
and vulnerability identification; risk analysis (likelihood × impact); risk
evaluation; risk ownership; documentation of results. Each step maps to one of
the elements above.

**The criteria:**

| Likelihood | | Impact | |
| --- | --- | --- | --- |
| 1 | Rare — exceptional circumstances only | 1 | Negligible |
| 2 | Unlikely | 2 | Minor |
| 3 | Possible | 3 | Moderate |
| 4 | Likely | 4 | Major |
| 5 | Almost certain — e.g. phishing, hostile traffic at the firewall | 5 | Severe — e.g. ransomware that ends the business |

**Risk score = likelihood × impact, maximum 25.**

| Score | Level | Meaning |
| --- | --- | --- |
| 1–6 | Low | Acceptable — monitor |
| 7–14 | Medium | Mitigate or justify |
| 15–25 | High | Unacceptable — treat |

The acceptance thresholds are **management's decision, not the GRC analyst's.**
The analyst proposes; leadership endorses. In practice almost no organisation
chooses to accept high risk on the record, but the endorsement still has to happen.

**Threat sources:** OWASP Top 10, NIST publications, threat intelligence, and
**internal incident history** — the one most often forgotten, and often the most
predictive.

**Outputs:** a risk register, a risk assessment report, an updated asset
inventory, a risk treatment plan, and the SoA. These don't have to be separate
documents — for a small organisation they can live in one spreadsheet — but they
have to exist. Without them the process produces nothing auditable.

### The hidden mandatory document

This is the most useful insight in the lesson. The risk assessment process starts
with *asset identification* — and you cannot identify assets without a defined way
of discovering, recording and classifying them. So an **asset management policy
becomes effectively mandatory**, even though no clause names it.

An auditor reading "step 1: asset identification" will ask how assets are
identified. If there's no answer, that's a nonconformity. The mandatory clauses
require certain documents explicitly, and those documents quietly require others.
That's why an ISMS that looks small from the outside isn't, and why technical
people who read the standard and conclude "this is easy" are usually wrong.

The scale point is worth recording too: two documents — the risk process and the
asset policy — took an experienced practitioner around a week, and in a real
engagement they'd be built with the IT, risk and management teams and endorsed
before use. Short documents are not quick documents.

## The asset management and data classification policy

**Asset types:** information assets (source code, data, documentation); IT assets
and cloud services; applications; personnel and roles. Not drawn from any
standard — agreed between the GRC function, IT and management, and debatable at
the edges (a CI/CD tool could arguably be an information asset). Operational
technology is the common absence for a software company.

**What the policy covers, and where it starts referencing Annex A:**

- **A.5.9 inventory** — every asset recorded with ID, description, type,
  location, owner, classification, threats and vulnerabilities, with a review
  frequency and a named maintainer
- **Asset ownership** — assigned
- **A.5.10 acceptable use** — which references an acceptable use policy that
  doesn't exist yet, so now one has to be written
- **A.5.12 classification**, based on CIA: Confidential, Restricted, Internal Use
  Only, Public
- **A.5.13 labelling** — which doesn't mean a physical label; a classification
  recorded against an asset ID counts
- **Media handling** — encrypt, track, wipe; which requires an encryption policy
- **Asset lifecycle** — through to decommissioning
- Roles, responsibilities and review

Two things this shows. Policies cascade — one document generates the need for
two more. And the policy can be deliberately lean: enough to be certified, then
improved once audited, rather than twenty pages of prescription before anything
is tested.

## The asset register and risk register

**Five assets in scope:**

| ID | Asset | Classification | C | I | A |
| --- | --- | --- | --- | --- | --- |
| A001 | Source code repository | Confidential | High | High | Medium |
| A002 | AWS EC2 production | Restricted | High | High | High |
| A003 | CI/CD pipeline | Confidential | Medium | High | High |
| A004 | Developer laptop | Internal Use Only | Medium | Medium | Medium |
| A005 | Data | Confidential | High | High | Medium |

**The scoping judgement worth noting:** only the developer's laptop is included,
not the infrastructure engineer's. Reasoning: stay tight to the application scope,
and in practice whatever endpoint controls apply to one laptop will apply to all
of them anyway. It's a defensible call either way, and the ISMS process has two
audits to catch it if it's wrong.

Classifications come from the policy's legend and are negotiated with asset
owners rather than imposed. Source code is Confidential because a competitor
copying it ends the business model. Processed data is Confidential even though
the raw inputs are public — the processing is the value.

**Five risks, one per asset:**

| ID | Risk | L | I | Score | Level |
| --- | --- | ---: | ---: | ---: | --- |
| R001 | Unauthorised access to source code | 4 | 5 | 20 | High |
| R002 | Service disruption due to DoS | 3 | 5 | 15 | High |
| R003 | Compromise of deployment pipeline | 3 | 4 | 12 | Medium |
| R004 | Malware infection via phishing | 4 | 3 | 12 | Medium |
| R005 | Unauthorised access or corruption of data | 4 | 5 | 20 | High |

All five are treated by mitigation. Residual score, residual level, owner and
status stay empty until controls are selected and implemented.

**The point the lesson makes about volume:** the risk assessment exists to select
controls, not to enumerate every conceivable scenario. A hundred risk lines would
most likely select the same Annex A controls as five. Another assessor might
write more scenarios and reach the same SoA — and an auditor may ask for more,
which is a conversation, not a failure.

## 6.1.3 — risk treatment

**Objective:** reduce risk to an acceptable level. Not eliminate — *reduce*,
either the likelihood (better access control makes theft less likely) or the
impact (good backups make theft less damaging).

| Option | Meaning |
| --- | --- |
| **Mitigate** | Apply a control to reduce likelihood or impact |
| **Avoid** | Stop the activity that creates the risk. Rare — the lesson's example is a social media campaign cancelled once the brand and staff-welfare impact of it backfiring was laid out |
| **Transfer** | Shift the financial consequence, e.g. insurance. The risk itself remains |
| **Accept** | A documented decision to carry the risk, usually once it's been reduced |

**Control selection considers** risk severity, the nature of the asset and threat,
business context, and **resource availability** — Stark can't absorb a
ten-million-dollar control set, and recommending one is useless. The honest move
is to state the risk plainly and let the organisation decide with full
information.

**Residual risk acceptance belongs to top management.** The CEO isn't in the risk
workshops, but signs off on residual risk — not line by line, but on whatever
exceeds tolerance. **Risk owners implement**: the developer applies secure coding
practices; the GRC analyst supplies the process and the recommendation, not the
code.

**Evidence follows selection.** Related records — residual risk acceptance log,
control implementation logs, internal audit reports — exist because recommending a
control isn't the same as implementing it, and the standard wants proof of the
second.

## The Statement of Applicability

All 93 Annex A controls, each marked in or out of scope with a justification.
Every control selected becomes an implementation obligation with evidence
attached; that's the reason to be deliberate.

**Involve asset owners.** They know controls already in place that the GRC team
doesn't, and people involved in selecting controls are more willing to implement
them. **The counter-risk:** some stakeholders reject everything as out of scope.
The answer isn't argument — it's the risk assessment. Controls are selected
*because* they treat assessed risks, and the certification mandate comes from top
management. The risk register is the source of truth in that conversation.

**The shape of Stark's selections:**

- **Organisational (A.5)** — policies, roles, SoD, asset management, access
  control, supplier agreements and cloud services (AWS), incident management,
  business continuity, legal and contractual requirements, independent review and
  policy compliance **in**. Contact with authorities and special interest groups,
  threat intelligence, project management, ICT supply chain, supplier change
  management, IP rights, records, PII and documented operating procedures **out**
- **People (A.6)** — **all in**. Most organisations already screen staff, use
  employment terms and NDAs, and run some training; including them is cheap to
  evidence through existing HR documents
- **Physical (A.7)** — **all out**, on the basis that no premises are in scope
- **Technological (A.8)** — the bulk **in**: endpoints, privileged access, source
  code access, authentication, malware, vulnerabilities, configuration, logging,
  monitoring, redundancy, networks, cryptography, secure development and coding.
  Data masking, DLP, privileged utilities, outsourced development, change
  management and test information **out**

**Justifications are not prescribed by ISO.** Clear and reasonable is the bar,
and an auditor may still push back. That's normal.

**The warning repeated throughout:** organisations select controls generously and
then discover implementation will take an extra six months or a year. What goes
in the SoA is what the team signs up to deliver.

## The policy cascade

The SoA's "yes" column turns into documents. For Stark: Access Control,
Acceptable Use, Asset Management and Data Classification, Business Continuity and
Disaster Recovery, Cryptography, Data Retention and Disposal, Incident Management,
Monitoring and Logging, Secure Development (SDLC), Supplier Management, and
Training and Awareness.

They follow one template: purpose, scope, principles, the operative sections,
roles and responsibilities, review. A few observations from the walkthrough:

- **Access control** defines principles, user registration and deregistration,
  access review, remote and third-party access, authentication, access to
  sensitive data, and a segregation of duties table
- **BCDR** defines RTO and RPO — and the lesson is explicit that **those numbers
  are not the GRC analyst's to choose**. They come from the infrastructure owner
  and the business. The application isn't mission-critical, but it's sold as
  highly available, which ties straight back to the business objectives in the
  clause 5 policy
- **Incident management** is the incident response plan from module 8 written as
  a policy — SANS-style phases, different wording

Policy writing is rarely done from a blank page in practice. Existing documents
get updated, and new ones get built from examples.

## 6.2 — ISMS objectives

The objectives couldn't have been written earlier: they depend on knowing the
assets, the risks and the controls. The clause wants objectives consistent with
the policy, measurable *where practicable*, informed by the risk assessment,
monitored, communicated, updated, and owned.

Each objective has a **target, a measurement method, an owner and a review
frequency**:

1. All code through secure code review
2. Application penetration testing
3. Platform uptime of 99.9% — achievable on AWS, so the job is not to undermine
   it from the application side
4. All staff trained on security awareness, the policy and acceptable use
5. All critical vulnerabilities addressed
6. Annual internal audit of the ISMS
7. Risk register kept current
8. Achieve ISO 27001 certification

On measurability, the lesson's warning is fair: some auditors want a number on
everything, and some objectives don't take one sensibly. Measurable where it's
practical; don't contort the rest.

## Where I'd push back

**The risk matrix contradicts the score bands.** This is the finding I'd raise
first. The legend sheet carries a likelihood × impact heat map and a separate
score-band table, and they disagree. By the bands, R001 (likelihood 4, impact 5,
score 20) is **High**. On the heat map, the impact-5 / likelihood-4 cell reads
**Low**. The heat map also rates impact 1 / likelihood 1 as Medium. It looks like
the impact rows were inverted when the grid was built.

That isn't cosmetic. Clause 6.1.2 requires the process to produce **consistent,
valid and comparable results**, and two scales in the same methodology giving
opposite answers is precisely what that requirement exists to prevent. The fix is
to rebuild the heat map from the score formula, or drop it and use the bands only.

**The asset register doesn't match the organisation it describes.** The developer
laptop is owned by James Rhodes — the Information Security Analyst — rather than
Natalia Romanoff, the developer. The data asset is owned by "Abed Hamdan", who
doesn't appear anywhere in the Stark brief. And the laptop's location is "Austin
HQ" for a company described as based in New York. A.5.9 requires an inventory
*including owners*; ownership that points at the wrong person or a non-existent
one is a nonconformity, and it also breaks risk ownership downstream.

**Several SoA exclusions contradict the asset register.** These are the ones I'd
expect an auditor to pick at:

- **A.5.32 intellectual property rights — excluded as "no intellectual
  property".** The source code is classified Confidential *specifically* so that
  competitors can't copy it. It's the company's core IP. The register and the SoA
  disagree
- **A.5.5 contact with authorities — excluded because no confidential data is
  stored.** Again, the register classifies two assets as Confidential. And with
  incident management (A.5.24–5.28) in scope, the organisation needs to know whom
  to contact during a DoS extortion attempt or a breach regardless of data type
- **All of A.7 excluded as "no premises in scope", while A004 is a physical asset
  in scope.** A.7.9 security of assets off-premises, A.7.10 storage media and
  A.7.14 secure disposal all apply to a laptop. Excluding the whole theme while
  including a physical device needs at least a partial reversal
- **A.8.32 change management — excluded.** Clause 6.3 is mandatory and the lesson
  itself says change goes through change management. R003 is pipeline
  compromise. A SaaS company deploying through CI/CD without change management in
  its ISMS will struggle to defend that
- **A.8.29 security testing in development** isn't selected, yet the clause 6.2
  objectives include secure code review and an application penetration test —
  which are exactly the evidence for 8.29
- **A.5.34 PII — excluded**, consistent with the brief but resting on the "no
  PII" assumption I flagged at the start of the project and still haven't seen
  tested

**Some inclusions are justified by convenience rather than risk.** Capacity
management and clock synchronisation are in because "IT does this anyway".
That's pragmatic and common, but 6.1.3 expects controls to be *determined from
risk treatment*. A justification that traces back to R002 (availability) is
stronger than "it happens by default", and costs one extra phrase.

None of this says the approach is wrong — the method is sound and the lesson is
honest that justifications are a negotiation with the auditor. It says the
*consistency* between artefacts is where an ISMS gets tested, because an auditor
reads the register, the SoA and the policies side by side.

## My take

**Documents imply other documents.** The asset management insight generalises:
every mandatory artefact has dependencies the standard never names, and an
auditor will follow them. Mapping those dependencies early is how you size an ISMS
project honestly.

**Consistency is the real test.** Most of the issues above aren't errors in any
single document — each document is reasonable on its own. They're contradictions
*between* documents: a source code repo classified Confidential in one place and
an "IP: not applicable" in another; a physical asset in scope and the physical
theme excluded; a heat map and a score table that disagree. That's what clause
6.1.2's "consistent, valid and comparable" is really about, and it's the habit I
want to build: read the register, the SoA and the policies against each other
before an auditor does.

**The risk assessment as source of truth is the line I'll keep.** When a
stakeholder says a control is out of scope, the response isn't opinion — it's
"which risk does that leave untreated?" That turns a negotiation into an analysis,
and it's the same move as the capstone's "does this verdict change what I
recommend?"

**The 6.2 objectives close the gap I raised in clause 5.** There I argued
"achieve certification" shouldn't stand alone as an objective. Here it sits
alongside seven others with targets, measures and owners — which is the right
shape. Certification as a milestone, the other seven as what gets reported at
every management review after it.

**Repo note:** the course's clause 6 documents, policies and spreadsheet are its
material and stay out of the repo. The register, SoA and policy set I write for
Stark go in `deliverables/`.
