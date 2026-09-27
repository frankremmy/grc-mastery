# Normative vs informative

> Module 12, lesson 5. _Two words that mean mandatory and optional, and the
> Annex A nuance underneath them._

## Summary

**Normative means mandatory.** It's the content defining what must be met to
claim conformity or achieve certification. In ISO 27001, **clauses 4 to 10 are
normative** — fail them and you fail the audit.

**Informative means guidance.** Background, context, examples, explanation.
**Clauses 0 to 3 are informative** — nothing in them creates an obligation.

**The language is the tell.** Normative text uses *shall*, *must*, *is required
to*. Informative text uses *may*, *can*, *for example*. When reading an ISO
document or a client's certification report, the verb tells you whether something
is a requirement or a suggestion.

### Where you'll actually meet these words

Four situations:

- **Working as a GRC analyst** at an organisation already certified — the
  existing ISMS documentation will use them
- **Third-party risk management** — a certified supplier's documentation will use
  them
- **Auditors**, particularly newer ones who have just learned the standard and
  use the vocabulary to impress or to intimidate. "Show me your normative
  clauses" is a real thing people say, and the course's observation is that it
  usually isn't the good auditors saying it
- **Interviews**, as a screening question. When a CV claims years of ISO
  experience, "what's the difference between normative and informative?" is a
  fast way to find out whether that's real, with follow-up questions depending on
  the answer

### The Annex A nuance

This is the part that matters more than the definition.

Annex A is a comprehensive list of controls. **It is not mandatory to implement
all of them** — that would be as absurd as telling an organisation to implement
every control in NIST 800-53. These catalogues are deliberately comprehensive;
no single organisation needs everything in them.

What *is* mandatory, as part of the normative clauses, is that your risk
assessment **selects** Annex A controls. And once selected, those controls become
mandatory to implement — they become normative for that organisation.

**And you must justify the ones you didn't select.** Excluding a control isn't
enough; the exclusion needs a documented reason. The course flags this as a
mistake junior auditors make — they check that selected controls are implemented
and never ask why the others weren't.

## Key concepts

| Term | Meaning | In ISO 27001 |
| --- | --- | --- |
| Normative | Mandatory; required for conformity | Clauses 4–10 |
| Informative | Guidance; no obligation created | Clauses 0–3 |
| *shall* / *must* / *is required to* | Marks a requirement | Normative language |
| *may* / *can* / *for example* | Marks permission or illustration | Informative language |
| Annex A | Reference catalogue of 93 controls | Not implemented wholesale; selected via risk assessment |
| Selected controls | Controls chosen through risk assessment | Become mandatory to implement |
| Exclusion justification | Documented reason a control was not selected | Mandatory, and commonly missed |

## Two things worth adding

**The wording isn't a translation quirk — it's a documented drafting
convention.** The course speculates it might come from ISO being Swiss and
standards being translated. The actual answer is that the **ISO/IEC Directives,
Part 2** define the verbal forms used across every ISO standard, precisely so
requirements are identifiable regardless of language:

| Verb | Meaning |
| --- | --- |
| **shall** | Requirement — mandatory |
| **should** | Recommendation — advised, not required |
| **may** | Permission — allowed |
| **can** | Possibility or capability — a statement of fact |

Knowing this is a codified convention rather than an accident is a better answer
than the definition alone, and it's exactly the kind of follow-up that separates
someone who has worked with the standards from someone who memorised a
distinction.

**"Should" is the word the course's list leaves out, and it's the one that causes
trouble.** It sits between mandatory and optional — a recommendation. It matters
because ISO 27002, the implementation guidance for the Annex A controls, is
written almost entirely in *should*. People read 27002, see detailed
instructions, and assume they're requirements. They aren't. The requirement is in
27001; 27002 tells you one way to satisfy it.

**Annex A's own status is more precise than "not mandatory".** In ISO 27001:2022,
clause 6.1.3(c) requires the organisation to compare the controls it determined
against Annex A **to verify that no necessary control has been omitted**. So
Annex A is normative in the sense that you are required to *use* it as a
checklist, even though no individual control is individually compulsory. That
resolves the apparent contradiction — the annex is mandatory to consult, the
controls are selected by risk. And clause 6.1.3(d) is where the Statement of
Applicability comes from: it must record the necessary controls, the
justification for including them, whether they're implemented, and **the
justification for excluding** the rest.

## My take

The exclusion justification is the part I'd want to remember, because it's where
the useful information lives and it's the half everyone skips.

For supplier assessment this is immediately practical. In module 9 I concluded
that the right thing to ask a certified supplier for is the SoA rather than the
certificate. This lesson sharpens why: the SoA's **exclusions and their stated
reasons** tell you what the organisation decided it didn't need. A supplier who
excluded a control because it genuinely doesn't apply — no software development,
no on-premises servers — has made a defensible call. A supplier who excluded
something load-bearing with a thin justification has told you something the
certificate never would.

The interview framing is worth noting too. The definition — normative is
mandatory, informative is guidance — is the answer that gets you past the screen.
The answer that demonstrates experience is the Annex A one: not all controls are
required, the ones your risk assessment selects become required, and the
exclusions need justifying in the SoA. That's a distinction you only articulate
that way if you've had to produce or review one.
