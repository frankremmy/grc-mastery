# Quantifying Oscorp's phishing risk — FAIR analysis

**Module:** 11 — Cyber Risk Quantification
**Type:** Self-directed — my own application of the FAIR model
**Companion file:** [`11-fair-calculator.xlsx`](11-fair-calculator.xlsx)

**Why this exists.** In module 6 I recommended that Oscorp invest in an awareness
and phishing simulation programme. That recommendation was entirely qualitative —
it argued the current programme was outdated and that report rate matters more
than click rate. Both true, and neither is an answer to "is it worth the money".
This is the same recommendation expressed in a currency a finance director
accepts.

The calculator is my own build, not the course's. It implements the Open FAIR
ontology, models secondary loss properly as SLEF × SLM, and carries a sensitivity
sheet — because a single figure is the weakest form of this argument.

---

## 1. Scenario

| Element | Value |
| --- | --- |
| Scenario | A phishing email delivered to an Oscorp employee results in credential compromise or malware execution, requiring incident response and potentially exposing research data |
| Asset | Employee mailboxes and credentials; the research data estate reachable from them |
| Threat | External actors sending phishing email — commodity criminal through to targeted |
| Loss form | Confidentiality, with availability and response cost consequences |

---

## 2. The estimating problem, stated honestly

The course's worked example had SOC telemetry — a known number of phishing
attempts and a known success rate. **Oscorp has neither.** There is no security
operations centre, no email gateway reporting, and no incident record to draw on.
Every likelihood input here is therefore an estimate, not an observation.

That is worth stating plainly rather than hiding, for two reasons. It is the
honest position, and it is also itself a finding: an organisation that cannot
answer "how much phishing reaches our people and how often does it work" cannot
measure its own exposure, and that gap is separately worth fixing.

| Input | Value | Basis | Confidence |
| --- | ---: | --- | --- |
| Threat Event Frequency | 3,000/yr | ~250 staff × ~12 phishing emails reaching inboxes per year | **Low** — assumption |
| Susceptibility | 0.20% | Share of delivered phishing becoming a loss event, given onboarding-only training last refreshed in 2013 and no simulation | **Low** — assumption |
| Primary Loss | €18,000 | IR hours, external IR provider call-off, credential reset, user downtime, forensic review. Oscorp has no internal IR team, so this is largely external cost | **Medium** |
| Secondary Loss Magnitude | €250,000 | Regulatory notification and legal costs, research partner contract consequences, potential research IP exposure | **Low** — needs legal input |
| Secondary Loss Event Frequency | 15% | Share of loss events producing fallout. Contained credential compromises mostly won't; anything touching research data will | **Low** — needs legal and business owner input |
| Control effectiveness | 50% | Deliberately below typical vendor claims | **Low** |
| Control cost | €60,000/yr | Licence plus internal administration, not licence alone | **Medium** |

**Susceptibility is not click rate.** A click stopped by MFA is not a loss event.
This models the proportion of delivered phishing that results in something
requiring incident response.

---

## 3. Result

| Step | Calculation | Value |
| --- | --- | ---: |
| Loss Event Frequency | 3,000 × 0.20% | **6 loss events/yr** |
| Expected Secondary Loss | €250,000 × 15% | €37,500/event |
| Loss Magnitude | €18,000 + €37,500 | €55,500/event |
| **Annualised Loss Exposure** | 6 × €55,500 | **€333,000/yr** |
| Residual susceptibility with control | 0.20% × (1 − 50%) | 0.10% |
| Residual LEF | 3,000 × 0.10% | 3/yr |
| **Residual ALE** | 3 × €55,500 | **€166,500/yr** |
| Risk reduction | €333,000 − €166,500 | €166,500/yr |
| Total annual cost with control | €166,500 + €60,000 | €226,500/yr |
| **Net annual benefit** | €333,000 − €226,500 | **€106,500/yr** |
| ROSI | (€166,500 − €60,000) ÷ €60,000 | **178%** |
| **Break-even effectiveness** | €60,000 ÷ €333,000 | **18%** |

---

## 4. Sensitivity

The headline figure depends on estimates I have marked Low confidence. What
matters is whether the *conclusion* depends on them.

**Net annual benefit against control effectiveness:**

| Reduction achieved | 20% | 30% | 40% | 50% | 65% |
| --- | ---: | ---: | ---: | ---: | ---: |
| Net annual benefit | €6,600 | €39,900 | €73,200 | €106,500 | €156,450 |

The programme remains net positive at every effectiveness level down to the
break-even point of 18%. The full tables in the workbook also flex threat event
frequency, susceptibility, and both secondary loss inputs.

**The most robust number in this analysis is the 18% break-even**, because it
depends only on the control cost and the current exposure — not on any claim the
vendor makes about their own product. That is the figure I would put in front of
Norman Osborn.

---

## 5. What I would say to Oscorp

Oscorp's phishing exposure is in the region of **€330,000 a year**, dominated not
by the cost of responding to incidents but by what follows one that reaches
research data. The awareness and simulation programme returns roughly €106,000 a
year net at a conservative 50% effectiveness, and **pays for itself at anything
above an 18% reduction** — a bar that is difficult for a programme of this kind
to miss, given the current baseline is a single training module written in 2013.

Two caveats I would give alongside it.

**These numbers are estimates, and the largest ones are the least certain.** They
should be replaced with real figures before this drives a significant decision —
gateway telemetry for the frequency, legal input for the secondary loss. The
conclusion survives every pessimistic assumption I tested, but the precision of
€333,000 is not real and I would not present it as though it were.

**Oscorp cannot currently measure this.** The absence of the data needed for this
analysis is its own finding, and it connects to the module 8 work: an
organisation without detection and monitoring cannot quantify what it doesn't
observe. That's a second investment case, and arguably the prior one.

---

## Design notes

Not part of the analysis — my reasoning.

**I built the calculator rather than reusing the course's.** Partly so this is my
own work in a portfolio, and partly because I wanted three things the teaching
example leaves out: secondary loss modelled as SLEF × SLM rather than applied to
every event, a source-and-owner column beside every input, and a sensitivity
sheet. The teaching version simplifies for clarity, which is right for teaching
and overstates exposure by treating fallout as certain.

**I modelled the control on susceptibility, not on loss event frequency.** They
are arithmetically identical here, but the reasoning matters: awareness training
does not reduce how much phishing arrives. Getting this the right way round is
what lets you compare an email gateway and a training programme in the same model.

**I led the recommendation with break-even rather than with the headline.** The
€333,000 is the number that gets attention and the 18% is the number that
survives scrutiny. A CFO can dispute my secondary loss estimate; they cannot
easily dispute that a €60,000 control against a €333,000 exposure needs only an
18% reduction to pay for itself. Leading with the robust figure and supporting it
with the headline is the opposite of what a vendor would do, which is rather the
point.

**Every assumption is labelled as one.** Oscorp's headcount, its phishing volume
and its legal exposure are not stated anywhere in the course material — I
inferred them. Presenting inferred figures as findings would be the exact failure
the module warns about, and a portfolio piece that does it is worse than one that
shows its working.
