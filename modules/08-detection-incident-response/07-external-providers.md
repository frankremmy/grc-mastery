# The role of external service providers in incident response

> Module 08, lesson 7. Arranging expert help before you need it, because the
> arranging is what takes time.

## Summary

An **incident response retainer** is a contract — or simply an established
relationship — with an external firm specialising in incident response. It exists
for the case where a sophisticated attack exceeds what the organisation can handle
alone.

The value is **speed**. A retainer shortens the gap between the incident happening
and expert help arriving. Without one, the organisation is negotiating a contract
and doing supplier onboarding while an attack is underway.

**Who provides it:** specialist firms such as Mandiant or Verizon, or the large
consultancies like Deloitte and PwC. It can also come from **government or law
enforcement** — not unusual where a sophisticated incident affects critical
infrastructure.

**The GRC advice** is to establish that relationship in advance. It matters most
for small and mid-sized organisations without in-house expertise, and it remains
sensible for large ones.

**What it looks like in practice** can be as simple as a list of names and phone
numbers contactable 24/7.

And the reason it matters: rapid intervention in a serious attack can be the
difference between an incident costing **$500 and $500 million**. Both outcomes
happen.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| IR retainer | A pre-arranged contract or relationship with an IR specialist | Removes procurement from the critical path during an incident |
| Time to expert engagement | The gap between incident and specialist involvement | The variable the retainer is bought to reduce |
| Specialist IR firms | Mandiant, Verizon, the large consultancies | The commercial route |
| Government and law enforcement | State assistance, especially for critical infrastructure | A route many organisations don't realise exists |
| Contact list | Names and numbers reachable 24/7 | The minimum viable version of the arrangement |
| Capability honesty | Recognising what the organisation cannot handle alone | The judgement that makes the retainer necessary |

## Where this shows up in a real job

The general principle is familiar from support: the time to establish an escalation
path is before you need it. Working out who to call, whether they're reachable, and
whether anyone has authority to engage them — while something is actively
breaking — is the worst possible moment to discover the answer is no.

The Malta angle is worth noting for my own purposes. For regulated sectors here —
financial services, iGaming — there are national and sector arrangements for
incident reporting and assistance, and the ACSC template I read for the previous
lesson has a whole section on sector, jurisdictional and national response
arrangements. Knowing what exists in the jurisdiction you're advising in is part of
this recommendation, and it's specific rather than generic knowledge.

I haven't been involved in engaging an IR firm or in the contracting around one, so
this is advisory knowledge rather than experience.

## My take

The strongest framing is that **a retainer removes procurement from the critical
path.** The expertise is available commercially at any time — what isn't available
during an incident is the two weeks it takes to agree a contract, run supplier due
diligence, negotiate liability terms and get purchase approval. The retainer isn't
buying skills you couldn't otherwise obtain; it's buying the paperwork being done
in advance. Framed that way it's easy to justify to a finance director, because the
cost is modest and the thing it removes is unambiguous.

Three things:

**A contact list is the minimum, and it decays like every other list.** Names and
numbers reachable 24/7 is genuinely the starting point — and it's also the artefact
most likely to be out of date, because people change jobs and nobody revisits it
until it's needed. So the assessment question isn't "do you have a retainer" but
"when was the contact list last verified, and has anyone ever called the number."
That pairs with the drill from the previous lesson: a tabletop exercise that
includes phoning the retainer contact is a cheap way to test both at once.

**The terms matter more than the existence.** Retainers vary considerably — how
many hours are included, what the response time commitment is, whether the provider
has done any preparatory work on your environment, and whether unused hours can be
spent on proactive work. A retainer with a 72-hour response commitment is a
different product from one promising engagement within four hours, and both are
called a retainer. Worth asking for the terms rather than accepting the label,
which is the same discipline as asking what an MSSP contract actually covers.

**Provider familiarity is what turns hours into speed.** A firm arriving cold spends
its first day learning the estate — what systems exist, where logs are, who to talk
to. A provider who has been given an architecture overview, an asset inventory and
access arrangements in advance starts investigating instead. That's a direct payoff
from module 4's asset management work, and it's an argument for doing preparation
that otherwise looks optional.

The $500-to-$500-million framing is rhetorical, and the mechanism underneath it is
real: the cost of an incident scales with dwell time, because an attacker who is
undisturbed keeps moving, keeps escalating privilege, and keeps taking data. Every
hour before a competent responder engages is an hour of that compounding — which
is why time-to-engagement is the number this control is aimed at, and a reasonable
thing to put in a risk register entry.
