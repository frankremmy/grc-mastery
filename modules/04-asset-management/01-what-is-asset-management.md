# What is asset management?

> Module 04, lesson 1. A short lesson making a large claim: this is where risk
> management actually starts.

## Summary

The point of GRC is to manage cyber security risk, and the first step in doing
that is asset management — working out what the organisation actually has, so that
it can be protected. The line the lesson turns on: **you can't protect the
unknown**.

The second claim is about difficulty. Asset management is genuinely complex and
one of the things organisations most consistently struggle with. It also gets very
little attention — conversation about security gravitates to malware, attackers,
incident response, SIEM tooling. The inventory underneath all of that is assumed
rather than discussed.

Short lesson, and it reorders everything that came before it. Threat
identification in module 2 asked what the organisation is exposed to. That
question can only be answered properly once you know what's there to expose.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Asset management | Identifying and tracking what the organisation has, so it can be protected | The precondition for every other control decision |
| "You can't protect the unknown" | An asset nobody has recorded gets no controls, no patching, no monitoring | The most compact argument for the whole discipline |
| First step, not a side task | Asset management precedes threat identification and risk assessment | An assessment against an incomplete inventory is confidently wrong |
| A known pain point | Most organisations do this badly, including mature ones | Worth expecting a mess rather than treating one as unusual |

## Where this shows up in a real job

This is the most familiar territory in the course so far. A WordPress site's real
security posture is largely a question of what's installed on it — which plugins,
which themes, which versions, which of them are still maintained. That list *is*
an asset inventory, and the sites that get compromised are usually the ones
running something nobody remembered was there.

My CVE detection lab depends on the same thing from the other direction. A feed of
vulnerabilities is only actionable against a known estate; "is this CVE relevant
to us" is an inventory question before it's a security question. The matching is
the easy half.

The support version is "which sites are affected by this?" — a question that
sounds operational and is really about whether anyone knows what's deployed.

## My take

The asymmetry is what makes this worth taking seriously. A defender needs the
inventory to be complete; an attacker needs one forgotten thing. Every other
control is scoped by this list, so an asset missing from it is missing from
patching, from monitoring, from access review and from the risk assessment — all
at once, and silently.

Two things I expect to matter as the module goes on:

**An inventory is a living record, not a project.** The estate changes constantly —
cloud instances, SaaS subscriptions bought on a card, contractor laptops, a server
someone stood up for a trial. Anything that produces a correct list on one day and
no process for the next day is a snapshot, and snapshots rot quietly.

**The reason it's neglected is that it's unglamorous and never finished.** There's
no incident to respond to and no obvious moment of completion, which makes it the
first thing to lose to more urgent work — the same dynamic module 2 described for
risk documentation. Both are foundational, both are invisible when done well, and
both get dropped for exactly that reason.
