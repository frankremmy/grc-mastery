# Risk registers

> Module 02, lesson 4. Where identified risks go to become someone's problem, on
> purpose.

## Summary

A risk assessment produces a report — the process, the methodology, the findings.
But the place the risks have to land is the risk register. Its form is a detail:
a spreadsheet in a small organisation, enterprise GRC software in a mature one.
What makes it the register isn't the tooling, it's that senior management can see
it.

That visibility is the whole argument. There's usually an enterprise risk
committee looking across every material risk the organisation carries — financial,
operational, cyber — and a cyber risk that isn't in the register isn't in that
conversation. Technical analysts are good at stopping attacks and generally not
equipped, or positioned, to raise what they see in a form the board can act on.
Executives and CIOs don't see what happens in the trenches. Writing the risk down
in the register is the mechanism that closes that distance, and it's a large part
of what the GRC role is actually for.

The fields in a simple register: describe the risk, rate the impact and say what
that rating means for the organisation, rate the likelihood of it materialising,
add notes giving context, and — the one the lesson puts most weight on — assign a
**risk owner**. The owner is a named person responsible for following the risk
through to either mitigation or a decision to accept it.

Acceptance is the honest ending the register makes possible. There is never
enough money to close every finding, so a risk gets written down, and a senior
manager or executive signs off: we know about this, we're choosing to carry it for
now, we'll look again in six months. The register is what turns "we didn't get to
it" into a decision someone made on the record.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Risk register | The record of identified risks, their ratings, owners and decisions | The artefact that gives risks an existence outside the security team |
| Enterprise risk committee | The forum reviewing all material risks across the organisation | Cyber risk competes here with financial and operational risk, in the same language |
| Risk description | A plain statement of the risk and what it would mean | Written for a reader who wasn't in the assessment |
| Impact and likelihood | The two ratings, each with a stated reason | Ratings without reasoning can't be challenged or compared |
| Risk owner | The named individual accountable for driving the risk to a conclusion | A risk with no owner has no one to follow it up; "the security team" is not an owner |
| Risk acceptance | A documented decision to carry a risk rather than treat it | Legitimate — the register's purpose is to make it deliberate and attributable |
| Sign-off | The senior person who accepts the risk, on the record | Acceptance is only meaningful from someone with the authority to carry it |
| Review date | When the accepted risk gets looked at again | Prevents "accepted" quietly becoming permanent |

## The template

`templates/risk-register.csv` is the blank I'll use for the practical
assessments. Columns, and why each is there:

| Column | Purpose |
| --- | --- |
| `risk_id` | Stable reference so a risk can be cited in a report or a meeting |
| `date_raised` | When it entered the register; makes age visible |
| `scope` | The system, project or business area the risk sits in |
| `risk_description` | The scenario in plain language |
| `threat` | The actor or event |
| `vulnerability` | The weakness being exploited |
| `existing_controls` | What's already in place — the starting position |
| `likelihood` / `impact` | The two ratings, with reasoning in `notes` |
| `inherent_rating` | The combined rating before new treatment |
| `proposed_treatment` | The control or action proposed |
| `treatment_effect` | Whether it reduces likelihood or impact |
| `residual_rating` | What's left once the treatment is in place |
| `owner` | Named individual, not a team |
| `decision` | Treat, accept, transfer, avoid |
| `decided_by` / `decision_date` | Who signed and when |
| `review_date` | When it comes back |
| `status` | Open, in progress, accepted, closed |
| `notes` | Context, reasoning behind the ratings, anything a reader needs |

Registers live as CSV rather than markdown tables: GitHub renders CSV as a table
anyway, so nothing is lost on the page, and a CSV diffs cleanly and matches the
artefact a real organisation would hand you.

## Where this shows up in a real job

The register is the artefact I recognise most from the Helium Health ISO 27001
work — it was the thing we maintained, and the thing the auditor asked for.
What I understand better now is why the owner column mattered so much and why
filling it in was so often the hard part. A risk with no owner doesn't get
followed up; a risk owned by "IT" is owned by nobody.

There's a support parallel worth naming. A known issue with no assignee and no
review date behaves exactly like an unowned risk: everyone has seen it, nobody is
moving it, and it resurfaces every few weeks as if it were new. The register is
the same fix applied to a different problem — write it down, name someone, set a
date.

## My take

The register's real function is transfer of responsibility, not documentation.
Before it's written down, an unfunded risk is the security team's private worry.
After it's written down, rated, owned and signed, it's an organisational decision
with a name attached. That's the step that changes what happens when it goes
wrong — and it's why calling a risk out matters even when you already know there's
no budget to fix it.

Three things I want to get right when I build one:

**The owner is a person.** Not a department, not a role that's currently vacant.
Someone who can be asked in six months what happened.

**Acceptance needs a signature, a date and an expiry.** All three. Sign-off
without a review date is how an accepted risk becomes a permanent one, and the
organisation loses the ability to say what it knew and when.

**Write the reasoning next to the rating.** "Impact: high" is unarguable in the
worst way — nobody can challenge it, so nobody engages with it. "Impact: high —
checkout unavailable, roughly £X of sales per hour, no manual fallback" gives a
reader something to push back on, and pushing back is the point.
