# Types of assets

> Module 04, lesson 2. The first cut at categorising what an organisation has.

## Summary

Assets split into two types.

**Tangible** — physical things. Hardware, laptops, routers, firewalls, medical
equipment, generators.

**Intangible** — everything that isn't physical: people, data, information,
software, services, trademarks, copyright, patents, intellectual property, brand
image, reputation.

The hospital example makes it concrete. Tangible: medical equipment, PCs, laptops,
network devices, specialist surgical devices. Intangible: staff — doctors and
nurses — patient data, medical imaging, and the hospital's reputation.

## Key concepts

| Concept | What it means | Why it matters in practice |
| --- | --- | --- |
| Tangible asset | A physical item the organisation owns or operates | Countable, serial-numbered, and the easiest part of an inventory to get right |
| Intangible asset | Non-physical: data, software, services, people, IP, reputation | Harder to enumerate, and usually where the value actually sits |
| People as assets | Staff are listed as assets in their own right | Skills and knowledge leave with them, which is why key-person risk is a risk |
| Data and information | Patient records, imaging, research, customer records | Almost always the crown jewels, and never visible on a stock-take |
| Reputation and brand | The organisation's standing with clients and the market | Named as an asset; behaves differently from the rest — see below |

## Where this shows up in a real job

The hospital example maps directly onto Helium Health. Patient data and medical
imaging were the assets that mattered, and the hardware existed largely to hold
and move them. When we scoped the ISO 27001 work, the arguments were never about
laptops.

WordPress work sits almost entirely on the intangible side. For a typical site
there's no hardware to count — the hosting belongs to someone else — and the asset
list is the site's data, its customer records, the content, the domain name, the
integrations, and the reputation of whoever runs it. That's the modern shape of
the problem: as infrastructure becomes someone else's tangible asset, almost
everything left on your own list is intangible, and none of it can be found by
walking around the building.

## My take

The most useful thing in this split is that **the assets you can photograph are
rarely the ones that matter**. Tangible assets are easy to inventory — they have
serial numbers, they arrive on purchase orders, someone signs for them. Intangible
assets carry most of the value and have none of those handles. So an inventory
built from what's easy to count will be accurate and beside the point.

Two things worth carrying forward:

**Assets depend on each other, and the inventory has to show it.** Patient data is
an intangible asset that lives on tangible ones — a server, a device, a backup
drive — and reaches people through software and services. Protecting the data means
knowing which physical things hold it. A list of assets in two separate columns
misses the relationships, which is where the actual exposure lives. I'd expect the
CMDB lesson to be about precisely this.

**Two of the listed items behave differently from the others.** Most entries are
things you can enumerate, assign an owner to and apply a control to. Reputation
and brand image aren't — you can't patch reputation or give it an owner in the way
you can a database. They're better understood as what gets damaged when other
assets fail, which makes them closer to an impact category than an inventory item.
Keeping them in view matters; putting them in the same list as laptops makes the
list harder to act on.

People sit awkwardly in a two-box model too. Staff are genuinely assets — the
knowledge is real and it walks out of the building — but calling a doctor
"intangible" strains the word, and people need controls (training, access,
succession) that don't resemble anything applied to data or hardware. For an
actual inventory I'd expect to see them as their own category rather than filed
under intangibles.
