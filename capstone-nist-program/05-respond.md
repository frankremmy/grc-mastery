# Respond — solution walkthrough

> Capstone, lesson 5. _Fifteen controls, fifteen fails, and what that means for
> the recommendations._

## Summary

Every control in Respond fails. Oscorp has an IT team and no security resource,
no detection capability and no response capability. There is no plan to execute,
no defined roles, no reporting criteria, no stakeholder coordination, no
forensics, no categorisation, no containment or mitigation procedures, no
lessons-learned step, and nothing to update.

The walkthrough is direct about what that means for the deliverable: **this is
the biggest problem Oscorp has, and it should drive the recommendations.** An
organisation in this position has no way of knowing whether it has been
compromised, and no way of responding when it is told. That combination is the
red flag.

## Where my assessment diverged

Nowhere. I scored 0 of 15 and so did the solution — the only function where we
matched exactly.

That agreement is worth something, because the scoring rule that caused my twelve
divergences elsewhere doesn't apply here. There was no partial implementation to
be generous or harsh about. Where a capability genuinely does not exist, the
assessment is the same however you read the control.

## My take

This confirms the framing I led my executive summary with. I wrote that the zero
in Respond is not one gap among many — it means that on the day Oscorp has a
serious incident there is no plan, no roles, no escalation, no forensics and one
generalist analyst working business hours. The walkthrough reaches the same
conclusion and calls it the organisation's biggest problem.

**One place my roadmap sequences differently from that emphasis, and I want to be
explicit about it.** If detection and response is the single biggest problem, the
obvious move is to put the SIEM in year 1. I put the incident response plan and
an external IR retainer in year 1 Q3, and the SIEM and managed detection in year
2.

The reasoning: the plan and the retainer are what actually close the Respond gap,
and both are fast and comparatively cheap. A retainer buys forensics and surge
capability that Oscorp cannot justify hiring. The SIEM sits later because its
value depends on knowing what to onboard, which depends on the asset inventory
and the SaaS catalogue that don't exist yet — and Oscorp has already demonstrated
what happens when it buys a security tool ahead of the process to use it, with
Qualys producing findings nobody actions.

**But there's a reasonable argument the other way**, and I don't want to pretend
otherwise. You could pull managed detection forward to year 1 Q4, accept
incomplete log coverage, and reason that partial monitoring beats none while the
inventory work continues in parallel. Given Oscorp holds research IP and has
already had a suspected insider disclosure, an assessor who judged the exposure
severe enough to accept imperfect coverage would be making a defensible call.

The distinction between the two options is a risk appetite question rather than a
technical one — which is exactly the kind of decision the cyber risk process in
year 1 Q2 exists to make. I'd present both sequences to Norman Osborn with that
framing rather than assert mine as the only answer.
