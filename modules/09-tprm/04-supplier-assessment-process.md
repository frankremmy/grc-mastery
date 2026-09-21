# The supplier assessment process

> Module 09, lesson 4. _What actually happens between having a classified
> supplier list and having a decision._

## Summary

With the list built and the suppliers tiered, the assessment itself is a
reasonably plain sequence. A set of cyber security questions goes out to the
supplier. The supplier answers them and supplies evidence. A GRC analyst reviews
the answers, inspects the evidence, and decides whether what came back is
satisfactory. Where the answers are incomplete, or the evidence doesn't support
the claim, the analyst can request a call with the supplier's security team to
get clarification rather than guessing.

The output is a report. It describes the supplier and what they do, what data
they handle, which controls were assessed, and the conclusion. Where findings
exist, they're stated as findings, with recommendations for fixing them. Then —
and this is the part I think carries the most weight — the report goes to a
**senior manager and the business owner** of the application or service the
supplier supports. Both of them, not one. They read what the risks are, and they
decide, together with the security team, whether to accept the risk or to
remediate it.

That last step is the whole shape of GRC again. The analyst produces findings and
recommendations; the analyst does not decide. The business owner owns the service
and the senior manager carries the authority, so the risk is theirs to accept or
reject. It's the same structure as the audit reporting line in module 3 and the
risk treatment decision in module 2: assessment is advisory, acceptance is
accountable, and the two are deliberately held by different people.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Questionnaire | The set of security questions sent to the supplier | The mechanism, but only as good as the verification behind it |
| Evidence | Artefacts backing the supplier's answers | An unevidenced answer is a claim, not a control |
| Validation | The analyst inspecting evidence and judging whether answers hold | The step that distinguishes an assessment from a survey |
| Clarification meeting | A call with the supplier's security team where answers are incomplete | Faster and more honest than a second round of email |
| Assessment report | Supplier description, data handled, controls assessed, conclusion, findings, recommendations | The deliverable — written for a manager, not for the security team |
| Findings and recommendations | What's wrong, and what would fix it | Recommendations without owners and dates don't get actioned |
| Business owner review | The owner of the application or service reviews the report | They carry the operational consequence of the decision |
| Senior management review | A senior manager reviews alongside the business owner | Risk acceptance needs someone with the authority to accept it |
| Accept or remediate | The decision the business takes after reading the report | The analyst informs it; the analyst doesn't make it |

## Where this shows up in a real job

This is the job I'd most plausibly be hired into first, and the shape of it is
familiar from support in a way I didn't expect. Reviewing questionnaire responses
against evidence is the same cognitive move as reading a customer's description
of a problem against what the logs actually show. People describe their systems
as they believe them to be, usually sincerely, and frequently wrongly. The skill
is holding the stated version and the evidenced version side by side without
treating the gap as dishonesty — because most of the time it isn't.

The clarification call is the part I'd expect to be good at and the part I'd have
to be careful with. Support work trains you to ask questions without putting the
other person on the defensive, which matters here: the supplier's security team
is being examined by a customer, and a call that feels like an interrogation
produces less information, not more. But the same instinct — being accommodating,
accepting a plausible explanation to keep things moving — is the failure mode
when the job is verification. I'd rather notice that now than discover it in a
report I signed.

## My take

The thing I want to fix in my head is *when* this happens. The lesson describes
the mechanics without naming the trigger, and it matters enormously: the
assessment belongs **before the contract is signed**. That's the only point where
the organisation has leverage. Afterwards you can write a finding, recommend a
fix, and have no means of compelling anything — the supplier is embedded, the
business depends on them, and "we found a gap" competes against the cost of
unpicking the relationship. Everything the process can achieve depends on
happening early enough to still be able to walk away.

The second thing is that "remediate" means something different here than
everywhere else in this course. In every other module, remediation is work we do.
With a third party, we have no authority to fix anything. The real options are a
contractual remediation plan with dates attached, a compensating control we
implement on our own side to reduce the exposure, formal risk acceptance, or not
proceeding. A report that says "supplier should implement MFA" without saying
which of those four is happening hasn't closed anything.

And I'd want the evidence standard defined by tier, otherwise the process drifts
towards whatever the supplier finds convenient to send. A completed questionnaire
is self-attestation — it's the supplier telling you what they believe about
themselves. Independent assurance is a different category of thing, and for a
tier 1 supplier it's the one worth insisting on.
