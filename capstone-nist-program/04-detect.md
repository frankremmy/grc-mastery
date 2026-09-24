# Detect — solution walkthrough

> Capstone, lesson 4. _The function where real organisations fail most, and the
> clearest statement of how scoring judgement should work._

## Summary

Detection is the area the course says it sees the most problems with in the real
world, and Oscorp is unexceptional. Antivirus alerts arriving at an IT team is
not security detection. There is no SIEM, so Oscorp has no way of knowing whether
someone is in the environment — and no trained person to respond if it found out.
Most of the function fails immediately on that basis.

**Four passes:**

- **Physical environment monitored** — 24/7 monitoring of the research labs and
  facilities
- **Malicious code detected** — Microsoft Defender is deployed. The walkthrough
  is candid that this is the bare minimum rather than a strong control
- **Unauthorised mobile code detected** — same anti-malware coverage
- **Vulnerability scans performed** — Pass, with "further improvements needed"

Everything else fails: no baseline of normal network behaviour, no event
analysis, no aggregation or correlation, no impact determination, no alert
thresholds, no network monitoring, no personnel activity monitoring, no
monitoring of third-party providers, no detection of unauthorised devices or
connections, no defined detection roles, no compliance mapping, no testing, no
communication paths, no improvement cycle.

### The scoring principle, stated plainly

On the vulnerability scanning control the walkthrough says something worth
lifting out: scans *are* performed, so it passes — **but marking it Fail is
perfectly fine, because the recommendation to the business is identical either
way.** Oscorp needs a comprehensive vulnerability management programme; ad hoc
scans with a purchased scanner are not enough.

That's the cleanest articulation of the scoring rule in the whole capstone. The
question to ask of a borderline control is not "is this a pass or a fail?" but
**"does my verdict change what I recommend?"** If it doesn't, the verdict is
presentational and either answer is defensible. If it does, the verdict matters
and needs thinking about properly.

## Where my assessment diverged

I scored 3 passes against the solution's 4. The single difference is the
vulnerability scanning control, which I failed and the walkthrough explicitly says
can go either way. So Detect is effectively a match, and my Fail is one the
solution itself sanctions.

That's a more useful outcome than agreeing would have been, because it shows what
the earlier divergences were really about. Where I diverged elsewhere, my Fails
changed nothing about the recommendations either — which is exactly why the
solution's approach is better presentation of the same conclusion.

## My take

**A question I would ask Oscorp that neither the notes nor the walkthrough
settle:** *which* Microsoft Defender? The current-state document says "Microsoft
Defender", and that name covers two very different things. Defender Antivirus is
the anti-malware engine built into Windows. Defender for Endpoint is a full EDR
platform with behavioural detection, threat hunting and response capability, and
it is a genuinely strong product that rates at the top of independent evaluations
— not the weak default the walkthrough implies.

The distinction matters enormously here. If Oscorp already licenses Defender for
Endpoint through its Microsoft estate, a meaningful part of the detection gap
could be closed by configuring what they already own rather than buying anything.
If it's the built-in antivirus only, then the gap is real and the SIEM and MSSP
recommendations stand as written. That single question changes the shape of the
year 2 investment case, and it's exactly the kind of thing a live assessment
should establish rather than assume.

The other thing this function confirms is the structural point from my programme
document. Detect and Respond score 17% and 0% while Protect scores 37% — Oscorp
has bought protective controls and has no ability to see whether they are
working or to act when they aren't. Detection is the function that tells you
whether everything else is doing its job, and an organisation without it is
relying on the assumption that its controls are effective, with no mechanism to
discover otherwise.
