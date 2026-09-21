# The supplier discovery process

> Module 09, lesson 2. _You cannot assess a supplier you don't know you have._

## Summary

Before any assessment happens, you need the list. Who are our suppliers,
actually — all of them, current, accurate. In a small company that's an
afternoon. In a large one it's thousands of entries that change every week as
contracts start and end, and the list is stale the moment it's written.

The lesson gives a sequence for building it. Start with **procurement**, because
procurement processes invoices and payments, so they hold the closest thing to a
system of record for who the organisation pays. Then go to **IT**, who know which
vendors sit behind the critical applications — the finance system, the HR
platform holding PII — and who maintain and support them. Then **validate with
the business departments**, especially the ones handling sensitive information.
If IT says the finance application is maintained by Oracle, the finance team
confirms that's still true and supplies the current contact. Three sources,
cross-referenced, each correcting the others.

What makes this a real process rather than a data-gathering exercise is the
cross-referencing. No single team has the whole picture. Procurement knows who
gets paid but not what access they hold. IT knows who's connected but not what
was contractually agreed. The department heads know who they actually deal with
day to day, including the arrangements that never went through a formal process.
Each list is incomplete in a different direction, which is exactly why you need
all three.

The lesson also notes that a GRC professional can meet TPRM from three
directions: building the process from scratch, running the assessments within an
existing process, or auditing whether the process works. All three start at the
same place — is the supplier list complete? An assessment programme running
perfectly against an incomplete list is producing false assurance, which is worse
than no assurance because somebody is relying on it.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Supplier discovery | Building a comprehensive, current, accurate list of all third parties | The first step; every later step inherits its gaps |
| Procurement as primary source | The team processing invoices and payments holds the closest thing to a master list | Best available starting point, not a complete one |
| IT as second source | IT knows the vendors behind critical applications and who supports them | Surfaces access and system dependency that payment records don't show |
| Departmental validation | Confirming with the teams that actually use the supplier | Catches what's out of date and what never went through procurement |
| Cross-referencing | Reconciling sources against each other rather than trusting one | Each source is incomplete in a different direction |
| Prioritising sensitive areas | Starting validation with departments handling sensitive data | Discovery is unbounded; you need a sequence that front-loads what matters |
| Onboarding and offboarding churn | Suppliers constantly joining and leaving | Makes the list a maintained record, not a one-time deliverable |

## Where this shows up in a real job

This is the asset management problem again with a different noun. In module 4 the
lesson was that you can't protect what you haven't identified, and the asset
register only stays useful if something keeps it current. Suppliers are the same
shape: same discovery difficulty, same staleness problem, same dependence on
people outside security telling you the truth about what they use. I'd expect the
supplier list to sit alongside the asset register rather than in a separate world
— plenty of entries appear on both, since a critical application usually has a
vendor attached.

From support work I have a concrete sense of where the gaps come from. Teams
adopt tools because a tool solves a problem this week, and the procurement
conversation happens later or not at all. A subscription on a corporate card, a
free tier that quietly accumulates real data, a contractor still in a shared
workspace after the project ended. None of that is malicious and none of it shows
up cleanly in an invoice list.

## My take

The thing I want to remember is that this lesson is describing a *reconciliation*,
not a request. The instinct is to email procurement, get a spreadsheet, and treat
that as the answer. The procurement list is genuinely the best starting point,
but it answers one specific question — who do we currently pay — and that is not
the same question as who holds our data or has access to our systems. A supplier
whose contract ended last year may still be sitting on sensitive information, and
they're off procurement's list precisely because the payments stopped.

Which makes the cross-check the actual work. Where two sources disagree is where
the useful information is: the vendor IT knows about but procurement doesn't have
a contract for, the contract with no system owner, the department still sending
files to a supplier everyone assumed was gone. Those discrepancies aren't noise
in the data-gathering, they're findings.

And discovery can't be a project with an end date. If the only thing keeping the
list current is someone repeating this exercise annually, it's wrong for eleven
months of the year. It has to hook into the moment a supplier is onboarded — and
into offboarding, which gets far less attention and is where the residual data
risk from lesson 1 actually lives.
