# Conduct cyber security risk assessments

> Module 02, lesson 3. Working through scenarios on a scoped system, and proposing
> controls that actually move something.

## Summary

A risk assessment starts with a scope. Not "the organisation" but a defined thing
— an application, a project, a system — because the threats worth listing depend
entirely on what you've drawn a box around.

The worked example is a supermarket's payment application, which stores payment
and customer information, and which we're told to treat as not internet-connected.
That assumption does real work: asked whether external attackers are a threat, the
answer for this scope is largely no, so it doesn't earn a place in the assessment.
Ruling a threat out on the basis of actual exposure is as much a part of the job
as listing the ones that stay in.

Two scenarios carry the lesson. First, **availability**. If the application is
down, customers are queuing and nobody can pay. Impact on the business is high —
depends on the supermarket, but a till that can't take money is straightforwardly
serious. The proposed control is a fallback: a machine to one side running a
spreadsheet to capture sales while the application is fixed. The detail I want to
keep is what that control does and doesn't do. It doesn't make the outage any less
likely. It makes the outage cost less. Controls act on likelihood or on impact,
and knowing which one you're buying is the difference between a considered
treatment and a purchase.

Second, **insider fraud**. A cashier takes a customer's money and doesn't record
the sale. Likelihood here is a judgement about context rather than technology — a
family-run shop is not the same bet as a newly hired cashier nobody knows. The
proposed control is CCTV, which works by changing the cashier's calculus and by
leaving evidence afterwards; it can't physically stop the act. That puts it on the
deterrent and detective side rather than the preventive side, which matters when
you're claiming what a control actually buys you.

The method underneath both is the same: walk concrete scenarios. Who or what could
act, against what, with what consequence, and what would change the odds or the
damage.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Scope | The defined system, application or project the assessment covers | Decides which threats are even in play; an unscoped assessment can't be finished |
| Risk scenario | A concrete story: this actor, this weakness, this consequence | The practical unit of assessment — easier to rate and to argue about than an abstract risk |
| Ruling a threat out | Excluding a threat because the exposure isn't there | A real output; the reasoning should be written down, since exposure changes |
| Impact | What it costs the organisation if the scenario happens | Half of the rating, and the half that survives when likelihood is a guess |
| Likelihood | How probable the scenario is, given context | Often a judgement about people and process rather than technology |
| Control | A measure that reduces likelihood or reduces impact | Naming which of the two it does keeps treatment honest |
| Preventive / detective / deterrent | Stop it, notice it, or discourage it | CCTV deters and detects; it doesn't prevent. Claiming prevention overstates coverage |
| Residual risk | What's left once the control is in place | The number that actually gets accepted or escalated |

## Where this shows up in a real job

The availability scenario is the one I've watched play out. A WooCommerce store
with a broken checkout is the same risk as the supermarket's dead till: the
customers are there, the intent to pay is there, and the money doesn't arrive.
Support tickets frame that as a technical fault, and the business frames it as
revenue per hour — same event, two vocabularies, which is the translation problem
from lesson 1 at a smaller scale.

The fallback control is familiar too. The stores that handle an outage best are
the ones with a manual route to take an order, and the ones that suffer most are
those where the application is the only path. That's an impact control, arrived at
by instinct rather than by assessment.

I'd be overclaiming to say I've run a formal risk assessment. What I've done is
the triage half — sizing an incident and choosing what to do first — without the
documentation or the scenario discipline that makes it repeatable.

## My take

Scenarios are the part I'll actually carry into practice. "What are the risks to
this application" is a question that produces a blank page; "a cashier rings up a
sale and pockets the cash" is a question you can rate, argue about and control.

Three things worth holding onto:

**Decide which term a control moves.** The spreadsheet fallback does nothing to
the likelihood of an outage and a lot to its cost. CCTV works the other way. Two
controls, two different jobs, and a treatment plan that doesn't distinguish them
ends up with three impact controls and a risk that still fires just as often.

**Re-rate after the control.** The rating you start with is the inherent risk. The
one that gets accepted, escalated or funded further is what's left afterwards. An
assessment that stops at "here's a control" hasn't finished the sentence.

**Controls bring their own risks.** The fallback spreadsheet holds payment and
customer data on a machine to the side of the till, with none of the protection
the application had. That's availability bought with confidentiality, which may
well be the right trade — but it's a trade, and it should appear in the assessment
rather than be quietly introduced by the fix. Worth noting too that an application
storing payment card data brings compliance obligations of its own, which is a
different question from whether it's technically exposed.
