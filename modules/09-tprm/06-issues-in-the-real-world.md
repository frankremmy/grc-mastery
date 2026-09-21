# Issues with TPRM in the real world

> Module 09, lesson 6. _Where supplier risk programmes break, and what to do
> when someone tells you the whole thing is unnecessary._

## Summary

Even mature organisations with a working TPRM process turn out, on inspection, to
have large gaps in it. Most small and medium businesses have no process at all.
The lesson starts with a proportionality point that I think matters: for a very
small organisation dealing with one or two long-standing suppliers, a full TPRM
programme is overkill. A conversation with that supplier may be genuinely
sufficient. The problem sits with medium and large organisations, where the
supplier count is high enough that informality stops working and nobody has
replaced it with anything.

The failure modes are fairly consistent. **Scanning tools sold as assessment** —
products that run an external scan against the supplier's website and produce a
report. An inexperienced IT or security manager can mistake that for an
assessment. It isn't: nothing observable from outside tells you how a company
manages security internally, which is the actual question from lesson 1.
**Findings that go nowhere** — the assessment happens, the report identifies that
a supplier isn't encrypting sensitive data, and six months later nothing has
changed. Security teams are overworked and pulled towards incidents and tickets,
suppliers are slow and can simply not respond, and the finding quietly ages.
**No supplier inventory**, which is lesson 2's problem persisting because
discovery was treated as a one-off. And organisations that dispute the premise
altogether and don't see why supplier security is their concern.

The remedies the lesson gives are practical. For findings: fix a date at the
point the risk is raised, with an explicit follow-up process — a finding without
a deadline and an owner is a record, not a remediation. For inventory: integrate
with procurement so that a new supplier purchase or a contract renewal
automatically raises a work order or ticket for the security team to assess. That
turns discovery into something continuous rather than an annual archaeology
project. For scale: get a firm handle on the critical suppliers first with a
defined assessment schedule, then extend to the rest on a realistic timeline —
and if a team says it will cover tier 2 and tier 3 in six months, the honest
advice is that 12 to 18 months is more likely.

For the organisation that doesn't accept the premise, there are two arguments.
The breach argument: a large share of significant attacks arrive through a
supplier. And the compliance argument: privacy law makes the organisation
responsible for personal data it has handed to a processor, so assessing that
processor's controls is not discretionary.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Proportionality | A full TPRM programme is overkill for a very small organisation | Right-sizing is a legitimate answer, not a cop-out |
| Scan-based "assessment" | Tools that scan a supplier's external surface and issue a report | Measures externally visible hygiene, not internal control maturity |
| Findings neglect | Identified supplier risks that are never chased | The most common failure in programmes that otherwise work |
| Dates and follow-up | Every finding gets a remediation deadline and a named follow-up | Converts a report into an action |
| Procurement integration | New purchase or contract renewal auto-raises an assessment ticket | Makes discovery continuous; catches suppliers at the point of leverage |
| Contract renewal as a trigger | Renewals, not just new purchases, prompt reassessment | Catches relationships that have quietly changed scope |
| Critical-first sequencing | Lock down tier 1 coverage before extending downward | The only realistic approach at thousands of suppliers |
| Realistic timelines | Assessment programmes take longer than teams estimate | Six-month plans for tier 2 and 3 usually mean 12–18 |
| Breach argument | Many major incidents arrive through a third party | The persuasion lever when risk framing fails |
| Compliance argument | Privacy law holds the organisation responsible for data given to suppliers | Turns a discretionary activity into an obligation |

## Where this shows up in a real job

The findings-neglect problem is the one I recognise most directly. In support,
the equivalent is the ticket escalated to a team with no capacity for it: the
escalation was correct, the handoff happened, and then it sits. Nobody decided to
ignore it. It just never became anyone's priority ahead of the thing in front of
them. What fixed it was never goodwill or better intentions — it was the work
being visible somewhere with a date attached, in a queue someone reviewed. The
same applies here, and it's why "we'll follow up with the supplier" without a
date and an owner is a sentence that predicts nothing will happen.

The proportionality point also matters for how I'd talk to a smaller Maltese
business. Telling a twelve-person company it needs a tiered questionnaire
programme is the fastest way to have security advice ignored entirely. The useful
version is: know who holds your data, get the contract terms right, and have the
conversation. That's proportionate, and it's more likely to actually happen.

## My take

I'd be more precise than the lesson about scanning tools. Sold as a replacement
for assessment, they are exactly as useless as described — externally observable
hygiene tells you almost nothing about how a company runs security internally,
and a manager who accepts that report as an assessment has bought false
assurance. But they do have one honest use, which is the gap this module never
closes: a questionnaire is a point-in-time self-report, and between annual
assessments you have no visibility at all. Continuous external monitoring is weak
evidence, but it's weak evidence arriving continuously, which makes it usable as
a tripwire rather than as an assessment. The distinction I'd want to be able to
defend is *replacement, no; supplementary signal between assessments, reasonable.*

The related gap is that nothing in this module covers what happens between
assessments. The things that actually close it are contractual rather than
technical: a clause requiring the supplier to notify you of their own breaches, a
clause requiring notice before they change subprocessors, and defined events that
force a reassessment regardless of schedule — a breach, an acquisition, a
material change in the service. Without those, a supplier can be compromised,
change ownership and re-architect their platform, and your file still says they
passed.

On findings, I'd go one step past dates. The reason supplier findings rot is that
they typically live in a separate document with no governance forum attached.
Internal risks go into the risk register and get reviewed; supplier risks go into
a supplier report and get filed. Putting third-party findings into the **same**
risk register, with the same owner-and-review discipline, is what stops them
existing in a parallel universe where nobody has to look at them.

And on the compliance argument, the EU version is considerably stronger than
"privacy laws". GDPR requires a controller to use only processors offering
sufficient guarantees and prescribes what the processor contract must contain;
NIS2 names supply chain security as a required measure for in-scope entities. For
an organisation arguing that supplier assessment is optional, that is a shorter
conversation than the breach statistics.
