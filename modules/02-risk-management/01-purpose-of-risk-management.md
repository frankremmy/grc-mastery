# The real purpose of cyber security risk management

> Module 02, lesson 1. Why the spreadsheets exist, answered with a budget problem
> rather than a definition.

## Summary

The lesson opens on a complaint I've heard myself: experienced analysts asking
why GRC people spend their lives documenting risks in spreadsheets, and whether
any of it is necessary. The answer is a scenario. You run security for a
hospital. You commission a penetration test, the testers get in, and the report
comes back with a long list of real findings. Fixing all of them costs $5 million.
You have $500,000. Which findings do you fix, which do you leave, and how do you
justify either answer to anyone?

That question can't be answered from the technical report. The report tells you
what's broken; it doesn't tell you what matters. Rating each finding for impact
and likelihood, ranking the results and writing them down is the activity that
turns a list of defects into a decision anyone can make — and that activity is
cyber risk management. Once it exists, senior management has something they can
act on: fund the remediation, or knowingly accept the risk.

The framing I'm keeping is **risk management as a translation layer**. The board
doesn't know what a firewall is and doesn't need to. It does understand risk, and
in the hospital case it understands that some of these findings end in harmed
patients. The CISO's job is to carry the technical reality up into language that
supports a funding decision, and to bring the decision back down. Directors are
the ones who ultimately answer for the organisation's risk exposure, so they need
to be the ones choosing — which they can only do if someone translates first.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| The prioritisation problem | Remediation cost routinely exceeds available budget | The permanent condition of the job; the reason risk management exists at all |
| Impact and likelihood | Rating how bad a risk would be, and how probable it is | The two axes that turn an unordered finding list into a ranked one |
| Risk management as translation | Converting technical findings into business-language risk | Without it, the board can't fund or accept anything, so nothing gets decided |
| Risk acceptance | Management knowingly choosing to live with a risk rather than fix it | A legitimate outcome — but only when someone senior owns the decision |
| Board accountability | Directors answer for the organisation's risk exposure | Determines who the reporting is actually *for*, which shapes how it's written |
| Non-financial impact | Harm that isn't measured in money — patient safety, in the hospital case | The impacts that most matter are often the ones the scale handles worst |

## Where this shows up in a real job

This is the closest the course has come so far to something I do daily. Support
triage *is* risk prioritisation under a hard capacity limit: more broken things
than hours, a severity call on each, and a defensible reason for the order. The
mechanics are smaller but the shape is identical, including the part where the
honest answer to "why wasn't this fixed?" is "because these three were worse."

The translation half is the part I'd argue is my strongest transferable skill
into GRC, and it's the one that looks least impressive on a CV. Four years of L2
and L3 has been four years of restating technical failure in terms of what it
costs the person on the other end. That's the same move the CISO makes to the
board, aimed at a different audience.

The health-sector framing lands close to Helium Health, though I want to be
precise about the seat I was in: I coordinated an ISO 27001 certification, which
is compliance work. I wasn't making treatment calls on clinical risk.

## My take

The hospital scenario is the best answer I've seen to "why do GRC people live in
spreadsheets". The necessity is structural: remediation cost exceeds budget as a
permanent condition, and nothing in a technical report tells you which findings
matter most. Rating and ranking them is what turns a defect list into a decision
someone can actually make.

Two things I want to hold onto. Acceptance is a legitimate outcome, but it only
counts when a named person senior enough to carry it signs, with a date it gets
revisited and a record of what was known at the time — otherwise it's the risk
falling off the list with extra steps. And the example works because patient harm
isn't measured in money, which is a useful reminder that the impacts that matter
most are often the ones a financial scale handles worst.

The findings list also isn't the risk universe. It's what testers found in what
they were pointed at; the biggest exposure might be a supplier, a process or a
person that no pentest would surface.
