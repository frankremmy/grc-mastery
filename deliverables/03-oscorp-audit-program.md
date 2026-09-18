# Cyber security audit program — Oscorp

**Module:** 03 — Cyber Security Audit
**Type:** Practical assessment
**Status:** My own answer, written before watching the solution.
**Role:** External cyber security consultant engaged by Oscorp's CEO.

---

## Situation

Oscorp needs its cyber security controls tested on a periodic basis, following
Harry Osborn's breakthrough on the confidential medication.

What Oscorp has today:

- A small cyber security team performing technical work — detecting and
  responding to incidents, managing firewalls.
- An internal audit function that conducts financial audits only.

What it doesn't have is any independent assurance over cyber security.

---

## Design

I would build the program around the three lines of defence, so that managing,
monitoring and independently auditing cyber risk sit with different people.

### First line — operational management and control owners

IT staff, system owners, and the employees responsible for operating Oscorp's
systems and protecting the confidential medication information.

Responsibilities:

- Following security policies and procedures.
- Managing user access and permissions.
- Applying security patches and maintaining systems.
- Operating backups and recovery procedures.
- Protecting confidential research data.
- Reporting security incidents and weaknesses.

Control owners perform regular checks confirming their controls operate correctly,
and retain evidence of those checks.

**Oscorp's existing cyber security team sits here for the work it actually
performs.** Managing firewalls and responding to incidents are operational
activities — the team owns and runs those controls. That placement matters,
because it means they cannot also be the ones assuring them.

### Second line — oversight and challenge

This is the layer Oscorp does not currently have, and the main gap in the design.

Second line's role is oversight: setting policy and standards, monitoring whether
controls are effective, tracking risks and remediation, and reporting cyber risk
to management. It reviews first line's work and asks for evidence; it does not
operate the controls itself.

Given the size of the organisation, a full second-line team isn't realistic. Two
workable options:

1. **Appoint a security risk and compliance role** reporting outside the cyber
   security team's management chain — to the CFO, COO or equivalent — with a remit
   to challenge rather than operate.
2. **Interim arrangement:** an external provider performs second-line review on a
   defined cycle until the role is filled. This is a stopgap, not the destination.

Either way the separation is what matters. A firewall configured and reviewed by
the same team produces a self-assessment, which the model exists to avoid.

Example activity: periodically reviewing who has access to Harry's confidential
research and identifying unnecessary or excessive permissions — performed by
someone who does not administer that access themselves.

### Third line — internal audit

Oscorp's internal audit function should provide independent assurance. Its scope
currently covers financial audit and should be expanded to include cyber security.

Internal audit should independently test access control, incident response,
backup and recovery, vulnerability management, firewall management, and protection
of confidential information — verifying evidence rather than relying on
confirmation from the cyber security team.

Two conditions on this:

- **Competence.** Internal audit has no cyber specialism today. Qualified external
  cyber auditors can support the function while it remains independent, or the
  function can recruit the skill directly over time.
- **Independence by reporting line.** Internal audit's standing comes from
  reporting beyond executive management — to the board, or an audit committee.
  Expanding scope without fixing the reporting line produces a third line that can
  be overruled by the people it audits.

---

## The audit program

### Audit universe

Before scheduling anything, define the auditable entities: the systems,
processes and controls that can be audited. Without that list, "risk-based" has
nothing to rank.

For Oscorp, at minimum: identity and access management; the confidential research
environment and its data stores; endpoint and anti-malware; firewall and network
controls; backup and recovery; incident detection and response; patch and
vulnerability management; third-party and supplier access; physical access to lab
and research areas.

### Risk-based schedule

Frequency follows risk rather than treating everything equally. Indicative
cadence:

| Tier | Areas | Frequency |
| --- | --- | --- |
| High | Systems holding confidential research; access to the medication project; backup and recovery for those systems | Every 6 months |
| Medium | Firewall and network controls; incident response; patch and vulnerability management; endpoint protection | Annually |
| Lower | Awareness training; physical access; general policy compliance | Every 18–24 months, or on change |

Anything materially changed — a new system, a new supplier with access, a
significant incident — triggers a review regardless of where it sits in the cycle.

### Conduct

Each audit is documented as an audit program setting out objective, scope,
criteria, period covered, and a test plan naming for each control the test
procedure, the evidence requested, and the sample. The
[audit program template](../templates/audit-program.md) is the format.

Testing verifies evidence rather than accepting assertion, and works up the
layers: that the control exists, that it is designed to address the risk, that it
covers the whole estate, that it is current, that it operates, and that its output
reaches someone who acts on it.

### Findings and remediation

- Every finding gets a rating, a named owner, and a due date.
- Findings are tracked to closure in a central register.
- Closed findings are re-tested rather than closed on assertion.
- Serious findings are escalated promptly rather than held for the report.
- Overdue and repeat findings are reported as a pattern, since a recurring
  finding usually means the underlying cause was never addressed.

### Reporting

Routine reporting goes to executive management. Summary reporting — control
status, significant findings, remediation progress and overdue items — goes to
the board or audit committee on a regular cycle.

---

## Assessment notes

**The confidential project must be in scope, and that needs settling in writing
up front.** The CEO is the engagement sponsor and the sponsor of the confidential
medication project. A program that reports cyber findings only to him, and that
can exclude his project from audit scope, provides very little assurance about
the thing Oscorp most needs assured. Scope inclusion and the reporting path to
the board should be agreed before the program starts, not negotiated after the
first uncomfortable finding.

**My own independence has a limit here.** Designing this program is advisory work.
Having designed it, I shouldn't also be the party providing assurance against it —
that's assessing my own design. If Oscorp wants external assurance support for
internal audit, it should come from a different team or a different firm.

**Proportionality.** Oscorp is small. The program above is deliberately modest —
one to three audits a year, a single risk-based schedule, and a findings register
rather than an audit management platform. A program designed for a bank would not
get run, and an audit program nobody runs is worse than a smaller one that
happens.

**What the first line can realistically do.** Asking a small team already doing
detection, response and firewall management to also perform structured
self-assessment is asking for capacity that may not exist. The control checks
should be few, specific and scheduled — a short list of evidence produced monthly
or quarterly — rather than an open-ended obligation that quietly stops happening.

---

## What I'd change on reflection

My first pass placed Oscorp's cyber security team in the second line. That's a
legitimate model in organisations where security sets policy and IT operates the
controls — but it doesn't fit the facts here. The scenario says this team manages
firewalls and responds to incidents, which is operating controls, and the same
team can't credibly review the configurations it maintains.

Correcting that made the real gap visible: **Oscorp has a first line and a third
line, and no second line at all.** Naming that as the finding, rather than
assigning the label to an existing team, is a stronger answer — and it's the gap
module 3 says most organisations get wrong.
