# Data labelling

> Module 07, lesson 3. Applying the classification scheme to actual data — the
> part that's genuinely hard.

## Summary

Classification defines importance by criticality and sensitivity. Writing the
definitions is easy; applying them in practice is the challenge.

Data is organised in one of two ways:

**Structured data** — well organised, in databases and spreadsheets. In the
insurance example, the HR system holding employee information is structured: it
sits in a database that can be accessed and referenced.

**Unstructured data** — files and documents on laptops and SharePoint, images,
social media posts. Anything not sitting in a database or spreadsheet.

Both need labelling, so that the labels can drive encryption and specific DLP
rules.

**Labelling structured data is comparatively straightforward.** The database
software usually provides the capability — Oracle and Microsoft SQL Server both
have built-in options to classify data, which is genuinely useful.

**Unstructured data is where it gets chaotic.** Commercial tools exist that scan
hard drives and email systems to detect sensitive data, but they aren't especially
accurate and need a lot of tuning and monitoring. Clients commonly complain that
labelling and tagging data is hard — which is bad news, because organisations can
have terabytes sitting on old servers and old laptops that still need watching.

**The notable product** is Microsoft's, referred to in the lesson as Azure AIP,
which makes tagging and labelling much easier for the many organisations already on
Office 365. It makes labelling a Word document straightforward, and prompts
employees to tag and label emails as they send them — so someone sending something
confidential or sensitive can mark it, which lets the organisation intercept it,
stop it, or require encryption.

## Structured vs unstructured

| | Structured | Unstructured |
| --- | --- | --- |
| Where it lives | Databases, spreadsheets | Laptops, SharePoint, email, file shares |
| Examples | HR system, insurance claims database | Documents, images, exports, social posts |
| How it's labelled | Built-in database classification features | Scanning tools, or the user at creation |
| Difficulty | Manageable — finite, centralised, owned | Hard — dispersed, duplicated, unowned |
| Volume problem | Bounded by the schema | Terabytes on forgotten servers and old laptops |

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Labelling | Attaching the classification to the actual data | What turns a policy into something a control can act on |
| Structured data | Data in a defined schema — databases, spreadsheets | The tractable half of the problem |
| Unstructured data | Files, documents, images, email | The majority of most estates, and the difficult half |
| Native database classification | Labelling features in Oracle, SQL Server and similar | Labels applied where the data already is, at column level |
| Discovery scanning | Tools that crawl drives and mail for sensitive content | Useful, inaccurate, and needs continuous tuning |
| User-applied labels | Prompting people to label documents and emails as they create them | Scales in a way scanning doesn't; depends on people |
| Label-driven enforcement | Labels feeding encryption and DLP decisions | The reason labelling exists at all |

## Where this shows up in a real job

The unstructured problem is the one I recognise. In support, customer data lives in
the database *and* in the exported CSV someone attached to a ticket, the screenshot
pasted into a thread, and the backup copy on a laptop. The system of record is the
part that's easy to find and protect; the copies are where the exposure actually
sits, and nothing indexes them.

Old servers and old laptops holding terabytes nobody watches is the asset
management problem from module 4 arriving in a different form — the same forgotten
systems, now framed by what's on them rather than by what they are. The two
exercises would find the same machines.

I haven't deployed a labelling tool or run a discovery scan, so I'd be assessing
this from principles.

## My take

The honest framing of this lesson is that **labelling is where data protection
programmes actually stall.** Everything before it is comparatively cheap — writing
definitions, holding workshops, producing a policy. Labelling is the step that
touches every file in the organisation, and it's the reason a scheme can exist on
paper for years while no control acts on it.

Three things:

**The structured/unstructured split predicts where the effort goes, and it's
lopsided.** Structured data is a minority of most estates and the easy part: finite,
centralised, schema-defined, and someone owns each database. Unstructured data is
the majority, is duplicated constantly, has no owner, and grows without anyone
deciding. So a programme reporting "we've classified our data" has usually
classified the databases. The assessment question is what proportion of
unstructured data carries a label, and the answer is generally uncomfortable.

**Labelling at creation beats labelling by discovery, and the two solve different
problems.** Scanning finds what already exists and is inaccurate because it's
inferring sensitivity from content. Prompting the author to label at the moment of
creation is accurate, because the person writing the document knows what's in it —
and it scales, because the work is distributed. The catch is that it depends on
people making a judgement they may not care about, which is why the scheme needs
few levels and clear examples, and why a default label matters for whatever nobody
chooses. Practically: scanning for the backlog, user labelling for everything new.

**A label is a persistent claim about data, which is what makes it powerful and
fragile.** Labels travel with the file, so a document marked confidential can be
blocked at the mail gateway or encrypted automatically wherever it goes. But labels
are lost by copy-paste into a new document, by export to a different format, by
screenshots, and by anything that extracts content without the metadata. So
label-driven DLP is strong against the ordinary case and weak against the
determined one — worth knowing before recommending it as the answer to insider
threat.

On the product: the Microsoft offering has been renamed since — Azure Information
Protection folded into **Microsoft Purview Information Protection**, with
sensitivity labels managed there. Same capability, current name. Worth using the
current terminology, since AIP as a standalone name is on its way out of the
documentation.
