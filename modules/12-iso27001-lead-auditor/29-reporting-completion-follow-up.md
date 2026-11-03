# Lesson 29 — Reporting, completion and follow-up

## Summary

The last three activities are the audit report, the closing meeting, and follow-up on any nonconformities.

**The audit report** is the formal record of the audit and must make sense on its own. It includes:

- objectives, scope and criteria
- the audit client, team and auditee representatives
- dates and locations
- findings and conclusions
- significant limitations and unresolved disagreements
- a statement that the audit was based on sampling

It must be accurate, concise, evidence-based and consistent with what the auditee was told during the audit. It must leave out unsupported opinions, unnecessary confidential data, findings the auditee never heard about, and prescribed fixes. Before issuing it, the lead auditor checks that evidence supports every finding, that criteria are referenced correctly, that the conclusions follow from the findings, and that confidentiality is protected. It goes only to authorised recipients, within the agreed timeframe.

**The closing meeting**, chaired by the lead auditor, presents the findings, classifications, conclusions and limitations, plus reporting, corrective action and follow-up arrangements, any disagreements, and recommendations where these are permitted. The auditee can ask questions and offer additional evidence.

**Completion** means the agreed activities are done and reported. Audit information is then kept or disposed of according to programme, contract, legal and confidentiality requirements, and lessons learned are fed back.

**Follow-up.** The auditee owns the correction (fixing the problem) and the corrective action (removing the cause). The auditor verifies that the action was *implemented* and that it was *effective*. The method should match how significant the finding is. Completing an action does not prove it worked.

The course provides three example records. I describe them here rather than reproduce them:

- **D1 — Final audit report.** Objectives, scope and criteria; summary of methods, sampling and coverage; F01 (minor NC, privileged access removal) and F02 (conformity, backup); a conclusion that the ISMS conforms subject to correcting F01; corrective action within 30 days; report control and approval.
- **D2 — Closing meeting record.** Agreed findings and conclusion, follow-up action and verification, and stakeholder confirmation.
- **D3 — Corrective action and follow-up record.** Root cause: HR leaver and mover notifications were not triggered on time. Corrective action: workflow improved, owned by the IT Operations Lead. The auditor verified the records, and the status is closed.

## Key concepts

| | Correction | Corrective action | Follow-up verification |
|---|---|---|---|
| Question | Is the immediate problem fixed? | Is the cause removed? | Was it done, and does it work? |
| Example (F01) | Remove the lingering privileges | Fix the HR-to-IT notification trigger | Re-sample leavers and movers since the change |
| Owner | Auditee | Auditee | Auditor |

## Where this shows up in a real job

- **The report must stand on its own.** A customer's TPRM analyst, the certification body or a regulator may read only this document. That's why it repeats scope and criteria from the plan. In module 9, when I asked Horizon Labs for "the audit report", this is what I needed.
- **Follow-up depends on severity.** A minor NC is often verified with documents, remotely or at the next surveillance audit. A major NC usually needs a dedicated verification, often on-site, before certification.

## Where I'd push back

- **The order in the transcript differs from 19011.** The transcript says "finish the report, then take them through it in the closing meeting". The lesson text and ISO 19011 put the closing meeting first, then the report. Both work in practice if the meeting uses a *draft*. Under the "no surprises" rule, the issued report can't contain anything the closing meeting didn't cover, whichever order is used.
- **The corrective action is owned by the wrong team.** The root cause sits in HR (notifications not triggered on time), but the action belongs to the IT Operations Lead. The fix should include HR or the HR-to-IT integration, such as an automated trigger from the HRIS. If not, IT has improved its side of a handoff whose broken half it doesn't control. I would ask how the corrective action addresses the cause that was identified.
- **"Closed" after 30 days may only prove the fix was implemented.** It doesn't necessarily prove the fix works. Effectiveness means new leavers and movers processed on time *after* the change. If few or none left during the 30 days, there's no population to test. In that case the honest status is "implemented, effectiveness to be verified at the next audit". This is the lesson text's own point: completion is not effectiveness.
- **"Subject to correction" depends on the type of audit.** For a Stage 2 audit with only a minor NC, certification bodies normally need an *accepted corrective action plan*, not a closed and verified fix, before they decide on certification. Full verification usually happens at the first surveillance audit. The example handles F01 the way a major NC would be handled. That's stricter than required. It isn't wrong, but it's worth knowing the difference for the exam.
- **The conclusion inherits the open audit trail from lesson 28.** The report says sampling was sufficient. Yet the "isolated or systematic?" trail was never shown to be closed. A report reviewer should check that before signing.

## My take

The report is the one artefact that outlives the audit, so it has to stand alone. Every statement in it should trace back to the working papers. The follow-up record is where audits most often go easy: something was done, so the item gets closed. I'll keep the two questions separate: did they do it, and did it fix the cause? For root causes that span teams, like HR to IT, I'll check that the corrective action reaches the team that owns the cause.
