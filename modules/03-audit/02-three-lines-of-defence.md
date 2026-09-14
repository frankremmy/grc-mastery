# The three lines of defence model (3LOD)

> Module 03, lesson 2. How an organisation checks its own work, in three layers of
> increasing independence.

## Summary

Audit in practice is usually organised around the three lines of defence — a model
for splitting who owns a risk, who oversees it, and who independently assures it.

**First line** is the control owner. In the lesson's framing that's the security
team: the person who installs the firewall, configures it and keeps it running.
They can self-assess and self-report — tell management the firewall is configured
well, stopping attacks, covering the estate. In the broader corporate version of
the model, first line is business and operational management generally, owning and
managing the risks that arise in their own day-to-day work, implementing controls
and following policy.

The weakness is obvious once stated. Someone reporting on work they did
themselves is not a neutral witness. The usual failure is flattering — of course
it's working, I built it. The lesson also names the opposite: people who report
everything as broken regardless. Either way the report says as much about the
reporter as the control.

**Second line** is risk management and compliance — and in the wider model, legal
and quality assurance too. They sit in a different team under different
management, and their job is oversight and challenge of the first line. They ask
what controls are in place, and then ask for evidence: log extracts, design
diagrams, the results of a penetration test that would show whether the firewall
actually stops anything. They also build and maintain the risk frameworks and
policies the first line works within, advise the first line, monitor whether
controls are effective, and watch for emerging risks.

**Third line** is internal audit — the terms are interchangeable. It provides
independent assurance over both of the other lines, reporting findings to senior
management and the board. Its choices are interesting: it can re-verify something
second line already checked, or it can ask what second line *didn't* check. If
second line validated the firewall but never looked at the identity solution,
third line goes and audits identity. Coverage of the assurance itself is part of
what third line assures.

All three lines are internal. Even when consultants are brought in to help, work
done as first, second or third line is still the organisation auditing itself.

**External audit** is a separate thing, outside those three. An independent entity
from outside the organisation, often required by regulation — financial services
firms have to have one. The three lines can all be functioning and an external
auditor is still needed to confirm it independently. As a GRC professional you'll
encounter external auditors, but most time is spent within the three lines.

## The three lines at a glance

| | First line | Second line | Third line |
| --- | --- | --- | --- |
| Who | Control owners — the security team, operational and business management | Risk management, compliance, legal, quality assurance | Internal audit |
| Role | Own and manage the risk; implement and run controls | Oversight and challenge; set frameworks and policy; advise and monitor | Independent assurance over lines one and two |
| Typical activity | Configure the firewall; run the control; self-assess and report | Ask for evidence — logs, diagrams, test results; monitor effectiveness; track emerging risk | Audit the controls and the assurance itself; report to senior management and the board |
| Independence | None — reporting on own work | Separate team and management chain | Highest; reports beyond executive management |

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Control owner | The person or team that runs the control | Accountability starts here; so does the bias problem |
| Self-assessment | First line reporting on its own controls | Useful and cheap, but never sufficient on its own |
| Independence | Separation between the doer and the checker | The thing each successive line adds; it's what makes assurance worth anything |
| Evidence | Logs, diagrams, test results — not assertions | What second line asks for, and the difference between a review and a conversation |
| Assurance coverage | Which controls have actually been independently checked | Third line's distinctive question: what has nobody looked at? |
| Internal vs external audit | Inside the organisation, versus an outside entity | Consultants doing line-two work are still internal; external audit is a different category |
| Regulatory external audit | An outside audit mandated by rules, not chosen | Common in financial services; not a substitute for the three lines |

## Where this shows up in a real job

Helium Health is where I saw this in practice without the vocabulary. Preparing
evidence for the ISO 27001 certification audit was first-line work; the external
certification body was outside the three lines entirely. What I now realise is
that we had very little second line — the challenge function that asks for
evidence *before* the auditor does. That's the layer that makes certification
week calm rather than frantic.

The bias problem is familiar from support, in both directions. Asked whether a fix
worked, the person who wrote it is the worst-placed person to answer, and the
chronic pessimist on the team isn't much better. Neither is lying; both are
reporting a position as well as a fact. It's why someone else verifies.

I've never worked in a second- or third-line function, and I'd be careful not to
imply otherwise. What I have is a clear view of what first line looks like from
inside it, which is the line most GRC roles spend their time asking questions of.

## My take

The model's logic is that **independence increases as you climb**, and that's the
only thing each line really adds. First line knows the most and is trusted the
least. Third line knows the least detail and carries the most weight, because it
has the least stake in the answer. That trade — knowledge for objectivity — is the
whole design.

Three things worth holding:

**Independence is structural, not personal.** It isn't about being honest or
fair-minded; it's about reporting lines. Second line only functions as a challenge
if it sits under different management, and third line's standing comes from
reporting past executive management to the board or audit committee. A "second
line" reporting to the same person as the team it challenges is decorative.

**Second line has a built-in tension.** It both advises the first line and
challenges it — helps build the framework, then monitors compliance with it. That's
the same conflict as advisory versus assessment in consulting: the more helpful
second line has been in designing a control, the less independent its assessment
of that control can be. Worth watching for when a second-line function is very
proud of a process it also grades.

**The best third-line question is about gaps in assurance, not gaps in controls.**
Asking "what has nobody verified?" finds different things from asking "does this
control work?" — and it's a question only a line above the checkers can ask. It's
also a useful habit anywhere: the unexamined area is more dangerous than the
examined-and-imperfect one.

One piece of terminology to keep current: the model is widely known as the three
lines of defence, and the Institute of Internal Auditors updated it in 2020 to
simply the **Three Lines Model**, dropping the defensive framing and the rigid
numbering in favour of roles — governing body, management, internal audit. Most
organisations still say 3LOD. Knowing both names costs nothing and occasionally
signals that you've read past the course.
