# Lesson 24 — Implementing, monitoring and improving the audit programme

## Summary

After the programme is set up, it is delivered through individual audits. For each audit, the programme manager:

- sets the audit's objectives, scope and criteria
- chooses the methods and the team
- appoints the audit team leader early
- manages the results and records
- monitors and improves the programme itself

The instructor's main point is to plan methods and people at programme level. If you know there are foreign data centres you can't travel to, plan remote auditing, access and confidentiality from the start. If you know specific applications will be audited, line up technical experts ahead of time. An individual audit plan should never be where these needs first come to light.

## Key concepts

**Objectives, scope and criteria** for each audit:

| | Answers | Examples |
|---|---|---|
| Objectives | What is this audit for? | Conformity, effectiveness, risk management, verifying corrective actions, legal/contractual requirements, improvement |
| Scope | Where are the boundaries? | Locations (physical and virtual), units, processes, systems, services, period covered |
| Criteria | What do we compare the evidence against? | 27001 requirements, policies, objectives, risk treatment, SoA, legal and contractual obligations |

**Methods.** Interviews, document and record review, observation, system examination, data analysis, sampling, remote demonstrations, secure remote access, site visits.

- Remote work brings risks around connectivity, identity, confidentiality and limited observation.
- On-site work brings travel, safety and security risks, and disrupts operations.

**Team.** The team as a whole has to cover the competence the audit needs: technical, sector, management system, legal, language, audit tooling, and independence. A technical expert brings specialist knowledge but is not an auditor. Auditors in training work under supervision.

**Results and records.** The programme manager:

- confirms the audit's objectives and scope were covered
- controls who receives the reports
- follows up on actions
- looks across audits for recurring weaknesses

Records are sensitive, so access, storage, transfer, retention, backup and disposal all need controls.

**Monitoring and review.** Check more than whether audits happened. Check whether they were effective and reliable: schedule kept, objectives achieved, auditor performance, feedback, quality of documentation, risks managed. Things that should trigger a change include significant findings, incidents, changes to the ISMS, new legal requirements, supplier changes, new technology and conflicts of interest.

## Where this shows up in a real job

- **Data analysis can beat sampling.** For a leaver-access check, compare the full HR leavers list against the directory's disabled accounts. That tests 100% of the population and removes sampling risk altogether. Sample when you can't analyse the full set, not as a reflex.
- **"View, don't take" for remote audits.** In a screen-share walkthrough, the auditor sees the evidence without receiving copies of sensitive data. Record the screenshot reference, not the customer data.
- **The programme review uses the same loop as the ISMS.** The audit function improves itself the way clauses 9 and 10 make the ISMS improve: monitor, review, act on findings.

## Where I'd push back

- **The instructor's example timeline mixes two programmes again.** "Initial audit in 3 months, Stage 2 in 6 months" combines the organisation's internal programme with the certification body's programme. Stage 1 and Stage 2 belong to the certification body. The organisation's programme should have its internal audit and management review *finished before* Stage 1, because the certification body expects to see them.
- **Remote auditing for certification has its own rules.** Certification bodies follow IAF MD 4 when they use ICT to audit. Some evidence can't be properly verified remotely, physical controls (A.7) for example, so the report has to state that as a limitation. That's the fair-presentation principle again.
- **A technical expert can't own a finding.** The expert advises. The auditor evaluates the evidence against the criteria and writes the finding. A report that says "the expert found X" without the auditor's own evaluation leaves the finding without anyone accountable for it.

## My take

This lesson is project management with an audit vocabulary. The useful habit is front-loading. Any requirement that would derail an individual audit belongs in the programme: remote sites, specialist systems, confidentiality arrangements, auditor independence. A lead auditor who finds these needs in the opening meeting has inherited a programme that wasn't planned properly.
