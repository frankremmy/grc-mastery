# Identify — solution walkthrough

> Capstone, lesson 2. _Working the Identify function, and where my own scoring
> diverged._

## Summary

Identify spans several domains at once — asset management, business environment,
governance, risk assessment and risk management strategy. That mix is the first
thing to notice about NIST CSF: a single function pulls in areas this course
taught as separate modules.

**Asset management.** Physical devices inventoried — **Pass**, with a comment that
the CMDB needs periodic reviews. Software and applications inventoried — **Fail**;
a CMDB has to cover software and intellectual property as well as hardware, and
Oscorp holds serial numbers for laptops and nothing else. Being exclusively SaaS
means laptops genuinely *are* most of the physical estate, which makes the
software and IP side the larger gap for a scientific research company. Data flows
mapped — **Pass**, the network team keeps current diagrams. External information
systems catalogued — **Fail**; this covers consumed SaaS and third-party suppliers,
and Oscorp does nothing on third-party risk. Roles and responsibilities —
**Fail**.

**Business environment.** Role in the supply chain — **Fail**, since Oscorp has
not established who its suppliers are or what part they play. Critical
infrastructure — **N/A**; in this framing critical infrastructure means something
whose failure disrupts the nation, like public transport. Business strategy —
**Pass**, and worth noting the control is about the organisation rather than
about security. Dependencies and critical functions — **Fail**; this one is about
the critical services Oscorp *consumes*, internally or from suppliers, and
whether they've been identified and classified. Resilience requirements —
**Pass**. "Resilience" in NIST language means business continuity and disaster
recovery, which Oscorp has.

**Governance.** Information security policy — **Fail**. Roles coordinated with
internal and external partners — **Fail**. Legal and regulatory requirements —
**Fail**. Governance and risk processes addressing cyber risk — **Fail**.

**Risk assessment and risk management strategy.** Almost entirely **Fail**, with
the critical-infrastructure-dependent control marked N/A.

### Two points from the walkthrough worth keeping

**The Comments column is for the assessor, not the client.** The spreadsheet is a
working document for you and your team. What the client receives is a summary
report with recommendations. That reframes what the comments are for — working
notes and the basis for later recommendations, not client-facing prose.

**Shared responsibility is a governance question, not a technical one.** Oscorp's
most critical asset is research data in a third party's SaaS platform. Who is
responsible for securing it — the provider, Oscorp, or both in defined parts —
has never been established. That's what the roles-and-responsibilities control is
actually asking about once third parties are involved.

## Where my assessment diverged

I scored 2 passes in Identify against the solution's 4 passes and 2 N/A.

| Control | Solution | Me | Outcome |
| --- | --- | --- | --- |
| Physical devices inventoried | Pass | Fail | Solution right |
| Resilience requirements | Pass | Fail | Solution right |
| Critical infrastructure (×2) | N/A | Fail | Mostly solution's call |

**Physical devices.** I failed it because the spreadsheet covers laptops only and
nothing reviews it. The solution passes the control and records the review gap in
the comment. Its reading is better: the control asks whether devices are
inventoried, and they are. The shortfall still becomes a recommendation — it just
doesn't destroy the signal about where Oscorp stands.

**Resilience requirements.** I read "resilience" as including supplier resilience
due diligence and failed it on the absent TPRM. The walkthrough is explicit that
resilience here means BC/DR, which Oscorp does well. I imported a requirement the
control doesn't carry.

**Critical infrastructure.** The walkthrough defines it as nationwide disruption —
public transport is the example — and on that definition Oscorp plainly isn't. My
Fail was on a different basis: that Oscorp has never *determined* its status, and
that sector regulation draws the line differently from the colloquial sense
(NIS2 Annex I covers the health sector and pharmaceutical manufacture; Australia's
SOCI Act names healthcare and medical). I'd keep that as a live question for a
pharma client with a marketed medicine, but N/A is the reasonable answer at the
level this exercise works at, and marking it Fail overstated the finding.

**An inconsistency in my own work.** I used a "Pass + NOT APPLICABLE" label in
Protect for the software development and server maintenance controls, but marked
the critical infrastructure controls in Identify as Fail. Those are the same
situation handled two different ways. The source spreadsheet doesn't state an N/A
convention, but I should have picked one and applied it throughout — and N/A is
the right one, because it keeps inapplicable controls out of both the numerator
and the denominator.

## My take

The correction I'm taking from Identify is the same one the overall comparison
surfaced: **assess the control, record the gap in the comment.** But the
walkthrough adds the reason it matters, which I hadn't fully appreciated. The
comments are working notes that become the recommendations. So a comment reading
"CMDB needs periodic reviews" on a passed control still produces the same
recommendation my Fail would have — while preserving the information that Oscorp
has *something* here rather than nothing. Failing it loses that distinction and
gains nothing.

The other thing worth holding is the observation that SaaS-heavy organisations
with a competent IT team frequently have decent business continuity almost by
accident, because the platform provides much of it. That explains Oscorp's
otherwise odd profile — strong on continuity and physical security, absent on
detection and response. It isn't a coincidence or a sign of unusual foresight;
it's what you get when infrastructure decisions carry security properties along
with them and nobody has made a deliberate security decision at all.
