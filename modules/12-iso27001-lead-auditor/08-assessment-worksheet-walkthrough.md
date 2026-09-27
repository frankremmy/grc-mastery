# Assessment worksheet walkthrough

> Module 12, lesson 8. _The working spreadsheet, and what it is structurally._

## Summary

The whole standard is laid out across two working tabs, plus a disclaimer.

**Mandatory Clauses** — clauses 4 to 10, broken into **30 requirement rows**.
Columns: clause, name, control number, control title, control description,
**questions to ask**, **examples**.

**Annex A** — the **93 controls** across the four themes. Columns: clause, name,
control number, control title, control description, **In Scope (Y/N)**,
**Justification**.

**What's official and what isn't.** The control numbers, titles and descriptions
are ISO's own text. The *questions to ask* and *examples* columns are the
course's additions — practical prompts for interviewing a client or building an
ISMS, not requirements. The disclaimer exists because someone will inevitably
treat the sheet as official documentation.

The reason those columns exist is that the standard's language is dense.
Clause 4.1 says the organisation shall determine external and internal issues
relevant to its purpose that affect its ability to achieve the intended outcomes
of its ISMS. The translation into usable questions: what internal factors affect
the ISMS (structure, culture, resources)? What external ones (regulators,
industry trends, risks)? How do you review and update that understanding over
time? Are these factors feeding into the risk assessment and security strategy?

That last pair is a best-practice addition rather than a literal reading — the
continuous review and the integration into risk assessment are the things that
separate a documented answer from a working one.

**The Annex A controls will feel familiar.** 5.3 segregation of duties —
"conflicting duties and conflicting areas of responsibility shall be segregated"
— is module 5 in ISO's wording. 6.2 terms and conditions of employment requires
employment agreements to state the personnel's and the organisation's information
security responsibilities, which is the roles-and-responsibilities theme running
through this whole course. Past the jargon, it's material already covered.

## Structure worth noticing

**The requirement rows per clause:**

| Clause | Requirement rows |
| --- | ---: |
| 4 Context | 4 |
| 5 Leadership | 3 |
| 6 Planning | 5 |
| 7 Support | 7 |
| 8 Operation | 3 |
| 9 Performance evaluation | 6 |
| 10 Improvement | 2 |
| **Total** | **30** |

Support and performance evaluation carry the most individual requirements, which
is not where most people's attention goes — clause 7 covers resources,
competence, awareness, communication and documented information, and clause 9
covers monitoring, internal audit and management review. Both are
evidence-heavy, and both are where certification readiness usually falls short.

Two 2022 version markers visible in the structure: **clause 6.3 "planning of
changes" is new** in this revision, and clause 10 reversed its sub-clause order —
continual improvement is now 10.1, nonconformity and corrective action 10.2.

**The Annex A tab confirms the theme counts:** 37 organisational, 8 people, 14
physical, 34 technological.

## The Annex A tab is a Statement of Applicability

That's the structural point. "In Scope (Y/N)" plus "Justification" against every
one of the 93 controls *is* the SoA — the document clause 6.1.3(d) requires.

Which makes it worth checking against what that clause actually demands. The SoA
must contain:

- the necessary controls
- **justification for their inclusion**
- **whether they are implemented or not**
- **justification for excluding** any Annex A controls

The sheet covers inclusion, exclusion and justification. It has **no
implementation status column**. That's a real gap if the tab is used as a
finished SoA rather than as a selection worksheet — an auditor looking at an SoA
expects to see which selected controls are actually in place, because selected
and implemented are different states and the difference is where the findings
live.

Easy fix: add an "Implemented (Y/N/Partial)" column, and ideally a reference back
to the risk that drove the selection, since the standard expects control
selection to trace to the risk treatment.

## Repo handling

**This spreadsheet doesn't go in the repo.** It carries ISO's official control
text, and the standard is a paid publication — the same reason the case study
source documents are linked rather than copied.

What can go in: an SoA I produce for Oscorp listing **control numbers, short
titles, my scope decision and my justification**, without reproducing ISO's
description text. That's how published SoAs are generally written, and it keeps
the work mine rather than a copy of the standard.

## My take

The two-tab structure makes the shape of ISO 27001 clear in a way the lessons
alone didn't: **30 requirements you must satisfy, and 93 controls you choose
from.** The first number is fixed for everyone. The second is where two certified
organisations can look completely different.

It also reframes what the "questions to ask" column is. It isn't a study aid —
it's an audit programme. Turning a control statement into a question you can put
to a person is the actual skill of an assessor, and it's the same thing the NIST
capstone spreadsheet did. Having now worked through one framework that way, the
format is recognisable: control, question, evidence, verdict, comment. The
framework changes; the method doesn't.

One habit I'd carry from the capstone into this: when I fill the Annex A tab for
Oscorp, the justification column needs to be written for someone who wasn't in
the room. "Not applicable" is not a justification. "Excluded — Oscorp performs no
software development and consumes only SaaS" is, and it's the difference between
an SoA that survives an audit and one that generates a finding.
