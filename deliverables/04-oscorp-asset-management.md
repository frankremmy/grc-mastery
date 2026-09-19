# Asset management process and CMDB design — Oscorp

**Module:** 04 — Asset Management
**Type:** Practical assessment
**Status:** My own answer, submitted before seeing the course solution, followed by
a comparison written afterwards.
**Role:** External cyber security consultant advising Oscorp.

---

## Situation

KPMG, acting as Oscorp's internal audit function, found that asset management
needs enhancement — specifically that there is no up-to-date central asset
management database. Oscorp currently keeps a single spreadsheet with some ad-hoc
IT system details.

---

## My answer (as submitted)

Oscorp should replace the current ad-hoc spreadsheet with a structured asset
management process supported by a central CMDB.

The first step is to define which assets must be recorded. This should include
laptops, servers, network devices, applications, databases, cloud services,
virtual machines and other critical IT systems. For each asset, Oscorp should
record key details such as asset name, unique ID, owner, location, business
purpose, system type, operating system, criticality, support team and lifecycle
status.

The existing spreadsheet can be used as the starting point. Oscorp should review
and clean the data, remove duplicates, identify missing assets and assign clear
ownership before migrating the information into a central CMDB or asset management
tool.

Asset management should then become part of normal IT processes. New assets should
be registered before they are placed into production. Any major change, transfer,
upgrade, ownership change or decommissioning activity should also trigger an update
to the CMDB.

Clear responsibilities are important. Asset owners should confirm that the
information relating to their assets is accurate, while the IT or asset management
team should maintain the overall database and process.

Oscorp should also carry out regular checks to ensure the CMDB remains accurate.
Automated discovery tools can help identify devices and systems on the network and
compare them against the CMDB. Periodic reviews, such as quarterly checks, should
be performed to identify missing, outdated or incorrect information.

Finally, Oscorp should track measures such as assets without owners, unidentified
assets, outdated records and end-of-life systems. This will improve security
monitoring, vulnerability management, incident response and audit readiness.

---

## Comparing against the course solution

### What I missed

**Oscorp is a scientific research organisation, and I answered as though it were
any company.** My asset list was laptops, servers, network devices, applications,
databases, cloud services and virtual machines — a generic IT estate. The course
solution's central point is that Oscorp's **research intellectual property is its
most critical asset**, and that the identification work must include meeting
stakeholders from each research group to understand what IP they hold.

This is the substantive miss, and it's worth sitting with. Module 4 lesson 3 said
explicitly that sector determines scope — an insurer's list is software and
hardware, a manufacturer's includes control systems, a research company's centre of
gravity is intellectual property. I wrote a correct generic process and skipped the
one thing that makes it Oscorp's process. A generic asset inventory at a
bioengineering firm captures the machines and misses the reason the company exists.

It also contradicts my own earlier work: the CIA triad assessment for Oscorp
identified the formulation document as the crown jewel, and the risk profile lists
research IP as the highest-value asset. I had the context and didn't apply it.

**Senior management endorsement.** The solution ends by requiring that the roles
and responsibilities are documented *and that senior management endorses and
supports the process*. I documented roles but stopped short of the sponsorship.
That matters more than it sounds: Phase-2 style interviews across research groups
and business units are requests that departments can decline, and without an
executive mandate the exercise stalls at whoever is willing to cooperate. The
ownership vacuum from lesson 6 is exactly what sponsorship is there to close.

### Where the solution and I differ

**Tooling.** I proposed migrating the cleaned data into a central CMDB or asset
management tool. The solution says to keep improving the spreadsheet as you go. On
reflection the solution is right for Oscorp's situation — a tool purchase before
the process exists produces an empty expensive system instead of a stale cheap one,
and the audit finding is about currency, not about the file format. The right
trigger for tooling is when the estate outgrows manual maintenance: continuous
discovery becomes necessary, changes need an audit trail, or several people
maintain the record at once.

**Review cadence.** I proposed quarterly checks; the solution suggests six to
twelve months depending on how busy the IT team is. I'd keep a split: quarterly
attestation for crown-jewel assets, annual full re-identification for everything
else. Quarterly for the whole estate is probably unrealistic at Oscorp's size, and
an unrealistic cadence quietly becomes no cadence.

**Who maintains it.** The solution assigns maintenance to the IT team. My answer
said IT or an asset management team. I'd now be more specific: IT maintains the
record and supplies the technical data; security or GRC remains accountable for
the process happening at all. Shared ownership works only when the split is
asymmetric and named — two teams with equal responsibility is how this stalls.

**Classification.** The solution routes classification through the data governance
or risk team. I had criticality as a field but no classification step and no owner
for the scheme. The point is that criticality and sensitivity definitions have to
be consistent across departments, and that requires someone to own the definitions
rather than each department rating its own systems highly.

### Where my answer went further

**Metrics.** The solution doesn't mention measurement. My answer tracked assets
without owners, unidentified assets, outdated records and end-of-life systems.
Given that KPMG's finding is about the CMDB being out of date, agreeing what "up to
date" means and measuring it is how the finding gets closed against a definition
rather than an impression.

**Explicit update triggers.** I named the events that must trigger a CMDB
update — change, transfer, upgrade, ownership change, decommissioning — and required
registration *before* an asset enters production. The solution covers periodic
review but not capture at the point of creation. Periodic review is a safety net;
catching assets when they come into existence is the durable control.

**Lifecycle status as a field.** End-of-life systems are a specific risk
concentration, and tracking status makes them visible rather than leaving them to
be discovered during an incident.

---

## Revised design

Combining both, the process I'd actually recommend to Oscorp:

**1. Start from the existing spreadsheet.** Clean it, deduplicate it, restructure
it to a defined schema — see
[`../templates/asset-register.csv`](../templates/asset-register.csv). No tooling
purchase yet.

**2. Discovery, from three directions, then reconcile.**
Network scanning across all sites, compared against the existing list. Validation
sessions with the IT team, who are the best source for hardware and software.
And interviews with the business — research groups first. Assets found by scanning
that nobody claims, and assets claimed that scanning can't see, are findings in
their own right rather than rows to be quietly added.

**3. Research IP as the priority workstream.** Meet each research group and
establish what intellectual property they hold, where it lives, who has access, and
what would be lost if it were disclosed or altered. This is Oscorp's crown-jewel
inventory and it should be completed first. The confidential medication project
belongs here, recorded with its owner and ratings while detailed location data is
held under restricted access — leaving it out entirely would put the most important
asset outside every process built on the register.

**4. Classification, with an owner for the scheme.** Work with the data governance
or risk function to define what critical and sensitive mean for Oscorp, then rate
each asset on confidentiality, integrity and availability separately. For a
research organisation, silently altered experimental data is worse than a day of
downtime, and a single blended score hides that.

**5. Maintenance, documented in the register itself.**

| Control | Cadence |
| --- | --- |
| Registration before an asset enters production; owner and purpose required | At acquisition |
| CMDB update on change, transfer, upgrade, ownership change, decommissioning | Event-driven |
| Discovery output reconciled against the register | Monthly or quarterly |
| Crown-jewel owner attestation | Quarterly |
| Full re-identification and validation | Annually |

**6. Roles, documented and endorsed.** IT maintains the register and supplies
technical data. Security/GRC is accountable for the process running. Business and
research owners validate ratings and attest. Internal audit tests the process.
Senior management endorses the process and mandates participation — without that,
the interviews in step 2 are optional from the other side of the table.

**7. Measure it, so the finding can be closed.** Assets without owners;
unidentified assets found by discovery; records not validated within their review
period; end-of-life systems. Agree the targets with KPMG before the next audit.

---

## Note on independence

I designed the audit program that produced this finding and I'm now advising on
remediation. Both are advisory engagements, which is consistent — but I should not
later provide assurance over a process I designed. That assessment belongs to KPMG
or another independent party.
