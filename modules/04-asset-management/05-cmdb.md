# CMDB

> Module 04, lesson 5. Where the asset record lives, why it's usually thin, and
> why a spreadsheet is a respectable place to start.

## Summary

**CMDB** stands for Configuration Management Database — the store holding
information about assets. Everything identified and everything classified should
end up here.

In practice it's usually narrower than that. Traditionally a CMDB was the IT
team's database of server, network and switch names, and maintaining it got
called asset management. The problem is context. Open one and you'll find
hostname, serial number, IP address — all useful, none of it telling you what the
thing *represents*. For GRC, where the whole purpose is understanding which assets
are valuable, a list of hostnames and serial numbers doesn't answer the question.
It's a start, not an answer.

So the working pattern is: export what's in the CMDB, then add what's missing —
criticality rating, asset classification, asset owner. Along the way, remove
duplicates and clean it up, because there will be duplicates.

On tooling, the lesson is refreshingly unexcited. Plenty of vendors sell CMDB
solutions, none of them stands out, and some are better than others depending on
what the organisation will spend. And the practical advice: **a spreadsheet is
not a bad idea**, particularly as a starting point. If an organisation has nothing
at all, a spreadsheet recording the asset, serial number, owner and risk rating is
a genuinely good start — better than a database full of serial numbers with no
context. There's no shame in documenting your work in a spreadsheet.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| CMDB | Configuration Management Database — the store of asset records | The intended home for identification and classification output |
| The context gap | Hostnames, serials and IPs with no business meaning attached | The reason a CMDB alone doesn't answer GRC's question |
| Enrichment | Adding rating, classification and owner to the technical record | The step that turns an IT inventory into an asset register |
| Deduplication | Removing repeated entries before the data is usable | Duplicates are normal, and they distort any count built on the data |
| Tooling is secondary | No vendor solution is decisively better; investment varies | Don't let a tool selection become the reason nothing gets recorded |
| Spreadsheet as a start | Asset, serial, owner, rating in a sheet | Beats an uncontextualised database, and beats nothing by a wide margin |

## Where this shows up in a real job

The context gap describes internal tooling I've used. A list of customer sites
gives you hostnames, plans and technical attributes — everything except which ones
matter and to whom. The information that determines how carefully you treat a case
usually isn't in the system; it's held by whoever knows the account.

The WordPress equivalent of a CMDB is a site management dashboard listing
installed plugins, themes and versions across sites. Technically complete and
business-blind: it knows a site runs forty plugins, not whether the site is a
hobby blog or someone's entire income.

"Export it, clean it, add the columns that matter" is also just familiar work.
Reconciling partial lists from different sources into something usable is a large
part of any support or operations job, and it's the same skill here with different
column headings.

## My take

The context gap has a cause worth understanding rather than just noticing: the
CMDB was built for a different job. Configuration management databases come out of
IT service management, where the question is what's deployed, how it's configured
and what a change will affect. Hostname, serial and IP are exactly right for that.
They're thin for GRC because GRC is asking a question the tool was never designed
to answer — what is this worth, and who owns it. That reframes the enrichment step
as translation between two disciplines rather than as fixing someone's sloppy
database, which is also a better conversation to have with the IT team who
maintain it.

Two practical points:

**The export-and-enrich pattern creates two records that immediately start
drifting.** IT keeps updating the CMDB as machines come and go; the enriched
spreadsheet is a photograph. Within months the classification work describes an
estate that has moved on. The fix is to decide up front which system holds which
truth — the CMDB for existence and technical facts, the register for
classification and ownership — and to set a refresh cadence for pulling one into
the other. Without that, the enriched copy silently becomes historical.

**Duplicates are a signal, not just mess.** Repeated entries usually mean several
discovery sources feeding the same database with no agreed key to match on — the
network scan and the procurement record disagree about what to call the same
server. Cleaning them is necessary, but the underlying question is what identifier
the organisation treats as authoritative. Otherwise the duplicates come back.

On the spreadsheet: the advice is right, and the reason is that starting beats
selecting. An organisation that spends six months evaluating CMDB vendors has six
months of no inventory. Worth being clear-eyed about what a spreadsheet defers,
though — no change history, no access control, no automatic refresh, and one
person's laptop as the single point of failure. Those aren't reasons to avoid it;
they're the criteria for knowing when the inventory has outgrown it.
