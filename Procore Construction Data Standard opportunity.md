
## Executive summary

Construction is a $13T+ global industry where productivity has stalled due to fragmented data. A typical commercial project uses dozens of disconnected software systems across the architect/engineer, general contractor, owner, and subcontractors, generating data in incompatible formats that die at organizational boundaries. No one has successfully defined a standard for construction project data that works across source systems, project phases, and organizations.

Procore is uniquely positioned to define the Procore Construction Data Standard, a machine-readable dictionary that defines what construction data means, how it relates, where it lives across any system, and how it can be shared between project stakeholders.

The Construction Data Standard is not a database, a data warehouse, or a new data model. It's a reference standard, a dictionary. We already have the data. Procore's native data lives in the RAM, and external data from ERPs, scheduling tools, safety platforms and more is already flowing into Procore through Datagrid's data connectors. The standard doesn't move data or create new pipelines. It gives all of that data — Procore-native and connector-sourced — a common language: consistent definitions, typed relationships, validated business rules, per-system mappings, and a sharing model that defines how data travels between companies. A "change order" means the same thing whether it comes from Procore, Sage, or Viewpoint. Systems built on the standard can query across sources because every source speaks the same language.

We have the pieces to define this that no one else has: 20 years of encoded construction relationships in our Reporting & Analytics model (RAM), the largest structured dataset in the industry, and Datagrid's connector infrastructure already ingesting data from external systems. The Construction Data Standard is the missing piece that connects them into something no one else can replicate. When anyone can build a construction app with a prompt, the company that owns the canonical definition of construction data wins.


## Problem to solve

The construction industry's data fragmentation is a structural bottleneck driven by four compounding forces:

- **System proliferation without integration.** 12-20 systems per project (design, PM, scheduling, ERP, accounting, field, safety, BIM). None speak the same language.

- **Data dies at organizational boundaries.** Owners, GCs, subs, and A/E firms can't share structured data. An owner can't query a GC's daily logs. A GC can't see a sub's safety history. Every time a project moves between stakeholders, the digital thread is severed.

- **No lifecycle continuity.** Preconstruction data doesn't flow into construction. Construction data doesn't flow into operations. Each phase starts from scratch.

- **No standard taxonomy.** MasterFormat covers cost codes. IFC covers geometry. Nothing connects the financial reality of a project to its field progress or its schedule.

The result: Excel, PDFs, and stale spreadsheets remain the industry's universal language. Without a shared vocabulary for construction data, AI and agents can only see a fraction of the project reality.


## Defining the Construction Data Standard

### What the standard is (and isn't)

The Construction Data Standard is a dictionary, a machine-readable reference that defines what construction data means. It has four parts:

1. **Domains and elements** — the standard organizes construction into domains covering the full project lifecycle — from what's being built (building elements, resources, locations) to how it's managed (financial instruments, schedule, contracts, quality & safety records, field operations) to who's involved (organizations, roles) to what governs it (permits, standards, risk, workflows). Each domain contains canonical elements with typed attributes, valid states, common values, industry standard references, and standard measures for benchmarking.

2. **Relationships** — how construction actually works, formalized. Categories of typed, directed relationships with cardinality: compositional (what contains what), financial (how money flows), lifecycle (how things evolve — an RFI becomes a change order), causal (what triggers what), temporal (sequencing and dependencies), responsibility (who owns what), and others covering spatial, resource, organizational, document, compliance, risk, and benchmark connections. These aren't generic foreign keys — they're 20 years of construction domain knowledge written down as traversable connections.

3. **Per-system mappings** — where each element lives in each source system. Procore's `change_events.estimated_cost`, Sage's `JC_COST_DETAIL.AMOUNT`, and Viewpoint's `JCCost.CostAmt` all map to the same standard element: `ChangeEvent.cost`. One mapping file per source system translates that system's schema to standard definitions.

4. **Sharing model** — how data travels between companies on a project. Default visibility tiers per element, a consent model for each party to specify what they share and with whom, and authorization rules for cross-org queries. The sharing model separates format from access — the standard makes format universal, each company independently controls who sees what.

The standard is a semantic layer that sits on top of Procore's existing data sources. The RAM already encodes how construction works — an observation links to a vendor, a location, a spec section, and the downstream change event. Datagrid connectors are already bringing in external data from ERPs, scheduling tools, and safety platforms. The standard doesn't replace any of this. It gives all of it — the RAM, connector data, and external classification systems like MasterFormat, UniFormat, and IFC — a shared vocabulary. It's source agnostic, workflow agnostic, and role agnostic. Per-system mapping files translate each source's schema. Per-customer configurations handle company-specific variation — field values, custom fields, cost code structures. The standard defines what things mean. The mapping file says where things live. The config says how each customer expresses them. Adding a new source system means connecting it through Datagrid and writing one mapping file.

### Why a standard, not a warehouse

The obvious alternative is to build a consolidated data warehouse. We shouldn't. The data is already here — Datagrid connectors already solved the ingestion problem. A warehouse solves storage but not semantics — data from Sage and Viewpoint can sit in adjacent tables and still mean different things. A warehouse doesn't solve cross-company sharing — it doesn't define who sees what or how authorization works across GCs. And a warehouse is expensive and slow — multi-year ETL infrastructure vs. a reference layer that delivers value the moment a mapping file is written. The right architecture: data stays where Datagrid already put it, the standard gives it meaning, and the sharing model gives it boundaries.

### Products built on the standard

The standard is the durable layer. Products above it are thin and composable. Hub Pages, Pages, 360 Reporting, Dataset Editor, Tool Studio, Cloud Connector, and Insights all benefit from the same thing: data from any connected system resolves to the same definitions, so every product works with every source automatically.

Agents are the biggest unlock. Today, an agent built for a Sage customer has to be rebuilt for a Viewpoint customer — even though all the data is already inside Procore. With the standard, agents reason against canonical definitions (ActualCost, ChangeOrder, Vendor, Inspection) regardless of source. Write the agent once, it works for every customer, every system combination. Procore becomes the platform agents are built for.


## Why Procore — and why no one else can

**We know how things are related.** The RAM encodes the change order cascade, cost-to-trade attribution, field-to-financial linkage, vendor performance across projects. 20 years of construction domain knowledge. The standard writes it down in a portable format.

**We have the data.** 3M+ projects, 17K+ customers — the largest structured construction dataset in the industry. The standard's definitions and business rules are grounded in real project data, not theoretical models.

**We have the connectors — and the data is already flowing.** Datagrid is already ingesting from ERPs, scheduling tools, safety platforms, accounting systems. That external data is already inside Procore. The standard gives it meaning.

**We understand multi-party data sharing.** Procore handles company-level partitioning, project- and tool-level permissions, and role-based access for Procore data. Extending to cross-company, cross-system sharing is new territory — our current permission system only governs Procore data. But no one else has even started. We're the right company to define how it should work.

**We have the industry.** Procore is the go-to platform for GCs in North America, pulling owners and specialty contractors in every day. The standard doesn't start from zero adoption — it gives a common vocabulary to a network that already exists.

### Competitive landscape

Nobody is building what the Construction Data Standard would be. Each player owns a slice. None span operational, financial, and field execution data with cross-company coverage.

**Palantir for Construction.** The most direct comparison — their Foundry "ontology" is conceptually similar. But Palantir builds a custom ontology per customer, has no shared standard, no cross-company benchmarking, no self-service path ($1M+ contracts), and no construction data of its own. They can wire systems together for one company. The standard gives an entire project — across companies — a shared vocabulary.

**Autodesk Platform Services (formerly Forge).** Autodesk owns design data — BIM visualization, clash detection, model coordination. ACC has lighter modules for Issues, RFIs, and Cost Management, but no daily logs, observations, inspections, or safety data. No cross-company view, no benchmarking. Autodesk Tandem covers facility operations but skips the construction phase entirely. The standard covers everything Autodesk doesn't: the operational and financial lifecycle.

**Oracle Aconex + Primavera.** Strong on owner-side cost controls and scheduling for megaprojects. But separate products, not a unified data layer. No cross-company benchmarking, limited US GC adoption. Different market.

**buildingSMART / IFC.** The closest thing to an open construction data standard — but a design interchange format in practice. The gap in operational and financial data is exactly where the standard sits.

**ERP vendors and horizontal platforms.** ERPs (Trimble/Viewpoint, Sage, CMiC) own back-office finance but live in silos — they are sources the standard maps, not competitors. Snowflake and Databricks are infrastructure. They provide compute. The standard provides semantics.


## Customer value

**One view of the full project, across every system.** The standard defines what data means across tools so any product can show cross-system data in one place. A change order in Procore and its actual cost in Sage resolve to the same definition. Estimates seed budgets, budgets track to actuals, actuals become asset records. A renovation project starts with the original project's full history.

**Works with existing tools.** Customers don't rip and replace. Data is already flowing in through Datagrid — the standard gives it a common vocabulary. Connect a new system and every report, dashboard, and agent works with the new data automatically.

**Share data across companies without sharing systems.** Today, cross-company sharing means PDFs and manual re-entry. The standard separates format from access. Format becomes universal: an owner doesn't reconcile reports from three GCs using three different systems. Access control is independent: the GC configures what they share (cost summaries yes, line-item markup no), the sharing model enforces it. The owner queries live data across GCs within the bounds each authorized.

**Cross-system discrepancy detection.** When Procore's committed cost and the ERP's actual cost map to the same definition, discrepancies surface automatically — before month-end reconciliation.


### A day in the life: GC project manager

Today: Sarah is a PM running a $45M healthcare project. She starts her morning pulling a cost report from Procore, but her committed costs in Viewpoint Vista don't match because three change orders were approved in the ERP yesterday. She opens P6 to check the schedule impact of a mechanical delay, then cross-references it against the budget in Excel. Her super texts that a fire stopping inspection failed — she logs into SafetyCulture, then re-enters the key info into Procore so the owner can see it. After lunch, her owner asks for a rework summary across three active projects. Sarah spends 90 minutes pulling data from three Procore projects, two ERP instances, and the owner's spreadsheet. By 3pm she hasn't walked a single jobsite.

With the standard: Sarah opens her hub page at 7am. Viewpoint's change orders and Procore's committed costs map to the same definition — a discrepancy flag shows the 3 newly approved COs that haven't synced. An agent queried the P6 schedule and calculated $380K budget exposure across three cost codes. The SafetyCulture inspection flowed in overnight, mapped to the same Inspection definition as Procore's, tagged to the responsible sub. When her owner asks for the rework summary, she shares a live dashboard pulling from all three projects — all speaking the same language. She's on the jobsite by 9am.


### A day in the life: Owner's rep

Today: Marcus manages a $200M capital program across two GCs. GC1 runs Procore + Sage, GC2 runs Autodesk Build + CMiC. He gets monthly PDF reports in completely different formats, re-keys numbers into Excel, and spends a week building one-time analyses for the board.

With the standard: Both GCs' data maps to the same definitions. Each GC configured their sharing policy: cost summaries, schedule milestones, and quality observation counts are visible to Marcus; internal markups and daily logs are not. When the board asks about design-change exposure, Marcus asks: "What's our total design-related change order cost across the program?" Answer in seconds: $8.2M, 62% in mechanical, GC2's hospital at 2.4x the benchmark. No reports requested, no spreadsheets reconciled — and each GC controls exactly what he sees.


## Procore value

**Data gravity.** Once a customer's systems speak the same vocabulary, leaving means losing the common language and re-fragmenting everything. The standard creates switching costs that compound with every connected system.

**The baseplate.** The standard shifts Procore from competing on individual tools to owning the definitions that tools connect to. Anyone can build on top, but they reference the standard to function.

**Network effects.** When an owner requires GCs to connect, GCs comply without changing tools — they just map them. The sharing model removes the biggest objection: "I don't want to expose my data." Adoption drives itself through project relationships.

**New markets.** The standard unlocks architects, engineers, insurers, and third-party developers who want to build against it — customers Procore doesn't serve today.

**AI moat.** Generic AI tools can generate dashboards in seconds. They cannot replicate the construction domain knowledge and the dataset that validated the standard. The standard is what makes construction data meaningful to any agent, product, or partner.
