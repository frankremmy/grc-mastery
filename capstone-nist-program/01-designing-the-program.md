# Designing a comprehensive cyber security program

> Capstone, lesson 1. _The method: framework as scaffold, interview notes as
> evidence, gaps as recommendations._

## Summary

The capstone is an end-to-end security programme for a whole organisation —
normally the work of a senior consultant, a security manager, or a CISO. The
method has three steps.

**1. Use a framework as the reference.** The NIST Cyber Security Framework,
worked through a spreadsheet with one tab per function: **Identify, Protect,
Detect, Respond, Recover**. Each tab holds that function's subcategories with an
explanation of the control area, a control description stating the practice
expected, and a question to put to the organisation to establish whether the
control exists. The control descriptions are effectively a statement of good
practice; asking whether the organisation meets each one is the assessment.

**2. Gather information.** In a real engagement this is interviewing stakeholders
and taking notes. Here the interviews are supplied as a current-state document,
which is the evidence base for every answer.

**3. Assess and recommend.** Work through each control description, answer pass
or fail from the notes, and the failures become the recommendations. Where the
notes don't cover something, make an assumption and answer anyway rather than
leaving it blank.

The framing worth holding onto is that the recommendations aren't invented at the
end — they fall out of the assessment. Every fail is a recommendation, which means
the quality of the programme depends entirely on how honestly the controls are
answered.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Framework as scaffold | NIST CSF provides structure and coverage | Stops an assessment reflecting the assessor's favourite topics |
| Five functions | Identify, Protect, Detect, Respond, Recover | The top-level organisation of the assessment |
| Control description | The practice expected of a mature organisation | The benchmark a pass or fail is measured against |
| Assessment question | What to ask the stakeholder | Turns a control statement into an interview |
| Evidence base | Current-state notes standing in for stakeholder meetings | Answers must trace to something, not to intuition |
| Pass / fail | The verdict per control description | Binary by design — forces a position |
| Gaps become recommendations | Every fail is something to fix | The programme is the output of the assessment, not a separate exercise |
| Documented assumptions | Answer even where the notes are silent, and say so | Silence is not a pass; an unanswered control is a hidden gap |

## Where this shows up in a real job

The shape is the same as the module 3 audit work — a control set, evidence against
each control, a conclusion per control, findings from the failures. The difference
is scope. An audit tests a defined area; this covers the whole organisation, which
means the discipline that matters most is not going deep on the parts I find
interesting. My instinct was to spend disproportionate time on IAM and incident
response because I'd just done detailed work on both. The framework exists
precisely to stop that.

The interview step is the one I'd expect to be strongest at, and it's simulated
away here. Getting an accurate picture of how something actually works from
someone describing how they believe it works — without making them defensive about
the gaps — is most of what support escalation is. The notes document is a
cleaned-up version of a genuinely messy activity.

## My take

**Pass or fail is a judgement, and the burden of proof decides the result.** A
control the notes are silent about is not a pass. Nor is a control where something
exists but nothing maintains it — an asset spreadsheet that was accurate when
built and has never been reviewed fails a control asking for a current inventory.
That distinction came up in almost every module, and it was the main thing
separating a careful assessment from a generous one here.

**Recommendations need sequencing, not just a list.** A large assessment produces
dozens of failures, and handing back a flat list is a backlog rather than a
programme — the organisation will start with whichever is easiest. What turns
findings into a programme is ordering them by dependency: what must exist before
other things can work, what is free and immediate, what is a funded project. Asset
management usually comes first for exactly that reason.

**Record where evidence ran out.** An assessment that doesn't distinguish evidence
from inference reads as more certain than it is, and the reader can't tell which
conclusions to challenge.

## Method note for this repo

My own pass went in before the course's solution. The comparison afterwards is
the point — where I was harsher, where I was generous, and what I missed.

**Deliverables:** [NIST CSF assessment](../deliverables/capstone-oscorp-nist-assessment.xlsx)
· [Security programme and three-year roadmap](../deliverables/capstone-oscorp-security-program.md)
