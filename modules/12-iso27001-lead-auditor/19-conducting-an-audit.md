# Lesson 19 — Conducting an ISO 27001 audit

## Summary

Internal audits and certification audits follow the same nine steps:

1. Scope and objectives
2. Audit plan
3. Checklist
4. Opening meeting
5. Audit activities
6. Findings
7. Closing meeting
8. Report
9. Follow-up

The structure itself is simple. The skill is in two things. First, staying a partner to the auditee without going soft on findings. Second, treating every claim as unproven until you've seen evidence ("trust, but verify").

The course provides a list of mandatory and best-practice documents to use as a checklist. It isn't reproduced here. Organisations often merge or split documents, or keep them in a GRC tool, so match the checklist to what the requirement asks for, not to file names.

## Key concepts

| Step | What matters | Evidence it leaves |
|---|---|---|
| 1. Scope and objectives | The part of the ISMS being audited, the criteria (27001 clauses, the controls the SoA selects, internal policies, legal duties), and the purpose (full audit, surveillance, phased) | Scope statement in the plan |
| 2. Audit plan | Dates, auditees, access, methods (interview, observation, record sampling). Book stakeholders early. Estimates always run long | Plan sent to auditees |
| 3. Checklist | Clauses 4–10, the SoA, the risk treatment plan, internal policies. A guide, not a limit | Working papers |
| 4. Opening meeting | Introductions, confirm scope and agenda, ground rules, confidentiality | Agenda, attendance, minutes |
| 5. Audit activities | Objective evidence. Sample, and record how the sample was chosen | Sampled records, interview notes |
| 6. Findings | Conformity, major NC, minor NC, OFI. Raise each one with the auditee as you find it | Findings log |
| 7. Closing meeting | Nothing new to the auditee. Agree next steps and dates | Minutes, draft report |
| 8. Report | Scope, methodology, findings, next steps. The certification body will read an internal audit report | Final report |
| 9. Follow-up | Check that fixes were made and that they worked, then close with evidence | Closure evidence on the NC log |

Major vs minor, using the course's examples. Vulnerability scanning that runs but misses some assets is a minor NC: the process exists, but it has gaps. A bigger gap in coverage could tip it to major. Awareness training that reaches everyone but is dull is an OFI: the requirement is met, and the auditor is suggesting an improvement.

## Where this shows up in a real job

- A junior GRC consultant mostly does steps 2, 3 and 5: chasing documents into a tracker before fieldwork, collecting evidence, and drafting findings for the lead to review.
- My Stark clause 6–10 notes are good practice for step 5. Each critique there (e.g. the SoA contradicts the asset register) is a finding with evidence attached.
- Being "a partner without compromising" works the same way as support escalation. You can be kind about how you deliver the news without changing what the news is.

## Where I'd push back

- **"The organisation cannot be certified with nonconformities" is too strong.** In practice, every major NC must be corrected, and the certification body must verify the fix, before certification is granted. A minor NC usually needs only an accepted corrective action plan, with the fix checked at the next surveillance audit. Certificates are regularly issued with open minors.
- **The auditor must not write the correction plan.** The auditee owns the correction, the root cause analysis and the corrective action, and the auditor checks them. If an internal auditor designs the fix and then audits it, they are auditing their own work, which breaks clause 9.2's objectivity requirement. For a certification body it's worse: ISO/IEC 17021-1 forbids consulting for the organisations it certifies. An auditor can recommend a fix, but the plan belongs to the auditee.
- **Step 9 skips over the clause 10.2 sequence.** The steps are: correction (contain the problem now), root cause, corrective action (stop it recurring), then an effectiveness check. "Corrective action plan" lumps all four together. This is the same gap I flagged in the Stark nonconformity log.
- **The draft report is for agreeing facts and dates, not for agreeing findings.** The auditee can correct factual errors and agree the remediation timeline. Whether something is a nonconformity is the auditor's call. The lesson makes this point too: call out what's significant even when the team pushes back.
- **This lesson describes a single audit. Clause 9.2.2 also requires an audit programme:** the multi-year plan that decides which parts of the ISMS get audited when, based on importance and previous results. The "phase the audit over two years" scenario is really an audit programme decision.
- **Sampling needs a rationale.** ISO 19011 (A.6) separates judgement-based sampling from statistical sampling. Write down the population, the sample size and how the sample was chosen, so another auditor could reach the same result.

## My take

An audit is a conversation about evidence. The report should never be the first time the auditee hears about a finding. I especially like the "no surprises" rule. It's the same as a good support handover: whoever receives the escalation should never learn about a problem from the ticket alone. The point I'll hold firmly is independence. Help the auditee understand a finding, but let them own the fix, because the moment I design it, I can't audit it.
