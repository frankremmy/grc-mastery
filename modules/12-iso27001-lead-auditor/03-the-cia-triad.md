# The CIA triad

> Module 12, lesson 3. _Covered in module 2 — this note records what's specific
> to ISO 27001 rather than repeating it._

## Summary

The CIA triad describes the three objectives every security control and decision
should serve.

**Confidentiality** — only authorised individuals can access information. Breached
by a publicly accessible storage bucket holding financial records, an employee
sharing credentials outside the organisation, or a phishing attack that extracts
access.

**Integrity** — information is accurate, unaltered and reliable. Breached by an
attacker altering transaction logs, a software bug corrupting pricing data, or an
undetected change to audit records. The consequence is decisions made on
incorrect data.

**Availability** — authorised users can reach information and systems when they
need them. Breached by a DDoS attack, a server failure with no failover, or
ransomware locking the organisation out of its own data. Perfect data nobody can
reach on time is useless.

**The ISO connection:** the triad is what the ISMS exists to protect and
preserve. Everything in ISO 27001 — the scope, the risk assessment, the control
selection — serves these three properties.

## Already covered

I wrote this up in [module 2, lesson 6](../02-risk-management/06-cia-triad.md),
and applied it in the
[Oscorp CIA triad assessment](../../deliverables/02-cia-triad-assessment.md). The
substance hasn't changed. What follows is only what's new in an ISO context.

## What's specific to ISO

**The formal definitions are in ISO/IEC 27000.** In an ISO setting you're
expected to use the standard's own wording rather than a general description —
confidentiality as information not being made available or disclosed to
unauthorised individuals, entities or processes; integrity as the property of
accuracy and completeness; availability as being accessible and usable on demand
by an authorised entity. Worth knowing they're defined terms, not shorthand.

**Clause 6.1.2 makes the triad the risk identification method.** The standard
requires risks to be identified in terms of the **loss of confidentiality,
integrity and availability** of information within the ISMS scope. So the triad
isn't a teaching model that sits alongside the risk process — it *is* the
structure the risk process uses. "What could cause loss of C, I or A to this
asset" is the question the standard asks you to answer.

**The 2022 Annex A tags every control with the properties it supports.** The
revision introduced control attributes, and one of them is information security
properties — each of the 93 controls is labelled with which of confidentiality,
integrity and availability it serves. That makes the triad operational rather
than decorative: you can filter Annex A by property and see which controls
address an availability risk versus a confidentiality one.

**ISO also defines authenticity and non-repudiation** as related properties.
They're not part of the triad but they appear in the standard's vocabulary, so
the triad isn't presented as the complete set of security properties — just the
three the ISMS is organised around.

## My take

The thing worth carrying from this lesson is that ISO gives the triad a job. In
most contexts it's an explanatory device — a way of teaching that security isn't
only about secrecy. In ISO 27001 it's the actual mechanism: clause 6.1.2 asks you
to identify risks as losses of C, I or A, and the Annex A attributes let you trace
from a property back to the controls that support it.

That matters for my Oscorp work. The module 2 assessment identified research IP
as the crown jewel and reasoned that confidentiality dominated — with a note that
integrity of research data mattered more than the CEO's framing suggested. The
module 8 incident response plan later made integrity of data supporting a marketed
medicine an escalation trigger in its own right, on patient safety grounds. If
Oscorp ran an ISO risk assessment, that integrity concern would surface as a
distinct risk with distinct controls, rather than being folded into a general
worry about the research data being stolen. Separating the three properties
changes which controls you end up selecting, which is the whole point of doing it
formally.
