# Practical example — quantifying phishing risk

> Module 11, lesson 4. _Working the model end to end, and turning the answer into
> a business case._

## Summary

The scenario: a firm is being hit by phishing, staff are getting compromised, and
the security team wants to buy an awareness and simulation platform costing
$80,000 a year. Management accepts phishing is a problem but isn't convinced it's
an $80,000 problem. The job is to answer that with FAIR rather than with
conviction.

### Working the model

**Define the scenario.** "A phishing attack could compromise client project
data." This fixes the scope — which asset, which threat, what kind of loss.
Vague scenarios produce unusable numbers.

**Identify assets and threats.** Staff mailboxes, credentials, the applications
reachable once an account is compromised, the client data behind them. This is
where a decent asset register from module 4 pays off — if assets are already
identified and classified, you're copying, not discovering.

**Threat Event Frequency — 25 phishing attempts a year.** You get this from the
SOC, not from imagination. The real figure is normally far higher; 25 keeps the
arithmetic legible.

**Susceptibility — 20% succeed.** Also from the SOC or incident response team:
over the last twelve months, what proportion of phishing attempts actually landed?

There's a useful shortcut here. FAIR derives susceptibility from threat capability
against resistance strength, and in this scenario you genuinely cannot assess the
capability of whoever is sending the emails — it could be a commodity crew or a
state actor. But you don't need to, because you have **observed outcome data**.
Knowing that 20% succeeded tells you what the capability-versus-controls
interaction actually produced, without having to estimate either side. Where real
data exists, it replaces the estimate.

**Loss Event Frequency = TEF × Susceptibility = 25 × 0.20 = 5.** Five successful
phishing events a year.

**Primary Loss — $40,000 per event.** The security and incident response time
spent on a successful phishing incident: hours worked, costed at salary. If that
seems high for one phishing incident, it isn't — a single successful phish can
take down a substantial part of a network.

**Secondary Loss — $60,000 per event.** Legal fees, client compensation,
regulatory exposure, lost customers. Obtained by asking legal and the contracts
team, not by estimating from the security desk. Note that it exceeds the primary
loss, which is typical — the hours your own staff spend are rarely the expensive
part compared with losing a major client.

**Total loss per event = $100,000.**

**Annualised Loss Exposure = $100,000 × 5 = $500,000 a year.**

### Turning it into a business case

$500,000 against an $80,000 solution looks decisive, but the lesson makes the
point that the job isn't finished. Presented with that number, management will
reasonably ask what the firewalls and the SOC were for, and how they know *this*
purchase will help. So you model the control's effect.

The vendor — or industry research — puts the reduction in successful phishing at
**60%**. So:

| | Annual loss | Control cost | Total annual cost |
| --- | ---: | ---: | ---: |
| Without the programme | $500,000 | — | $500,000 |
| With the programme | $200,000 | $80,000 | $280,000 |

New LEF = 5 × (1 − 0.6) = 2. New ALE = $100,000 × 2 = $200,000. Add the $80,000
and the total annual cost becomes $280,000 against $500,000 — a **net saving of
$220,000 a year**, or a return on security investment of 275%.

The contrast is the whole point of the module. "We have a phishing problem, it's
high risk, I need $80,000" is a request. "We lose $500,000 a year to phishing,
this reduces it to $200,000, so the $80,000 returns $220,000" is a business case
in the language the people holding the budget already use.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Scenario definition | A specific asset, threat and loss type | Everything downstream inherits its precision |
| Observed data over estimation | Using actual success rates instead of estimating TCap and RS | Where you have data, you don't need the abstraction |
| LEF = TEF × Susceptibility | Loss events per year | The likelihood arithmetic in one line |
| Primary Loss per event | Direct response and recovery cost | Costed from hours and salaries — defensible |
| Secondary Loss per event | Legal, client, regulatory fallout | Usually larger; only obtainable from other teams |
| ALE = loss per event × LEF | Annualised loss exposure | The headline figure |
| Control effectiveness | Expected reduction from the proposed control | Sourced from vendor or industry data, and always below 100% |
| ALE after control | Residual exposure with the control in place | What the organisation still carries |
| Net saving | Reduction in loss minus the control's cost | The number that answers "is it worth it" |
| ROSI | Return on security investment | Frames security spending as investment rather than overhead |

## Where this shows up in a real job

This connects directly to the module 6 work. I evaluated a phishing simulation
platform for Oscorp and argued for it on the grounds that report rate matters
more than click rate — which is a good argument and an entirely qualitative one.
This lesson is the version of that argument that survives contact with a finance
director. Same recommendation, different currency.

The other thing I notice is how much of this calculation is other people's data.
The SOC supplies the frequency and the success rate. Incident response supplies
the hours. Legal and contracts supply the secondary loss. Finance supplies the
salary costs. The security analyst supplies the structure and does the arithmetic.
That division of labour is worth internalising, because it means the skill being
tested is knowing what to ask and of whom — which is much closer to support
escalation work than to anything technical.

## My take

The most important honest observation about this example is that **the model's
credibility rests entirely on four estimates, and only two of them are solid.**
TEF and susceptibility came from SOC data and are defensible. The $40,000 primary
loss is calculable from hours and salaries and is reasonably defensible. The
$60,000 secondary loss and the 60% control effectiveness are the soft ones — and
they're the two that drive the conclusion. A sceptical CFO will go straight for
them, and the right response is to have the source ready and to show what happens
to the answer if they're wrong.

Which is why I'd present this with sensitivity rather than as a single figure. If
the awareness programme achieves 30% rather than 60%, the saving drops to $70,000
— still positive, but a different conversation. If it achieves 20%, the
programme roughly breaks even. Showing that range makes the case stronger, not
weaker, because it demonstrates the conclusion survives pessimistic assumptions
rather than depending on optimistic ones. A single number invites someone to
attack the assumption; a range shows you already did.

Two modelling points I want to remember. **The control acts on susceptibility,
not on threat event frequency** — awareness training doesn't stop attackers
sending emails, it reduces how many land. Scaling LEF by 0.4 is arithmetically
the same thing here, but the reasoning matters when you're choosing between
controls: an email filter and awareness training both cut susceptibility, whereas
almost nothing an organisation buys reduces TEF.

And **this worked example applies secondary loss to every loss event**, which
implicitly sets the secondary loss event frequency at 100%. The full model says
SL = SLEF × SLM and that SLEF is below 100%, because not every incident produces
fallout. Five contained phishing incidents in a year probably don't all trigger
legal costs and client losses. Simplifying it makes the arithmetic clearer for
learning, and it does overstate the exposure — worth knowing before presenting a
figure built this way to someone who knows FAIR properly.
