# Asset classification

> Module 04, lesson 4. Deciding which assets matter — and being clear that it
> isn't the GRC professional's decision to make.

## Summary

With a list of assets collected, the next step is classifying them: recording
whether each one is **critical** and whether it's **sensitive**.

The important qualifier comes immediately. Critical and sensitive mean critical
and sensitive *to the business*, not to the person doing the assessment. And the
person doing the assessment shouldn't be the one deciding — every business is
different, and the judgement belongs to the business stakeholders who own the
work. The GRC professional's job is to go and ask them.

**The criticality matrix** is the usual instrument — typically a spreadsheet that
defines what "critical" means for this organisation. Classification is driven by
the asset's impact on the business. For an insurance company: if the claims
database were destroyed or compromised, could the business function? Almost
certainly not, so it's critical.

**Maximum tolerable outage** is the second measure. How long can the business
cope without this application — an hour, two hours, longer? The answer is a direct
indicator of how critical the asset is.

Ideally the **enterprise risk team** defines what critical and sensitive mean for
that particular business. GRC takes those definitions and assesses each asset
against them — then validates every rating with the relevant business stakeholder
rather than assuming.

The two worked examples make the point through contrast:

**The insurance claims database.** Holds all the claims data and financial
information. It *sounds* critical, and probably is — but that still needs
validating. You go to the claims department, explain the classification exercise,
and ask them to rate it against the matrix: what's the impact, how long could you
tolerate an outage, is it sensitive, is it critical.

**The employee gift card portal.** An internal web application where staff claim
gift cards. If it goes down, can the business function? Yes. Maximum tolerable
outage? Possibly months. So it looks non-critical — and even that needs checking
with HR. Perhaps morale is poor and the rewards scheme is carrying more weight
than an outsider would guess. GRC has no way of knowing that, which is exactly why
the question gets asked rather than answered from the desk.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Classification | Recording how critical and how sensitive each asset is | Turns a flat inventory into something that can drive priority |
| Critical to the business | Impact on the organisation's ability to function, not on security's preferences | The rating belongs to the business, and so does the judgement |
| Criticality matrix | A defined scheme — usually a spreadsheet — setting out what each rating means | Makes ratings comparable and challengeable rather than personal |
| Maximum tolerable outage | How long the business can operate without the asset | A concrete, answerable proxy for criticality |
| Enterprise risk team | Defines what critical and sensitive mean for this organisation | Keeps definitions consistent across cyber, financial and operational risk |
| Stakeholder validation | Confirming every rating with the department that owns the work | The step that separates a real classification from a guess |
| Documenting the outcome | Recording ratings in asset management software or a spreadsheet | The classification only exists if it's written down |

## Where this shows up in a real job

Maximum tolerable outage is a question I've effectively been answering for years
without the term. Triaging a broken WooCommerce store is exactly this: checkout
down is measured in lost revenue per hour, a broken admin screen can wait until
tomorrow. The severity call is a criticality judgement made under time pressure
and without a matrix.

The gift card example lands close to something I recognise too. Support gets a
steady stream of issues that look trivial from a systems perspective and matter
enormously to the person reporting them, and the technical view of importance is
frequently wrong. The lesson's point that HR might rate a rewards portal far
higher than an outsider would is the same phenomenon with a governance wrapper.

At Helium Health, patient data was obviously the critical asset and nobody needed
a matrix to say so. What a matrix would have helped with is everything in the
middle — the dozens of systems where the honest answer is "fairly important" and
where consistency matters more than precision.

## My take

The instruction not to decide is the most professionally useful thing in this
lesson. It's tempting to classify from the desk — you've seen the architecture,
you know which database holds what, and booking meetings with six departments is
slow. But criticality is a statement about business consequence, and that
knowledge sits with the people doing the work. Getting it wrong in either
direction is costly: over-classify and everything is critical, so nothing is
prioritised; under-classify and a control gap goes unnoticed on something the
business actually depends on.

Three things:

**Maximum tolerable outage is the best question in the module so far.** "Is this
critical?" invites a yes from everyone, because no department thinks its systems
are unimportant. "How long could you work without it?" produces a number, forces a
real answer, and is checkable against what happened the last time it broke. It
converts a status question into an operational one.

**Stakeholder input needs calibration as well as collection.** Every department
will rate its own systems highly, and asking without a shared matrix produces a
list where everything is critical. That's what the enterprise risk team's
definitions are for — they make one department's "high" mean the same as another's.
Collecting opinions without that anchor gives you an average of local biases.

**Classification is a claim with consequences, so it should be signed.** A
criticality rating drives backup frequency, recovery targets, monitoring, access
restriction and where remediation money goes. The department that rated the gift
card portal as low is, in effect, accepting a slower recovery for it. Recording
who gave the rating and when makes that visible — and it's the same discipline as
a named risk owner on a register entry.

**Availability isn't the whole picture.** Maximum tolerable outage measures
availability, and the lesson pairs it with sensitivity, which is really about
confidentiality. Worth noting that an asset can rate low on outage tolerance and
still be highly sensitive — a research archive nobody touches daily, for instance —
so the two ratings need to be kept separate rather than collapsed into one score.
