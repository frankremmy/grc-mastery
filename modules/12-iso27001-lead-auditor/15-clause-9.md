# Clause 9 — performance evaluation

> Module 12, lesson 15. _Measuring the ISMS, auditing it independently, and
> getting management to review it on the record._

## What clause 9 asks for

| Requirement | What it means | Stark document |
| --- | --- | --- |
| 9.1 Monitoring, measurement, analysis and evaluation | Measure whether the ISMS meets its objectives — KPIs | **Monitoring, Measurement, Analysis and Evaluation Procedure** |
| 9.2.1–9.2.2 Internal audit | An independent internal audit programme | **Internal Audit Programme** |
| 9.3.1–9.3.3 Management review | Top management reviews the ISMS, with inputs and outputs recorded | **Management Review Procedure** and an agenda and minutes tracker |

Clause 9 is the *Check* in Plan–Do–Check–Act: did what we did actually work?

## 9.1 — monitoring and measurement

The objective is to check the clause 6.2 objectives were met, as quantitatively as
possible, and to feed the management review. Many organisations do this as a
spreadsheet; for Stark it's a procedure with a KPI table inside.

The scope point matters: this measures **what's in the ISMS scope**, not all of
the organisation's security activity.

**The KPI table:**

| Area | Frequency | Owner | Target |
| --- | --- | --- | --- |
| ISMS objectives | Quarterly | IS Manager | At least 80% achieved |
| Security incidents | Monthly | Security Analyst | Zero critical incidents |
| Access control reviews | Quarterly | Infra Engineer | No unauthorised access |
| Training completion | Quarterly | GRC Analyst | 100% |
| Backups | Monthly | Infra Engineer | 100% success |
| Patch management | Monthly | Infra Engineer | Critical patches within SLA |
| Secure code review | Each major release | Developers, GRC | No unresolved critical findings |
| Vulnerability scans | Quarterly | Security Analyst | High and critical remediated |
| Penetration tests | Annual or major release | External vendor | High and critical remediated |
| Audit findings | Annual | Internal audit | Zero major nonconformities |
| Log review | Daily | Security Analyst | All anomalies resolved |

The targets are illustrative; in practice they'd be set from real baselines.

**Methods of analysis:** trend analysis, root cause analysis, KPI dashboards, and
comparison against objectives and baselines — ten critical vulnerabilities last
quarter, zero this quarter, is a result you can show.

**Records** are the part an auditor tests. "We reduced incidents" invites "show
me" — an incident log, scan reports with remediation status, training completion
records, access review records.

## 9.2 — internal audit

**Independence is the whole problem for a small company.** Internal audit must be
impartial, so the person who implemented the ISMS can't audit it — that would be a
self-assessment, not an audit. Stark has no separate risk or audit function, so
the realistic answer is an external consultant.

**That consultant can't be the certification body.** The ISMS gets audited at
least twice by different parties: once internally, then by the body that issues
the certificate. Hire one firm for internal audit, a different one to certify.

Usually the firm doing the internal audit writes the plan. The Stark programme is
a template for when it falls to you — or for a large organisation with its own
second- and third-line audit staff.

**Why it matters for certification:** the internal audit finds the
**nonconformities** — mandatory requirements not met, or SoA controls not
implemented properly — so they're fixed before the external audit. From the
external auditor's side, the internal audit report is one of the first things
read after the scope and SoA. A credible report with findings that were
remediated says the ISMS is in good shape. A thin report from an unknown provider
with zero findings says the opposite.

**What the programme covers:**

- **Objectives:** verify conformity with ISO 27001; identify nonconformities,
  risks and **opportunities for improvement**; confirm objectives are met; and
  validate the **effectiveness** of SoA controls
- **Frequency:** the full scope annually, plus targeted audits after major
  changes, significant incidents, or management decisions. Annual is the usual
  balance; large organisations may audit selected areas every six months
- **Independence:** auditors independent of the *area* being audited — not
  necessarily of the organisation. External help for complex areas
- **Methods:** document review, interviews, observation of control
  implementation, sampling of records, testing of operational controls
- **Records:** plan, checklists and working papers, evidence, reports,
  corrective action requests and follow-up — the external auditor audits these too
- **Reporting:** to management within 14 days; corrective actions tracked;
  results feed the management review

**Three kinds of output.** A *nonconformity* blocks certification. A *risk* may
be acceptable under the criteria but still worth fixing. An *opportunity for
improvement* doesn't affect certification — a training programme with 100%
completion that's badly out of date — but management should see it.

**Effectiveness, not just design.** The lesson's pro tip, and it's the
operating-effectiveness point from the audit module: a vulnerability management
process that exists on paper is design. Whether the scans find what they should,
and whether they're authenticated, is effectiveness. An internal auditor who only
reads documents hasn't done the job — and the external auditor will look at the
technical implementation regardless.

## 9.3 — management review

Management has to know how the ISMS is doing, so nothing in the external audit
surprises them, and has to see the nonconformities, because fixing them may need
money or more time.

**Evidence is the requirement.** "Management was on the call" isn't evidence.
Agendas, attendance and minutes showing who, what, when and how often are.
More frequent isn't automatically better — the aim is a pragmatic rhythm.

**Inputs** the procedure lists: internal audit results; stakeholder feedback;
incidents, breaches and nonconformities; monitoring results; risk assessment and
treatment updates; corrective action status; changes in internal and external
issues; progress on objectives; resource needs.

**Outputs:** decisions on improvement, updates to the risk treatment plan and SoA,
resource allocation, policy approvals, and new risks or opportunities. Even a
review that changes nothing needs a record that management approved that.

**The GRC skill this clause depends on:** translating incident data into business
language. Not "here are the incident reports", but "five critical incidents, here
is what they meant for the business, and here is whether they threaten the sales
objective". That's the job.

**The budget point** is the one I'd remember: if something keeps appearing in
audit reports and management reviews, it's already known by the time budgets are
set — which makes asking for money much easier.

## Where I'd push back

**The management review procedure cites the 2013 standard.** It lists "status of
corrective *and preventive* actions (Clause 10.1)" as an input. Two problems: in
ISO 27001:2022, nonconformity and corrective action is **10.2**, not 10.1 — 10.1
is continual improvement, and the order changed in 2022. And "preventive action"
was removed from the standard in 2013, replaced by risk-based planning in
clause 6. Both are small, but a document claiming 2022 alignment that uses 2013
terminology is the kind of detail an auditor notices.

**The internal auditor is appointed by the person being audited.** The programme
says the Information Security Manager assigns auditors. The ISM leads the ISMS
implementation — they're the person with most at stake in the audit result.
Appointment should sit with top management, which is a one-word fix that removes
an obvious independence question.

**The 99.9% uptime objective isn't measured.** Clause 6.2 set platform
availability as an objective, and 9.1 exists to measure the 6.2 objectives. The
KPI table has backups and patching but no availability metric. The same goes for
"keep the risk register up to date". Every 6.2 objective should have a row in 9.1;
otherwise one of them can't be shown to have been achieved.

**Some targets reward the wrong thing.** "Zero critical incidents" as a KPI
quietly penalises detection — the better the monitoring, the worse the number
looks, and the incentive is not to report. Mean time to contain, or the
proportion of incidents handled within the response SLA, measures what the
organisation actually controls. "No unauthorised access" has the same problem:
access reviews can show permissions were reviewed and corrected, not that nothing
unauthorised ever happened.

**The audit criteria include obligations clause 4 said don't exist.** The
programme audits against "legal, regulatory and contractual obligations relevant
to the SaaS platform". The clause 4 scope document says there are none. One of
the two is wrong — and I'd argue it's clause 4, as I did in my notes on it.

## My take

**Clause 9 is where an ISMS proves it's a system.** Everything up to clause 8 can
be true on paper. Clause 9 asks for numbers, an independent opinion, and
management's signature on both — and the records only exist once the ISMS has run
for a while. That's why a young ISMS has its thinnest evidence here.

**The two-audit structure is worth stating clearly in an interview.** Internal
audit and certification audit are different parties by design, and the
certification body can't be the one that helped you prepare. That separation is
what makes the certificate mean anything — it's the same independence logic as
the three lines of defence, applied to the standard itself.

**The KPI design point generalises.** A metric should measure something the
organisation controls and should improve when the organisation improves. "Zero
incidents" fails both tests. It's the same lesson as the phishing click rate
versus report rate in module 6.

**Repo note:** the three course procedures and the meeting tracker stay out of
the repo. Mine go into the Stark ISMS set.
