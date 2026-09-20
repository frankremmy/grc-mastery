# Practical limitations of DLPs

> Module 07, lesson 6. Why organisations still struggle with a control they've
> already paid for.

## Summary

DLP wasn't a success when it arrived — expensive, and organisations struggled to
get value from it. They still struggle. So when you ask what protects their data
and they answer "we have a DLP", the details are what matter. Plenty of senior
managers and executives without technical background assume DLP protects them from
everything, and explaining the limits — and how to improve on them — is where your
expertise earns its place.

**Limitation one: rules, and the monitor-versus-block trap.**

DLP runs on detection rules. Credit card data is the easy case because the format
is fixed. Once the rule exists, you decide: alert, or block?

Block is operationally dangerous. Teams that legitimately work with card
information need to send it, and blocking stops them doing their jobs. So rules
start in monitor mode — and the failure is that many organisations leave them there
**forever**. The DLP generates a large volume of alerts, nobody investigates them,
and the control becomes effectively useless. This is common.

The questions to ask: how many alerts are generated, who investigates them, and
does that team genuinely have the capacity to work through them?

**Limitation two: false positives, especially for intellectual property.**

Card numbers have a format. A secret project or intellectual property does not, so
detection falls back to keyword matching, which generates many false positives — an
alert fires, someone investigates, and the keyword was present but the content
wasn't sensitive. Since security teams are usually under-resourced and overworked,
nobody has the capacity to examine every alert. So an assessment has to ask whether
the team can actually operate the DLP: there's no point running one if nobody
investigates and tunes the alerts.

**Limitation three: DLP is only as good as your data classification.**

The lesson's example is an organisation with a well-configured DLP, good rules, and
full-time DLP analysts — and poor data classification. Sensitive material sits
unlabelled on SharePoint and on desktops, so the DLP doesn't know it's sensitive
and no alert fires. **The DLP is as effective as the classification is.** Which is
why assessing DLP effectiveness starts with data classification and labelling.

**Limitation four: DLP is one control among many.**

Having a DLP doesn't remove the need for everything else — it's one layer in
defence in depth. Identity and access management matters here in particular:
least privilege means employees hold only the minimum data access their job
requires, which reduces the chance of someone leaking data they should never have
been able to reach. Good access control makes the DLP more effective, not less
necessary.

The message for senior management: DLP is a good and effective control, and it's
part of a larger ecosystem for reducing cyber risk.

## The limitations, and what to ask

| Limitation | The failure it produces | Assessment question |
| --- | --- | --- |
| Monitor mode forever | Alerts nobody reads; control exists on paper only | How many alerts per week, and how many were investigated? |
| Blocking breaks work | Business routed around the control, or endless exceptions | Which rules block, and what's the exception list look like? |
| False positives on IP | Analyst time consumed, real alerts buried | What's the false positive rate, and who tunes the rules? |
| Weak classification | Sensitive data invisible to the DLP | What proportion of sensitive data is labelled? |
| Treated as sufficient | Under-investment in access control and everything else | What else protects this data if the DLP misses it? |

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Monitor mode | Alerting without blocking | The safe starting point, and the permanent resting place for too many deployments |
| Block mode | Preventing the transfer outright | Effective and operationally risky; needs confidence in the rule |
| Alert capacity | Whether anyone can work through the volume | Determines whether the control functions at all |
| False positive | An alert where the content wasn't actually sensitive | The cost that quietly consumes the analyst team |
| Rule tuning | Ongoing refinement of detection logic | An operating cost, not a deployment step |
| Classification dependency | DLP can only act on data it knows is sensitive | Why DLP assessment begins outside the DLP |
| Defence in depth | DLP as one layer, alongside least privilege | Prevents the "we have DLP" conversation from ending the discussion |

## Where this shows up in a real job

The alert-nobody-reads pattern is something I recognise from support tooling in
general. Monitoring that fires constantly gets filtered, muted, or ignored — not
through negligence, but because a channel that's wrong most of the time stops
carrying information. The alert volume decides whether anyone reads it, and that's
true well beyond DLP.

The classification dependency also explains something about this module's ordering.
Classification and labelling came first, and it looked like preamble before the
interesting controls. It isn't preamble — it's the input the controls run on, and
the module is arranged that way deliberately.

I haven't tuned DLP rules or worked an alert queue, so the operational weight of
this is understanding rather than experience.

## My take

The strongest idea here is that **DLP is a control whose effectiveness is decided
almost entirely outside the DLP.** Classification determines what it can see;
analyst capacity determines whether its output means anything; access control
determines how much data is in reach to be leaked in the first place. You could
assess a DLP deployment thoroughly without ever logging into the console, which is
a useful thing to realise about a product-shaped control.

Three things:

**Monitor mode forever is a specific, checkable finding, and it deserves a
number.** "Are you monitoring or blocking" gets a vague answer. "How many alerts
did this generate last month, how many were investigated, and how many resulted in
an action" gets three numbers whose ratio tells you everything. An organisation
generating two thousand alerts and investigating forty has a metric problem and a
control that isn't operating, and those numbers are harder to argue with than an
opinion about tuning.

**False positives are a budget, not a defect.** Every alert consumes analyst time,
so the honest framing is that the rule set has to fit the capacity available. Two
well-tuned rules that the team can actually work are worth more than twenty
producing noise — and that's a design decision, not a failure. It also gives a
constructive recommendation for an under-resourced team: reduce the rule set to
what you can service, rather than aspiring to coverage you can't.

**The classification dependency has an uncomfortable implication worth stating.**
If DLP only sees labelled data, then a DLP deployment in an organisation with poor
labelling is protecting the data someone already cared enough about to label — and
missing everything else. That inverts the usual assumption: it's not that DLP
catches most things and misses edge cases, it's that it catches the documented
cases and is blind to the undocumented ones. For an organisation whose crown jewel
is unlabelled research sitting on a laptop, the DLP provides very little.

Which is the honest answer to the executive who says the data is protected because
there's a DLP: the DLP protects what you've told it about. What have you told it
about?
