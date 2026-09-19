# Phishing

> Module 06, lesson 2. The most common attack, and the stack of controls that
> stands between it and an incident.

## Summary

Phishing remains the most common type of cyber attack. An attacker sends a
fraudulent email or SMS impersonating your bank, a government body, or sometimes a
friend or family member. The message asks for money, tells you to change your
banking password, or directs you to click a link — and that link leads to a page
where you enter a username and password, bank details or card information.

Defending against it is defence in depth applied to one attack path. Each layer
catches what the previous one missed:

1. **Email gateway.** Filters messages carrying malware or ransomware. Not
   infallible — something new in the wild may be unknown to the gateway and pass
   through.
2. **Anti-malware.** May detect what the gateway didn't, on the endpoint.
3. **Security operations centre.** If malware does land and starts copying files
   or reaching out to a command-and-control server, that behaviour is what analysts
   are watching for. Detection moves from *recognising the file* to *recognising
   what it does*.
4. **Education and awareness.** Teaching people to spot phishing emails, not click
   malicious links, and not enter credentials into fraudulent pages. It genuinely
   reduces the likelihood of a phish succeeding, which is why it belongs in every
   security programme.

For a GRC professional, this arrives as two tasks: **assessing the effectiveness**
of an awareness programme, and **improving** one.

## The layers, and what each one can and can't do

| Layer | Catches | Misses |
| --- | --- | --- |
| Email gateway | Known malicious attachments, links and senders; bulk campaigns | Novel payloads; messages with no attachment or malicious link at all |
| Anti-malware | Known malware on the endpoint | Anything new, and attacks that never drop a file |
| Security operations | Behaviour after compromise — file access, command-and-control traffic | Nothing, if the activity resembles normal use |
| People | The message that looks wrong to a human | Whatever looks convincing |

The pattern worth noticing: the first two layers ask *is this thing known to be
bad*, the third asks *is this behaviour wrong*, and the fourth asks *does this
message make sense*. Three different questions, which is why the layers genuinely
add up rather than duplicating each other.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Phishing | Fraudulent messages impersonating a trusted party to extract money or credentials | The most common attack, and usually the first move in a larger one |
| Smishing | The same attack delivered by SMS | Outside the email gateway entirely — no filter sits in front of it |
| Credential harvesting page | A fake login page capturing what's typed into it | No malware involved, so file-based defences never engage |
| Email gateway | Filtering at the boundary before delivery | Removes the bulk of commodity attacks |
| Behavioural detection | Spotting what malware does rather than what it is | The layer that catches the genuinely new |
| Command and control | Malware contacting the attacker's infrastructure | A detectable signature of compromise after the fact |
| Awareness as a layer | People trained to recognise and not act on phishing | Reduces likelihood; doesn't eliminate it |
| Assessing effectiveness | Judging whether an awareness programme works | The GRC task, and harder than it sounds |

## Where this shows up in a real job

The WordPress ecosystem generates a constant supply of these. Fake plugin update
notices, messages claiming a site has been suspended, forged invoices from a host.
The craft is often poor and the success rate is still not zero, which is the
economics the lesson describes — volume makes a low hit rate sufficient.

Support is also where the layers become visible from underneath. When someone
forwards a suspicious message and asks whether it's real, that person is the fourth
layer working. Whether they're thanked or brushed off determines whether the layer
still exists next month.

I've never run an awareness programme or administered a simulation platform, which
matters because the next lessons are about measuring and improving them. I'd be
assessing from principles rather than from having operated one.

## My take

The layer that fails most quietly is the credential harvesting page, and it's
worth separating from "phishing" generally. A message with no attachment, no
malicious link signature and a convincing login page carries nothing for the
gateway or anti-malware to detect. There is no file, so the behavioural layer has
nothing to observe until the stolen credentials are used somewhere. Between the
click and the login, the only control operating is the person. That's the specific
case where awareness isn't one layer among four — it's the only one in play, which
is a much stronger argument for the programme than "people make mistakes."

Two things:

**SMS sits outside the stack almost entirely.** The lesson mentions fraudulent SMS
in the same breath as email and then describes a defence chain that begins with an
email gateway. Nothing equivalent filters a text message to a personal phone, no
endpoint agent inspects it, and the SOC has no visibility of it. An organisation
with excellent email security can be phished through a channel it cannot see at
all — which is why the reporting mechanism matters more there than anywhere, and
why "how would someone report a suspicious text" is a good assessment question.

**Detection and reporting close the gap the other layers leave.** Awareness is
usually framed as prevention — don't click. Prevention is the weaker half. The
person who clicked and immediately says so gives the organisation minutes rather
than weeks, and that interval decides whether a credential gets used before it's
reset. A programme measured only on how few people clicked is measuring the half it
can't win, which is worth remembering when the module reaches measurement.

One connection back: if phishing is the usual way in, and the objective is
credentials, then what happens *after* a successful phish is decided by module 5.
Phishing-resistant MFA, least privilege, and monitoring determine whether stolen
credentials achieve anything. The awareness programme reduces how often the attempt
works; the identity controls decide what it's worth when it does.
