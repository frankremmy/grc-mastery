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

## Gotchas / what most orgs get wrong

- **The lesson proves prioritisation is necessary, then quietly assumes one
  method.** "Rate impact, rate likelihood, multiply, rank" is presented as *the*
  technique. It's a technique — and a contested one. Ordinal scales (1–5, or
  low/medium/high) aren't numbers you can legitimately multiply; the arithmetic
  produces an ordering that looks quantitative and isn't. Module 11 teaches FAIR,
  which exists largely because of this problem. The course teaches both and
  doesn't say they disagree. Worth flagging now so I read module 2 knowing
  module 11 is coming to argue with it.
- **The analysts complaining about spreadsheets are half right.** The lesson
  treats their objection as ignorance. The steelman: a register that doesn't lead
  to a funding decision or a signed acceptance is genuinely wasted effort, and
  plenty of them don't. The defence of risk management isn't "we document
  things", it's "documenting things is what unlocked the budget." If it didn't
  unlock anything, the analyst's complaint stands.
- **"Accept" without an owner and an expiry means "ignore".** The lesson names
  acceptance as a valid outcome but not what makes it valid. An accepted risk
  needs a named individual senior enough to carry it, a date it gets revisited,
  and a record of what was known at the time. Without those three, acceptance is
  just the risk falling off the list with extra steps.
- **A register built from pentest findings inherits the pentest's scope.** The
  $5M list is what testers found in what they were pointed at. The organisation's
  largest risk may be a supplier, a process, or a person, and no amount of ranking
  the report surfaces it. Treating the findings list as the risk universe is how
  you end up with a well-prioritised register that misses the thing that actually
  happens.
- **The hospital example is strong precisely because money isn't the unit.** The
  board understands patient harm without translation into dollars. Most risk
  matrices are calibrated in financial impact and handle safety, legal and harm
  impacts by squeezing them onto the same scale. The lesson's best example is one
  its own method struggles with.
