# The supplier assessment questionnaire

> Module 09, lesson 5. _Designing the instrument the whole process runs on._

## Summary

The questionnaire is where the assessment actually happens, and the lesson is
mostly about restraint. The questions come from frameworks rather than from
whatever the analyst happens to think of — same principle as every other
assessment in this course — and the framework choice should reflect the
organisation's sector and jurisdiction. Healthcare in the US points at HIPAA; in
Australia, where there's no healthcare-specific framework, you reach for
something covering personal information like the Privacy Act; in Europe that's
GDPR. But you're not confined to one. NIST is comprehensive enough to be a sound
starting point, and you add controls from whatever else is relevant to your
industry and country.

The restraint part is length. The course has seen questionnaires running past 900
questions, and the point is that this defeats itself: suppliers ignore it, or
take months, or fill it in carelessly, and you end up with a large quantity of
worthless answers. The fix is to stop treating each control as its own question.
One well-framed question can cover a group of controls — "is the data encrypted,
and if so provide details" does the work of five separate encryption questions
and produces a better answer than any of them would.

Two structural requirements. **Evidence has to be built into the questionnaire**,
as a field next to each question, not chased afterwards. You don't accept yes or
no — a claim about password policy comes with the policy document or a screenshot
of it. And **the questionnaire differs by tier**. Tier 1 gets the comprehensive
version asking for real depth; tier 2 and tier 3 get progressively less, because
the detail genuinely matters less there. That's what makes the classification in
lesson 3 do any work.

On tooling, the lesson is refreshingly blunt: a spreadsheet is fine. Large
organisations run entire supplier assessment teams on spreadsheets successfully.
GRC software is worth buying once the process is working and you want the time
back, but the tool is not the thing that makes the process good.

Evidence depth varies in practice with the supplier's maturity and the
sensitivity of the system. Some suppliers refuse to hand over evidence at all. A
workable answer is a screen-share where they walk you through it live, even if
you can't take copies — and that constraint gets documented in the report rather
than glossed over.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Framework-derived questions | Questions mapped to recognised control frameworks, not invented | Defensible, comparable, and mappable back to a control when reporting |
| Sector and jurisdiction fit | HIPAA (US healthcare), Privacy Act (AU), GDPR (EU) | The obligations you inherit depend on where you and your data are |
| Multi-framework | Draw from several standards rather than one | No single framework covers every sector and country obligation |
| NIST as a base | Comprehensive, broad coverage, good starting point | Start there, supplement for industry and country |
| Control grouping | One question covering several related controls | The difference between a questionnaire that gets completed and one that doesn't |
| Questionnaire length | Keep it proportionate — 900 questions is self-defeating | Long questionnaires produce non-responses and careless answers |
| Built-in evidence field | A column for evidence beside every question | Stops the second round of chasing; makes "yes" cost something |
| Never accept yes/no alone | Every claim needs supporting artefact | An unevidenced answer is an assertion |
| Tiered questionnaires | Separate versions for tier 1, 2 and 3 | This is what makes classification operational rather than decorative |
| Tooling | Spreadsheet first; GRC platform later | Process quality is independent of tool sophistication |
| Evidence refusal | Supplier won't share artefacts — use a walkthrough session | Acceptable, but the limitation belongs in the report |

## Where this shows up in a real job

GDPR is the relevant frame for me, working in Malta. That makes this less
abstract than the course's framing suggests: under GDPR a controller is required
to use only processors providing sufficient guarantees, and there are prescribed
terms that have to exist in the processor contract. So in the EU the supplier
assessment isn't only a good idea — a chunk of it is a legal obligation with a
defined minimum, and the questionnaire is one of the ways you demonstrate you met
it. Worth knowing which questions exist because they're good practice and which
exist because a regulator will ask.

The "don't go crazy" advice also lands from the other side of the desk. At
Automattic, requests arriving from enterprise customers' security teams were a
real workload, and a bloated questionnaire got the treatment bloated
questionnaires deserve — slow, delegated, answered at the minimum. The people
filling these in are not the people who wrote them, they're usually busy, and
they're being asked to do unpaid work for someone else's assurance programme.
Designing for that reality isn't softness, it's the difference between getting
usable answers and getting a completed file.

## My take

The tiered questionnaire is the piece that makes the last three lessons hang
together. Discovery gives you the list, classification sorts it, and this is
where the sorting cashes out — different instruments, different depth, different
evidence expectations. Without this step the tiering was a colour-coding
exercise.

What I'd add for myself is that grouped questions need a defined answer
structure, or the economy gains something and loses something else. "Is data
encrypted, provide details" produces free text, and free text can't be compared
across forty suppliers or trended over time. I'd want each grouped question to
have a constrained part — yes/no/partial, plus the specific sub-points that must
be addressed — so the answers stay analysable while the question count stays
sane. Otherwise you've traded a 900-row spreadsheet nobody completes for a
40-row one nobody can summarise.

The evidence refusal case deserves more weight than a note in the report. If a
tier 1 supplier won't evidence its controls, that is itself a finding, and the
report should say plainly which claims could not be independently verified —
that's the assurance-limitation discipline from the audit module applied here.
The honest sentence is "the supplier asserts X; we were not able to verify it."
A report that presents unverified assertions in the same voice as evidenced ones
is misleading whoever signs the risk acceptance.

And on tooling I'd take the advice seriously in both directions. A spreadsheet is
fine, and the reason large teams run on them is that the hard parts — framework
selection, question design, judging evidence, writing the report — are not
problems software solves. Buying a platform before the process works usually just
automates a process that didn't work.
