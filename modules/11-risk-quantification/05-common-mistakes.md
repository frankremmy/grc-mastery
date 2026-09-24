# Common mistakes with cyber risk quantification

> Module 11, lesson 5. _Why most organisations either never start, or start and
> then let it rot._

## Summary

**Most organisations don't do it at all.** The industry's cyber risk maturity is
generally lower than its operational maturity — plenty of organisations have a
decent SOC, analysts and a compliance programme, and are still struggling with
asset management and detection. Quantification gets filed under "advanced", and
the reasoning is that everything else must be fixed first.

The course disagrees, and the argument is a good one: **you don't have to
quantify everything.** Quantification works perfectly well as a targeted
exercise. Use it to justify a specific purchase. Use it to present the top ten
risks to the board with monetary values attached, rather than handing executives
a spreadsheet covering everything the organisation owns. The value arrives
immediately and without an organisation-wide programme behind it. Start narrow
and grow.

**The numbers are often wrong, in two different ways.** The obvious one is the
security team working in isolation and making up figures for assets it doesn't
own. You cannot produce these numbers alone; the business value of an asset comes
from the people who run it.

The subtler one — the failure the course says it repeatedly finds on returning to
organisations two years later — is that **the calculation was done once and never
revisited.** None of these inputs are constant. Phishing volume changes. The cost
of a ransomware event changes. An application that was critical this year may
have been migrated or deprioritised. If you are presenting top risks to
executives, stale numbers get noticed — someone will ask why a capability the
business abandoned is still showing a large exposure, and the credibility of the
whole exercise goes with the answer.

**Overcomplication.** Beginners in particular disappear into trying to calculate
every branch of the model precisely. The model looks complex and invites that
response, but in practice the work is a conversation with stakeholders and a
short calculation. A junior taking six months over a single quantification isn't
being rigorous, they're lost.

**Stopping at the risk figure.** The most common miss, including among
experienced consultants: quantify the risk, note the cost of the solution,
observe that one is bigger than the other, and stop. That is a correct conclusion
and a weaker case than it could be. Going the extra step — modelling the control's
effectiveness and calculating the return on the investment — is what makes senior
management take the work, and the team producing it, seriously.

## Key concepts

| Mistake | What it looks like | The correction |
| --- | --- | --- |
| Never starting | "We need to fix the fundamentals first" | Quantification is useful at any maturity; start with one decision |
| Boiling the ocean | Attempting to quantify the entire risk register | Top risks, or a single investment decision |
| Working in isolation | Security inventing asset values | Stakeholder input is what makes the numbers real |
| One-and-done | Calculated once, never revisited | Periodic review; inputs change every year |
| Stale exposure figures | Big numbers attached to things the business no longer cares about | Executives notice, and credibility doesn't recover easily |
| Overcomplication | Months spent perfecting one calculation | Good enough and defensible beats precise and late |
| Stopping at the risk number | "Risk is $500k, solution is $80k, obviously buy it" | Model the control's effect and present the return |

## Where this shows up in a real job

The one-and-done failure is the same pattern as almost every other artefact in
this course — the asset register that was accurate on the day it was built, the
supplier list that reflects who was being paid two years ago, the incident
response plan with a contact list full of people who've left. Documents that
describe a moving organisation decay unless something owns keeping them current.
Quantification is more exposed than most, because a stale number is presented to
executives *as a fact* and can be contradicted by someone in the room.

The overcomplication warning is one I'd apply to myself. My instinct with a model
like FAIR is to want every branch filled in properly before I'd trust the output,
and this lesson is a useful corrective: the objective is a defensible figure that
informs a decision, not a complete model. Perfect inputs that arrive after the
budget round have no value at all.

## My take

The "start narrow" argument is the most useful thing in this lesson, and it
reframes what quantification is. It isn't a programme the organisation adopts, it
is a **technique you apply to a specific question** — is this purchase worth it,
which of these three risks deserves the budget, what is our largest exposure.
Framed that way it needs no maturity prerequisite and no approval to begin,
because the first one can be done for a single decision on a spreadsheet. That's
also why I'd expect it to spread: one convincing business case creates demand for
the second.

On accuracy, I'd separate two things that "wrong numbers" runs together. Being
*imprecise* is unavoidable — every input is an estimate and the output inherits
that. Being *undefended* is a choice. An estimate with a stated source, a stated
assumption and a range around it is honest work even when it turns out wide. A
confident single figure with no provenance is the one that collapses under the
first challenge. I'd rather present a wide range I can defend than a narrow one I
can't.

The review point deserves a mechanism rather than good intentions, and the model
makes that easy: each input has an owner. The SOC owns threat event frequency and
susceptibility. Incident response owns the primary loss. Legal and the business
own the secondary loss. Vendors and experience own control effectiveness. If each
input is dated and attributed, refreshing the analysis becomes a short round of
requests rather than redoing the work — and you can see at a glance which figure
is three years old.

And the ROI point is the one with career consequences. The lesson frames it as
more persuasive, which it is, but the larger effect is on how the security
function is seen. A team that arrives with spending requests is a cost centre. A
team that arrives with a quantified return is doing what every other function
does when it asks for money. That is the actual argument for learning this.
