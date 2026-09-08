# Introduction to GRC

> Module notes from GRC Mastery. Status: **in progress**

## What this module covers

GRC, governance, risk and compliance, as it applies specifically to cyber
security, which is a narrower thing than corporate GRC. Corporate GRC covers
financial controls, ESG, legal exposure and a lot else. Cyber GRC is the slice of
that concerned with information security risk. Worth being precise about, because
the terms get used interchangeably and the scope difference matters when you're in
a room with the wider risk function.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Governance | The rules, structures and accountability for managing security risk — policies, a CISO, a risk committee | Without it nobody owns the decision, and security becomes whatever the loudest engineer thinks is urgent |
| Risk management | Identifying what matters, assessing the threats to it, ranking what gets fixed first | Budget and headcount are finite; this decides where they go |
| Compliance | Meeting the laws, regulations and standards that apply — privacy law, sector rules, certifiable standards | Often the forcing function that gets security funded at all, for better and worse |
| Cyber GRC vs corporate GRC | Cyber GRC is a subset scoped to information security | Avoids overclaiming scope in interviews and with the wider risk function |

## Practical work

- [x] Knowledge check
- [ ] Introducing Oscorp (running case study org for the course)
- [ ] Lesson summary

## Where this shows up in a real job

The ISO 27001 coordination work at Helium Health was all three of these at once,
though nobody used the vocabulary. Governance was the steering group and who
signed off. Risk management was the register we maintained. Compliance was the
certificate at the end. The named framework is new to me; the activity isn't.

Support work touches this more than people assume. Every access request, every
"can you just give me admin on this," is an access control decision that
governance is supposed to have already answered. When it hasn't, L2 ends up making
risk decisions by default and without a mandate.

## Gotchas / what most orgs get wrong

- **The course's house analogy doesn't hold up.** It files the alarm under
  governance and the locks under risk management. Both are controls — the output,
  not the discipline. A version that maps properly: governance is the household
  rules and who enforces them; risk management is deciding the back window is the
  weak point and worth spending on before the shed; compliance is the building
  inspector signing off. Keeping this clean matters, because the most common
  failure in real programs is exactly the confusion the analogy encodes — buying
  tools and calling it a risk program.
- **The three aren't sequential.** They run continuously and feed each other.
  Treating GRC as a project with an end date is how you get a policy set that's
  accurate on certification day and stale six months later.
- **Compliant is not secure.** A certificate proves a control existed at audit
  time. It says nothing about whether it worked on any other day.

## Post

- Blog: _link_
- LinkedIn: _link_