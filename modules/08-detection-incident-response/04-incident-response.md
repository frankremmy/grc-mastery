# Cyber security incident response

> Module 08, lesson 4. Making sure the organisation can respond — people, process
> and technology — without being the one who responds.

## Summary

Incident response is paired with detection because detection is the first step and
response is the next. **GRC professionals don't respond to attacks.** The job is
ensuring the organisation has the people, process and technology to respond
properly.

**People.** Experienced incident responders are hard to find. The experience takes
training, knowledge and time, and people who have it command high salaries — so
small and mid-sized organisations struggle to attract and keep them.

**Process.** Assuming capable people exist, the next requirement is
well-documented, easy-to-follow, **tested** procedures. There are two kinds of
plan.

### Enterprise-wide incident response plan

Covers a severe incident affecting the whole organisation — a large ransomware
attack shutting down the business or a significant part of it. For that scenario
the plan sets out what to do, who to contact, how to escalate, and how to inform
senior management.

It should **invoke the organisation's crisis management plan**, because an incident
at that severity is an organisational crisis rather than a technical problem. Most
organisations have a crisis plan covering who to contact, how to escalate to the
CEO, and how to communicate with the board or the press. This is where a **war
room** or **bridge** forms — senior stakeholders and representatives from every
team, deciding and executing next steps.

If there's no crisis management plan, the incident response plan has to document
who to contact in a crisis itself. It doesn't need to be complicated, but it must
clearly state the **escalation points and the thresholds or conditions** that
trigger escalation.

### Scenario-specific plans (playbooks)

Technical, step-by-step procedures for particular incident types. Not every
scenario needs one, but the common ones should be covered:

- Phishing attack
- Denial of service
- Compromised user account
- Malware
- Compromised web page or server

Those cover the majority of what a security team actually meets.

## Two published plans, compared

Both attached examples are public documents and worth reading as models.

| | **ACSC Cyber Incident Response Plan Template** | **Carnegie Mellon University CSIRP** (v1.6) |
| --- | --- | --- |
| Type | A template to be filled in | A live organisational plan |
| Phases | Detection, investigation, analysis and activation → containment, evidence collection and remediation → recovery → learn and improve | Preparation → detection → containment → investigation → remediation → recovery |
| Structure | Roles, communications, playbooks, sector/jurisdictional/national arrangements, notification and reporting | Purpose, scope, authority, definitions, roles, methodology, guidelines, escalation |
| Notable inclusions | Readiness checklist, triage questions, situation report template, incident log, evidence register, remediation action plan, post-incident review template, role cards, categorisation matrix | Event vs incident definitions, evidence preservation, law enforcement interaction, communications plan, privacy, documentation and tracking |
| Teams named | Cyber Incident Response Team (operational) and Senior Executive Management Team (strategic) | Incident Response Coordinator, Incident Response Handlers, Office of General Counsel, Officers, Key Stakeholders |
| Basis | NIST Computer Security Incident Handling Guide threat vector taxonomy | References NIST SP 800-61 |

The two-tier team split in the ACSC template — an operational CIRT and a strategic
SEMT — is the enterprise-plan-plus-playbook idea expressed as org structure.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| The GRC role in IR | Ensuring capability exists; not performing the response | Defines what you assess and what you don't touch |
| Enterprise-wide plan | What to do in a severe, organisation-level incident | Written for decision makers under pressure |
| Scenario playbook | Step-by-step technical procedure for a specific incident type | Written for responders during the event |
| Crisis management plan | The organisation's existing crisis process | Cyber severity should invoke it rather than duplicate it |
| War room / bridge | The forum where senior stakeholders decide and execute | Where a technical incident becomes a business response |
| Escalation thresholds | The stated conditions that trigger escalation | The part that removes judgement from whoever is on shift |
| Event vs incident | Not every anomaly is an incident | CMU's plan defines this explicitly; it controls what the process applies to |
| Evidence preservation | Collecting and handling evidence defensibly | Speed of recovery has to be balanced against it |
| Tested procedures | Plans exercised, not just written | The difference between a document and a capability |

## Where this shows up in a real job

This is the module where my own work lines up most closely. The incident response
lab series I've been working through — 25 labs across IR and digital forensics —
covers the responder side, and I produced a cyber incident response plan as part of
it. That's real, and it's worth being precise about what it demonstrates: I've
written a plan and worked scenarios, in an environment I controlled.

What that doesn't include is the part this lesson is actually about — an
organisation with a crisis plan, executives who need briefing, legal counsel,
communications, and escalation thresholds that have to work when the person on
shift has never seen this before. The plan I wrote had no board to notify.

From the support side, the escalation-threshold problem is familiar in miniature.
The question of when something stops being a ticket and becomes an incident is
answered by whoever is holding it, and the quality of that call varies with
experience unless the threshold is written down.

## My take

The two plan types have **different readers**, and that's the most useful thing to
take from this lesson. The enterprise plan is read by executives during a crisis —
people who need to know who decides, who to call, and what to tell the board. The
playbook is read by a responder at 3am who needs the next command. A single
document trying to serve both is too detailed for the executive and too vague for
the responder, and that's a common finding worth looking for: one plan, one
audience, and whichever reader it wasn't written for is unserved.

Three things:

**Escalation thresholds are the load-bearing component.** Everything else in an
enterprise plan describes what happens once escalation occurs; the threshold
decides whether it occurs at all. Without stated conditions, the decision falls to
whoever is on shift, who is junior, tired, and reluctant to wake an executive over
something that might be nothing. Both sample plans handle this — ACSC with a
categorisation matrix and activation criteria, CMU with High/Medium/Low
categorisation on data exposure, resource criticality, scope and persistence. That
comparison is the model: severity defined by stated factors, not by instinct.

**CMU's plan contains a detail worth stealing.** It specifies what happens when the
Incident Response Coordinator is *themselves* a person of interest in an incident —
the CISO acts instead; and if the CISO is implicated, the CIO does. That's
separation of duties applied to incident response, and it matters for exactly the
Oscorp-style scenario where the suspected insider might be senior. Most plans
assume the responders are trustworthy and say nothing about the case where they
aren't.

**A plan is only a capability once it's been tested, and two practical failures
recur.** The plan stored only on the network that ransomware just encrypted, and
the contact list that's a year out of date. Offline copies and a current call tree
are unglamorous and they're the difference between a plan and a PDF nobody can
open. The ACSC template's readiness checklist exists for this reason, and cyber
drills — the next lesson — are how the rest gets found.

One assessment question I'd add to the lesson's list: **when was the plan last
used, and what changed afterwards?** Both sample documents have revision histories,
and CMU's shows six revisions across eight years with the reasons recorded. A plan
that has never been revised has either never been tested or never been learned
from.

## Reference

- ACSC, *Cyber Incident Response Plan Template* — <https://www.cyber.gov.au>
- Carnegie Mellon University, *Computer Security Incident Response Plan* v1.6
