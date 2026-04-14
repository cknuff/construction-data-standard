# Palantir Construction Ontology: Research Brief

**Date**: 2026-03-23

---

## What Palantir Built for Construction

**"Palantir for Construction"** launched as a vertical offering in early 2026, built on their existing Foundry + AIP platforms. It's not a new product — it's their general-purpose platform configured for construction.

**Customers**: Thomas Cavanagh Construction (flagship, Canadian GC), EllisDon, FLINT, Jacobs, Lennar, Asplundh, The Nuclear Company. Heavy Canadian GC skew — suggests a single sales beachhead, not broad market penetration yet.

**8 functional modules**: Estimating, Procurement, Labor, Equipment, Subcontractors, Project Management, Production/Execution, Back Office. They cover high-level operational workflows (automated takeoffs, three-way match reconciliation, equipment dispatch, supplier scoring, digital timecards).

**What they DON'T cover**: Daily logs, RFIs, submittals, punch lists, observations, inspections — the granular PM workflows that are Procore's core. They position as a layer ON TOP of tools like Procore, not a replacement.

**GTM**: Enterprise-only, no self-service, $1M+ annual contracts, "AIP Bootcamp" model (hands-on with real customer data, proof-of-value in 2 days). No public pricing.

### Claimed Results

| Metric | Claim | Attribution |
|--------|-------|-------------|
| $161M | Supply chain and inventory cost savings | Over 3 years (customer not named) |
| $126M | Procurement cost savings | 315% ROI, <6-month payback (unnamed) |
| 40% | Reduction in material shortages | Unattributed |
| 1 hour to 5 min | Foremen timecard collection | Thomas Cavanagh Construction |
| Days to real-time | Project reporting | Unattributed |

### Customer List Detail

| Customer | Type | Notes |
|----------|------|-------|
| Thomas Cavanagh Construction | GC (heavy civil, Canadian) | Flagship reference; keynote, podcast, blog |
| EllisDon | Large GC (Canadian, top ENR) | No public case study details |
| Jacobs | E&C / engineering firm | Case study focuses on water treatment, not construction |
| FLINT | Industrial contractor (Canadian) | No public case study details |
| Lennar | Homebuilder (US, Fortune 500) | No public case study details |
| Asplundh | Infrastructure services / utility | No public case study details |
| The Nuclear Company | Nuclear construction | No public case study details |

No specialty trade contractors. No US-based GCs. No owner/developer customers visible.

---

## What the "Ontology" Actually Is

Palantir's ontology is **not** a database, not a data warehouse, not a knowledge graph. It's a **semantic + operational metadata layer** that sits between raw data and applications/AI.

### The Three Layers

1. **Semantic** (what things ARE): Typed business objects with named properties and relationships. A "Project" has a "total_value" and links to "Vendors" and "ChangeOrders." The ontology knows the domain — it's not tables and columns, it's business entities.

2. **Kinetic** (what things DO): Actions — validated, parameterized business operations like "Approve Change Order" or "Reassign Superintendent." These aren't just CRUD. They have input validation, business rules, side effects, and audit trails. This is what makes it operational, not just analytical.

3. **Dynamic** (how things CHANGE): Real-time integration with operational systems and AI agents. WebSocket-based live updates, event-driven automation, streaming data processing.

### The Building Blocks

**Object Types**: The entity definitions (Project, ChangeOrder, Vendor). Each has typed properties, a backing dataset (Spark table, virtual table), and a primary key. The ontology is a *projection* — it doesn't duplicate data, it maps to where data already lives.

**Links**: First-class typed relationships between objects. Not implicit foreign keys — explicitly named, traversable edges. `Project --HAS_VENDOR--> Vendor`, `ChangeEvent --ORIGINATED_FROM--> RFI`. Applications and AI can navigate these without knowing any SQL.

**Actions**: Write operations with validation + audit. `approveChangeOrder(orderId, approverNote)` is a typed operation the ontology validates before executing. This is what makes AI operational — the LLM calls actions, not SQL.

**Functions**: TypeScript/Python business logic for computed properties and complex operations. Deterministic guardrails that complement AI reasoning.

**Permissions**: Object-level, property-level, action-level access control. A superintendent's AI agent sees different data than a CFO's.

### Technical Architecture

```
Applications / AI Agents / Partner Integrations
    |
ONTOLOGY LAYER (object types, links, actions, permissions)
    |
Resolution Engine (maps ontology to storage)
    |
Storage (warehouse, graph DB, operational DB, external systems)
```

Below the ontology: Raw data integration. 300+ connectors. Batch pipelines (Spark), streaming (Flink), CDC, virtual tables pointing to external warehouses (BigQuery, Snowflake, S3).

The ontology itself: Typed, relationship-rich, action-enabled data model that maps cleaned datasets to business entities.

Above the ontology: Applications (Workshop, Object Explorer, custom OSDK apps), AI agents (AIP), functions, and operational workflows.

### How Data Maps to Ontology Objects

1. **Ingest**: 300+ connectors bring raw data into Foundry as datasets
2. **Transform**: Pipelines clean, join, aggregate (Spark, Flink, SQL, Python)
3. **Map to Ontology**: Each object type gets a backing dataset, property mappings, primary key, search config, security policies
4. **Define Links**: Relationship types configured between object types (similar to FK but first-class)
5. **Define Actions**: Parameterized operations with validation rules and write-back logic
6. **Consume**: Apps, AI agents, and operators interact via OSDK (TypeScript/Python), REST APIs, Workshop, or AIP

### How the Ontology Enables AI (AIP)

This is where the strategic significance lives:

- **Tool Factory**: Existing ontology objects, actions, and functions become "AI-tuned tools" that LLMs can call. An Action like "Reassign Work Order" becomes a tool an AI agent invokes.
- **Grounding**: The LLM reads the ontology to understand "a ChangeOrder has a cost_amount and links to a Project and Vendor." No hallucination about data structure.
- **Navigation**: Multi-hop reasoning — "start at this budget variance, follow to the change order, follow to the vendor, check their other projects."
- **Validated Actions**: The LLM calls `flagSafetyHazard(projectId, description)` as a validated tool — not just answering questions, taking action with guardrails.
- **Permission-Aware**: AI respects access controls automatically. A subcontractor's agent only sees their own data.
- **Audit Trail**: Every AI action is tracked — who, what, when, why.

---

## How It Differs from Standard SaaS Architecture

| Dimension | Standard SaaS (Procore today) | Palantir Ontology |
|-----------|------|------|
| Data model | Tables and columns (technical) | Objects and relationships (semantic) |
| Relationships | Foreign keys, implicit JOINs | First-class typed links with properties |
| Schema knowledge | Locked inside application code | Externalized, queryable, self-describing |
| API contract | Endpoint-per-resource (GET /projects) | Uniform object/link/action API across all types |
| Cross-domain queries | Requires knowing which tables to JOIN | Navigate relationships without SQL knowledge |
| Actions | Custom endpoint per operation | Typed action framework with validation + audit |
| AI accessibility | AI must learn your specific API | AI reads the ontology to understand what exists and what it can do |
| Permissions | Role-based at endpoint level | Object/property/action-level, classification-aware |

## How It Differs from a Knowledge Graph

| Dimension | Knowledge Graph (Neo4j, RDF) | Palantir Ontology |
|-----------|------|------|
| Read vs. Write | Read-heavy, query-focused | Read AND write through typed Actions |
| Schema | Often schema-flexible (triples) | Strongly typed object types with validation |
| Actions/Mutations | No native action model | First-class Actions with validation, parameters, audit |
| Application layer | Requires separate app framework | Built-in SDK (OSDK) with type-safe code generation |
| AI integration | Can be used as LLM context | Actions become AI tools; full governance system |
| Backing store | Graph database | Backed by datasets (Spark/Iceberg) — NOT a separate graph store |
| Business logic | Not native | Functions (TypeScript/Python) embedded in the ontology |

---

## Construction-Specific Details

### Objects They Model

Explicitly named: Projects, Activities, Equipment, Subcontractors, Budget line items, Phases, Schedules, Stakeholders.

Implied from functional modules: Materials/inventory, Contracts, Purchase orders/invoices, Timecards, Change orders, Drawings/3D models, Specifications, RFQs, Vendor performance scores, Scope of work documents.

**Key point**: Palantir does NOT publish a fixed construction ontology schema. They define object types per customer deployment. The objects above are from marketing — the actual ontology for EllisDon differs from Lennar's.

### Construction Workflows Enabled

| Module | Key Actions |
|--------|------------|
| Estimating | Automated takeoffs from drawings, spec extraction, risk flagging |
| Procurement | Three-way match (PO/invoice/receipt), contract clause extraction, material forecasting |
| Labor | Digital timecards, recruiting automation, HR integration |
| Equipment | Utilization analytics, intelligent dispatch, fleet management |
| Subcontractors | Supplier 360 scoring, LLM-powered scope generation, payment tracking |
| Project Management | Project 360 unified view, schedule-budget integration, resource planning |
| Production | Real-time job costing, immediate change order capture, buyout-to-closeout |
| Back Office | AP/AR automation, payroll from timecards, invoice generation |

### Comparison to IFC/buildingSMART

| Dimension | Palantir Ontology | IFC Standard |
|-----------|------------------|--------------|
| Scope | Business operations (cost, schedule, labor, procurement) | Physical building model (geometry, materials, spatial structure) |
| Schema | Custom per deployment | Universal standard — 1,300 entities |
| Primary data | Financial, schedule, workforce transactions | 3D geometry, building components |
| Real-time | Yes — streaming, event processing | No — static file exchange |
| AI/ML | Core capability | Not part of the standard |
| Target users | PMs, estimators, procurement, executives | Architects, engineers, BIM coordinators |

Palantir does NOT reference IFC or buildingSMART anywhere. Their ontology covers how a building gets BUILT (operations), not what a building IS (design). These are complementary, not competing.

---

## What This Means for Procore

### They're competing at OUR layer, not the PM layer
Palantir isn't building daily logs or punch lists. They're building the data integration, analytics, and intelligence layer — exactly what Reporting, Analytics, Insights, Hub Pages, Data Connectors, and Cloud Connector cover.

### They need OUR data to succeed
Palantir's Construction Ontology requires data FROM project management tools. They either integrate with Procore via API, get customers to export, or build their own PM layer — option 3 is years away. We control the data supply.

### Our moat is the cross-company view
Palantir sees one company's data at a time. We see the industry. Our benchmarks (rework cost percentiles, quality issue patterns by project type, material delay rates) are built from thousands of companies. Palantir can never replicate that from single-customer deployments.

### The real risk
The risk isn't replacement — it's commoditization. If Palantir becomes the analytics layer for top-100 contractors, Procore gets reduced to "the system that captures data" rather than "the system that drives decisions." That's why the Insights and curated datasets strategy matters.

### Where Palantir's approach is instructive

1. **The ontology concept itself.** Named business objects with typed relationships and governed actions is a powerful abstraction. Our data models already do this — but we could make it more explicit and AI-consumable.
2. **Cross-system data unification.** Same need our Data Connectors and Cloud Connector serve. Palantir provides integration AND analytics; we provide the data and let customers do the integration.
3. **LLM-powered scope generation.** Using LLMs + historical docs to generate scopes of work — concrete use case we could replicate with our own document data.
4. **Supplier 360 pattern.** Cross-project vendor intelligence with performance scoring — exactly the kind of curated dataset we could build with far MORE data than any Palantir deployment.
5. **"Field-first" language.** Their emphasis on replacing paper and capturing data on-site aligns with the "enable customers where and when they need it" principle.

---

## What We Could Build to Replicate This

### What We Already Have

- **366 tables across 6 schemas** in Databricks = candidate object types
- **Column metadata** with types = property definitions
- **Foreign keys** (project_id, company_id, wbs_code_id) = implicit relationship graph
- **Validated business rules** from insight work (CE/CCO dedup, observation leading indicators, delay_type enums) = ontology constraints
- **Data Connectors + Cloud Connector** = external data integration
- **Cross-company data** = benchmarking moat Palantir doesn't have

### What We'd Need to Build

#### Phase 1 — Ontology Schema Registry (3-6 months)

Formalize our data model as a machine-readable, self-describing registry:

- JSON/YAML definitions of every object type (Project, ChangeOrder, Vendor...) with typed properties
- Explicit relationship definitions (not just foreign keys — named, directed links with cardinality)
- Business rule annotations (CE/CCO deduplication logic, financial tool availability flags, tier classification rules)
- This is metadata only — no new infrastructure

#### Phase 2 — Resolution Engine + API (6-12 months)

Build a layer that translates ontology concepts to warehouse queries:

- GraphQL or similar API that speaks in business terms ("give me this project's change orders with vendor details") and compiles to SQL/Spark
- Relationship traversal without requiring consumers to know join paths
- This is what AI agents and applications consume

#### Phase 3 — Action Framework (12-18 months)

Add the operational layer:

- Typed actions with validation, parameters, and audit trails
- Write-back to operational systems
- Ontology-aware permissions (object/property/action level)
- This is what makes it operational, not just analytical

#### Phase 4 — AI-Native Consumption (ongoing)

- Actions become "tools" for AI agents
- Ontology provides self-describing context for LLMs
- Agents can navigate relationships and take validated actions
- Insights product becomes the AI that operates on the ontology

### Technology Recommendation

**Don't buy Palantir or add a graph database.** Build incrementally on what exists:

- Keep data in Databricks (already there, 366 tables)
- Build the ontology as a **metadata layer + API** on top
- Relationship traversal via SQL joins is fine to start — graph DB only if specific traversal patterns become bottlenecks
- The ontology schema registry is the critical first step — it makes everything else possible

### Technology Comparison

| Capability | Palantir | Snowflake Cortex | dbt MetricFlow | Stardog | Build Our Own |
|-----------|----------|-----------|-----|---------|---------|
| Object types | Yes | Tables | Entities | Classes (OWL) | Yes (YAML/JSON) |
| Typed relationships | Yes | Basic FK | Join paths | Yes (triples) | Yes |
| Action framework | Yes | No | No | No | Build it |
| Permissions | Object/property/action | RBAC | No | Named graph | Build it |
| AI integration | AIP (deep) | Cortex | Via APIs | SPARQL + NL | Build it |
| Data location | Projection | In Snowflake | In warehouse | Virtualized | In Databricks |
| Write-back | Yes | No | No | Limited | Build it |
| Cost | $1M+/year | Snowflake pricing | Open source | $100K+/year | Engineering time |

### Key Architecture Decisions

**Centralized vs. Federated**: Start centralized for core entities (Project, Company, User, Vendor) and cross-domain links. Let domain teams (finance, quality, scheduling) extend for their specific types. "Federated with a shared core."

**Static vs. Dynamic Schema**: Dynamic for properties (customers already have custom fields). Semi-dynamic for object types (we define core types, allow extension). Static for link types (core relationships should be stable).

**Graph DB vs. Warehouse Overlay**: Start with warehouse overlay. Build ontology metadata + API on top of Databricks. Only add graph materialization if specific traversal patterns become bottlenecks.

**Build vs. Buy**: Build incrementally. The strategic thesis is that Procore IS the construction data hub. Buying someone else's ontology platform contradicts that.

### What a Construction Ontology Needs to Model

**Organizational**: Company, Vendor/Subcontractor (with role-per-project polymorphism), User (with project role memberships), Crew/Team

**Project Structure**: Project (type, phase, location, value, dates), Sub-Job, Location (hierarchical), Phase/Stage

**Financial**: Budget, Budget Line Item, Cost Code/WBS Code/Budget Code, Commitment, Change Event, Change Event Line Item, Commitment Change Order, CCO Line Item, CPCO, Direct Cost, Invoice, Budget Modification

**Schedule**: Schedule Task (with predecessors/successors), Schedule Task Change, Milestone, Baseline Schedule

**Quality & Safety**: Observation (category: Quality/Safety/Environmental; hazard_name for safety), Inspection/Inspection Item, Punch Item, Incident, Corrective Action

**Field Operations**: Daily Log (notes, weather, visitors), Daily Log Delay (structured delay_type), Timecard, Equipment Log, Delivery

**Documents & Communication**: RFI (with predicted_topic), Submittal (with overdue flag), Drawing/Spec, Meeting, Correspondence, Photo

**Coordination**: Coordination Issue (issue_type: Clash, Design Review, Constructability)

**Pre-Construction**: Estimate, Bid Package

### Critical Relationships

```
Project --HAS_BUDGET--> Budget --CONTAINS--> BudgetLineItem
Project --HAS_COMMITMENT--> Commitment --HAS_CO--> CommitmentChangeOrder
Project --HAS_VENDOR--> ProjectVendor (with role, trade)
ChangeEvent --BECOMES--> CommitmentChangeOrder (via CPCO bridge)
ChangeEvent --ORIGINATED_FROM--> RFI | Observation | Meeting
Observation --FOUND_ON--> Project, --ASSIGNED_TO--> Vendor
RFI --LINKED_TO--> CoordinationIssue
PunchItem --ON_PROJECT--> Project, --ASSIGNED_TO--> Vendor
DailyLogDelay --LOGGED_ON--> Project, --TYPE--> Material|Weather|Safety
BudgetLineItem --CATEGORIZED_BY--> WBSCode --MAPS_TO--> CostCode + BudgetCode
ScheduleTask --PREDECESSOR_OF--> ScheduleTask
Inspection --CONTAINS--> InspectionItem --REFERENCES--> Location
User --HAS_ROLE_ON--> Project (via ProjectRoleMembership)
```

### Construction-Specific Nuances

1. **Role polymorphism**: A company is a "GC" on Project A and a "Subcontractor" on Project B. Model this as a property of the relationship, not the entity.
2. **Financial lifecycle**: CE -> CPCO -> CCO has deduplication rules (GREATEST(CE, CCO) for cost, never sum). Encode these in the ontology.
3. **Temporal context**: Budget snapshots vs. current budget. Schedule baselines vs. current. Needs temporal versioning.
4. **Structured + unstructured**: Some fields are enums (delay_type, change_reason). Others need NLP (daily log notes, observation names). Distinguish in the ontology.
5. **Cross-company benchmarking**: Multi-tenant data with isolation AND aggregation paths.
6. **Tool availability variance**: Not all customers have financial tools. No budget data doesn't mean no rework — it means no financial tools. Model which modules are active per project.

---

## The Strategic Opportunity

Nobody has built a comprehensive ontology for construction project management. IFC covers the physical building (design/BIM). Nothing covers the operational domain — finances, schedules, quality, safety, field operations, risk.

Every validated insight we've built (rework cost, material shortages, quality issues, design change impact, recurring violations) is a **validated fragment of this ontology** — proven entity relationships, business rules, and data quality. The question is whether we formalize it into a self-describing, AI-consumable layer or leave it as knowledge locked in Databricks queries.

Palantir is selling the concept. We have the data to actually build it.
