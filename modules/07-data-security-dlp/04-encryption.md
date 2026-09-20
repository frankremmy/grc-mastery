# Encryption in the real world

> Module 07, lesson 4. What a GRC professional actually needs to know about
> encryption — and what's a distraction.

## Summary

The lesson opens by narrowing the subject deliberately. Security professionals
don't design encryption algorithms and don't write encryption software. Plenty of
training takes you into the mathematics behind each algorithm, and that knowledge
doesn't make you better at this job.

**What encryption is:** scrambling data so it isn't readable without the key,
performed by an algorithm — a mathematical formula that makes the data readable
only to a key holder. Digital signatures and hashes sit under the same broad
umbrella, worth knowing by definition rather than in depth.

**What the GRC role actually involves.** When assessing an application, check
whether the data is encrypted. The sequence:

1. Understand the data in the application — is it classified, is it labelled?
2. Check what the information security policy requires. If sensitive data must be
   encrypted, and this data is sensitive, then encryption is required.
3. Ask the application developers or administrators. They explain the method and
   provide evidence that the data is encrypted.

That's the level of involvement.

**When there's no policy to check against.** Many organisations, especially small
and medium ones, have weak information security policies and no data classification
policy at all. Then you make a judgement call: ask how important the data is, how
severe the consequences would be if it were leaked or breached, take them through
the worst case, and find out how well they could tolerate it. If the data is
sensitive, recommend encryption.

**The good news — most of it is already on by default:**

| Where | Default position |
| --- | --- |
| Web traffic | HTTPS in use for applications served over the web |
| Databases | Encryption enabled by default in most modern systems |
| Microsoft 365 documents and email | Encrypted by default |
| AWS S3 buckets | Encrypted by default |

This wasn't always so — extra measures used to be needed. Now checking usually
confirms it's already there.

**Laptop hard drives** are the place to check explicitly. Employee laptops hold
data, and the drive should be encrypted — BitLocker on Windows enables this, and
once on, a stolen laptop is much harder to read. Verify with the IT team whether
drives are encrypted by default.

**The exceptions.** Around 1% of situations. Military and defence organisations use
genuinely advanced algorithms and detailed secure processes for handling keys.
Large banks use hardware encryption devices. In both, the identity and access
management principles apply to **key management**: separation of duties so no one
person holds a key that decrypts everything, and more than one person and more than
one approval before data can be decrypted. If you're involved, assess how keys and
the encrypted data are handled — not the mathematics.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Encryption algorithm | The mathematical formula that scrambles data | Know the names and uses; the internals aren't your job |
| Encryption key | The secret enabling decryption | The whole control depends on it, which is why key handling is the real subject |
| Policy-driven requirement | The security policy says which classifications must be encrypted | Turns "should we encrypt this" into a check against a stated rule |
| Judgement call | Recommending encryption where no policy exists | Common in smaller organisations; use consequence questions to get there |
| Evidence of encryption | Developers or administrators demonstrating it, not asserting it | Same evidence standard as any other control |
| Encryption by default | HTTPS, modern databases, M365, S3 | Reduces the work to verification rather than implementation |
| Full disk encryption | BitLocker and equivalents on endpoints | The one place still commonly unverified |
| Key management | Who holds keys, who can approve decryption | Where separation of duties and least privilege apply |

## Where this shows up in a real job

The "encryption by default" point matches what I see. A WordPress site on decent
hosting gets HTTPS automatically, and the database is encrypted at rest by the
provider. That's genuinely good — and it's also why site owners conclude they're
secure, which is the misconception from lesson 1. The default encryption is real
and it covers a narrow set of threats.

Disk encryption is the gap I'd expect to find. It's a setting rather than a
project, it's invisible when it's on, and nothing fails when it's off — so nobody
notices for years. A stolen laptop is where it gets discovered.

I've enabled BitLocker and worked with HTTPS configuration, which is enough to
have the conversation credibly. I haven't been near hardware security modules or a
formal key management process, and those are the deep end of this topic.

## My take

The most useful instruction here is the one about scope: **don't learn the
mathematics, learn the questions.** That's a genuinely freeing message for someone
moving into this field, because the cryptography rabbit hole is deep, well
documented, and almost entirely irrelevant to assessing whether an organisation
protects its data. The assessable questions are what's encrypted, in which states,
who holds the keys, and how that's evidenced.

Three things:

**"Is it encrypted?" is three questions, and the default-on cases only answer some
of them.** Data exists at rest, in transit, and in use. HTTPS covers transit.
Database and storage encryption cover at rest. Nothing in the default list covers
data in use — an application querying the database sees plaintext, which is the
point from lesson 1 about encryption defeating storage theft rather than access
theft. So the precise version of the check is "encrypted in which state, against
which threat", and an organisation answering "yes, we use HTTPS" has answered one
third of it.

**Default-on encryption usually means the provider holds the keys**, and that's the
question worth asking next. S3 encrypted with AWS-managed keys protects against
someone stealing the physical disks; it doesn't protect against a misconfigured
bucket policy, because anyone authorised to read the object gets it decrypted
automatically. Which is why nearly every reported S3 breach is an access
misconfiguration, not a cryptographic failure. Customer-managed keys change who
can be compelled or mistaken, and that's a real decision for sensitive data rather
than a technicality.

**Key management is the whole subject once the algorithms are settled**, and the
lesson is right to hand it to the IAM principles. Encryption converts a data
protection problem into a key protection problem — the data is now exactly as safe
as the key. So the assessment questions are the ones from module 5 wearing
different clothes: who can access the key, is that access logged, is it
time-bounded, can one person decrypt everything, what happens when the key holder
leaves, and how are keys rotated or recovered. An organisation with excellent
encryption and a key in a shared password manager has a single point of failure
with a mathematical wrapper.

Worth adding to the "check it's on" list: backups. A backup of an encrypted
database is frequently written somewhere with different protections — and it's the
same data. Lesson 1's spreadsheet fallback problem, at scale.
