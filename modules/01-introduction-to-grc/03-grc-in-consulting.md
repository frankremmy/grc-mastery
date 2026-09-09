# How does GRC fit within cyber security consulting?

> Module 01, lesson 3. Why external consultants exist at all, and the two very
> different jobs they get hired to do.

## Summary

The lesson starts from a gap I hadn't named before. A security team does the work
of managing cyber risk, but senior management has no direct way to know whether
that work is actually happening or actually working. They're being asked to take
the security team's word for it. That gap — between *doing* security and
*evidencing* it to people who can't evaluate it themselves — is where external
consultants get pulled in, and it's why GRC knowledge is what the job needs. What
a consultant hands to the board isn't a technical report; it's a risk-based view
of the organisation's security posture, in language the board can act on.

The second half is the distinction I'll actually use: **assessment vs advisory**.
Assessment is the assurance job — an independent party comes in, evaluates, and
reports findings upward. Advisory is the opposite posture: you're hired to help
build the thing. A bank going for PCI DSS brings in a consultant to help
implement the program and to bring across what they've seen work at other orgs.
They're not there to judge your compliance, they're there to get you there.

The detail that makes this concrete: an advisory consultant effectively operates
*as part of your security team*, not as an external entity. Assessment
consultants are external by definition — the independence is the product.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| The assurance gap | Senior management can't verify the security team's work by inspecting it themselves | The whole commercial reason external cyber consulting exists |
| Assessment (assurance) | An independent party evaluates posture and reports findings to management | The consultant's independence *is* the deliverable; lose it and the report is worthless |
| Advisory | A consultant hired to help design or implement a program, bringing cross-industry experience | Judged on whether the program gets built, not on whether it passes |
| Risk-based view of posture | Findings framed as business risk and priority, not as a technical defect list | A board can fund or accept a risk; it can't act on a vulnerability scan |
| Insider vs outsider posture | Advisory consultants work as part of the team; assessors stay outside it | Determines what they can see, and what their opinion is worth afterwards |

## Where this shows up in a real job

I've been on the receiving end of this rather than doing it. The Helium Health
ISO 27001 work involved exactly this split — external help getting the ISMS into
shape, and a separate external party whose whole job was to not be involved in
building it. At the time I read that as bureaucratic duplication. It isn't: the
second party's report only means something *because* they didn't build the thing.

The assurance gap itself is familiar from support, at a smaller scale. "Is the
team handling escalations properly?" is not answerable by asking the team. It
needs evidence someone outside the queue can check — which is the same structural
problem the board has with security, minus a few zeroes.

I should be careful not to overclaim here: I have no consulting experience. What
I have is the client-side view of one certification, which is a different seat.

## Gotchas / what most orgs get wrong

- **The two roles conflict, and the lesson doesn't say so.** If a firm advises you
  on building your program and then assesses it, they're auditing their own work.
  The advisory consultant who "acts as part of your team" has, by that very fact,
  disqualified themselves from assuring it. This isn't a hypothetical purity
  concern — it's the thing independence rules in the audit world exist to stop,
  and it's why large firms wall the two practices apart. Worth checking how PCI's
  QSA independence requirements handle exactly this case, since the lesson uses
  PCI as its advisory example.
- **"We got a clean report" is the compliant-is-not-secure error again.** An
  assessment is point-in-time and scope-limited. Management reads it as a verdict
  on the organisation; it's a verdict on whatever was in scope, on the days the
  assessor looked.
- **Scope is set by whoever's paying.** The consultant assesses what the
  engagement letter says. An organisation that doesn't want a particular area
  looked at simply leaves it out, and nothing in the resulting report will say so
  loudly. When reading someone else's assessment, the scope section is the most
  informative page in it.
- **Advisory creates a knowledge cliff.** Bringing in cross-industry expertise
  works, but when the engagement ends the expertise leaves unless someone internal
  owned it the whole way through. Orgs that treat advisory as outsourcing rather
  than as transfer end up re-hiring for the same problem in two years.
