# Oscorp cyber security programme and three-year roadmap

**Capstone:** NIST Cyber Security Framework assessment and programme design
**Type:** Capstone deliverable
**Status:** My own work, completed before seeing the course solution.
**Companion file:** [`capstone-oscorp-nist-assessment.xlsx`](capstone-oscorp-nist-assessment.xlsx)

**Brief.** Norman Osborn has offered me a full-time Senior Cyber Security
Consultant role at Oscorp, conditional on designing a comprehensive security
programme that identifies current deficiencies and sets a three-year roadmap to
uplift Oscorp's security posture.

---

## 1. Executive summary

Oscorp scores **20 of 98 NIST CSF control descriptions as implemented (20%)**.
The distribution matters more than the total:

| Function | Pass | Fail | Total | Coverage |
| --- | ---: | ---: | ---: | ---: |
| Identify | 2 | 22 | 24 | **8%** |
| Protect | 13 | 22 | 35 | 37% |
| Detect | 3 | 15 | 18 | **17%** |
| Respond | 0 | 15 | 15 | **0%** |
| Recover | 2 | 4 | 6 | 33% |
| **Total** | **20** | **78** | **98** | **20%** |

Four of the Protect passes are *not applicable* rather than implemented — Oscorp
writes no software and runs no on-premises servers — so real control coverage is
lower than 20% suggests.

**The single most important finding is the shape of that distribution.** Oscorp
has bought good technology and built genuinely strong physical security, but it
has almost no capability to *know* what is happening and no capability at all to
*respond* when something does. A zero in Respond is not a gap among gaps; it
means that on the day Oscorp has a serious incident, there is no plan, no defined
roles, no escalation path, no forensics capability and one generalist analyst
working business hours.

Underneath that sits a governance problem that explains most of the rest: **nobody
owns security.** Roles are undefined, there is no security strategy, no security
policy, no cyber risk process, and the security analyst reports to the IT manager
— which makes the function assessing the controls a subordinate of the function
that builds and operates them.

### What is genuinely strong

Worth stating plainly, because the roadmap should not disturb it:

- **Physical security.** Secure facility, CCTV, extensive personnel vetting, 24/7
  monitoring of research labs. For a business whose crown jewel is research, this
  is the right place to have been serious
- **Business continuity and disaster recovery.** Documented plans, regular DR
  testing, tested backups. Rare at this maturity level and the foundation for
  ransomware recovery
- **Network architecture.** Palo Alto NGFW, regularly updated and annually
  reviewed, VLAN segmentation, current network diagrams including cloud
- **Standard build.** An SOE image keeps the laptop fleet on a current Windows
  baseline

### The five deficiencies that matter most

1. **No incident response capability** — nothing in Respond, and no plan to invoke
2. **No detection** — no SIEM, no log aggregation, no monitoring beyond Defender alerts
3. **Shared administrator credentials and no MFA** — the two highest-impact access control failures, and the cheapest to fix
4. **No cyber risk process and no security governance** — nothing decides what gets fixed first, and no one is accountable
5. **No third-party risk management** — Oscorp's key critical application is a SaaS service from Horizon Labs, a supplier separately assessed as carrying material security risk

---

## 2. Method and scoring rule

Each control description was assessed Pass or Fail against the current-state
notes, with the reasoning recorded in the Comments column.

**The rule I applied:** a control passes where the notes affirmatively evidence
its substance. It fails where a material element is absent, contradicted, or
merely asserted without a supporting process.

Three consequences worth stating, because they explain most of the harsh marks:

- **Silence is not a pass.** Where the notes say nothing, the control fails, and
  the comment records that it is an assumption rather than a finding
- **An artefact without a process fails.** The laptop spreadsheet exists; nothing
  reviews it. Qualys is owned; nothing schedules it. Both fail controls that ask
  for a maintained inventory and a vulnerability management programme
- **Partial credit is recorded, not awarded.** Where one half of a control is met
  — encryption at rest is default in Azure, DR testing is regular, staff vetting
  is thorough — the comment says so and the verdict still reflects the missing
  half

Controls that do not apply are marked Pass and labelled NOT APPLICABLE, so they
can be excluded when reading the coverage figure.

---

## 3. Three-year roadmap

The roadmap is sequenced by dependency, not by severity. Several urgent things
cannot be done well until less urgent things exist — you cannot monitor an estate
you have not inventoried, and you cannot prioritise remediation without a risk
process to rank it.

### Year 1 — Accountability, visibility and the cheap wins

*Theme: decide who owns security, find out what Oscorp has, and close the
highest-impact gaps that cost almost nothing.*

**Q1 — Ownership and immediate risk reduction**

| Initiative | Why first |
| --- | --- |
| **Establish security ownership.** A Head of Security accountable for the function, reporting outside the IT line | Every other failure traces back to nobody owning this. Reporting into the IT manager means security assesses its own parent function |
| **Deploy MFA across all accounts**, prioritising administrative and remote access | The single largest risk reduction available to Oscorp. Entra ID licensing is already owned; this is configuration, not procurement |
| **Eliminate the shared administrator password.** Individual named admin accounts, credentials rotated | Shared credentials mean no accountability, no attribution, and no ability to investigate. Immediate and free |
| **Determine regulatory applicability.** Confirm NIS2 status (Annex I covers pharmaceutical manufacture) and GDPR obligations with legal | Deadlines and obligations cannot be met by an organisation that has not established which apply to it |

**Q2 — Foundations**

| Initiative | Why |
| --- | --- |
| **Information security policy set**, with a data classification scheme | Nothing can be classified, handled or enforced without it. Prerequisite for DLP, labelling and asset prioritisation |
| **Asset inventory**, extended beyond laptops to the SaaS estate, cloud services and network devices, with owners, classification and a review cycle | Prerequisite for vulnerability coverage, monitoring scope and third-party risk |
| **Cyber risk management process** — register, assessment methodology, risk appetite statement, and a route for risks to reach the board | Creates the mechanism that decides what years 2 and 3 actually prioritise |

**Q3 — Response and the human layer**

| Initiative | Why |
| --- | --- |
| **Cyber incident response plan**, with defined roles, categorisation, escalation and regulatory notification timelines; supported by an external IR retainer | Respond scores zero. A retainer buys the forensics capability Oscorp cannot justify hiring |
| **Security awareness programme** with refresher training and phishing simulation | Quantified separately at roughly €107,000 net annual benefit, break-even at an 18% reduction |
| **Formalise vulnerability management.** Scheduled authenticated Qualys scans, defined remediation SLAs by severity, and a burn-down plan for the existing high and severe backlog | Qualys is already paid for and currently produces findings nobody acts on |

**Q4 — Close the loop**

| Initiative | Why |
| --- | --- |
| **Third-party risk management process** — supplier inventory, tiering, assessment questionnaire, contractual security clauses | Horizon Labs is a tier 1 supplier holding research data, already assessed as materially risky, with no contractual remedy available |
| **Access reviews and least privilege.** Periodic recertification, role-based access, removal of standing privilege | Follows the asset inventory and classification work |
| **First penetration test**, scoped to the external perimeter and the M365/Azure tenant | Establishes an independent baseline once the obvious gaps are closed |

**Year 1 exit criteria:** security has a named owner; MFA is universal; no shared
admin credentials; an incident response plan exists and has been walked through;
an asset inventory and classification scheme exist; a risk register is live and
reported; vulnerability scanning is scheduled with SLAs.

### Year 2 — Detection, response maturity and data protection

*Theme: build the capability to see and react. Year 1 reduced exposure; year 2
makes Oscorp able to detect what still gets through.*

| Initiative | Notes |
| --- | --- |
| **SIEM deployment.** Microsoft Sentinel is the natural fit for an all-Azure, all-M365 estate | Detect scores 17%; almost every failure traces to the absence of log aggregation |
| **Log onboarding and use case development** — Entra ID, M365, Defender, Palo Alto, Azure activity, and the Horizon Labs SaaS platform | A SIEM with no logs onboarded is a common and expensive way to score no better |
| **Managed detection and response (MSSP)** for 24/7 coverage | Oscorp has one analyst. 24/7 cannot be staffed internally at this size; an MSSP is the honest answer |
| **Privileged access management** with just-in-time elevation | Completes the year 1 admin credential work |
| **Data protection: Microsoft Purview** for labelling and DLP across M365 and Azure | Depends on the year 1 classification scheme; without labels, DLP has nothing to enforce |
| **Supplier assessment programme in operation** — tier 1 suppliers assessed, remediation plans contracted | Year 1 built the process; year 2 runs it |
| **Detection testing and IR exercising**, including a tabletop with the executive team | The module 8 finding: a drill attended only by the security team tests the wrong thing |

**Year 2 exit criteria:** Sentinel operational with core log sources onboarded;
24/7 monitoring in place; PAM deployed; DLP enforcing on classified data; tier 1
suppliers assessed; incident response tested with executives.

### Year 3 — Assurance, measurement and continuous improvement

*Theme: prove the programme works, measure it, and make it self-sustaining.*

| Initiative | Notes |
| --- | --- |
| **Purple team exercise** against the detection capability built in year 2 | Only worth doing once there is something to detect with |
| **Insider threat programme**, given research IP concentration and prior suspected disclosure | Deferred deliberately — it depends on monitoring and DLP existing first |
| **Cyber risk quantification** for the top risks, reported to the board in monetary terms | Turns the risk register into investment decisions |
| **Security metrics and board reporting** — remediation SLA performance, detection coverage, phishing report rate, third-party assurance status | Makes the programme measurable rather than anecdotal |
| **Certification readiness** — ISO 27001, or a formal NIS2 compliance position if in scope | External assurance for Oscorp's research partners and customers |
| **Continuous improvement cycle** — annual reassessment against this framework | The programme has to survive its author |

**Year 3 exit criteria:** independently tested detection; quantified top risks
reported to the board; measurable SLA performance; a defensible external
assurance position.

---

## 4. Resourcing and governance

The current structure cannot deliver this. Three changes are prerequisites
rather than initiatives.

**Security must not report into IT.** The analyst reports to the IT manager and
the network engineer reports to the network team leader. That makes the people
assessing controls subordinate to the people who build and run them — a first and
second line collapsed into one, and exactly the independence problem the three
lines model exists to prevent. Security should report to the CEO or an executive
outside the IT delivery line.

**Headcount.** One generalist analyst cannot deliver this roadmap. Year 1 needs
at least a security manager and a second analyst; year 2's 24/7 requirement is
met by an MSSP rather than by hiring, which is the cost-effective answer at
Oscorp's size.

**Board oversight.** Cyber risk currently reaches no governance forum. The
existing risk team covers financial risk only. Cyber risk should be reported
through the same channel with the same discipline, not maintained as a parallel
artefact nobody reviews.

---

## 5. What I would say to Norman Osborn

Oscorp has spent money on good things — the firewalls, the facility, the backups,
the continuity planning — and those decisions were sound. What is missing is not
mostly technology. It is that nobody owns security, nothing decides what to fix
first, and there is no capability to detect or respond to an incident.

The three most valuable things Oscorp can do in the next ninety days cost almost
nothing: turn on multi-factor authentication, stop sharing the administrator
password, and give the security function an owner who does not report to the team
they assess. Those three close more real risk than anything else on this roadmap.

The rest is a three-year build, and it should be funded as one. The year 1 work
is foundational and mostly process. Year 2 is where the significant spend sits —
SIEM, managed detection, PAM, DLP — and it is deliberately deferred, because
buying monitoring before knowing what you own produces an expensive tool watching
an unknown estate.

One point I would not soften: Oscorp's most critical application is a SaaS
platform supplied by Horizon Labs, which was separately assessed as having no
access control model, no monitoring and no incident response capability. Oscorp's
research data sits inside that supplier. That risk exists today, it is not
addressed by anything Oscorp builds internally, and it needs a decision — a
contractual remediation plan, compensating controls, or acceptance by a named
executive.

---

## Design notes

Not part of the programme — my reasoning.

**I sequenced by dependency rather than by severity.** The naive roadmap puts the
scariest findings first, which would mean buying a SIEM in month one. But
monitoring scope comes from the asset inventory, DLP enforcement comes from the
classification scheme, and prioritisation comes from the risk process — so the
unglamorous year 1 work is what makes the year 2 spend effective. Getting that
order wrong is how organisations end up owning expensive tools that produce
nothing, which is exactly what has already happened to Oscorp with Qualys.

**I separated the free fixes from the funded ones.** MFA, ending shared admin
credentials and fixing the reporting line need no budget and close more risk than
any purchase on this roadmap. Leading with them makes the programme credible —
it shows the recommendation isn't a procurement exercise — and it buys goodwill
for the parts that do cost money.

**The reporting line is a finding, not an aside.** The notes present the team
structure as background. It is the structural cause of the governance failures,
and a roadmap that leaves security reporting into IT would deliver controls
without the independence to assess them honestly.

**I deferred the insider threat programme deliberately**, despite Oscorp's
research IP concentration making it a genuine concern. It depends on monitoring
and data labelling that will not exist until year 2, and building it earlier
would produce a policy document with no technical capability behind it.

**Not applicable is recorded separately from implemented.** Four Protect passes
exist because Oscorp writes no software and runs no servers. Counting those as
control maturity would overstate the position by four points, and a reader
comparing Oscorp against another organisation would be misled.

**I reused work from earlier modules rather than starting fresh** — the incident
response plan, the Horizon Labs supplier assessment, and the quantified case for
the awareness programme. A real consultant with prior engagements at the client
would do the same, and it makes the roadmap concrete where it would otherwise be
generic.
