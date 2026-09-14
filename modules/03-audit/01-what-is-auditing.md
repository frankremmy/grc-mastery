# What is auditing?

> Module 03, lesson 1. Checking that the controls an organisation paid for are
> actually doing the job.

## Summary

Audit, at its simplest, is reviewing an organisation's cyber security posture:
the risks it carries, the threats it faces, the controls it has in place, and —
the part that does the work — how effective those controls actually are at
reducing likelihood and impact.

The lesson makes this concrete with anti-malware, and the value is in how many
distinct questions come out of one control. An organisation says it has
anti-malware. The auditor's job is to verify and validate that claim, which turns
out to mean:

- Is the solution up to date?
- How well does it handle new and emerging malware, not just known samples?
- Is it deployed on **everything** — laptops, desktops, MacBooks, servers, cloud
  instances — or only the estate somebody remembered?
- How often does it run a full scan?
- When it detects something on a server at three in the morning on a weekend, does
  it raise an alert, where does that alert go, who picks it up, and what happens
  next?

Each of those is a separate way the control can be real on paper and useless in
practice. Having the solution is one thing. Having it deployed everywhere is
another. Keeping it current is another again. And an alert nobody acts on is not
a detection.

The purpose behind all of it is assurance: giving senior management confidence
that the money spent on controls bought working controls, and that cyber risk is
being managed. For a GRC professional, audit is both something you work alongside
and a role you can move into.

## The layers in one control

The anti-malware example is really a ladder, and a control can fail at any rung
while looking fine from the one below:

| Layer | The question | How it fails |
| --- | --- | --- |
| Existence | Is there a control at all? | Nothing in place; rare, and the easiest to spot |
| Design | Would this control stop the thing it's aimed at, if it worked perfectly? | Right category of tool, wrong fit for the threat |
| Coverage | Is it on every asset in scope? | Deployed on the corporate laptop fleet; not on servers, Macs, or cloud instances |
| Currency | Is it kept up to date? | Signatures or agent versions drifting behind |
| Operation | Is it actually running, and running often enough? | Installed but disabled, or scanning quarterly |
| Response | Does anything happen when it fires? | An alert at 03:00 on a Saturday that lands in an unmonitored mailbox |

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Audit | Independent review of controls and how well they work | The mechanism that turns a claim about security into evidence |
| Assurance | Confidence, for people who can't verify it themselves, that controls work | The output senior management is actually buying |
| Verify and validate | Confirm the control exists, and confirm it does its job | Two separate checks; passing the first says little about the second |
| Design effectiveness | Whether the control, working as intended, would address the risk | A well-run control aimed at the wrong thing is still a gap |
| Operating effectiveness | Whether it works that way in practice, over time, across the estate | Where most real findings come from |
| Coverage | The proportion of in-scope assets the control actually reaches | The quiet failure — nobody lies about it, they just forget the servers |
| Alert handling | What happens between detection and someone acting | The end of the chain, and the part with a human in it |

## Where this shows up in a real job

The three-in-the-morning question is the one I recognise most. In support, the gap
between "the system detected it" and "somebody did something about it" is where
things actually go wrong — an alert with no owner, a notification into a channel
nobody watches, a monitor that fires into a mailbox that was decommissioned. The
technical half usually works. The handoff is what breaks.

My Wazuh lab makes the same point from the builder's side. Getting detections to
fire is the satisfying part and it's maybe a third of the problem; deciding where
an alert goes, who is responsible at 3am, and what they're supposed to do with it
is the rest, and that half doesn't exist in a home lab because there's nobody to
hand off to.

The coverage question maps onto something I see constantly in WordPress work: a
security plugin installed and left on defaults, or backups configured years ago
and never restored from. The control is present in every meaningful sense except
the one that matters.

At Helium Health I was on the other side of this — assembling evidence for the
ISO 27001 auditor rather than asking the questions. Knowing what an auditor is
actually trying to establish would have made that job considerably easier.

## My take

The single most useful idea here is that **existence is not effectiveness**, and
that there are about five distinct rungs between them. Most control claims are
true at the bottom of the ladder and unverified further up, and an audit is
mostly the work of climbing it.

Two things I want to carry:

**The alert question tests the whole chain at once.** "What happened the last time
this fired at 3am on a weekend?" reaches the tool, the configuration, the routing,
the rota and the person — in one question, with a specific answer that can be
checked against a ticket. That's a much better question than "do you have alerting
configured?", which can be answered yes by a system that has never usefully
alerted anyone.

**Evidence beats assertion, and the type of evidence matters.** Asking someone
whether a control works is the weakest form of checking; being shown a
configuration is better; seeing a report covering the whole estate is better
again; and best of all is watching the control do the thing, or re-performing the
test yourself. "They told me it was fine" is not an audit finding.

Audit and risk assessment answer different questions and need each other. The risk
assessment says what matters and what should be protected. The audit says whether
the protection that was bought is real. Do one without the other and you either
secure the wrong things well, or the right things on trust.
