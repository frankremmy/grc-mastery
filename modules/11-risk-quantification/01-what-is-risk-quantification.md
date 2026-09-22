# What is cyber risk quantification?

> Module 11, lesson 1. _Saying how high "high" actually is._

## Summary

Everything in this course up to now has rated risk on a word scale — low, medium,
high, sometimes critical. That is the entire resolution of the measurement, and
the lesson's point is that it hides differences that matter enormously. Two risks
both rated High can be nothing like each other. One might hurt badly and be
survivable; the other might end the organisation. Recording them identically is
not a rounding error, it's a failure to distinguish between an expensive problem
and an existential one.

Cyber risk quantification is the practice of attaching a monetary value to the
impact of a risk. Instead of "the risk of ransomware affecting our financial
services application is High", you say it is High and could cost the organisation
in the region of two million — or two million and upwards. The rating stays; the
number tells you what the rating means.

The value of doing this is mostly about who you can then talk to. A security
leader arguing for budget with a heat map is asking a finance function to accept a
colour. The same argument carrying a loss figure is in the language executives and
boards already use for every other decision they make. It also lets stakeholders
take a risk seriously in proportion to what it would actually cost them, rather
than in proportion to how alarming the security team sounds.

The lesson frames this as intermediate-to-advanced and comparatively rare —
plenty of GRC professionals have never worked with it, which makes it both
something you could introduce in an organisation and something worth being able
to discuss in an interview. The underlying disposition is the one this whole
course keeps returning to: security decisions are business decisions, and a GRC
professional's job includes carrying the business context that the purely
technical view leaves out.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Qualitative rating | Risk expressed as low / medium / high / critical | Easy, fast, and loses the difference between painful and fatal |
| Resolution problem | Two risks rated the same can differ by orders of magnitude | The prioritisation you build on the ratings is only as good as the ratings |
| Cyber risk quantification | Expressing risk impact in monetary terms | Turns a colour into a comparable figure |
| Business language | Loss figures rather than severity words | Finance and boards already decide in this unit |
| Budget justification | Using loss exposure to argue for investment | Lets a control's cost be compared with what it avoids |
| Stakeholder influence | Numbers move people that adjectives don't | Proportionate attention rather than loudest-voice attention |
| Maturity signal | Uncommon among GRC practitioners | A genuine differentiator in interviews and in an organisation |

## Where this shows up in a real job

I have not done this, and there's no honest way to claim otherwise. What I do
have is the experience of running into the problem it solves. In the module 2
risk assessment I produced a register where several rows carried the same rating
for risks that clearly were not equivalent, and the ordinal scale gave me no way
to say so — the register recorded that they were both High and quietly implied
they deserved the same attention. I noted the limitation at the time without
knowing there was an established answer to it.

The closer parallel from support is the difference between "this is urgent" and
"this is costing the customer X per hour". The first is a claim about my
assessment; the second is a claim about their business, and only the second
reliably changes what happens next. The same asymmetry seems to be what this
module is built on.

## My take

The part I want to hold onto is *why* the qualitative scale fails, because it
isn't obvious. It isn't that words are imprecise — it's that a word scale is
**ordinal**. High is worse than Medium, but nothing in the scale says by how
much, and the intervals between the levels aren't equal or even known. Which
means you cannot legitimately add ratings, average them, or total up a register
to get an overall exposure, even though organisations do all three constantly.
Attaching money doesn't just add detail, it changes the scale to one where
arithmetic is meaningful — you can sum exposures, compare them against a control's
cost, and ask whether the treatment is worth more than the risk.

The thing I'd be careful about is the single figure. "Two million" reads as far
more certain than any such estimate can be, and a number stated with false
precision is easy for a sceptical CFO to dismantle — one challenged assumption
and the entire credibility goes. The lesson's phrasing of "two million or higher"
already hints at the better form, which is a range with some statement of
likelihood attached. I'd expect the model in the next lessons to work that way,
and I'd rather present an honest range than a confident point.

And I'd want to be clear about what quantification is *for*. It's expensive —
gathering loss data and estimating properly takes real effort — so it isn't a
replacement for qualitative rating across an entire register. It earns its cost on
the small number of decisions where the answer actually turns on the size of the
number: the big investment cases, the top few risks, the ones where the board has
to choose. Quantifying everything would be the fastest way to make the technique
unpopular before it demonstrates its value.
