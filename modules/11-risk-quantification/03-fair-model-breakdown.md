# The FAIR model breakdown

> Module 11, lesson 3. _Every box in the tree, and what you actually have to
> estimate._

## Summary

### The output

Before working through the branches, it's worth being clear what the model is
producing. Risk under FAIR is expressed one of two ways: an **annualised
monetary value** ("this risk costs us around €2 million a year"), or a
**probability of exceeding a magnitude in a timeframe** ("there is a 50% chance
of a loss greater than €100,000 in the next year"). The second form is the more
honest one, because it carries its own uncertainty in the statement.

### Loss Event Frequency — the likelihood side

**Loss Event Frequency (LEF)** is how often, within a given timeframe, a threat
agent's actions inflict harm on an asset. It can be stated as a frequency (once
in twenty years) or a probability (5% chance in the next twelve months). The kind
of harm has to be specified — data theft, an outage, destruction of a facility —
because "harm" on its own isn't estimable.

LEF comes from **Threat Event Frequency** and **Susceptibility**.

**Threat Event Frequency (TEF)** is how often a threat agent acts in a way that
could cause loss. Threat agents aren't only hackers — they can be people,
animals, technology or natural forces, acting deliberately, accidentally, or just
by being weather. TEF splits again:

- **Contact Frequency (CF)** — how often the agent comes into contact with the
  asset, meaning they are in a position to act against it. An internet-facing web
  application has near-total contact frequency: bots find everything, and any
  firewall log shows constant attempts. An isolated system on a military base has
  contact frequency close to zero, because nobody can reach it.
- **Probability of Action (PoA)** — given contact, how likely is the agent to
  actually act. For a natural force this is effectively certain; weather doesn't
  deliberate. For a rational agent it depends on three judgements *the agent*
  makes: the **perceived value** of acting, the **perceived effort** required,
  and the **perceived risk to themselves**.

The two worked examples make the point. For the internet-facing application:
perceived value is high (a foothold to pivot inward), effort is low (automated
tooling does it), and risk to the attacker is low (offshore, obscured). So PoA is
high. For a bank employee with access to a financial system: perceived value may
be high, but effort is significant and the personal risk — getting caught,
prosecuted — is severe. That last factor alone drives PoA down hard.

**Susceptibility (Susc)** is the probability that a threat event becomes a loss
event. High TEF doesn't mean high LEF: an application under constant attack with
strong controls may have very low susceptibility, so the loss event frequency
stays low despite the noise. Susceptibility depends on:

- **Threat Capability (TCap)** — the agent's ability to defeat controls,
  expressed as a percentile against the overall threat population. An ordinary
  criminal community might sit at the 50th–75th percentile
- **Resistance Strength (RS)** — how effective the controls are, on the same
  percentile scale. Controls rated 70–90% repel attackers below that band;
  anything above 90% capability gets through

This is where the model earns its keep. The same application with the same
controls has low susceptibility against commodity attackers and high
susceptibility against a nation-state actor, because TCap moved. Nothing about
the application changed.

### Loss Magnitude — the impact side

**Primary Loss (PL)** happens directly from the event — losing access to data,
paying €200,000 to a firm to restore it. More certain to occur, and often the
smaller figure.

**Secondary Loss (SL)** is the fallout: what other stakeholders do afterwards.
Customers leaving, investors reacting, lawsuits, regulatory fines, partners
invoking contract terms. Because it's indirect, its probability is below 100% —
not every incident produces fallout. So SL splits into:

- **Secondary Loss Event Frequency (SLEF)** — the proportion of loss events
  expected to produce fallout. Labelled a frequency but measured as a percentage:
  an SLEF of 80% means eight in ten loss events have secondary consequences
- **Secondary Loss Magnitude (SLM)** — how much that fallout costs

The lesson makes an honest concession here: someone could reasonably argue that
fines and lost customers are primary losses. They could. This is FAIR's
definition rather than a law of nature, and both figures end up in the total
either way. What matters is that separating them forces the fallout question to
be asked at all.

Treating secondary loss as its own small risk — with its own likelihood and its
own impact — is the mental model that makes it click. Losing a customer really is
a risk; here it's a consequence of another one.

### Where the numbers come from

Same answer as the last lesson: other people. The marketing team knows their
customers, can survey them, and can give a defensible estimate of how likely
those customers are to leave after a breach and what each one is worth. Security
cannot produce that number alone, and shouldn't try.

## Key concepts

| Concept | Definition | Estimated as |
| --- | --- | --- |
| Risk | Probable frequency and magnitude of future loss | Annualised value, or probability of exceeding a magnitude |
| Loss Event Frequency | How often harm actually occurs in a timeframe | Frequency or probability; harm type must be specified |
| Threat Event Frequency | How often the agent acts in a way that might cause loss | Frequency in a timeframe |
| Contact Frequency | How often the agent is in a position to act | Frequency in a timeframe |
| Probability of Action | Whether they act, given contact | Probability; for rational agents from value, effort and risk to them |
| Susceptibility | Probability a threat event becomes a loss event | Probability, from TCap against RS |
| Threat Capability | The agent's ability to defeat controls | Percentile against the whole threat population |
| Resistance Strength | Control efficacy against that population | Percentile band |
| Loss Magnitude | Size of the loss | Monetary |
| Primary Loss | Direct consequences of the event | Monetary; more certain, often smaller |
| Secondary Loss | Fallout from stakeholder reactions | Monetary; probability under 100% |
| Secondary Loss Event Frequency | Share of loss events producing fallout | Percentage, despite the name |
| Secondary Loss Magnitude | Cost of that fallout | Monetary |

## Where this shows up in a real job

The probability-of-action decomposition is the part I find genuinely clever,
because it makes you model the attacker's decision rather than your own fear.
Value, effort and personal risk — from the agent's point of view, not ours. That
reframing is what separates "an employee could steal this data" from "an employee
probably won't, because the effort is high and the consequences for them are
severe", and only the second is a statement you can put a number on.

It also lines up with the insider threat work in module 7. The reason that brief
focused on detection and deterrence rather than raw capability is essentially a
PoA argument: most people with access don't act, and the controls that matter are
the ones changing their perceived risk of being caught.

## My take

The TCap and RS pairing is the most useful idea in the model. Putting both on the
same percentile scale turns "are we secure?" — unanswerable — into "are our
controls stronger than the attackers who are likely to come at us?", which is
answerable and specific. It's also the mechanism that makes a business case
computable: a proposed control raises resistance strength, which lowers
susceptibility, which lowers loss event frequency, which lowers annualised loss.
That chain is how you say what a security investment is worth in money rather
than in reassurance.

It follows that **the threat community has to be named before susceptibility
means anything.** "How susceptible are we" has no answer until you say to whom.
Commodity ransomware operators and a state actor are different percentiles and
produce different risks from identical infrastructure. An assessment that skips
this is quietly assuming an attacker without saying which one.

The secondary loss branch is the one I'd expect organisations to get wrong most
often. Primary loss is what the security team can estimate on its own, so it's
what gets estimated, and it's usually the smaller number. For a regulated
business the fines, legal costs and lost customers can be multiples of the
incident response bill — and they're exactly the figures that require going and
asking legal, finance and the business. The branch that's hardest to fill in is
the one carrying most of the money.

Two mechanical things to remember. **SLEF is a percentage despite being called a
frequency** — a genuine trap in the terminology. And **high threat event
frequency does not mean high risk**; an internet-facing application is attacked
constantly, and if resistance strength is high, the loss event frequency can
still be near zero. Confusing attack volume with risk is how security teams end
up reporting "blocked attacks" as if that were a risk measure.
