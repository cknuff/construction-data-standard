# The Construction Ontology Opportunity
## Summary

*March 2026*

---

## Executive Summary

Construction is a $13T+ global industry that runs on fragmented data. A typical commercial project uses 12-20 disconnected software systems, generating data in incompatible formats that die at organizational boundaries. No one has successfully built a full-lifecycle construction data model that works across source systems, project phases, and organizations.

Procore can create this — the **Procore construction ontology** — a canonical, unopinionated data model that normalizes data from any source system into a single, queryable representation of a construction project's full lifecycle.

Procore is uniquely positioned to do this with:
- Datagrid's data connector capabilities to ingest data across common construction systems.
- Procore's Reporting & Analytics model (RAM) that structures data across Procore construction entities, including the relationships between entities that encode how construction actually works (change order cascades, cost attribution chains, field-to-financial linkages).
- A new permissions and data access model to the RAM that controls who sees what, at what granularity, across projects, roles, and tools - the infrastructure needed for multi-party data sharing.
- Datagrid's agentic capabilities built on top of this data.
- Cloud Connector for seamless customer access to data.
- The largest structured construction dataset in the industry (3M+ projects, 17K+ customers).

**This is not a reporting or analytics feature. This is an infrastructure play that could make Procore the gravitational center of construction data and AI, regardless of what tools a customer or their collaborators use.**

---

## Why Procore Can Do This and Others Can't

**We know how things are related.** The RAM encodes construction as a system of relationships: the change order cascade (CE → CPCO → CCO → Budget), cost-to-trade attribution, field-to-financial linkage, vendor performance graphs across projects. These aren't generic foreign keys — they're 20 years of encoding construction domain knowledge. No one starting from scratch can reverse-engineer them.

**We already solve permissions at scale.** Company-level partitioning, project-level permissions, role-based access, tool-level gating, vendor-scoped views — all battle-tested across 17K+ customers. Extending to multi-party cross-system sharing is an evolution of what we already do, not a greenfield problem.

**We have the data.** 3M+ projects, 17K+ customers, 336 tables across 5 domains. This is the largest structured construction dataset in the industry. It took 20 years to accumulate. No one is replicating it, and no one can build the proprietary data assets from it that we can.

**We have the connectors.** The Datagrid acquisition gives us data connector infrastructure to ingest data from the other systems customers use — ERPs, scheduling tools, safety platforms, accounting systems. The ontology needs pipes to feed it. We already have them.

**We have the industry.** Procore is the go-to platform for GCs in North America, and we're pulling owners, subs, and specialty contractors into that ecosystem every day. The ontology doesn't need to start from zero adoption — it extends a network that already exists.

---

## Why Data and AI Infrastructure, Not UI, Is Where We Win

Stripe didn't win payments by building the best checkout UI — they became the payments infrastructure. Salesforce didn't win by building the best contact form — they became the CRM platform. Each won by owning the canonical data model for their domain and letting everything else build on top.

Procore's path is the same. AI is making UI generation trivial. The cost of building "the app" is collapsing toward zero. What AI cannot generate is:

- **The data model** — the domain-specific schema that encodes how construction actually works.
- **The data itself** — 3M+ projects of structured construction data that took 20 years and 17K+ customers to accumulate.
- **The relationships** — which sub worked on which project, what happened when, how costs flowed from estimate to commitment to actual.

The company that owns the canonical data model and the data flowing through it wins. UIs become thin, interchangeable consumption layers. The ontology becomes the durable asset.

**But it's not just about the data - being the data hub for construction makes us the agentic hub.**

Procore already has agents that act across systems via Datagrid's connectors. But there's a critical difference between agents with **pipes to data** and agents with **a world model.**

**Today (agents with pipes):** Datagrid connects to Sage, P6, Viewpoint, and other systems. But each system is a foreign language. When you ask "what's my rework cost exposure?" the agent has to know that in Procore it's `change_events` with specific reason codes, in Sage it's `JC_COST_DETAIL` with different category values, in Viewpoint it's `APInvoice` with yet another structure. An agent built for a Sage customer has to be rebuilt for a Viewpoint customer.

**With the ontology (agents with a world model):** The agent reasons against canonical entities — `ActualCost`, `ChangeOrder`, `Vendor`, `Inspection` — with consistent meaning regardless of source. The normalization layer already did the translation.

What changes:
- **Cross-system relationships become queryable.** "This observation caused this change event which impacted this schedule task" — no single system knows that chain. With the ontology, it's a pre-resolved relationship graph.
- **Agent logic is system-agnostic.** Write the agent once. It works for every customer regardless of their tech stack.
- **Permissions travel with the data.** The permission layer is canonical — agents respect the same access controls regardless of source system.
- **New systems don't require new agents.** Customer connects a new ERP? Every existing agent immediately works with that data.

The ontology turns Datagrid from a powerful connector into a platform. **Connectors give agents reach. The ontology gives agents understanding.**

---

## What This Looks Like in Practice

### A Day in the Life: GC Project Manager

**Today:** Sarah is a PM running a $45M healthcare project. She starts her morning pulling a cost report from Procore, but her committed costs in Viewpoint Vista don't match because three change orders were approved in the ERP yesterday. She opens P6 to check the schedule impact of a mechanical delay, then cross-references it against the budget in Excel. Her super texts that a fire stopping inspection failed — she logs into SafetyCulture, then re-enters the key info into Procore so the owner can see it. After lunch, her owner asks for a rework summary across three active projects. Sarah spends 90 minutes pulling data from three Procore projects, two ERP instances, and the owner's spreadsheet. By 3pm she hasn't walked a single jobsite.

**With the ontology:** Sarah opens her hub page at 7am. The ontology has already normalized Viewpoint's change orders against Procore's committed costs. An agent detected the P6 delay and calculated $380K budget exposure across three cost codes. The SafetyCulture inspection flowed in overnight, tagged to the responsible sub. When her owner asks for the rework summary, she shares a live dashboard pulling from all three projects — Procore field data, Viewpoint actuals, owner milestone tracking — all normalized. She's on the jobsite by 9am.

### A Day in the Life: Owner's Representative

**Today:** Marcus manages a $200M capital program across two GCs. GC1 runs Procore + Sage, GC2 runs Autodesk Build + CMiC. He gets monthly PDF reports in completely different formats, re-keys numbers into Excel, and spends a week building one-time analyses for the board. He suspects GC2 has a rework problem but can't prove it because their quality data is locked in Autodesk Build.

**With the ontology:** Both GCs' data flows into the ontology via Datagrid — Procore, Sage, CMiC, Autodesk Build, all normalized to the same model. When the board asks about design-change exposure, Marcus asks Datagrid: "What's our total design-related change order cost across the program?" Answer in seconds: $8.2M, 62% in mechanical, GC2's hospital at 2.4x the benchmark. He drills in and sees quality observations from Autodesk Build confirming the pattern. No reports requested, no spreadsheets reconciled.

---

## The Problem To Solve

**Five compounding problems keep construction data fragmented:**

1. **System proliferation without integration.** 12-20 systems per project (design, PM, scheduling, ERP, accounting, field, safety, document management, BIM). None speak the same language.

2. **Data dies at organizational boundaries.** Owners, GCs, subs, and A/E firms can't share structured data. An owner can't query a GC's daily logs. A GC can't see a sub's safety history. Procore Connect addresses this in an opinionated, tool-specific way, but doesn't account for the many systems customers use.

3. **No lifecycle continuity.** Preconstruction data doesn't flow into construction. Construction data doesn't flow into operations. Each phase starts from scratch. The "digital twin" promise focused on BIM geometry, not operational and financial data.

4. **No standard taxonomy.** MasterFormat covers cost codes. IFC covers BIM geometry. COBie covers asset handover. None connect financial to field to design to schedule. None handle multi-party permissions.

5. **Excel is still the universal translator.** PMs download from 3-4 systems, paste into spreadsheets, manually reconcile, email results. Stale, fragmented, no automation, no benchmarking.

---

## What We Would Build

The **Procore Construction Ontology** extends the existing RAM (336 tables, 5 domains) from an internal analytical model to a universal construction data layer. Five extensions:

**1. External data normalization.** Datagrid connectors provide the pipes. The ontology provides the schema. Each adapter maps a source system (Sage, Viewpoint, P6, CMiC) to canonical entities. Procore data maps natively.

**2. Multi-party data model.** The RAM is company-scoped. The ontology adds project-centric, multi-party views with permissioned sharing. Each party owns their data. Queries cross org boundaries with authorization. Entity resolution matches the same sub across different systems.

**3. Lifecycle continuity.** Estimates flow into budgets flow into actuals flow into asset records. Bid packages become commitments become payment histories. Permit requirements become inspection checklists become compliance certificates.

**4. Unified classification.** The ontology bridges MasterFormat, UniFormat, OmniClass, IFC, and company-specific codes. "HVAC rough-in" maps to the same entity whether it comes from Procore, Sage, or a custom cost code.

**5. Temporal model.** Time as a first-class concept. Point-in-time queries, change attribution, trend analysis, bid-to-forecast-to-actual comparison.

### Flexible, Unopinionated UIs on Top

The ontology is the hard, durable layer. The UI layer should be thin, flexible, and composable. Products we already have that point here:

- **Hub Pages** — canvas-based, drag-and-drop. With the ontology: widgets from ANY connected system on one canvas.
- **Pages** — document-style with embedded live data. With the ontology: combine Procore observations, Sage costs, and P6 schedule in one document.
- **Dataset Editor** — user-defined datasets. With the ontology: join across systems because they share the same model.
- **Tool Studio** — no-code custom tools. With the ontology: build construction apps on the full data estate, not just Procore modules.
- **Cloud Connector** — data export. With the ontology: export the full normalized dataset to Power BI, Tableau, or custom apps.

**Then AI composes the UI itself.** A PM asks "show me everything at risk" → an agent queries across financial, schedule, quality, and safety signals, then assembles a hub page. An owner says "I need a board report" → an agent builds a Pages document from cross-project ontology data. Procore doesn't need to anticipate every view. It needs the data model right, composable UI primitives, and AI to connect them.

---

## What This Unlocks

### 1. Data Gravity
Procore becomes the place where ALL project data lives unified. Once a customer's data from 10 systems is normalized into the ontology, leaving means re-fragmenting everything. AI can generate a dashboard in 30 seconds. It cannot generate 336 tables of construction-specific relationships.

### 2. Cross-Organizational Analytics
Owners benchmark GCs across projects regardless of PM tools. GCs benchmark subs even when subs use different systems. Insurance/surety companies get risk profiles from actual data, not questionnaires.

### 3. The Agentic Hub
Agents get a complete world model, not just pipes to data. Third-party agents — insurance, estimating, safety, scheduling — all build against the ontology. Procore becomes the platform agents are built FOR.

### 4. New Revenue Streams
Connector marketplace, Cloud Connector premium (full normalized dataset), benchmarking-as-a-service, data quality scoring, partner API.

### 5. Lifecycle Value
Construction data stops dying at phase boundaries. Estimates seed budgets, budgets track to actuals, actuals become asset records. A renovation project starts with the original project's full history — not a blank spreadsheet.

### 6. Solving Customer Inaction
Lower setup cost (pre-built analytics work across any source combination). Data flows in automatically from systems people already use. Value visible before full Procore adoption — connect any source, see results immediately.

### 7. Competitive Positioning Shift

**The positioning ladder:**
1. **Tool** (where most see us today) → "Procore is the best construction PM platform"
2. **Data hub** (near-term shift) → "Procore is where all your construction data comes together"
3. **Agentic hub** (the unlock) → "Procore is where construction agents live — reading, reasoning, and acting across your entire project data estate"
4. **Industry standard** (long-term) → "Procore's ontology is the construction data model. Everything else plugs in."

---

## Why Now?

1. **Datagrid acquisition complete.** The connector infrastructure exists. Now it's "what flows through the pipes."
2. **AI requires complete data.** Helix, Agents, and Copilot are bounded by data completeness. The ontology makes AI work with ALL of a customer's data.
3. **Industry is ready.** 53% workforce retirement by 2036, rising complexity, margin pressure. If Procore doesn't build the data infrastructure, someone will try — but no one else has the data gravity to make it work.

---

## The Bottom Line

The RAM is the foundation. Datagrid connectors are the plumbing. The ontology is the missing piece that connects them into something no one else can replicate. When anyone can build a construction app with a prompt, the company that owns the canonical data model wins. 

And when every construction company needs agents that can reason and act across their full project data estate, the company that owns the data model becomes the platform those agents are built on. That should be Procore.
