# Data loss protection mechanisms

> Module 07, lesson 5. How DLP actually works, what it's asked to catch, and the
> use cases that justify it.

## Summary

DLP appeared in the early 2000s and became common from around 2006–2007 onwards,
first in large financial institutions and highly secure environments like defence.
Early products were appliances bought from a vendor and deployed on site —
Symantec and Forcepoint among the popular ones — and they were, in the lesson's
account, a considerable pain to work with. Many organisations spent heavily on DLP
and never got the value they expected.

Banks invested most, because financial regulation requires financial data to be
protected. And that was an era before encryption by default, so DLP controls
mattered for keeping credit card and financial information inside the
organisation.

### The two modes DLP looks at

| Mode | What it means | Examples |
| --- | --- | --- |
| **Data at rest** | Stored and not moving | Files on a disk, databases on a hard drive |
| **Data in motion** (in transit) | Moving from one place to another | An email leaving the organisation; copying files to a USB drive |

### How it works

Detection rules are created to monitor the movement of sensitive data. Two
possible responses:

- **Monitor and alert.** Sensitive data moves, DLP raises an alert, and a security
  professional investigates.
- **Block.** An employee tries to email credit card information to a personal
  address; DLP detects the card data in the email and stops it leaving.

### What gets detected

- **Credit card information** — central for banks and financial services.
- **Personally identifiable information.**
- **Intellectual property** — a secret recipe, or the ingredients of a drug a
  pharmaceutical company is developing, which shouldn't leave on a USB drive or by
  email.
- **Manually defined keywords** — the name of a sensitive project, or even
  profanity the organisation doesn't want sent to customers.

### Two use cases worth knowing

**Insider threat monitoring, especially around resignations.** People who resign
frequently try to copy their work and projects to personal email, often believing
that because they worked on it they own it — while legally the work is the
company's intellectual property. So security teams commonly apply extra monitoring
to people who have resigned. And the lesson makes a point worth keeping: more often
than not this isn't malicious, it's negligence, and DLP is effective at stopping it.

**Large transfer detection, for exfiltration.** A rule alerting on any attempt to
transfer files larger than, say, 5 GB. When an attacker gets into an organisation,
copying large volumes of data out is one of the first things they do — and DLP can
block it and alert the security team. The lesson's experience is that this alert is
how several organisations discovered they were under attack at all: attackers are
often good at hiding their activity, and the moment they start moving data out is
where the alert finally fires.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Data at rest | Stored data, not moving | Discovery — finding sensitive data where it shouldn't be |
| Data in motion | Data moving between locations | Where most DLP enforcement happens |
| Detection rule | The logic identifying sensitive content in movement | The configuration that determines whether DLP works at all |
| Monitor vs block | Alert on movement, or prevent it | Different operational and business consequences |
| Pattern-based detection | Card numbers, identifiers, defined keywords | Effective for structured, recognisable formats |
| Insider threat monitoring | Watching for data taken by employees | The most common business justification |
| Leaver monitoring | Extra scrutiny after someone resigns | A specific, defensible, time-bounded application |
| Volume-based rules | Alerting on unusually large transfers | Content-agnostic, and often the detection that catches an intrusion |

## Where this shows up in a real job

The leaver scenario is entirely recognisable, and the "negligence not malice" point
matches what I'd expect. People take their work because they think of it as theirs
— a portfolio, a reference, the thing they spent two years on. Almost nobody
framing it that way thinks of it as theft, which is exactly why a control is more
effective than an expectation.

The large-transfer rule is the part I find most interesting, because it's the one
that doesn't depend on understanding the content at all. My CVE lab and the
detection work I've done are about recognising known-bad things; this is about
recognising *abnormal volume*, which catches what no signature covers.

I haven't operated a DLP platform, tuned detection rules, or handled DLP alerts —
so this is understanding rather than experience.

## My take

The two detection approaches in this lesson are doing genuinely different jobs, and
the difference is worth holding.

**Content-based rules** — card numbers, identifiers, keywords — are precise where
the data has a recognisable shape and weak everywhere else. A credit card number
has a fixed format and a checksum, so it's detectable with high confidence.
Oscorp's formula, by contrast, is prose and numbers in a Word document with no
distinguishing pattern, which is why keyword rules get used and why they're
brittle: rename the project and the rule stops matching.

**Volume-based rules** ignore content entirely and ask whether this movement is
normal. That's why the 5 GB rule catches intrusions that content rules miss —
attackers exfiltrate data the DLP was never taught to recognise. It's behavioural
detection rather than signature detection, the same distinction as the anti-malware
versus SOC layers from module 6.

A programme relying only on the first kind protects the data it can describe. Most
organisations can describe card numbers and struggle with everything else.

Two more:

**Monitor-versus-block is a business decision, not a technical setting.** Blocking
stops the leak and also stops the false positive — the legitimate email with a
customer's details that a salesperson genuinely needed to send. Get that wrong at
scale and the business routes around the control, or the exceptions list grows
until the control is decorative. The usual honest sequence is monitor first to
learn the false positive rate, then block the narrow categories where confidence is
high. An organisation that switched straight to blocking on day one either has
excellent classification or a quiet backlog of workarounds.

**Leaver monitoring is the clearest case where the GRC question isn't technical.**
Watching a specific named employee more closely after they resign is proportionate,
time-bounded and defensible — and it's also surveillance of an individual, which
needs a documented basis, a defined duration, a limit on who sees the output, and
in some jurisdictions disclosure in the employment terms. That's the privacy
assessment territory from module 2. Doing it without that basis turns a reasonable
control into an employment law problem, and this is exactly the kind of thing a
GRC professional is there to catch before it becomes one.
