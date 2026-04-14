# The Construction Ontology Opportunity
## A Strategic Analysis for Procore Data & Analytics

*March 2026*

---

## Executive Summary

Construction is a $13T+ global industry that runs on fragmented data. A typical commercial project uses 12-20 disconnected software systems, generating data in incompatible formats that die at organizational boundaries. No one has successfully built a full-lifecycle construction data model that works across source systems, project phases, and organizations.

Procore can create this - the **Procore** **construction ontology** — a canonical, unopinionated data model that normalizes data from any source system into a single, queryable representation of a construction project's full lifecycle.

Procore is uniquely positioned to do this with:
- Datagrid's data connector capabilities to ingest data across common construction systems.
- Procore's Reporting & Analytics model that structures data across Procore construction entities, including the relationships between entities that encodes how construction actually works (change order cascades, cost attribution chains, field-to-financial linkages).
- A new permissions and data access model that controls who sees what, at what granularity, across projects, roles, and tools, the exact infrastructure needed for multi-party data sharing.
- Datagrid's agentic capabilties built on top of this data.
- Cloud Connector for customers to seamless access to data.
- The largest structured construction dataset in the industry (3M+ projects, 17K+ customers).

**This is not a reporting or analytics feature. This is an infrastructure play that could make Procore the gravitational center of construction data and AI, regardless of what tools a customer or their collaborators use.**

### Why Data and AI Infrastructure, Not UI, Is Where We Win

The competitive landscape is shifting underneath every SaaS company. AI is making UI generation trivial. The cost of building "the app" is collapsing toward zero. What AI cannot generate is:

- **The data model** — the domain-specific schema that encodes how construction actually works (change order cascades, AIA-style invoicing, 5-level location hierarchies, budget-to-WBS mappings).
- **The data itself** — 3M+ projects of structured construction data that took 20 years and 17K+ customers to accumulate.
- **The relationships** — which sub worked on which project, what happened when, how costs flowed from estimate to commitment to actual.

The company that owns the canonical data model and the data flowing through it wins. UIs become thin, interchangeable consumption layers. The ontology becomes the durable asset.

**Being the the data hub for construction makes us the agentic hub.**

Every project's data — from any system, any phase, any party — normalizes into our ontology. Customers, partners, and AI agents consume it through whatever interface they want (Procore's own products, Power BI, custom apps, LLM-generated UIs). The interface doesn't matter. The data model and the data do.

Procore already has agents that act across systems via Datagrid's connectors. But there's a critical difference between agents with **pipes to data** and agents with **a world model.**

**Today (agents with pipes):** Datagrid connects to Sage, P6, Viewpoint, and other systems. Agents can read and write across them. But each system is a foreign language. When you ask "what's my rework cost exposure?" the agent has to know that in Procore it's `change_events` with specific reason codes, in Sage it's `JC_COST_DETAIL` with different category values, in Viewpoint it's `APInvoice` with yet another structure. Every system requires bespoke schema interpretation. An agent built for a Sage customer has to be rebuilt for a Viewpoint customer. Relationships that span systems — this observation caused this change order which impacted this schedule task — don't exist anywhere and the agent has to figure out the joins on the fly.

**With the ontology (agents with a world model):** The agent doesn't think in terms of Sage tables or Viewpoint schemas. It reasons against canonical entities — `ActualCost`, `ChangeOrder`, `Vendor`, `Inspection` — with consistent meaning regardless of source. The normalization layer already did the translation. The agent queries "ActualCost where category = rework" and gets the answer whether the customer runs Sage, Viewpoint, CMiC, or all three.

What changes concretely:

- **Cross-system relationships become queryable.** "This observation in Procore caused this change event which maps to this cost increase in Sage which impacted this schedule task in P6." No single system knows that chain. With the ontology, it's a pre-resolved relationship graph, not a runtime join across three foreign schemas.
- **Agent logic is system-agnostic.** Write the agent once against the canonical model. It works for every customer regardless of their tech stack. Without the ontology: N systems × M agents = N×M integrations to maintain. With it: N adapters + M agents = N+M. That's the difference between O(n²) and O(n).
- **Reliability goes up dramatically.** "Amount" in one system means committed cost, in another it means invoiced amount, in another it means budget allocation. The ontology resolves those ambiguities once. Agents operate on semantically consistent data, not best-guess schema interpretation.
- **Permissions travel with the data.** Today if an agent reads from Sage, who controls access? With the ontology, the permission layer is canonical — the agent respects the same access controls regardless of source system.
- **New systems don't require new agents.** Customer connects a new ERP? The normalization adapter maps it to the ontology. Every existing agent immediately works with that data.

The ontology is what turns Datagrid from a powerful connector into a platform. Connectors give agents reach. The ontology gives agents understanding.

This is how the data hub begets the agentic hub:
1. **Data hub** — all construction data normalizes into the ontology
2. **Intelligence layer** — proprietary datasets builds understanding on top of normalized data (benchmarks, predictions, anomalies)
3. **Agentic layer** — Agents reason and act against the canonical model, not raw system schemas. One agent works for every customer.
4. **Ecosystem lock-in** — third-party agents (customer-built, partner-built, industry-built) all target the ontology as their runtime. Procore becomes the platform agents are built FOR.

This is the same playbook that made Stripe the payments infrastructure (not a checkout UI), Snowflake the data cloud (not a BI tool), and Salesforce the CRM platform (not a contact form). Procore becomes the construction data infrastructure — and the agentic runtime — that everything else runs on.

### What This Looks Like in Practice

#### A Day in the Life: GC Project Manager

**Today (fragmented world):**
Sarah is a PM running a $45M healthcare project. She starts her morning pulling a cost report from Procore, but her committed costs in Viewpoint Vista don't match because three change orders were approved in the ERP yesterday but haven't been reconciled. She opens P6 to check the schedule impact of a two-week mechanical delay, then manually cross-references it against the budget in Excel to estimate the cost exposure. Her super texts that a fire stopping inspection failed — she logs into SafetyCulture to see the details, then re-enters the key info into Procore so the owner can see it. After lunch, her owner asks for a portfolio-level rework summary across their three active projects. Sarah spends 90 minutes pulling data from three different Procore projects, two ERP instances, and the owner's cost tracking spreadsheet, then reconciles it all in Excel. By 3pm she hasn't walked a single jobsite.

**With the ontology (data hub + agentic hub):**
Sarah opens her Procore hub page at 7am. The ontology has already normalized last night's Viewpoint change orders against Procore's committed costs — the numbers match, flagged as reconciled. An agent has detected the mechanical delay in P6 and automatically calculated the budget exposure using the ontology's schedule-to-cost linkage: $380K potential impact, with three affected cost codes highlighted. The failed fire stopping inspection from SafetyCulture flowed into the ontology overnight — it's already visible in the daily log, tagged to the responsible sub and linked to the spec section. When Sarah's owner asks for the rework summary, she shares a live dashboard that pulls from the ontology across all three projects — Procore field data, Viewpoint actuals, and the owner's milestone tracking — all normalized and current as of this morning. She's on the jobsite by 9am.

#### A Day in the Life: Owner's Representative

**Today (fragmented world):**
Marcus manages a $200M capital program — four active projects across two GCs. Each GC uses different tools: GC1 runs Procore + Sage 300, GC2 runs Autodesk Build + CMiC. Marcus can't compare them. He gets a monthly PDF cost report from each GC in completely different formats. He manually re-keys the numbers into his own Excel model to get a portfolio view. When the board asks "what's our total design-change exposure across the program?" he spends a week collecting data, normalizing cost code structures, and building a one-time analysis that's stale before he presents it. He suspects GC2 has a rework problem on the hospital project, but he can't prove it because their safety and quality data is locked in Autodesk Build and he only sees what they put in the monthly report.

**With the ontology (data hub + agentic hub):**
Marcus logs into his owner dashboard. Both GCs — despite using completely different tool stacks — have their data flowing into the ontology via Datagrid connectors. Procore data, Sage data, CMiC data, Autodesk Build data — all normalized to the same canonical model. His portfolio view shows real-time budget performance across all four projects with consistent cost code mapping (the ontology bridges Sage's and CMiC's different code structures through MasterFormat). When the board asks about design-change exposure, he asks Copilot: "What's our total design-related change order cost across the program, broken down by project and trade?" The answer comes back in seconds — $8.2M, 62% in mechanical, with GC2's hospital project at 2.4x the benchmark. He drills in and sees the quality observation data (from Autodesk Build, normalized into the ontology) confirming the pattern: recurring MEP coordination issues flagged over the past 8 weeks. He didn't have to ask either GC for a report. He didn't reconcile a single spreadsheet. The data was just there — structured, current, and queryable — because both GCs' systems feed the same ontology.

---

## Part 1: The Opportunity and Problems to Solve

### The Construction Data Crisis

**The numbers are stark:**
- **18% of project time** is lost just searching for data
- **28% of project time** is wasted on rework caused by information gaps
- **76% of builders** acknowledge they are not fully leveraging historical data
- Construction productivity has grown only **1% annually** over the past 20 years, vs. 3.6% in manufacturing (McKinsey Global Institute)
- The industry generates an estimated **1.8 petabytes** of data annually but uses less than 1% of it for decision-making (IDC)

**Why? Five compounding problems:**
#### Problem 1: System Proliferation Without Integration
A typical commercial construction project involves 12-20 software systems:
- **Design:** Revit, AutoCAD, Bluebeam, Tekla
- **Project Management:** Procore, Autodesk Build, PlanGrid, Fieldwire
- **Scheduling:** Primavera P6, Microsoft Project, Asta Powerproject
- **Estimating:** Sage Estimating, ProEst, PlanSwift, DESTINI
- **Financial/ERP:** Sage 300 CRE, Viewpoint Vista, Foundation, ComputerEase, CMiC
- **Accounting:** QuickBooks, Sage Intacct
- **Field:** Raken, Rhumbix, FieldLens
- **Safety:** iAuditor, SafetyCulture, ComplianceQuest
- **Document Management:** Aconex, Newforma, Box, SharePoint
- **BIM Coordination:** Navisworks, BIM 360 Glue, Solibri
- **Plus:** Email, Excel, PDFs, paper

Each system has its own data model, terminology, and export format. None of them speak the same language.

#### Problem 2: Data Dies at Organizational Boundaries
Construction projects are multi-party by nature:
- **Owners** use one set of tools (cost tracking, scheduling, asset management)
- **GCs** use another (project management, financial controls, field operations)
- **Subcontractors** use another (time tracking, safety, material management)
- **Architects/Engineers** use another (BIM, RFIs, submittals, specs)

Data created by one party is rarely accessible to others in a structured way. An owner can't query a GC's daily log data. A GC can't see a sub's safety violation history across projects. An architect can't track how design changes impact field costs. This isn't a technology problem — it's a data model problem. There's no shared language.

Procore Connect seeks to solve this problem in an opinionated, tool specific, workflow oriented fashion, but doesn't take into account the many systems our customers could be working in.

#### Problem 3: No Lifecycle Continuity
Data generated in preconstruction (estimates, bids, schedules) doesn't flow into construction execution (budgets, daily logs, change orders). Construction data doesn't flow into operations (facility management, maintenance, asset management). Each phase starts from scratch:

```
Preconstruction → [WALL] → Construction → [WALL] → Operations → [WALL] → Renovation
    Estimates          Budgets              Facility Mgmt           New Estimates
    Bid packages       Change orders        Maintenance             New Bids
    Design models      Daily logs           Energy data             New Models
    Site analysis      Inspections          Tenant requests         New Site data
```

The "digital twin" promise was supposed to solve this. It hasn't, because digital twins focused on geometric models (BIM), not operational and financial data. A 3D model of a building tells you nothing about which subcontractor caused the most rework, what the actual cost per square foot was, or how long mechanical inspections typically take.

#### Problem 4: No Standard Taxonomy
Construction has classification systems, but they don't work together and none of them are comprehensive enough:

| Standard | What It Covers | Limitation |
|----------|---------------|------------|
| **MasterFormat** (CSI) | Work results / spec sections (50 divisions) | Cost codes only. No project structure, no relationships, no temporal data |
| **UniFormat** (CSI) | Building systems/assemblies | Design-phase classification. Doesn't map to field execution |
| **OmniClass** (CSI) | Broad taxonomy (14 tables) | Too abstract for operational use. Tables are disconnected from each other |
| **IFC** (buildingSMART) | Building geometry + properties | BIM-centric. Weak on financial, scheduling, field operations data. Extremely complex |
| **COBie** (buildingSMART) | Asset handover data | Narrow scope (closeout only). Spreadsheet-based. Poorly adopted |
| **Project Haystack** | Building systems/IoT data | Operations/facilities only. No construction-phase data |
| **Brick Schema** | Building metadata for HVAC/energy | Even narrower than Haystack — building systems ontology only |
| **GS1/ETIM** | Product/material classification | Procurement only. No project context |

**The gap:** No standard covers the full lifecycle from preconstruction through operations. No standard connects financial data to field data to design data. No standard handles multi-party data sharing with proper ownership and permissions.

#### Problem 5: Excel Is Still the Universal Translator
Because no unified model exists, Excel remains the default integration layer. PMs download data from 3-4 systems, paste it into spreadsheets, manually reconcile, and email results. This creates:
- **Stale data** — exports are outdated the moment they're pulled
- **Version chaos** — which spreadsheet is current?
- **No audit trail** — who changed what, when?
- **No automation** — every report is manually rebuilt
- **No benchmarking** — company knowledge lives in individual spreadsheets, not in a queryable system

### What "Solving This" Actually Means

Solving this does NOT mean:
- Replacing every construction software tool with Procore
- Building another BIM standard
- Creating a data warehouse product

Solving this DOES mean:
- Creating a **canonical data model** — a shared schema that can represent any construction data from any source
- Making it **unopinionated** — it works whether you use Procore or not, whether you're a GC or a sub or an owner
- Making it **full lifecycle** — preconstruction through operations
- Making it **multi-party** — data ownership and sharing work across organizational boundaries
- Making it **extensible** — construction companies have unique processes; the model must accommodate them
- Making it **queryable** — not just a data lake, but a structured, relationship-rich model that enables analytics, AI, and automation

---

## Part 2: What We Would Build

### The Procore Construction Ontology (PCO)

The PCO is a **semantic data model** that defines the entities, relationships, and classification systems needed to represent any construction project's full lifecycle. It extends Procore's existing RAM from an internal analytical model to a universal construction data layer.

### How It Extends the Existing RAM

Procore's RAM is already the most comprehensive structured construction data model in the industry:

**Current RAM Coverage (336 tables, 5 domains):**

| Domain | Tables | What It Models |
|--------|--------|---------------|
| **Core** | 18 | Companies, projects, users, vendors, locations, roles, tools |
| **Finance** | 101 | Budgets, commitments, change orders (CEs, CPCOs, CCOs), direct costs, invoicing, payments, lien waivers, ERPs |
| **Project Execution** | 167 | Daily logs (20+ types), RFIs, submittals, inspections, observations, punch items, drawings, schedule, incidents, coordination, photos, forms, meetings, correspondence |
| **Resource Mgmt** | 43 | Timecards, crews, equipment, T&M, productivity, materials |
| **Precon** | 5+ | Estimates, bids, bid packages, assemblies |

**What makes the RAM strong:**

- **We know how things are related — and that's the hard part.** The RAM doesn't just store tables of data. It encodes how construction actually works as a system of relationships. A change event becomes a potential change order becomes a commitment change order becomes a budget modification. An observation links to a vendor, a location, a spec section, and potentially a change event. A budget line item connects to a WBS code, which connects to a cost code, which maps to a commitment, which maps to a subcontractor. These aren't generic foreign keys — they're construction-specific workflows that took years of working with thousands of contractors to get right. No one starting from scratch — not an AI company, not a startup, not a generic data platform — can reverse-engineer these relationships. They're the product of 20 years of encoding construction domain knowledge into a data model.

  Key relationship chains that only Procore has fully modeled:
  - **Change order cascade:** CE → CPCO → CCO → Budget modification (with deduplication logic, void filtering, and multi-currency handling)
  - **Cost attribution:** Budget line → WBS code → cost code → commitment → vendor → project (full cost-to-trade traceability)
  - **Field-to-financial:** Observation → change event origin → cost impact (field activity directly linked to financial consequence)
  - **Location hierarchy:** 5-level physical space mapping (Building → Floor → Unit → Room → Wall) used by daily logs, inspections, punch items, and submittals
  - **Schedule-to-cost:** Schedule tasks → delays → budget exposure (linking time impacts to dollar impacts)
  - **Vendor performance graph:** Vendor → project assignments → quality observations → safety incidents → change orders → cost performance (a sub's full track record across every project)

- **We already solve permissions and data access at scale — and that's the other hard part.** Building a data model is one thing. Controlling who sees what, at what granularity, across organizational boundaries — that's the problem most data platforms punt on. Procore doesn't. The RAM already handles:
  - **Company-level partitioning** — every table is scoped by `partition_company_id`. A GC's data is isolated from other GCs by default.
  - **Project-level permissions** — `project_users` and `permission_template_name` control what each person can see on each project. A PM sees budget details; a sub sees only their scope.
  - **Role-based access** — `project_role_memberships` with role names and groups (design team, field team, management) determine what data surfaces to whom.
  - **Tool-level gating** — `project_tools` tracks which Procore modules are active per project. No financial tools purchased? Financial data doesn't exist, and the model handles that gracefully.
  - **Vendor-scoped views** — project vendors see their own commitments, invoices, and change orders but not other vendors' data on the same project.

  This is infrastructure that took years to build and battle-test across 17K+ customers. It's not a feature you bolt on — it's foundational to how the data model works. And it's exactly what the ontology needs to extend to multi-party, cross-system data sharing. The permission model is already there. Extending it to say "the owner can see aggregated cost data from the GC's ERP but not line-item sub pricing" is an evolution of what we already do, not a greenfield problem.

- **Field operations depth:** 20+ daily log types, structured observation categories, OSHA-aligned hazard taxonomies, inspection item status tracking
- **Financial specificity:** AIA-style invoicing, retainage tracking, multi-currency support, ERP sync, lien waiver compliance
- **Scale:** 3M+ projects, 40K+ companies, hourly refresh cycles

**What the RAM lacks (and the ontology would add):**

#### Extension 1: External Data Normalization Layer
The RAM models Procore's own data. The ontology adds a **normalization layer** that maps external data sources into the same structure:

```
┌──────────────────────────────────────────────────┐
│              CONSTRUCTION ONTOLOGY                │
│  (Canonical entities, relationships, taxonomy)    │
├──────────────────────────────────────────────────┤
│                                                  │
│   ┌─────────┐  ┌─────────┐  ┌─────────┐        │
│   │ Procore  │  │ Sage    │  │ P6      │  ...   │
│   │ Adapter  │  │ Adapter │  │ Adapter │        │
│   └────┬────┘  └────┬────┘  └────┬────┘        │
│        │            │            │               │
├────────┼────────────┼────────────┼───────────────┤
│        ▼            ▼            ▼               │
│   Procore API   Sage 300 CRE   Primavera P6     │
│   Procore DB    Viewpoint      MS Project        │
│                 CMiC           Asta               │
│                 Foundation     Phoenix            │
│                 QuickBooks                        │
└──────────────────────────────────────────────────┘
```

Each adapter maps a source system's schema to the canonical ontology. For example:
- Sage 300 CRE `JC_COST_DETAIL` → ontology `actual_cost` entity
- Primavera P6 `TASK` → ontology `schedule_activity` entity
- Viewpoint Vista `APInvoice` → ontology `subcontractor_invoice` entity
- Procore `change_events` → ontology `change_event` entity (already native)

**This is what Datagrid enables.** The data connectors provide the pipes; the ontology provides the schema.

#### Extension 2: Multi-Party Data Model
The RAM is company-scoped (`partition_company_id` on every table). The ontology adds a **project-centric, multi-party layer**:

```
PROJECT (canonical)
├── OWNER data (cost tracking, milestones, cash flow)
├── GC data (field operations, financial controls, safety)
│   ├── Sub A data (labor, equipment, materials)
│   ├── Sub B data (labor, safety, quality)
│   └── Sub C data (T&M, schedule)
├── A/E data (design changes, RFIs, submittals, specs)
└── SHARED data (schedule, budget baseline, milestones)
```

Key concepts:
- **Data ownership:** Each party owns their data. Sharing is explicit, permissioned, and auditable.
- **Data federation:** Queries cross organizational boundaries with proper authorization (an owner can see aggregated GC data but not line-item sub costs unless shared).
- **Entity resolution:** The same subcontractor appears differently in the owner's system vs. the GC's system vs. their own system. The ontology resolves these to a single canonical entity.

#### Extension 3: Lifecycle Continuity
The RAM covers construction execution. The ontology extends backward to preconstruction and forward to operations:

```
PRECONSTRUCTION                CONSTRUCTION              OPERATIONS
─────────────────────          ──────────────────        ──────────────
Conceptual estimate     →      Budget baseline    →     Actual cost record
Bid packages            →      Commitments        →     Warranty tracking
Design model (IFC)      →      Shop drawings      →     As-built model
Site conditions         →      Daily logs          →     Facility condition
Permit requirements     →      Inspections         →     Compliance records
Preliminary schedule    →      Baseline schedule   →     Maintenance schedule
```

This means:
- An estimate line item flows into a budget line item flows into an actual cost
- A bid package becomes a commitment becomes a payment history
- A design element becomes a punchlist item becomes an asset record
- A permit requirement becomes an inspection checklist becomes a compliance certificate

#### Extension 4: Unified Classification System
The RAM uses Procore's internal taxonomy (cost codes, WBS codes, budget codes). The ontology adds mappings to industry standards:

```
Ontology Entity: "Mechanical Rough-In — HVAC Ductwork"
├── MasterFormat: 23 31 00 (HVAC Ducts and Casings)
├── UniFormat: D30 (HVAC)
├── OmniClass: 22-03 30 (Mechanical Distribution)
├── IFC: IfcDuctSegment
├── Procore cost code: Company-specific
├── Sage cost code: Company-specific
└── Custom: Customer-defined
```

This enables:
- **Cross-company benchmarking** — compare "HVAC rough-in" costs even when companies use different cost code structures
- **Cross-system reporting** — unify Procore budgets with Sage actuals using MasterFormat as the bridge
- **Automated classification** — new data entering the system gets auto-tagged with standard codes

#### Extension 5: Temporal and Versioning Model
Construction data changes constantly. The ontology makes time a first-class concept:
- **Point-in-time queries:** "What was the budget on March 1st?"
- **Change attribution:** "Who changed this, when, and why?"
- **Trend analysis:** "How has this cost code's forecast changed over the past 6 months?"
- **Snapshot comparison:** "Compare bid-day estimate to current forecast to final actual"

The RAM's `budget_snapshot_line_items` and `history` table hint at this, but the ontology makes it systematic across all entities.

### Technical Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    CONSUMPTION LAYER                             │
│  Procore Analytics │ Insights │ Hub Pages │ AI Agents │ API     │
├─────────────────────────────────────────────────────────────────┤
│                    INTELLIGENCE LAYER (Helix)                    │
│  Benchmarks │ Predictions │ Anomaly Detection │ Recommendations │
├─────────────────────────────────────────────────────────────────┤
│                    ONTOLOGY LAYER (NEW)                          │
│  Canonical Entities │ Relationships │ Taxonomy │ Permissions     │
│  Entity Resolution │ Lifecycle Links │ Temporal Model           │
├─────────────────────────────────────────────────────────────────┤
│                    NORMALIZATION LAYER (Datagrid-powered)        │
│  Source Adapters │ Schema Mapping │ Quality Scoring │ CDC        │
├─────────────────────────────────────────────────────────────────┤
│                    SOURCE SYSTEMS                                │
│  Procore │ Sage │ Viewpoint │ P6 │ Revit │ Excel │ Custom      │
│  (via Data Connectors + Cloud Connector + Datagrid)             │
└─────────────────────────────────────────────────────────────────┘
```

### Core Ontology Entities (Conceptual)

Based on extending the RAM's existing structure:

**Project Core**
- `Project` — canonical project record (extends `core.projects`)
- `Organization` — company/party (extends `core.companies` + external orgs)
- `Person` — individual across organizations (extends `core.users`)
- `Location` — hierarchical place (extends `core.locations`)
- `Contract` — agreement between parties (extends `finance.commitments` + `finance.prime_contracts`)

**Financial**
- `BudgetLine` — planned cost allocation (extends `finance.budget_line_items`)
- `ActualCost` — realized expenditure (unifies `change_events`, `commitment_change_orders`, `direct_costs`, `erp_job_costs`)
- `Invoice` — billing document (extends owner + sub invoices)
- `Payment` — money movement (extends `finance.payments_*`)
- `ChangeProposal` — proposed modification (extends `change_events` + `commitment_potential_change_orders`)
- `ChangeOrder` — approved modification (extends `commitment_change_orders` + `prime_contract_change_orders`)
- `CostCode` — classification (bridges MasterFormat, UniFormat, company-specific codes)

**Field Operations**
- `DailyRecord` — daily log entry (unifies 20+ daily log types)
- `Issue` — problem requiring resolution (unifies RFIs, observations, punch items, coordination issues)
- `Inspection` — compliance check (extends `inspections` + `inspection_items`)
- `Incident` — safety event (extends `incident` + related tables)
- `Submittal` — approval workflow item (extends `submittals`)
- `Drawing` — design document (extends `drawing_revision`)

**Schedule**
- `Activity` — scheduled work (extends `schedule_task` + external schedule data)
- `Milestone` — key date (derived from activities + contract dates)
- `Delay` — schedule impact event (extends `daily_log_delay`)

**Resources**
- `LaborEntry` — work hours (extends `timecard_entries` + external time systems)
- `Equipment` — machinery/tools (extends `workforce.equipment`)
- `Material` — physical goods (extends `workforce.materials` + procurement)
- `Crew` — work team (extends `workforce.crew_memberships`)

**Design (new domain)**
- `DesignElement` — BIM object or drawing element (from IFC/Revit via connectors)
- `Specification` — performance/material requirement (extends `specification_sections`)
- `Clash` — design conflict (extends `coordination_issue`)

**Operations (new domain)**
- `Asset` — physical building component (derived from design elements at handover)
- `MaintenanceOrder` — work order on asset
- `WarrantyItem` — guarantee on installed work
- `FacilityCondition` — assessment of asset state

### Why "Unopinionated" Matters

The ontology must be **unopinionated** in three ways:

1. **Source-agnostic:** It doesn't favor Procore data over Sage data or P6 data. All sources map to the same canonical model with equal fidelity.

2. **Workflow-agnostic:** It doesn't enforce a particular change order process or approval chain. It captures what happened, regardless of the workflow that produced it.

3. **Role-agnostic:** It serves owners, GCs, subs, and A/E firms equally. The same ontology can power an owner's capital program dashboard and a sub's labor productivity report.

This is critical because:
- Customers won't adopt a data model that's biased toward one source system
- Construction workflows vary dramatically by company, project type, and geography
- The value of a universal model comes from network effects — the more parties that contribute data, the more valuable it becomes for everyone

### Flexible, Unopinionated UIs on Top

If the ontology is the hard, durable layer — the UI layer above it should be the opposite: thin, flexible, and composable. The ontology doesn't prescribe how you look at the data. It just makes the data available, structured, and queryable. What you build on top is up to you.

This is already the direction Procore's own products are heading:

**Products we have today that point here:**
- **Hub Pages** — canvas-based, drag-and-drop home pages. Users compose their own view from widgets. No fixed layout, no prescribed workflow. An owner's hub page looks nothing like a super's.
- **Pages** — document-style surfaces with embedded live data. A PM creates a project status page by dropping in data components — tables, charts, text, images — in whatever arrangement makes sense for their audience. The page is the UI; the ontology is the data.
- **Dataset Editor** — users define their own datasets by selecting entities, fields, and relationships from the data model. They're building their own views of the ontology without writing SQL.
- **Analytics** — interactive dashboards. Already unopinionated in the sense that users build what they need.
- **Insights** — automated, pre-built analysis cards. The ontology makes these dramatically more powerful because they can draw from normalized multi-system data, not just Procore's slice.
- **Tool Studio** — lets customers build custom tools and workflows on top of Procore's platform without writing code. This is the clearest signal: Procore is already moving from "we build the tools" to "we give you the platform to build your own." With the ontology underneath, Tool Studio becomes a construction app builder that can access data from any connected system, not just Procore modules.

**Where this goes with the ontology:**

The ontology turns these products from "Procore data visualization tools" into "construction data composition surfaces." The shift:

| | Today | With Ontology |
|---|---|---|
| **Hub Pages** | Widgets show Procore data | Widgets show data from ANY connected system — ERP cost summaries next to Procore field data next to P6 schedule milestones, all on one canvas |
| **Pages** | Embedded Procore tables and charts | Embedded data from the full ontology — a project status page that combines Procore observations, Sage committed costs, and P6 critical path in one document |
| **Dataset Editor** | Build datasets from Procore entities | Build datasets from the canonical ontology — join Procore daily logs with Viewpoint job costs with P6 schedule tasks, because they all map to the same model |
| **Analytics** | Dashboards on Procore data | Dashboards on the full construction data estate. Cross-system, cross-org, cross-lifecycle |
| **Insights** | Automated cards from Procore signals | Automated cards from ALL signals — rework insights that combine Procore observations with ERP cost actuals with schedule delays from P6 |
| **Tool Studio** | Build custom tools on Procore data and workflows | Build custom construction apps on the full ontology — a GC builds a sub performance tracker pulling from Procore quality data + ERP cost data + scheduling milestones, no code required |
| **Cloud Connector** | Export Procore data to customer BI tools | Export the full normalized ontology — customers build their own UIs in Power BI, Tableau, Looker, or custom apps, all against the canonical model |

**And then AI composes the UI itself:**

This is the final move. When the ontology makes all construction data structured and queryable, and the UI primitives (Hub Pages, Pages, widgets, charts, tables) are composable building blocks — AI can assemble the right view for the right person at the right moment:

- A PM asks "show me everything at risk on this project" → an agent queries the ontology across financial, schedule, quality, and safety signals, then composes a Hub Page with the relevant widgets, pre-filtered and prioritized
- An owner says "I need a board report on the capital program" → an agent pulls cross-project data from the ontology and assembles a Pages document with embedded charts, variance tables, and narrative summaries
- A super walks onto a jobsite → their mobile hub page auto-populates with today's relevant data: crew assignments (from workforce), open inspections (from PM), weather delays (from daily logs), material deliveries due (from submittals) — sourced from whatever systems those data points live in

The UI becomes a runtime that the ontology populates and AI assembles. Procore doesn't need to anticipate every possible view or build every possible dashboard. It needs to:
1. **Get the data model right** (the ontology)
2. **Build composable UI primitives** (Hub Pages, Pages, widgets, Dataset Editor)
3. **Let AI and users compose** whatever they need on top

This is what "unopinionated UI" means in practice. The ontology doesn't care how you consume it. The UI primitives don't enforce a workflow. The intelligence layer (Helix + agents) connects the two — understanding what data matters for this person, in this role, on this project, right now, and composing the right surface to show it.

---

## Part 3: What This Unlocks for Procore

### Unlock 1: Data Gravity — Procore Becomes the Construction Data Hub

This is the central thesis. Everything else flows from it.

**Today:** Procore is one of 12-20 systems on a project. Customers extract data from Procore to combine with other sources in Excel or BI tools. Procore competes on features — better PM tools, better financial controls, better field apps. But in a world where AI commoditizes UI and workflow, feature competition is a treadmill.

**With the ontology:** Procore becomes the place where ALL project data lives in a unified model. Data flows IN from other systems (via Datagrid connectors), gets normalized to the canonical model, and gets consumed through whatever interface the customer wants — Procore's own products, third-party BI tools, AI-generated dashboards, or custom applications.

**The data hub model inverts Procore's competitive dynamics:**

| | Today (Tool Company) | With Ontology (Data Hub) |
|---|---|---|
| **What we sell** | PM, financial, field, analytics tools | The canonical construction data model + intelligence |
| **How we win** | Better features than competitors | Data gravity — all roads lead to the ontology |
| **Lock-in mechanism** | Workflow adoption, user habits | Normalized data from 10+ systems. Leaving = re-fragmenting everything |
| **AI advantage** | Procore data only | Complete project data from all connected systems |
| **Network effects** | More Procore users = more value | More connected systems AND more participating companies = exponentially more value |
| **Competitor response** | Build similar features | Cannot replicate the data model + data + relationships. Would need to start from scratch |
| **Revenue model** | Per-user SaaS subscriptions | Subscriptions + connector marketplace + benchmarking + platform API + Cloud Connector premium |

**Why the data hub is defensible when UIs are not:**
- AI can generate a dashboard in 30 seconds. It cannot generate 336 tables of construction-specific relationships, 20 years of structured project data, or entity resolution across 40K+ companies.
- A competitor can clone Procore's UI. They cannot clone the ontology populated with a customer's normalized data from Sage + P6 + SafetyCulture + Viewpoint + Procore.
- As LLMs get better at building interfaces, the value of the interface layer drops. The value of the structured data layer underneath rises proportionally.

### Unlock 2: Cross-Organizational Analytics

**Today:** An owner can't compare GC performance across projects unless they manually collect data. A GC can't benchmark subs across projects without spreadsheet gymnastics.

**With the ontology:**
- **Owner dashboards:** Real-time visibility into GC performance, budget adherence, schedule performance — across all their projects, regardless of which PM tools each GC uses
- **GC benchmarking:** Compare sub performance (cost, quality, safety, schedule) across all projects, even if subs use different systems
- **Sub self-service:** Subs see their own performance benchmarked against peers (anonymized), driving competitive improvement
- **Insurance/surety analytics:** Risk profiles based on actual project data, not self-reported questionnaires

This directly addresses the collaboration problem between owners, GCs, and subs by giving each party the right view of shared project data.

### Unlock 3: The Data Hub Makes Us the Agentic Hub

**Today:** Procore's AI (Helix, Agents, Copilot) works with Procore data only. Agent Builder lets customers create automations, but agents can only see and act on Procore's slice of the project. Every integration to an external system is a separate, bespoke connector.

**With the ontology, Procore becomes the agentic runtime for construction:**

**Agents get a complete world model.** An RFI agent doesn't just check Procore — it checks the schedule (from P6), checks the budget impact (from Sage), drafts the RFI (in Procore), and notifies the architect (in their system). All data maps to the same model, so the agent reasons across the full project, not just one system's view of it.

**Agents get smarter predictions.** Rework cost predictions use Procore observations AND Sage cost actuals AND P6 schedule data, not just the Procore slice. Risk models draw on the complete picture.

**Copilot answers whole questions.** "What's the total committed cost for mechanical including approved change orders?" can be answered even when commitments are in Procore and ERPs are in Viewpoint, because both map to the same `ActualCost` entity.

**Third-party agents target our ontology.** When the construction ontology becomes the standard data layer, every AI company building construction agents builds against OUR model. Insurance companies, estimating tools, safety platforms, scheduling optimizers — they all write agents that consume and produce data through the ontology. Procore becomes the platform agents are built FOR, not just one of many systems agents connect TO.

**The flywheel:**
```
More data in the ontology → agents are more capable →
more agents built on the ontology → more data flows in →
Procore becomes the indispensable infrastructure layer
```

This is why data hub and agentic hub are the same thing. You can't be the agentic hub without the data. And once you're the data hub, becoming the agentic hub is a natural extension — agents need structured data to reason against, and the ontology is that structure.

### Unlock 4: The Construction Data Platform Business

**Today:** Procore monetizes through SaaS subscriptions for project management, financials, and analytics tools.

**With the ontology, new revenue streams emerge:**

1. **Data Connector Marketplace:** Charge for pre-built adapters to common systems (Sage, Viewpoint, P6, etc.). Datagrid's connector technology already exists.

2. **Cloud Connector Premium:** The existing Delta Share-based Cloud Connector exposes Procore data. With the ontology, it exposes a customer's ENTIRE normalized dataset — orders of magnitude more valuable.

3. **Benchmarking-as-a-Service:** Anonymized cross-company benchmarks powered by the ontology's unified classification. "Your mechanical rough-in cost is $28/SF vs. industry median $24/SF for similar commercial projects in the Southeast."

4. **Data Quality Scoring:** Rate the completeness, timeliness, and accuracy of a customer's data across all connected systems. This drives adoption of better data practices (and more Procore tool usage).

5. **Partner API:** Third-party analytics tools, AI companies, and insurance/surety firms query the ontology via API. Procore becomes the data infrastructure layer that others build on.

### Unlock 5: Lifecycle Value Capture

**Today:** Procore primarily captures value during the construction phase. Preconstruction is emerging (Precon SKU). Operations is a blank space.

**With the ontology:**
- **Preconstruction → Construction:** Estimates automatically seed budgets. Bid results flow into committed costs. Design decisions link to budget impacts. This makes the Precon SKU dramatically more valuable.
- **Construction → Operations:** As-built data (actual costs, installed materials, inspection results, warranty info) flows to facility management systems. This creates a new touchpoint with owners AFTER project completion.
- **Operations → Renovation:** When a building is renovated, historical construction data (original costs, materials, issues) is available without archaeology. This starts the next project with better data.
- **Portfolio learning:** Company-wide patterns emerge across project lifecycles. "Our healthcare projects average 3.2% rework, primarily in MEP, with design changes as the leading cause, and the rework typically surfaces 60% through the schedule."

### Unlock 6: Solving the Real Competition

The CLAUDE.md states the real competition is customer inaction — "most customers don't use data enough." The ontology directly attacks this:

1. **Lower the setup cost:** Instead of manually configuring reports and dashboards from scratch, a normalized data model enables pre-built analytics that work out of the box with any combination of source systems.

2. **Make data entry someone else's problem:** Data doesn't have to originate in Procore. If a sub tracks safety in SafetyCulture and a GC tracks costs in Sage, both can flow into the ontology automatically. The PM doesn't need to re-enter anything.

3. **Show value before full adoption:** Customers see value as soon as they connect ANY data source. They don't need to fully adopt Procore across all tools first. This is a Trojan horse strategy — start with data, expand to tools.

4. **Cross-company standards create peer pressure:** When an owner requires their GCs to connect to the ontology, GCs comply. When a GC requires subs to connect, subs comply. Network effects drive adoption from the top down.

### Unlock 7: Competitive Positioning Shift

**Current positioning:**
- vs. Excel: "Real-time, centralized, multi-project"
- vs. Autodesk: "Better PM and financial data"
- vs. Generic AI: "Proprietary construction data"

**With ontology positioning — Procore is the data hub AND the agentic hub for construction:**
- vs. Excel: "The industry's data infrastructure — Excel can't normalize 15 systems into one model, and agents can't run on spreadsheets"
- vs. Autodesk: "We unify ALL construction data, not just BIM. Connect Autodesk data INTO Procore's ontology. Our agents operate across the full project, not just the design phase."
- vs. Oracle: "Modern, cloud-native, open. Oracle locks data in; we connect everything. Our agent ecosystem is open — anyone can build construction agents on our ontology."
- vs. Generic AI: "ChatGPT can answer questions about construction. Procore agents can act on your actual project data — across every system you use — because they run on the construction ontology."
- vs. Everyone: "The construction data standard. The construction agent runtime. Build on us."

**The positioning ladder:**
1. **Tool** (where most see us today) → "Procore is the best construction PM platform"
2. **Data hub** (near-term shift) → "Procore is where all your construction data comes together"
3. **Agentic hub** (the unlock) → "Procore is where construction agents live — reading, reasoning, and acting across your entire project data estate"
4. **Industry standard** (long-term) → "Procore's ontology is the construction data model. Everything else plugs in."

---

## Implementation Considerations

### Phase 1: Extend the RAM (6-12 months)
- Formalize the RAM's entity model as a published ontology specification
- Add classification system mappings (MasterFormat, UniFormat, OmniClass)
- Build the normalization layer for top 5 external source systems (Sage 300, Viewpoint Vista, P6, QuickBooks, Excel/CSV)
- Pilot with 10-20 customers who use Procore + ERP + scheduling

### Phase 2: Multi-Party Model (12-18 months)
- Add cross-organizational data sharing with permissions
- Build entity resolution (matching the same vendor across systems)
- Launch owner-GC-sub analytics use cases
- Extend to 15+ source system adapters

### Phase 3: Full Lifecycle (18-24 months)
- Add operations domain entities (asset management, maintenance, warranty)
- Build preconstruction → construction → operations data bridges
- Partner with CMMS/CAFM vendors for operations data connectors
- Launch lifecycle analytics and benchmarking products

### Phase 4: Platform (24+ months)
- Open the ontology specification for public contribution
- Launch partner API for third-party applications
- Build data quality marketplace
- Industry standard adoption campaign (construction industry equivalent of FHIR in healthcare)

### Risks
- **Adoption chicken-and-egg:** The ontology is only valuable with data in it. Customers won't invest in connecting data until they see value. Procore's 17K existing customers + native data gives a head start.
- **Connector maintenance:** Each source system adapter needs ongoing maintenance as those systems evolve. Datagrid's architecture should handle this, but it's an operational cost.
- **Standards politics:** Existing standards bodies (CSI, buildingSMART) may resist a proprietary ontology. Consider open-sourcing the core specification while keeping the implementation commercial.
- **Complexity:** An ontology that's too complex won't be adopted. The "unopinionated" principle must be enforced ruthlessly — model what IS, not what SHOULD BE.

---

## Why Now?

Three forces converge in 2026:

1. **Datagrid acquisition complete.** The data connector infrastructure exists. Before Datagrid, this was a "build the pipes first" problem. Now it's a "what flows through the pipes" problem.

2. **AI requires complete data.** Procore's AI strategy (Helix, Agents, Copilot) is bounded by data completeness. Every customer has data in systems Procore doesn't control. The ontology makes AI work with ALL of a customer's data, not just the Procore slice.

3. **Industry is ready.** The 53% workforce retirement by 2036, rising project complexity, and margin pressure mean construction companies MUST get better at using data. The question isn't whether — it's who provides the data infrastructure. If Procore doesn't, someone else will try (and likely fail, because they don't have the existing data gravity).

---

## The Bottom Line

Every SaaS company is about to face the same reckoning: AI makes building interfaces trivial, so what's left to compete on? The answer is data — the model, the relationships, the domain knowledge encoded in the schema.

Procore already has the most comprehensive construction data model in the industry (336 tables, 5 domains, 3M+ projects). Extending it into an unopinionated, full-lifecycle ontology transforms Procore from "the best construction project management platform" into "the construction data infrastructure that everything else runs on."

The RAM is the foundation. Datagrid is the plumbing. Helix is the intelligence. The ontology is the missing piece that connects them into something no one else can replicate.

When anyone can build a construction app with a prompt, the company that owns the canonical data model wins. That should be Procore.
