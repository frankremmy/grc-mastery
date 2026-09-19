# Measuring the effectiveness of education and awareness programs

> Module 06, lesson 5. Assessing a programme that exists — and improving one that
> isn't working.

## Summary

The engagement comes in two shapes. Sometimes awareness is one component of a
whole-programme assessment; sometimes it's the specific brief. Usually the ask is
to measure whether the programme does what it's supposed to. Sometimes it's to
improve one — an organisation has a programme, notices users are still falling for
attacks, and brings in a consultant to do it differently.

**Start with the training itself, and its age.** Some organisations are running
courses close to ten years old, full of outdated information and dated graphics.
That ticks the box that training exists while being ineffective, because nobody
engages with it. The recommendation: **take the course yourself, end to end**, and
form a view on what could be improved.

**Then verify everyone has actually completed it.** Training should be part of
onboarding, so every new joiner completes it as compliance training. This gets more
nuanced with size — onboarding processes are not always effective, so meet the HR
people who own it and validate that everyone really does it. Things found in
practice:

- Training that was **optional**, so nobody completed it.
- More insidiously, training that employees completed but which **never applied to
  contractors and consultants**. That's a substantial gap, and a common one.

The recommendation is that training is mandatory *including* for contractors and
external consultants — plenty of organisations have been compromised because a
contractor or third party brought malware in with them.

**Check it runs periodically.** Never a one-off. At least every 12 months, 18 at
the outside, and ideally updated each time with anything new. The bare minimum is
mandatory annual delivery.

**Then look at simulated phishing.** If the organisation doesn't run simulations,
recommending a platform is the improvement. If it does, look deeper at what's being
sent:

- **Calibrate the difficulty.** Not so complicated that it's deliberately tricking
  users; not so easy that it's a giveaway. Striking that balance is a craft.
- **Never name and shame.** A serious mistake. It backfires — people come to resent
  security and some cause problems deliberately. Send a training course instead.

**Finally, look at the data.** Where simulations have run for years, chart the
click numbers and look for trend: rising, falling, flat. But **context matters** —
an organisation that doubled in headcount will have more people clicking simply
because there are more people. Over three to five years a genuine improvement is
often visible, and senior management won't have noticed it because they're occupied
with day-to-day work. Zooming out and showing the long view is something a
consultant is well placed to do.

## The assessment sequence

| # | Check | What you're looking for |
| --- | --- | --- |
| 1 | Course quality and age | Outdated content and graphics; take the course yourself |
| 2 | Completion coverage | Is it in onboarding; is it mandatory; does it reach contractors |
| 3 | Frequency | Annual at minimum; updated, not merely repeated |
| 4 | Simulation existence | Running or not; recommend a platform if not |
| 5 | Simulation design | Difficulty calibrated between tricky and trivial |
| 6 | Response to clicks | Training, never naming and shaming |
| 7 | Trend over years | Direction of travel, normalised for headcount |

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Course age | How long since content was written or refreshed | Old content is the most common cause of disengagement |
| Taking the course yourself | Experiencing the training end to end | The only way to judge whether it's any good |
| Onboarding integration | Training delivered as part of joining | Where coverage is won or lost |
| The contractor gap | Third parties excluded from mandatory training | A frequent finding and a real breach path |
| Mandatory vs optional | Whether completion is required | Optional training is not a control |
| Simulation difficulty | Calibrating between a giveaway and a trap | Too hard measures the designer, not the workforce |
| Naming and shaming | Publicly identifying people who clicked | Actively harmful; damages the reporting culture |
| Normalising for growth | Adjusting figures for changing headcount | Raw counts mislead in a growing organisation |
| The long view | Multi-year trend analysis | What management can't see from inside the day-to-day |

## Where this shows up in a real job

The contractor gap is the finding I'd expect to be able to spot, because I've been
the contractor. Access arrives quickly when someone needs you productive; the
compliance wrapper around that access often doesn't, and nobody notices because the
onboarding checklist belongs to a process built for employees.

Taking the course yourself is advice I'd follow without being told. Judging a
training module from a completion report is like judging an application from its
documentation — the experience is the thing being assessed, and it takes half an
hour to find out.

I haven't analysed multi-year simulation data or run a campaign, so the
measurement half of this is principle rather than practice for me.

## My take

The most transferable technique here is **experiencing the control rather than
reading about it**. Taking the course end to end is the awareness equivalent of
watching a control operate instead of accepting a screenshot — the evidence
hierarchy from module 3, applied to a training module. It also produces findings
nobody can dispute, because you sat through it.

Three things:

**Normalising the data matters more than the lesson suggests, and the honest
metric is a rate.** Raw click counts are meaningless in a changing organisation,
and headcount isn't the only confounder — campaign difficulty, the pretext used,
the time of year and which departments were targeted all move the number. Two
campaigns aren't comparable unless they were comparably hard. So the defensible
presentation is click rate and report rate together, with the campaign design noted
alongside, and a caution that a single campaign's figures are weak evidence in
either direction.

**Report rate is the metric the lesson still doesn't reach.** Everything here
measures failure: who clicked, whether clicks are falling. Clicking can be reduced
and never eliminated, so a programme judged solely on it is judged on the half it
cannot win. Reporting is a capability that can be built, it's the only detection
for a phish that beat every filter, and the time between click and report is most
of what determines the damage. If I were improving a programme, I'd introduce
report rate and median time-to-report as the headline measures and demote click
rate to a supporting one.

**Difficulty calibration has a purpose worth stating explicitly.** The lesson says
strike a balance without saying what the balance is for. A simulation that's too
easy tells you nothing because everyone passes; one built to defeat anyone tells
you nothing because everyone fails, and it damages trust in the programme. The
useful design sits at the level of attack the organisation actually receives — which
means the best source for simulation content is the real phishing the gateway
caught last quarter. That also answers the "is this fair" objection, because it is
by definition.

On naming and shaming, the reason it backfires is worth being precise about. It
doesn't just cause resentment — it teaches people that admitting a mistake is
dangerous, which lengthens the interval between a real click and a real report.
That interval is the thing the whole programme exists to shorten, so the practice
undermines the objective directly rather than just being unkind.
