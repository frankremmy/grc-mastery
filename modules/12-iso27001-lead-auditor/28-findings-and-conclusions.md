# Lesson 28 — Developing findings and conclusions

## Summary

Once the evidence is collected, the team evaluates it against the audit criteria. An **audit finding** is the result of that comparison. It can be a conformity, a nonconformity, legal compliance or non-compliance, good practice, or an opportunity for improvement (OFI). Every finding should link three things:

1. **the criterion**, meaning the requirement
2. **the objective evidence**
3. **the evaluation**, meaning how the evidence shows the requirement was or wasn't met

Personal opinion has no place in a finding. A nonconformity describes the problem and doesn't prescribe the fix. Classification (major or minor) follows the defined criteria, not the auditor's instinct.

The lead auditor reviews each proposed finding for the right criterion, enough evidence, accurate wording, justified classification, and whether it falls within scope. Each finding is then retained, revised, reclassified or withdrawn. Potential nonconformities are discussed with the auditee to check the facts, but the auditee doesn't have to agree. Disagreements are settled on evidence, not on pressure or seniority, and any that stay unresolved are recorded.

Recommendations are allowed only if they are non-binding. Auditors must not design processes, select controls, write corrective actions or make management decisions. The **audit conclusion** weighs every finding against the objectives, scope coverage and limitations. It must not claim more confidence than the evidence supports.

The course provides three example internal records, described here rather than reproduced:

- **C1, interview, evidence and sampling record.** Interview questions and answers, the objective evidence checked, the result, a sampling table, audit trails, and the auditor's assessment.
- **C2, findings and nonconformity record.** F01 is a nonconformity graded minor (privileged access kept after a role change or termination). F02 is a conformity (backup). Also covers nonconformity details and the communication log.
- **C3, team debrief.** Activities complete, sampling sufficient, no conflicts, positive practice noted (backup testing), findings confirmed, team sign-off.

## Key concepts — the evidence chain in the example

| Step | Privileged access approval | Leaver/role-change removal |
|---|---|---|
| Interview claim | Manager approval, reviewed quarterly | IT removes access when HR notifies them |
| Evidence checked | Procedure, privileged access register, approvals, quarterly reviews | Termination and role-change records, system access logs |
| Sample | 6 of 42 privileged accounts (judgement) | 4 of 12 recent leavers/movers (judgement) |
| Exception | One role change kept privileges for 8 days | One delayed removal |
| Audit trail | — | Expand the sample: is this an isolated slip or a systematic failure? |
| Result | Conformity | F01, minor nonconformity |

The interview tells you where to look. The records are what decide the finding.

## Where this shows up in a real job

- **Writing the finding statement.** Use the pattern *requirement → evidence → gap*. For example: "Policy X requires privileged access to be removed within N days of a role change (A.5.18, A.8.2). In 1 of 6 sampled privileged accounts and 1 of 4 sampled leavers, access remained for up to 8 days." No adjectives, no fix.
- **Good practice belongs in the report.** It isn't flattery. It is fair presentation. It also tells the certification body which areas are mature.
- **The difference from a pen test report.** A pen test reports what an attacker could do. An audit reports which requirement wasn't met and the evidence for it. The same leaver-access issue can appear in both, written in different ways.

## Where I'd push back on the example records

- **The audit trail isn't closed.** C1 says to expand the sample to decide whether the delay was isolated or systematic. C2 then says no further evidence is needed and grades the finding minor. That grade depends on the answer to the isolated-or-systematic question. If the expanded sample turned up more failures, the leaver process isn't working, and that could reach a major nonconformity under typical criteria. The record needs to state the expanded sample's size and result before it can justify "minor".
- **"It should have been removed right then and there" is an opinion unless the policy says so.** The criterion is the organisation's own required timeframe, which A.5.18 and A.8.2 leave the organisation to define. If the policy allows 10 days, an 8-day delay is a conformity. The finding has to quote the timeframe.
- **The populations are small enough to test in full.** All 12 leavers and movers, and even all 42 privileged accounts, can be checked by comparing the HR list against the identity provider export. Judgement sampling on a population of 12 adds sampling risk for no benefit, and it hands the auditee the "unlucky sample" argument.
- **Use the right control again.** Privileges kept after a role change are A.8.2 *Privileged access rights* together with A.5.18 *Access rights*. Termination adds A.6.5. A.8.3 doesn't fit well.
- **Whose classification criteria apply depends on the audit.** In a certification audit, the certification body's major/minor definitions apply, which is what the assessment will give me. In an internal audit, the organisation's own procedure applies (my Stark clause 10 note asked for one). The lesson text says "the organisation's defined criteria", but the transcript points to the certification body's. Both are right, for different audits.

## My take

A finding is a three-part sentence: requirement, evidence, gap. If any part is missing, the finding is either opinion or trivia. The hardest discipline here is closing every audit trail before classifying, because the severity often depends on the trail I'm tempted to skip when time is short. Where the population is small, I would test all of it rather than sample.
