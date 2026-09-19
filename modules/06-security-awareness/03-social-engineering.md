# Social engineering

> Module 06, lesson 3. Attacking the person rather than the system, and the
> techniques that keep working.

## Summary

Social engineering is psychological manipulation used to get people to reveal
sensitive information or take actions that compromise security — clicking a link,
entering credentials into a fraudulent page. The attacker typically poses as
someone the target trusts: a friend, their bank, a company, a government agency.

The techniques the lesson covers:

**Email and SMS.** Phishing by email, and text messages carrying links that deliver
mobile malware or lead to a page harvesting card details. These scams cost people
millions every month.

**Urgency.** The most reliably effective device, because it works. "Your credit
card has been stolen, call us immediately" or "enter your details now" pushes the
target to act before thinking. Simple, and extremely effective.

**Baiting.** Leaving something the target will pick up. The lesson's worked
example: helping a mature organisation extend its awareness programme by loading
fake malware onto USB drives and scattering them in the company car park before
anyone arrived. A large number of employees plugged them into work laptops without
hesitating — it looked like a freebie, or curiosity won. Those drives could have
carried ransomware capable of shutting the organisation down.

**Physical impersonation.** Dressing as tradespeople, carrying a ladder, arriving
to "fix the air conditioning". Once inside the building, USB devices or other
malicious hardware can be planted. Simple, and effective.

**Phone calls.** Still working. Calling a receptionist or a personal assistant:
"your boss is trying to make a payment, it's failed several times, we need the card
details urgently." One of the most effective forms of social engineering there is.

**The defence.** There is no easy safeguard other than education and awareness.
Users have to be told repeatedly about the dangers, how not to fall for phishing,
how to stay alert to scam SMS. Which is why security education and awareness
remains one of the most important parts of cyber security.

## Techniques at a glance

| Technique | How it arrives | Why it works |
| --- | --- | --- |
| Phishing | Email | Volume; a small success rate is enough |
| Smishing | SMS | No filtering layer; personal devices; short messages carry fewer tells |
| Urgency | Any channel | Time pressure suppresses the checking someone would otherwise do |
| Baiting | Physical media, or an offer too good to ignore | Curiosity, and the appearance of a free thing |
| Impersonation | In person, with props and a plausible errand | People don't challenge someone who looks like they belong |
| Vishing | Phone call | Real-time pressure, no written record, and a helpful person on the line |

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Social engineering | Manipulating people rather than exploiting technology | Bypasses technical controls entirely |
| Pretexting | The invented story that makes the request plausible | The scenario is the payload, not the link |
| Urgency | Manufactured time pressure | Removes the pause where someone would verify |
| Baiting | Planting something a target will pick up and use | Turns curiosity into initial access |
| Tailgating and impersonation | Physical entry using a convincing role | Puts an attacker inside the network perimeter |
| Vishing | Voice-based social engineering | Highly effective against helpful, customer-facing staff |
| Awareness as the primary control | Training is the main defence available | True as far as it goes — see below |

## Where this shows up in a real job

Support roles are the natural target for the phone and email versions, because the
job is to be helpful to people who can't prove who they are. Every request to reset
access, confirm an account detail or make an exception is, structurally, the same
request a social engineer makes. The difference between a good day and an incident
is whether there's a verification step that doesn't depend on how convincing the
person sounds.

The urgency device is the one I recognise most. Genuine urgency exists constantly
in support, so a manufactured version doesn't stand out — it blends into the
background rate of real emergencies. That's uncomfortable and worth naming: the
tell that works in a training deck is much weaker in a queue where everything is
urgent.

I haven't run a simulated baiting exercise or a physical social engineering test.
I've read about them and now seen one described; that's not the same as having
planned one, and the planning is where the consent and safety questions live.

## My take

The USB exercise is a good illustration and the story it tells is slightly
different from the one intended. Employees plugged in an unknown drive because
curiosity is normal and nothing stopped them. The awareness conclusion is *teach
people not to*. The engineering conclusion is *why did the laptop execute it* —
device control policies can block unknown removable media outright, and where
that's configured the exercise measures nothing about the employees. That's worth
separating in an assessment: a baiting test with no device control in place is
measuring a gap in configuration as though it were a gap in training.

Two things:

**"Awareness is the only defence" is the one claim I'd qualify.** It's true that no
technical control stops someone being manipulated, and false that awareness is
therefore all you have. Verification procedures are the real control: a rule that
payment details are never changed on a phone call, that a card change requires
callback on a number already held, that visitors are escorted regardless of what
they're carrying. Those work whether or not the person on the phone has had
training this year, because they remove the judgement call. Awareness teaches
people to be suspicious; process means they don't have to be right.

That reframing also answers the receptionist example. The receptionist shouldn't be
expected to detect a convincing fraud — they should have a procedure that makes the
answer "I can't do that over the phone" for everyone, every time, with no
discretion to exercise and no need to be confrontational about it.

**Urgency is the tell to teach, because it's the one constant.** The channels vary
and the pretexts change; the compressed timeline is present in almost every case,
because thinking time is what the attacker cannot afford to give. "Anything urgent
is worth one minute of verification" is a rule that survives new attack formats in
a way that "check the sender address" does not.

One ethical note on baiting exercises, which the lesson doesn't raise: these tests
are performed on people, and how the results are used determines whether they
improve anything. A run that identifies individuals for sanction produces a
workforce that hides mistakes; a run reported as an aggregate figure with a
follow-up briefing produces a workforce that reports them. The exercise design and
the data handling are as much part of the control as the test itself — and that,
rather than the trick, is the part a GRC professional actually owns.
