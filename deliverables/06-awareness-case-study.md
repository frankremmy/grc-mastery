# Security awareness program case study — Kentucky Wesleyan College

**Module:** 06 — Security Education and Awareness
**Type:** Practical case study
**Source:** Kentucky Wesleyan College, *Security Awareness Program Plan*, version
1.1 — published at
<https://intranet.kwc.edu/_uploads/sites/3/PLAN01-Awareness-Program-Plan.pdf>.
Linked rather than copied here: publicly available, but KWC's document to
redistribute, not mine.
**Status:** Study notes on the plan. Assessment answers to follow.

---

## The plan at a glance

| Attribute | Value |
| --- | --- |
| Document | Security Awareness Program Plan |
| Issue date | 1 May 2022; effective 1 January 2023 |
| Version | 1.1 |
| Owner | Director of Information Technology |
| NIST control family | **AT** (Awareness and Training) |
| Basis | NIST SP 800-16 and NIST SP 800-50 |
| Authorship | v1.0 drafted by GreyCastle Security (external); v1.1 reviewed, finalised, approved and published by KWC |

Note the control mapping: the plan is explicitly tied to **AT**, the awareness and
training family in the 800-53 catalogue — which links this case directly to the
control catalogue held in `reference/`.

---

## Scope

Covers all departments, divisions, locations, roles and responsibilities. Intended
audiences include **employees, faculty, and vendors/third parties** — and the plan
states that an awareness programme should reach all levels of the organisation,
**including senior management**.

Two things worth marking: third parties are in scope (the contractor gap the
module warns about is closed here, at least on paper), and so are executives.

The plan also says success relies on awareness becoming **part of the
organisation's culture**, not just on explaining correct behaviours.

## Program considerations

The design factors the plan says were taken into account:

- Who is responsible for implementing and maintaining the programme
- Timeframe for new-hire training completion
- Any compliance or regulatory driver
- Frequency of training and testing (annual, quarterly, monthly)
- Content type and delivery method
- Which groups and individuals to include
- Time constraints and availability
- **Senior leadership buy-in**
- **How non-compliance will be handled and enforced**

Delivery runs over one year and may include instructor-led training,
computer-based training using quizzes, tests or videos, and social engineering.
Role-based training is anticipated for specific audiences.

## Roles and responsibilities

Everything sits with the **Director of Information Technology**, who is
responsible for:

- Implementing, developing and maintaining the programme
- Coordinating with departments to ensure participation and completion
- Tracking attendance in personnel files, and filing attestations and
  post-training quizzes or tests
- Scheduling and conducting on-site training, on-site table events, computer-based
  training, and performing social engineering testing

## Training strategy

**Baseline:** general security awareness training **at least annually** for all
employees. New hires have **30 days** to complete it.

**Core module:** computer-based, based on NIST SP 800-16, **15–45 minutes**.
Minimum content:

- Current threats and common attacks
- Data protection
- Security policies and procedures
- Privacy
- Best practices for passwords, email, web browsing, mobile devices, social media,
  wireless networks, antivirus, social engineering (phishing and vishing), and
  physical security
- Identifying and responding to incidents

**Additional role-based training**, computer-based, targeting groups with
specialised roles, privileges or risks. Topics may include HIPAA, FERPA, data
classification handling, cyber security for IT, **cyber security for senior
management**, cyber security for travellers, Gramm-Leach-Bliley, and GDPR.

## Metrics

The plan says metrics should measure overall **human risk and behaviour**, confirm
regulatory compliance, and show whether **behaviour is changing**. Listed metrics:

- Number of employees who attended the last training
- **Number of users reporting phishing attacks**
- Number of users falling victim to phishing attacks
- Number of users who fail sanctioned phishing tests

It adds that further assessment may be needed to capture overall effectiveness.

**Training records** are kept per the college's security risk assessment guidance,
and are available to HR on demand.

## Testing and assessment

Social engineering is defined in the plan as psychological manipulation of people
into performing actions or divulging confidential information — a confidence trick
that is often one step in a larger fraud scheme.

Tests are to run **on a regular basis** to continuously measure susceptibility, in
two formats:

- **Phishing** — emails with links, attachments and other requests
- **Physical** — impersonation or intrusion into access-controlled areas, or a
  walk-through of office space to detect security deficiencies or violations

Results are incorporated into the programme and tracked. The Director of IT owns
follow-up and further training.

## Non-compliance

The Director of IT works with HR to ensure completion. The escalation path:

1. Employee is notified of non-compliance and given a **2-week extension**.
2. Failure after the extension — the employee's **manager or supervisor** is
   notified.
3. Continued failure **may lead to loss of access** to college systems, and/or
   further sanctions as HR deems appropriate.

## Timeline

**Training plan**

| Title | Audience | Sessions | Frequency |
| --- | --- | --- | --- |
| Security Awareness Proficiency Assessment | All faculty, staff | 1 | Annually |
| Security Awareness Training | All faculty, staff | 1 | Ongoing |
| Incident Response Tabletop | Information Technology team | 1 | Annually |

**Testing plan**

| Type | Format | Number of tests | Frequency |
| --- | --- | --- | --- |
| Social engineering | Phishing | **Bi-weekly** | Ongoing |
| | Physical observation checks | Continuously | Ongoing |

## References cited by the plan

- NIST SP 800-16, *Information Technology Security Training*
- NIST SP 800-50, *Building an Information Technology Security Awareness and
  Training Program*

---

## Observations for the assessment

Points that look likely to matter when the questions arrive.

**Strengths against what module 6 teaches:**

- Third parties and vendors are explicitly in scope — the contractor gap is
  addressed.
- Senior management is explicitly in scope, and has its own role-based module.
- **Report rate is a named metric** — "number of users reporting phishing
  attacks" — which the course's own lessons never reached.
- The stated purpose of metrics is whether *behaviour is changing*, not merely
  completion.
- Annual minimum with a 30-day new-hire window; a defined, enforced non-compliance
  path.
- Multiple delivery formats, plus role-based training layered on the baseline.
- Physical social engineering is tested, not just email.

**Weaknesses and open questions:**

- **Everything depends on one person.** The Director of IT develops, delivers,
  tracks, tests and follows up. No second line, no independent check, and a clear
  key-person risk — and the person running the tests also reports on their results.
- **Bi-weekly phishing tests is very frequent** — far beyond the six-to-twelve
  months the module recommends, and likely to produce fatigue and resentment
  rather than learning.
- **No targets or thresholds.** Metrics are listed but no acceptable levels are
  defined, so there's no way to tell a good result from a bad one.
- **No content review cycle.** Nothing states when the training material itself
  gets refreshed — the exact failure the module describes with a decade-old module.
- **Tracking in personnel files**, with records available to HR, and manager
  notification for non-completion. That's compliance enforcement, and it sits
  uncomfortably close to the culture the plan says it wants. Worth distinguishing
  failure to *complete training* from failure on a *phishing test* — the plan's
  non-compliance section covers the first; the risk is it bleeding into the second.
- **Version and date inconsistency.** The cover page shows version 1.1 issued
  1/5/2022 with no revision date; the page headers say version 1.0 effective
  1/1/2023; the revision table shows 1.0 as the initial draft and 1.1 as reviewed
  and approved with no date recorded. Minor, but it's a document control finding in
  a document whose own currency matters.
- **SP 800-16 and SP 800-50 are the cited basis**, and both are old — worth
  checking whether either has been superseded before relying on the mapping.
- No mention of what happens to the reporting channel: the plan counts reports but
  never describes how someone reports, or what response they get.
