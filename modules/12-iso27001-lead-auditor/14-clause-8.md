# Clause 8 — operation

> Module 12, lesson 14. _Where the plan gets implemented, and the tracker that
> proves it was._

## What clause 8 asks for

Clause 6 planned. Clause 7 resourced. Clause 8 is where the controls actually get
implemented — and, for certification, where the organisation has to **show
evidence** that they were.

| Requirement | What it means | Stark |
| --- | --- | --- |
| 8.1 Operational planning and control | Processes exist to deliver what was planned, and you can show they ran | **Control evidence tracker** |
| 8.2 Information security risk assessment | Perform the assessments defined in 6.1.2 | Done — the risk register |
| 8.3 Information security risk treatment | Implement the treatment plan from 6.1.3 | Done — treatment plan and SoA, tracked through implementation |

The distinction with clause 6 is planning versus doing. 6.1.2 defines how
assessment works; 8.2 says you actually do it. 6.1.3 defines treatment; 8.3 says
you actually treat.

## Evidence

A policy says what will happen. Evidence shows it did. The lesson's examples of
what counts:

- Screenshots of configured controls — common for small organisations
- Vulnerability scan and penetration test reports, **plus evidence the findings
  were remediated**
- Procedures and how-tos — SharePoint articles, SOPs, Jira pages
- Anything else that shows a control operating

There's no single required format. Large organisations evidence through their
ticketing and knowledge systems; small ones often through a folder of
screenshots.

## The control evidence tracker

Whatever the evidence looks like, the GRC analyst keeps **one spreadsheet that
tracks it** — control, whether it's implemented, what the evidence is, where it
lives, and who owns it. The technical evidence sits in folders and systems owned
by the engineers; the tracker is the index. When the auditor arrives, they get the
tracker.

**Structure:** control number, title, description, status, implementation
status, evidence type (document, screenshot, report), evidence location
(SharePoint, Jira, a drive), responsible owner, date verified, comments.

**It covers the 63 controls the SoA selected** — 27 organisational, 8 people, 28
technological, and no physical controls. The other 30 of the 93 were excluded in
the SoA, so they have nothing to evidence.

Everything starts as Planned / To be determined / To be assigned. It's a template,
because in practice the evidence format depends entirely on the organisation.

## Where I'd push back

**Add a risk reference column.** The tracker lists controls without saying which
risk each one treats. Clause 6.1.3 expects controls to come *from* risk treatment,
and an auditor following the thread from R001 (source code access) to its
controls to their evidence has to cross-reference the SoA and the register by
hand. One column — "Treats risk" — makes the whole chain traceable in one sheet,
and makes residual risk easier to reassess once the evidence is in.

**Clause 8.1 covers outsourced processes, and the tracker doesn't.** 8.1 requires
externally provided processes relevant to the ISMS to be controlled. Stark's
entire production environment is AWS. The shared responsibility boundary — what
AWS evidences (its own ISO 27001 and SOC 2 reports) and what Stark evidences
(configuration, access, application) — belongs here. Without it, controls like
A.8.14 redundancy and A.8.20 network security have evidence split across two
organisations and no record of which half is whose.

**8.2 isn't one assessment.** The clause requires risk assessments at planned
intervals *and when significant changes occur*. The tracker evidences that the
first one happened; the process needs a trigger for the next. A new feature, a
new AWS service or a new supplier should all prompt a reassessment, and the
change management gap I flagged in clause 6 is what would normally raise that
trigger.

**Two smaller data points.**

- *Status* and *Implementation Status* look like the same field twice. Pick one,
  with defined values — Planned, In progress, Implemented, Verified — so the
  sheet can be filtered.
- The control numbers are stored inconsistently: some as numbers, some as text.
  That's not cosmetic. As a number, **5.10 is the same value as 5.1**, so a sort
  or a lookup can silently merge two different controls. Store them all as text.

## A correction to my clause 6 notes

In clause 6 I said A.8.29 security testing wasn't selected in the SoA. The
tracker includes it, so it was selected. I've removed that point from the clause
6 note.

## My take

**The tracker is where an ISMS stops being documents and starts being evidence.**
Everything up to clause 7 can be written in an office. Clause 8 can't — it needs
engineers to have actually configured the controls and someone to have captured
proof they did. That's why the lesson's warning in clause 6 matters: organisations
that select controls generously discover here, at implementation, that it'll take
another six months.

**The format choice is right: index, not repository.** The GRC analyst doesn't
need to hold the evidence, just know where every piece of it is and who owns it.
That's a working pattern for any audit, not just ISO — and it's the same idea as
the asset register, applied to proof instead of systems.

**Repo note:** the course's tracker stays out of the repo. My own tracker for
Stark — with the risk reference and AWS columns — goes in with the ISMS document
set.
