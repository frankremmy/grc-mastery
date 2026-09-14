# Risk assessment case study — Wayne Enterprises insider data leak

**Module:** 02 — Cyber Security Risk Management
**Type:** Practical case study
**Status:** My own answer, written before watching the solution.
**Register:** [`02-wayne-risk-register.csv`](02-wayne-risk-register.csv)

---

## Scenario

An employee at Wayne Enterprises has leaked confidential financial data —
including employee salaries — to a competitor. The consequences named are loss of
competitive advantage, legal exposure and reputational damage. Estimated financial
loss: $700,000.

The assessment uses the scoring criteria supplied with the case: risk score is
likelihood multiplied by impact, each on a three-point scale, with bands mapping
the product to a risk level and a required response.

---

## Answers

### 1. Risk score: **9**

**Impact = 3.** The estimated loss of $700,000 sits above the $500,000 threshold
for the top impact band.

**Likelihood = 3.** The top likelihood band explicitly covers events that have
already happened, and this one has. There's no estimation to do — the scenario
states the leak occurred.

**3 × 3 = 9.**

### 2. Response: **Propose immediate risk treatment**

A score of 9 falls in the highest band, which the criteria define as unacceptable
and requiring treatment. That rules out accepting the risk. Transfer — insurance,
or contractually shifting exposure — isn't a fit either: the competitive advantage
is already gone, and no policy restores confidentiality of a formula for salary
structure that a competitor now holds. Justification isn't available at this level
under the supplied bands.

### 3. With likelihood reduced to 1: **Acceptable**

Likelihood 1 against an unchanged impact of 3 gives a score of 3, which falls in
the lowest band and is defined as acceptable.

Two caveats I'd attach in a real report. The score of 3 sits on the boundary
between the low and medium bands as written, so the answer depends on reading the
lowest band as taking precedence. And impact has not moved — the compensating
control addresses how likely a recurrence is, not how much a recurrence would
cost. A 1×3 risk and a 3×1 risk both score 3 and are not the same risk.

---

## Assessment notes

**The likelihood rating is about recurrence, not the incident.** Rating a realised
event as "likely" is correct under the supplied criteria, but it's worth being
precise about what the register is tracking afterwards. The leak has happened;
that's an incident, and incident response — containment, legal action, notifying
affected parties — runs on its own track. What the risk register carries forward
is the likelihood of it happening *again*, which is what a compensating control
can actually change. Conflating the two is how a register ends up describing
history instead of exposure.

**The impact scale only measures money, and the scenario names three harms.**
Loss of competitive advantage, legal repercussions and reputational damage are all
called out, and the criteria convert impact into a single financial band. The
$700,000 figure captures one of the three. Legal exposure has its own dynamics —
employment law, potential regulatory involvement — and reputational damage to an
employer whose staff now know their salaries went to a competitor is real and not
denominated in dollars. The score of 9 is already the maximum, so nothing is lost
operationally here, but if the estimate had been $400,000 the arithmetic would
have produced a medium rating for an event that isn't medium. I'd record the
non-financial harms in the register notes rather than let the scale silently drop
them.

**Salary data is employee personal information.** That makes this more than a
confidentiality incident against company data — there are privacy obligations to
the affected employees, and depending on jurisdiction, potential notification
duties. That's a separate assessment with a separate owner, and the right move is
to flag it rather than fold it into this one.

**The vulnerability is access, not technology.** No system was breached. Someone
with legitimate access to confidential financial data removed it. That shapes the
treatment: the controls that matter are least privilege, classification,
monitoring of bulk access and egress, and the joiner-mover-leaver process — not
perimeter defence. It's also a reminder that "no attacker got in" and "the data
left" are compatible statements.

**What the score can't tell you.** Nine is the maximum on this scale, and so is a
$50 million loss that's certain to recur. Three-point ordinal scales compress
hard at the top, which is fine for triage and poor for choosing between two
high-rated risks. When everything important scores 9, the register has stopped
prioritising — which is the problem quantitative methods like FAIR exist to
address, and which module 11 covers.

---

## Proposed treatment

| Control | Effect | Rationale |
| --- | --- | --- |
| Access review and least privilege on HR and finance data | Likelihood | The leak required access; most holders of that access don't need it |
| Data classification and labelling | Likelihood | Handling rules can't attach to data nobody has classified |
| DLP on egress channels — email, cloud upload, removable media | Likelihood | Puts a control on the path the data actually took |
| Monitoring and alerting on bulk access and download | Likelihood, and impact | Detection wouldn't have prevented this leak, but would have shortened it |
| Access recertification on a schedule | Likelihood | Stops access accumulating silently as people change roles |
| Joiner-mover-leaver process enforcement | Likelihood | Role changes and departures are where excess access concentrates |
| Awareness training covering confidentiality obligations | Likelihood | Addresses the accidental and careless cases, not the deliberate one |
| Contractual and legal follow-up — NDAs, enforcement | Impact | Doesn't undo disclosure; may limit what the competitor can act on |

Nothing here restores the confidentiality that's been lost. Every control above
addresses the next occurrence, which is the honest thing to tell an executive
signing this off.
