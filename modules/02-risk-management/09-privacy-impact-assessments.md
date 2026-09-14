# Privacy Impact Assessments (PIA)

> Module 02, lesson 9. A parallel assessment with a different question behind it —
> and one I'm told not to run myself.

## Summary

Privacy impact assessments sit alongside cyber security risk assessments. The two
overlap, and they are not the same activity. A PIA is triggered when personally
identifiable information is in play.

PII is anything that identifies a person: a combination of first name, last name
and date of birth, and on into details like religion or political views — anything
that both identifies an individual and could be used against them. The worked
example is a financial application holding names, dates of birth and credit card
numbers. Assessing that application for security risk, the right move is to flag
that a PIA needs to happen.

The part of the lesson with the sharpest edge is about ownership. The GRC
professional is not the person who conducts the PIA. Management will sometimes ask,
and the instructor's position is to decline: privacy assessments need legal
training, so they belong with lawyers or solicitors. The security role is to
support — explain how the application works, what data moves where, what controls
exist — not to own the assessment or make the legal call.

The habit that comes out of it is a question to ask early in every assessment:
does this system handle PII? If yes, two things follow — ask what protects it, and
ask for a PIA to be conducted.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Privacy impact assessment | An assessment of how a system affects individuals' privacy | Answers a different question from a security assessment, so it can't be folded into one |
| PII | Information that identifies an individual, alone or in combination | The trigger condition; also why a "harmless" field can matter once combined with others |
| Identifiability in combination | Name plus date of birth identifies where either alone might not | Scope is about the dataset, not any single field |
| Runs alongside, stays separate | PIA and security risk assessment happen together and stay distinct | Different questions, different expertise, different owner |
| Supporting role | Security explains the technical reality; legal makes the determination | Knowing the boundary is part of doing the job properly |
| The PII question | "Does this system handle PII?" asked at the start of every assessment | Cheap to ask, and it changes what else you have to do |

## Where this shows up in a real job

Helium Health is the clearest case — health data is PII and then some, and the
privacy questions there were genuinely different from the security ones we were
answering for ISO 27001. At the time I'd have described both as "compliance". They
aren't.

In WooCommerce support, PII is routine. Stores hold customer names, addresses,
order histories and payment details, and a reasonable share of tickets are
privacy-shaped rather than security-shaped: exporting a customer's data on
request, erasing an account, working out what a plugin is storing and where. I've
been answering the technical half of privacy questions for years without the
vocabulary for the other half.

The boundary in this lesson also matches something I already do. When a support
question turns into a legal one — liability, what a store owner is obliged to do —
the correct move is to stop and route it, not to improvise. Same instinct, higher
stakes.

## My take

The reason a PIA can't be folded into the security assessment is that they're
asking different questions. Security asks whether the data is protected. Privacy
asks whether you should be holding it at all — on what basis, for what purpose,
for how long, and what the person it describes can ask you to do about it. A
system can pass every security control and still be handling data it had no
business collecting. That distinction is the whole point, and it's why the answer
"it's encrypted" doesn't close a privacy question.

Two things to carry:

**Ask the PII question first.** It costs one sentence and it changes the shape of
the whole assessment — what's in scope, who else needs to be involved, which
obligations attach. Finding out late is expensive.

**Know where my judgement stops.** Explaining what an application does with data
is squarely my job. Deciding whether that use is lawful is not, and being clear
about the line is more professional than being helpful past it. The supporting
role is still substantial — a privacy assessment done without someone who
understands the system produces confident conclusions about a system nobody
actually described.
