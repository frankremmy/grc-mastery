# Introduction to ISO 27001 lead auditor training

> Module 12, lesson 1. _What this module sets out to do, and how I'm handling it
> in this repo._

## Summary

This is the longest module in the course — twenty lessons covering ISO 27001
end to end, and it's taught as an implementation rather than a lecture. The
approach is to build the thing from scratch: work through the clauses one at a
time, go through the Annex A controls line by line, and produce the policies and
documentation a real ISMS requires. The course supplies spreadsheets and
documentation intended to be reusable on the job.

The framing is that it works for two audiences — people meeting ISO 27001 for the
first time, and people already holding the Lead Auditor certificate who have done
the theory without ever implementing anything.

## Where this fits for me

ISO 27001 has come up repeatedly already. The Oscorp applicability analysis in
module 1 separated it from the legal obligations as *a voluntary certifiable
standard, not a law* — a distinction the CEO's "pass all regulations" framing got
wrong. The Horizon Labs assessment in module 9 leaned on the difference between a
certificate and its scope statement. The capstone roadmap put certification
readiness in year 3, as external assurance for Oscorp's research partners rather
than as an end in itself.

So this module fills in the thing I've been referring to without being able to
work with directly.

## Two things I want to be careful about

**The 2022 revision.** ISO/IEC 27001:2022 restructured Annex A substantially —
from 114 controls across 14 domains down to 93 controls in four themes
(organisational, people, physical, technological), with eleven new controls
including threat intelligence, cloud services, and secure coding. Anyone
describing Annex A in the old shape is working from ISO 27001:2013. Worth
checking which version the course material reflects as I go, because in an
interview the version I describe dates me.

**Lead Auditor training is not certification.** Completing this module teaches the
material; the credential comes from an accredited training provider with an exam,
and being a *certified* lead auditor able to conduct third-party audits requires
that plus logged audit experience. I'll describe what I've done accurately in the
repo and on my CV — "worked through ISO 27001 lead auditor training material" is
true and useful; "ISO 27001 Lead Auditor" as a credential is not.

## Repo handling

The course provides templates and documentation. Those are its paid product, so
they don't go in this repo — same rule as the case study source documents.

What does go in: policies, registers and audit artefacts **I write myself** for
Oscorp, following the structure the module teaches. That's the same arrangement
as the FAIR calculator in module 11 — I built my own rather than committing the
course's spreadsheet, and the result was more useful because I had to understand
every cell to build it.
