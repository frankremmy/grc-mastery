# How I work in this repo

## Structure

- `modules/NN-slug/` — one folder per module. The README is an **index**: a table
  of that module's lessons and the filename each one uses. Notes live in
  per-lesson files named `NN-lesson-slug.md`, numbered in course order.
- `deliverables/` — finished artefacts from the practical assessments.
- `templates/` — reusable blanks: risk register, audit program, TPRM
  questionnaire, lesson notes, module README, blog post.
- `capstone-nist-program/` — the NIST CSF capstone.

Notes started out in the module READMEs; they moved to one file per lesson so
commits stay granular and each lesson maps to one potential post.

## Lesson note format

Summary → key concepts table → "where this shows up in a real job" → gotchas.
See `templates/lesson-notes.md`. The gotchas section is the differentiator: it's
where I disagree with the course or add what the lesson left out. A note without
one isn't finished.

## Content rule

Nothing from the course is reproduced verbatim — the repo is public and the
material is someone's paid product. Notes are rewritten in my own words.
Transcripts, if generated for study, stay local and gitignored (`transcripts/`,
`*.m4a`, `*.wav`).

## Commits

- One commit per lesson or assessment. Message format: `mod-05: notes on PAM`.
- Push my own answers to the practical assessments **before** watching the
  solution videos, and say so in the commit. A repo of transcribed model answers
  is worth less than one showing where I disagreed with them.
- Update the progress table in the root README when a module closes out.

## Assets

Screenshots as `[Screenshot: filename.png]` placeholders in drafts; real files
under the module's `assets/` folder when publishing.

## Publishing

Short notes here, longer write-ups on [frankremmy.com](https://frankremmy.com)
linking back. Weekly cadence rather than per-lesson.
