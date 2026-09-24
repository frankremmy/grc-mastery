# Recover — solution walkthrough

> Capstone, lesson 6. _All six pass, and the one place I'd hold my ground._

## Summary

All six Recover controls pass. The reasoning: a competent IT team combined with a
SaaS and cloud environment usually produces good business continuity and disaster
recovery, because the platform makes it straightforward. Spinning up a new cloud
environment or running a highly available SaaS instance is comparatively easy
work, so organisations of Oscorp's shape tend to land here even without a
security function. Oscorp has documented business continuity plans and conducts
regular disaster recovery testing, so recovery planning, improvements and
communications all pass.

## Where my assessment diverged

This was my largest single divergence: **I scored 2 passes, the solution scored
6.** I failed four controls — lessons learned in recovery plans, public relations
managed, reputation repaired, and communication of recovery activities to
stakeholders — on the basis that the notes evidence none of them.

**On two of those I was wrong.** Recovery plans incorporating lessons learned and
recovery strategies being updated are reasonable inferences from documented plans
that are regularly tested. Testing without feeding the results back is unusual,
and my rule that silence fails was applied too mechanically to a control area the
notes describe as mature. The solution's reading is better.

**On the three Communications controls I would keep a Fail**, or at minimum
record them as not evidenced. This is the one place in the whole capstone where I
think the solution stretches, and the reason is structural rather than a matter of
generosity:

- Nothing in the current-state document mentions crisis communications, public
  relations, or a spokesperson. The inference has nothing to attach to
- Oscorp has **no cyber incident response plan at all** — the solution itself
  fails PR.IP-9 and PR.IP-10 on exactly that basis
- A disaster recovery plan and a crisis communications capability are different
  things. A DR plan covers restoring service after an outage. It does not
  typically contain holding statements, a designated spokesperson, regulatory
  notification wording, or a plan for telling research partners that their data
  was exposed

The gap matters for this client specifically. Oscorp is a pharmaceutical research
business with a marketed medicine that has already drawn press attention. The
reputational consequences of a research data breach are a material part of its
loss exposure — that was the largest component of the secondary loss figure in my
module 11 quantification. Passing "reputation after an event is repaired" for an
organisation with no cyber incident response plan and no communications function
records a capability Oscorp does not have.

I'd put it this way in a report: **Oscorp can restore a service. It cannot manage
a crisis.** Those are both recovery activities and only one of them is evidenced.

## My take

The substantive lesson stands and I've taken it: where an area is demonstrably
mature, inferring the surrounding process is reasonable, and my blanket "silence
fails" rule cost me information rather than adding rigour. Four of my twelve
divergences were in this one function, and two of them were straightforwardly my
error.

But the correction has a limit, and Recover is where I'd draw it. Inference is
legitimate when it extends an evidenced capability into its natural neighbours —
tested DR plans imply a feedback loop. It becomes unsafe when it crosses into a
different capability entirely, especially one the same assessment has already
found absent elsewhere. The three Communications controls are downstream of
incident response, not of disaster recovery, and the assessment failed incident
response comprehensively.

The wider observation the walkthrough makes is the useful one and it closes the
picture on Oscorp: strong continuity, strong physical security, nothing on
detection or response. That isn't a strategy, it's a by-product. The cloud
supplied the resilience and the leased facility supplied the physical controls,
and no one at Oscorp has made a deliberate security decision. Recognising which
strengths were *chosen* and which were *inherited* matters, because inherited
strengths tell you nothing about the organisation's capability to maintain them —
and a roadmap that assumes competence where there was only a fortunate default
will overestimate how much the client can absorb.
