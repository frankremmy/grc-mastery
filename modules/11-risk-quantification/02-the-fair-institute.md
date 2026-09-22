# The FAIR Institute and the FAIR model

> Module 11, lesson 2. _The standard everyone uses, and what its diagram is
> actually saying._

## Summary

The FAIR Institute is a not-for-profit research organisation behind the FAIR
model — Factor Analysis of Information Risk — which is the dominant standard for
cyber risk quantification and the one most likely to turn up in industry.

FAIR defines risk as **the probable frequency and probable magnitude of future
loss**. That sounds unfamiliar and isn't: probable frequency is likelihood,
probable magnitude is impact. It's the same two variables from the module 2 risk
assessments, stated more carefully. The "future loss" being referred to is a loss
of confidentiality, integrity or availability — also nothing new.

Under FAIR, a risk has three dependencies, all of which the course has already
covered separately:

- **Asset** — something of value. An information asset, an application, hardware,
  a laptop, a process
- **Threat** — an actor or event that could compromise that asset. A hacker, or
  an earthquake
- **Impact** — the magnitude of the loss. Money paid out, reputational damage,
  revenue lost while a service is down

### The model

The diagram looks intimidating and mostly isn't. Read top down: **Risk** splits
into **Loss Event Frequency** and **Loss Magnitude** — which are just likelihood
and impact again. Everything below that is the model breaking those two into
smaller pieces that can actually be estimated.

```
Risk
├── Loss Event Frequency (LEF)          — how often a loss happens
│   ├── Threat Event Frequency (TEF)    — how often the threat comes at us
│   │   ├── Contact Frequency (CF)      — how often it makes contact
│   │   └── Probability of Action (PoA) — how often contact becomes an attempt
│   └── Susceptibility (Susc)           — how likely an attempt succeeds
│       ├── Threat Capability (TCap)    — how good the attacker is
│       └── Resistance Strength (RS)    — how good our controls are
└── Loss Magnitude (LM)                 — how much a loss costs
    ├── Primary Loss (PL)               — direct cost to us
    └── Secondary Loss (SL)             — cost from others' reactions
        ├── Secondary Loss Event Frequency (SLEF)
        └── Secondary Loss Magnitude (SLM)
```

Threat event frequency is as it sounds — how often the event occurs. In an area
with no earthquakes the frequency is near zero; in an earthquake zone it's high.
Susceptibility is how vulnerable we are when it does occur.

### Two things the lesson insists on

**Remember what the exercise is for.** The output is not a completed spreadsheet;
it is an accurate monetary figure for the risk. If the number isn't accurate, the
work was decorative.

**Accuracy comes from talking to other people.** This is the part that decides
whether the model produces anything real. The security team cannot sit alone and
compute values for an application it doesn't operate. If the marketing team owns
an application, you meet the marketing team — what does this application bring in,
what happens to the business when it's down, what would actually be lost. Numbers
produced inside the security team and handed out don't work.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| FAIR | Factor Analysis of Information Risk — the dominant quantification standard | What you're most likely to meet in industry |
| FAIR definition of risk | Probable frequency and probable magnitude of future loss | Likelihood and impact, stated precisely enough to calculate with |
| Asset, threat, impact | The three dependencies of any risk | The same building blocks from earlier modules |
| Loss Event Frequency | How often a loss event occurs | The likelihood side of the tree |
| Threat Event Frequency | How often the threat acts against us | Split into contact frequency and probability of action |
| Susceptibility | How likely an attempt is to succeed | Threat capability weighed against our resistance strength |
| Resistance Strength | How well controls hold up against a capable attacker | Where control investment shows up in the model |
| Loss Magnitude | The size of the loss | The impact side of the tree |
| Primary Loss | Costs falling directly on us | Response, replacement, lost productivity |
| Secondary Loss | Costs from how others react | Fines, legal action, customers leaving — often the larger figure |
| Decomposition | Breaking hard estimates into answerable ones | The core idea; nobody can estimate "risk", people can estimate parts |
| Stakeholder involvement | Getting the numbers from the teams who own the asset | The difference between a real figure and an invented one |

## Where this shows up in a real job

The decomposition idea is the one I actually recognise, just from a different
setting. In support, "the site is slow" is not a question anyone can answer — it
becomes answerable when you break it into which request, which layer, which
query, measured how. Nobody estimates the whole thing; you measure parts you can
observe and reassemble them. FAIR is doing the same move on risk, and the
intimidating diagram is just the list of parts.

The stakeholder point is where I'd expect to be most useful and least expert.
Going to the marketing team and asking what an application is worth is a
conversation, not a calculation, and the failure mode is obvious from support
work: ask a vague question, get a defensive or useless answer. "How much is this
worth?" invites either a shrug or an inflated number. "If this were down for a
full working day, what stops, and who notices?" is answerable, and the money
falls out of the answer. I have no FAIR experience, but I have had a few thousand
versions of that second conversation.

## My take

The model's value is that it moves the estimating down to a level where people
can honestly answer. Nobody can tell you the annual likelihood of a ransomware
event. But a threat intel feed can say how often phishing reaches the
organisation, the security team knows roughly how often someone clicks, and the
control owners know what stands in the way after that. Those are knowable. The
tree exists so the hard question is never the one being asked.

The same is true on the loss side, and I think the **primary/secondary split is
the most practically useful part of the whole model.** Primary loss is what most
people instinctively estimate — incident response costs, rebuilding, downtime.
Secondary loss is what everyone else does to you afterwards: regulatory fines,
legal action, customers leaving, contract terms renegotiated. For a regulated
organisation the secondary figure frequently dwarfs the primary one, and it is
routinely left out of informal estimates. Splitting it forces the question to get
asked.

Two cautions for myself. First, this produces a number, and a number carries
authority its inputs may not deserve — the estimates underneath are still
judgements, and the output is only as sound as they are. Presenting the range and
the assumptions alongside the figure is what keeps that honest.

Second, the stakeholder conversation is a governance point disguised as a data
gathering step. If the marketing team supplies the value of their application,
they own that number, and they're far more likely to act on a risk assessment
built from figures they provided than one delivered to them by security. The
involvement isn't only about accuracy — it's how the result gets accepted.
