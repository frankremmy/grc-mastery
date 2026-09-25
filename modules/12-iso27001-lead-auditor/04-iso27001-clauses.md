# ISO 27001 clauses

> Module 12, lesson 4. _The structure of the standard, and the half of it that
> actually gets organisations certified._

## Summary

Every framework brings its own vocabulary, and the first job when learning one is
getting past the jargon. NIST CSF has functions, categories and controls. ISO
27001 has **clauses**.

The standard runs from clause 0 to clause 10.

**Clauses 0–3 are informative.** They explain the standard rather than requiring
anything, and there is nothing in them to implement or assess.

- **0 Introduction** — why information security matters and how ISO 27001
  provides a systematic approach
- **1 Scope** — what *the standard* covers: requirements for establishing,
  implementing, maintaining and continually improving an ISMS, applicable to any
  organisation in any sector
- **2 Normative references** — points to ISO/IEC 27000 as the reference for terms
  and ISMS concepts
- **3 Terms and definitions** — establishes consistent language, again via
  ISO/IEC 27000

**Clauses 4–10 are mandatory requirements.** These are what an organisation must
implement to be certified.

### Clause 4 — Context of the organisation

Understand the environment the organisation operates in. Three things:

- Identify internal and external issues affecting information security
- Identify interested parties and their expectations — staff, customers,
  regulators
- **Define and document the ISMS scope**

Scope is the one that matters most. Certification is never a blanket statement
that everything was assessed. It could cover one application, one department,
several departments, or — rarely — the whole organisation.

*Worked example (running through the rest of the lesson):* a small company
building a SaaS application it wants to sell. Scope is the application and the
systems storing its data. Internal interested parties are the developers and the
cloud/IT team. If the application holds patient data and the company is in the
US, the external interested party is the HIPAA regulator.

### Clause 5 — Leadership

Nothing works without top management behind it, so the standard makes that
explicit and documented rather than assumed.

- Appoint someone from top management to own the ISMS
- An information security policy **aligned with business objectives** — not a
  generic document, but one that states why the security work serves the
  business. For the SaaS example: we're pursuing certification to give clients
  assurance the application is secure, which supports sales
- Roles and responsibilities clearly defined — who manages what, who is
  accountable

### Clause 6 — Planning

Where risk assessment happens.

- Conduct a comprehensive risk assessment identifying risks, threats and
  vulnerabilities. For the SaaS app: insecure code, unpatched vulnerabilities,
  where the data sits, whether it's encrypted, who has access
- Develop a **risk treatment plan** documenting how each risk will be handled —
  developers follow OWASP Top 10, secure coding training is mandatory, a
  penetration test happens before go-live
- Define **measurable information security objectives** aligned with the
  organisation's mission. Genuinely hard at small organisations that have no
  articulated mission

### Clause 7 — Support

- Resources: people, tools and budget
- Competence and awareness: staff in scope have the skills to manage the
  identified risks
- **Documented information**: policies, procedures and records, maintained
- **Communication**: the ISMS is explained to the people who have to operate it,
  and they actually understand it. Judging whether they do is a skill — and it's
  a common weak point across every standard, not just this one

### Clause 8 — Operation

Where the plan becomes practice.

- Execute the risk treatment plan from clause 6
- Ensure operational security procedures are followed in reality, not only on
  paper
- Manage changes to business processes and IT

For the SaaS example: confirm the developers actually completed the secure coding
training, that a secure code review process exists and runs, and that changes are
raised, approved and documented.

### Clause 9 — Performance evaluation

- Monitor, measure, analyse and evaluate ISMS performance
- **Internal audits** at planned intervals, assessing whether controls, policies
  and procedures are effective
- **Management review** — senior management periodically reviews ISMS
  performance, signs off, and drives improvement
- **KPIs** for the ISMS. Hard at the start, but achievable: findings closed,
  risks treated, phishing awareness improving over time

### Clause 10 — Improvement

- Respond to **nonconformities** through corrective action. A nonconformity is
  ISO's word for a finding — something the standard requires that the
  organisation isn't doing
- Continually improve, driven by audit findings and security incidents

Identifying problems isn't enough; the standard requires documented evidence that
they were corrected.

## The learning approach

Don't memorise the clauses. Understand them, work with them practically, and
refer to the standard when needed. The course is explicit that it doesn't
memorise frameworks either — it downloads and reads them. That's the right
posture for any framework.

## A structure that makes them stick

ISO management system standards are built on **Plan–Do–Check–Act**, and the
clauses map onto it directly:

| PDCA | Clauses |
| --- | --- |
| **Plan** | 4 context · 5 leadership · 6 planning · 7 support |
| **Do** | 8 operation |
| **Check** | 9 performance evaluation |
| **Act** | 10 improvement |

That's four ideas rather than seven, and it's the same shape as the ISMS cycle
from lesson 2. It also explains why the clause order is what it is — and why
every other ISO management system standard (9001 for quality, 22301 for
continuity) has the same clause numbering. Learn this structure once and you can
navigate any of them.

## Two things worth getting right

**Clause 1 Scope is not the ISMS scope.** The infographic describes clause 1 as
defining "the boundaries and applicability of the ISMS" — that's clause **4.3**.
Clause 1 is the scope of *the standard itself*: what the document covers and who
it applies to. The written material has this right. It's an easy conflation and
a bad one to make out loud, because scope is the thing everyone in an ISO
conversation cares about.

**Clause count.** The lesson says eleven clauses numbered 0 to 10; the written
material says ten. Both are describing the same thing — 0 through 10 is eleven
numbered sections, and clause 0 is an introduction rather than a clause carrying
requirements, so people count it either way. Not worth arguing about, but worth
not being caught out by.

## My take

**The clauses are where certification is actually won or lost, and Annex A is
where everyone looks.** Annex A has the 93 controls, so it attracts the
attention — it's the part that feels like security. But clauses 4 to 10 are the
management system, and an organisation with excellent technical controls and no
management review, no internal audit programme and no documented risk treatment
plan fails certification regardless.

Oscorp makes that concrete. From the capstone: no information security policy
(clause 5.2), no defined roles (5.3), no cyber risk process (6.1), no internal
audit (9.2), no management review (9.3), no corrective action process (10.2).
Oscorp would fail at clause 5 and never reach Annex A. And the roadmap I wrote
put a Head of Security, a policy set and a risk process in year 1 — not because I
was thinking about ISO, but because those are what everything else depends on.
The standard's clause order encodes the same conclusion.

**The other thing I'd flag is that the standard names its mandatory records.**
The scope statement, the policy, the risk assessment and treatment process and
their results, the Statement of Applicability, the objectives, competence
evidence, monitoring results, the internal audit programme and its results,
management review records, and nonconformity and corrective action records. An
auditor arrives knowing that list. Which means the first useful question when
assessing readiness isn't "do you have controls" — it's "show me these documents,
and show me the evidence each one was produced by a process that actually ran."
