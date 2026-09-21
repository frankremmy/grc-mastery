# What is third-party risk management?

> Module 09, lesson 1. _Why a company's security depends on the security of
> companies it doesn't control._

## Summary

Third-party risk management is the work of managing the cyber security risk that
comes from suppliers, vendors and external service providers. The name changes
depending on where you work — supplier risk management, vendor risk management,
supply chain security — but it is the same discipline. Every organisation has
third parties. The laptops run someone else's operating system, the website was
built by an agency, the payroll runs on a platform nobody in the building owns.
Each of those is a company whose security posture your organisation inherits
without having any authority over it.

The point I had to sit with is *which* security you are assessing. When I first
heard "assess the web agency's security" I assumed it meant how securely they
built the site. That matters, but it isn't TPRM. TPRM asks how that agency runs
security **inside its own business** — whether they patch, whether staff use MFA,
whether they have anywhere near a process for disposing of client data. That
question matters for two separate reasons. First, residual data: during the
project I hand them things about my company, and a firm with weak internal
security is both more likely to be breached and more likely to still be holding
material it should have destroyed. Second, standing access: if there's a
maintenance contract, that supplier has credentials into my environment, and
their compromise becomes my intrusion. The Target breach is the standing example
— the attackers didn't start at Target, they started at a heating and air
conditioning contractor and moved from there.

The lesson also raises a reason that gets skipped in security-led TPRM: the risk
of doing business with a company you shouldn't be doing business with at all.
Sanctions exposure, money laundering, forced labour in the supply chain. That is
due diligence rather than cyber security, and it lands on the organisation as
legal and reputational risk regardless of whether the supplier's firewall is any
good. Worth knowing it exists on the same assessment, even where a different team
owns it.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Third party | Any external organisation supplying a product or service — software vendor, agency, contractor, cloud provider | The definition is broader than most people assume; the facilities contractor counts |
| TPRM | Managing the cyber risk that third parties introduce | Risk you carry but don't control — you can only assess, contract and monitor |
| Internal vs delivered security | How the supplier secures *their own* business, as distinct from how securely they build *your* thing | This is the distinction that defines the discipline; both matter, only one is TPRM |
| Residual data | Information about you the supplier still holds after the work ends | Breach of a former supplier can still be your incident |
| Supplier access | Credentials or connectivity granted to a third party | Turns their compromise into your entry point |
| Supply chain attack | Reaching a target by compromising something it trusts | Target, and most of the high-profile breaches since |
| Due diligence | Checking a supplier isn't engaged in illegal or unethical activity | Sanctions, money laundering, forced labour — legal exposure, not technical |

## Where this shows up in a real job

The honest version of this for me is that I have mostly been on the *other* side
of it. At Automattic I was a support engineer with access to customers'
WordPress.com and WooCommerce sites. To every one of those customers, Automattic
was the third party, and I was the access path — exactly the standing-access risk
this lesson describes. Nobody framed it to me that way at the time. The controls
around it were real enough (the access model, the logging, the training), but I
experienced them as workflow rather than as somebody else's risk treatment. Being
able to see that from both directions is the useful part: I know what a supplier's
access to a customer environment actually looks like day to day, which is the
thing a questionnaire is trying to find out and usually doesn't.

It also means I have a realistic view of what a supplier can honestly answer. A
support engineer does not know the retention schedule for the data they touch.
That is worth remembering before writing an assessment that assumes the person
filling it in has the answers.

## My take

The part I want to hold onto is that TPRM is an authority problem more than a
technical one. Every other control I've studied in this course is something the
organisation can implement directly — configure the MFA, write the policy, run
the awareness programme. Here you can't. You can ask, you can contract, and you
can walk away, and that's the whole toolkit. Which is why the assessment happens
*before* signing, and why contract terms carry so much of the weight — once the
supplier is embedded and holding data, leverage is mostly gone.

The second thing: the boundary of "third party" is drawn too narrowly by
instinct. It's easy to list the SaaS platforms and stop. The Target lesson isn't
"check your vendors", it's that the attacker went looking for the supplier
*nobody was thinking about* — the one with network access and no reason for anyone
to consider it a security-relevant relationship. The discovery problem comes
before the assessment problem, which I'd guess is where the next lesson goes.
