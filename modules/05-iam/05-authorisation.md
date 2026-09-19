# Authorisation

> Module 05, lesson 5. Once the system knows who you are, deciding what you're
> allowed to do.

## Summary

Authorisation determines whether a user or device may access a resource,
application or system — and whether they may perform a particular action.

The employee example carries both halves. Logging in, you see your own inbox, the
applications your job requires, and your own salary, sick leave and holiday
entitlement. Try to view another employee's salary and access is blocked: you're
not authorised to see it. Try to delete your own salary record and that's blocked
too — an action you're not permitted to perform even on data you're permitted to
see. Resource *and* action.

Two mechanisms matter.

**Access control lists (ACLs).** Old, still widely used, and effective. You build
a list and grant access to what's on it — take every employee in the accounting
department and permit only those usernames to reach the accounting application.
Network engineers use them constantly, grouping IP addresses to permit or block
traffic. ACLs are essentially binary: on the list or not, access or no access.
Rudimentary, and it works.

**Role-based access control (RBAC).** More sophisticated: access is granted
according to the role a person performs. Return to the accounting list — if every
name on it has full control, every accountant can read financial data *and* delete
complete financial records. Some may need that; a junior accountant probably
shouldn't have it. So you create two roles, senior and junior accountant, and grant
different access and different permitted actions to each.

RBAC is how the principles from the OWASP lesson get implemented:

- **Least privilege** — each person receives the minimum access needed for their
  task, and no more.
- **Separation of duties** — one group of accountants can read financial data,
  another can write and modify it. No individual or group holds more than they
  should, which reduces the attack surface and limits the impact of any single
  compromised account, because a privileged action requires more than one person.

**The assessment questions.** Whether assessing a whole organisation or a single
application: Do you implement least privilege, and how? How is access assigned —
ACLs or RBAC? How many users hold admin access, and has that access been
compartmentalised? Is separation of duties in place?

In practice the answer to "is least privilege followed" is frequently no,
because developers and companies are rushing to get things into production. The
recommendation is to step back and implement role-based access so that different
users hold genuinely different access — which pays off over time in fewer
incidents and less remediation.

## ACL and RBAC compared

| | Access control list | Role-based access control |
| --- | --- | --- |
| Grants access to | Named identities or addresses | Roles, which people are assigned to |
| Granularity | Typically binary — permitted or not | Access *and* permitted actions per role |
| Maintenance | Edit the list as people change | Change the person's role; permissions follow |
| Suits | Network rules, simple resource gating | Applications with varied duties and seniority |
| Supports least privilege | Weakly — access tends to be all or nothing | Directly — roles are defined by what a job needs |
| Supports separation of duties | Not really | Yes — read and write can be separate roles |

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Authorisation | Deciding what an authenticated identity may access and do | The second half of IAM; authentication alone grants nothing safely |
| Resource vs action | What you can reach, and what you can do to it | Read, modify and delete are different permissions on the same data |
| ACL | A list of identities granted access to something | Simple, binary, and still everywhere |
| RBAC | Access granted by role rather than by individual | Scales with people changing jobs; the practical route to least privilege |
| Least privilege | Minimum access needed for the task | Caps the damage a compromised account can do |
| Separation of duties | Splitting a privileged capability across people | Requires collusion rather than a single compromise |
| Admin count | How many users hold administrative access | One of the fastest signals of how well access is managed |

## Where this shows up in a real job

WordPress ships with RBAC and demonstrates both the value and the failure mode.
Administrator, editor, author and contributor are genuinely different roles with
different capabilities — and a large share of sites give everyone administrator
because it's the role that definitely works. The junior accountant with delete
rights is the same problem with different labels.

The rushing-to-production observation matches what I see in support. Access design
is deferred during a build because it isn't what gets a launch over the line, and
retrofitting it afterwards is harder — people are already working with the access
they were given, and taking it away is a conversation rather than a configuration
change.

Building Active Directory in the lab made group-based access concrete rather than
theoretical, which helps. What it doesn't teach is what happens when the role model
meets an organisation where nobody's job matches the roles that were defined.

## My take

The distinction I'll keep is that **authorisation covers actions, not just
resources**. It's easy to think about access as a list of systems someone can
reach, and the salary example makes the finer point — you may view your own record
and still be forbidden from deleting it. A model that only answers "can this person
open this application" has answered the easier half of the question, and the
destructive actions live in the half it skipped.

Three things:

**ACLs and RBAC aren't really rivals, and describing them as a progression
oversimplifies.** ACLs are the right tool where the decision genuinely is binary —
network traffic, file shares, simple resource gating. RBAC is the right tool where
the same population needs different capabilities within one system. Most
organisations run both, and an assessment should ask which is used where rather
than treating ACLs as an outdated thing to be replaced.

**RBAC's real difficulty is role design, not implementation.** Defining two roles
for accountants is easy. Real organisations end up with hundreds of roles, or three
roles that fit nobody, and then exceptions attached to individuals — at which point
you have an ACL again with extra steps. The questions that find this are "how many
roles exist", "when was the role model last reviewed", and "how many users have
permissions outside their role". That last one is where the truth is.

**Privilege accumulates through role changes, and no single decision causes it.**
Someone moves from junior to senior accountant and gains the senior role; they
rarely lose the junior one. Do that across a career and you get people whose access
reflects their employment history rather than their job. Least privilege isn't only
about what you grant — it's about what you remove, which is why access
recertification and a joiner-mover-leaver process are the controls that actually
keep it true.

The admin-count question is the one I'd lead with in an assessment. It's a single
number, the organisation can usually produce it, and it's immediately comparable
against the headcount. A number far larger than expected tells you the role model
isn't holding, before you've looked at a single configuration.
