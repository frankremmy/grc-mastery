# IAM recommendations — Oscorp formula database

**Module:** 05 — Identity and Access Management
**Type:** Practical assessment
**Status:** My own answer, written before seeing the course solution.
**Role:** External cyber security consultant advising Oscorp.

---

## Situation

Oscorp's medication has launched successfully and the formula remains secret. It
is the organisation's most sensitive asset. Supporting documentation is held in a
Microsoft SQL Server 2022 database.

The assessment found:

- Any employee who is a member of the research lab has read access to the formula.
- Harry Osborn has full administrative access to the database.
- Employees authenticate to the database with a username and password.

---

## My answer (as submitted)

Since the medication formula is Oscorp's most sensitive asset, access to the SQL
Server database should follow the principles of least privilege and need-to-know.
Being a member of the research lab alone should not automatically provide access to
the formula.

First, Oscorp should implement Role-Based Access Control (RBAC). Specific roles
should be created based on job responsibilities, and only employees who genuinely
require the formula to perform their duties should receive read access. Access
requests should require approval from the appropriate data or business owner.

Harry Osborn's full administrator access should also be reviewed. If database
administration is not part of his responsibilities, his admin privileges should be
removed. Administrative access should be restricted to authorised database
administrators and provided only when required. Privileged accounts should also be
separate from normal user accounts.

Oscorp should strengthen authentication by introducing Multi-Factor Authentication
(MFA), particularly for privileged and sensitive database access. Password policies
should require strong passwords, and shared accounts should be prohibited so that
activity can be traced back to an individual.

A formal joiner, mover and leaver process should also be established. New employees
should receive only approved access, access should be adjusted when employees
change roles, and accounts should be promptly disabled when employees leave Oscorp.

Access to the formula should be logged and monitored. Oscorp should record
successful and failed login attempts, privileged activities and access to sensitive
information. Unusual or unauthorised activity should generate alerts for
investigation.

Finally, access rights should be reviewed periodically, for example quarterly, by
the asset owner and IT/security team. Unnecessary, excessive or unused privileges
should be removed.

These controls would reduce the risk of unauthorised access while ensuring that
only appropriately authorised employees can access Oscorp's secret formula.

---

## Additions on review

### 1. The authentication method is the blocker, and it has to change first

"Employees can log in using a username and a password" describes **SQL Server
authentication** — logins created and held inside the database engine itself,
outside Active Directory or Entra ID.

That single fact undermines several of my own recommendations, because those
accounts sit outside every identity process Oscorp might build:

- They can't carry MFA. SQL Server authentication has no second factor.
- They aren't covered by the joiner-mover-leaver process, because the directory
  doesn't know they exist. A leaver can be disabled in Entra ID and still hold a
  working database login.
- They don't inherit password policy, conditional access, or sign-in risk
  detection.
- They're commonly shared, because creating one is quicker than requesting a
  directory account.

So the first recommendation should be to **migrate to Microsoft Entra ID
authentication** (or Windows authentication for on-premises), disable SQL Server
authentication logins, and grant access through directory groups. Everything else —
MFA, JML, conditional access, centralised review — becomes possible once
identities live in the directory, and remains partly theoretical while they don't.

This is the technically decisive recommendation and I had the right controls
without the enabler underneath them.

### 2. Separate the data owner role from the database administrator role

My answer says to review Harry's admin access, which is right but soft on the
reasoning. Harry is the Chief Scientist. Database administration is not his job,
and there is no scientific task that requires the ability to alter schemas, change
permissions or drop tables.

The stronger framing: Harry should be the **data owner** — the person who approves
who may access the formula and who attests to the access list quarterly — and hold
**no technical administrative rights at all**. Those two roles being separate is
separation of duties applied to the crown jewel.

Framing it this way also answers the political objection before it's raised.
Removing Harry's admin rights doesn't reduce his authority over the formula; it
increases it, because approving access becomes a documented decision he makes
rather than something anyone with the admin account can do silently.

### 3. Non-human identities

My answer addressed employees and said nothing about applications. A SQL Server
database in production is almost certainly accessed by service accounts —
applications, reporting tools, backup jobs, ETL processes — and those accounts
typically hold broad standing privilege, have passwords that never rotate because
something would break, and belong to nobody in particular.

Every recommendation needs to cover them explicitly: enumerate the service
accounts, assign each a named human owner, grant each the minimum rights its
function requires, store credentials in a vault rather than in configuration files
or connection strings, and include them in the quarterly review.

### 4. Revoke what exists, don't only design what should exist

I described the target model without saying what happens to the current grants.
Designing better roles while leaving the research lab group's read access in place
changes nothing — it just adds a better model alongside the old one.

The sequence should be explicit: identify everyone with current access, require
the data owner to re-approve each individually against need-to-know, and **revoke
by default** anything not re-approved within a set period. Grandfathered access is
how these exercises quietly fail.

### 5. Name the privileged access model

My answer said admin access should be "provided only when required", which is the
right instinct without the mechanism. What the module describes is **just-in-time
privileged access**: no standing administrative accounts, credentials held in a
vault, access requested and approved, granted for a bounded period, and every
session recorded.

With that comes the requirement for a documented **break-glass account** —
emergency access that bypasses the normal path, held securely, alarmed on use, and
reviewed after every activation. Introducing MFA and vaulting without an emergency
route is how organisations lock themselves out of their own systems.

### 6. Monitoring needs a recipient and independence

I said alerts should be generated for investigation without saying who receives
them. Two points worth adding: alerts must route to a named function with a
response expectation, and **privileged activity should not be reviewed solely by
the people performing it**. Database administrators reviewing their own audit logs
is self-assessment, which module 3 covers well.

Specific to this asset: bulk reads of the formula tables — large result sets,
exports, unusual query volumes — deserve their own alert, because read access
already permits copying the entire formula. Legitimate read access and
exfiltration look identical unless volume is being watched.

---

## Comparing against the course solution

The solution recommends: enterprise-wide two-factor authentication, plus an
**additional** factor specifically to reach the database (biometric was the
example), and an approval process for access requests. Least privilege via RBAC,
with the formula role **assigned temporarily for the duration of the need and
revoked when the task is complete**. Separation of duties for Harry — a read-only
account for daily work and a separate admin account for write access, with
**formal approval from two executives** to obtain temporary admin access. And
regular user access reviews.

### What the solution had that I didn't

**Layered authentication at the asset.** I recommended MFA; the solution
recommends MFA to enter the environment *and a further factor at the database
itself*. That's defence in depth applied to authentication — the crown jewel gets
its own gate rather than inheriting the perimeter's. It's a better answer than
mine, and it's the kind of step-up control that distinguishes a sensitive asset
from an ordinary one.

**Time-bound access for ordinary users, not just administrators.** I applied
just-in-time thinking to admin rights. The solution applies it to the read role:
the formula role is granted for the duration of a task and revoked afterwards.
That's stronger and less obvious, and it changes the question from *who should
have access* to *who needs access right now* — which is the more defensible
position for an asset like this.

**Dual approval by two executives.** I said approval by the data or business
owner. The solution requires two executives for admin access, which is genuine
dual control — one compromised or coerced approver isn't enough. Worth adopting as
the pattern for the highest-value privilege.

### What I had that the solution didn't

**Logging and monitoring.** The solution doesn't mention it at all. Access control
decides who may read the formula; logging is the only way to know who did. For an
asset where read access is indistinguishable from theft, that gap is significant.

**Joiner–mover–leaver.** Without it, every access decision decays. The solution's
temporary-role model reduces the exposure, but permanent accounts still need a
lifecycle.

**Prohibiting shared accounts and requiring traceability**, password policy, and
removal of unused privileges during review.

Plus the additions above: moving off SQL Server authentication, service accounts,
revoking existing grants rather than only designing new roles, and a break-glass
procedure.

### One note on the biometric suggestion

Biometrics at a database is unusual in practice. The biometric normally unlocks a
credential held on a device rather than authenticating to a server directly, so
the implementable version is a phishing-resistant hardware key or a conditional
access policy requiring a compliant device and a strong factor for that resource.
The principle — a distinct, stronger factor for the crown jewel — is right; the
mechanism would more likely be a security key than a fingerprint reader wired to
SQL Server.

---

## Out of scope, flagged rather than assessed

The question asks for IAM recommendations, so this is deliberately excluded — but
identity controls alone don't protect the formula. Encryption at rest and in
transit, restricting which hosts can reach the database, backup security (a backup
of this database is the formula, with none of the access controls), and data loss
prevention on egress paths all bear on the same asset. Worth raising with Oscorp
as adjacent work rather than leaving the impression that access control is
sufficient on its own.

Read access also cannot be undone. Anyone who has already read the formula holds
it, and no future control retrieves it — so the current access list is also a list
of people who may already have the crown jewel, which is a risk to record rather
than a control to implement.
