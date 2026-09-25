# Recommendations — solution walkthrough

> Capstone, lesson 7. _Turning the assessment into recommendations, and one
> distinction worth getting right._

## This was advisory, not an audit

The walkthrough opens with a correction that matters more than it first appears.
What we did is **consultation or advisory work**. It is not an audit.

Using a recognised framework, asking control questions and recording pass/fail
answers makes it *look* like an audit, and people in the industry claim it as one
regularly. It isn't. An audit is scoped as an audit from the outset, with its own
rules, independence requirements and reporting obligations — as covered in module
3. Calling advisory work an audit misrepresents the assurance it provides.

Worth holding onto for two reasons. It's a credibility marker: someone who
conflates the two hasn't worked alongside a real audit function. And it's an
honesty point — an audit carries assurance weight that a consultant's assessment
does not, and claiming the stronger word oversells the work.

## Why an industry framework

Not because NIST is uniquely good, but because of what it enables:

- **Comprehensiveness.** The controls cover essentially everything a security
  programme needs, so recommendations aren't a list of whatever the assessor
  happened to think of
- **A measurable baseline.** The report leads with recommendations and carries
  the control-by-control assessment in an appendix. Re-run the same assessment in
  twelve months and you can show exactly how far the organisation has moved

That second point is the argument for keeping the completed spreadsheet as a
deliverable rather than treating it as working paper. It is the baseline.

**Recommendations are not written in the framework's words.** You take the
control's intent and express it in language the client can act on, drawing on
experience. There's no single correct wording — what matters is covering the
substantive points.

## The recommendations

**Cyber security governance — first, because everything depends on it.** Oscorp
has no security team; security is handled by IT, which lacks the skills, the
expertise and the capacity. Hire a cyber security manager or CISO to lead the
function — that person then writes the policies and standards. Document roles and
responsibilities and socialise them with senior management, including making the
board aware of its own security duties. Produce an information security policy
**endorsed by senior management**, not a Word document nobody uses. Then hire
security professionals to run the practice.

**Asset management.** Nothing exists; a programme has to be started.

**Third-party risk management.** Also nothing. The walkthrough notes the industry
pattern: an organisation with no security team, where IT owns security, almost
certainly has no asset management and no TPRM either. Oscorp is a realistic
example rather than an exaggerated one.

**Cyber security risk management.** A process to assess and manage cyber risk,
prioritising by criticality and business impact; endorsed by the audit and risk
committee *and the existing risk team* — or by senior management if no committee
exists; a cyber risk register; and an internal audit programme with cyber in
scope.

**Identity and access management.** Two-factor authentication rolled out across
the organisation is the urgent one — non-negotiable, high impact, not especially
hard. Least privilege and separation of duties across the organisation, which is
a large undertaking. Review admin users, eliminate shared admin passwords, and
implement role-based access control — shared admin passwords are described as a
big red flag, and the answer is assigning the role rather than sharing the
credential. Then regular user access reviews, because implementing a principle
once is not the same as maintaining it.

**Security education and awareness.** Not a priority relative to everything else,
given the current state. Training at least every 12 months; consider a simulated
phishing solution.

**Data security and DLP.** Identify, classify and label the data. Microsoft's
information protection and DLP tooling, since the environment is already
Microsoft. Block USB flash drives — easy to implement, a quick win, and it
removes a lot of headache.

**Detection and response.** A SIEM, either in-house or through an MSSP — probably
an MSSP, because hiring security professionals will be difficult for Oscorp. And
cyber security incident response plans.

The closing note is honest: almost none of this is easy. A few items are quick
wins; most are substantial programmes of work requiring real time and money.
Which is precisely why hiring the right people comes first.

## How my recommendations compared

The substance matched closely — governance and a named security leader, asset
management, TPRM, a cyber risk process, MFA as the urgent item, least privilege
and access reviews, eliminating shared admin credentials, periodic training with
phishing simulation, data classification with labelling and DLP, and SIEM via
MSSP with incident response plans.

**What I'd already conceded, and now see the full reasoning for:** the internal
audit programme with cyber in scope, and explicitly endorsing the risk process
through the audit and risk committee and the *existing* risk team rather than
standing up a parallel one. Both are third-line and governance-integration points
I under-weighted.

**What I'd add to my roadmap after this:** blocking USB drives as a named quick
win. I recorded removable media as a finding but never surfaced it as an action,
and it belongs in the ninety-day list next to MFA — cheap, fast, and it closes a
real exfiltration path for research data.

**One place I'd hold my sequencing.** The solution deprioritises awareness
training given everything else that's wrong. That's reasonable on attention
grounds, but I put it in year 1 for two reasons. The quantification in module 11
put it at roughly €107,000 net annual benefit with break-even at an 18% reduction
— a stronger case than most things competing for the same year. And it draws on
different people: awareness runs through HR and communications, so it doesn't
consume the new security leader's bandwidth the way the governance and IAM
programmes will. Deprioritising by severity alone ignores that some work runs in
parallel for free.

**What my answer had that the solution doesn't.** A three-year sequence with
dependencies and exit criteria — the brief asked for a roadmap, and the solution
gives prioritised areas without phasing. The reporting-line independence finding.
Regulatory applicability as an explicit task. Vulnerability management SLAs and
backlog burn-down, PAM, an IR retainer, penetration testing, metrics.

## My take

The advisory-versus-audit distinction is the thing I'd most want to remember,
because it's the kind of error that is invisible until someone senior notices it.
I checked my own deliverable — I used "assessment" and "assessed against"
throughout and never called it an audit, which was luck as much as judgement. Now
I know why it matters.

The second is the baseline argument for the spreadsheet. I'd been treating the
completed assessment as evidence for the recommendations. It's also the
measurement instrument: the same 98 controls re-scored in twelve months is the
only objective way to show whether a three-year programme is actually working.
That reframes it from working paper to deliverable, and it's why my year 3
"annual reassessment against this framework" line matters more than it looked
when I wrote it.

The third is the honest closing note, which I think is the most professionally
mature thing in the walkthrough: almost none of this is easy, most of it is
expensive, and a consultant who presents a roadmap as though it were a checklist
is setting the client up to fail. Saying plainly which items are quick wins and
which are multi-quarter programmes with real cost is what makes the rest of the
advice believable.
