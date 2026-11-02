# Clause 10 — improvement

> Module 12, lesson 16. _The last mandatory clause: keep improving, and fix what
> the audits found — with proof the fix worked._

## What clause 10 asks for

| Requirement | What it means | Stark |
| --- | --- | --- |
| 10.1 Continual improvement | Keep improving the suitability, adequacy and effectiveness of the ISMS | No separate document — it's built into everything already |
| 10.2 Nonconformity and corrective action | Record nonconformities, act on them, and check the action worked | **Nonconformity Log** |

Clause 10 is the *Act* in Plan–Do–Check–Act. By this point the controls are
implemented, the internal audit has run, and the findings are known.

## 10.1 — continual improvement

A separate "continual improvement" document would add nothing, because the
improvement is already designed in:

- Every ISMS document carries a review frequency and next review date
- Recurring penetration tests and vulnerability scans
- The annual internal audit and the management reviews

The evidence is the history: document control tables showing more than one
review, a second year's pen test compared against the first, audit findings that
were closed. That's what an auditor looks for.

## 10.2 — nonconformity and corrective action

The clause auditors care about most here, because they need nonconformities dealt
with before they'll certify.

A nonconformity can come from the internal audit, the external audit, a
stakeholder, or an incident. For each one, record it, link it to the clause or
Annex A control it breaches, record the corrective action, and **show the action
actually fixed it**.

**The log** has columns for control name, owner, description, finding date,
resolution date, status and comment. It's a blank template — a hypothetical
project has no real findings — and it doesn't need to be sophisticated.

## Worth adding

**Correction is not corrective action.** This is the distinction 10.2 turns on. A
*correction* fixes the instance: the leaver's account that was still active gets
disabled. A *corrective action* removes the cause: the offboarding process gets a
step that disables accounts on the last day, so it doesn't recur. The clause asks
for both, and specifically asks the organisation to determine the cause and
whether similar nonconformities exist elsewhere.

**What 10.2 requires the record to show** — the nature of the nonconformity, the
actions taken, and the results of the corrective action. The Stark log covers the
first two loosely and the third not at all. I'd add:

| Column | Why |
| --- | --- |
| NC ID | So findings can be referenced in minutes and audit reports |
| Source | Internal audit, external audit, incident, stakeholder |
| Clause / control reference | Separate from the name, so it can be filtered |
| Severity — major or minor | A major nonconformity blocks certification; a minor one needs a plan |
| Root cause | 10.2 asks for the cause, not just the symptom |
| Correction and corrective action | Two columns, for the two different things |
| Effectiveness check — date and result | The step the clause requires and most logs skip |

**Major versus minor matters for the timeline.** A major nonconformity — a
mandatory requirement missing entirely, or a control failing systemically —
generally has to be closed before the certificate is issued. A minor one can
usually be certified with an agreed corrective action plan. That's exactly the
distinction management needs from the log, because it decides whether the
certification date moves.

**The log feeds the management review.** Clause 9.3 lists the status of
corrective actions as an input, so the log is what the GRC analyst brings to the
meeting — and repeated nonconformities against the same control are the clearest
argument for budget.

## My take

**Effectiveness checking is the part I'd hold myself to.** Closing a finding is
easy: write "fixed" and a date. Showing the fix worked — the next access review
found no stale accounts, the next scan didn't repeat the finding — is what the
clause actually asks for, and it's the same design-versus-operating-effectiveness
test that's run through every module of this course. A nonconformity log with a
resolution date and no evidence of effectiveness is a list of claims.

**Clause 10 closes the loop that clause 4 opened.** The scope decided what to
protect; 5 assigned the accountability; 6 planned; 7 resourced; 8 implemented; 9
measured; 10 fixes what the measuring found and feeds it back into the next
cycle's risk assessment. Reading the clauses in order, the standard is one
argument, not ten requirements.

**Repo note:** the course's log template stays out of the repo. Mine, with the
added columns, goes into the Stark ISMS set.
