# Enterprise-wide cyber incident response plan — Oscorp

**Module:** 08 — Detection and Incident Response
**Type:** Practical assessment
**Status:** My own answer, written before seeing the course solution.

**Basis.** Structure and terminology follow the **ENISA Good Practice Guide for
Incident Management** (Detection → Triage → Analysis → Incident Response; ENISA
role definitions). Reporting obligations follow **NIS2 Article 23** and **GDPR
Articles 33–34**. An EU framing was chosen deliberately — see Design Notes.

> Values in `<angle brackets>` are Oscorp's to supply. A plan containing invented
> contact details reads as finished while being unusable.

---

## Document control

| Field | Value |
| --- | --- |
| Document | Oscorp Enterprise Cyber Incident Response Plan |
| Version | 1.0 — draft for endorsement |
| Owner | `<Head of IT / Security>` |
| Endorsed by | `<Chief Executive Officer>` |
| Approval date | `<date>` |
| Review | Annually, and after any Significant Incident or Cyber Emergency |
| Related | Scenario playbooks · Crisis Management Plan · Business Continuity Plan · Data Classification Policy · Asset Register · Records of Processing (GDPR Art. 30) |

---

## 1. Purpose and scope

### 1.1 Purpose

This plan sets out how Oscorp manages an enterprise-wide cyber crisis: how an
incident is triaged and categorised, when it escalates, who is convened, who
decides, who must be notified and by when, and how Oscorp communicates.

It is **not** a technical procedure. Containment and eradication steps for
specific incident types live in separate scenario playbooks (section 8). This
document is written for the people who make decisions during a crisis.

### 1.2 Scope

All Oscorp information systems, data and personnel, including Microsoft 365, Azure
and SharePoint; the research data estate and the formulation database; laboratory
systems and networked instrumentation; and third parties with access to Oscorp
systems or data.

### 1.3 Authority and review

Endorsed by the Chief Executive Officer. Once activated, the Incident Manager may
direct response activity and authorise containment that interrupts business
services, within the limits at section 5.3. Reviewed annually and after every
Significant Incident, and exercised at least annually (section 11).

---

## 2. Regulatory applicability

Oscorp must confirm which obligations apply before relying on section 6. An
incident response plan that assumes the wrong regime misses deadlines.

| Regime | Trigger | Oscorp position |
| --- | --- | --- |
| **GDPR Arts. 33–34** | Personal data breach | **Applies** — employee data at minimum; research subject data if held |
| **NIS2 Art. 23** | Being an essential or important entity | **Likely applies** — NIS2 Annex I covers the health sector and manufacture of pharmaceutical products. Oscorp must confirm its classification with `<national competent authority>` and whether it is *essential* or *important* |
| **Medicines regulation** | Incidents affecting the integrity of data supporting a marketed medicinal product | **Likely applies** — obligations to `<national medicines authority / EMA>`; confirm with regulatory affairs |
| **Contractual** | Research partner and customer notification clauses | Confirm per contract |
| **Cyber insurance** | Policy notification conditions | Confirm per policy |

**Action before this plan is endorsed:** legal and regulatory affairs confirm
Oscorp's NIS2 classification, the competent authority and CSIRT to be notified,
and any sector-specific reporting duties. Section 6 is written assuming NIS2
applies; if it does not, those rows are removed rather than left ambiguous.

---

## 3. Definitions and categorisation

**Event** — an occurrence that may become an incident; not confirmed. Repeated
failed logons; antivirus disabled; an unexplained configuration change.

**Incident** — a confirmed breach of security policy threatening confidentiality,
integrity or availability. Ransomware; account compromise; unauthorised
disclosure of research data.

**Crisis** — an incident managed as an organisational emergency, requiring
executive direction and external communication.

### Categorisation

| Category | Description | Team activated | Notification |
| --- | --- | --- | --- |
| **C0 — Event** | Unconfirmed; no established impact | Duty Officer, business hours | Logged |
| **C1 — Minor incident** | Confirmed compromise, minor impact. No personal data, no research IP, no safety implication | Incident Handler; Incident Manager informed | Internal |
| **C2 — Significant incident** | Involves **research IP or formulation data**; **personal data**; multiple systems; a third party; or material service disruption | **IMT activated**; SEMT notified | GDPR and NIS2 clocks assessed immediately (section 6) |
| **C3 — Cyber emergency** | Threatens Oscorp's ability to operate, the integrity of data supporting a marketed medicine, patient safety, or carries imminent public or regulatory exposure | **IMT and SEMT convened** | Regulators, board, external IR provider; communications on standby |

### Escalation triggers

Any of the following raises the category immediately, without discussion:

- Research IP or formulation data accessed, altered or exfiltrated — confirmed or
  suspected
- Personal data exposed — confirmed or suspected
- **Any indication that research or clinical data integrity has been affected.**
  Oscorp's medicine is on the market; this is a potential patient safety and
  pharmacovigilance matter, not only a security one
- Evidence of an insider, or of an attacker holding privileged access
- Any laboratory system or networked instrument affected
- Contact from media, a regulator or law enforcement
- Incident not contained within `<4 hours>` of confirmation

De-escalation requires the Incident Manager's agreement, and the SEMT Chair's at
C2 and above.

---

## 4. Roles

ENISA role names are used so the plan aligns with the vocabulary Oscorp's CSIRT
contacts and external providers will expect.

### 4.1 Incident Management Team — operational

| ENISA role | Held by | Responsibility |
| --- | --- | --- |
| **Duty Officer** | `<rota>` | First receipt of reports and alerts; initial logging |
| **Triage Officer** | `<name>` | Categorisation against section 3; assignment |
| **Incident Handler** | `<name>` | Investigation, containment, eradication, recovery |
| **Incident Manager** | `<Head of IT / Security>` | Directs the response; owns categorisation and escalation decisions |
| **Legal Officer** | `<name / external counsel>` | Regulatory obligations, privilege, law enforcement liaison |
| **Public Relations Officer** | `<name>` | Internal messaging; drafts external statements |
| Research systems liaison | `<name>` | Laboratory systems and research data estate |
| Records | `<name>` | Incident log, evidence register, situation reports |
| Data Protection Officer | `<name>` | GDPR assessment and supervisory authority liaison |
| External IR provider | `<firm, 24/7 number>` | Specialist investigation |

### 4.2 Senior Executive Management Team — strategic

Convened at C3, or at C2 on the Incident Manager's request.

| Role | Held by | Responsibility |
| --- | --- | --- |
| Chair | Chief Executive Officer (Norman Osborn) | Strategic direction; disclosure decisions |
| Deputy Chair | `<Head of IT / Security>` | Bridge to the IMT |
| Chief Scientist | Harry Osborn | Research and scientific integrity impact |
| Legal | `<name>` | Regulatory exposure, liability, insurance |
| Regulatory affairs | `<name>` | Medicines authority obligations |
| Finance | `<name>` | Emergency expenditure |
| Communications | `<name>` | Public and stakeholder communication |
| People and culture | `<name>` | Staff welfare and employment matters |

If the SEMT cannot convene, decision authority rests with `<named delegate>`. A
crisis must not stall because a meeting cannot be arranged.

### 4.3 Conflict of interest

Where an IMT or SEMT member is a subject of the incident — suspected of
involvement, or owner of the asset under investigation — they are **recused for
that incident**:

- Incident Manager a subject → CEO appoints an alternate
- CEO a subject → `<board chair / non-executive director>` chairs the SEMT
- Chief Scientist a subject → research impact assessed by `<alternate senior
  researcher>`

Oscorp's most sensitive asset is owned and administered by its most senior people,
and the organisation has already experienced a suspected insider disclosure. A
plan assuming every responder is disinterested is untested against the case most
likely to need it.

---

## 5. Response process

ENISA phases. Technical steps sit in the playbooks.

### 5.1 Detection

Sources: security monitoring and alerting; staff reports; notification from a
provider, partner or national CSIRT; external report from a researcher, customer
or journalist.

The Duty Officer logs every report. **Reporting is never penalised** — the
interval between something going wrong and someone saying so is the single
largest factor in eventual impact.

### 5.2 Triage

The Triage Officer establishes whether this is an event or an incident, determines
preliminary scope and impact, and **categorises it** against section 3. Spend no
more than **one hour** on initial triage before engaging external expertise.

Do not probe suspected attacker infrastructure from Oscorp's network.

### 5.3 Analysis and response

At C2 the Incident Manager activates the IMT and notifies the SEMT; at C3 both
convene. The IMT works from `<location>`, remote bridge `<details>` — assuming
Oscorp's usual systems may be unavailable (section 10).

Containment takes priority over service availability from C2. **Evidence
preservation runs in parallel with containment, not after it** — isolate rather
than wipe, capture logs before they roll, record chain of custody. Decisions with
business impact beyond `<threshold>` need SEMT approval.

### 5.4 Recovery and closure

Restore once eradication is verified. Stand down on the Incident Manager's
recommendation, authorised by the SEMT Chair at C3. Post-incident analysis within
`<10 working days>` (section 9).

---

## 6. Notification and reporting

**Clocks run from awareness, not from resolution.** At every IMT meeting from C2,
the Legal Officer and DPO confirm whether any threshold has been crossed. This is
a standing agenda item, not a later step.

### 6.1 NIS2 — multi-stage reporting

Applicable if Oscorp is an essential or important entity (section 2). Reports go
to `<national CSIRT / competent authority>`.

| Stage | Deadline from awareness | Content |
| --- | --- | --- |
| **Early warning** | **24 hours** | That a significant incident has occurred; whether suspected unlawful or malicious; whether cross-border impact is possible. Assistance may be requested at this point |
| **Incident notification** | **72 hours** | Update to the early warning; initial assessment of severity, impact and indicators of compromise |
| **Final report** | **One month** | Detailed description, severity and impact, root cause, mitigation applied, cross-border effects |

An intermediate report may be requested by the authority; Oscorp supplies it on
request.

### 6.2 GDPR — personal data breach

| Obligation | Deadline | Owner |
| --- | --- | --- |
| Notify `<supervisory authority>` (Art. 33) unless unlikely to result in risk | **72 hours** from awareness | DPO with Legal |
| Communicate to affected individuals (Art. 34) where high risk to their rights and freedoms | Without undue delay | DPO with Communications |
| Internal breach register (Art. 33(5)) | Always, regardless of notification | DPO |

Where the 72-hour deadline cannot be met, the notification is made late **with
reasons** — not withheld.

### 6.3 Other

| Audience | Trigger | Owner |
| --- | --- | --- |
| `<National medicines authority / EMA>` | Integrity of data supporting a marketed medicinal product affected | Regulatory affairs with Legal |
| Law enforcement | Suspected criminal activity | Legal, on SEMT decision |
| Cyber insurer | Any C2+ incident | Finance — often a condition of cover |
| Research partners, customers | Contractual clauses | Legal with Communications |
| Media | SEMT approval only | Communications |

**Only the designated spokesperson speaks publicly.** Holding statements are
drafted in advance (section 11).

---

## 7. Documentation

Maintained from activation: **incident log** (decisions with rationale, actions,
timings, author); **situation reports** (hourly at C3, `<4-hourly>` at C2, covering
status, category, scope, impact, severity and IMT contacts); **evidence register**
(items, collector, time, custody); **resolution action plan** (actions, owners,
deadlines).

The incident log supports regulatory submissions, insurance claims and the
post-incident analysis. It is written during the incident because it cannot be
reconstructed afterwards.

---

## 8. Supporting playbooks

Ransomware · business email compromise · account compromise · personal data breach
· malware outbreak · denial of service · insider data theft · compromise of
research systems or laboratory instrumentation.

---

## 9. Post-incident analysis

Within `<10 working days>` of stand-down: timeline; what worked; what didn't;
whether categorisation and escalation were correct; **whether every notification
deadline was met**; root cause.

Output is an action register with named owners and dates, tracked to closure, and
**an updated version of this plan.** A review that changes nothing has not been
done properly.

---

## 10. Availability

This plan, the contact list and the playbooks are held in Oscorp's document
management system **and as an offline copy** — printed and in an out-of-band
location `<detail>`. A plan reachable only through systems ransomware has
encrypted is not a plan. Contact details verified `<quarterly>`.

---

## 11. Testing and maintenance

| Activity | Frequency |
| --- | --- |
| Tabletop exercise including IMT **and SEMT** | Annually |
| Contact list verification | Quarterly |
| Plan review | Annually and post-incident |
| Playbook review | Annually |
| Pre-drafted holding statements review | Annually |
| NIS2 / GDPR applicability re-confirmation | Annually, and on any change of activity |

Exercises must include executives. The gap this plan exists to close cannot be
tested in a drill attended only by the security team.

---

## Appendices

A. Situation report · B. Incident log · C. Resolution action plan · D. Evidence
register · E. Contacts — IMT, SEMT, national CSIRT, supervisory authority,
medicines authority, external IR provider, legal, insurer · F. Pre-drafted holding
statements · G. NIS2 early warning submission template

---

# Design notes

Not part of the plan — my reasoning.

**Why an EU basis.** The first draft of this plan used an Australian government
template. The structure transferred fine and the *regulatory spine did not*, which
is the part of an incident response plan that carries real consequence. Reporting
deadlines are jurisdictional, and a plan built on the wrong ones produces a
well-organised response that misses a statutory notification. So this version is
built on ENISA's incident management guidance for structure and vocabulary, with
NIS2 and GDPR as the notification backbone.

**The multi-stage NIS2 reporting is the distinctive EU element**, and it changes
the shape of the plan. A single 72-hour deadline can be handled as a task. A
24-hour early warning means the *first day* of an incident includes a regulatory
submission — while the facts are still unclear. That is why triage is time-boxed
to an hour and why regulatory assessment is a standing agenda item rather than a
later step.

**Section 2 exists because applicability is not assumed.** NIS2 Annex I covers the
health sector and pharmaceutical manufacture, so Oscorp is likely in scope — but
"likely" is not a basis for a plan. Legal confirms classification, competent
authority and CSIRT before endorsement. This is the same applicability discipline
as the Oscorp regulatory analysis in module 1: comply with what is triggered,
not with everything named.

**Why this plan is not technical.** Oscorp's stated problem is no procedure for
engaging senior managers during a crisis — a decision and communication gap.
Module 8 lesson 4 separates the enterprise plan from scenario playbooks, and the
common failure is one document attempting both.

**Three escalation triggers are Oscorp-specific.** Research IP or formulation data;
any indication that research data *integrity* is affected; anything touching
laboratory systems. The integrity trigger matters most — the medicine is marketed
and has already drawn press attention over side effects, so an incident affecting
the supporting data is a patient safety matter. A security-only response to that
would be the wrong response.

**The conflict of interest clause** is adapted from Carnegie Mellon's published
plan, which specifies what happens when the responder is themselves a person of
interest. At Oscorp the crown jewel is owned by the Chief Scientist and sponsored
by the CEO, and there has already been one suspected insider disclosure.

**Evidence preservation sits in parallel with containment.** The instinct under
pressure is to wipe and rebuild, which destroys the basis for any regulatory
submission, insurance claim or prosecution.

**Placeholders are visible on purpose.** Contacts, thresholds and authority names
are Oscorp's to supply. A plan with invented details reads complete and cannot be
used.

**Next step beyond the document.** A tabletop with the SEMT within `<30 days>` of
endorsement. Until then the plan is an untested hypothesis, and the problem it
addresses — executives not knowing how to engage — is only solved once they have
practised it once.

## Sources

- ENISA, *Good Practice Guide for Incident Management* —
  <https://www.enisa.europa.eu/sites/default/files/publications/Incident_Management_guide.pdf>
- ENISA, Incident response topic — <https://www.enisa.europa.eu/topics/incident-response>
- European Commission, *NIS2 Directive FAQs* (reporting stages and deadlines) —
  <https://digital-strategy.ec.europa.eu/en/faqs/directive-measures-high-common-level-cybersecurity-across-union-nis2-directive-faqs>
- Directive (EU) 2022/2555 (NIS2) — <https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A32022L2555>
