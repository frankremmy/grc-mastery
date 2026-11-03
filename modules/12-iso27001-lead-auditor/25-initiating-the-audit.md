# Lesson 25 — Initiating the audit

## Summary

Once the programme manager assigns an audit, the audit team leader runs it through to completion. Initiating the audit involves two activities:

1. **Contact the auditee.** Confirm the following:
   - Who represents the auditee, and that there is authority to audit.
   - The objectives, scope, criteria and methods.
   - The team and any technical experts.
   - Dates, locations and duration.
   - Which people are available, and what access you will have to systems and records.
   - Confidentiality, safety and site-access rules.
   - Whether guides, observers or interpreters will attend.

   For ISO 27001, ask for the planning information: ISMS scope, organisational structure, policies, risk assessment, risk treatment plan, Statement of Applicability (SoA), and previous audit results. Raise any conflicts of interest now.
2. **Decide whether the audit is feasible.** This rests on four things:
   - enough information,
   - enough cooperation,
   - enough time and resources,
   - nothing external that would prevent the audit.

   If the original arrangements won't work, options include changing the date, duration, scope, methods or team, auditing remotely, adding a technical expert, or postponing. Don't carry on unchanged when the objectives can't be met.

## Key concepts

| Feasibility factor | Example of failure | First response |
|---|---|---|
| Information and access | Key records missing, criteria unclear, systems or sites restricted | Look for alternative evidence before calling the audit infeasible |
| Cooperation | Access to people or systems refused | Escalate to the audit client. Without access, the audit can't conclude |
| Time and resources | Window too short, no expert available, remote setup unreliable | Extend the duration or re-scope |
| External circumstances | Major outage, emergency, travel restriction, serious incident | Reschedule, or move parts to remote |

The test is not whether the audit *can start*. It is whether the team can *reach reliable conclusions* against the objectives.

## Where this shows up in a real job

- **The first email to the auditee is effectively a document request list.** Scope, SoA, risk register, risk treatment plan, last internal audit report, management review minutes, and the nonconformity log. This is the evidence tracker from earlier lessons, sent out ahead of time.
- **Reading the SoA and risk register before fieldwork shows where to sample.** In the Stark files, the SoA contradicts the asset register. I would have spotted that during preparation, before I ever met the auditee.
- **An incident shortly before the audit doesn't automatically make it infeasible.** If people are available, it is often the best evidence you will get that the incident process (A.5.24–5.28) actually runs.

## Where I'd push back

- **The audit team leader recommends whether the audit is feasible. They don't decide alone.** The lesson presents feasibility as the lead auditor's call. Under ISO 19011, if the audit isn't feasible, the team leader proposes alternatives to the audit client, consulting the auditee. Changes to scope or objectives are agreed with the client and the programme manager, because they affect the whole programme.
- **Team selection belongs to the programme manager.** The transcript says the lead auditor selects team members, but the programme lesson gave that job to the programme manager. The team leader confirms the team is suitable and asks for changes, for example over competence or conflicts. They don't pick the team from scratch.
- **Changing scope is where integrity gets tested.** An auditee who asks to "drop the cloud environment, it's not ready" is trying to remove the area most likely to produce findings. If scope changes, record the reason and the excluded area in the audit plan and the report. For a certification audit, the ISMS scope on the certificate can't silently grow larger than the scope that was actually audited.
- **Confidentiality can rule out sending documents in advance.** An auditee may refuse to send the risk register off-site. That is a valid control, not a lack of cooperation. Review the register on-site or by screen-share instead. This is the "consider alternative evidence" rule applied from the other side.

## My take

Initiation is a scoping conversation with a go/no-go decision at the end. The habit worth keeping is to write down the feasibility check: what you asked for, what you got, and what you changed. If the report later states a limitation, the reader can see it was identified at the start and not found too late to fix.
