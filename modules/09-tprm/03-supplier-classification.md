# Supplier classification

> Module 09, lesson 3. _Sorting the supplier list by how much damage each one
> could do._

## Summary

The discovery process produces a list. The list on its own doesn't tell you
anything — a cleaning contractor and the vendor running your payroll are both
just rows. Classification is the step that turns it into something you can act
on, by sorting suppliers into tiers based on the criticality and sensitivity of
what they provide or hold. It's the same move as asset classification in module 4
and data classification in module 7: you can't treat everything as critical, so
you decide what critical means and apply it consistently.

**Tier one** is anything meeting any one of three conditions — direct access to
our environment, holding sensitive information belonging to us, or providing a
service the business can't operate without. Any single one of those qualifies; a
supplier doesn't need all three. The course's example is an online airline
ticketing business and the vendor supplying its booking software: if that
software is down, the company isn't trading. That's tier one on the service
criticality test alone, before you ask what data it holds.

**Tier two** is suppliers who handle data that matters but isn't sensitive, and
whose service the business can survive losing for a while. We still don't want
them breached — this is a lower priority, not an acceptable one. **Tier three**
is everyone else: no access, no data, no critical dependency.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Supplier tiering | Sorting suppliers by criticality and sensitivity | Assessment effort is finite; tiering is how it gets allocated |
| Tier 1 | Direct access to our environment, **or** holds our sensitive data, **or** provides a service we can't operate without | Any one condition qualifies — it's an OR, not a checklist to satisfy fully |
| Tier 2 | Handles non-sensitive data; service loss is survivable | Lower priority, not no priority |
| Tier 3 | No access, no data, no critical dependency | The bulk of the list by count, the minority of the risk |
| Access as a criterion | Connectivity or credentials into our environment | Their breach becomes our intrusion — the lesson 1 point |
| Sensitivity as a criterion | What the supplier holds about us or our people | Employee PII puts a supplier in tier 1 on its own |
| Criticality as a criterion | Whether the business runs without the service | An availability question, independent of data |
| Consistency with asset and data classification | Same logic already applied to assets and data | The schemes should agree — a tier 3 supplier handling your most sensitive data class is a contradiction worth chasing |

## Where this shows up in a real job

The three criteria map onto the CIA triad cleanly enough to be a useful memory
hook: access is a confidentiality and integrity question, sensitive data is
confidentiality, and critical service is availability. Doing the CIA triad
assessment in module 2 is what makes this feel obvious rather than arbitrary —
it's the same question asked about a company instead of an asset.

The support angle that stays with me is scope creep. A supplier gets onboarded
for something small and harmless, then eighteen months later somebody needs an
integration and grants them API access to make a workflow happen. The access
request gets approved on its own merits. Nobody goes back to the supplier record
and asks whether the tier still holds, because re-tiering isn't part of anyone's
job and the original classification was made by someone who has since moved on.
The record says tier 3 and the reality is tier 1.

## My take

Tiering is only worth doing if something actually differs between the tiers. The
lesson defines the boxes carefully but doesn't say what changes once a supplier
is in one, and that's the part that makes it real: depth of assessment, what
evidence you'll accept, how often you reassess, which contract clauses are
non-negotiable, whether they get an exit plan. If a tier 1 and a tier 3 supplier
receive the same questionnaire on the same schedule, the classification was a
labelling exercise. I'd want the treatment defined at the same time as the tiers,
not afterwards.

The second thing is where the tier gets assigned. Classifying thousands of
existing suppliers retroactively is a project that never finishes. It has to be
part of onboarding — a few questions the business owner answers when the supplier
is brought in, before contracts are signed, because that's the only moment you
have leverage anyway. Then the backlog gets worked through by priority rather
than alphabetically.

And I'd want a trigger for reclassification, because the scope creep case above
is the realistic failure. Tier is assigned once, at the point of least
information, and then never revisited while the relationship deepens around it.
An annual refresh catches it eventually; a check at the point new access is
granted catches it at the right time.
