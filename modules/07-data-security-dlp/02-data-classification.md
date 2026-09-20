# Data classification

> Module 07, lesson 2. Deciding what's worth protecting, before deciding how to
> protect it.

## Summary

You can't encrypt everything and put DLP controls over all of it. That isn't
practical — it produces thousands of alerts and stops the business operating. So
protection has to be selective, and selecting requires knowing what the data is.

That makes **data classification** the first thing to look at when assessing data
security. The question to the organisation: do you have a data classification or
information classification policy?

**Whose job it is.** These documents are usually produced by data governance
professionals or data privacy officers. Creating them is not the GRC
professional's role — though you may be asked to assist, and where you add value is
the security expertise: the impact of a breach, the consequences of particular data
becoming public, what attackers can do with personally identifiable information.
The rule to hold: **classifying the data isn't your job, but understanding how it's
classified is.**

### The worked example: an insurance company

**Step one — data identification.** What data does the organisation have, and
where does it live?

- **Employee data.** For 200 employees, held in an HR system — employee numbers,
  salary details.
- **Employee files.** Documents on desktops and laptops, and in SharePoint if the
  organisation uses Office 365, which is common.
- **Customer data.** The people holding insurance claims — names, contact details,
  claim details — held in an insurance database.

**Step two — classification.** Organising data by how sensitive or important it
is. The organisation defines the scheme in a document stating what each level
means. For this insurer:

| Classification | Definition in this example | Why |
| --- | --- | --- |
| **Sensitive** | Data containing personally identifiable information — first name, last name | Identifies individuals |
| **Confidential** | Data containing financial information — e.g. "$500 million paid in claims last year" | Valuable to the organisation, but identifies no individual |
| **Public** | Information anyone can already find, such as content on the website | No consequence if it leaks, because it's already out |

The distinction between sensitive and confidential in the example is worth noting:
the claims total is confidential rather than sensitive precisely *because* it
doesn't say which customers claimed what. Aggregate financial data and personal
data are different kinds of problem.

And public data needs no encryption and no DLP rules — spending controls on it is
waste.

**Then the hard part.** Writing the definitions is theoretically easy. Applying
them to actual data — labelling — is the difficult part, and it's the next lesson.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Selective protection | Controls applied where they're needed, not everywhere | Protecting everything equally is operationally impossible |
| Data classification policy | The document defining what each sensitivity level means | The reference every later control decision points back to |
| Data identification | Finding what data exists and where it lives | Precedes classification, as asset identification precedes asset classification |
| Ownership of the scheme | Data governance or privacy professionals write it; security advises | Know where your judgement is wanted |
| Security's contribution | Breach impact, consequences of exposure, what attackers do with PII | The expertise you bring to someone else's document |
| Sensitive vs confidential | Identifies a person vs valuable to the organisation | Different harms, different obligations, different controls |
| Public data | Already accessible, no protection required | Controls here are pure cost |
| Alert volume | Over-classification produces noise | The practical reason classification has to discriminate |

## Where this shows up in a real job

The structure here is exactly module 4's asset management with a narrower subject:
identify first, classify second, and the classification decides what gets
protected. Recognising that pattern makes this lesson much faster to absorb — and
it suggests the same failure modes will apply, particularly the one where the
exercise is done once and never maintained.

The "data lives in more places than the system of record" point is familiar from
support. Customer data is in the database, and it's also in exported spreadsheets,
in email attachments, in a screenshot someone pasted into a ticket, and in whatever
someone downloaded to their laptop to work on at the weekend. The database is the
easy part to find and protect.

I haven't written or applied a classification scheme, so this is principle for me
rather than practice.

## My take

The clearest idea is that **classification exists to make protection affordable**.
It isn't a documentation exercise for its own sake — it's what makes it possible to
say no to protecting something, which is what keeps the controls usable. An
organisation that classifies everything as sensitive has, in effect, classified
nothing, because every control then applies everywhere and the alerts become
unreadable.

Three things:

**Keep the number of levels small, and define them by consequence.** Three or four
levels is normally enough. Schemes fail when they add levels nobody can
distinguish, because the person labelling a document has to make the call in a few
seconds. The definitions that work are phrased as *what happens if this gets out* —
"would harm an individual", "would harm the business", "no harm" — rather than as
abstract categories, because that's a question the person holding the document can
actually answer.

**Sensitive data carries obligations, not just risk.** The example treats PII as
the most sensitive category on impact grounds, which is right, and there's a second
reason: personal data comes with legal duties — lawful basis, retention limits,
subject rights, breach notification. That's the module 2 privacy point resurfacing.
It means the sensitive tier isn't simply "more important", it's the tier where
someone outside the organisation has a say in what you do.

**Classification is a living record, and it's where I'd expect the gap in any
assessment.** A scheme written in 2019 describes the data the organisation had in
2019. New systems, new data types, new integrations and acquisitions all arrive
unclassified by default. So the assessment questions aren't only "do you have a
policy" but "when was it last reviewed", "what classifies new data when it's
created", and "who decides". Exactly the questions that mattered for the asset
register, for the same reason.

One practical note for the next lesson: the classification scheme is only as useful
as the organisation's ability to apply it consistently. Two people labelling the
same document differently is a scheme problem, not a discipline problem — which is
why the definitions need examples attached, not just descriptions.
