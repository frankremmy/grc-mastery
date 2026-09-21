# Cyber drills and crisis simulation

> Module 08, lesson 6. Testing the plan before the plan is needed — and not
> confusing this with disaster recovery.

## Summary

Cyber drills — also called cyber crisis simulations or just crisis simulations —
are exercises simulating what a major attack would look like, run periodically to
test the incident response plan. You follow the plan, find the gaps, and update it
on the strength of what the drill revealed.

**Scale varies.** A small, contained exercise run internally by the security team,
or something much larger involving multiple teams and stakeholders — up to and
including the board and the CEO.

**The point is communication.** Testing how different stakeholders communicate
during a cyber crisis, familiarising teams and senior management with what to do
when a major attack happens, and improving communication between them.

Some technical practitioners dismiss these drills as silly because they aren't
technical. That isn't right — not understanding the value of an exercise doesn't
make the exercise pointless. Running them with many organisations, sitting in war
rooms with senior executives, the outcome is consistent: **gaps in the incident
response plan are almost always found**, and the recurring one is that the security
team struggles to communicate cyber issues to senior management. Drills bridge
that gap and teach both sides how to talk to each other during a real attack.

The practical argument: you don't want to be writing email templates and
communications during a real incident. Everyone is stressed, overworked and short
of time — which is exactly when an organisation sends the wrong thing to the press
and chaos follows. Prepare before the crisis.

**Designing a drill.** There's no framework for this. Someone from the security
team writes a scenario — ransomware, a phishing attack — and the steps to simulate
it. Simulate doesn't mean a real attack: most often it's a **tabletop exercise**,
with emails saying "we're under attack, here's what we've seen", and the whole
thing conducted through communication rather than live malware.

Organisations commonly **hire external providers** to run drills. That gets them
tested on scenarios they wouldn't have thought of, and makes the test independent —
removing bias.

In some cases the simulated attack can be a program that mimics an attack. That
isn't necessary, especially for a first or second drill. A tabletop exercise is
enough.

**The distinction that matters: cyber drills are not disaster recovery testing.**
DR testing takes an IT system down and tests recovery — high availability, restoring
backups. A cyber drill specifically tests response to a *cyber security incident*.
Organisations confuse these constantly: asked whether they run cyber drills they
say yes, and the evidence they produce is their disaster recovery plan.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Cyber drill | A simulated incident used to test the response plan | Turns a written plan into a tested capability |
| Tabletop exercise | Scenario played through discussion and communication | Cheap, effective, and the right starting format |
| Scale of exercise | Team-level up to board and CEO involvement | Determines what's being tested — technical steps or executive decision-making |
| Communication as the target | Testing how stakeholders talk to each other under pressure | The gap drills most reliably expose |
| Prepared communications | Templates and messages written before the incident | Prevents improvised statements to the press under stress |
| External facilitation | An outside provider designing and running the drill | Unfamiliar scenarios, and independence from internal bias |
| Simulation tooling | Programs that mimic attack activity | Available, and not required early on |
| Drill vs DR test | Testing incident response vs testing system recovery | A frequent and consequential confusion |

## Where this shows up in a real job

The tabletop format is the part I could contribute to now. Running a session where
the value comes from facilitation and communication rather than tooling is close to
what the WordPress meetups and do_action events involved — designing something a
room of people with mixed expertise can engage with, and keeping it moving.

The incident response labs I've worked through are the other half: I've played
through scenarios, but as the responder in a controlled environment rather than as
a facilitator with executives in the room. Those are different skills, and the
second is the one this lesson is about.

The communication gap the lesson describes is recognisable from support. Explaining
a technical problem to someone who needs a decision rather than an explanation is a
distinct skill from diagnosing it, and plenty of capable engineers find it
uncomfortable. A drill is one of the few settings where that gets practised
deliberately.

## My take

The drill-versus-DR confusion is the most immediately useful thing here, because
it's a **specific evidence question**. Asked whether they run cyber drills, an
organisation says yes. Asked for the evidence, what arrives is a DR test report:
system taken offline, backup restored, recovery time recorded. That answers "can we
restore a system" and not "do we know who decides, who calls the regulator, and
what we tell customers." Requesting the artefact and reading what it actually
tested is the whole check — and it's the evidence-over-assertion principle from
module 3 applied to a place where the assertion is usually sincere.

Three things:

**Drills test the parts of the plan nothing else touches.** Detection can be tested
technically, containment can be rehearsed by responders — but the escalation
threshold, the decision to notify a regulator, the call to the CEO and the
statement to the press exist only as paragraphs until someone has to execute them
under time pressure. That's precisely the enterprise-plan layer from lesson 4, and
a tabletop is the only realistic way to exercise it.

**The dismissal by technical practitioners has an answer worth having ready.**
"It's not technical" is true and irrelevant — the drill isn't testing whether
engineers can contain malware, it's testing whether the organisation can make
decisions while they do. Recast that way, the exercise is aimed at the layer most
likely to fail, which is also why the people most likely to dismiss it are the ones
least affected by that failure.

**Prepared communications are the most transferable output.** A drill that produces
nothing but a set of drafted holding statements, a contact tree that's been
verified, and an agreed spokesperson has already paid for itself. Those are
artefacts, they survive the exercise, and they're exactly what nobody can write
well at 2am. When assessing a drill, I'd ask what *artefacts* came out of it rather
than whether it happened.

One assessment question worth adding: **who was in the room?** A drill involving
only the security team tests the security team. The gap the lesson identifies —
security struggling to communicate upward — cannot be found, let alone fixed, in an
exercise where nobody from upward was present.
