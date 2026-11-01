# Clause 5 — leadership

> Module 12, lesson 11. _Two documents, one distinction that matters more than
> either of them._

## The method

Clause 5 has three requirements — 5.1 leadership and commitment, 5.2 the
information security policy, 5.3 roles and responsibilities. **Two documents
rather than one:** an Information Security Policy, and an ISMS Roles and
Responsibilities document.

The stated reason is readability, plus roles not changing often. I'd add a
stronger one: **the two have different review cycles.** The policy is reviewed at
planned intervals and after significant change; roles change whenever someone
joins, leaves or is restructured. Splitting them means updating the roles
document doesn't force a new version of the policy and a fresh CEO signature.

## Document 1 — Information Security Policy

**Purpose.** Commitment to protecting the confidentiality, integrity and
availability of information assets; sets out the requirements; and — the precise
part — **applies to all employees, contractors, systems and services within the
defined ISMS scope.**

That scoping line matters. This is not a general corporate information security
policy. A large organisation will already have one covering everything, and may
need a separate ISMS-specific policy for the certified scope. Stark is small
enough that the distinction is academic in practice, but the document still has
to exist for certification. An organisation that already has a policy usually
needs to modify it rather than write from scratch.

**Business objectives first, then security aligned to them.** This is the part I
think is most easily got wrong, and the lesson calls it out directly: **business
objectives are business objectives, not security objectives.** Stark's are
selling a SaaS marketing platform to small and mid-sized businesses, growing the
customer base, delivering reliable service, and meeting customer security
expectations to stay competitive. The business exists to sell software.

Security appears inside the business objectives only where the business itself
cares — reliability, availability, meeting customer security expectations. That's
the alignment clause 5.2 asks for, and it reads as alignment precisely because
the business objective wasn't rewritten into a security objective.

Where these come from in practice: meeting business stakeholders, or reading the
organisation's own business documents.

**Information security objectives**, stated separately: secure deployment and
operation of the platform; maintain availability; minimise risk of unauthorised
access; promote security awareness across all staff; achieve ISO 27001
certification. Plus a statement that they are measurable, reviewed regularly and
integrated into relevant business processes.

The first three are the CIA triad restated as objectives. Awareness is in there
because the standard expects staff training, so putting it in the objectives
anticipates a requirement rather than waiting for it.

**Commitment to continual improvement**, written explicitly even though the
document control table already implies periodic review. The reasoning is worth
adopting: an auditor shouldn't have to hunt. If a requirement is satisfied
somewhere implicitly, saying it plainly costs a sentence and saves an argument.

**An explicit statement that the ISMS complies with ISO 27001**, which feels
redundant and is cheap to include.

**Leadership commitment in writing.** It can be evidenced other ways — emails,
meeting minutes, public statements from the CEO — but written and signed is
better. It saves time for the internal auditor and the certification body, and
it's there when asked for.

**Approval block:** signed by, date. CEO, CISO, or executive leadership.

## Document 2 — ISMS Roles and Responsibilities

**These are ISMS roles, not general job descriptions.** A security analyst does
many things; this document covers only the parts relating to the ISMS.

Format is a free choice — table or bullets. ISO doesn't prescribe document
structure, and the lesson uses a different format here deliberately to show that.

| Role | ISMS responsibility |
| --- | --- |
| CEO | Overall **accountability** for the ISMS |
| Information Security Manager | Leads implementation, oversees risk management, ensures compliance |
| Cyber Security GRC Analyst | Manages ISMS processes day to day; tracks every action |
| Information Security Analyst | Technical — incidents, alerts, monitoring |
| IT Infrastructure Engineer | AWS, network, backups, endpoints |
| Software Developer | Secure coding practices, code vulnerabilities |
| All employees | Accept the policy; complete security awareness training |

**Authority delegation**, stated explicitly: leadership delegates day-to-day ISMS
work to the Information Security Manager, because executives don't have the
capacity to run information security themselves.

**And the distinction that carries the clause: responsibility is not
accountability.** The Information Security Manager is *responsible* for
implementing and leading the ISMS. The CEO remains *accountable* — the person who
answers to customers when something goes wrong. Delegating the work does not
delegate the answerability.

## Worth adding

**Clause 5.2 has mandatory content the lesson doesn't fully enumerate**, and one
item is easy to miss. The policy shall: be appropriate to the organisation's
purpose; include information security objectives or a framework for setting them;
include a commitment to satisfy applicable requirements; include a commitment to
continual improvement; be available as documented information; be **communicated
within the organisation**; and be **available to interested parties as
appropriate**.

The Stark policy covers most of that. The two worth checking are the last pair —
*communicated* needs evidence that it reached people (acknowledgement records),
and *available to interested parties* means deciding whether customers can see
it. For a company whose customers are demanding certification, publishing a
summary policy is a reasonable answer and a sales asset.

**Clause 5.1's evidence mostly gets generated later.** The clause asks top
management to ensure the policy and objectives are compatible with strategic
direction, integrate ISMS requirements into business processes, make resources
available, communicate the importance of the ISMS, direct and support people, and
promote improvement. A signed policy is thin proof of all that on its own. The
substantial evidence is **management review minutes under clause 9.3**, budget
and resource decisions, and objectives visibly tied to strategy. Worth knowing
that clause 5 gets audited partly through clause 9 artefacts.

**"Achieve ISO 27001 certification" as an information security objective is
debatable.** Clause 6.2 wants objectives that are measurable, monitored, and
relevant to information security. Certification is a project milestone — once
achieved, the objective is finished, and there's nothing to monitor at the next
management review. Plenty of real ISMSs list it and auditors usually let it pass,
but I'd pair it with objectives that persist and have numbers attached:
proportion of staff completing awareness training, time to remediate critical
vulnerabilities, overdue corrective actions. The policy states the objectives
*are* measurable without saying what the measures are — those targets need to
live somewhere, most naturally in the clause 6 planning document.

**The "all employees" row does more work than it looks.** It's what makes A.5.4
(management responsibilities) and A.6.3 (awareness training) evidenceable later —
the obligation has to be stated somewhere before you can show people met it.

## My take

The responsibility-versus-accountability distinction is the thing I'd take from
this lesson into any job, not just ISO work. It's the formal version of the
point that kept surfacing in the capstone: someone has to own security, and
owning it is different from doing it. Stark's CEO does none of the work and
answers for all of it, and writing that down is what makes clause 5 real rather
than ceremonial.

It also explains why clause 5 sits where it does. Context (4) defines what you're
protecting; leadership (5) establishes who answers for it; only then does
planning (6) decide what to do. An ISMS built in a different order produces
controls nobody owns — which is precisely what the Oscorp capstone found.

**Repo note:** the course's two PDFs stay out. My own Stark policy and roles
document go in `deliverables/`.
