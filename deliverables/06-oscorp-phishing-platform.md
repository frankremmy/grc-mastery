# Evaluating a simulated phishing platform — Oscorp

**Module:** 06 — Security Education and Awareness
**Type:** Practical assessment
**Status:** My own answer, written before seeing the course solution.
**Role:** External cyber security consultant advising Oscorp.

---

## Situation

Norman Osborn was taken to lunch by a cyber security vendor. The sales
representative argued that the human element is the weakest link, stressed the
importance of simulated phishing, and pitched his company's platform. Norman has
asked me to evaluate whether it's worth the investment, noting an excess in budget
following the success of the new medication.

Oscorp's current programme: one security training module, completed on joining,
covering general security "tips". Introduced in 2013 when the company was founded.

---

## My answer (as submitted)

Before investing in the simulated phishing platform, I would first assess Oscorp's
current security awareness program. The existing approach is clearly outdated
because employees only receive a general security training module when they join,
and the content has not been significantly updated since 2013.

I would recommend improving the overall security awareness program rather than
treating simulated phishing as a standalone solution. Training should be refreshed
regularly and cover current threats such as phishing, social engineering,
credential theft, suspicious links, MFA-related attacks and safe handling of
sensitive information. Employees should also receive periodic refresher training
instead of training only during onboarding.

The proposed phishing platform should then be evaluated through a pilot before
committing to a full purchase. The pilot could involve a controlled group of
employees and test whether the platform can safely simulate realistic phishing
scenarios without disrupting business operations.

I would assess features such as customisable phishing scenarios, automated training
for employees who need additional support, reporting capabilities, integration with
Oscorp's email environment, data protection, access controls and the vendor's
security practices.

The purpose of phishing simulations should be education and risk reduction rather
than blaming employees. Results should be used to identify areas where additional
training is required. Useful measures could include reporting rates, training
completion rates and whether employee responses improve across repeated exercises.

I would also compare the platform's cost, functionality and security benefits with
alternative vendors before making a purchasing decision.

Given Oscorp's outdated awareness program, simulated phishing could be a useful
component of a broader security awareness programme. However, I would recommend
investing only if the pilot demonstrates measurable value and the platform meets
Oscorp's security, privacy and operational requirements.

---

## Additions on review

### 1. Name where this purchase came from

The answer evaluates the platform on its merits and says nothing about how the
question arrived. That's the part the scenario is built around: a CEO was pitched
over a free lunch, and is now considering a purchase because there is spare money.
Neither the vendor's pitch nor a budget surplus is a reason to buy a control.

Said diplomatically to Norman, the point is this: Oscorp has an open list of known
security findings, and the right way to decide where spare budget goes is to rank
that list by risk — not to fund whichever control was most recently sold to us.
Buying from a pitch is how organisations end up well defended against the threat
their last lunch was about.

This isn't an argument against the platform. It's an argument for putting it in a
queue with everything else and seeing where it lands.

### 2. Rank it against Oscorp's existing open findings

I answered as though Oscorp were a company with no history, and it isn't. From
earlier work:

| Open finding | Source | Nature |
| --- | --- | --- |
| Formula database uses SQL Server authentication — no MFA possible, outside directory governance | Mod 05 assessment | Crown-jewel asset, unmitigated |
| Entire research lab has read access to the formula | Mod 05 assessment | Crown-jewel asset, excessive access |
| Harry Osborn holds full database admin rights | Mod 05 assessment | Crown-jewel asset, no separation of duties |
| No current, complete asset inventory | KPMG audit finding, mod 04 | Audit finding requiring closure |
| No second line of defence | Mod 03 audit program design | Structural |
| Awareness programme untouched since 2013 | This assessment | The subject of this request |

Against that list, a simulated phishing platform is not the highest-value use of
spare budget. The formula is Oscorp's most sensitive asset, and the controls
protecting it are known to be weak *today*. Simulated phishing reduces the chance
of credentials being stolen; fixing the database authentication reduces what stolen
credentials are worth. The second is the better purchase, and it's cheaper.

The honest recommendation: fix the identity gaps on the formula database first,
close the KPMG asset finding, refresh the training — and then, if budget remains,
pilot the platform.

### 3. Push back on the pitch itself

The representative's framing — the human element is the weakest link — is a sales
device. It's not wrong, and it's not complete. People are also the first line of
defence and the only detection for a phish that beat every filter. More
importantly, a click is not the end of the story: the payload can still be caught
at the proxy, by anti-malware, or by someone watching for unusual behaviour.

Worth telling Norman explicitly, because the belief that one click ends everything
leads in two bad directions — overspending on the one control being sold, or
concluding that security is futile. Either way the decision stops following the
risk.

### 4. Two Oscorp-specific details

**The executive team must be in scope.** Senior people attract disproportionate
phishing because the payoff is larger. A simulation programme that quietly exempts
the executives — which is the usual outcome — measures the part of the
organisation least likely to be targeted. Norman being the person asking for this
is an opportunity to get that agreed at the start rather than argued about later.

**Research staff need content that matches their exposure.** A bioengineering firm
with a valuable formula is a target for industrial espionage, not only commodity
phishing. Simulation scenarios drawn from generic templates won't reflect the
approaches Oscorp's research staff would actually see — a conference invitation, a
collaboration request, a supplier query. The platform's value depends heavily on
whether scenarios can be tailored to that, which strengthens the customisation
requirement I already listed.

### 5. Evidence before purchase, not just a pilot

A pilot tests the platform. A **baseline simulation** tests whether there's a
problem worth buying a platform for. Most vendors will run one during evaluation,
and the result is a click rate and a report rate against a workforce that has had
one training module since 2013. If the numbers are poor, that's the business case,
written in Oscorp's own data. If they're fine, Norman has saved the money and
learned something.

That also gives a defensible before-and-after measure later — which the answer's
metrics need in order to mean anything.

### 6. The training fix is cheap and immediate

Worth separating clearly for Norman: refreshing a thirteen-year-old module costs
very little and can start now. The platform is a recurring licence with an
implementation project attached. Presenting them as one decision risks the cheap
fix waiting on the expensive one.

Also — an onboarding-only module means anyone who joined Oscorp in 2013 has had
exactly one hour of security training in their entire career there. Making it
annual and mandatory, including for contractors and lab collaborators, is the
single highest-return change available.

---

## Recommendation to Norman, in short

1. Refresh the training now and make it annual and mandatory, including
   contractors — low cost, immediate.
2. Run a baseline simulation during vendor evaluation to establish whether there's
   a measurable problem.
3. Direct the available budget first at the open findings on the formula database
   and the asset inventory, which protect the crown jewel and close an audit
   finding.
4. If budget remains after that, pilot the platform against defined success
   measures — report rate and time-to-report as the headline, click rate as
   supporting — and buy only if the pilot demonstrates value.
5. Whatever is bought, results are never used to name individuals.

## Comparing against the course solution

The solution runs in three steps. First, evaluate the current training module:
refresh and modernise it, and move it from onboarding-only to every 12 months.
Second, before purchasing anything, start publishing periodic articles on the
company intranet covering phishing, complex passwords, malware and similar topics.
Third — the logical next step — invest in a simulated phishing platform, evaluated
properly: request a demo from Norman's vendor, request a price quotation, then
conduct market research with demos and quotations from **at least three further
vendors**, compare, and present the findings to Norman.

### What the solution had that I didn't

**Intranet articles as the intermediate step.** This is the cheap-additions
material from lesson 4 used exactly where it fits: something that improves
awareness immediately, costs almost nothing, and buys time before a purchase
decision. My answer went from "refresh the training" straight to "evaluate the
platform" and skipped the rung between them. Worth remembering as a pattern —
when asked about an expensive control, look for the cheap thing that can start
tomorrow.

**A concrete procurement sequence.** I said compare cost and functionality against
alternatives. The solution specifies the process: demo, quotation, then the same
from at least three more vendors, then a comparison presented to the sponsor.
That's a more useful answer because it's actionable, and because naming a minimum
number of comparators is what stops "we looked at alternatives" meaning a glance at
one website. It also quietly protects against the conflict in the scenario — a
vendor who reached the CEO socially now has to win on a comparison.

### What I had that the solution didn't

**Ranking the spend against Oscorp's open findings.** The solution treats this as
a procurement exercise. Oscorp has unresolved findings on the formula database —
authentication that can't carry MFA, lab-wide read access, a Chief Scientist with
full admin — plus an open KPMG asset management finding. Spare budget directed at
those protects the crown jewel and closes an audit point; a phishing platform
doesn't.

**Pushing back on the vendor's framing**, and on a purchase originating at a lunch
rather than from the risk assessment.

**Baseline measurement before purchase**, no-blame handling, data protection and
vendor security review, and defined success measures for the pilot.

### The judgement call between them

The solution answers the question Norman asked. Mine answers the question behind
it. Both are defensible, and widening the scope uninvited carries its own risk —
a consultant who responds to "evaluate this platform" with "you're spending money
badly" can be heard as obstructive, particularly when the CEO is enthusiastic.

The version I'd actually deliver does both, in that order: answer the question
properly with the procurement process, then note that the same budget has
higher-value uses and let Norman decide. Answering first earns the right to widen
the frame.

## Note on the engagement

Declining to endorse a purchase the CEO has been enthusiastically pitched is the
uncomfortable part of this advice, and it's the part that makes it advice rather
than agreement. The recommendation isn't "no" — it's "not first, and not because
of the lunch."
