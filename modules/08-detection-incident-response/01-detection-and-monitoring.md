# Detection and monitoring

> Module 08, lesson 1. The layer that assumes the other layers failed — and a
> lesson about how to talk about all of them.

## Summary

Security teams exist to stop criminals getting in, and the defence in depth model
is how that's attempted. But **there is no such thing as 100% secure**, and attacks
still happen.

Which leads to the language point, and it's made deliberately. Don't say security
measures *stop* cyber attacks. Say they **reduce the likelihood of an attack
happening and reduce the impact if it does**. Precision in language matters,
especially for GRC professionals, because the audience is decision makers and
senior executives.

That's where detection and response come in. The security team needs visibility
across the network so it can see anything unusual — malware someone downloaded, an
attacker trying to break in, or an honest mistake like an employee sending
sensitive information outside the organisation.

Detection and monitoring are another layer of defence. **The goal is to detect that
something is wrong and stop it escalating** — to control the damage as quickly as
possible.

**Who does it.** Usually people titled cyber security analyst or security engineer.
Depending on size, an organisation may run a dedicated **security operations
centre (SOC)** with analysts monitoring 24/7. Models vary: shifts covering morning
and evening; a team in another country covering out-of-hours; or an escalation
point where whoever is on in the evening escalates to a senior analyst. The module
covers these models later.

**And the honest assessment:** in the instructor's long experience, this is by far
the **weakest area in most organisations**. Getting a good handle on detection and
response is challenging and expensive.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| No such thing as 100% secure | Attacks can succeed despite every control | The premise the entire detection layer rests on |
| Precise language | "Reduce likelihood and impact", not "stop attacks" | Overpromising to executives sets up a failure you'll own |
| Visibility | Being able to see what's happening across the estate | You cannot detect what you cannot see |
| Detection as a layer | Monitoring as part of defence in depth | Assumes prevention failed, which is why it exists |
| Containing escalation | Stopping an incident growing, not just noticing it | Detection without response is observation |
| Security analyst / engineer | The roles that do this work | Where detection sits as a career |
| SOC | A dedicated team monitoring continuously | The mature form; expensive, and not universal |
| Coverage models | Shifts, follow-the-sun, or on-call escalation | How organisations cover the hours they can't staff |
| The common weak point | Detection and response are poorly done in most organisations | Sets expectations for what an assessment will find |

## Where this shows up in a real job

The Wazuh lab is the most directly relevant thing I've built for this module, and
it covers the technical half — collecting logs, writing rules, making alerts fire.
What it doesn't have is the part this lesson is really about: coverage across a
real estate, people to receive alerts at 3am, and a decision about what constitutes
"unusual" in an environment with actual business noise in it.

The escalation model point is familiar from support, though. Coverage across
timezones, handover between shifts, and a defined path to a senior person are the
same operational problems whether the queue is tickets or alerts — and the handover
is where things get dropped in both.

The lesson's observation that honest mistakes are also detection targets is worth
noting. Plenty of what a detection capability catches isn't an attacker at all,
which changes how the alerts should be handled and who needs to be involved.

## My take

The language instruction is the most immediately useful thing here, and it's not
pedantry. "We stop cyber attacks" is a claim that gets disproved the first time
anything succeeds, and the person who made it loses credibility exactly when they
need it most. "We reduce likelihood and impact" survives the incident, because it
was never a promise of prevention. For someone whose value depends on being
believed by executives, choosing language that survives contact with reality is a
professional skill rather than a style preference.

It also connects back to the metrics problem from module 6. A team that claims
prevention is measured on incidents not happening — which is unmeasurable and
confounded. A team that claims reduced likelihood and impact can be measured on
detection time, containment time and blast radius, which are real numbers.

Two other things:

**Detection exists because prevention is assumed to fail, and that inverts the
question.** The preventive controls are designed against known attacks. Detection
has to work against the ones that got through, which by definition are the ones
nothing recognised. So the useful question in an assessment isn't "what do you
detect" — every tool has a rule list — but "what would you see if something
unfamiliar were happening", which is the difference between signature and
behavioural detection from module 6.

**"This is the weakest area in most organisations" is worth taking seriously as a
prediction.** It's expensive because it needs tooling, log storage, and people
awake at unsociable hours — and unlike a firewall it produces no artefact you can
show a board. My expectation for any assessment: the tooling will exist, the
coverage will be partial, and the gap will be in the hours nobody is watching and
the systems nobody connected to the logging. That matches the three-in-the-morning
question from module 3, which now looks like the same finding approached from the
audit side.

One thing I'd want to establish early in an assessment: detection and response are
two capabilities, not one. An organisation can genuinely detect and still have no
one empowered to act at the moment it matters — which is a different finding, with
a different fix, from not seeing the event at all.
