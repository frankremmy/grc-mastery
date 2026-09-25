# Common mistakes with NIST assessments

> Capstone, lesson 8. _How frameworks vary in practice, and why maturity scores
> deserve scepticism._

## Summary

**Frameworks are more alike than they look.** ISO 27001, PCI DSS, sector-specific
healthcare frameworks — the language differs, the controls all come back to the
same security fundamentals. Having worked one framework end to end, you can read
any of them. You don't need to memorise each one; you need to be able to
interpret a control and tie it back to something you understand.

**Expect variation in the wild:**

- Organisations using NIST will have spreadsheets that look different from this
  one, with slightly different interpretations of the same controls. Normal
- Organisations often **pick and choose** the controls relevant to them. Oscorp's
  critical infrastructure controls are a good example — an Oscorp-specific
  framework inspired by NIST would simply drop them
- Organisations **mix and match** across frameworks, taking some controls from
  NIST and others from elsewhere

**Pass/fail is one convention among several.** It answers a single question: does
the organisation have this control? But consider a vulnerability management
programme that works well and doesn't cover the whole estate. Calling that a
failure is inaccurate. "Partially effective", or "effective, further improvements
needed", describes it better, with the coverage gap recorded in the comments and
the recommendation.

**Maturity scoring is common and the course advises against it.** Consulting
firms often score each control 1 to 5 — 1 meaning not implemented, 5 meaning
implemented with continuous enhancement and possibly automation — then average
across controls to produce a single figure. An organisation will tell you it
"scored 3 out of 5".

Three problems:

**It is far less objective than it looks.** There will be scoring criteria, but
no two consultants score the same controls identically. Scores are limited by the
consultant's experience, by how much time they spent with the organisation, and
by how much the organisation chose to share.

**It gets used to demonstrate progress that may not exist.** Scoring 2.5 one year
and 3.5 the next makes a compelling slide for the board. If the underlying
scoring was subjective, the improvement may be an artefact of a different
consultant with a different judgement.

**Benchmarking against peers is worse.** Organisations ask for the industry
average, wanting to know how they compare. The data is incomplete — scores aren't
published — and the comparison is unsound to begin with. Worse, a low industry
average is sometimes used as justification: *our peers score badly too, so we're
fine.* That reasoning offers no protection whatsoever when you are the one
breached.

## My take

**This lesson retro-fits the cleanest explanation of my own divergences.** I
scored twelve controls Fail that the solution passed, and in almost every case
the honest description was neither — it was *partially effective*. Oscorp's asset
inventory exists and covers only laptops. Vulnerability scanning happens and
isn't scheduled. Awareness training is mandatory and happens once. A binary scale
forced each of those into a box that lost the information, and I consistently
chose the harsher box while the solution chose the kinder one. A three-point scale
would have let both of us record the same reality.

So the lesson I'd carry is not "be more generous" but **pick a scale with enough
resolution for what you're describing, and say which convention you used at the
top of the report.**

**On maturity scoring I'd add a mathematical objection to the practical ones.**
Averaging 1-to-5 maturity scores makes the same mistake module 11 identified in
risk heat maps: the scale is **ordinal**, not interval. Level 4 is better than
level 3, but nothing establishes that the distance from 3 to 4 equals the
distance from 1 to 2 — so the arithmetic mean of a column of maturity levels has
no defensible meaning. "We scored 3.2" is a number produced by an operation the
scale does not support, and the decimal place gives it a precision it cannot
possibly have. That's a stronger objection than subjectivity, because it holds
even if every consultant scored identically.

**One thing worth knowing about NIST's own terminology.** The CSF defines
**Implementation Tiers** — Partial, Risk Informed, Repeatable, Adaptive — and NIST
is explicit that these are *not* a maturity model and not a target to maximise.
They describe how rigorously an organisation's risk management practices are
integrated, and a smaller organisation may sit at a lower tier entirely
appropriately. The 1-to-5 maturity scoring consultancies apply is imported from
CMMI-style models, not from NIST. People conflate the two constantly, so being
able to separate "CSF Tiers" from "a maturity score" is a useful distinction to
have.

**And the benchmarking argument has a further edge now.** Where regulation sets a
floor — NIS2 for in-scope EU entities, DORA for financial ones — "our peers are
also weak" is not merely unhelpful, it's irrelevant. The comparator is the legal
minimum, not the industry average. Peer comparison is legitimate as *context* for
a conversation; it is never a target and never a defence.

## Closing note on the capstone

Working the whole framework once was the point. The controls were familiar
because every one of them traced back to a module in this course — asset
management, IAM, data security, detection, incident response, third-party risk,
risk management, governance. The framework didn't teach me anything new; it gave
me a structure to apply what the course had already covered, and a way to check I
hadn't skipped anything because it was less interesting.

The part I'd have got wrong without the walkthrough is the scoring judgement, and
that's a presentation skill rather than a knowledge gap. The substance held up.
