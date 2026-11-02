# Clause 7 — support

> Module 12, lesson 13. _Resources, competence, awareness, communication and
> documented information — one new document, and most of the rest already done._

## What clause 7 asks for

Clause 6 planned everything. Clause 7 makes sure the organisation has what it
needs to deliver the plan.

| Requirement | What it needs | Where Stark covers it |
| --- | --- | --- |
| 7.1 Resources | The resources to establish, run and improve the ISMS | Roles document, policies, budget decisions |
| 7.2 Competence | People doing ISMS work are competent, with **evidence** | **Competence Management and Awareness Record** — new |
| 7.3 Awareness | People know the policy, their contribution, and the consequences of not conforming | Training and Awareness Policy; 6.2 objective on staff training |
| 7.4 Communication | What, when, with whom and how to communicate | The communication sections in each policy |
| 7.5 Documented information | Created, identified, reviewed, approved and controlled | The document control table on every document |

Most of the clause is satisfied by work already done. The document control table
on the front of each ISMS document *is* the 7.5 answer — identification,
versioning, review, approval. That's why it was there from the first document.

## The competence record

**Purpose and scope**, then a definition of competence. It's established through:

- Formal education and certifications
- Professional experience and skills
- Completion of security training and awareness programmes
- **Role-specific requirements** — the line that matters most. Some roles need
  skills that no degree or general course provides, such as training on a
  particular application

**The record table** — name, role, required competencies, evidence, training
completed, review date:

| Role | Required competence | Training |
| --- | --- | --- |
| CEO | ISMS leadership, risk oversight | ISMS awareness |
| Information Security Manager | Security governance, compliance | ISO 27001 lead auditor training |
| Security Analyst | Monitoring, incident response | Incident response training |
| Developer | Secure coding, threat modelling | Secure coding, OWASP Top 10 |
| IT Infrastructure Engineer | Network security, cloud configuration | AWS security training, network hardening |
| GRC Analyst | Risk assessment, compliance reporting | ISO 27001 awareness, risk management |

The CEO needs to understand what the ISMS is for, not how to audit it. The
security manager is accountable for the build, so needs to know how one is built.
Each role's requirement traces back to something earlier: the analyst's incident
response training to the incident management policy, the developer's OWASP
training to the secure development policy and R001.

**Competence maintenance and review** close the document: annual review, plus
review after role changes, new requirements, significant incidents or audit
findings.

### The judgement calls in competence

**ISO doesn't define what counts as evidence.** Implementers and auditors decide.
The lesson's experience from audits: people have offered webinars and reading
articles as evidence. That's evidence of a sort, and certifications aren't proof
either — passing a multiple-choice exam says less about ability than people
assume. It's subjective, and there are no hard rules.

**Be wary of auditors who insist a role requires a specific certification.** The
infrastructure engineer's requirement is written as "AWS security training"
rather than "AWS certification" deliberately. Training is broader, leaves room for
different courses, and doesn't pretend a certificate equals competence.

**Involve the people.** Show them the tasks their role carries under the ISMS and
ask whether they feel competent. They're the domain experts, and they can ask for
the training they need rather than having it assigned.

## Where I'd push back

**The evidence column mostly isn't evidence.** Clause 7.2 requires the
organisation to *retain documented information as evidence of competence*. Entries
like "ISO 27001 knowledge", "AWS knowledge" and "SDLC knowledge" are claims about
competence, not evidence of it. Evidence is a certificate, a training completion
record, a CV entry, a supervised piece of work. The column should point at
something an auditor can look at.

**The GRC Analyst has the weakest ISO competence on the team.** The person
building the ISMS is listed with "ISO 27001 awareness", while the manager
overseeing it has lead auditor training. That's backwards for the person writing
the risk assessment and the SoA. It's the kind of gap clause 7.2 exists to catch,
and the right response is the one the clause itself prescribes — take action to
acquire the competence.

**Clause 7.2 also asks that you evaluate whether the actions worked.** The
maintenance section says gaps lead to training or reassignment. It doesn't say how
anyone checks the training closed the gap. Even a line — reviewed at the next
annual performance review, or demonstrated in an exercise — would cover it.

**The document is titled an awareness record but doesn't record awareness.**
Clause 7.3 is about people knowing the policy and their part in the ISMS. The
evidence for that is policy acknowledgement and training completion, with dates,
for everyone in scope. Either the record needs those columns, or the Training and
Awareness Policy needs a separate log — but as written, 7.3 has a policy and no
record.

**Two smaller things.** The scope lists HR and legal personnel, and Stark has
neither. And every review date reads "[Insert Date]" — fine for a template, but an
auditor reading the live document needs dates, because the review cycle is the
thing being tested.

## A correction to my clause 6 notes

In clause 6 I flagged "Abed Hamdan" as a data owner who doesn't exist in the
Stark brief. The competence record shows Abed Hamdan is the GRC Analyst. So the
name was real — I've updated that note. The finding changes shape rather than
disappearing: the GRC analyst shouldn't be the owner of an asset the ISMS
assesses. Owners should be accountable in the business, and the person running
the assessment owning the asset compromises the independence of that assessment.

## My take

**Clause 7 is mostly about evidence, not documents.** The documents for 7.1, 7.3,
7.4 and 7.5 largely exist already. What the clause actually tests is whether
records prove the documents are working — training completed, policy
acknowledged, competence demonstrated. That's the same design-versus-operating
distinction as every other part of this course, and it's where a young ISMS is
weakest, because the records only accumulate once the system has run for a while.

**The certification-versus-competence point is one I'd take to any hiring
conversation.** A certificate is evidence; it isn't the only evidence and it isn't
proof. Writing "training" rather than "certification" into a competence
requirement is a small drafting choice that reflects a sound view of what
competence is.

**Repo note:** the course's clause 7 document stays out of the repo. The course
folder on my laptop is the reading reference for the remaining clauses.
