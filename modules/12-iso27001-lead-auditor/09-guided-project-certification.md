# Guided project — achieving ISO 27001 certification

> Module 12, lesson 9. _The brief, and the decisions I want to get right before
> the clause work starts._

## The project

Build a complete ISO/IEC 27001:2022 ISMS from scratch for **Stark Industries** —
a small US software company with a SaaS marketing automation platform hosted on
AWS — and take it to certification. Prospective clients are demanding the
certificate as a condition of procurement, so the driver is commercial rather
than regulatory.

Full details in [`stark-industries-profile.md`](stark-industries-profile.md).

**Scope is given, not chosen:** strictly the newly developed SaaS application —
its development, deployment and management.

**On the difficulty.** Building an ISMS end to end is a senior task. A junior or
mid-level GRC analyst won't be handed one on their own. What's realistic is being
part of a team doing it, or a junior consultant helping organisations through it,
usually with someone senior supplying examples and review. The same framing as
the NIST capstone — worth doing, not worth claiming as routine.

The point of doing it once is that everything from lessons 1 to 8 stops being
abstract. And the spreadsheet stays available afterwards, which is how this works
in practice: references and standards on hand, nothing memorised.

## What I want to get right

**Scope is the decision everything else inherits.** Stark's scope is the SaaS
application, not the company. That's the commercially sensible choice — it's
faster and cheaper, and it satisfies the procurement requirement that triggered
the project. It's also exactly the pattern I read in the Monash certificate
earlier in this module: an institution certified for two platforms, not for
itself.

Which is a useful symmetry. I've just spent a lesson learning to read a narrow
scope sceptically from the outside; now I'm building one from the inside. The
honest position is that a narrow scope isn't a trick — it's how the standard is
meant to be used — but the certificate will say nothing about Stark's corporate
IT, its finance systems or its HR data, and a customer reading it should
understand that. Getting the scope statement precise is what makes the difference
between a legitimately narrow certification and a misleading one.

**The "no PII" claim needs testing before it drives exclusions.** The brief says
the application doesn't store personally identifiable information — it collects
marketing data and provides insights. I'd want to confirm what that means,
because marketing automation for small businesses normally runs on contact lists,
email addresses and behavioural data belonging to the *clients'* customers. "No
PII" most likely means none about Stark's own users, not that no personal data
passes through the platform.

That distinction matters. If the platform processes personal data on behalf of
clients, Stark is a processor, several Annex A controls become clearly
applicable, and if any client operates in the EU, GDPR can reach Stark through
them. Building exclusion justifications on an untested "no PII" statement is the
kind of thing that surfaces at the certification audit rather than before it.

**AWS is an interested party, and the shared responsibility boundary drives
exclusions.** Several Annex A controls will be satisfied by AWS rather than by
Stark, and several will remain Stark's regardless of what AWS does. That boundary
needs writing down — it's the difference between a defensible exclusion and one
that reads as an assumption. A.5.23, information security for use of cloud
services, is new in the 2022 revision and lands squarely here.

**Two structural problems a six-person company will hit.** Segregation of duties
(A.5.3) is genuinely hard when one developer, one infrastructure engineer and two
security people cover everything — that's a constraint to document and
compensate for, not a control to claim. And clause 9.2 requires internal audits
by someone who can be objective. If I build the ISMS, I cannot audit it. For an
organisation this size the realistic answers are an external party or someone
internal with no stake in the ISMS, and it's better settled at the start than
discovered in month eleven.

That second one is the module 3 independence argument and the capstone's
reporting-line finding arriving in a third form. It keeps showing up because it
keeps being the thing small organisations get wrong.

## Where this fits in the repo

Stark Industries gets its own profile file rather than joining the Oscorp thread —
different organisation, different sector, different jurisdiction, and the two
shouldn't blend.

The deliverables from this project will be documents I write: the scope
statement, the policy, the risk assessment and treatment plan, and the SoA. None
of them reproduce ISO's text, so they belong in `deliverables/` in the usual way.
