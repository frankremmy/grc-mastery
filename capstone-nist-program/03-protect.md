# Protect — solution walkthrough

> Capstone, lesson 3. _The longest function, and the one where scoring judgement
> matters most._

## Summary

Protect is the largest function and spans access control, awareness and training,
data security, information protection processes, maintenance, and protective
technology — five of this course's modules in one tab.

A point the walkthrough opens with and that applies throughout: **the control
descriptions are deliberately broad**, because the framework has to serve
organisations of every kind. The questions column offers several ways into each
control, and not all of them apply to every organisation. Reading the control
generously and the questions selectively is the intended approach.

### Access control

**Identities and credentials managed — Fail.** Active Directory provides a
username and password to get onto the network, and after that almost nothing
manages authorisation. Access is granted to whoever asks; there is no approval
step. Add no two-factor authentication. Worth noting the framing: 2FA is not
strictly mandated by NIST, but it has become a de facto standard and running a
business without it is indefensible.

**Physical access — Pass.** A general observation here: organisations tend to do
well on this control almost by default, because leased office space comes with
physical security built in.

**Remote access — Fail.** A VPN alone used to be an acceptable answer. It isn't
now, because once credentials get you onto the network you reach everything,
there is no 2FA, and nothing has been said about how contractors and third-party
providers connect. In a live engagement this is where you probe — ask them to
walk you through how a contractor is granted access.

**Least privilege and separation of duties — Fail.** **Network segregation —
Pass**, via VLANs; traditional network teams generally handle this well.

### Awareness and training

**All users informed and trained — Pass**, with improvement notes in the
comments. Oscorp mandates the induction module, so the control is met; the
comment records that training should happen at least every 12 months and that
simulated phishing would improve it.

The walkthrough makes the method point explicitly here: **pass and fail are not
black and white.** You can pass a control and still record opportunities for
improvement, and the recommendations that follow are prioritised by what matters
most to the organisation. Flexibility in scoring is intended, not sloppy.

**Privileged users understand roles — Fail.** Shared admin passwords and no means
of managing privileged access.

**Senior executives understand roles — Fail**, and this is the subtle one. Board
members are generally *not employees*. They don't get company accounts, they
aren't onboarded, and so they never get auto-assigned the security training that
staff receive. The fix is an information security policy that defines board
roles and responsibilities, plus mandated training specifically for them. This is
a real-world pattern I hadn't encountered.

**Physical and information security personnel understand roles — Pass.**

### Data security

**Data at rest — Fail.** Office 365 and the Microsoft cloud encrypt by default,
so the encryption element is satisfied — and **encryption alone is not
sufficient**. Without classification and labelling, nobody knows what should be
protected or who should reach it; with no DLP and no access management, the
environment is effectively open to anyone with a login. Protecting data at rest
properly means classifying it first, then applying specific controls to the
sensitive subset: dedicated permissions, user groups, or separate encryption keys.

**Data in transit — Fail**, for the same reason. Encrypted by default, but with
nothing classified there is no way to know what needs protecting.

**Removal, transfer and disposition — Fail.** The current-state document doesn't
say Oscorp fails to dispose of data, but it follows from the absence of
classification: if you have not identified sensitive data, you cannot be managing
its disposal. Reasoning from a known absence to a dependent one is legitimate
here.

**Capacity and availability — Pass.** Modern platforms are highly available by
default, business continuity is documented, and denial-of-service protection is
straightforward at the network layer.

**Data leak protection — Fail.** No DLP. **Integrity checking — Pass**, treated as
an outdated control that modern systems implement inherently. **Dev/test separate
from production — N/A**, since Oscorp writes no software.

### Information protection processes and procedures

The shortcut the walkthrough offers: Oscorp has no security team, only IT
operations, so documented security processes broadly don't exist.

**Baseline configuration — Pass**, the SOE image used for all laptops.
**SDLC — N/A.** **Change control — Fail**, tied to the same absence of an approval
process that lets anyone request and receive access. **Backups — Pass**, taken
regularly and tested. **Physical environment policy — Pass.** **Data destruction
— Fail.** **Continuous improvement — Fail**, since there are no protection
processes to improve. **Sharing effectiveness with peers — Fail**, no security
team to do it.

**Response and recovery plans — Fail.** Oscorp has business continuity and
disaster recovery; an incident response plan is a *different document* with a
different purpose. **Plans tested — Fail**, because the IR plan doesn't exist to
be tested.

**Cyber security in HR practices — Pass**, on the strength of background checks.
**Vulnerability management plan — Fail**; owning a scanner is not a programme.

### Maintenance and protective technology

**Both maintenance controls — N/A.** Oscorp has no hardware estate beyond
laptops.

**Audit logs — Fail.** No SIEM and no security team, so nobody reviews logs.
**Removable media — Fail**, USB use is unrestricted. **Least functionality —
Pass**; note this is *not* least privilege — it means one service per system
rather than email, FTP and DNS on the same box, and SaaS and cloud deliver it by
default. **Communications protected — Pass**, encrypted by default.

## Where my assessment diverged

I scored 9 genuine passes plus 4 N/A against the solution's 12 passes plus 4 N/A.
Three controls where they passed and I failed:

| Control | Their reasoning | My read now |
| --- | --- | --- |
| PR.AT-1 all users informed and trained | Training is mandated; improvements go in the comments | **Conceded.** See below |
| PR.AT-5 security personnel understand roles | Physical security is mature | Largely conceded, with a caveat |
| PR.IP-11 cyber in HR practices | Background checks are explicitly stated | Conceded — I failed it on an unevidenced sub-part |

**On awareness training I've changed my position.** I argued for keeping the Fail
because module 6 of this course spent a lesson establishing that onboarding-only
training is inadequate. That argument was about emphasis, not scoring, and it
assumed a Pass would lose the finding. It doesn't — the comment carries it, and
the solution's recommendations do call for annual training and simulated
phishing. The substantive outcome is identical either way, and the Pass preserves
the information that Oscorp has *something*. The Fail bought nothing.

**On PR.AT-5 a small caveat stands.** The control covers physical *and*
information security personnel. Physical security staff clearly know their roles;
information security roles are explicitly undefined at Oscorp. Passing on the
strength of one half is the same partial-credit judgement being applied, so I
don't object to the verdict — but it's worth noticing that the control is doing
double duty.

**One observation about assumptions.** The solution asserts denial-of-service
protection under capacity and availability, and states that USB drives are
allowed under removable media. Neither appears in the current-state document —
both are reasonable inferences, exactly the kind the exercise invites. I reached
similar conclusions and labelled mine ASSUMPTION in the comments. That habit came
from the earlier modules and I'd keep it: in a real report, the reader needs to
know which lines are evidence and which are inference, because only the inferences
need confirming with the client.

## My take

The most useful new thing in this walkthrough is the board training point. It's
the sort of detail that only comes from having run these assessments — board
members sit outside the employee lifecycle entirely, so every control that relies
on onboarding silently skips the people with the most authority. The remedy is
governance rather than technology: name their responsibilities in the information
security policy and mandate training for them separately. I'd never have found
that by reasoning from the framework.

The second is the reminder on encryption. "Data is encrypted at rest" is the
answer that sounds like a pass and frequently isn't, because encryption at the
platform layer protects against the wrong threat. It defends a stolen disk; it
does nothing against an authenticated user who should never have been able to
open the file. That's the same argument I made about Horizon Labs in module 9,
and seeing it restated as a scoring judgement here is a good confirmation that
the instinct was right.

The third is a small vocabulary trap worth keeping: **least functionality is not
least privilege.** One is about how many jobs a system does; the other is about
how much access a person has. They sound alike and mean different things.
