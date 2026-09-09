# Cyber security GRC examples

> Module 01, lesson 2. Worked examples that separate governance from risk
> management, and the third part of compliance nobody budgets for.

## Summary

Lesson 1 defines the three disciplines; this one works through examples of each,
which is where telling governance and risk management apart gets hard — they
happen in the same room, often in the same meeting. The discriminator I'm keeping is
**setup vs operate**. Creating the risk committee is governance. What the
committee decides is risk management. Hiring a CISO is governance; the CISO's
treatment calls — accept, mitigate, transfer, avoid — are risk management. The
structure and the mandate are governance; the judgements made inside that
structure are risk management.

This test survives cases the house analogy mangles, because it asks about the
*activity* rather than the artefact. It also fails cleanly, which is a virtue:
when you genuinely can't tell whether something is setup or operation, that's
usually a real signal that the mandate is unclear, not that the test is bad.

Compliance also gets unpacked further than I expected. It's three parts:
adhering to the standard, closing the gaps an audit finds, and maintaining
current, readable documentation. The third is where the effort actually goes and
it's the one that gets forgotten at planning time.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Setup vs operate | Governance builds the structure and mandate; risk management is the decisions made inside it | The cleanest test for sorting an activity into the right discipline |
| Risk treatment decisions | Accept, mitigate, transfer, avoid — the choices a risk owner makes about a specific risk | These are risk management even when a governance body rubber-stamps them |
| The three parts of compliance | Adhere to the standard; close audit gaps; maintain current readable documentation | The documentation part is most of the ongoing cost and is almost never resourced |
| Documentation currency | Policies and evidence that describe what the org does *now*, not at last audit | Stale documentation is the most common audit finding and the cheapest to prevent |

## Where this shows up in a real job

The documentation point is the one I recognise. In the Helium Health ISO 27001
run, writing the policies was a defined piece of work with an end date; keeping
them true afterwards was nobody's named job. That's the gap this lesson is
pointing at, and it's the part I'd resource differently if I ran it again.

The setup-vs-operate test is also a useful lens on support escalation paths. An
escalation policy is governance. Deciding that *this* ticket is a security
incident is not — that's an operational risk judgement, and it's usually made by
whoever picked up the ticket, whether or not governance intended that.

## Gotchas / what most orgs get wrong

- **The course's own examples disprove its house analogy.** Its governance
  examples are a security policy, appointing a CISO, standing up a risk
  committee — all setup. Its risk management examples are identify, assess,
  mitigate, monitor — all operation. That's the setup-vs-operate split, drawn
  cleanly, in the same material that elsewhere files an alarm under governance and
  locks under risk management. The examples are right and the analogy is wrong;
  worth noticing which one to keep.
- **The test is about the activity, not the artefact.** A risk register is not
  "governance" because a committee owns it. Writing the mandate that says a
  register must exist is governance; the entries in it are risk management.
- **Documentation currency is treated as an admin chore.** It's the compliance
  work with the highest recurring cost and the lowest status, so it's the first
  thing dropped. An org that can't produce a current, readable policy set on
  demand doesn't have a compliance function, it has a certificate.
- **"Closing audit gaps" quietly assumes the audit found them.** The three-part
  model describes compliance as reactive to audit findings. That's honest about
  how most orgs behave, but it means an unaudited control can be broken for
  years and the compliance function is working as designed. Worth naming rather
  than treating audit coverage as complete by default.
