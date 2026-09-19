# Problems with education and awareness in the real world

> Module 06, lesson 6. Two bad ideas that survive in senior management, and what
> each one costs.

## Summary

**Problem one: the "one click and it's game over" belief.**

There are people — including CIOs, general managers and senior executives — who
believe that if a single employee clicks a phishing link, the organisation is
finished, and that security investment is therefore pointless. The lesson's guess
at the origin is salespeople pushing phishing software and awareness training,
persuading executives that this is the most important thing there is.

It isn't true, and defence in depth is why. A click isn't the end of the story.
The payload can be caught at the proxy on its way out, anti-malware can stop it, or
a good analyst in the security operations centre can spot the unusual behaviour and
block it. Many things can still happen after the click.

So part of the GRC job is educating senior management and business leaders:
awareness matters, and it is not the whole of security. The belief is dangerous
precisely because it leads leaders to stop investing — if it's hopeless, why fund
it.

**Problem two: measuring the programme by real phishing incidents.**

Some organisations judge their awareness programme by counting actual phishing
incidents. Five users fell for real phishing last year, one this year, therefore
the programme works.

That isn't accurate, for two reasons:

- **Luck.** The organisation may simply have received fewer phishing attacks this
  year. The programme might be effective — you can't tell from this.
- **Blind spots.** Some organisations are bad at detecting phishing. Users may be
  falling for attacks and nobody knows. This happens in fairly large organisations.

So when an IT manager says the programme is excellent because there have been no
phishing incidents, that's not evidence. The answer is to look into the programme
properly using the assessment steps from the previous lesson.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| "One click, game over" | Belief that a single click dooms the organisation | Leads to disinvestment, because the effort appears futile |
| Post-click controls | Proxy, anti-malware, SOC detection after a click | The evidence that the belief is wrong |
| Vendor-driven fear | Security sold by overstating a single threat | A plausible source of the distorted view |
| Educating executives | Explaining where awareness sits among controls | A GRC responsibility, not an optional extra |
| Incident count as a metric | Judging the programme by real phishing incidents | Confounded by attack volume and by detection quality |
| Absence of evidence | No reported incidents ≠ no incidents | Silence may mean nothing is being detected |

## Where this shows up in a real job

The second problem is the one I recognise most directly. In support, "no tickets
about X" almost never means X isn't happening — it means people aren't reporting
it, or it isn't being noticed. The absence of a signal and the absence of a problem
look identical from a dashboard, and telling them apart requires knowing whether
the detection was ever capable of firing.

The first problem I've mostly seen in its smaller form: site owners who conclude
that because a breach is possible, effort is pointless — so they skip backups and
updates as well. Fatalism doesn't stop at the control that prompted it; it spreads
to the ones that would have limited the damage.

I haven't had to make this argument to an executive, and it's clearly a
presentation skill as much as a technical one.

## My take

The two problems are the same error pointing in opposite directions, which is what
makes them worth learning together. "One click and we're finished" treats one
control as everything. "No incidents, so we're fine" treats a single metric as
proof. Both collapse a layered system into a single number, and a GRC professional's
contribution in each case is restoring the layers to view.

Three things:

**The fatalism argument has a specific counter, and it's a question rather than a
lecture.** Telling an executive that defence in depth exists rarely moves anyone.
Asking *"what actually happened the last time someone clicked?"* does, because
either the organisation can describe the detection, containment and reset — in
which case it has just disproved its own belief — or it can't, in which case the
belief isn't the problem, the missing detection is. Same question, and it's useful
whichever way it resolves.

**"No incidents" is unfalsifiable until you know the detection works, and that's
testable.** The chain to check is whether phishing reaching users can be seen,
whether credential use from unusual locations is detected, whether reports from
employees are recorded anywhere, and whether anyone reviewed them. An organisation
that can answer those has earned the right to interpret a low incident count. One
that can't has a reporting gap dressed as a success. This is where the report-rate
metric earns its place — zero reports in a year is not a good sign, it's an alarm.

**A low incident count and a healthy programme can both be true, and saying so is
what makes the challenge credible.** The point isn't that the organisation is
deceiving itself; it's that the number can't distinguish between three different
worlds — fewer attacks, better people, or worse detection. Framing it that way
invites the client to help work out which, rather than defending a claim. That's a
more productive posture than "your metric is wrong," and it's the difference
between a finding that gets acted on and one that gets argued with.

One thing worth holding from the vendor observation: fear is a selling technique,
and it distorts priorities in a specific direction — towards whatever is being
sold. The corrective isn't cynicism about vendors, it's insisting that spending
follows the risk assessment. Which is where module 2 came in, and it's the same
answer to the executive who thinks awareness is everything and the one who thinks
it's pointless.
