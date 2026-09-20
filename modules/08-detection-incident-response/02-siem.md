# Security information and event management (SIEM)

> Module 08, lesson 2. The central log platform detection runs on, and the five
> questions that reveal whether it works.

## Summary

A SIEM is a centralised log system — a server or group of servers ingesting logs
from most or all systems. Instead of reading firewall logs in the firewall and
email logs in the email system, everything lands in one place.

Two things follow from that. **Detection use cases** can be built in the SIEM, so
unusual activity raises an alert for an analyst to investigate, rather than each
system alerting separately and leaving the investigator to stitch it together. And
logs can be **correlated** — an attacker who comes through the firewall and then
attacks the email system produces one picture in one place rather than two
unrelated entries.

**The products:** Splunk is the most popular; Microsoft Sentinel is growing,
especially with Azure.

**The GRC role** isn't checking the SIEM's configuration — that's for analysts and
security engineers. It's assessing it from a risk and governance perspective.

### Why SIEMs are hard

**Cost.** SIEMs are expensive. Splunk is notoriously costly, and pricing scales
with the volume of logs ingested.

**Skills.** Even after buying one, finding a qualified, experienced analyst to
configure it is difficult. It doesn't work out of the box — someone has to onboard
the logs and build the detection use cases.

**Coverage is a compromise.** Ideally every log goes in. Practically that isn't
possible, so you start with important systems: email, cloud instances, servers,
critical applications. Even that isn't straightforward, and more logs means more
cost — which organisations aren't always willing to pay.

**Detection use cases are ongoing work.** Rules built to detect unusual activity
generate alerts; some genuine, many **false positives** — an alert says phishing,
you investigate, it's noise, and the rule needs tuning. That tuning never finishes.
It's a continuous programme requiring qualified analysts, not a configuration task
that completes.

### The five assessment questions

When an organisation says it has a SIEM:

1. **What's the coverage?** Which system logs are onboarded? Anything not onboarded
   is invisible — if those systems are attacked, no alert fires.
2. **Are detection use cases aligned to an industry framework?** Frameworks such as
   MITRE ATT&CK exist so you can check you're detecting the range of malicious
   activity rather than whatever occurred to someone.
3. **How often are use cases reviewed?** Periodically, to confirm they generate
   valid alerts rather than noise.
4. **Is there 24/7 coverage?** What happens to an alert at 3am on a weekend — does
   an analyst see it, or does nobody find out?
5. **How is out-of-hours handled?** An on-call roster, or a managed security
   service provider doing the monitoring.

Answers to those tell you whether the SIEM is effective.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| SIEM | Centralised log collection, correlation and alerting | The platform detection capability is built on |
| Log ingestion | Feeding system logs into the SIEM | Determines what can be seen at all |
| Correlation | Linking events across systems into one picture | Turns scattered entries into an attack narrative |
| Detection use case | A rule identifying suspicious activity | The thing that actually produces alerts |
| False positive | An alert that turns out to be noise | The recurring cost that consumes analyst capacity |
| Tuning | Ongoing refinement of use cases | A programme, not a deployment step |
| Coverage | Which systems are onboarded | The single most revealing question in an assessment |
| Framework alignment | Mapping use cases to MITRE ATT&CK or similar | Guards against detecting only what you thought of |
| Out-of-hours coverage | On-call rota or MSSP | Decides whether detection exists at 3am |

## Where this shows up in a real job

This is the lesson my Wazuh lab maps onto most directly — Wazuh is a SIEM, and
building one taught me what ingestion, rules and alerts actually involve. The part
the lab can't reproduce is the economics: at home, ingesting everything costs
nothing and the alert volume is whatever I generate deliberately. In an
organisation, ingestion has a price per gigabyte and alerts have a price in analyst
hours, and those two constraints shape every real deployment.

The false positive dynamic is familiar from support monitoring more broadly. A
channel that's wrong most of the time stops being read, and the failure looks like
negligence when it's actually a rational response to a noisy signal.

I haven't worked with Splunk or Sentinel, and I haven't tuned use cases against
production noise — which is the difference between having built a SIEM and having
operated one.

## My take

The five questions are the most directly reusable thing in this module so far, and
what makes them good is that **each one is answerable with a fact rather than an
opinion.** "Do you have a SIEM" gets a yes from almost everyone. "Which systems are
onboarded" gets a list, and the list can be compared against the asset register —
which is exactly why module 4 came first. A SIEM's coverage cannot be assessed by
an organisation that doesn't know what it owns.

Three things:

**Coverage is where the finding usually is, and it has a predictable shape.** Cost
scales with ingestion, so organisations onboard what's cheap or obviously
important and leave out what's noisy, legacy, or awkward to integrate. That tends
to mean the older systems, the ones acquired through a merger, and anything without
a native connector — which is also a reasonable description of where attackers find
purchase. The gap isn't random; it follows the budget.

**Framework alignment answers a question the other four don't: what are you not
looking for?** Reviewing existing use cases tells you whether what you built still
works. Mapping them to ATT&CK tells you which techniques have no detection at all.
That's the difference between improving what exists and discovering what's absent,
and it's the same move as third line asking what nobody has verified.

**"We have a SIEM" and "we have detection" are different claims.** A SIEM with
partial ingestion, unreviewed rules and nobody watching overnight is a log
archive — genuinely useful after an incident for reconstructing what happened, and
not a detection capability. Worth separating in a report, because an organisation
in that position has something valuable and should be told what it actually has
rather than only what it lacks.

One economic point worth carrying into any recommendation: because SIEM cost scales
with volume, "ingest more logs" is never free advice. The defensible version
prioritises by the asset register and the crown jewels — onboard the systems that
hold what matters first, and say so explicitly, rather than recommending coverage
in the abstract and leaving the client to discover the invoice.
