# Construction Data Standard

A unified data model for the construction industry covering 18 domains, 817 elements, and 8,361 relationships. This standard defines the entities, attributes, and connections that describe how construction projects are planned, executed, and tracked.

## Domains Overview

| Domain | Description | Connections |
|--------|-------------|-------------|
| Building Elements | What's being built — the physical systems, assemblies, and components that make up a constructed facility | 4 out / 12 in (16 total) |
| Resources | What's used to build — the labor, equipment, and materials consumed during construction | 2 out / 9 in (11 total) |
| Phases | When work happens in the project lifecycle — the major stages from conception through operations | 6 out / 6 in (12 total) |
| Project Attributes | What defines a project — the properties used to classify, compare, and segment projects | 8 out / 0 in (8 total) |
| Organizations | Who's involved — the companies, firms, and entities that participate in a project | 5 out / 7 in (12 total) |
| Roles | What function people play on a project — distinct from the organization they belong to | 2 out / 4 in (6 total) |
| Locations | Where work happens physically — the hierarchical spatial decomposition of a project site | 4 out / 9 in (13 total) |
| Financial Instruments | How money flows through a project — the budgets, contracts, changes, costs, and payments | 12 out / 3 in (15 total) |
| Schedule | How work is sequenced — the tasks, milestones, dependencies, and baselines that define project timing | 5 out / 9 in (14 total) |
| Documents & Communications | What information is created and exchanged — the formal and informal records of a project | 12 out / 4 in (16 total) |
| Quality & Safety Records | How quality and safety are tracked — the observations, inspections, incidents, and deficiencies found during construction | 11 out / 4 in (15 total) |
| Field Operations | What happens on site daily — the real-time records of labor, equipment, materials, weather, and activity | 7 out / 6 in (13 total) |
| Standards & Classifications | External taxonomies and codes that construction data maps to — the shared language of the industry | 6 out / 4 in (10 total) |
| Permits & Regulatory | Jurisdictional requirements — the permits, certificates, and regulatory approvals required to build | 4 out / 7 in (11 total) |
| Contracts & Procurement | Commercial instruments — how work is scoped, bid, awarded, and managed through the project lifecycle | 2 out / 7 in (9 total) |
| Workflows & Statuses | How things move through states — the lifecycle stages and approval chains that records follow | 3 out / 1 in (4 total) |
| Risk | What could go wrong — the identification, assessment, and management of project risks | 4 out / 4 in (8 total) |
| Models & BIM | Digital representations of the physical building — the 3D models, reality captures, and virtual coordination tools | 4 out / 5 in (9 total) |

## Domain Elements

Each domain contains categorized elements representing the fundamental concepts in construction data.

### Building Elements

**Site & Earthwork**
- **Excavation & Shoring** (`be-excav`): Bulk and detailed excavation, sheeting, shoring, and underpinning. Typical trades: equipment operators, general laborers. Often the first major activity on site — schedule and cost overruns here cascade through the project. [MasterFormat 31 10 00 – 31 50 00 | Medium]
- **Backfill & Grading** (`be-backfill`): Structural fill, fine grading, compaction, and subgrade preparation. Equipment-heavy — dozers, loaders, compactors. Quality depends on compaction testing (typically third-party geotechnical). [MasterFormat 31 20 00 – 31 23 00 | Medium]
- **Dewatering** (`be-dewater`): Wellpoints, sump pumps, and groundwater control during construction. Triggered by water table conditions — not present on every project. Can become a major unplanned cost if unexpected. [MasterFormat 31 23 19 | Low]
- **Erosion & Sediment Control**: Silt fence, construction entrances, inlet protection, and SWPPP compliance. Required by EPA/state permits — inspected regularly. Trades: general laborers. [MasterFormat 31 25 00 | Medium]

**Foundations**
- **Deep Foundations** (`be-deep-fdn`): Driven piles, drilled shafts, caissons, micropiles, and helical piers. Requires specialized subcontractors and equipment. Production rates (piles per day) are a key schedule driver. Trades: pile drivers, equipment operators. [MasterFormat 31 62 00 – 31 66 00 | Medium]
- **Shallow Foundations** (`be-shallow-fdn`): Spread footings, strip footings, mat foundations, and pier pads. Concrete and formwork are the primary cost drivers. Trades: concrete workers, carpenters (formwork). Pour records track volume and placement. [MasterFormat 03 30 00 | Medium]
- **Foundation Walls** (`be-fdn-walls`): Cast-in-place or precast foundation walls and retaining walls. Formwork complexity drives cost. Waterproofing is a critical follow-on trade. Trades: concrete workers, carpenters. [MasterFormat 03 30 00 | Medium]
- **Grade Beams** (`be-grade-beams`): Reinforced concrete beams connecting foundation elements at or below grade. Transfer loads between piles/piers. Trades: concrete workers, carpenters. [MasterFormat 03 30 00 | Low]
- **Slab on Grade** (`ph-slab`): Ground-supported concrete floor slabs with vapor barriers and joint sealants. Includes reinforcement (rebar, WWF, fiber). Quality depends on subgrade prep and finishing. Trades: concrete workers. [MasterFormat 03 30 00 | Medium]
- **Below-Grade Waterproofing** (`be-bg-wp`): Foundation waterproofing membranes, dampproofing, underslab vapor barriers, and drainage boards. Failure leads to long-term moisture intrusion. Trades: specialty waterproofing applicators. [MasterFormat 07 10 00 – 07 16 00 | Medium]

**Site Utilities**
- **Water Main / Service**: Underground domestic and fire water supply piping from street to building. Requires coordination with municipality. Trades: plumbers/pipefitters, equipment operators. [MasterFormat 33 10 00 | Low]
- **Sanitary Sewer** (`be-sanitary`): Underground sanitary waste piping from building to main, with manholes and cleanouts. Gravity-driven — slope is critical. Trades: plumbers/pipefitters, equipment operators. [MasterFormat 33 30 00 | Low]
- **Storm Drainage** (`be-storm`): Underground storm water piping, catch basins, and retention/detention systems. Sized by hydrological analysis. Subject to local stormwater regulations. Trades: plumbers/pipefitters, equipment operators. [MasterFormat 33 40 00 | Low]
- **Gas Service** (`be-gas-svc`): Underground gas piping from meter to building. Small scope on most projects but requires specialty inspection. Trades: plumbers/pipefitters. [MasterFormat 33 50 00 | Low]
- **Site Electrical & Telecom Ductbank**: Underground electrical and telecom conduit banks, manholes, and handholes. Coordinates with power company. Trades: electricians, equipment operators. [MasterFormat 33 70 00 – 33 80 00 | Low]

**Structural Frame**
- **Columns** (`be-columns`): Steel or concrete vertical load-bearing members. Steel columns: W-shapes, HSS, pipe. Concrete columns: CIP with rebar cages, formwork. Trades: ironworkers (steel), concrete workers (concrete). Critical path activity. [MasterFormat 03 30 00 / 05 12 00 | Medium]
- **Beams & Girders** (`be-beams`): Steel or concrete horizontal spanning members. Steel: W-shapes, built-up sections. Concrete: CIP or precast. Camber and deflection are key design parameters. Trades: ironworkers, concrete workers. [MasterFormat 03 30 00 / 05 12 00 | Medium]
- **Floor Slabs & Metal Deck**: Composite metal deck with concrete topping, post-tensioned slabs, or precast plank. Deck erection and concrete pours are major scheduling milestones. Trades: ironworkers (deck), concrete workers (topping). [MasterFormat 03 30 00 / 05 31 00 | Medium]
- **Roof Structure** (`be-roof-struct`): Steel or concrete roof framing — long-span joists, trusses, and moment frames. Trades: ironworkers. Often governs crane duration and pick sequence. [MasterFormat 05 12 00 / 05 21 00 | Low]
- **Structural Connections & Embeds**: Bolted and welded connections, embed plates, anchor bolts, and base plates. Connection design generates heavy RFI activity — a leading indicator of structural complexity. Trades: ironworkers. [MasterFormat 05 12 00 | Medium]
- **Stairs & Ramps** (`be-stairs`): Cast-in-place or steel stairs and structural ramps, with handrails. Both temporary and permanent stairs. Punch items frequently reference stairs and railings. Trades: ironworkers, concrete workers. [MasterFormat 03 30 00 / 05 51 00 | Medium]
- **Miscellaneous Metals**: Lintels, loose angles, shelf angles, channels, bollards, and structural railings. Small scope individually but high coordination — nearly every other trade needs miscellaneous metals embedded. Trades: ironworkers. [MasterFormat 05 50 00 | Medium]

**Exterior Enclosure**
- **Curtain Wall** (`be-curtainwall`): Aluminum-framed glass curtain wall systems — unitized or stick-built. High RFI and coordination issue activity (MEP penetrations, structural anchors). Major submittal packages. Trades: glaziers, curtain wall installers. [MasterFormat 08 44 00 | High]
- **Windows** (`be-windows`): Punched window units in opaque wall systems. Product submittals drive procurement timeline. Trades: glaziers. [MasterFormat 08 50 00 | Medium]
- **Exterior Doors & Entrances**: Entrance doors, storefronts, revolving doors, overhead doors, and service doors. Door hardware drives complexity. Trades: glaziers (storefronts), carpenters (hollow metal). Doors are one of the highest punch item categories. [MasterFormat 08 10 00 – 08 42 00 | High]
- **Masonry Veneer / Backup Wall**: Brick veneer, stone veneer, and CMU backup walls with through-wall flashing and weep systems. Quality depends on mortar joints, flashing, and drainage. Trades: masons. [MasterFormat 04 20 00 – 04 40 00 | Medium]
- **Precast / Metal Panels** (`be-panels`): Architectural precast concrete, insulated metal panels (IMP), ACM panels, and terra cotta. Panel layout coordination with structure and MEP is critical. Trades: ironworkers (erection), specialty installers. [MasterFormat 03 45 00 / 07 42 00 | Medium]
- **Air & Moisture Barrier** (`ph-barrier`): Fluid-applied or sheet membrane air/vapor barriers on exterior sheathing. Performance-critical — failures here cause long-term moisture damage. Third-party inspection is common. Trades: specialty applicators. [MasterFormat 07 25 00 – 07 27 00 | Medium]
- **Exterior Insulation** (`be-ext-insul`): Continuous insulation (CI) on exterior walls — mineral wool, rigid foam, or spray foam. Energy code compliance driver. Trades: specialty installers, general laborers. [MasterFormat 07 21 00 | Low]

**Roofing**
- **Roof Membrane** (`be-roof-mem`): Single-ply (TPO, PVC, EPDM), built-up, or modified bitumen roofing membranes. Warranty is a key deliverable — manufacturer requirements drive installation quality. Trades: roofers. [MasterFormat 07 50 00 | High]
- **Roof Insulation & Cover Board**: Rigid insulation and tapered systems for drainage, with cover boards. Tapered layout is a design coordination item. Trades: roofers. [MasterFormat 07 22 00 | Low]
- **Flashing & Sheet Metal**: Roof edge metal, copings, counterflashing, reglets, gutters, and downspouts. Flashing failures are a top source of roof leaks. Trades: roofers, sheet metal workers. [MasterFormat 07 60 00 | Medium]
- **Roof Drainage** (`be-roof-drain`): Interior roof drains, scuppers, overflow drains, and conductor piping. Cross-trade coordination — roofer installs drain bodies, plumber runs pipe. Design drives structural loads (ponding). [MasterFormat 07 63 00 / 22 14 00 | Low]
- **Skylights & Roof Hatches**: Unit skylights, smoke vents, and roof access hatches. Small scope but high defect rate per unit — curb flashing is a common failure point. Trades: glaziers, specialty installers. [MasterFormat 08 62 00 / 07 72 00 | Low]

**HVAC**
- **Ductwork** (`be-ductwork`): Supply, return, and exhaust ductwork — sheet metal, flex, and fittings. Routing coordination with other MEP systems drives schedule. Trades: HVAC/sheet metal workers. [MasterFormat 23 31 00 | High]
- **HVAC Piping** (`be-hvac-pipe`): Chilled water, hot water, condenser water, and refrigerant piping with insulation. Pipe sizing and routing are key RFI topics. Trades: pipefitters. [MasterFormat 23 21 00 | Medium]
- **Air Handling Equipment**: AHUs, RTUs, fan coil units, VAV boxes, and exhaust fans. Major submittals — equipment delivery is a key scheduling milestone. Trades: HVAC mechanics. [MasterFormat 23 73 00 – 23 74 00 | High]
- **Heating Equipment** (`be-heating`): Boilers, unit heaters, radiant heating, and heat exchangers. Seasonal dependency — heating system must be operational for winter work. Trades: HVAC mechanics. [MasterFormat 23 52 00 | Medium]
- **Cooling Equipment** (`be-cooling`): Chillers, cooling towers, condensing units, and split systems. Heaviest and most expensive MEP equipment — rigging and crane logistics are critical. Trades: HVAC mechanics. [MasterFormat 23 64 00 | Medium]
- **Duct Insulation** (`be-duct-insul`): Thermal and acoustic insulation on ductwork. Required by energy code on exposed supply and return duct. Trades: insulators. [MasterFormat 23 07 00 | Low]
- **HVAC Controls & Thermostats**: DDC controls, thermostats, sensors, damper actuators, and building automation system (BAS) programming. Controls/commissioning generates heavy RFI and punch item activity. Trades: controls technicians, HVAC mechanics. [MasterFormat 23 09 00 / 25 00 00 | Medium]
- **Testing Adjusting & Balancing** (`ph-tab`): Air and water system balancing and commissioning verification. Late-project activity — results validate design assumptions. Trades: TAB contractors, commissioning agents. [MasterFormat 23 05 93 | Low]

**Plumbing**
- **Domestic Water Supply**: Hot and cold water distribution piping, valves, hangers, and insulation. Leak testing is a key milestone. Trades: plumbers/pipefitters. [MasterFormat 22 11 00 | Medium]
- **Sanitary Waste & Vent**: DWV piping, cleanouts, floor drains, and traps. Gravity-driven — slope is critical and generates RFIs for routing in tight ceilings. Trades: plumbers/pipefitters. [MasterFormat 22 13 00 | Medium]
- **Interior Storm Drainage**: Interior roof drain leaders, area drains, and conductor piping. Connects roof drainage to underground storm system. Trades: plumbers/pipefitters. [MasterFormat 22 14 00 | Low]
- **Gas Piping (Interior)**: Interior natural gas distribution to equipment — boilers, water heaters, kitchen equipment. Requires pressure testing and inspection. Trades: plumbers/pipefitters. [MasterFormat 22 11 00 | Low]
- **Plumbing Fixtures** (`ph-plumb-fix`): Toilets, urinals, sinks, faucets, drinking fountains, and floor drains. High submittal activity (product approvals) and very high punch item rates — plumbing fixtures are a top punch category. Trades: plumbers. [MasterFormat 22 40 00 | High]
- **Water Heaters** (`be-water-htr`): Domestic water heating — tanks, tankless, and heat pump water heaters. Small scope but affects hot water distribution design. Trades: plumbers. [MasterFormat 22 33 00 | Low]
- **Pipe Insulation** (`be-pipe-insul`): Thermal insulation on plumbing piping. Required by energy code on hot water and chilled supply lines. Trades: insulators. [MasterFormat 22 07 00 | Low]

**Electrical**
- **Power Distribution** (`be-power-dist`): Main switchgear, distribution panels, transformers, bus duct, and feeders. Major submittals with long lead times — procurement timing is critical. Trades: electricians. [MasterFormat 26 24 00 – 26 28 00 | High]
- **Branch Wiring & Devices**: Outlets, switches, junction boxes, home runs, and branch circuits. Highest-volume electrical work. Punch items for cover plates and device alignment are top closeout issues. Trades: electricians. [MasterFormat 26 27 00 | High]
- **Conduit & Raceways** (`be-conduit`): EMT, rigid, PVC conduit, cable tray, and wireways. Routing coordination with other MEP systems is a major schedule driver. Trades: electricians. [MasterFormat 26 05 33 | Medium]
- **Lighting Fixtures & Controls**: Interior and exterior lighting fixtures, controls, occupancy sensors, and daylight harvesting systems. High submittal and punch item activity. Trades: electricians. [MasterFormat 26 50 00 – 26 56 00 | High]
- **Emergency / Standby Power**: Emergency generators, automatic transfer switches (ATS), UPS systems, and emergency circuits. Code-required for life safety. Trades: electricians. [MasterFormat 26 32 00 – 26 36 00 | Medium]
- **Grounding & Lightning Protection**: Building grounding system, lightning rods, and bonding. Code-required; tested during construction. Small scope. Trades: electricians. [MasterFormat 26 05 26 / 26 41 00 | Low]

**Fire Protection**
- **Sprinkler Mains & Branches**: Fire sprinkler distribution piping — mains, cross-mains, and branch lines with seismic bracing. Head layout coordination with ceilings and MEP is a top coordination issue. Trades: sprinkler fitters. [MasterFormat 21 13 00 | High]
- **Sprinkler Heads** (`be-sprink-head`): Pendant, upright, sidewall, and concealed sprinkler heads. Very high punch item rate — concealed head cover plates are a top closeout item. Trades: sprinkler fitters. [MasterFormat 21 13 00 | High]
- **Standpipes & Hose Connections**: Standpipe risers, hose valves, and fire department connections (FDC). Required for buildings above certain heights. Flow testing is a code requirement. Trades: sprinkler fitters. [MasterFormat 21 12 00 | Low]
- **Fire Pump** (`be-fire-pump`): Fire pump, jockey pump, controller, and test header. Required when municipal water pressure is insufficient. Acceptance testing is code-required. Trades: sprinkler fitters, electricians. [MasterFormat 21 11 00 | Low]
- **Fire Alarm & Detection**: Fire alarm control panel (FACP), pull stations, smoke/heat detectors, notification appliances, and duct detectors. Code-required system with acceptance testing. Trades: electricians, low-voltage technicians. [MasterFormat 28 31 00 | High]

**Low Voltage & Technology**
- **Data / Telecom Cabling**: Cat6/fiber optic cabling, patch panels, racks, and telecom rooms. Pathway coordination with electrical. Trades: low-voltage technicians. [MasterFormat 27 10 00 – 27 15 00 | Medium]
- **Security Systems** (`be-security`): CCTV cameras, access control (card readers, controllers), and intrusion detection. Integrates with door hardware — coordination signal. Trades: low-voltage technicians. [MasterFormat 28 20 00 – 28 23 00 | Medium]
- **Audio / Visual Systems**: AV systems — displays, speakers, distributed audio, and conference room systems. Often owner-furnished / contractor-installed (OFCI). Trades: low-voltage technicians. [MasterFormat 27 40 00 | Low]
- **Building Automation Devices & Wiring**: BAS field devices, sensors, actuators, and control wiring (not programming — see HVAC Controls). Different installer than the controls programmer. Trades: low-voltage technicians. [MasterFormat 25 10 00 | Low]
- **Specialty Systems** (`pa-specialty-system`): Nurse call, intercom, paging, distributed antenna (DAS), and clock systems. Project-type dependent — nurse call for healthcare, DAS for large buildings. Trades: low-voltage technicians. [MasterFormat 27 50 00 – 27 53 00 | Low]

**Interiors**
- **Metal Stud Framing** (`ph-framing`): Interior metal stud partitions, soffits, and bulkhead framing with blocking. Layout accuracy drives downstream finish quality. Trades: drywall hangers. [MasterFormat 09 22 16 | Medium]
- **Drywall / Gypsum Board**: Gypsum board installation, taping, and finishing — including specialty boards (moisture-resistant, fire-rated, abuse-resistant). Drywall damage and finish quality are top punch categories. Trades: drywall hangers, finishers. [MasterFormat 09 29 00 | High]
- **Interior Doors Frames & Hardware**: Interior hollow metal and wood doors, frames, and finish hardware (hinges, closers, locks, pulls). Hardware sets are complex submittals. Doors/hardware is consistently a top 3 punch item category. Trades: carpenters. [MasterFormat 08 11 00 – 08 71 00 | High]
- **Acoustic Ceilings** (`be-act`): Suspended acoustic ceiling grid and tile systems. Layout coordination with lighting, sprinklers, and diffusers. Trades: ceiling installers. [MasterFormat 09 51 00 | High]
- **Drywall Ceilings Soffits & Bulkheads**: Drywall ceilings, soffits, bulkheads, and light coves — non-acoustic applications. More complex framing than walls. Trades: drywall hangers, finishers. [MasterFormat 09 29 00 | Medium]
- **Paint & Wall Coatings** (`ph-paint`): Interior painting, primer, specialty coatings, stain, and clear finishes. Paint/finish is the #1 punch item category universally — touch-ups and color inconsistency dominate closeout. Trades: painters. [MasterFormat 09 91 00 | High]
- **Wallcovering** (`be-wallcover`): Vinyl wallcovering, specialty wall finishes, and wall protection (corner guards, crash rails). Common in healthcare and hospitality. Trades: painters, specialty installers. [MasterFormat 09 72 00 / 10 26 00 | Low]
- **Floor Tile & Stone**: Ceramic, porcelain, and natural stone tile for floors and walls — including setting materials and grout. Cracked tiles, grout, and lippage are common punch items. Trades: tile setters. [MasterFormat 09 30 00 | High]
- **Carpet & Resilient Flooring**: Carpet (broadloom, tile), VCT, LVT, rubber, and sheet vinyl with resilient base. Seams, transitions, and base are frequent closeout items. Trades: floor installers. [MasterFormat 09 68 00 | High]
- **Specialty Flooring** (`be-spec-floor`): Polished concrete, epoxy, terrazzo, and resinous flooring. Project-type dependent — common in industrial, healthcare, and education. Trades: specialty installers. [MasterFormat 03 35 00 / 09 67 00 | Medium]
- **Casework & Millwork** (`ph-casework`): Cabinets, countertops, shelving, built-in furniture, and wood trim (base/crown molding). High punch item rate — scratches, chips, alignment, and door adjustment. Trades: carpenters. [MasterFormat 06 20 00 – 12 30 00 | High]
- **Countertops** (`be-countertop`): Solid surface, stone, quartz, and plastic laminate countertops. Templated after casework installation — template-to-install cycle is a schedule constraint. Trades: specialty installers. [MasterFormat 12 36 00 | Medium]
- **Toilet Accessories & Specialties**: Toilet partitions, accessories (paper holders, grab bars, soap dispensers), mirrors, and signage. High punch item rate — installation alignment, missing items, and damage. Trades: carpenters, general laborers. [MasterFormat 10 21 00 – 10 28 00 | High]
- **Signage & Wayfinding**: Room signs, directional signs, code-required signs, and ADA signage. Late-project scope — often last items installed before occupancy. Trades: specialty installers. [MasterFormat 10 14 00 | Low]

**Elevators**
- **Elevator Car & Hoistway**: Passenger, service, and freight elevator cars — hoistway doors, cab finishes, and controls. Elevator installation is a major scheduling milestone. Long lead time item. Trades: elevator mechanics. [MasterFormat 14 20 00 | High]
- **Elevator Machinery & Controls**: Traction machines, hydraulic units, motor controllers, and dispatching systems. Acceptance testing/inspection by authority having jurisdiction (AHJ) is required. Trades: elevator mechanics. [MasterFormat 14 20 00 | Medium]

**Site Improvements**
- **Paving** (`be-paving`): Asphalt and concrete paving for parking lots, access roads, and loading areas. Temperature-sensitive installation (asphalt). Trades: equipment operators, general laborers. [MasterFormat 32 12 00 – 32 13 00 | Medium]
- **Sidewalks & Curbs**: Concrete sidewalks, curbs, gutters, ADA ramps, and pavers. ADA compliance is a common observation and punch item trigger. Trades: concrete workers. [MasterFormat 32 16 00 | Medium]
- **Landscaping & Irrigation**: Trees, shrubs, ground cover, turf, and irrigation systems. Usually one of the last exterior scopes. Plant survival warranty (typically 1 year) extends beyond project completion. Trades: landscape contractors. [MasterFormat 32 90 00 | Medium]
- **Site Lighting** (`be-site-light`): Parking lot and pathway lighting — poles, bollard lights, and site electrical. Coordinates with site electrical underground. Trades: electricians. [MasterFormat 26 56 00 / 32 00 00 | Low]
- **Fencing & Gates**: Chain link, ornamental, and security fencing with gates and barriers. Small scope on most projects. Trades: fence contractors. [MasterFormat 32 31 00 | Low]

**Standard Measures**
- **Cost per SF by System**: Total cost of each building system divided by gross building area (SF). The primary unit cost benchmark for comparing systems across projects. Calculation: system cost / gross SF. Source: budget line items, cost codes, building area. [AACE | Medium]
- **Punch Item Rate by Element Category**: Count of punch items per unit area (per 1000 SF) or per unit count (per door, per fixture) for each element category. Tracks closeout quality. Calculation: punch count / area or unit count. Source: punch items, building area. [N/A | High]
- **RFI Density by System**: Count of RFIs per system per million dollars of contract value. Tracks design coordination complexity. Calculation: RFI count / (contract value / $1M). Source: RFIs, contract value. [N/A | Medium]
- **Observation Rate by Element**: Count of quality/safety observations per unit area or per system. Tracks field issue frequency. Calculation: observation count / area. Source: observations, building area. [N/A | Medium]
- **Submittal Cycle Time by System**: Average days from submittal creation to final approval for each system. Tracks procurement timeline performance. Calculation: avg(approval_date - created_date) by system. Source: submittals. [N/A | Medium]
- **Coordination Issue Density** (`bim-coord-issue-2`): Count of coordination issues per system or trade per million dollars. Tracks MEP/architectural coordination complexity. Calculation: issue count / (contract value / $1M). Source: coordination issues, contract value. [N/A | Medium]

### Contracts & Procurement

**Procurement Lifecycle**
- **Prequalification** (`cp-prequalification`): Vetting of a contractor or vendor's financial health, safety record, bonding capacity, and relevant experience BEFORE they are invited to bid. The gatekeeping step that determines who is eligible to compete for work. [AGC Prequalification Standards | None]
- **Bid Package** (`cp-bid-package`): A defined scope of work issued to qualified contractors for competitive pricing. Bundles drawings, specifications, schedule, and commercial terms into a single solicitation. The unit of procurement — one package per trade or work scope. [AIA A701 (Instructions to Bidders) | None]
- **Request for Qualification** (`cp-req-qualificatio`): Formal solicitation to assess contractor capabilities before inviting bids. Used on complex or specialized scopes where not all contractors can perform the work. Shortlists the field before pricing begins. [AIA | None]
- **Request for Proposal** (`cp-req-proposal`): Detailed solicitation requesting scope, approach, schedule, and price from qualified contractors. More comprehensive than a simple bid — evaluates methodology, not just price. Common on negotiated or best-value procurements. [AIA | None]
- **Proposal / Bid** (`cp-proposal-bid`): A contractor's formal response to an ITB, RFQ, or RFP — includes pricing, scope clarifications, exclusions, alternates, and schedule. The document that becomes the basis for contract negotiation upon award. [AIA | None]
- **Bid Evaluation / Leveling** (`cp-bid-evaluation`): Comparative analysis of competing proposals — normalizing scope, pricing, qualifications, and exclusions to make an apples-to-apples recommendation. Identifies the apparent low bidder or best-value selection. [AIA | None]
- **Award / Notice to Proceed** (`cp-award-notice`): Formal notification to the selected contractor that they have won the work and are authorized to begin. Triggers mobilization, procurement, and insurance/bonding requirements. May precede the executed contract via a Letter of Intent. [AIA A101/A201 | Low]

**Contract Instruments**
- **Subcontract** (`cp-subcontract`): Executed agreement between a general contractor and a subcontractor for a defined scope of work at an agreed price. The primary commercial vehicle for trade work. Includes scope, price, schedule, insurance, and flow-down terms. [AIA A401 (Standard Subcontract) | High]
- **Purchase Order** (`cp-purchase-order`): Agreement for material supply, equipment rental, or services at a specified price. Simpler than a subcontract — typically no labor/scope-of-work component. Tracks what was ordered, from whom, at what cost. [UCC (Uniform Commercial Code) | High]
- **Prime Contract** (`cp-prime-contract`): Agreement between the project owner and the general contractor or CM. The top-level commercial agreement that defines the overall project price, scope, schedule, and terms. All subcontracts flow down from this. [AIA A101/A102/A103 | Low]
- **Master Service Agreement** (`cp-master-service`): Standing agreement with a vendor or subcontractor that covers multiple projects or a defined time period. Sets standard terms so individual project work orders can be issued without full contract negotiation each time. [AGC | None]

**Contract Terms & Exhibits**
- **Scope of Work** (`cp-scope-work`): Detailed description of contracted work — defines what the subcontractor or vendor is responsible for delivering. May reference drawings, specifications, and schedule. The single most important exhibit to any construction contract. [AIA A201 | Low]
- **General Conditions** (`cp-gen-cond`): The standard legal and administrative terms that apply to all contracts on a project — defines roles, responsibilities, dispute resolution, insurance requirements, and procedural obligations. The 'rules of the game' for the project. [AIA A201 (General Conditions) | None]
- **Retainage Terms** (`cp-retainage-terms`): Contractual provision specifying the percentage of each payment withheld until substantial completion or final acceptance. Protects the owner/GC against incomplete or defective work. Typically 5-10% of contract value. [AIA A201 (9.3.1) | Medium]
- **Liquidated Damages** (`cp-liquidated-damag`): Pre-agreed daily or milestone-based financial penalty for late completion. Establishes the cost of delay without requiring the owner to prove actual damages. A critical risk term that drives schedule urgency. [AIA A201 (4.3) | None]
- **Allowance** (`fi-allowance`): A budgeted amount included in the contract for work that cannot be fully defined at contract execution. Spent against actual costs as scope is clarified. Commonly used for concealed conditions, owner selections, or design development items. [AIA A201 (3.8) | Medium]

**Surety & Insurance**
- **Bid Bond** (`cp-bid-bond`): A surety bond submitted with a bid guaranteeing the bidder will enter into the contract at the bid price if awarded. Typically 5-10% of bid amount. Protects the owner against bidders who withdraw after bid opening. [Miller Act (federal) | None]
- **Performance Bond** (`cp-perf-bond`): Surety guarantee that the contractor will complete the work per contract terms. If the contractor defaults, the surety must complete the work or compensate the owner. Typically 100% of contract value. [Miller Act | None]
- **Payment Bond** (`cp-payment-bond`): Surety guarantee that the contractor will pay subcontractors, suppliers, and laborers. Protects the project from mechanic's liens filed by unpaid parties. Typically 100% of contract value. [Miller Act | None]
- **Insurance Certificate** (`cp-insurance-cert`): Proof of insurance coverage — documents that the contractor carries required general liability, workers' comp, auto, umbrella, and builders risk coverage. Verified before work begins and tracked throughout the project. [ACORD forms (25, 28) | High]
- **Builders Risk** (`cp-builders-risk`): Insurance policy covering physical loss or damage to the building under construction. Typically carried by the owner or GC and covers all parties. Separate from the contractor's general liability. [AIA A201 (11.3) | None]

**Warranty & Closeout**
- **Warranty** (`cp-warranty`): Post-construction guarantee that work will be free from defects for a specified period. Standard is 1 year from substantial completion; extended warranties apply to specific systems (roofing: 20 years, HVAC: 5 years, waterproofing: 10 years). [AIA A201 (3.5, 12.2) | Low]
- **Substantial Completion** (`cp-substantial-comp`): The milestone when the project is sufficiently complete for the owner to occupy and use for its intended purpose. Triggers warranty start dates, retainage release, and final completion punchlist. A contractual — not just physical — milestone. [AIA A201 (9.8) | Medium]
- **Final Completion** (`cp-final-completion`): The point at which ALL contract work is complete — all punch items resolved, all closeout documents delivered, all training completed. Triggers final retainage release and contract closeout. The true end of the project. [AIA A201 (9.10) | Medium]

**Compliance Documents**
- **Prevailing Wage Certification** (`cp-prevailing-wage`): Documentation proving that workers on public projects are paid at or above the locally determined prevailing wage rate. Required on federal (Davis-Bacon) and most state public work. Submitted with each pay period. [Davis-Bacon Act | Medium]
- **Diversity / DBE Certification** (`cp-diversity-dbe`): Documentation of participation by disadvantaged, minority, women-owned, veteran-owned, or small businesses. Required on most public projects and increasingly on private work. Tracked as percentage of contract value. [FAR (federal) | Low]
- **Closeout Document Package** (`cp-closeout-doc`): The collection of documents required for project handover — as-builts, O&M manuals, warranties, training records, commissioning reports, and final lien waivers. The deliverable set that closes out the contract. [AIA A201 (9.10) | Medium]

**Standard Measures**
- **Bid Coverage Rate** (`cp-bid-coverage`): Percentage of project scope (by value) that was competitively bid vs. sole-sourced or negotiated. Formula: SUM(competitively_bid_contract_value) / total_contract_value. Higher rate = more price discovery. [AGC | None]
- **Average Bidders per Package** (`cp-average-bidders`): Mean number of competing proposals received per bid package. Formula: AVG(bidders_per_package). More bidders = more price competition and market depth. [AGC | None]
- **Award Cycle Time** (`cp-award-cycle-time`): Mean elapsed time from bid opening to contract execution. Formula: AVG(contract_date - bid_due_date). Shorter cycles get subs mobilized faster and reduce price escalation risk. [AGC | None]
- **Insurance Compliance Rate** (`cp-insurance-comp`): Percentage of active subcontractors with current, compliant insurance certificates. Formula: COUNT(compliant_vendors) / COUNT(active_vendors). Below 100% = uninsured work exposure. [AIA A201 | High]
- **Change Order Rate** (`fi-chg-order-rate`): Ratio of total change order value to original contract value. Formula: SUM(CO_value) / original_contract_value. Higher rate = more scope change, design issues, or unforeseen conditions. [AACE | High]
- **Subcontractor Retention Rate** (`cp-sub-retention`): Percentage of subcontractors used on previous projects that are re-engaged on new projects. Formula: COUNT(repeat_subs) / COUNT(total_subs). Higher rate = stronger trade partner relationships. [AGC (partnering standards) | Medium]

### Documents & Communications

**Design & Construction Documents**
- **Drawing Set** (`doc-drawing-set`): Complete package of design documents issued for a project phase — architectural, structural, MEP, civil, landscape sheets organized by discipline and numbered by convention. Issued at milestones (SD, DD, CD, IFC, As-Built). [AIA E202 (BIM Protocol), AIA G702, NCS (National CAD Standard), US National BIM  | High]
- **Drawing Sheet** (`doc-drawing-sheet`): Individual sheet within a drawing set — identified by discipline prefix and sheet number (e.g., S-301, M-201, A-102). Contains plan views, sections, details, schedules, and notes for a specific scope. [NCS (sheet numbering convention), AIA CAD Layer Guidelines | High]
- **Drawing Revision** (`doc-drawing-revision`): A new version of a drawing sheet issued to correct errors, incorporate changes, or add information. Tracked by revision number (Rev A, Rev B, or numeric) with a revision date and description of changes. Each revision supersedes the prior version. [AIA standard revision tracking, NCS revision block format | High]
- **Specification Section** (`sc-specification-se`): Written document defining material, product, and installation requirements for a specific scope of work — organized by CSI MasterFormat division and section number. Contains Part 1 (General), Part 2 (Products), Part 3 (Execution). [CSI MasterFormat (50 divisions), CSI SectionFormat (3-part structure), ASTM refe | Medium]
- **Addendum** (`doc-addendum`): Formal modification to bidding or contract documents issued before contract execution — changes drawings, specs, or bid conditions. Numbered sequentially (Addendum 1, 2, 3). [AIA A701 (Instructions to Bidders), AIA A201 (General Conditions §1.1) | Low]
- **Bulletin / Architect's Supplemental Instruction (ASI)** (`doc-bulletin-archite`): Post-contract design clarification or minor change issued by the architect that does not change the contract sum or time. ASIs modify drawings or specs to clarify intent, correct minor errors, or adjust details. [AIA G710 (Architect's Supplemental Instructions) | Low]

**Requests & Clarifications**
- **Request for Information (RFI)** (`doc-req-info-rfi`): Formal question from the contractor to the design team requesting clarification on drawings, specs, or design intent. RFIs have a structured lifecycle: initiated → assigned → responded → closed/accepted. [AIA G716 (Request for Information), ConsensusDocs 200 | High]
- **RFI Response** (`doc-rfi-response`): Formal answer to an RFI from the design team — provides the clarification, direction, or decision requested. May include supplementary sketches, revised details, or references to existing drawings. Response status (official vs. [AIA G716 | High]
- **Request for Proposal (RFP) / Pricing Request** (`doc-req-proposal-rfp`): Formal request from GC to subcontractor or supplier for pricing on a change, additional work, or alternate scope. Not the same as a bid-phase RFP — this is a construction-phase pricing exercise. [No universal standard | Medium]

**Submittals & Approvals**
- **Submittal** (`doc-submittal`): Formal submission of product data, shop drawings, samples, or other documentation to the design team for review and approval before procurement or installation. Every specified material requires a submittal. [CSI standards, AIA A201 §3.12 (Shop Drawings, Product Data, Samples), spec secti | High]
- **Submittal Response / Review** (`doc-submittal-respon`): The design team's review action on a submittal — approve, approve as noted, reject, or revise and resubmit. Reviewer markups on shop drawings are binding design modifications. [AIA A201 §4.2.7 (Review of Submittals) | High]
- **Shop Drawing** (`doc-shop-drawing`): A subcontractor-prepared or fabricator-prepared detailed drawing showing dimensions, connections, materials, and fabrication details for their specific scope — submitted for design team review. [AIA A201 §3.12, AISC Code of Standard Practice (steel), PCI (precast) | High]
- **Product Data Submittal** (`doc-product-data`): Manufacturer's published literature, cut sheets, performance data, and test reports submitted to demonstrate that a specific product meets specification requirements. [CSI submittals classification, ASTM/UL/FM test standards referenced in specs | High]
- **Sample Submittal** (`doc-sample-submittal`): Physical material sample submitted for design team review and approval — colors, textures, finishes, and material quality. Includes mockup panels, paint samples, flooring tiles, stone selections, hardware finishes. [AIA A201 §3.12 (Samples) | Medium]

**Correspondence & Notices**
- **Correspondence** (`doc-correspondence`): Formal written communication between project parties — letters, emails tracked as project records, and notices that require acknowledgment or response. Correspondence types are configurable per project (letters, notices, memos, transmittals). [AIA A201 (various notice provisions), contract-specific notice requirements | High]
- **Transmittal** (`doc-transmittal`): Cover document accompanying a package of drawings, specifications, submittals, or other documents sent between parties. Records what was sent, to whom, when, and for what purpose (for review, for approval, for information, for construction). [AIA G810 (Transmittal Letter) | Medium]
- **Notice of Delay** (`doc-notice-delay`): Formal written notification that a delay event has occurred or is anticipated — required by most contracts within a specified timeframe (often 7-14 days) to preserve delay claim rights. [AIA A201 §15.1.6 (Claims for Additional Time), ConsensusDocs 200 §6.3 | Low]
- **Change Directive / Construction Change Directive (CCD)** (`doc-chg-directive`): Owner-issued directive requiring the contractor to proceed with changed work before the cost and time impact is agreed upon. Used when urgency prevents waiting for a negotiated change order. [AIA A201 §7.3 (Construction Change Directives), AIA G714 | Low]

**Meeting Records**
- **Meeting** (`doc-meeting`): Formally scheduled project meeting with defined attendees, agenda, and documented outcomes. Meetings are the primary decision-making forum on construction projects. [No universal standard | High]
- **Meeting Minutes / Meeting Item** (`doc-meeting-minutes`): Individual agenda item or action item within a meeting — captures topic, discussion, responsible party, due date, and status. Meeting items carry forward between meetings (rolling action item log). [AIA G712 (Project Meeting Minutes form) | High]

**Field Communications**
- **Daily Report / Daily Log** (`doc-daily-report`): Comprehensive daily site record compiled by the superintendent or project engineer — combines weather, manpower, equipment, deliveries, visitors, delays, notes, safety violations, and work performed into a single daily project narrative. [No universal standard | High]
- **Daily Log Note** (`fo-daily-log-note`): Free-text field observation entered as part of the daily log — captures site conditions, work progress, issues, coordination problems, or any noteworthy event that doesn't fit structured log categories. Notes may be flagged as issue days. [No standard | High]
- **Site Instruction** (`doc-site-instruction`): Written directive from the GC superintendent or project manager to a subcontractor or crew — directs specific field action. Site instructions address means and methods, sequence changes, safety corrections, or quality requirements. [No universal standard | Medium]
- **Phone Call Log** (`doc-phone-call-log`): Record of field phone calls tracked as part of the daily log — documents who called whom, subject, and outcome. Captures communications that don't have a formal paper trail. [No standard | Medium]
- **Plan Revision Notice** (`doc-plan-revision`): Field-level record that a new drawing revision has been received and acknowledged on the jobsite. Ensures the construction team is working from current documents. [No standard | Medium]

**Action Plans & Tasks**
- **Action Plan** (`qsr-action-plan`): Structured set of tasks with assignments, due dates, and completion tracking — used for punch list management, commissioning tasks, closeout activities, safety action items, or any coordinated work sequence. [No universal standard | High]
- **Action Plan Line Item (Task)** (`qsr-action-plan-line`): Individual task within an action plan — a specific work item assigned to a responsible party with a due date and status. [No standard | High]
- **Project Task** (`doc-project-task`): General-purpose task tracked at the project level — not tied to an action plan. Used for ad-hoc work items, reminders, and assignments that don't fit the formal action plan structure. Lighter weight than action plan tasks but less structured. [No standard | Medium]

**Visual Documentation**
- **Photo** (`doc-photo`): Photograph documenting site conditions, work progress, quality issues, safety hazards, or installed work. Photos are attached to locations, observations, inspections, daily logs, and punch items. [No standard | High]
- **Video** (`doc-video`): Video recording of site conditions, work-in-progress, or safety events. Increasingly used for progress documentation (time-lapse), drone flyovers, quality recording (concrete pours, waterproofing installation), and safety incident documentation. [No standard | Low]

**Regulatory & Compliance Documents**
- **Permit Application / Building Permit Record** (`doc-permit-applicati`): Documentation submitted to and received from regulatory authorities — building permit applications, permit issuance records, permit conditions, and inspection cards. Tracks permit status from application through issuance. [IBC (International Building Code), local building codes, local permit applicatio | Low]
- **Certificate of Insurance (COI)** (`doc-cert-insurance`): Proof of insurance coverage provided by a subcontractor, vendor, or other project party — verifies they meet the contractual insurance requirements (general liability, workers' comp, auto, umbrella, builders risk). [ACORD 25 (Certificate of Liability Insurance), ACORD 28 (Evidence of Property In | High]
- **Lien Waiver** (`fi-lien-waiver`): Legal document in which a contractor, subcontractor, or supplier waives their right to file a mechanic's lien against the property — exchanged with payment. [State-specific lien waiver statutes (e.g., California Civil Code §8132-8138), AI | High]
- **Safety Plan / Site Safety Documentation** (`doc-safety-plan-site`): Project-specific safety plan defining hazard controls, emergency procedures, PPE requirements, and safety protocols. Required by OSHA and most contracts. [OSHA 29 CFR 1926 (Construction Safety Standards), ANSI/ASSP Z590.3 (Prevention t | Low]
- **SWPPP / Environmental Compliance Document** (`doc-swppp-enviro`): Stormwater Pollution Prevention Plan and related environmental compliance documentation — required by EPA and state environmental agencies for construction sites disturbing 1+ acre of soil. [EPA NPDES Construction General Permit, Clean Water Act §402, state stormwater pr | None]

**Closeout Documents**
- **Punch List (as Document)** (`doc-punch-list-as`): Formal list of deficiencies and incomplete work items that must be corrected before the owner accepts the project — compiled during substantial completion walkthrough. [AIA A201 §9.8 (Substantial Completion), AIA G704 (Certificate of Substantial Com | High]
- **As-Built Documentation** (`ph-asbuilt`): Marked-up drawings and records showing the actual constructed conditions — deviations from design documents, field modifications, and final installed locations of all systems. As-built documentation is a contractual closeout deliverable. [AIA A201 §3.11 (Documents at the Site), contract-specific as-built requirements | Low]
- **O&M Manual (Operations & Maintenance)** (`doc-o-m-manual`): Compiled documentation of all installed equipment and systems — manufacturer manuals, maintenance schedules, warranty information, spare parts lists, and operating procedures. Required closeout deliverable for building handover. [AIA A201 §9.10 (Final Completion), spec section 01 78 00 (Closeout Submittals) | Medium]
- **Warranty Documentation** (`doc-warranty-docs`): Written guarantees from manufacturers, subcontractors, and the GC covering defects in materials and workmanship for a specified period after substantial completion. [AIA A201 §3.5 (Warranty), spec section 01 78 36 (Warranties), manufacturer-speci | Low]

**Forms & Templates**
- **Form / ProForma Form** (`doc-form-proforma`): Configurable structured form for data collection — checklists, inspection templates, safety forms, quality records, or any project-specific data collection need. [No industry standard for form structure | High]
- **Daily Log Template** (`doc-daily-log`): Configurable template defining which daily log sections are required for a project — determines which daily log tables are populated. [No standard | Medium]

**Standard Measures**
- **RFI Response Time** (`doc-rfi-response-2`): Average elapsed time from RFI issuance to final response — measures design team responsiveness and information flow efficiency. Formula: Response Date − Issue Date (in calendar or business days). [CII benchmarking metrics | High]
- **RFI Volume Density** (`doc-rfi-volume`): Total RFI count relative to project size — measures design completeness and coordination quality. Formula: Total RFIs / Project Value (per $M) or Total RFIs / Project SF. High RFI density suggests incomplete design documents or poor coordination. [CII benchmarking | High]
- **Submittal Cycle Time** (`doc-submittal-cycle`): Average elapsed time from submittal submission to final approval — measures the review and approval efficiency for product data and shop drawings. Formula: Approval Date − Submission Date (in business days). Includes resubmission cycles. [CSI Practice Guide for Submittals | High]
- **Submittal Rejection Rate** (`doc-submittal-reject`): Percentage of submittals rejected or returned for revision on first review — measures submittal preparation quality and design coordination. Formula: (Rejected + Revise & Resubmit) / Total Submittals × 100. [CSI submittal review categories | High]
- **Drawing Revision Frequency** (`doc-drawing-revision-2`): Average number of revisions per drawing sheet — measures design stability and change volume. Formula: Total Revisions / Total Drawing Sheets. Late-stage revisions (post-IFC) are a stronger signal of design instability than early-stage revisions. [NCS revision numbering conventions | High]
- **Daily Log Completion Rate** (`fo-daily-log-2`): Percentage of working days with a completed daily log entry — measures field reporting consistency. Formula: Days with Daily Log / Total Working Days × 100. Consistent daily logging is a prerequisite for field data quality. [Company-specific daily reporting requirements | High]
- **Correspondence Response Time** (`doc-correspondence-r`): Average elapsed time from correspondence issuance to response — measures communication efficiency between project parties. Formula: Response Date − Issue Date (in business days). [Contract-specified response periods | High]

### Field Operations

**Daily Log Framework**
- **Daily Log (Header)** (`fo-daily-log-header`): The parent record for all daily field data — one per project per day. Acts as the container that links all log sections (manpower, equipment, weather, delays, notes, etc.) to a single date and project. [No universal standard | High]
- **Daily Log Section Configuration** (`fo-daily-log`): The template configuration that defines which log sections are required, optional, or hidden for a project. [No standard | Medium]

**Field Notes & Communications**
- **Daily Log Note** (`fo-daily-log-note`): Free-text narrative entry by field personnel documenting site conditions, work progress, issues, and events — the superintendent's daily diary. Multiple notes may be entered per day by different team members. [No universal standard | High]
- **Phone Call Log Entry** (`fo-phone-call-log`): Record of field-related phone calls — caller, recipient, subject, and notes. Documents verbal communications for the project record. [No universal standard | Medium]
- **Plan Revision Receipt** (`fo-plan-revision`): Field record of updated drawing revisions received on site — which drawings were updated, to what revision, and when the field team received them. Critical for confirming that construction crews are working from current documents. [AIA A201 (document distribution) | Medium]

**Workforce & Labor**
- **Manpower Log Entry** (`fo-manpower-log`): Daily record of workforce on site by trade and vendor — captures trade name, number of workers, hours per worker, total man-hours, and the vendor/subcontractor responsible. One entry per trade per vendor per day. [No universal standard | High]
- **Construction Report Entry** (`fo-const-report`): Certified payroll and workforce diversity reporting record — tracks hours by worker classification (apprentice, journeyman, foreman) and demographic category (minority, women, veteran, local) per trade and vendor. [Davis-Bacon Act (federal prevailing wage), state prevailing wage statutes, local | High]
- **Timecard Entry** (`fo-timecard-entry`): Structured record of individual worker hours — employee, date, hours worked, cost code, project, overtime classification. More granular than manpower log (individual workers vs. crew-level). [FLSA (Fair Labor Standards Act), state labor laws, union agreements for overtime | None (Not Ready)]
- **Employee Record** (`fo-employee-record`): Master record for a field worker — name, role, job title, trade classification, certifications, company assignment. The identity record that timecards, crew memberships, and workforce planning reference. [No universal construction standard | None (Not Ready)]
- **Crew / Crew Membership** (`fo-crew-crew`): Grouping of workers into a named crew assigned to a specific scope of work — crew name, members, lead/foreman, trade, and assignment. Crews are the operational unit of field labor management. [No standard | None (Not Ready)]

**Equipment**
- **Equipment Log Entry** (`fo-equip-log-entry`): Daily record of equipment on site — equipment name, hours operating, hours idle, and inspection status. One entry per piece of equipment per day. Captures both utilization (operating vs. idle) and safety compliance (inspected flag, inspection_time). [OSHA 29 CFR 1926 Subpart N (Cranes), Subpart O (Motor Vehicles), Subpart P (Exca | High]
- **Equipment Master Record** (`fo-equip-master`): Catalog record for a piece of equipment — type, model, serial number, capacity, ownership/rental status, maintenance schedule. The identity record for equipment that field logs, timecards, and maintenance records reference. [No universal standard | None (Not Ready)]
- **Equipment Timecard Entry** (`fo-equip-timecard`): Structured time record for individual equipment — hours by category (operating, idle, maintenance, travel), cost allocation, and operator assignment. More granular than the daily equipment log (includes cost allocation and maintenance time). [No universal standard | None (Not Ready)]

**Materials & Deliveries**
- **Delivery Log Entry** (`fo-dlvy-log-entry`): Daily record of materials received on site — contents description, delivery source, tracking number, time, and comments. One entry per delivery event per day. The contents field is a free-text description of what was delivered. [No universal standard | High]
- **Material Shipment Record** (`fo-mat-shipment`): Structured tracking of material shipments from supplier/fabricator to jobsite — shipment date, expected arrival, contents, quantity, and carrier. Tracks the supply chain between purchase order and site delivery. [No universal standard | None (Not Ready)]
- **Material Receipt Record** (`fo-mat-receipt`): Formal acknowledgment that materials arrived on site matching the purchase order — quantity verification, condition inspection, and storage location. More structured than the delivery log (which is a field observation). [No universal standard | None (Not Ready)]

**Weather**
- **Weather Log Entry** (`fo-weather-log`): Daily record of observed weather conditions on the project site — temperature, precipitation, wind, sky conditions, humidity, ground conditions, and whether weather caused a delay. Multiple readings may be taken throughout the day. [No universal standard | High]

**Delays**
- **Delay Log Entry** (`fo-delay-log-entry`): Record of a delay event during construction — structured type, duration, start/end time, comments, and location. Delay entries document when work was stopped or significantly slowed and why. [AACE 29R-03 (Forensic Schedule Analysis), AIA A201 §15.1.6 (Claims for Additiona | High]

**Productivity & Quantities**
- **Productivity Log Entry** (`fo-productivity-log`): Daily record of quantities delivered and used/installed — tracks material flow from delivery to installation by vendor and commitment line item. Captures previously_delivered, previously_used, quantity_delivered (today), and quantity_used (today). [No universal standard | Low]
- **Quantity Log Entry** (`fo-quantity-log`): Daily record of installed quantities by cost code — quantity, unit of measure, description, and cost code. Distinct from productivity log (which tracks vendor-level delivery and installation). [No universal standard | Medium]

**Safety**
- **Safety Violation Log Entry** (`fo-safety-violation`): Daily log record of a safety violation observed during field walkthroughs — subject, comments, issued_to (person or company), compliance_due date, and safety_notice type. [OSHA 29 CFR 1926 (Construction Safety Standards), company safety programs | Medium]
- **Accident Log Entry** (`fo-accident-log`): Daily log record of an accident or safety event — involved person, involved company, time, comments, and location. [OSHA 29 CFR 1904 (Recording and Reporting), OSHA 300/300A/301 forms | Medium]

**Inspections**
- **Daily Log Inspection Entry** (`fo-daily-log-insp`): Inspection event recorded as part of the daily log — inspecting entity, inspection type, inspector name, start/end time, and comments. [Building code inspection requirements, OSHA, project specifications | Medium]

**Visitors**
- **Visitor Log Entry** (`fo-visitor-log`): Daily record of non-project visitors on the construction site — visitor identity, purpose, arrival/departure times, and comments. Required for site security, safety compliance (visitors must be briefed on site hazards), and liability documentation. [OSHA general duty clause (site safety for visitors), company safety policies, co | Medium]

**Waste & Environmental**
- **Waste Log Entry** (`fo-waste-log-entry`): Daily record of construction waste generated and removed — material type, quantity, disposal method, disposal location, and vendor. Tracks what waste was produced, how much, and where it went. [LEED MR Credit (Construction Waste Management), EPA RCRA (hazardous waste), loca | Medium]
- **Dumpster Log Entry** (`fo-dumpster-log`): Daily record of dumpster activity — dumpsters delivered and removed from the site. Tracks the containers, not the waste contents (that's the waste log). Dumpster management is a general conditions cost item. [No standard | Medium]

**Scheduled Work**
- **Scheduled Work Log Entry** (`fo-scheduled-work`): Daily record of subcontractors scheduled to work — whether they showed up, how many workers, hours, and what tasks they were assigned to. The 'showed' boolean is the simplest plan-vs-actual signal in field operations. [No universal standard | High]
- **Scheduled Work Task Link** (`fo-scheduled-work-2`): Junction record linking a scheduled work entry to one or more CPM schedule tasks — the bridge between 'what was planned today' (daily log) and 'what the schedule says' (CPM). [No standard | High]

**Field Productivity Measurement**
- **Field Productivity Record** (`fo-field-productivi`): Structured measurement of field production — actual quantities produced vs. planned, by trade and activity. [No universal standard | None (Not Ready)]
- **Actual Production Quantity** (`fo-actual-productio`): Recorded measurement of work actually completed — the 'actuals' side of earned value. Tracks what was installed in the field, by scope item, providing the physical percent complete that drives payment and forecasting. [PMI PMBOK (Earned Value Management), AACE | None (Not Ready)]
- **Budgeted Production Quantity** (`fo-budgeted-product`): Planned quantity for a scope item — the 'budget' side of production tracking. Defines how much work is expected to be installed, creating the baseline for earned-value comparison. [PMI PMBOK, AACE | None (Not Ready)]

**Time & Material Tracking**
- **T&M Ticket** (`fo-t-m-ticket`): Time and material ticket documenting extra work performed outside the base contract — captures labor hours, equipment hours, and materials used for change work or disputed scope. [AIA A201 §7.1.3 (for cost-plus changes), contract-specific T&M provisions | None (Not Ready)]
- **T&M Labor Entry** (`fo-t-m-labor-entry`): Labor portion of a T&M ticket — worker classification, hours, rate, and total labor cost. Multiple labor entries per ticket (different workers, different rates). [Contract schedule of rates, prevailing wage (if applicable) | None (Not Ready)]
- **T&M Equipment Entry** (`fo-t-m-equip-entry`): Equipment portion of a T&M ticket — equipment type, hours, rate, and total equipment cost. Equipment rates follow the contract schedule or industry published rates (Blue Book, FEMA). [Blue Book rental rates, FEMA equipment rates, contract-specific rates | None (Not Ready)]
- **T&M Material Entry** (`fo-t-m-mat-entry`): Material portion of a T&M ticket — material description, quantity, unit cost, and total material cost. Materials must be documented with receipts or invoices. Markup on materials is governed by contract terms (typically 10-15% overhead and profit). [Contract markup provisions | None (Not Ready)]

**Workforce Planning**
- **Assignment** (`fo-assignment`): Allocation of a worker or crew to a specific project for a date range — the workforce planning layer above daily manpower logs. Assignments represent the planned labor allocation; manpower logs record the actual. [No standard | None (Not Ready)]
- **Workforce Request** (`fo-workforce-req`): Request for additional workers or specific trades — submitted by field teams to the home office or labor pool. Tracks the demand signal for labor that may not yet be assigned. Request status (open, filled, unfilled) indicates workforce availability. [No standard | None (Not Ready)]

**Field Reporting & Distribution**
- **Daily Report Distribution** (`fo-daily-report`): The act of sending the completed daily log to stakeholders — tracks who received the compiled report, when it was distributed, and by whom. Distribution is a formal project management action — it makes the daily log an official project record. [Contract-specific distribution requirements | High]

**Standard Measures**
- **Daily Log Completion Rate** (`fo-daily-log-2`): Percentage of project days with completed daily logs — completed logs / total project days × 100. The single best metric for field data quality across all sections. Projects below 80% completion rate have unreliable field data. [No universal standard | High]
- **Daily Log Distribution Rate** (`fo-daily-log-dist`): Percentage of completed daily logs distributed to stakeholders — distributed / completed × 100. Distribution transforms the daily log from internal notes into an official project record with contractual weight. [Contract-specific distribution requirements | High]
- **Peak Daily Headcount** (`fo-peak-daily`): Maximum number of workers on site in a single day during the project — MAX(SUM(workers per trade per vendor) per day). Indicates project peak complexity and coordination burden. [OSHA staffing ratios | High]
- **Average Daily Headcount** (`fo-average-daily`): Average number of workers on site per active construction day — AVG(daily headcount) across construction days, excluding non-work days. Indicates sustained labor intensity throughout the project. [No universal standard | High]
- **Equipment Utilization Rate** (`fo-equip-utilizatio`): Percentage of equipment time spent operating vs. idle — operating hours / (operating + idle hours) × 100. Calculated per equipment type and per project. Low utilization indicates over-provisioning or scheduling inefficiency. [No universal standard | High]
- **Plan Percent Complete (PPC)** (`fo-plan-percent`): Percentage of scheduled work that was actually performed — showed / total scheduled × 100. The Last Planner System's primary reliability metric. Measures whether the weekly or daily work plan was executed as planned. No-show rate = 1 - PPC. [Lean Construction Institute | High]
- **Delay Frequency** (`fo-delay-frequency`): Number of recorded delay events per active project month, segmented by delay type — total delays / active months. Enables comparison of delay exposure across projects, geographies, and seasons. [AACE 29R-03 (Forensic Schedule Analysis) | High]
- **Weather Delay Rate** (`fo-weather-delay`): Percentage of project days with weather-related delays — weather delay days / total project days × 100. Geographic and seasonal comparison metric. Combines weather observation data (conditions) with delay records (impact). [Contract-specific weather provisions | High]
- **Waste Diversion Rate** (`fo-waste-diversion`): Percentage of construction waste recycled or diverted from landfill — recycled/diverted volume / total waste volume × 100. Required for LEED MR credit (50-75% target). Increasingly required by local ordinances and owner sustainability mandates. [LEED MR Credit (Construction Waste Management) | Medium]

### Financial Instruments

**Budget & Cost Structure**
- **Project Budget** (`fi-project-budget`): The total approved budget for a project — the financial ceiling against which all costs are measured. Lifecycle: Created (preconstruction) → Approved → Active → Modified (via budget modifications) → Closed (at closeout). Original budget vs. [AACE 18R-97 (Cost Estimate Classification) | High]
- **Budget Line Item** (`fi-budget-line-item`): An individual row in the project budget — allocates a specific dollar amount to a specific cost code or scope of work. Lifecycle: Created → Active → Modified (via budget modifications and change orders) → Closed. [CSI MasterFormat (cost code basis) | High]
- **Cost Code** (`fi-cost-code`): A categorization code that classifies costs by type of work — typically based on MasterFormat divisions. The Rosetta Stone between financial data and building systems. Key properties: code number, description, MasterFormat division, standard vs. [CSI MasterFormat (50 divisions) | High]
- **WBS Code** (`fi-wbs-code`): Work Breakdown Structure code that adds a second dimension to cost classification — segments cost within a cost code by phase, location, or category. Example: cost code 03 30 00 (Cast-in-Place Concrete) + WBS 'Foundation' vs. WBS 'Elevated Slab'. [PMI PMBOK WBS (§5.4) | Medium]
- **Budget Code** (`fi-budget-code`): A grouping code applied to budget line items for reporting and categorization — distinct from cost codes. Key properties: code, description, project-specific or company-standard. Budget codes are a REPORTING overlay, not a transactional code. [Company-specific reporting hierarchies | Medium]

**Commitments**
- **Commitment (Subcontract)** (`fi-commit-subcontra`): A legally binding agreement between the GC and a subcontractor for a defined scope of work — the largest category of project spend. Lifecycle: Draft → Out for Signature → Executed → Active → Complete → Closed. [AIA A101/A201 (owner-contractor) | High]
- **Commitment (Purchase Order)** (`fi-commit-purchase`): An agreement to purchase materials, equipment, or services from a supplier — typically for materials not included in a subcontract scope. Lifecycle: Draft → Issued → Active → Complete → Closed. [UCC Article 2 (sale of goods) | High]
- **Commitment Line Item** (`fi-commit-line-item`): A cost-code-level detail row within a commitment — breaks the total commitment into budget-aligned allocations. Key properties: cost code, WBS code, description, amount, commitment reference. [Follows parent commitment's standard/format | High]

**Change Management**
- **Change Event (CE)** (`fi-chg-event-ce`): A documented scope or cost change that captures the initial identification of a change — before formal commitment modification. Lifecycle: Created → Pending → Approved → Void; also mapped to Potential Change Order. [AACE RP 10S-90 (Cost Engineering) | High]
- **Change Event Line Item** (`fi-chg-event-line`): A cost-code-level detail row within a change event — breaks the estimated change cost into budget-aligned allocations. [Follows parent CE standard/format | High]
- **Potential Change Order (CPCO)** (`fi-pot-chg-order`): An intermediate instrument that bridges a change event to a commitment change order — represents the GC's request to modify a specific subcontract based on an approved change. Lifecycle: Created (from CE) → Pending → Approved (becomes CCO) → Void. [AIA G709 (Proposal Request) | High]
- **Commitment Change Order (CCO)** (`fi-commit-chg-order`): A formal, approved modification to a subcontract or purchase order — changes the committed dollar amount. Lifecycle: Draft → Pending → Approved → Void; also Proceeding. [AIA G701 (Change Order) | High]
- **CCO Line Item** (`fi-cco-line-item`): A cost-code-level detail row within a commitment change order — modifies specific commitment line item amounts. [Follows parent CCO standard/format | High]
- **Owner Change Order (Prime Contract CO)** (`fi-owner-chg-order`): A formal modification to the prime contract between owner and GC — changes the contract value and potentially the schedule. Lifecycle: Draft → Pending → Approved → Void. [AIA G701 (Change Order) | Medium]
- **Budget Modification** (`fi-budget-mod`): An internal budget transfer or adjustment — moves money between budget line items without changing the total budget. Lifecycle: Created → Approved → Posted. [Company-specific budget transfer policies | High]

**Cost Tracking**
- **Direct Cost** (`fi-direct-cost`): A non-commitment expenditure — costs that don't flow through a subcontract or purchase order. Includes GC self-performed labor, small material purchases, equipment rental, T&M charges, reimbursables. Lifecycle: Created → Approved → Paid. [Company-specific cost tracking policies | High]
- **Direct Cost Line Item** (`fi-direct-cost-line`): A cost-code-level detail row within a direct cost — enables granular cost tracking for non-commitment expenses. Key properties: cost code, WBS code, description, amount, direct cost reference. [Follows parent direct cost format | High]

**Billing & Payment**
- **Owner Invoice / Pay Application** (`fi-owner-invoice`): A periodic billing from the GC to the owner for work completed — the GC's request for payment under the prime contract. Lifecycle: Draft → Submitted → Under Review → Approved → Paid; also Rejected, Revised. [AIA G702/G703 (Application and Certificate for Payment) | High]
- **Subcontractor Invoice** (`fi-sub-invoice`): A periodic billing from a subcontractor to the GC for work completed under a subcontract. Lifecycle: Draft → Submitted → Under Review → Approved → Paid; also Rejected, Revised. [AIA G702/G703 (adapted for sub billing) | High]
- **Retainage** (`fi-retainage`): Funds withheld from progress payments as security for completion of work — released at substantial completion or final completion. [State retainage statutes (vary by jurisdiction) | Medium]
- **Payment** (`fi-payment`): The actual transfer of funds between parties — the final step in the billing cycle. Lifecycle: Scheduled → Processed → Cleared. Key properties: amount, date, from party, to party, invoice reference, payment method. [Prompt Payment Acts (federal and state) | High]
- **Lien Waiver** (`fi-lien-waiver`): A legal document in which a party waives their right to file a mechanic's lien against the property — exchanged with each payment. [State mechanic's lien statutes (vary by jurisdiction) | High]

**Financial Classification**
- **Schedule of Values (SOV)** (`fi-schedule-values`): A cost breakdown of a contract that defines the billing structure — line items represent discrete portions of work that can be billed as completed. Lifecycle: Created (with contract) → Active (updated each billing cycle) → Complete (100% billed). [AIA G703 (Continuation Sheet) | Medium]
- **Allowance** (`fi-allowance`): A budget line item for work that cannot be precisely defined at contract time — price is estimated and reconciled to actual cost. Lifecycle: Established (in contract) → Active (as work performed) → Reconciled (actual vs. allowance). [AIA A201 §3.8 (Allowances) | Low]
- **Contingency** (`fi-contingency`): A budget reserve for unforeseen costs — not allocated to any specific scope until needed. Lifecycle: Established (in budget) → Active (drawn down as changes occur) → Depleted or Returned. Key properties: contingency type (owner vs. GC vs. [AACE 10S-90 (Cost Engineering) | Low]

**Earned Value & Forecasting**
- **Cost Forecast / Estimate at Completion (EAC)** (`fi-cost-forecast`): A projection of total project cost at completion — combines actual cost to date with estimated cost to complete. Updated monthly or more frequently on active projects. EAC = Actual Cost to Date + Estimated Cost to Complete. [AACE RP 10S-90 | Medium]
- **Cash Flow Projection** (`fi-cash-flow`): A time-phased projection of money in (owner payments) and money out (sub payments, direct costs) — shows when cash is needed. Updated monthly. Key properties: period, projected income, projected outflow, net cash position, cumulative cash position. [PMI PMBOK cash flow management | Low]

**Standard Measures**
- **Budget Variance** (`fi-budget-variance`): The difference between budgeted cost and actual cost (committed + direct + approved changes) at any point in time. Formula: Budget Amount − (Committed Cost + Direct Cost + Approved Changes). [AACE cost variance analysis | High]
- **Cost Growth %** (`fi-cost-growth`): The percentage increase from original budget to final cost. Formula: (Final Cost − Original Budget) / Original Budget × 100. Measures total cost escalation including all changes, direct costs, and adjustments. [AACE 10S-90 | High]
- **Cost Performance Index (CPI)** (`fi-cost-perf-index`): The ratio of earned value to actual cost — measures cost efficiency. Formula: CPI = Earned Value / Actual Cost. CPI > 1.0 = under budget. CPI < 1.0 = over budget. CPI = 1.0 = on budget. Used as a multiplier in EAC forecasting. [ANSI/EIA-748 (EVMS) | Medium]
- **Committed Cost vs. Budget** (`fi-committed-cost`): The ratio of total committed cost (subcontracts + POs + approved changes) to budget. Formula: Total Committed / Budget × 100. Measures how much of the budget is locked into contracts. [AACE cost control | High]
- **Change Order Rate** (`fi-chg-order-rate`): The number and value of change orders relative to original contract value. Formula: (Total CO Value / Original Contract Value) × 100. Can be computed separately for owner COs (revenue) and commitment COs (cost). [CII benchmarking metrics | High]
- **Contingency Burn Rate** (`fi-contingency-burn`): The rate at which contingency is consumed relative to project progress. Formula: (Contingency Used / Original Contingency) / (% Complete). Burn rate > 1.0 = contingency consumed faster than progress, indicating the project may exhaust reserves. [AACE contingency management | Low]
- **Invoice Processing Time** (`fi-invoice-processi`): The elapsed time from invoice submission to approval. Formula: Approval Date − Submission Date (in business days). Measures administrative efficiency and cash flow impact. [Prompt Payment Act benchmarks | High]
- **Cash Flow Variance** (`fi-cash-flow-2`): The difference between projected cash position and actual cash position at a point in time. Formula: Actual Cash Position − Projected Cash Position. Positive = more cash than expected. Negative = less cash than expected. [AACE cash flow analysis | Low]
- **Estimate at Completion Variance** (`fi-estimate-at`): The difference between the projected final cost (EAC) and the original budget. Formula: EAC − Original Budget. Tracks how the projected final cost evolves over time. Early EAC variance is a leading indicator of final cost growth. [AACE 10S-90 | Medium]

### Locations

**Site Level**
- **Project Site** (`loc-project-site`): The overall geographic boundary of a construction project — everything within the property line or limit of work. Top of the location hierarchy; every project has exactly one. Anchored by coordinates (lat/long or state plane). [OmniClass Table 13 | High]
- **Building** (`loc-building`): A distinct structure within the project site — the primary vertical container for constructed space. Multi-building projects separate records by structure. Single-building projects still carry one Building node for hierarchy consistency. [OmniClass Table 13 | High]
- **Exterior Zone** (`loc-exterior-zone`): A defined area outside the building envelope but within the project site — organized by function or orientation. Facade orientation zones (N/S/E/W) are critical for enclosure work as different exposures have different weather and solar conditions. [OmniClass Table 13 | Medium]
- **Laydown / Staging Area** (`loc-laydown-staging`): Designated areas for material storage, prefabrication, and equipment staging. Shift as construction progresses — what was steel staging becomes curtain wall staging. Tight urban sites have minimal laydown, requiring just-in-time delivery. Leaf node. [OSHA 1926.250 (Materials Storage) | Medium]
- **Right-of-Way** (`loc-right-way`): Public or utility easement areas where project work occurs outside the property line. Governed by municipal permits with strict restoration requirements. Work windows may be restricted (night work, traffic hours). [MUTCD (Manual on Uniform Traffic Control Devices) | Low]
- **Temporary Facility** (`loc-temp-facility`): Contractor-provided temporary structures that support construction but are removed at completion. General conditions cost items. Location on site affects logistics. Removed before final site improvements. Leaf node. [OSHA 1926 Subpart F (Fire Protection) | Low]

**Building Vertical**
- **Floor / Level** (`loc-floor-level`): A horizontal plane within a building that divides it vertically — the primary vertical organizing unit. The most universally used location level. Most field records attach at floor level or below. [OmniClass Table 13 | High]
- **Below-Grade Level** (`loc-below-grade`): Floors below ground level — basements, sub-basements, parking levels, underground mechanical spaces. Unique challenges: waterproofing, hydrostatic pressure, radon mitigation, garage ventilation, fire department access. [IBC Chapter 4 (special uses) | High]
- **Roof Level** (`loc-roof-level`): The top of the building including roof surface, mechanical penthouse, and rooftop equipment areas. Both an enclosure system (membrane, insulation, flashing) and a mechanical platform (RTUs, cooling towers, exhaust fans). [NRCA Roofing Manual | High]

**Floor Division**
- **Zone / Wing** (`loc-zone-wing`): A horizontal subdivision of a floor — used for phasing, scope separation, or building geometry. Project-specific designations defined by the team to organize work. A 50-story tower might define zones as quadrants per floor. [Project-specific | Medium]
- **Core / Shaft** (`loc-core-shaft`): Vertical penetrations that run through multiple floors — stairs, elevators, mechanical shafts, duct risers. Unique vertical elements that span the building height. [IBC Chapter 7 (fire-resistance-rated assemblies) | Medium]
- **Ceiling Plenum** (`loc-ceiling-plenum`): The space between the finished ceiling and the structural deck above — where most MEP distribution occurs. The most contested space in a building — 5+ trades working in the same 18-36 inch space. [IBC 717 (fire dampers in plenums) | Low]

**Room & Space**
- **Room / Space** (`loc-room-space`): An individually identifiable enclosed space within a building — defined by walls, doors, and a room number. The unit of occupancy. Healthcare patient rooms may have 150+ punch items each. [OmniClass Table 13 | Medium]
- **Functional Area** (`loc-functional-area`): A space defined by its function rather than enclosure — may span rooms or be part of a larger space. Functional areas have specific code requirements: mechanical rooms (ventilation, fire separation), electrical rooms (clearances, access), data rooms ... [IBC Chapter 4 (special uses by function) | Medium]
- **Wet Area** (`loc-wet-area`): Spaces with plumbing fixtures and waterproofing requirements — bathrooms, kitchens, janitor closets, mechanical rooms with floor drains. Waterproofing testing (shower pan flood tests, floor drain tests) required before finishes. [IPC/UPC (plumbing codes) | Medium]

**Sub-Space**
- **Wall / Surface** (`loc-wall-surface`): An individual wall or surface within a room — identified by orientation or designation. Primarily BIM-driven and punch-item-driven. [OmniClass Table 13 | Low]
- **Equipment Location** (`loc-equip-location`): The specific location of a major piece of installed equipment — tracked for commissioning, maintenance, and warranty. Every major equipment piece gets a unique tag (AHU-1, CHL-1) that persists from design through 30+ years of operations. [ASHRAE Standard 202 (commissioning) | Low]
- **Penetration / Opening** (`loc-penetration-open`): A specific penetration through a fire-rated or smoke-rated assembly — tracked for firestopping compliance. Every penetration through a rated assembly must be firestopped per a UL-listed system. [IBC 714 (penetrations) | Low]

**Cross-Cutting Overlay**
- **Fire / Smoke Compartment** (`loc-fire-smoke`): A code-defined area enclosed by fire-rated or smoke-rated construction — may span rooms or zones. A regulatory overlay on the physical layout that defines where fire barriers must be maintained, smoke dampers required, and rated doors installed. [IBC Chapters 7 & 7A | Low]
- **Work Zone / Phase Area** (`loc-work-zone-phase`): A temporary designation that defines where active construction work is occurring — shifts as the project progresses. Dynamic — moves weekly or daily. Safety zones (crane radius, excavation, hot work) have specific regulatory requirements. [OSHA 1926 Subpart N (Cranes) | Medium]
- **Commissioning Zone** (`loc-cx-zone`): A grouping of spaces for the purpose of systems commissioning — may align with HVAC zones, floors, or functional groups. Groups equipment and spaces tested together. [ASHRAE Standard 202 (Commissioning) | Low]
- **Grid Line Intersection** (`loc-grid-line`): A coordinate location defined by the intersection of structural grid lines — the universal reference system for locating anything in a building. Every drawing references grid lines. Survey and layout is done to grid lines. [AIA A201 (drawing standards) | Low]

**Standard Measures**
- **Location Depth Utilization** (`loc-location-depth`): Measures how many levels of the location hierarchy a company uses in field records — from site-level only (depth 1) to room-level (depth 4+). Higher depth = more granular defect tracking. [None — operational maturity metric | High]
- **Defect Density by Location Type** (`loc-defect-density`): Count of quality observations, punch items, and inspection deficiencies per location node — reveals where problems concentrate. Calculation: (observations + punch items + deficient inspections) / location count at each hierarchy level. [ISO 9001 (nonconformance tracking) | High]
- **Punch Items per Room** (`loc-punch-items-per`): Count of punch list items assigned to each room-level location — the primary closeout workload metric. Calculation: total punch items / total rooms. Segmented by room type for cross-project comparison. [AIA/AGC best practices for punchlist management | High]
- **Floor Completion Rate** (`loc-floor-completion`): Percentage of punch items and observations closed per floor over time — tracks vertical closeout progress. Calculation: closed_items / total_items per floor measured weekly. [Lean Construction (last planner system) | High]
- **Location Coverage Rate** (`loc-location-coverag`): Percentage of defined locations that have at least one quality record (observation, inspection, or punch item) attached — measures inspection thoroughness. Calculation: locations_with_records / total_defined_locations. [ISO 19011 (audit sampling) | High]
- **Safety Incident Density by Zone** (`loc-safety-incident`): Count of safety observations and incidents per work zone or floor — identifies high-risk areas. Calculation: safety_observations / active_work_zones. [OSHA recordkeeping | Medium]
- **Firestopping Deficiency Rate** (`loc-firestopping-def`): Percentage of inspected penetrations with firestopping deficiencies — a top quality metric for multi-story buildings. Calculation: deficient_penetrations / inspected_penetrations. Segmented by shaft type, rated assembly type, and floor. [IBC 714 | Medium]

### Models & BIM

**BIM Authoring Models**
- **3D Building Information Model** (`bim-3d-building-info`): A parametric digital representation of the physical and functional characteristics of a building — the authoritative geometric and data source for design, construction coordination, and facility operations. [AIA E203 (BIM and Digital Data Protocol) | None]
- **Federated Model** (`bim-federated-model`): A combined multi-discipline model assembled from individual discipline models — the integrated view used for coordination, clash detection, and owner reviews. [AIA E203 (multi-discipline coordination) | None]
- **4D Model (Schedule-Linked)** (`bim-4d-model`): A 3D model linked to the project schedule — visualizes construction sequence over time by associating model elements with schedule activities. Enables construction phasing visualization, logistics planning, and progress tracking. [BIM Execution Plan phasing requirements | None]
- **5D Model (Cost-Linked)** (`bim-5d-model-cost`): A 3D model linked to cost data — enables quantity-based estimating and cost visualization by associating model elements with cost information (cost codes, unit prices, assemblies). Quantities extracted from the model drive the estimate. [AACE cost estimating practices | None]
- **As-Built Model** (`bim-as-built-model`): A BIM model updated to reflect actual constructed conditions — incorporates field modifications, deviations from design, and final installed locations. [AIA E203 (as-built modeling requirements) | None]

**Model Elements & Properties**
- **Model Element** (`bim-model-element`): An individual component within a BIM model — a wall, beam, column, pipe, duct, fixture, or any other discrete building component with geometry, type, material, and location properties. [IFC entity types (IfcWall, IfcBeam, IfcPipeSegment, etc.) | None]
- **Level of Development (LOD)** (`bim-level-developmen`): A specification that defines the completeness and reliability of a model element at a given project phase — governs what information can be extracted from the model. [AIA E203 | None]
- **Quantity Takeoff** (`bim-quantity-takeoff`): Material quantities extracted from model elements — counts, areas, volumes, lengths, and weights derived from model geometry and type properties. Quantities drive estimating (5D), procurement, and production tracking. [AACE quantity surveying practices | None]
- **Model Properties & Parameters** (`bim-model-properties`): The non-geometric data attached to model elements — manufacturer, model number, fire rating, acoustic rating, energy performance, warranty period, maintenance requirements, and other attribute data. [COBie (Construction Operations Building Information Exchange) | None]

**Coordination & Clash Detection**
- **Clash Detection Result** (`bim-clash-detection`): An identified spatial conflict between model elements from different disciplines — a pipe running through a beam, a duct intersecting a structural column, or conflicting MEP routes. [BIM Execution Plan clash detection protocols | None]
- **Coordination Issue** (`qsr-coord-issue`): A design or constructability problem identified during BIM coordination review — the actionable output of clash detection and model review. [AIA E203 | High]
- **BIM Coordination Meeting** (`bim-bim-coord`): A regular team meeting where designers, trade contractors, and the GC review the federated model, resolve clashes, and make coordination decisions. Typically weekly during design and early construction. [AIA E203 (BIM coordination requirements) | Medium]

**Reality Capture**
- **Point Cloud / Laser Scan** (`bim-point-cloud`): 3D spatial data captured by terrestrial or mobile laser scanning — represents existing conditions or as-built geometry as millions of measured points. [ASTM E57 (3D Imaging Data Exchange) | None]
- **360 Photo / Spherical Capture** (`bim-360-photo`): Spherical photographs taken at regular intervals throughout the project — creates an immersive, navigable visual record of site conditions over time. [No universal standard | Medium]
- **Drone Capture** (`bim-drone-capture`): Aerial photography, videography, photogrammetry, and LiDAR data captured by unmanned aerial vehicles (UAVs) — provides site-level documentation, earthwork volume calculations, progress monitoring, and safety surveillance. [FAA Part 107 (commercial drone operations) | Low]
- **Construction Photo** (`bim-const-photo`): A standard photograph documenting site conditions, progress, quality issues, safety observations, or completed work — the most fundamental visual record in construction. [Company documentation protocols | High]

**Visualization & Communication**
- **Model-Based Drawing** (`bim-model-based`): A 2D drawing view generated from or linked to a 3D BIM model — plans, sections, elevations, and details extracted from the model rather than drawn independently. [NCS (National CAD Standard) | High]
- **Digital Twin** (`bim-digital-twin`): A living digital representation of the building that combines the as-built BIM model with real-time sensor data, maintenance records, and operational information — the post-construction evolution of BIM. Updated continuously during operations. [ISO 23247 (Digital Twin Manufacturing) | None]

**Standard Measures**
- **Coordination Issue Density** (`bim-coord-issue-2`): Number of coordination issues per million dollars of project value — measures the volume of BIM-identified spatial and design conflicts relative to project size. [No universal standard | High]
- **Coordination Issue Resolution Time** (`bim-coord-issue-3`): Average days from coordination issue creation to resolution — measures how quickly spatial and design conflicts are resolved. Faster resolution = less downstream delay. Segmented by issue_type (Clash vs. Design Review vs. [No universal standard | High]
- **Clash Resolution Rate** (`bim-clash-resolution`): Percentage of identified clashes resolved before construction start — measures pre-construction coordination effectiveness. Higher rate = fewer field conflicts. [No universal standard | Medium]
- **Drawing Revision Frequency** (`doc-drawing-revision-2`): Number of drawing revisions issued per drawing set per month — measures design stability and churn. High revision frequency late in the project signals design instability and increases rework risk. [No universal standard | High]
- **Photo Documentation Rate** (`bim-photo-docs-rate`): Number of construction photos documented per day or per million dollars — measures visual documentation discipline and thoroughness. Higher rates indicate more rigorous field documentation. [No universal standard | High]
- **BIM Coordination Adoption Score** (`bim-bim-coord-2`): A composite measure of BIM coordination maturity based on: (1) whether coordination_issues exist, (2) issue volume relative to project size, (3) issue_type diversity (Clash + Design Review + Constructability), (4) resolution rate, (5) RFI linkage rat... [No universal standard | Medium]

### Organizations

**Owner / Developer**
- **Private Developer** (`org-private-develope`): Company or individual funding a project for profit — develops to sell, lease, or operate. Decision authority on scope, budget, and schedule. [State real estate licensing | Low]
- **Institutional Owner** (`org-institutional-ow`): Organization building for its own use — corporate campus, hospital, university, government facility. End user and operator of the facility. Defines program requirements, coordinates stakeholders, provides operations input, and plans occupancy. [Joint Commission (healthcare) | Low]
- **Public / Government Entity** (`org-public-governmen`): Federal, state, or local government agency procuring a public project. Regulated procurement authority with statutory constraints — competitive bidding, prevailing wage enforcement, ADA compliance, environmental review. [Miller Act (federal bonding) | Low]

**Construction Management**
- **General Contractor (GC)** (`org-gen-contr-gc`): Company contracted to construct the project — holds risk for cost, schedule, and quality under lump sum or GMP contract. Single point of responsibility to the owner. Manages subcontractors, schedule, quality control, safety, and cost control. [AGC contract forms | High]
- **Construction Manager at Risk (CM at Risk)** (`org-const-manager-at`): CM engaged during design to provide preconstruction services (estimating, VE, constructability, scheduling), then transitions to GC role during construction under a GMP. Most common delivery method for large commercial projects. [AIA A133 (CM at Risk) | High]
- **Construction Manager Agency (CM Agency)** (`org-const-manager`): CM acts as owner's agent — manages project but does NOT hold trade contracts or bear construction cost risk. Provides schedule/budget management, trade coordination, quality oversight, and reporting. Owner holds direct contracts with trades. [AIA B132/B133 (CM services) | Medium]
- **Design-Builder** (`org-design-builder`): Single entity responsible for both design and construction under one contract. Single point of responsibility for owner. Manages architect directly and self-coordinates design-construction overlap. [AIA A141 (design-build) | High]
- **Program Manager** (`org-program-manager`): Firm managing a portfolio of related projects for an owner — multiple projects under one program. Provides portfolio-level schedule, budget, and risk management with standardization across projects. [CMAA (program management standards) | Medium]

**Design Team**
- **Architect of Record (AOR)** (`org-architect-record`): Licensed architecture firm responsible for building design and construction documents — stamp on architectural drawings. Performs construction administration (CA): submittal review, RFI response, field observation, punch list walk. [AIA B101 (design services) | Medium]
- **Structural Engineer** (`org-struct-engineer`): Licensed engineering firm responsible for structural system design — foundation design, connection design, structural calculations. Stamp on structural drawings. Performs submittal review and RFI response for structural scope. [ASCE 7 (structural loads) | Medium]
- **MEP Engineer** (`org-mep-engineer`): Licensed engineering firm(s) responsible for mechanical, electrical, and plumbing system design — HVAC, plumbing, electrical, fire protection. Energy code compliance, load calculations, equipment schedules. [ASHRAE (HVAC design) | Medium]
- **Civil Engineer** (`org-civil-engineer`): Licensed engineering firm responsible for site design — grading, utilities, stormwater, roadways, erosion control. Stamp on civil drawings. Active from Preconstruction through Sitework. Subconsultant to architect or direct owner contract. [ASCE (civil engineering) | Low]
- **Fire Protection Engineer** (`org-fire-prot`): Licensed engineering firm responsible for fire protection and life safety system design — sprinkler design, fire alarm design, smoke control, egress analysis, fire code compliance. Active from Preconstruction through Commissioning. [NFPA 13 (sprinklers) | Low]
- **Geotechnical Engineer** (`org-geotechnical-eng`): Licensed engineering firm investigating subsurface conditions and recommending foundation design — soil borings, lab testing, foundation recommendations, earthwork specs, dewatering recommendations. [ASTM D1586 (SPT) | Low]
- **Landscape Architect** (`org-landscape-archit`): Licensed design firm responsible for exterior landscape, hardscape, irrigation, and site amenity design. Produces planting plans, irrigation plans, hardscape details. Active during Preconstruction and Site Improvements phase. [ASLA standards | Low]

**Specialty Consultants**
- **Specifications Writer** (`org-specifications-w`): Firm or individual that writes the project manual (specifications) governing materials and installation methods. Product research, code cross-referencing, coordination with design team. Specifications are the legal backbone of construction quality. [CSI MasterFormat | Low]
- **Lighting Designer** (`org-lighting-designe`): Firm specializing in architectural and functional lighting design — lighting layout, fixture selection, controls design, daylighting analysis, energy code compliance. Bridges engineering and architecture. [IES (Illuminating Engineering Society) | Low]
- **Acoustics Consultant** (`org-acoustics-consul`): Firm specializing in sound isolation, room acoustics, and noise control — STC/IIC ratings, room finish recommendations, mechanical noise criteria, environmental noise assessment. Critical for healthcare, education, residential, and performing arts. [ASTM E90/E413 (STC) | None]
- **Building Envelope Consultant** (`org-building-envelop`): Firm specializing in design and performance of the building exterior skin — air/water/thermal barrier design, curtain wall engineering review, mock-up testing oversight, field quality inspection. [ASTM E2178/E2357 (air barrier) | Low]
- **Sustainability / LEED Consultant** (`org-sustainability-l`): Firm managing green building certification and sustainability requirements — LEED/WELL credit tracking, energy modeling coordination, material documentation (EPDs, HPDs, VOC content), commissioning coordination. [LEED (USGBC) | Low]
- **Code Consultant** (`org-code-consultant`): Firm specializing in building code interpretation and life safety compliance — code analysis, occupancy classification, egress analysis, fire resistance requirements, ADA compliance, variance applications. Critical for complex occupancies. [IBC/ICC (building code) | None]

**Trade Contractors**
- **Subcontractor (Trade-Specific)** (`org-sub-trade`): Specialty contractor performing a specific trade scope of work under contract to the GC — self-performs trade work, manages own workforce, procures trade-specific materials, responsible for quality of installed work and safety of own crews. [State contractor licensing | High]
- **Self-Performing GC Division** (`org-self-performing`): GC's own workforce performing specific trade work — typically concrete, carpentry, general conditions, demolition. Same scope as subcontractor but with GC-employed labor. Costs tracked as direct costs rather than commitments. [State contractor licensing | Medium]

**Suppliers & Fabricators**
- **Material Supplier** (`org-mat-supplier`): Company that sells construction materials — manufacturer or distributor. Supplies materials per purchase order, schedules deliveries, provides product documentation and warranties. Delivery reliability directly impacts schedule. [ASTM (material standards) | Medium]
- **Fabricator** (`org-fabricator`): Company that manufactures custom construction components from approved shop drawings — steel fabricators, curtain wall fabricators, precast producers, custom casework shops. Fabrication per approved shop drawings with factory QC. [AISC (steel fabrication) | Medium]
- **Equipment Rental Company** (`org-equip-rental`): Company providing construction equipment on a rental basis — tower cranes, excavators, aerial lifts, temporary fencing, generators. Equipment mobilization, maintenance, and operator support (if provided). Active during Construction. [OSHA 29 CFR 1926 Subpart N (cranes) | Medium]

**Testing & Inspection**
- **Special Inspection Agency** (`org-special-insp`): Independent testing firm performing code-required special inspections — structural steel connections, concrete testing, fireproofing thickness, welding inspection. Code requires independence from contractor. [IBC Chapter 17 (special inspections) | Medium]
- **Materials Testing Lab** (`org-mat-testing-lab`): Laboratory that tests construction materials for specification compliance — concrete cylinder testing (7-day and 28-day strength), soil compaction, steel tensile testing, asphalt testing, mortar testing. Active during Construction. [ASTM C31/C39 (concrete) | Low]
- **Commissioning Agent (CxA)** (`rl-cx-agent-cxa`): Independent firm verifying building systems perform to design intent — pre-functional testing, functional performance testing, seasonal testing. Produces commissioning plan, checklists, test reports, deficiency lists, final commissioning report. [ASHRAE Guideline 0 (commissioning) | Low]
- **Environmental Monitoring Firm** (`org-enviro-monitorin`): Firm monitoring environmental compliance during construction — air quality monitoring, noise monitoring, stormwater sampling, hazmat oversight, regulatory reporting. [EPA regulations | Low]

**Regulatory Authorities**
- **Building Department** (`org-building-departm`): Local government agency that reviews plans, issues building permits, performs progress inspections, and issues certificates of occupancy. Permit timeline varies from 2 weeks to 12+ months. Plan review comments generate design revisions. [IBC/ICC (building code) | Medium]
- **Fire Marshal / Fire Department** (`org-fire-marshal`): Fire authority having jurisdiction (AHJ) for fire and life safety compliance — fire protection plan review, fire alarm plan review, field inspections, acceptance testing, hydrant flow testing. Fire marshal sign-off is required for CO. [NFPA 1 (fire code) | Medium]
- **Health Department** (`org-health-departmen`): Government agency regulating health-related construction — healthcare facilities, food service, pools, labs, childcare. Plan review for health-related spaces, field inspections, operational permits. Active from Preconstruction through Closeout. [FGI Guidelines (healthcare) | Low]
- **Environmental / EPA Agency** (`org-enviro-epa`): Federal, state, or local environmental regulatory authority — environmental impact review, stormwater permit oversight, air quality compliance, hazmat oversight. NEPA review on federal projects can add years. [NEPA | Low]
- **OSHA / Safety Authority** (`org-osha-safety`): Federal or state occupational safety and health authority — workplace safety regulation, site inspections (scheduled and unscheduled), citation issuance, fatality investigation. [OSHA 29 CFR 1926 (construction safety) | Medium]
- **Zoning / Planning Authority** (`org-zoning-planning`): Local government agency controlling land use, density, setbacks, and project approvals — zoning compliance review, variance review, site plan approval, community review facilitation. Zoning approval is a prerequisite for building permit. [Local zoning codes | None]

**Financial Institutions**
- **Construction Lender** (`org-const-lender`): Bank or financial institution providing construction financing — construction loan funding, draw review, progress inspection (lender's inspector), compliance monitoring. Lender draws tied to percent complete — monthly pay applications scrutinized. [OCC (banking regulation) | Low]
- **Surety / Bonding Company** (`org-surety-bonding`): Insurance company issuing performance and payment bonds guaranteeing contractor's obligations. Bonds protect owner (performance bond) and subcontractors (payment bond). [Miller Act (federal bonding) | Low]
- **Insurance Broker / Carrier** (`org-insurance-broker`): Companies providing construction insurance — general liability, workers' comp, builders risk, professional liability, umbrella, OCIP/CCIP wrap-up programs. Certificate of insurance collection is a major administrative task. Active across all phases. [State insurance regulations | Medium]

**Utilities**
- **Electric Utility** (`org-electric-utility`): Local electric utility company providing permanent electrical service — service design review, transformer supply/placement, metering, permanent connection, energization. [NEC/NFPA 70 (service entrance) | Low]
- **Gas Utility** (`org-gas-utility`): Local gas utility providing natural gas service — service design review, gas main extension (if required), meter installation, service connection. Gas service for HVAC, domestic hot water, commercial kitchen. [NFPA 54 (National Fuel Gas Code) | Low]
- **Water / Sewer Authority** (`org-water-sewer`): Municipal authority providing domestic water and sanitary sewer service — service size determination, tap/connection permits, meter installation, water quality testing. Water service affects fire protection (hydrant flow, fire pump supply). [International Plumbing Code | Low]
- **Telecom / Internet Provider** (`org-telecom-internet`): Companies providing data, voice, and internet service — service design, conduit and fiber routing, equipment room requirements, service activation. Multiple carriers may serve the building. Active during Preconstruction and Construction. [TIA-568 (cabling standards) | Low]

**Standard Measures**
- **Subcontractor Count per Project** (`org-sub-count-per`): Total number of distinct subcontractors and suppliers engaged on a project — measured from awarded subcontracts and purchase orders. Indicates project complexity and coordination burden. [AGC (project complexity metrics) | High]
- **Trade Coverage Rate** (`org-trade-coverage`): Percentage of project scope covered by contracted subcontractors vs. remaining unawarded scope — awarded value / estimated total value × 100. Tracks buyout progress during procurement. [AGC (procurement metrics) | High]
- **Vendor Insurance Compliance Rate** (`org-vendor-insurance`): Percentage of project vendors with current, compliant insurance certificates on file — compliant vendors / total vendors × 100. Tracks risk exposure from uninsured or underinsured trades. [AIA A201 (insurance requirements) | High]
- **Subcontractor Safety Incident Rate** (`org-sub-safety`): OSHA recordable incident rate per subcontractor — (number of recordable incidents × 200,000) / hours worked. Enables comparison of safety performance across trades and companies. [OSHA 29 CFR 1904 (recordkeeping) | Medium]
- **Design Team Responsiveness** (`org-design-team`): Average days for design team members to respond to RFIs and review submittals — measured from RFI creation to response and submittal submission to review completion. Indicates design team engagement quality. [AIA A201 (RFI and submittal timelines) | High]
- **Change Order Dispute Rate by Trade** (`org-chg-order`): Percentage of change orders disputed or rejected by trade — disputed COs / total COs per trade × 100. Identifies which trade relationships generate the most commercial friction. [AIA A201 (change order process) | High]

### Permits & Regulatory

**Construction Permits**
- **Building Permit** (`pr-building-permit`): Primary authorization from the local building department to begin construction. Lifecycle: Application → Plan Review → Approval → Issuance → Active → Final Inspection → Closed. [IBC (International Building Code) | None]
- **Demolition Permit** (`pr-demolition-permi`): Authorization to demolish or remove existing structures. Lifecycle: Application → Hazmat Survey → Review → Approval → Issuance → Active → Completion Notification. [OSHA 29 CFR 1926 Subpart T (Demolition) | None]
- **Renovation / Alteration Permit** (`pr-renovation-alter`): Authorization for modifications to existing structures — alterations / repairs / changes of use. Triggers when work exceeds substantial improvement thresholds defined by the jurisdiction (often 50% of building value). [IBC Chapter 34 (Existing Buildings) | None]
- **Temporary Structures Permit** (`pr-temp-structures`): Authorization for temporary construction facilities — scaffolding / shoring / formwork / temporary enclosures / construction hoists. Required for structures affecting public safety or right-of-way. [OSHA 29 CFR 1926 Subpart L (Scaffolds) | None]
- **Trade Permit** (`pr-trade-permit`): Separate jurisdictional permits required for specific building system work — electrical / plumbing / mechanical / fire protection / elevator. [NEC (National Electrical Code) | None]

**Site & Environmental Permits**
- **Environmental Permit** (`pr-enviro-permit`): Regulatory authorizations for work affecting air quality / water resources / wetlands / hazardous materials. Issued by federal (EPA) / state / and local environmental agencies. [Clean Air Act | Low]
- **Stormwater Permit / SWPPP** (`pr-stormwater-permi`): Stormwater Pollution Prevention Plan and associated permit required for sites disturbing one or more acres. Mandates erosion and sediment control (ESC) best management practices (BMPs). [Clean Water Act Section 402 | Low]
- **Street / Right-of-Way Permit** (`pr-street-right-way`): Authorization for construction activities within the public right-of-way — lane closures / sidewalk closures / utility cuts / material staging / crane operations over public streets. Issued by local transportation or public works departments. [MUTCD (Manual on Uniform Traffic Control Devices) | None]
- **Utility Connection Permit** (`pr-utility-connecti`): Authorization to connect to or modify public utility infrastructure — water / sanitary sewer / storm sewer / gas / electric / telecommunications. Each utility provider has separate application processes and design review requirements. [Utility-specific standards (AWWA for water / NESC for electric) | None]

**Zoning & Land Use**
- **Zoning Approval** (`pr-zoning-appr`): Land use authorization confirming that the proposed project complies with local zoning ordinances — permitted uses / setbacks / height limits / lot coverage / floor area ratio (FAR) / parking requirements / density. [Local zoning ordinances | None]
- **Variance / Special Exception** (`pr-variance-special`): Formal relief from specific zoning requirements when strict compliance creates undue hardship. Lifecycle: Application → Staff Review → Public Hearing → Board Decision → Appeal Period. [State zoning enabling acts | None]

**Plan Review & Regulatory Approvals**
- **Building Department Plan Review** (`pr-building-departm`): Formal review of construction documents by the building department to verify code compliance before permit issuance. Covers structural / life safety / accessibility / energy / and building code requirements. [IBC | Low]
- **Fire Marshal Review** (`pr-fire-marshal`): Fire and life safety plan review and field approval by the fire marshal or fire prevention bureau. Covers fire sprinkler design / fire alarm systems / means of egress / fire-rated assemblies / hazardous materials storage / and fire access. [NFPA 1 (Fire Code) | Low]
- **Health Department Approval** (`pr-health-departmen`): Regulatory approval from the health department for projects involving food service / healthcare / pools / laboratories / or other health-regulated occupancies. [FDA Food Code | None]

**Regulatory Inspections**
- **AHJ Inspection** (`pr-ahj-insp`): Field inspections performed by the Authority Having Jurisdiction (building department) at required construction milestones. Verifies that work in place complies with approved plans and applicable codes. [IBC Section 110 (Required Inspections) | Medium]
- **Special Inspection** (`pr-special-insp`): Code-required inspections performed by independent certified special inspectors (not the building department) for critical structural and life-safety work. Required where deficiencies would be concealed and could create structural failure. [IBC Chapter 17 (Special Inspections and Tests) | Medium]
- **Third-Party Testing** (`pr-third-party`): Independent materials testing and quality assurance performed by certified testing laboratories. Verifies that construction materials and installed systems meet specifications and code requirements. [ASTM standards (C39 concrete / D1557 soil / E1105 water infiltration) | Low]

**Certificates & Occupancy**
- **Certificate of Occupancy** (`pr-cert-occupancy`): Final authorization from the building department to occupy and use a completed building for its permitted purpose. Confirms all code requirements met / all required inspections passed / all special inspection letters received. [IBC Section 111 (Certificate of Occupancy) | None]
- **Temporary Certificate of Occupancy** (`pr-temp-cert`): Conditional occupancy approval when a building is safe to occupy but has outstanding items preventing full CO. Specifies conditions and deadline for completing remaining work. [IBC Section 111.3 (Temporary Occupancy) | None]
- **Certificate of Completion** (`pr-cert-completion`): Regulatory sign-off confirming that construction work is complete and compliant — used for projects without occupancy (site work / infrastructure / demolition) or for trade-specific scope completion. [IBC Section 111.1 | None]
- **Letter of Compliance** (`pr-letter-comp`): Written confirmation from a regulatory agency / design professional / or special inspector that specific work or systems comply with applicable codes and standards. Lifecycle: Inspection/Testing → Report → Letter Issuance. [IBC Chapter 17 (Special Inspection letters) | None]

**Safety & Labor Compliance**
- **OSHA Notification** (`pr-osha-notificatio`): Required notifications to OSHA and activity-specific safety permits for hazardous construction operations. [OSHA 29 CFR 1926 (Construction Safety) | Low]
- **Site Safety Plan** (`pr-site-safety-plan`): Project-specific safety documentation identifying hazards / control measures / emergency procedures / and safety responsibilities. [OSHA 29 CFR 1926 Subpart C (General Safety) | Low]
- **Labor Compliance** (`pr-labor-comp`): Requirements for workforce compensation / documentation / and equal opportunity — particularly on public and federally funded projects. [Davis-Bacon Act (federal) | None]

**Permit Lifecycle & Tracking**
- **Permit Application** (`pr-permit-applicati`): The formal request to a regulatory agency for a permit / approval / or certificate. Includes project information / scope of work / applicable codes / required documents (plans / calculations / surveys) / and fees. [Local building department application requirements | Low]
- **Permit Status** (`pr-permit-status`): The current state of a permit in its lifecycle — from application through issuance / active construction / and final closeout. Tracking status across all required permits is a critical path management activity. [No universal standard — each jurisdiction defines its own status terminology | Low]
- **Inspection Scheduling** (`pr-insp-scheduling`): The process of requesting / scheduling / and coordinating regulatory inspections with the AHJ / special inspectors / and testing labs. [IBC Section 110 | Medium]

**Standard Measures**
- **Permit Cycle Time** (`pr-permit-cycle`): Elapsed time from permit application submission to permit issuance. Calculation: issuance date minus application date / optionally excluding resubmission periods. Segmented by permit type (building / trade / environmental) and jurisdiction. [No universal standard | Low]
- **Inspection Pass Rate** (`qsr-insp-pass-rate`): Percentage of regulatory inspections (AHJ and special) that pass on the first attempt. Calculation: passed inspections / total inspections × 100. [Industry benchmark: 85-95% first-pass rate for well-managed projects | Medium]
- **Regulatory Hold Duration** (`pr-reg-hold`): Total calendar days of construction delay caused by regulatory actions — stop-work orders / permit delays / failed inspections requiring correction / expired permits. [AACE delay classification | Low]
- **Open Permit Aging** (`pr-open-permit`): Average elapsed days that permits remain in open/active status. Calculation: sum of (current date or closure date minus issuance date) / total permits. Tracks whether permits are being closed out in a timely manner. [No universal standard | None]
- **Compliance Document Completeness** (`pr-comp-doc`): Percentage of required regulatory and compliance documents received and verified. Calculation: received documents / total required documents × 100. [Owner/CM contract requirements | Medium]
- **Permit Renewal Rate** (`pr-permit-renewal`): Percentage of permits that require renewal or extension during the project — indicating original validity period was insufficient. Calculation: renewed permits / total permits × 100. [No universal standard | None]

### Phases

**Preconstruction**
- **Programming & Feasibility** (`ph-program`): Owner defines project requirements and validates viability — needs assessment, site analysis, zoning review, pro forma development, and environmental studies. Gate: program approval / authorization to proceed with design. [ASTM E1557 (UNIFORMAT II) | None]
- **Design Development** (`ph-design`): Architects and engineers develop the design from concept through construction documents — schematic design (SD), design development (DD), construction documents (CD), code review, structural/MEP engineering, energy modeling, specifications. [AIA B101 (design services) | Low]
- **Estimating & Budgeting** (`ph-estimating`): Develop cost estimates from conceptual through detailed GMP or hard bid — quantity takeoff, unit pricing, subcontractor pricing, risk contingency, value engineering. Multiple estimate rounds: conceptual (SD), detailed (DD), final (CD). [AACE 18R-97 (cost estimate classification) | Medium]
- **Permitting & Approvals** (`ph-permit`): Secure regulatory approvals required before construction — building permits, zoning variances, environmental permits, utility coordination, fire marshal review, DOT permits, stormwater permits. Gate: building permit issued / notice to proceed. [IBC/ICC (building code) | Low]
- **Preconstruction Planning** (`ph-precon-plan`): GC develops execution strategy before breaking ground — baseline schedule, logistics plan, phasing strategy, safety plan, quality plan, procurement strategy, staffing plan. CM-at-Risk does this during design; design-bid-build GCs do it after award. [PMI PMBOK (scheduling) | Medium]

**Procurement**
- **Bidding & Buyout** (`ph-bidding`): Solicit bids from subcontractors and suppliers, level bids, negotiate scope, and award contracts — scope definition, bid solicitation, bid leveling, insurance/bonding verification, contract execution. [AIA A201 (general conditions) | Medium]
- **Submittals & Shop Drawings** (`ph-submittals`): Subcontractors prepare detailed fabrication and product documents for architect/engineer review — submittal preparation, review cycles, resubmittals, product substitution requests. Submittal log is a critical schedule driver. [CSI MasterFormat (section-based organization) | High]
- **Fabrication & Long-Lead Items**: Materials fabricated off-site with delivery schedules established — structural steel (8-16 wks), curtain wall (12-24 wks), elevators (16-30 wks), switchgear (12-20 wks), precast, HVAC equipment, custom casework. [AISC (steel fabrication) | Low]
- **Material Ordering & Delivery Coordination**: Standard materials ordered and delivery sequenced to match construction schedule — PO issuance, delivery scheduling, staging area planning, just-in-time coordination, material tracking. [CSI MasterFormat (material sections) | Medium]

**Mobilization**
- **Site Setup** (`ph-site-setup`): Establish temporary facilities and infrastructure to support construction — temporary fencing, construction entrance, trailer placement, temporary utilities (power, water, sanitation), site signage, erosion control, tree protection. [OSHA 29 CFR 1926 (site safety) | Medium]
- **Safety & Environmental Orientation** (`ph-safety-orient`): Establish safety culture and environmental compliance from day one — site-specific safety orientation, toolbox talks, emergency action plan, hospital route, environmental awareness training, hazard communication. [OSHA 29 CFR 1926.21 (safety training) | Medium]

**Sitework & Foundations**
- **Demolition & Site Clearing** (`ph-demo`): Remove existing structures and vegetation to prepare for new construction — building demolition, selective demolition, clearing and grubbing, underground obstruction removal, hazmat abatement if required. Gate: site cleared and ready for earthwork. [OSHA 29 CFR 1926.850 (demolition safety) | Medium]
- **Earthwork** (`ph-earthwork`): Excavate and prepare the ground for foundations — bulk excavation, rock removal, shoring/sheeting, dewatering, proof rolling, structural fill, compaction, fine grading. Differing site conditions are the #1 source of construction claims. [ASTM D698/D1557 (compaction testing) | Medium]
- **Site Utilities** (`ph-site-util`): Install underground infrastructure before building foundations cover access — sanitary sewer, storm drainage, domestic and fire water, gas service, electrical and telecom ductbank, grease interceptors. Must complete before foundation/slab work. [International Plumbing Code | Medium]
- **Foundations** (`ph-foundations`): Construct below-grade structural support — pile driving or drilled shafts, spread footings, grade beams, foundation walls, waterproofing, backfill, underslab plumbing and electrical. Concrete testing (cylinders) is mandatory. [ACI 318 (concrete design) | Medium]
- **Slab on Grade** (`ph-slab`): Pour ground-level concrete floor slab — vapor barrier, underslab insulation, rebar/WWF placement, embedded conduit, concrete placement, finishing, curing, control joint sawing. Large pours are major production events. [ACI 302.1R (floor slab construction) | Medium]

**Structure**
- **Structural Steel Erection** (`ph-steel`): Erect the steel frame including columns, beams, girders, metal deck, and shear studs — connection bolting/welding, plumbing and aligning. Tower crane operations dominate logistics. Fall protection is the primary safety concern. [AISC 360 (steel design) | High]
- **Elevated Concrete** (`ph-elev-conc`): Place concrete on metal deck or formwork for elevated floor slabs — deck prep, rebar/post-tensioning placement, embedded items, concrete pumping, finishing, curing, PT stressing. Follows deck erection floor-by-floor. [ACI 318 (concrete design) | Medium]
- **Concrete Frame** (`ph-conc-frame`): For concrete-framed buildings: form and pour columns, beams, and slabs floor-by-floor — formwork erection, rebar placement, embedded items, concrete placement, form stripping, shoring/reshoring, curing. Formwork cycle time drives schedule. [ACI 318 (concrete design) | Medium]
- **Stairs & Miscellaneous Metals**: Install permanent stairs, handrails, embed plates, lintels, shelf angles, bollards, and equipment supports. Shelf angles for masonry/exterior panels must be in place before enclosure starts. Stairs provide worker access between floors. [AISC (misc metals) | Medium]

**Building Enclosure**
- **Curtain Wall & Glazing** (`ph-curtainwall`): Install exterior glass and aluminum systems to enclose the building — curtain wall units (unitized or stick-built), windows, storefronts, structural silicone, perimeter sealant. [AAMA 501 (water testing) | High]
- **Masonry & Cladding** (`ph-masonry`): Install opaque exterior wall systems — brick veneer, precast panels, metal panels, backup wall, through-wall flashing, weep systems, control joints. Weather-sensitive: masonry can't be laid below 40°F without protection. [TMS 402/602 (masonry) | High]
- **Air & Moisture Barrier** (`ph-barrier`): Establish continuous air and moisture barrier across the building envelope — fluid-applied or sheet membrane, transition detailing at openings, penetration sealing, inspection and testing. [ASTM E2178/E2357 (air barrier testing) | Medium]
- **Roofing** (`ph-roofing`): Install roof membrane system to achieve weather-tight condition — roof insulation, cover board, membrane installation, flashing, sheet metal, roof drainage, penetration detailing. Dry-in is a major project milestone enabling interior work. [NRCA (roofing standards) | High]

**MEP Rough-In**
- **Above-Ceiling Coordination** (`ph-abv-ceil`): Resolve spatial conflicts between MEP systems before installation — 3D coordination / BIM clash detection, routing prioritization, trade coordination meetings, clearance verification. The difference between a smooth MEP install and chaos. [BIM Execution Plan (AGC/AIA) | Medium]
- **HVAC Distribution** (`ph-hvac-dist`): Install ductwork and hydronic piping — main duct and branch installation, HVAC piping (chilled/hot water), equipment pads, duct and pipe insulation, hanger installation. Ductwork is the largest spatial consumer in the ceiling. [SMACNA (duct construction) | High]
- **Plumbing Rough-In** (`ph-plumb-ri`): Install supply and waste piping — domestic water distribution, sanitary waste and vent, gas piping, pipe insulation, fire stopping at penetrations. Testing is a critical hold point: pressure test for supply, DWV test for waste. [International Plumbing Code (IPC) | High]
- **Electrical Rough-In** (`ph-elec-ri`): Install conduit, wire, and power distribution — main conduit and feeder installation, branch circuits, wire pulling, panel and switchgear installation, transformer setting, cable tray, grounding. Permanent power energization is a major milestone. [NEC/NFPA 70 (electrical code) | High]
- **Fire Protection** (`ph-fp-ri`): Install sprinkler mains, branches, standpipe risers, and fire pump — main and branch line installation, sprinkler head rough-in, seismic bracing, FDC installation. Sprinkler head layout drives ceiling coordination. Gate: system tested and tagged. [NFPA 13 (sprinklers) | High]
- **Low Voltage Rough-In** (`ph-lv-ri`): Install raceways and cabling for data, security, fire alarm, and AV — conduit and cable tray, backbone and horizontal cabling, fire alarm wiring, security wiring. Often the last trade into the ceiling space. Gate: cabling complete and tested. [TIA-568 (cabling) | Medium]

**Interior Rough-In**
- **Metal Stud Framing** (`ph-framing`): Frame interior partitions, soffits, and bulkheads — wall layout, metal stud framing, blocking for fixtures/casework, door frame setting, fire-rated assembly framing. Blocking for grab bars, casework, TV mounts must be coordinated with MEP. [ASTM C645/C754 (steel framing) | Medium]
- **Drywall** (`ph-drywall`): Hang and finish gypsum board — drywall hanging, taping and finishing, sanding, specialty boards (moisture/abuse/fire-rated), patching around MEP. Above-ceiling inspection must happen BEFORE drywall closes the ceiling. [GA-216 (gypsum application) | High]
- **Ceiling Grid** (`ph-ceil-grid`): Install suspension system for acoustic ceilings — main tee and cross tee, hanger wire, seismic bracing, grid leveling, access panel framing. Grid installation signals all above-ceiling MEP work must be complete. [ASTM C635/C636 (ceiling suspension) | Medium]

**Finishes & MEP Trim**
- **Paint & Wall Coatings** (`ph-paint`): Apply primers, paint, and specialty coatings — primer, first coat, second coat, touch-up, specialty coatings, wall protection. Paint is the most common punch item across ALL project types. Typically the first finish in a space. [MPI (Master Painters Institute) | High]
- **Flooring** (`ph-flooring`): Install floor finishes — tile (ceramic, porcelain, stone), carpet (broadloom, tile), resilient (LVT, VCT, rubber), specialty (epoxy, terrazzo, polished concrete), base, transitions. Sequence: tile before casework, carpet last. [TCNA Handbook (tile) | High]
- **Ceilings** (`ph-ceilings`): Install acoustic ceiling tile and specialty ceiling finishes — acoustic tile, specialty ceilings (wood, metal, drywall), ceiling access panels, edge trim. One of the last overhead activities. Gate: ceilings complete. Duration: 1-2%. [ASTM E1264 (acoustical ceiling products) | Medium]
- **Doors & Hardware** (`mat-doors`): Install door slabs and finish hardware — door hanging, hinges, closers, locksets, pulls, keying, access control coordination, fire-rated door labeling. Top-3 punch item category on every project type. Gate: all doors hung and hardware operational. [DHI (Door and Hardware Institute) | High]
- **Casework & Millwork** (`ph-casework`): Install cabinets, countertops, trim, and built-in furnishings — cabinet installation, countertop templating and installation, trim and base molding, built-in shelving, toilet partitions and accessories. Gate: casework and accessories complete. [AWI (Architectural Woodwork Institute) | Medium]
- **HVAC Trim & Controls** (`ph-hvac-trim`): Install visible HVAC devices and controls — diffusers, grilles, thermostats, VAV box controls, damper actuators, BAS device installation, final duct connections. Must be complete before TAB. Gate: HVAC devices complete — ready for commissioning. [ASHRAE (controls) | Medium]
- **Plumbing Fixtures** (`ph-plumb-fix`): Install visible plumbing fixtures — toilets, sinks, faucets, accessories, stop and waste valves, floor drain covers. Fixtures are damage-prone. Gate: plumbing fixtures complete and operational. Duration: 1-2%. [International Plumbing Code | High]
- **Electrical Devices & Lighting** (`ph-elec-dev`): Install visible electrical devices and light fixtures — outlets, switches, cover plates, light fixtures, exit/emergency lighting, lighting controls, panel labeling. Major visual milestone. Gate: all devices and lighting operational. Duration: 2-3%. [NEC/NFPA 70 | High]
- **Fire Alarm & Detection Devices**: Install visible fire alarm devices — smoke/heat detectors, pull stations, horn/strobes, duct detectors, device addressing, panel programming. Device placement must match approved fire alarm drawings. [NFPA 72 (fire alarm code) | High]
- **Low Voltage Devices** (`ph-lv-dev`): Install visible low voltage devices — data jacks, cameras, card readers, intercoms, paging, AV equipment. Cable labeling and testing required. Gate: devices complete and tested. Duration: 1-2%. [TIA-568 (cabling) | Medium]

**Commissioning**
- **Pre-Functional Testing** (`ph-prefunc`): Verify each system component is properly installed before energizing or flowing — equipment installation verification, valve/damper tag verification, motor rotation checks, control device calibration, breaker verification. [ASHRAE Guideline 0 (commissioning process) | Medium]
- **Systems Startup** (`ph-startup`): Energize and start up individual systems for the first time — electrical energization sequence, boiler/chiller startup, pump/fan startup, fire pump acceptance test, elevator acceptance test, generator load bank test. [NETA (electrical testing) | Low]
- **Testing Adjusting & Balancing** (`ph-tab`): Balance air and water systems to design flow rates — air system balancing (supply, return, exhaust), hydronic balancing (chilled, hot, condenser water), sound and vibration measurement. TAB contractor typically independent third party. [AABC (Associated Air Balance Council) | Low]
- **Integrated Systems Testing** (`ph-integrated`): Verify systems work together correctly under various operating conditions — sequence of operations verification, failure mode testing, emergency power transfer, fire alarm integration, smoke control testing, elevator recall, BAS trending. [ASHRAE Guideline 0 | Low]
- **Performance Verification** (`ph-perf-ver`): Confirm building performs to design intent under actual conditions — energy performance, thermal comfort, acoustics, lighting levels, indoor air quality, envelope performance. Some tests require seasonal conditions (heating vs. cooling season). [ASHRAE 90.1 (energy) | None]

**Closeout**
- **Punch List** (`ph-punch`): Identify and correct remaining deficiencies before owner acceptance — architect punchlist walk, owner punchlist walk, deficiency documentation, trade-by-trade correction, re-inspection, sign-off. Typical project: 500-5,000 punch items. [AIA A201 (substantial completion) | High]
- **Final Inspections & Approvals**: Secure regulatory sign-offs required for occupancy — fire marshal inspection, building department final, elevator inspection, health department, certificate of occupancy (CO), temporary CO (TCO). Gate: certificate of occupancy issued. Duration: 1-2%. [IBC/ICC (building code) | High]
- **As-Built Documentation** (`ph-asbuilt`): Compile record documents reflecting actual constructed conditions — as-built drawing markup, O&M manual compilation, warranty compilation, spare parts and attic stock delivery, equipment data sheets. [AIA A201 (record documents) | Medium]
- **Owner Training** (`ph-training`): Train owner's facilities staff on building systems operation and maintenance — HVAC operations, BAS, fire alarm, elevator, security, electrical distribution, plumbing. Often rushed or skipped — leads to operational problems. [ASHRAE Guideline 0 (training requirements) | Low]
- **Contract Closeout** (`ph-contract-close`): Complete commercial and legal close of all contracts — final change order reconciliation, final pay application, retainage release, lien waiver collection, consent of surety, final accounting, contract close letter. [AIA A201 (final payment, retainage) | High]

**Warranty & Operations**
- **Warranty Period** (`ph-warranty`): Contractor responsible for correcting defects discovered after substantial completion — warranty claim response, defect investigation, repair coordination, manufacturer warranty coordination, 11-month warranty walk. [AIA A201 (warranty provisions) | Low]
- **Seasonal Commissioning** (`ph-seasonal-cx`): Verify HVAC performance across heating and cooling seasons not available during initial commissioning — heating season verification, cooling season verification, BAS setpoint optimization, energy monitoring review. [ASHRAE Guideline 0 (seasonal testing) | None]
- **Facility Transition** (`ph-transition`): Transfer operational knowledge and responsibility from construction team to facilities team — maintenance schedule establishment, spare parts inventory, vendor contact transfer, BAS access transfer, service contract establishment. [IFMA (facility management) | None]

**Standard Measures**
- **Phase Duration Variance**: Actual phase duration compared to baseline schedule — (actual days - planned days) / planned days × 100. Positive = behind schedule. Measured per phase and sub-phase using schedule milestones and activity completion data. [PMI PMBOK (schedule management) | Medium]
- **Schedule Performance Index** (`sch-schedule-perf`): Earned value metric: SPI = Earned Value / Planned Value. SPI < 1.0 = behind schedule, SPI > 1.0 = ahead. Calculated at project or phase level using weighted activity completion against the baseline schedule. [AACE RP 10S-90 (earned value) | Low]
- **Phase Milestone Compliance**: Percentage of phase transition milestones achieved on or before scheduled date — on-time milestones / total milestones × 100. Tracks critical path gates between phases. [PMI PMBOK (milestone management) | Medium]
- **Phase Overlap Ratio**: Percentage of a phase's duration that overlaps with adjacent phases — overlap days / total phase days × 100. Higher overlap = more concurrent/fast-track execution. Normal for procurement to overlap with construction. [PMI PMBOK (fast tracking) | Low]
- **RFI Density by Phase**: RFIs generated during each phase, normalized by duration (RFIs per week) or project value (RFIs per $M). Indicates information gap intensity at each project stage. [CSI (RFI process) | High]
- **Punch Item Density** (`qsr-punch-item-3`): Punch items per unit area (per 1,000 SF) or per trade during closeout — calculated from punch item creation dates and project gross area. Indicates construction quality and closeout efficiency. [AIA A201 (substantial completion criteria) | High]
- **Submittal Cycle Time** (`doc-submittal-cycle`): Average days from submittal submission to final approval — calculated per submittal, then aggregated by trade, spec section, or phase. Longer cycles delay procurement and fabrication start. [CSI (submittal management) | High]

### Project Attributes

**Project Identity**
- **Project Type** (`pa-project-type`): Primary functional use of the constructed facility — the single most impactful attribute for benchmarking. A $50M hospital and a $50M warehouse have completely different cost profiles, risk patterns, and trade compositions. [CSI UniFormat | High]
- **Project Subtype** (`pa-project-subtype`): Further classification within primary project type — customer-defined refinement. Examples: 'Class A Office', 'Acute Care', 'Fulfillment Center', 'Garden-Style Apartments', 'Charter School'. [None — customer-defined | Low]
- **Sector** (`pa-sector`): Public vs. private funding and ownership — determines procurement rules, bonding requirements, prevailing wage, and compliance burden. Public projects have transparency requirements and standardized procurement. [Federal Acquisition Regulation (FAR) | Medium]
- **Work Type** (`pa-work-type`): New construction vs. renovation vs. addition — fundamentally different risk and cost profiles. Renovation projects have 2-3x the change order rate of new construction due to unknown existing conditions. [None — industry-standard categories | Medium]
- **Program Type** (`pa-program-type`): Owner's capital program classification — groups projects by investment purpose across a portfolio. Useful for owners running rollout or prototype programs (retail chains, QSR, healthcare clinics) where standardized scope enables tight benchmarking. [None — customer-defined | Low]

**Financial**
- **Estimated Value** (`pa-estimated-value`): Owner's initial budget or estimated total project cost at authorization — the 'what we thought it would cost' baseline. Set before contracts are awarded. Different from contract value (which is the GC agreement). [AACE Classification System (Class 1-5 Estimates) | High]
- **Contract Value** (`pa-contract-value`): Contracted amount between owner and GC/CM — the GMP, lump sum, or negotiated target. This is the number subcontractors and the market see. Updated via change orders over the project lifecycle. Represents the GC's contractual obligation. [AIA A101/A133 (contract forms) | High]
- **Total Value Band** (`pa-total-value-band`): Bucketed range for benchmarking by project scale — log-scale bands work better than linear because construction costs, risks, and outcomes don't scale linearly. [ENR Project Cost Ranges | High]
- **Cost per SF** (`pa-cost-per-sf`): Total project cost divided by gross building area — the most comparable unit cost metric across building projects. Only meaningful for building projects (not infrastructure). Varies enormously by type: warehouse $100-200/SF vs. [RS Means Square Foot Cost Data | Medium]
- **Hard Cost** (`pa-hard-cost`): Direct construction cost excluding soft costs (design fees, permits, FF&E, land, financing). Typically 60-80% of total project cost. Isolates construction cost from owner's total investment. Essential for apples-to-apples cost benchmarking. [AACE Recommended Practice 10S-90 | Low]
- **Contingency Budget** (`pa-contingency-budg`): Owner and/or GC contingency allowance at project start — the risk reserve. Owner contingency covers scope changes; GC contingency covers construction risks. How fast contingency burns is a leading indicator of project risk. [AACE Recommended Practice 40R-08 (Contingency Estimating) | Low]
- **Final Cost at Completion** (`pa-final-cost-at`): Actual total cost when project is complete — includes all change orders, allowance adjustments, and final settlements. The gap between contract value and final cost is the most important financial performance indicator. [AACE Recommended Practice 10S-90 | Medium]

**Location**
- **Address** (`pa-address`): Street address of the project site — source for all derived geographic attributes. Geocoding converts address to latitude/longitude for distance, climate zone, and cost index calculations. [None — standard address format | High]
- **City** (`pa-city`): City or municipality where the project is located — enables local market analysis. Labor rates, material costs, and subcontractor availability vary significantly by metro area. [None — geographic standard | High]
- **State / Province** (`pa-state-province`): State or province jurisdiction — major benchmarking dimension. State drives labor law (prevailing wage, right-to-work), building code edition, licensing requirements, and tax structure. Top 20 US states cover 80%+ of commercial construction volume. [None — ISO 3166-2 | High]
- **Country** (`pa-country`): Country where the project is located — relevant for international benchmarking. Most construction data models are US-centric. International projects require currency normalization and different code/standard references. [ISO 3166-1 | High]
- **ZIP / Postal Code** (`pa-zip-postal-code`): Postal code of the project site — enables micro-market analysis and cost index application. RS Means and other cost databases use ZIP code for location cost factors. [USPS ZIP Code system | High]
- **Climate Zone** (`pa-climate-zone`): ASHRAE or IECC climate zone based on project location — drives envelope design, energy code compliance, and expected weather delay days. Zone 1 (hot-humid) to Zone 8 (subarctic) have fundamentally different design and construction requirements. [ASHRAE Standard 169 | None]
- **Seismic Design Category** (`pa-seismic-design`): ASCE 7 seismic classification based on site soil conditions and proximity to faults. Higher SDC = more expensive structure and connections. [ASCE 7 | None]
- **Region** (`pa-region`): Geographic region for market-level analysis — aggregates state-level data for regional trends. Region definitions vary by organization but should align with labor market and cost index boundaries. [ENR Regional Cost Data | Low]

**Schedule**
- **Planned Start Date** (`pa-planned-start`): Scheduled construction start date — typically Notice to Proceed (NTP) or mobilization date. The contractual baseline against which all schedule performance is measured. Some owners define this as first day of site work; others use NTP date. [AIA A201 | High]
- **Actual Start Date** (`pa-actual-start`): Actual date construction work began on site — may differ from planned start due to permitting, financing, or design delays. The gap between planned and actual start captures pre-construction schedule risk. [None — project-specific | High]
- **Planned Completion Date** (`pa-planned-completi`): Contractual substantial completion date — when the owner can occupy the facility. Different from final completion (all punch items done, all contracts closed). Most contracts use substantial completion as the contractual milestone. [AIA A201 (Substantial Completion) | High]
- **Actual Completion Date** (`pa-actual-completio`): Actual date of substantial completion — only available when the project reaches that milestone. The gap between contractual and actual completion is the core schedule performance metric. Average schedule growth is 10-20% for well-managed projects. [None — project-specific | Medium]
- **Planned Duration** (`pa-planned-duration`): Contractual construction duration in calendar days from NTP to substantial completion. Industry typically uses calendar days for overall duration (not working days). Excludes pre-construction. [PMI PMBOK Schedule Management | Medium]
- **Actual Duration** (`pa-actual-duration`): Actual construction duration from start to substantial completion — compare to planned duration for schedule performance, compare to benchmarks by type/size for relative performance. [None — project-specific | Medium]
- **Preconstruction Duration** (`pa-preconstruction`): Time from design authorization to NTP — often ignored but significantly affects construction outcomes. Design-build and CMAR compress this phase. DBB has the longest preconstruction. [AIA B101 (Design Services) | Low]
- **Season of Start** (`pa-season-start`): Season when construction begins — affects early work scope and weather delay risk. Winter starts in cold climates (ASHRAE zones 5-8) face frozen ground, concrete cold weather protection, and shorter daylight hours. [None — derived from start date | Medium]

**Procurement**
- **Delivery Method** (`pa-dlvy-method`): Project delivery system defining the design-construction relationship — one of the strongest predictors of project outcomes. DBB separates design and construction (owner bears coordination risk). [AIA A201 / A133 / A141 | Low]
- **Contract Type** (`pa-contract-type`): Compensation structure between owner and GC/CM — determines who bears cost risk. GMP: GC bears overrun risk above the guaranteed maximum. Lump Sum: GC bears all cost risk. Cost Plus: owner bears cost risk. [AIA A101 (Lump Sum) | Low]
- **Bid Type** (`pa-bid-type`): How the contractor was selected — affects pricing competitiveness and project relationship dynamics. Open competitive typically yields lowest initial price but highest change order rate. [Federal Acquisition Regulation (FAR) | None]
- **Bonding Requirement** (`pa-bonding-requirem`): Whether performance and payment bonds are required — adds 1-3% to cost and limits the contractor pool to firms with adequate bonding capacity. Federal projects over $250K require bonds (Miller Act). [Miller Act (Federal) | None]
- **Prevailing Wage** (`pa-prevailing-wage`): Whether prevailing wage requirements apply — adds 10-30% to labor cost depending on market differential between prevailing and market rates. Federal (Davis-Bacon) and state prevailing wage laws apply to public projects. [Davis-Bacon Act (Federal) | None]
- **Union / Open Shop** (`pa-union-open-shop`): Labor agreement type on the project — affects labor rates, productivity assumptions, and trade jurisdiction rules. Union projects have higher hourly rates but potentially different productivity. [NLRA | None]

**Building**
- **Gross Building Area** (`pa-gross-building`): Total enclosed floor area including all floors — the primary size dimension for cost benchmarking. Gross area includes occupied, mechanical, circulation, and wall space. Different from rentable or usable area. [ASTM E1836 (Standard Classification for Building Floor Area) | Medium]
- **Number of Stories Above Grade** (`pa-number-stories`): Count of floors above ground level — affects structural system, vertical transportation requirements, fire protection, and egress. [IBC Chapter 5 (Height and Area) | Medium]
- **Number of Stories Below Grade** (`pa-number-stories-2`): Count of floors below ground level (basement levels) — below-grade construction costs 1.5-3x above-grade per SF due to excavation, shoring, waterproofing, and dewatering. Parking structures below grade are common in urban settings. [IBC | Low]
- **Building Height** (`pa-building-height`): Height from grade to highest occupied floor or roof peak — triggers high-rise code requirements (typically 75+ ft). Determines crane type (tower vs. mobile), wind load design, and elevator requirements. [IBC Chapter 5 | Low]
- **Site Area** (`pa-site-area`): Total area of the project site — affects logistics, staging, and site improvement cost. Tight urban sites increase logistics cost due to limited staging, laydown, and equipment access. Large sites increase paving, utilities, and landscaping scope. [None — project-specific | Low]
- **Structural System** (`pa-struct-system`): Primary structural framing system — the single biggest cost and schedule driver for any building. Steel frame: faster erection, lighter foundation. Concrete frame: potentially cheaper for regular grids, longer cycle time. [AISC | Low]
- **Foundation Type** (`pa-foundation-type`): Primary foundation system — driven by geotechnical conditions, not project type. Deep foundations (driven piles, drilled shafts) add $20-100/SF to substructure cost vs. shallow foundations (spread footings). [ASCE 7 | None]
- **Number of Units** (`pa-number-units`): Count of individual units — apartments, hotel rooms, patient rooms, beds, or seats. Per-unit cost is the primary benchmark for residential, hospitality, and healthcare. Only applicable for certain building types. [None — type-specific unit definition | Low]
- **Parking Type** (`pa-parking-type`): Type of parking provided — parking structure can be 15-25% of total project cost. Underground parking is most expensive ($50-80K/space). Structured above-grade: $20-40K/space. Surface: $2-5K/space. [IBC | None]
- **Construction Type** (`pa-const-type`): IBC construction type classification — determines allowable building height and area, required fire-resistance ratings for structural elements, and material restrictions. [IBC Chapter 6 (Types of Construction) | None]
- **Occupancy Group** (`pa-occupancy-group`): IBC occupancy classification — drives code requirements for occupant load, egress, fire protection, accessibility, and special inspections. I-2 (hospitals) is the most demanding occupancy. [IBC Chapter 3 (Use and Occupancy) | None]
- **Building Code Edition** (`pa-building-code`): Edition of the building code adopted by the jurisdiction — affects energy, structural, and accessibility requirements. Jurisdictions adopt different editions on different timelines. Newer codes have stricter energy requirements. [IBC (2015 / 2018 / 2021 / 2024) | None]
- **Fire Sprinkler Requirement** (`pa-fire-sprinkler`): Whether automatic fire sprinklers are required or provided — sprinkler cost is $3-8/SF but allows construction type trade-offs (increased height and area under IBC). Almost all new commercial and multi-family construction is now fully sprinklered. [NFPA 13 / 13R / 13D | None]
- **Accessibility Standard** (`pa-accessibility-st`): Applicable accessibility standard — affects interior layout, restroom count, fixture selection, and door hardware. ADA applies to all commercial and public buildings. Fair Housing Act applies to multi-family (4+ units). [ADA | None]

**Standards**
- **LEED Certification** (`sc-leed-certificati`): LEED certification level targeted or achieved — the most widely recognized green building standard. LEED adds 2-8% to construction cost depending on level. Gold is the most common target for institutional and corporate projects. [USGBC LEED v4 / v4.1 | Low]
- **WELL Certification** (`pa-well-certificati`): WELL Building Standard certification level — focuses on occupant health and wellness (air quality, water quality, light, fitness, comfort). Growing adoption in corporate office and multi-family. Adds operational requirements beyond construction. [International WELL Building Institute (IWBI) | None]
- **Energy Code** (`pa-energy-code`): Energy code or standard the project must meet — becoming a bigger cost driver as standards tighten. Energy code determines insulation R-values, glazing performance, HVAC efficiency, and lighting power density. [ASHRAE 90.1 (2016/2019/2022) | None]
- **Net Zero Target** (`pa-net-zero-target`): Whether the project targets net-zero energy consumption — requires on-site renewable energy (typically solar), high-performance envelope, and ultra-efficient MEP systems. Adds 10-25% to construction cost. [DOE Zero Energy Ready Home | None]
- **Resilience Requirements** (`pa-resilience-requi`): Special requirements for disaster resilience — essential facilities (hospitals, fire stations, EOCs) must remain operational post-disaster. Requires enhanced structural, MEP, and envelope systems beyond standard code. [ASCE 7 (Risk Categories) | None]

**Organization**
- **Owner Type** (`pa-owner-type`): Type of entity that owns the project — drives procurement method, bonding requirements, and decision-making speed. Private developers prioritize speed and cost. Public owners have procurement rules and transparency requirements. [None — industry categories | Medium]
- **GC / CM Firm** (`pa-gc-cm-firm`): General contractor or construction manager firm name — enables contractor-level performance benchmarking across projects. With enough data: compare change order rates, schedule performance, safety records, and cost outcomes by contractor. [None — company name | High]
- **Architect of Record** (`pa-architect-record`): Architect responsible for design and construction administration — A/E firm performance significantly affects construction outcomes. Firms with higher document quality produce fewer RFIs and change orders. [None — company name | Medium]
- **Number of Subcontractors** (`pa-number-subcontra`): Total count of subcontractor firms on the project — a proxy for project complexity. More subs = more coordination overhead, more meetings, more potential conflicts. A 100-sub project is fundamentally different from a 20-sub project. [None — derived from project data | High]
- **Peak Workforce** (`pa-peak-workforce`): Maximum number of workers on site during peak construction — a labor intensity metric. Peak workforce / SF indicates labor density. High peak on a constrained site creates safety and logistics challenges. [OSHA Multi-Employer Worksite Policy | Medium]
- **Self-Performed Work** (`pa-self-performed`): Percentage of work self-performed by the GC (not subcontracted) — affects risk profile and cost structure. Most GCs self-perform 5-15% (general conditions, concrete, carpentry). Trade-specific GCs may self-perform 40-60%. [AGC | None]

**Scope**
- **New vs. Existing** (`pa-new-vs-existing`): Whether the project involves existing structures or is entirely new — renovation content fundamentally changes cost and risk. Existing conditions discovery is the #1 source of changes on renovation projects. [None — industry categories | Low]
- **Occupied During Construction** (`pa-occupied-during`): Whether the building or adjacent spaces are occupied during construction work — adds logistics constraints, safety requirements, work hour restrictions, noise/vibration limits, and security requirements. [OSHA Multi-Employer Worksite | None]
- **Phased Construction** (`pa-phased-const`): Whether the project is built in distinct phases with partial occupancy or turnover between phases. Each phase requires its own punch list, inspections, and turnover. [None — project-specific | None]
- **Fast-Track** (`pa-fast-track`): Whether design and construction overlap — construction starts on early packages (sitework, foundations) while later packages (MEP, interiors) are still being designed. [CII Fast-Track Construction Research | None]
- **Site Constraints** (`pa-site-constraints`): Notable constraints on the construction site — multiple constraints compound and fundamentally change project complexity. [None — project-specific | None]
- **BIM Requirement** (`pa-bim-requirement`): Level of Building Information Modeling required on the project — BIM adoption level correlates with coordination quality and clash detection effectiveness. LOD 300-350 is becoming standard for commercial projects above $25M. LOD 400 for complex MEP. [AIA E203 (BIM Protocol) | None]
- **Modular / Prefab Content** (`pa-modular-prefab`): Percentage of construction using off-site prefabrication or modular methods — shifts labor from field to factory. Reduces on-site workforce peak but requires earlier procurement and more detailed coordination. [Modular Building Institute (MBI) | None]
- **Specialty Systems** (`pa-specialty-system`): Notable specialty building systems that add cost, schedule, and coordination complexity — specialty systems often have proprietary vendors, long lead times, and complex commissioning requirements. [None — type-specific | None]

**Performance**
- **Project Status** (`pa-project-status`): Current state of the project in its lifecycle — determines what data is available and how the project should be treated in benchmarks. Only closed/archived projects have final cost and schedule data. Active projects have in-progress metrics. [PMI PMBOK Project Lifecycle | High]
- **Current Phase** (`pa-current-phase`): Current construction phase based on the phases taxonomy — enables phase-aware analytics and 'where should you be at this point' benchmarks. [None — derived from project activity patterns | Low]
- **Percent Complete** (`pa-percent-complete`): Overall project completion percentage — multiple methods: cost-based (earned value), milestone-based, or units-based. Cost-based is most common for overall project. [PMI PMBOK Earned Value Management | Medium]
- **Earned Value — CPI** (`pa-earned-value-cpi`): Cost Performance Index — the most reliable predictor of final cost performance. Calculation: BCWP (Budgeted Cost of Work Performed) / ACWP (Actual Cost of Work Performed). CPI < 1.0 means over budget. [PMI PMBOK EVM | Low]
- **Earned Value — SPI** (`pa-earned-value-spi`): Schedule Performance Index — measures schedule efficiency. Calculation: BCWP (Budgeted Cost of Work Performed) / BCWS (Budgeted Cost of Work Scheduled). SPI < 1.0 means behind schedule. [PMI PMBOK EVM | Low]

**Standard Measures**
- **Cost Growth** (`pa-cost-growth`): Percentage increase from contract value to final cost at completion — the most important financial performance metric in construction. Calculation: (Final Cost − Contract Value) / Contract Value × 100. [AACE Recommended Practice 10S-90 | Medium]
- **Schedule Growth** (`pa-schedule-growth`): Percentage increase from planned to actual duration — the core schedule performance metric. Calculation: (Actual Duration − Planned Duration) / Planned Duration × 100. Average is 10-20% for well-managed projects. [CII Benchmarking | Medium]
- **Change Order Rate** (`fi-chg-order-rate`): Total approved change order value as percentage of original contract value — measures scope stability and document quality. Calculation: Total CO Value / Original Contract Value × 100. [AACE | High]
- **RFI Density** (`pa-rfi-density`): Number of RFIs per $1M of contract value — measures document quality and design completeness. High RFI density correlates with incomplete documents, aggressive fast-track schedule, or complex design. [CII Document Quality Research | High]
- **Safety Incident Rate (TRIR)** (`pa-safety-incident`): Total Recordable Incident Rate — OSHA-standard safety metric. Calculation: (Total Recordable Incidents × 200,000) / Total Labor Hours Worked. Industry average is 2.5-3.5 for commercial construction. Lower is better. [OSHA 300 Log | Medium]
- **Punch Item Density** (`qsr-punch-item-3`): Number of punch items per 1000 SF at substantial completion — measures overall quality of installed work. High density indicates quality issues during construction. Typical: 2-5 items per 1000 SF for well-managed projects. [None — industry practice | High]
- **Submittal Approval Rate** (`pa-submittal-appr`): Percentage of submittals approved on first submission — measures specification clarity, subcontractor preparation quality, and A/E review efficiency. Calculation: First-Submission Approvals / Total Submittals × 100. [None — industry practice | High]

### Quality & Safety Records

**Observations**
- **Observation** (`qsr-observation`): A documented finding from a site walk or inspection — captures conditions, hazards, deficiencies, or noteworthy items during active construction. The primary during-construction quality and safety signal. [OSHA 29 CFR 1926 (safety) | High]
- **Safety Observation** (`qsr-safety-observati`): An observation with category = 'Safety' — documents hazards, unsafe conditions, and safety compliance findings during site walks. [OSHA 29 CFR 1926 (Construction Safety) | High]
- **Quality Observation** (`qsr-quality-observat`): An observation with category = 'Quality' — documents workmanship deficiencies, material issues, and quality non-conformances during active construction. The strongest during-construction quality signal. [ISO 9001 §8.7 (Control of Nonconforming Outputs) | High]
- **Environmental / Commissioning Observation** (`qsr-enviro-cx`): Observations with category = 'Environmental' or 'Commissioning' — documents environmental compliance findings (erosion control, dust, spills) and commissioning findings (system performance, functional testing results, equipment issues). [EPA NPDES (environmental) | Medium]

**Inspections**
- **Inspection** (`qsr-insp`): A formal structured examination of work against defined criteria — conducted by quality managers, safety officers, third-party inspectors, or regulatory authorities. [ISO 9001 §8.6 (Release of Products) | High]
- **Inspection Item** (`qsr-insp-item`): An individual line item within an inspection checklist — the atomic unit of conformance checking. Key properties: name (item description), status (structured, capitalized: 'Conforming', 'Deficient', 'Not Applicable', 'Uninspected', 'Neutral'). [ISO 9001 checklist requirements | High]
- **Scheduled Inspection** (`qsr-scheduled-insp`): A recurring or planned inspection defined in advance — ensures systematic compliance checking on a regular cadence. Tracks inspection frequency, assigned inspector, and schedule compliance. [OSHA periodic inspection requirements | High]
- **Third-Party / Special Inspection** (`qsr-third-party`): An inspection conducted by an independent testing or inspection agency — required by building codes for structural, fire protection, and other critical systems. [IBC §1704 (Special Inspections) | Medium]

**Punch Items**
- **Punch Item** (`qsr-punch-item`): A documented deficiency or incomplete work item that must be corrected before the owner accepts the project — compiled during substantial completion walkthrough. The strongest closeout quality signal. [AIA A201 §9.8 (Substantial Completion) | High]
- **Punch Item (by Issue Category)** (`qsr-punch-item-issue`): A categorized view of punch items grouped by the 18 validated issue categories derived from keyword clustering on name field. [No industry standard for issue categorization | High]
- **Punch Item Resolution** (`qsr-punch-item-2`): The lifecycle tracking of a punch item from creation to closure — measures how quickly deficiencies are corrected and by whom. Key properties: workflow_status transitions (with timestamps), assignee response, resolution description, verification. [AIA A201 §9.8 | High]

**Incidents**
- **Incident** (`qsr-incident`): A safety event that results in injury, illness, property damage, near-miss, or environmental release — the formal record of what happened. [OSHA 29 CFR 1904 (Recordkeeping) | High]
- **Incident Record** (`qsr-incident-record`): A detailed record within an incident — captures specific injury details, property damage details, or environmental release information. One incident may have multiple records (e.g., two people injured in the same event). [OSHA 29 CFR 1904.7 (General Recording Criteria) | High]
- **Incident Witness Statement** (`qsr-incident-witness`): A documented account from a person who witnessed a safety event — captured as part of the incident investigation. Key properties: witness identity, statement text, date. Witness statements support root cause analysis and regulatory compliance. [OSHA investigation requirements | High]
- **Corrective Action / Incident Action** (`qsr-corrective-actio`): A required remediation or preventive measure assigned in response to an incident or recurring safety observation. Key properties: action description, assignee, due date, status (Open, In Progress, Complete), linked incident or observation. [ISO 45001 §10.2 (Incident Investigation and Corrective Action) | High]

**Formal Notices**
- **Safety Violation** (`qsr-safety-violation`): A specific regulatory violation documented during construction — OSHA citation, code violation, or company safety rule infraction. More formal than a safety observation — a violation implies a specific regulation was breached. [OSHA 29 CFR 1926 (Construction Safety Standards) | Medium]
- **Non-Conformance Report (NCR)** (`qsr-non-conformance`): A formal documented deviation from specifications, drawings, or quality standards — triggers investigation and disposition (accept as-is, rework, reject/replace). [ISO 9001 §8.7 (Control of Nonconforming Outputs) | Medium]
- **Deficiency Notice** (`qsr-deficiency-notic`): A formal written notification to a subcontractor or vendor that their work does not meet contract requirements — triggers contractual obligations to correct. [AIA A201 §12.2 (Correction of Work) | Low]

**Coordination Issues**
- **Coordination Issue** (`qsr-coord-issue`): A design or constructability problem identified during BIM coordination, drawing review, or field coordination — captures clashes, design conflicts, and constructability concerns before they become field problems. [BIM Execution Plan requirements | High]
- **Coordination Issue (Design-Related)** (`qsr-coord-issue-2`): Coordination issues with issue_type in (Design Review, Constructability, Requirement Change) — the subset that signals design quality and completeness problems. [AGC BIMForum | High]

**Test Reports**
- **Material Test Report** (`qsr-mat-test-report`): Results of material testing required by specifications and building codes — concrete cylinder breaks, soil compaction tests, steel mill certifications, fireproofing adhesion tests, waterproofing tests. Conducted by independent testing laboratories. [ASTM test standards (C39 concrete, D1557 soil, E119 fire) | Low]
- **System Performance Test** (`qsr-system-perf-test`): Results of functional testing for building systems — HVAC air balance, electrical load testing, fire alarm testing, plumbing pressure tests, elevator load tests, generator load bank tests. Conducted during commissioning phase. [ASHRAE standards (HVAC) | Low]

**Action Plans**
- **Action Plan** (`qsr-action-plan`): A structured set of tasks created in response to quality or safety findings — groups related corrective actions into a trackable plan with assignees, due dates, and approval workflows. [ISO 9001 §10.1 (Improvement) | High]
- **Action Plan Line Item (Task)** (`qsr-action-plan-line`): An individual task within an action plan — the atomic unit of remediation work. Key properties: description, assignee, due date, status, linked record (the source observation, punch item, or incident that triggered this task). [Follows parent action plan standard/format | High]

**Standard Measures**
- **Observation Density** (`qsr-observation-dens`): Total observations per unit of project size — measures the intensity of quality and safety monitoring. Formula: Total Observations / Project Value (per $M) or Total Observations / Project SF. Can be segmented by category (Quality vs. Safety). [Company-specific safety observation targets | High]
- **Deficiency Rate** (`qsr-deficiency-rate`): Percentage of inspection items found deficient — measures quality conformance. Formula: Deficient Items / Total Inspected Items × 100. Can be segmented by inspection type, building system, and trade. [ISO 9001 quality metrics | High]
- **Punch Item Density** (`qsr-punch-item-3`): Total punch items per unit of project size at substantial completion — measures closeout quality. Formula: Punch Items / Gross SF or Punch Items / Unit Count. Lower density = cleaner handover. [Industry closeout benchmarks | High]
- **Total Recordable Incident Rate (TRIR)** (`qsr-total-recordable`): The number of OSHA-recordable incidents per 200,000 worker hours — the standard safety performance metric in construction. Formula: (Recordable Incidents × 200,000) / Total Worker Hours. [OSHA 29 CFR 1904 | Medium]
- **DART Rate** (`qsr-dart-rate`): Days Away, Restricted, or Transferred rate — incidents per 200,000 hours that result in days away from work, restricted duty, or job transfer. A subset of TRIR that measures more severe incidents. [OSHA 29 CFR 1904 | Medium]
- **Hazard Recurrence Rate** (`qsr-hazard-recurrenc`): Percentage of identified hazards that recur within the same project — measures safety program effectiveness at eliminating root causes. Formula: Recurring Hazards / Total Unique Hazards × 100. [ISO 45001 continual improvement metrics | Medium]
- **Rework Cost Percentage** (`qsr-rework-cost`): Rework-attributable cost as a percentage of total project cost — the financial impact of quality failures. Formula: Rework Cost / Total Project Cost × 100. [CII (Construction Industry Institute) rework benchmarks | Medium]
- **Observation Resolution Time** (`qsr-observation-reso`): Average elapsed time from observation creation to closure — measures how quickly quality and safety findings are addressed. Formula: Closed Date − Created Date (in business days). Can be segmented by category (Quality vs. [Company-specific SLA targets | High]
- **Inspection Pass Rate** (`qsr-insp-pass-rate`): Percentage of inspections that pass on first attempt — measures work quality at the point of formal examination. Formula: Passed Inspections / Total Inspections × 100 (or at item level: Conforming Items / Total Items). [ISO 9001 first-pass yield | High]
- **Near-Miss Ratio** (`qsr-near-miss-ratio`): Ratio of near-miss reports to actual incidents — measures safety culture and proactive reporting. Formula: Near-Miss Count / Incident Count. Higher ratio = better safety culture (more proactive identification). [Heinrich's Safety Triangle | Medium]
- **Corrective Action Closure Rate** (`qsr-corrective-actio-2`): Percentage of corrective actions completed by their due date — measures the effectiveness of the remediation loop. Formula: On-Time Closures / Total Corrective Actions × 100. Tracks whether identified problems actually get fixed. [ISO 45001 §10.2 | High]

### Resources

**General Labor**
- **General Laborer** (`res-laborer`): General construction labor across all project phases — site prep through closeout. Lifecycle: mobilize → work → demobilize. [OSHA 29 CFR 1926 | Medium]
- **Carpenter** (`res-carpenter`): Rough and finish carpentry — one of the most versatile trades on any project. Rough carpenters build formwork, shoring, blocking, backing, and temporary structures during foundations and structural phases. [CSI MasterFormat 06 00 00 | Medium]
- **Concrete Worker** (`res-concrete`): All concrete forming, placing, and finishing — from foundations through elevated slabs. Sub-specialties: concrete finishers (screeding, finishing, curing flatwork), formwork carpenters (construction and stripping), and post-tension specialists (stran... [CSI MasterFormat 03 00 00 | Medium]

**Structural Trades**
- **Ironworker / Steel Erector**: Steel erection and reinforcing — structural steel columns, beams, and deck plus reinforcing bar placement. [CSI MasterFormat 05 00 00 | Medium]
- **Mason** (`res-mason`): All unit masonry — brick, block, and stone. Sub-specialties: bricklayers (face brick, thin brick veneer), block layers (CMU walls, backup walls, elevator shafts), and stone masons (natural and manufactured stone for exterior veneer and interior lobbi... [CSI MasterFormat 04 00 00 | Medium]

**Building Envelope**
- **Roofer** (`res-roofer`): All roofing work — membrane, metal, and built-up systems. Sub-specialties: membrane roofers (TPO, PVC, EPDM, BUR, modified bitumen) and metal roofers/sheet metal workers (standing seam, metal panels, copings, flashing). [CSI MasterFormat 07 50 00 – 07 60 00 | Medium]
- **Glazier / Curtain Wall Installer**: All glass and curtain wall work — unitized and stick-built curtain wall systems, punch windows, storefronts, entrances, and skylights. Highly specialized — usually one sub for the full building envelope scope. [CSI MasterFormat 08 40 00 – 08 80 00 | Medium]
- **Waterproofer** (`res-waterproofer`): Below-grade and above-grade moisture protection — foundation membranes, air/vapor barriers, and joint sealants. [CSI MasterFormat 07 10 00 – 07 92 00 | Medium]

**Interior Finishes**
- **Drywall Hanger / Finisher**: Metal framing and gypsum board — one of the largest interior workforces. Sub-specialties: metal framers (light-gauge steel framing, furring, soffits), drywall hangers (board hanging, specialty boards for moisture/abuse/fire), tapers/finishers (joint ... [CSI MasterFormat 09 20 00 – 09 29 00 | Medium]
- **Painter** (`res-painter`): All painting and coating work — interior and exterior. Sub-specialties: interior painters (walls, ceilings, trim, doors), exterior painters (elastomeric, high-performance coatings), and specialty coatings applicators (epoxy floors, intumescent firepr... [CSI MasterFormat 09 90 00 – 09 97 00 | Medium]
- **Floor Installer** (`res-floor`): All flooring installation — tile, carpet, resilient, hardwood, and specialty. Sub-specialties: tile setters (ceramic, porcelain, natural stone), carpet/resilient installers (carpet, LVT, VCT, sheet vinyl, rubber), and hardwood/specialty floor install... [CSI MasterFormat 09 30 00 – 09 68 00 | Medium]
- **Ceiling Installer** (`res-ceiling`): Ceiling systems — acoustic grid-and-tile and specialty ceilings. Sub-specialties: acoustic ceiling installers (grid, lay-in tile, tegular) and specialty ceiling installers (wood, metal, stretch, linear, cloud ceilings). [CSI MasterFormat 09 50 00 – 09 54 00 | Medium]
- **Insulation Installer** (`res-insulator`): Thermal and acoustic insulation — building envelope and mechanical systems. Sub-specialties: building insulation (batt, rigid, spray foam, blown-in for walls and roof) and mechanical insulation (pipe and duct insulation, jacketing). [CSI MasterFormat 07 21 00 | Low]
- **Fireproofer** (`res-fireproofer`): Fire protection of structural elements and through-penetrations. Sub-specialties: spray fireproofers (SFRM on structural steel — follows steel erection, critical path) and firestoppers (through-penetration and perimeter fire barrier — inspection-crit... [CSI MasterFormat 07 81 00 – 07 84 00 | Medium]

**MEP Trades**
- **Plumber / Pipefitter**: All plumbing and piping — domestic water, waste, vent, gas, and specialty process piping. Sub-specialties: plumbers (domestic water and DWV), steamfitters/HVAC pipefitters (chilled water, hot water, steam, refrigerant), medical gas installers (health... [CSI MasterFormat 22 00 00 | Medium]
- **HVAC / Sheet Metal Worker**: All HVAC ductwork and equipment — fabrication, installation, and commissioning. Sub-specialties: sheet metal workers (duct fabrication and installation), HVAC equipment installers (AHUs, RTUs, chillers, boilers, VRF), test and balance technicians (ai... [CSI MasterFormat 23 00 00 | Medium]
- **Electrician** (`res-electrician`): All electrical work — power distribution, lighting, fire alarm, and site electrical. Sub-specialties: power electricians (service entrance, distribution, branch circuits, devices), lighting electricians (fixture installation, controls, emergency), fi... [CSI MasterFormat 26 00 00 | Medium]
- **Sprinkler Fitter** (`res-sprinkler`): All fire suppression piping — wet, dry, pre-action, deluge, and specialty systems. Sub-specialties: wet system installers (mains, branches, heads for standard wet pipe) and specialty system installers (dry, pre-action, deluge, clean agent, kitchen ho... [CSI MasterFormat 21 00 00 | Medium]
- **Elevator Mechanic** (`res-elevator`): All elevator and vertical transportation work — traction, hydraulic, MRL, escalators, and moving walks. Typically proprietary — one manufacturer's installer per project. Long lead time for equipment. [CSI MasterFormat 14 00 00 | Medium]
- **Low Voltage Technician**: All low voltage and technology systems — data/telecom, security, AV, and fire alarm. Sub-specialties: data/telecom installers (structured cabling, fiber, racks), security installers (cameras, access control, intrusion), AV installers (audio, video, c... [CSI MasterFormat 27 00 00 – 28 00 00 | Medium]

**Site & Support**
- **Equipment Operator** (`res-operator`): Operation of construction equipment — earthmoving, cranes, and material handling. Sub-specialties: heavy equipment operators (excavators, dozers, loaders, graders, scrapers), crane operators (tower and mobile cranes — separately licensed), and forkli... [OSHA 1926 Subpart N/O/CC | Medium]
- **Surveyor / Layout Technician**: Survey and layout — establishing control points, building layout, grade verification, and as-built documentation. Uses total stations, GPS/GNSS, robotic instruments, and increasingly drones for progress documentation. [CSI MasterFormat 01 71 23 | Low]
- **Safety Professional** (`res-safety`): Safety management and compliance — hazard identification, incident investigation, OSHA compliance, and safety training. Typically a full-time role on projects above a threshold size. [OSHA 29 CFR 1926 | High]
- **Quality Control Inspector**: Quality assurance and testing — inspection of installed work, material testing coordination, and punch list management. May be a dedicated role or part of the superintendent's responsibilities. [ASTM testing standards | High]
- **Commissioning Agent** (`res-cxa`): Building systems commissioning — functional performance testing of MEP systems before owner occupancy. Increasingly required by code (IECC, ASHRAE 189.1) and LEED. Independent from installing contractors. [ASHRAE Guideline 0 | Low]

**Cranes**
- **Crane** (`res-crane`): Lifting equipment for vertical construction — tower cranes, mobile cranes, and overhead gantry systems. Tower cranes: hammerhead (fixed jib, high-rise), luffing (variable radius, tight urban sites), and self-erecting (low/mid-rise). [OSHA 1926 Subpart CC | Medium]

**Earthmoving**
- **Earthmoving Equipment**: Excavation, grading, and site preparation equipment. Types: track excavators (primary dig — bulk and detail), mini excavators (confined spaces, utilities), long-reach excavators (deep cuts), wheel loaders (material handling, stockpile), skid steers (... [OSHA 1926 Subpart O | Medium]

**Concrete Equipment**
- **Concrete Equipment**: Concrete placement and finishing equipment — pumps, mixers, vibrators, and saws. Boom pumps (truck-mounted, for elevated pours), line pumps (ground-level, for slabs and foundations), mixer trucks (ready-mix delivery), concrete vibrators (internal con... [ACI 304R | Medium]

**Material Handling**
- **Material Handling Equipment**: Equipment for moving materials on site — forklifts, telehandlers, conveyors, and hoists. Rough terrain forklifts (outdoor material handling), warehouse forklifts (indoor staging), telehandlers (variable-reach telescopic handler — most common material... [OSHA 1926 Subpart N | Medium]

**Access Equipment**
- **Access Equipment** (`res-access`): Equipment for elevated work access — boom lifts, scissor lifts, personnel hoists, and scaffolding. Boom lifts: articulating (around obstacles) and telescopic (maximum reach). [OSHA 1926 Subpart L (Scaffolds) | Medium]

**Compaction**
- **Compaction Equipment**: Soil and base compaction equipment — rollers, plate compactors, and rammers. Vibratory rollers (smooth drum or padfoot for large areas), plate compactors (walk-behind for trench backfill and confined areas), and pneumatic rollers (multi-tire for asph... [ASTM D698 | Low]

**Foundation Equipment**
- **Piling / Foundation Equipment**: Deep foundation equipment — pile drivers, drill rigs, and caisson drills. Impact and vibratory pile drivers (driven piles — steel H, precast concrete), drill rigs/auger equipment (drilled shafts, auger-cast piles), and caisson drills (large-diameter ... [ASTM D1143 | Low]

**Hauling**
- **Hauling Equipment**: Transport equipment — dump trucks, flatbeds, and water trucks. Dump trucks (on/off-site material hauling for earthwork and demo), flatbed trucks (material delivery and transport), and water trucks (dust control, compaction moisture). [DOT weight limits | Low]

**Temporary Utilities**
- **Temporary Utilities** (`res-temp-util`): Temporary site services during construction — power, compressed air, heating, lighting, and dewatering. [OSHA 1926 Subpart K | Medium]

**Welding & Fabrication**
- **Welding / Fabrication Equipment**: On-site welding and cutting equipment — arc welders and cutting tools. Arc welders (SMAW, GMAW, FCAW machines for structural and miscellaneous welding) and cutting equipment (oxy-fuel, plasma, saw cutting for steel modification and demolition). [AWS D1.1 | Low]

**Survey & Layout**
- **Survey / Layout Instruments**: Surveying and layout instruments — total stations, GPS/GNSS, lasers, and drones. Total stations (electronic survey instrument for precise layout), GPS/GNSS equipment (satellite positioning for grading and layout — enables machine guidance), laser lev... [ASCE Manual of Practice 98 | Low]

**Concrete**
- **Concrete** (`mat-concrete`): All cast-in-place and precast concrete — the most common structural material in construction. Types: ready-mix concrete (normal weight, lightweight, high-strength, SCC, fiber-reinforced), precast structural (hollow core plank, double tees, beams, col... [CSI MasterFormat 03 00 00 | Medium]

**Reinforcing**
- **Rebar & Reinforcing**: All concrete reinforcement — deformed bars, welded wire, post-tensioning, and mechanical couplers. Rebar (#3 through #18 deformed bars, epoxy coated), welded wire fabric (WWF/WWR for slabs), post-tensioning (PT strand, anchors, ducts, grout — special... [CSI MasterFormat 03 20 00 | Medium]

**Structural Metals**
- **Structural Steel & Metals**: All structural and miscellaneous steel and metal fabrications. Structural steel (wide flange, HSS, angles, channels, plates), steel deck (composite, non-composite, and roof deck), connection hardware (bolts, welds, base plates, shear studs), miscella... [CSI MasterFormat 05 00 00 | Medium]

**Wood & Composites**
- **Lumber & Wood** (`mat-lumber`): All wood and composite products — dimensional lumber, engineered wood, and sheathing. Dimensional lumber (studs, joists, blocking, plates), engineered wood (LVL, glulam, TJI, CLT, PSL), and sheathing/panels (plywood, OSB, cementitious board). [CSI MasterFormat 06 00 00 – 06 17 00 | Medium]

**Masonry**
- **Masonry** (`mat-masonry`): All unit masonry — CMU, face brick, natural stone, manufactured stone, and accessories. CMU (standard, lightweight, split face, ground face), face brick (modular, queen, king, thin brick), natural stone (limestone, granite, marble, sandstone, slate),... [CSI MasterFormat 04 00 00 | Medium]

**Roofing**
- **Roofing** (`ph-roofing`): All roofing materials — membrane, metal, built-up, and accessories. Single-ply membrane (TPO, PVC, EPDM), built-up/modified bitumen (BUR, SBS, APP), metal roofing (standing seam, corrugated, architectural panels), insulation (polyiso, EPS, XPS, cover... [CSI MasterFormat 07 50 00 – 07 70 00 | Medium]

**Waterproofing & Sealants**
- **Waterproofing & Sealants**: All moisture protection — below-grade waterproofing, air/vapor barriers, sealants, flashing, and expansion joints. [CSI MasterFormat 07 10 00 – 07 95 00 | Medium]

**Thermal & Fire Protection**
- **Thermal & Fire Protection**: Insulation and fireproofing materials — building insulation, spray fireproofing, and firestopping. Building insulation (batt, rigid board, spray foam, blown-in — energy code driven), spray fireproofing (SFRM — cementitious and intumescent on structur... [CSI MasterFormat 07 20 00 – 07 84 00 | Medium]

**Doors Frames & Hardware**
- **Doors Frames & Hardware**: All door assemblies — hollow metal, wood, specialty doors, finish hardware, and overhead doors. Hollow metal doors and frames (steel), wood doors (flush, stile and rail, fire-rated), specialty doors (FRP, aluminum, sliding, folding, acoustic), finish... [CSI MasterFormat 08 10 00 – 08 71 00 | Medium]

**Glass & Glazing**
- **Glass & Glazing** (`mat-glass`): All glass and glazing systems — curtain wall, windows, storefronts, skylights, and insulating glass units. [CSI MasterFormat 08 40 00 – 08 81 00 | Medium]

**Interior Framing & Board**
- **Interior Framing & Gypsum**: Metal framing and gypsum board — the backbone of interior partitions. Metal studs and track (light-gauge steel framing, deflection track, furring), gypsum board (regular, moisture-resistant, fire-rated, abuse-resistant, shaftliner), and plaster/stucc... [CSI MasterFormat 09 20 00 – 09 29 00 | Medium]

**Ceilings**
- **Ceiling Materials** (`mat-ceiling`): All ceiling systems — acoustic grid-and-tile and specialty ceilings. Acoustic ceilings (suspension grid, lay-in tile, tegular) and specialty ceilings (wood, metal, stretch, linear, open cell, cloud ceilings). [CSI MasterFormat 09 50 00 – 09 54 00 | Medium]

**Flooring**
- **Flooring** (`ph-flooring`): All flooring materials — tile, carpet, resilient, hardwood, stone, and resinous/specialty. Ceramic/porcelain tile (floor and wall tile, mosaics), carpet (broadloom, modular tile), resilient flooring (LVT, VCT, sheet vinyl, rubber, linoleum), hardwood... [CSI MasterFormat 09 30 00 – 09 68 00 | Medium]

**Paint & Coatings**
- **Paint & Coatings** (`be-paint`): All painting and coating products — interior paint, exterior coatings, specialty coatings, primers, and wall coverings. [CSI MasterFormat 09 72 00 – 09 97 00 | Medium]

**Specialties**
- **Specialties** (`mat-specialties`): Division 10 specialties — toilet accessories, signage, fire protection specialties, wall/corner protection, and lockers/storage. [CSI MasterFormat 10 00 00 | Medium]

**Casework & Millwork**
- **Casework & Millwork** (`ph-casework`): Cabinets, countertops, trim, and custom millwork. Plastic laminate casework (standard commercial cabinets), wood casework (stain-grade cabinets), countertops (solid surface, quartz, granite, laminate, stainless), and trim/millwork (base, crown, casin... [CSI MasterFormat 06 22 00 – 06 60 00 | Medium]

**Plumbing**
- **Plumbing Materials** (`mat-plumbing`): All plumbing piping, fittings, and fixtures. Pipe: domestic water (copper, PEX, CPVC, stainless), waste/vent (cast iron, PVC, ABS, no-hub), valves and fittings (gate, ball, check, PRV, backflow preventers), and hangers/supports. [CSI MasterFormat 22 00 00 | Medium]

**HVAC Distribution**
- **HVAC Distribution** (`ph-hvac-dist`): All HVAC ductwork, piping, and insulation. Ductwork: sheet metal duct (rectangular, round, oval), flexible duct, duct fittings and accessories (elbows, tees, dampers, turning vanes, access doors), and diffusers/grilles/registers (supply, return, exha... [CSI MasterFormat 23 07 00 – 23 37 00 | Medium]

**HVAC Equipment**
- **HVAC Equipment & Controls**: Major HVAC equipment and building automation controls. Equipment: air handling units (central station AHUs, make-up air), rooftop units (packaged RTUs, DX cooling), split systems/VRF/heat pumps, chillers (air-cooled, water-cooled), cooling towers, bo... [CSI MasterFormat 23 09 00 – 23 81 00 | Medium]

**Electrical Power**
- **Electrical Distribution & Wiring**: Power distribution equipment and wiring systems. Distribution: switchgear, transformers (dry-type, pad-mount), panelboards and breakers, disconnects and switches, motor starters/VFDs, and generators/UPS (permanent standby power). [CSI MasterFormat 26 05 00 – 26 32 00 | Medium]

**Lighting**
- **Lighting** (`be-lighting`): All light fixtures and controls — interior, exterior, emergency, and controls. Interior fixtures (troffers, downlights, pendants, linear, decorative), exterior fixtures (site, facade, parking, landscape lighting), emergency and exit (emergency batter... [CSI MasterFormat 26 50 00 – 26 56 00 | Medium]

**Fire Protection**
- **Fire Protection Systems**: All fire suppression and fire alarm materials — sprinkler pipe, heads, pumps, detection devices, notification devices, and control panels. [CSI MasterFormat 21 00 00 / 28 31 00 | Medium]

**Low Voltage**
- **Low Voltage Systems**: Data/telecom, security, AV, and paging systems. Communications: structured cabling (Cat6, Cat6A, fiber optic), data outlets and patch panels, data racks and enclosures, AV equipment (displays, projectors, speakers, conferencing, control), and paging/... [CSI MasterFormat 27 00 00 – 28 00 00 | Medium]

**Site Materials**
- **Site & Utility Materials**: Sitework and infrastructure materials — soil/fill, utility pipe, manholes, geotextiles, paving, fencing, and landscaping. [CSI MasterFormat 31 00 00 – 33 00 00 | Medium]

**Vertical Transportation**
- **Elevator & Conveying**: All vertical transportation — traction elevators, hydraulic elevators, MRL (machine-room-less) elevators, escalators, moving walks, and cab finishes. [CSI MasterFormat 14 00 00 | Medium]

**Standard Measures**
- **Labor Productivity Rate**: Output per labor hour for a given trade — the fundamental measure of workforce efficiency. Calculation: units installed ÷ total labor hours. Units vary by trade (CY for concrete, SF for drywall, tons for steel). [AACE RP 22R-01 | Medium]
- **Crew Size per Trade**: Average and peak headcount for a specific trade on a project. Calculation: sum of workers reported per trade per day from manpower logs. Tracking over time shows workforce loading curve — early ramp, peak, and demobilization. [OSHA recordkeeping | Medium]
- **Labor Cost per Unit**: Cost of labor per unit of output — combines productivity and wage rate. Calculation: total labor cost for trade ÷ total units installed. Requires cost code breakdown by trade and quantity tracking. [AACE Cost Engineering Terminology | Medium]
- **Equipment Utilization Rate** (`fo-equip-utilizatio`): Percentage of available time that equipment is actively in use. Calculation: active operating hours ÷ total available hours on site. High utilization indicates right-sizing; low utilization suggests oversized fleet or scheduling gaps. [CII Equipment Management | Low]
- **Material Waste Rate**: Percentage of material ordered that is not installed — waste, damage, theft, or over-ordering. Calculation: (quantity ordered − quantity installed) ÷ quantity ordered × 100. Typical rates: 2–5% for steel, 5–10% for concrete, 10–15% for drywall. [WRAP (Waste & Resources Action Programme) | Low]
- **Submittal Turnaround Time**: Days from submittal submission to final approval — a leading indicator of schedule risk. Calculation: approval_date − submission_date for each submittal. [AIA A201 (standard review periods) | High]
- **Trade Count per Project**: Number of distinct trade categories active on a project — a proxy for project complexity. Calculation: count of unique trades from manpower logs. More trades = more coordination overhead. Typical: 15–25 trades on a mid-size commercial project. [CII Complexity Assessment | Medium]
- **Material Delivery On-Time Rate**: Percentage of material deliveries arriving on or before the scheduled date. Calculation: on-time deliveries ÷ total scheduled deliveries × 100. Late deliveries cause trade stacking and schedule compression. [CII Materials Management | Medium]
- **Labor Hours per $1M Project Value**: Total labor hours normalized by project value — an efficiency metric that enables cross-project comparison regardless of size. Calculation: total manpower hours ÷ (project total value ÷ $1M). [CII Benchmarking | Medium]

### Risk

**Risk Framework**
- **Risk** (`rk-risk`): An identified potential event or condition that could affect project objectives — the fundamental unit of risk management. Defined by source (what causes it), trigger (what signals it), consequence (what it affects), and owner (who manages it). [PMI PMBOK Risk Management | None]
- **Risk Register** (`rk-risk-register`): A project-level inventory of all identified risks — the master document that tracks risk identification, assessment, response, and status throughout the project lifecycle. Maintained from preconstruction through closeout. [PMI PMBOK 11.2 | None]
- **Risk Category** (`rk-risk-category`): A classification that groups risks by their source or nature — the organizing principle for a risk register. Categories are typically defined at the company or program level and applied consistently across projects. [PMI PMBOK Risk Breakdown Structure (RBS) | None]
- **Risk Trigger** (`rk-risk-trigger`): An observable condition or event that signals a risk is materializing — the early warning system. Triggers convert abstract risks into actionable alerts. [PMI PMBOK 11.6 (Monitor Risks) | Low]
- **Risk Owner** (`rk-risk-owner`): The person or party responsible for monitoring a risk and executing the response plan — accountability for risk management. [PMI PMBOK 11.5 | None]

**Risk Assessment**
- **Likelihood Assessment** (`rk-likelihood-asses`): The evaluation of probability that a risk event will occur — qualitative (High/Medium/Low) or quantitative (percentage, frequency). [PMI PMBOK 11.3 | None]
- **Impact Assessment** (`rk-impact-assessmen`): The evaluation of consequence severity if a risk materializes — measured across one or more dimensions: cost, schedule, quality, safety, reputation. [PMI PMBOK 11.3 | Low]
- **Risk Score** (`rk-risk-score`): The combined measure of likelihood × impact that determines risk priority — the basis for triage and resource allocation. Typically displayed as a number (1–25 on a 5×5 matrix) or color (red/amber/green). [PMI PMBOK 11.3 | None]
- **Risk Matrix** (`rk-risk-matrix`): A visual grid that plots risks by likelihood (y-axis) and impact (x-axis) — the standard tool for risk prioritization. Typically 3×3 or 5×5 with color-coded zones (green = accept, amber = mitigate, red = escalate). [PMI PMBOK 11.3 | None]

**Risk Response**
- **Risk Response Type** (`rk-risk-response`): The strategic approach to managing an identified risk — the four fundamental options. Each risk in the register should have an assigned response type that determines the nature of the mitigation plan. [PMI PMBOK 11.5 | None]
- **Mitigation Action** (`rk-mitigation-actio`): A specific planned action to reduce the likelihood or impact of an identified risk — the operational response. Mitigation actions have owners, due dates, status, and cost. [PMI PMBOK 11.5 | Low]
- **Contingency Reserve** (`rk-contingency-rese`): A budget allocation held in reserve for identified risks — financial buffer against cost uncertainty. Contingency is typically 3-10% of project cost depending on project complexity and phase (higher in early phases, drawn down as risks are resolved o... [AACE 40R-08 (Contingency Estimating) | Low]
- **Schedule Buffer** (`rk-schedule-buffer`): Time reserves built into the project schedule to absorb schedule risk — the temporal equivalent of contingency reserve. Buffers may be explicit (milestone buffers between phases) or implicit (float in non-critical paths). [AACE 10S-90 | Low]
- **Residual Risk** (`rk-residual-risk`): The remaining risk exposure after mitigation actions are applied — the risk that persists despite response efforts. Residual risk may be accepted, monitored, or require additional response. [PMI PMBOK 11.5 | None]

**Risk Categories**
- **Design Risk** (`rk-design-risk`): Risk arising from incomplete, conflicting, or evolving design — the most common source of change orders in construction. [AIA A201 (design liability) | Medium]
- **Construction Execution Risk** (`rk-const-execution`): Risk from means and methods, productivity, sequencing, and trade coordination — the risk of building it wrong or slow. [OSHA 29 CFR 1926 | Medium]
- **Financial Risk** (`rk-financial-risk`): Risk of cost overruns, cash flow problems, payment disputes, or contractor default — the money risks. Includes budget variance (actual > plan), cash flow gaps (invoices outpacing payments), subcontractor financial health (inability to complete), and ... [AACE 62R-11 | Medium]
- **Schedule Risk** (`rk-schedule-risk`): Risk of delays and timeline overruns from any cause — weather, permits, material delivery, labor shortages, design changes, differing site conditions. [AACE 62R-11 | Medium]
- **Safety Risk** (`rk-safety-risk`): Risk of injuries, fatalities, and safety incidents — the most regulated and consequential risk category. Safety risk is measured by incident rates (TRIR, DART, EMR), managed through hazard identification and mitigation, and regulated by OSHA. [OSHA 29 CFR 1926 | High]
- **Environmental Risk** (`rk-enviro-risk`): Risk from contamination, hazardous materials, spills, weather events, and environmental compliance — both site-condition risk (what's already there) and operational risk (what the project creates). [EPA regulations | Medium]
- **Regulatory and Permit Risk** (`rk-reg-permit-risk`): Risk from permitting delays, code changes, inspection failures, and regulatory enforcement — the risk that authorities block or delay work. [IBC | Low]
- **Supply Chain Risk** (`rk-supply-chain`): Risk from material shortages, delivery delays, price escalation, and sole-source dependencies — the risk that what you need isn't available when you need it. [AACE 62R-11 | Medium]
- **Geotechnical Risk** (`rk-geotechnical-ris`): Risk from unforeseen subsurface conditions — the most unpredictable risk in construction. Includes unexpected soil conditions, groundwater, contamination, underground utilities, and rock. [ASCE 21 (Geotechnical Baseline Reports) | None]
- **Labor Risk** (`rk-labor-risk`): Risk from workforce availability, productivity variance, jurisdictional disputes, and labor relations — the people risk. [Bureau of Labor Statistics | Low]
- **Coordination Risk** (`rk-coord-risk`): Risk from trade interference, design conflicts, and inadequate planning — the risk that parallel workstreams collide. [BIM Execution Plan | Low]

**Risk Transfer & Allocation**
- **Insurance Requirement** (`rk-insurance-requir`): The contractual obligation for project participants to carry specific insurance coverages — the financial backstop for risk transfer. [AIA A201 (insurance provisions) | High]
- **Surety Bond** (`rk-surety-bond`): A three-party guarantee that a contractor will fulfill contractual obligations — bid bonds (guarantee bid price), performance bonds (guarantee completion), and payment bonds (guarantee subcontractor/supplier payment). [Miller Act (federal) | None]
- **Risk Allocation** (`rk-risk-allocation`): The contractual assignment of specific risks to parties — who bears the consequence when a risk materializes. Risk allocation is defined in contract terms and varies by delivery method. [AIA A201 | None]

**Standard Measures**
- **Risk Exposure Value** (`rk-risk-exposure`): Total financial exposure from identified risks — sum of (likelihood × cost impact) across all risks in the register. Provides a single number representing the project's aggregate risk in dollar terms. [AACE 40R-08 | None]
- **Contingency Burn Rate** (`fi-contingency-burn`): Rate at which contingency reserve is consumed over project duration — actual contingency usage divided by elapsed project time. A leading indicator: fast burn early signals cost risk. [AACE 40R-08 | Low]
- **Incident Rate (TRIR)** (`rk-incident-rate`): Total Recordable Incident Rate — the standard OSHA safety metric. Formula: (number of recordable incidents × 200,000) / total hours worked. Measures overall safety risk realization. [OSHA 29 CFR 1904 | High]
- **Risk Mitigation Completion Rate** (`rk-risk-mitigation`): Percentage of planned mitigation actions completed on time — measures the effectiveness of risk response execution. Formula: completed actions / total planned actions. Tracks whether the team is actually doing what they planned to manage risk. [PMI PMBOK 11.6 | Low]
- **Change Order Rate** (`fi-chg-order-rate`): Percentage of original contract value added through change orders — a proxy for scope and design risk realization. Formula: total approved change order value / original contract value. Higher rates indicate more realized risk. [AACE 62R-11 | High]
- **Schedule Float Erosion** (`rk-schedule-float`): Rate at which total float is consumed across the project schedule — a leading indicator of schedule risk. Formula: (baseline total float - current total float) / baseline total float. [AACE 10S-90 | Low]

### Roles

**Project Leadership**
- **Owner's Representative** (`rl-owner-s`): Owner's on-site or dedicated agent who makes decisions on the owner's behalf — design review, scope decisions, change authorization, acceptance of work, dispute resolution, stakeholder management. [CMAA (owner representation standards) | Medium]
- **Project Executive** (`rl-project-executiv`): Senior leader overseeing a project or group of projects for the GC or CM — portfolio oversight, client relationship, risk escalation, financial performance, resource allocation, contract negotiations. [PMI PMP/PgMP | Low]
- **Project Manager** (`rl-project-manager`): Day-to-day leader of the project — owns schedule, budget, and subcontractor management. Consumes daily reports, budget/schedule updates, RFIs, submittals, change events, pay applications. [PMI PMP | High]
- **Assistant Project Manager** (`rl-assistant-projec`): Supports PM with day-to-day management — often assigned specific scope areas or administrative functions. Manages submittal tracking, RFI coordination, subcontract administration, insurance tracking, meeting coordination, document control. [PMI CAPM | Medium]
- **Design Manager** (`rl-design-manager`): Manages the design process and design team coordination for the GC or owner — design review, constructability review, design schedule management, value engineering. Primarily a design-build or CM at Risk role. [AIA (design phase standards) | Low]

**Field Operations**
- **Superintendent** (`rl-super`): Senior field leader responsible for day-to-day construction operations — trade coordination, schedule enforcement, quality oversight, safety enforcement, site logistics, daily reporting. [OSHA 29 CFR 1926 (competent person requirements) | High]
- **Assistant Superintendent** (`rl-assistant-super`): Supports superintendent with field coordination — often assigned to specific building areas or trades. Manages area-specific trade coordination, daily documentation, inspection coordination, material tracking, quality walks. [OSHA 29 CFR 1926 | Medium]
- **Project Engineer** (`rl-project-engineer`): Technical field support — manages engineering and documentation aspects of field work. Drafts RFIs, coordinates submittals, tracks as-builts, reviews shop drawings, tracks quantities, solves technical problems. [PMI | Medium]
- **Field Engineer** (`rl-field-engineer`): Entry-level field position focused on surveying, layout, and construction documentation — concrete placement monitoring, quantity verification, material receiving, photo documentation. Starting point for most construction careers. [OSHA 10/30 (safety training) | Low]
- **Foreman / General Foreman** (`rl-foreman-gen`): Trade-specific field leader who manages a crew of 4-20 workers on a daily basis — daily work assignments, material coordination, quality of installed work, safety compliance, productivity. The link between management and craft workers. [OSHA 29 CFR 1926 (competent person) | Medium]
- **Journeyman / Craft Worker** (`rl-journeyman-craft`): Skilled tradesperson who performs the physical construction work — licensed or certified in their trade. Installs trade-specific work per drawings and specs, maintains quality workmanship, complies with safety procedures. [State licensing (electricians, plumbers) | Medium]
- **Apprentice** (`rl-apprentice`): Trades worker in training — learning under journeyman supervision as part of a formal 3-5 year program. Performs assigned tasks, attends trade school, progresses toward journeyman status. Active during Construction. [DOL (Department of Labor — registered apprenticeship) | Medium]

**Safety & Quality**
- **Safety Manager / Safety Director** (`rl-safety-manager`): Dedicated safety professional responsible for the project's or company's safety program — site inspections, incident investigation, OSHA compliance, safety training, subcontractor safety oversight. [OSHA 29 CFR 1926 | Medium]
- **Safety Officer / Safety Coordinator** (`rl-safety-officer`): Field-level safety personnel conducting daily site safety activities — safety walks, toolbox talks, new worker orientation, PPE compliance, housekeeping inspections, near-miss documentation. Boots-on-the-ground safety presence. [OSHA 29 CFR 1926 | Low]
- **Quality Manager / QC Inspector** (`rl-quality-manager`): Dedicated quality professional responsible for QA/QC across the project — inspection coordination, deficiency tracking, specification compliance, material testing coordination, non-conformance management. [ISO 9001 (quality management) | Medium]

**Preconstruction & Estimating**
- **Estimator / Chief Estimator** (`rl-estimator-chief`): Develops cost estimates from conceptual through detailed pricing — quantity takeoff, unit pricing, subcontractor bid solicitation and leveling, risk pricing, GMP development, value engineering. [AACE CEP (certified estimating professional) | Medium]
- **Preconstruction Manager** (`rl-preconstruction`): Leads the preconstruction effort — coordinates estimating, scheduling, constructability, client presentations, GMP negotiation, value engineering facilitation, risk assessment, subcontractor prequalification. Active during Preconstruction. [CMAA | Low]

**Project Controls**
- **Scheduler / Project Controls Manager** (`rl-scheduler-projec`): Manages the project schedule and schedule-related analytics — schedule development, updates, critical path analysis, delay analysis, resource loading, earned value management, schedule risk assessment. [AACE PSP (planning and scheduling professional) | Medium]
- **Document Controller** (`rl-doc-controller`): Manages the project document management system — document numbering, drawing distribution, revision control, submittal routing, RFI routing, transmittal management, archiving. Active across all phases. [CSI (document management standards) | Medium]
- **Cost Engineer / Cost Analyst** (`rl-cost-engineer`): Tracks and forecasts project costs — cost tracking, forecast updates, change order impact analysis, cash flow projections, earned value analysis, budget variance reporting. More common on large projects ($50M+). [AACE CCE (certified cost engineer) | Medium]

**BIM & Technology**
- **BIM Manager / VDC Coordinator** (`rl-bim-manager-vdc`): Manages the building information model and virtual design and construction processes — BIM execution plan, model management, clash detection, trade coordination, 4D scheduling, quantity extraction, reality capture management. [AIA E203 (BIM protocol) | Medium]
- **Technology Manager** (`rl-tech-manager`): Manages project technology infrastructure — software deployment, mobile device management, network infrastructure, system integration, data management, user training. Increasingly important as construction becomes more technology-dependent. [CompTIA | Low]

**Procurement & Contracts**
- **Procurement Manager** (`rl-procure-manager`): Manages the procurement process from bid solicitation through contract execution — bid package development, bid solicitation, bid leveling, scope review, contract negotiation, insurance and bonding verification. [ISM (Institute for Supply Management) | Medium]
- **Contract Administrator** (`rl-contract-adminis`): Manages contract compliance and commercial processes after execution — change order processing, pay application review, lien waiver collection, insurance certificate tracking, retainage management. Active from Construction through Closeout. [AIA A201 (contract administration) | Medium]

**Commissioning & Startup**
- **Commissioning Agent (CxA)** (`rl-cx-agent-cxa`): Independent professional who verifies building systems perform as designed — commissioning plan development, pre-functional testing, functional performance testing, deficiency tracking, seasonal testing, final report. [ASHRAE Guideline 0 | Low]
- **TAB Technician** (`rl-tab-technician`): Testing, Adjusting, and Balancing technician who measures and adjusts air and water flow rates to design values — air system balancing, hydronic balancing, sound and vibration measurement. [AABC (certification) | None]

**Office & Administrative**
- **Office Manager / Project Admin** (`rl-office-manager`): Manages the project office and administrative operations — office operations, filing, correspondence management, meeting scheduling, visitor management, event coordination. Active across all phases. [No specific industry standard — general office management | Low]
- **Accountant / Financial Analyst** (`rl-accountant-finan`): Manages project financial transactions and reporting — invoice processing, pay application processing, job cost tracking, financial reporting, audit support, tax compliance. Company-level role supporting multiple projects. Active across all phases. [AICPA | Medium]

**Standard Measures**
- **Staffing Ratio** (`rl-staffing-ratio`): Ratio of management staff (PM, super, PE, APM) to project value or subcontractor count — indicates project resourcing adequacy. Calculated as management headcount / project value band or management headcount / active subcontractor count. [PMI PMBOK (resource management) | High]
- **Role Coverage Rate** (`rl-role-coverage`): Percentage of key project roles filled at any point in the project timeline — filled roles / required roles × 100. Tracks gaps in project team staffing that create risk. [PMI PMBOK | High]
- **PM Workload Index** (`rl-pm-workload`): Number of active projects per project manager — indicates workload balance and risk of attention dilution. Calculated from PM role assignments across the active project portfolio. [PMI (resource management) | High]
- **Superintendent Span of Control** (`rl-super-span`): Number of active subcontractors and direct reports managed by a single superintendent — indicates field coordination burden. Calculated from active vendor count and crew headcount per superintendent. [AGC (field management staffing) | High]
- **Safety Staffing Ratio** (`rl-safety-staffing`): Ratio of dedicated safety personnel to total workforce — safety staff headcount / peak daily workforce × 100. Indicates safety program investment and correlates with incident rates. [OSHA recommendations | Medium]

### Schedule

**Activity Structure**
- **Detail Activity** (`sch-detail-activity`): The lowest-level schedulable work item — has its own duration, logic ties, resources, and cost assignment. The fundamental unit of CPM scheduling. Typical duration 5-20 working days; activities exceeding 20 days indicate insufficient detail. [AACE 10S-90 | High]
- **Summary Activity & WBS** (`sch-summary-activity`): Roll-up activity that aggregates child activities into a single bar — no independent duration or resources. Used for Work Breakdown Structure nodes, phase summaries, and area roll-ups. [AACE 10S-90 | Medium]
- **Milestone** (`sch-milestone`): Zero-duration marker representing a key event — start milestone or finish milestone. Contractual milestones carry liquidated damages. [AACE 10S-90 | High]
- **Activity Identification** (`sch-activity-identif`): The naming and coding conventions that make activities findable, filterable, and analyzable. Activity ID follows a coding convention encoding phase/area/trade (e.g., A1000, 03-EL-0100). [AACE 10S-90 | High]
- **Duration & Progress** (`sch-duration-progres`): The time dimension of an activity — original duration (planned at baseline), remaining duration (days left from data date), actual start/finish dates, and percent complete. [AACE 10S-90 | High]
- **Activity Codes** (`sch-activity-codes`): Classification codes assigned to activities for grouping, filtering, sorting, and reporting — the dimensional analysis framework for schedule data. [AACE 10S-90 | Medium]

**Logic & Dependencies**
- **Relationship Type** (`sch-relationship-typ`): The logical connection between two activities that drives the CPM calculation. Four types: Finish-to-Start (FS, most common, ~80-90% of ties), Start-to-Start (SS, overlapping work), Finish-to-Finish (FF, activities ending together), Start-to-Finish (... [AACE 10S-90 | High]
- **Lag & Lead Time** (`sch-lag-lead-time`): Time offset on a logical relationship — positive lag represents waiting time (concrete cure 7-28 days, submittal review 14-21 days, coating dry 1-3 days). Negative lag (lead) represents overlap — many specifications prohibit entirely. [AACE 10S-90 | High]
- **Dependency Classification** (`sch-dependency-class`): Categorization of why two activities are linked — determines which relationships can change during delay analysis. Mandatory (hard logic): physical or contractual requirement (foundation before structure). [AACE 10S-90 | Low]
- **Open Ends** (`sch-open-ends`): Activities missing predecessors (open start) or successors (open finish) — logic gaps that distort CPM calculations. Only the project start and finish milestones should have open ends. Open starts can begin on the data date regardless of logic. [AACE 10S-90 | Medium]
- **Logic Density & Redundancy** (`sch-logic-density`): Schedule connectedness measured by relationship-to-activity ratio. Logic density healthy range: 1.5-2.5 relationships per activity. Below 1.2 means loosely connected (CPM unreliable). Above 3.0 may indicate over-constraining. [AACE 10S-90 | Medium]

**Time Management**
- **Work Calendar** (`sch-work-calendar`): Definition of working days and hours that drives duration-to-date conversion in the CPM. Standard 5-day (Mon-Fri, default), 6-day (adds Saturday, +17% capacity), 7-day (continuous — for cure time and critical path compression), weather-adjusted (anti... [AACE 10S-90 | Medium]
- **Schedule Constraint** (`sch-schedule-constra`): Date override on an activity that restricts CPM calculation — from permissive (ASAP, the default) to absolute (Must Start/Finish On). Every non-default constraint should have documented justification. [AACE 10S-90 | Medium]
- **Calculated Dates** (`sch-calculated-dates`): Dates produced by the CPM forward and backward pass calculations. Early Start/Early Finish: earliest possible dates from forward pass through logic and calendars. Late Start/Late Finish: latest dates from backward pass without delaying the project. [AACE 10S-90 | Medium]
- **Data Date** (`sch-data-date`): The status date of the schedule update — divides past from future. All progress is recorded as-of the data date. Activities with actual start after the data date or remaining work before it are out-of-sequence. [AACE 10S-90 | Medium]
- **Baseline Dates** (`sch-baseline-dates`): The approved planned dates from the baseline schedule — the 'as-planned' reference against which all performance is measured. Original baseline (BL0) is the contractual reference submitted 30-90 days after NTP. [AACE 10S-90 | Medium]

**Schedule Analysis**
- **Float / Slack** (`sch-float-slack`): Calendar days an activity can be delayed without downstream or project-level impact. Total Float: delay without delaying project completion (LF-EF). Free Float: delay without delaying any immediate successor. [AACE 10S-90 | High]
- **Critical Path** (`sch-critical-path`): The longest continuous chain of activities and relationships determining minimum project duration — zero or least total float. Typically 10-15% of activities are critical on a well-built schedule. [AACE 10S-90 | High]
- **Path Analysis Methods** (`sch-path-analysis`): Advanced techniques for tracing schedule logic beyond simple total float. Longest Path: traces driving relationships backward from project finish — more reliable than TF=0 when constraints distort float. [AACE 10S-90 | Low]
- **Earned Schedule** (`sch-earned-schedule`): Time-based earned value method — measures schedule performance in time units instead of cost units. ES = the time at which current earned value should have been achieved per baseline. SPI(t) = ES / Actual Time. [AACE recommended practice | Low]

**Schedule Lifecycle**
- **Baseline Schedule** (`sch-baseline-schedul`): The approved planned schedule against which all performance is measured — the contractual 'as-planned' reference. Original Baseline (BL0) submitted 30-90 days after NTP per typical specifications with 2-4 review cycles. [AACE 10S-90 | Medium]
- **Schedule Update** (`sch-schedule-update`): The periodic progress recording and schedule recalculation cycle — the primary schedule management process. Monthly standard (bi-weekly on fast-track). [AACE 10S-90 | Medium]
- **Look-Ahead Schedule** (`sch-look-ahead`): Rolling short-term schedule showing daily/weekly detail for the next 3-6 weeks — the superintendent's primary planning tool. Three-week: daily detail for crew assignments, material deliveries, inspections. [Common practice | High]
- **Recovery Schedule** (`sch-recovery-schedul`): Plan to recover lost time and return to the contractual completion date after a delay. Required when negative float exceeds a contract threshold (often 10-20 days). [AACE 10S-90 | Low]
- **As-Built Schedule** (`sch-as-built`): Final schedule reflecting actual dates for all activities — the factual record of how construction actually progressed. All activities have actual start and actual finish with no remaining duration. [AACE 10S-90 | Low]

**Resource & Cost Loading**
- **Labor Loading** (`sch-labor-loading`): Trade-specific labor hours assigned to schedule activities — drives manpower histograms, workforce planning, and crew optimization. Shows when each trade peaks and valleys over the project. [AACE 10S-90 | Medium]
- **Equipment Loading** (`sch-equip-loading`): Major equipment utilization assigned to schedule activities — identifies mobilization timing, utilization gaps, and equipment-driven constraints. Tower crane is the most impactful — crane time allocation drives structural and enclosure sequences. [AACE 10S-90 | Medium]
- **Cost Loading & Cash Flow** (`sch-cost-loading`): Dollar values distributed across schedule activities for earned value measurement and cash flow projection. Activity cost = labor + material + equipment + subcontract. Produces the S-curve (cumulative planned vs. [AACE 10S-90 | Low]
- **Resource Leveling** (`sch-resource-levelin`): Adjusting activity timing within available float to smooth resource demand — avoid peaks and valleys without extending the project. [AACE 10S-90 | None]

**Delay & Claims**
- **Delay Classification** (`sch-delay-class`): Categorization of delays by cause and remedy — determines entitlement to time extension and/or compensation. Excusable Compensable: owner-caused, time + money (design errors, late owner items). [AACE 29R-03 | Medium]
- **Time Impact Analysis** (`sch-time-impact`): The gold standard prospective delay analysis method — inserts a fragnet (delay event network of 3-20 activities) into the updated schedule at the time of impact and compares before/after CPM results. [AACE 29R-03 | Low]
- **Retrospective Delay Analysis** (`sch-retrospective-de`): After-the-fact methods comparing planned vs. actual schedules. As-Planned vs. As-Built: simplest, compares BL0 to actual dates, shows variance but not causation. [AACE 29R-03 | Low]
- **Time Extension Request** (`sch-time-extension`): Formal written request for additional contract time due to an excusable delay event. Must be submitted within the contract notice period (typically 7-21 days). [Contract specifications | Medium]
- **Acceleration** (`sch-acceleration`): Direction (explicit or constructive) to complete work faster than the adjusted contractual schedule. Explicit: written owner directive with cost reimbursement. [AACE | Low]

**Schedule Quality**
- **DCMA 14-Point Assessment** (`sch-dcma-14-point`): Defense Contract Management Agency schedule assessment framework — 14 checks covering logic, durations, float, constraints, relationships, resources, and critical path. [DCMA 14-Point Assessment | Medium]
- **Specification Compliance** (`sch-specification-co`): Contract-specific schedule requirements that must be met for baseline approval and ongoing updates. Activity duration limits (typically 15-20 working day max), relationship type ratios (FS >80-90%), calendar assignment rules (cure on 7-day, work on 5... [Contract specifications | Medium]
- **Critical Path Length Index** (`sch-critical-path-2`): (Critical path remaining duration + total float) / critical path remaining duration — a single-number predictor of schedule outcome. CPLI > 1.0: buffer exists. CPLI = 1.0: no buffer. CPLI < 1.0: project will finish late without recovery. [DCMA 14-Point Assessment (check #13) | Medium]

**Schedule Integration**
- **Schedule Levels** (`sch-schedule-levels`): The hierarchy of schedule detail — from executive summary to daily work plan. Master/Summary: 50-200 activities, phase milestones, the owner's view. [AACE 10S-90 | High]
- **CPM Tool Integration** (`sch-cpm-tool`): Importing the detailed schedule from the authoring tool (P6, MS Project, Asta) into the project management platform. The schedule is authored externally and consumed broadly. Import via XER/XML/MPP format. [Common practice | High]
- **Schedule-to-Field Linkage** (`sch-schedule-field`): Connecting CPM activities to field data — daily logs, inspections, RFIs — to validate progress and identify discrepancies between planned and actual execution. The gap between CPM and field reality is the central problem in construction scheduling. [Emerging best practice | High]
- **Schedule Change Tracking** (`sch-schedule-chg`): Timestamped record of every change to every schedule activity — capturing old values, new values, author, timestamp, and reason. Critical evidence in delay disputes: who changed what and when. Change frequency per activity identifies unstable areas. [AACE 10S-90 (change documentation) | High]

**Lean & Alternative**
- **Last Planner System** (`sch-last-planner`): Collaborative scheduling methodology where the people doing the work make reliable promises. Pull Planning: trades work backward from milestones to identify handoffs and constraints. [Lean Construction Institute (LCI) | Medium]
- **Takt Time Planning** (`sch-takt-time`): Fixed-rhythm scheduling where each trade moves through zones at the same pace — manufacturing flow applied to construction. Takt time = available time / number of zones. All trades match the same rhythm. [Lean Construction Institute | Low]
- **Linear Scheduling** (`sch-linear-schedulin`): Scheduling methods for repetitive or linear work where location is the primary axis. Line of Balance (LOB): graphical method showing production rate across identical units — each trade plotted as a line with slope = production rate. [AACE | None]
- **4D/5D BIM Scheduling** (`sch-4d-5d-bim`): Linking 3D BIM model elements to CPM schedule activities for visual construction sequence simulation (4D) and adding cost data for time-phased cost visualization (5D). Animation shows construction progression over time. [AACE | Low]

**Standard Measures**
- **Schedule Performance Index** (`sch-schedule-perf`): Earned value / planned value — the primary schedule efficiency metric. Traditional SPI = EV/PV (cost-based, converges to 1.0 at project end, masking late delivery). Earned Schedule SPI(t) = ES/AT (time-based, remains accurate throughout). [PMI PMBOK | Low]
- **Baseline Execution Index** (`sch-baseline-executi`): Activities completed on or before baseline finish date / total activities completed in the period — measures execution discipline. Simpler and more intuitive than SPI. [AACE recommended practice | Medium]
- **Float Erosion Rate** (`sch-float-erosion`): Rate of total float decrease across schedule updates — reveals whether the schedule is tightening faster than planned work completion. Calculation: average TF change per update period or % of activities losing float period-over-period. [AACE 10S-90 | Medium]
- **Milestone Adherence Rate** (`sch-milestone-adhere`): Milestones completed on or before their baseline date / total milestones due to date — a high-level schedule health KPI. Focuses on key events rather than all activities. More meaningful to owners and executives than SPI or float analysis. [Custom metric | Medium]
- **Critical Activity Ratio** (`sch-critical-activit`): Percentage of remaining activities that are critical (TF ≤ 0) — measures how much of the schedule is at risk of delay. Calculation: critical activities / total remaining activities. [AACE 10S-90 | High]
- **Percent Plan Complete** (`sch-percent-plan`): Percentage of weekly commitments completed as planned — the core lean scheduling metric from the Last Planner System. Calculation: PPC = tasks completed as committed / tasks committed. Measures workflow reliability, not schedule progress. [Lean Construction Institute | High]
- **Out-of-Sequence Rate** (`sch-out-sequence`): Activities with progress that violates their logical predecessors / total in-progress activities — indicates schedule-to-field alignment. Calculation: out-of-sequence activities / total in-progress. [AACE 10S-90 | Low]
- **Schedule Health Score** (`sch-schedule-health`): Composite metric aggregating multiple quality indicators into a single score — typically based on DCMA 14-Point Assessment. Each check is binary pass/fail; total pass count produces the health score. [DCMA 14-Point Assessment | Medium]

### Standards & Classifications

**Cost & Work Classifications**
- **MasterFormat** (`sc-masterformat`): The 50-division classification system published by CSI/CSC that organizes construction costs and specifications by type of work. The single most important standard for cross-company financial data comparison. [CSI MasterFormat 2018 (50 divisions) | High]
- **Specification Section** (`sc-specification-se`): A numbered section within a project's technical specifications organized by MasterFormat — defines quality standards, materials, methods, and acceptance criteria for a specific scope of work. [CSI MasterFormat (section numbering) | Medium]
- **Standard Cost Code List** (`sc-std-cost-code`): A company-standard or industry-standard template of cost codes used to set up new projects — ensures consistency across an organization's project portfolio. Companies may maintain multiple lists for different project types. [Company-specific | High]
- **WBS Code Structure** (`sc-wbs-code`): Work Breakdown Structure code templates that provide a second dimension of cost classification beyond cost codes — segments costs by phase, location, category, or other company-defined dimension. [PMI PMBOK WBS (§5.4) | Medium]
- **Budget Code Structure** (`sc-budget-code`): Company-specific grouping codes applied to budget line items for executive reporting — distinct from cost codes (transactional) and WBS codes (segmentation). [Company-specific | Medium]

**Building & Element Classifications**
- **UniFormat** (`sc-uniformat`): A building element classification system that organizes construction by functional systems rather than by product type — the complement to MasterFormat. [ASTM E1557 (UniFormat) | Low]
- **OmniClass** (`sc-omniclass`): A comprehensive classification system covering ALL construction entities — buildings, spaces, elements, products, phases, disciplines, and more. [ASTM E2271 (OmniClass) | None]
- **IFC Classification (buildingSMART)** (`sc-ifc-class`): Industry Foundation Classes — an open data standard for BIM that defines entity types, properties, and relationships for all building elements. [ISO 16739 (IFC) | None]

**Safety & Hazard Classifications**
- **OSHA Hazard Categories** (`sc-osha-hazard`): Standardized safety hazard types defined by OSHA for construction — the Focus Four hazards (Fall, Struck By, Electrical, Caught In/Between) plus additional categories. [OSHA 29 CFR 1926 (Construction Safety Standards) | High]
- **OSHA Recordkeeping Classification** (`sc-osha-recordkeepi`): The OSHA system for classifying workplace injuries and illnesses by severity — determines which incidents are 'recordable' and drive TRIR and DART rate calculations. [OSHA 29 CFR 1904 (Recording and Reporting) | Medium]
- **ANSI Injury Classification** (`sc-ansi-injury`): The ANSI/BLS system for classifying injuries by nature (laceration, fracture, sprain), body part (hand, back, knee), and cause (fall, struck by, overexertion) — provides detailed injury taxonomy for pattern analysis. [ANSI Z16.1 (Injury Classification) | Medium]

**Building Codes & Regulatory**
- **International Building Code (IBC)** (`sc-international-bu`): The model building code adopted (with local amendments) by most US jurisdictions — governs structural design, fire safety, egress, accessibility, and building system requirements. [ICC International Building Code (IBC 2021, 2024) | Low]
- **NFPA Standards** (`sc-nfpa-stds`): National Fire Protection Association standards governing fire protection, life safety, and electrical systems — the technical basis for fire code requirements. [NFPA 13 (Sprinkler Systems), NFPA 72 (Fire Alarm), NFPA 101 (Life Safety Code),  | Low]
- **ADA / Accessibility Standards** (`sc-ada-accessibilit`): Americans with Disabilities Act Accessibility Guidelines (ADAAG) and ICC A117.1 — govern accessible design requirements for public and commercial buildings. [ADA/ADAAG (federal) | Low]
- **Energy Code Standards** (`sc-energy-code-stds`): Energy conservation codes (IECC, ASHRAE 90.1) and above-code programs — govern building envelope performance, HVAC efficiency, lighting power density, and renewable energy requirements. [IECC (International Energy Conservation Code) | Low]

**Sustainability & Certification**
- **LEED Certification** (`sc-leed-certificati`): Leadership in Energy and Environmental Design — the most widely recognized green building certification system. [USGBC LEED v4.1 (BD+C, ID+C, O+M) | Low]
- **WELL Building Standard** (`sc-well-building`): A performance-based standard focused on occupant health and wellness — covers air, water, nourishment, light, fitness, comfort, and mind. Less common than LEED but growing rapidly, especially in commercial office and healthcare. [IWBI WELL Building Standard v2 | None]
- **Resilience & Net Zero Standards** (`sc-resilience-net`): Emerging standards for climate resilience (RELi, FORTIFIED) and net-zero energy/carbon performance — increasingly required by institutional owners and government agencies. Resilience standards address flood, wind, seismic, and wildfire hazards. [RELi 2.0 (Resilience) | None]

**Contract & Delivery Standards**
- **AIA Contract Documents** (`sc-aia-contract`): The American Institute of Architects standard contract document series — the most widely used contract forms in US construction. [AIA A101, A201, A401, B101 (Owner-Architect), G-series (G701, G702, G703, G704,  | Low]
- **Delivery Method Classification** (`sc-dlvy-method`): The taxonomy of project delivery methods that determines how design, construction, and risk are allocated between parties. Each delivery method creates different document flows, change order patterns, and financial instrument relationships. [AIA delivery method documents (A-series) | Low]
- **AACE Cost Engineering Standards** (`sc-aace-cost`): The Association for the Advancement of Cost Engineering recommended practices — define cost estimating, scheduling, and project controls methodologies. Key standards: 18R-97 (Cost Estimate Classification), 10S-90 (Cost Engineering), EVMS practices. [AACE International Recommended Practices: 18R-97 (Estimate Classification), 10S- | Low]

**Standard Measures**
- **Cost Code Standardization Rate** (`sc-cost-code`): Percentage of a company's projects using a consistent standard cost code list — measures data readiness for cross-project benchmarking. Formula: Projects with Standard Cost Codes / Total Projects × 100. [Company-specific quality target | High]
- **MasterFormat Mapping Coverage** (`sc-masterformat-map`): Percentage of a company's cost codes that map to recognized MasterFormat divisions — measures the degree to which company codes can be normalized for cross-company comparison. [CSI MasterFormat mapping conventions | Medium]
- **Specification Section Coverage** (`sc-specification-se-2`): Percentage of project specification sections entered as structured data vs. remaining as PDF uploads — measures the quality of specification cross-referencing for submittals and RFIs. [CSI section count norms by project type | Medium]
- **Safety Classification Completeness** (`sc-safety-class`): Percentage of safety observations with a structured hazard_name classification — measures the quality of safety data for OSHA hazard analysis. Formula: Observations with hazard_name / Total Safety Observations × 100. [OSHA hazard category standards | High]
- **WBS Adoption Rate** (`sc-wbs-adoption`): Percentage of projects or companies using WBS codes for cost segmentation — measures the depth of financial data granularity available for building-element-level benchmarking. Formula: Projects with WBS Codes / Total Financial Projects × 100. [PMI WBS methodology adoption | Medium]
- **Certification Adoption Rate** (`sc-certification-ad`): Percentage of projects pursuing third-party certification (LEED, WELL, FORTIFIED, etc.) — measures the market penetration of green building and performance standards. Formula: Certified or Pursuing Projects / Total Projects × 100. [USGBC adoption reports | Low]

### Workflows & Statuses

**Universal Lifecycle Statuses**
- **Open** (`ws-open`): Record is active and available for action — the entry point for most construction records. Indicates the item has been created and is part of the active workflow. Every record type has some version of 'open' as its initial actionable state. [PMI PMBOK | High]
- **In Progress** (`ws-progress`): Work has begun on the record but is not yet complete. Indicates active effort by a responsible party — distinguishes items being worked on from those sitting idle. Common on tasks, action plans, inspections, and punch items. [PMI PMBOK | High]
- **Draft** (`ws-draft`): Record exists but has not been formally issued into the workflow. Editable, not yet visible to reviewers or counterparties. The pre-submission holding state where the creator refines before committing. [AIA A201 (document submission protocols) | High]
- **Closed** (`ws-closed`): Record has completed its lifecycle — no further action required. Terminal state indicating the workflow has run its course, whether resolved successfully or not. Distinct from Void (cancelled) and Approved (decision). [PMI PMBOK | High]
- **Void** (`ws-void`): Record has been invalidated or cancelled — the work was never completed, just abandoned. Distinct from Closed (completed lifecycle). Voided records should be excluded from most metrics but tracked as a signal of rework or process waste. [AACE 10S-90 (cost engineering terminology) | High]
- **On Hold** (`ws-hold`): Record is paused, awaiting external input, owner decision, or other blocking condition. Not cancelled — expected to resume. Common when waiting for design clarification, material delivery, or client direction. [PMI PMBOK (risk response: accept) | Medium]
- **Overdue** (`ws-overdue`): Record has passed its due date without reaching its expected next state. A computed status based on comparing due_date to current_date and record status. Indicates workflow stall requiring attention. [PMI PMBOK (schedule variance) | High]

**Approval & Review Statuses**
- **Pending** (`ws-pending`): Awaiting action from the next responsible party. The record has entered the workflow but the reviewer has not yet begun evaluation. Pre-action holding state that starts the response time clock. [AIA A201 (submittal review) | High]
- **Submitted** (`ws-submitted`): Formally sent to the reviewer or approver — the official handoff point. Clock starts on contractual response time. The creator has completed their work and is waiting for a decision. [AIA A201 (submittal procedures) | High]
- **Under Review** (`ws-under-review`): Actively being evaluated by the responsible party. Between submitted and decision. Some systems track this explicitly, others infer it from ball-in-court assignment. [AIA A201 | Medium]
- **Approved** (`ws-approved`): Accepted without conditions — authorizes the associated work, cost, or material to proceed. The positive terminal decision in an approval workflow. On financial records, triggers commitment of funds. [AIA A201 | High]
- **Approved as Noted** (`ws-approved-as`): Accepted with conditions, corrections, or minor modifications. Common on submittals — fabrication may proceed but noted changes must be incorporated. The 'yes, but' decision that avoids full rejection. [AIA A201 (submittal review actions) | High]
- **Rejected** (`ws-rejected`): Not accepted — requires rework before resubmission. A hard stop that sends the record back to the originator. Resets the workflow cycle. Should always include rejection reason for tracking. [AIA A201 | High]
- **Revise and Resubmit** (`ws-revise-resubmit`): Similar to rejected but with specific revision guidance — the reviewer has identified what needs to change. Softer than rejection, implies the approach is correct but execution needs refinement. Common on submittals. [AIA A201 (submittal actions) | High]

**Field Disposition Statuses**
- **Ready for Review** (`ws-ready-review`): Field work is complete and awaiting quality inspection, superintendent sign-off, or third-party verification. The handoff point between field crews and quality/management teams. [ISO 19650 (information handover) | Medium]
- **Conforming** (`ws-conforming`): Inspection item meets the specified requirements — pass disposition. The field evaluator has verified the work complies with plans, specs, or standards. Moves the item toward closure. [ISO 9001 (conformity assessment) | High]
- **Deficient** (`ws-deficient`): Inspection item fails to meet requirements — requires corrective action. A formal finding that the installed work does not comply with plans, specifications, or applicable codes. Triggers rework cycle. [ISO 9001 | High]
- **Not Applicable** (`ws-not-applicable`): Record or inspection item does not apply in this context — excluded from evaluation. Used when an inspection checklist item is irrelevant to the specific work being inspected. [ISO 9001 (scope exclusion) | High]

**Workflow Components**
- **Workflow Step** (`ws-workflow-step`): An individual stage in a multi-step approval or review process. Defines who must act, what action is required, and the sequence position. The atomic unit of workflow configuration. [PMI PMBOK (process groups) | Medium]
- **Approval Chain** (`ws-appr-chain`): Ordered sequence of reviewers and approvers that a record must pass through before reaching a terminal state. Defines the review hierarchy, required vs. optional reviewers, and fallback rules. [AIA A201 (submittal review requirements) | Medium]
- **Ball in Court** (`ws-ball-court`): The party currently responsible for taking the next action on a record. Construction-specific accountability term — at any moment, someone 'has the ball'. Changes as the record moves through workflow steps. [AGC (project management practices) | High]
- **Distribution List** (`ws-dist-list`): Set of parties notified when a record is created, changes status, or receives a response. Ensures relevant stakeholders stay informed without being in the approval chain. Notification, not action. [AIA A201 (distribution requirements) | High]
- **Workflow Response** (`ws-workflow-respons`): A reviewer's formal action at a workflow step — approve, reject, forward, return, or comment. The decision record that advances (or returns) the workflow. Timestamped for cycle time calculation. [PMI | Medium]
- **Due Date** (`ws-due-date`): The date by which action must be completed on a record or workflow step. Contractually significant — missed due dates can trigger liquidated damages, delay claims, or escalation. [AIA A201 (response time requirements) | High]
- **Response Time** (`ws-response-time`): The elapsed time between submission and response — either the contractual allowance or the actual measured duration. Critical for project pacing — slow responses cascade into schedule delays. [AIA A201 (14-day default) | Medium]
- **Escalation** (`ws-escalation`): Elevation of a stalled workflow item to a higher authority when the responsible party fails to act within the allowed response time. The safety valve for stuck workflows. [PMI PMBOK (issue escalation) | None]
- **Delegation** (`ws-delegation`): Temporary or permanent transfer of approval authority from one party to another. Required when the primary reviewer is unavailable — prevents workflow stalls during vacations, role changes, or emergencies. [PMI PMBOK | None]

**Workflow Patterns**
- **Sequential Approval** (`ws-sequential-appr`): Approvers review in a defined order — each must act before the next receives the item. Ensures layered review (PM → Architect → Owner). Most formal and slowest pattern. [AIA A201 (review sequence) | Medium]
- **Parallel Review** (`ws-parallel-review`): Multiple reviewers evaluate simultaneously — all must respond before the workflow advances. Faster than sequential but requires all parties to be available. Common on design submittals with multiple discipline reviewers. [AIA A201 (simultaneous review) | Medium]
- **Submit and Approve** (`ws-submit-approve`): Single submission followed by one or more approval decisions. The simplest and most common construction workflow pattern — the creator sends, the reviewer decides. [AIA A201 | High]
- **Review and Respond** (`ws-review-respond`): A question or information request requiring a formal written response. The RFI pattern — question asked, answer provided, response becomes part of the project record. Response may have cost/schedule impact. [AIA A201 (RFI procedures) | High]
- **Inspect and Disposition** (`ws-inspect-disposit`): Field evaluation of installed work against defined criteria, resulting in a conforming/deficient judgment. The quality assurance pattern — inspector walks the work, checks each item, renders a disposition. [ISO 9001 | High]
- **Create and Close** (`ws-create-close`): Simplest lifecycle: an item is created, worked on, and closed. No formal approval chain — the responsible party resolves and closes. The punch list and field finding pattern. [AIA A201 (punch list procedures) | High]
- **Multi-Stage Financial Review** (`ws-multi-stage`): A change progresses through independent budget, cost, and revenue stages — each with its own approval status. The change management pattern where a single event triggers parallel financial workflows across different ledgers. [AACE 10S-90 | High]

**Financial Workflow Stages**
- **Budget Stage** (`ws-budget-stage`): The budget approval phase of a change event — tracks whether the budget impact has been formally recognized and approved. First stage in the three-stage financial workflow. Controls whether the project budget is adjusted. [AACE 10S-90 | High]
- **Cost Stage** (`ws-cost-stage`): The cost commitment phase of a change — tracks whether costs have been formally committed to subcontractors or vendors via change orders. Second stage. Controls whether the commitment is updated. [AACE 10S-90 | High]
- **Revenue Stage** (`ws-revenue-stage`): The owner billing phase of a change — tracks whether the approved change has been incorporated into owner invoicing. Third and final stage. Controls whether the GC bills the owner for the change. [AACE 10S-90 | High]
- **Change Event Lifecycle** (`ws-chg-event`): The end-to-end progression of a change from identification through budget recognition, cost commitment, and revenue billing. The composite view across all three financial stages for a single change event. [AACE 10S-90 | High]
- **Mapped Status** (`ws-mapped-status`): A standardized status field that normalizes domain-specific statuses into a common vocabulary for cross-record comparison. Allows consistent filtering and aggregation across record types that use different status taxonomies. [Internal normalization (not an industry standard) | Medium]

**Electronic Signature Workflows**
- **E-Signature Request** (`ws-e-signature-req`): A digital signing request sent through an integrated e-signature platform (e.g., DocuSign). Overlays the standard approval workflow — the record's internal status and the e-signature status track independently. [ESIGN Act | Medium]
- **E-Signature Ball in Court** (`ws-e-signature-ball`): The signer currently expected to act on a digital signature request. Mirrors the construction ball-in-court concept within the e-signature workflow — identifies who is holding up execution. [ESIGN Act | Medium]

**Standard Measures**
- **Average Approval Cycle Time** (`ws-average-appr`): Mean elapsed time from formal submission to final approval decision. The primary workflow efficiency metric. Formula: AVG(approval_date - submitted_date) in business days. Segment by record type, reviewer, and project phase. [PMI PMBOK (schedule performance) | High]
- **Overdue Rate** (`ws-overdue-rate`): Percentage of records that exceed their due date before reaching the expected next state. Formula: COUNT(overdue_records) / COUNT(records_with_due_dates). Segment by record type and responsible party. [PMI PMBOK (schedule variance) | High]
- **First-Pass Approval Rate** (`ws-first-pass-appr`): Percentage of submissions approved on first review without requiring revision or resubmission. Formula: COUNT(approved_first_pass) / COUNT(total_submissions). Higher rate = better pre-submission quality. [ISO 9001 (first-pass yield) | Medium]
- **Resubmission Rate** (`ws-resubmission-rat`): Percentage of submissions that are rejected or returned for revision before eventual approval. Formula: COUNT(rejected_or_returned) / COUNT(total_submissions). The inverse complement of first-pass approval. [ISO 9001 | Medium]
- **Ball-in-Court Aging** (`ws-ball-court-aging`): Average time a record sits with the current responsible party before action is taken. Formula: AVG(current_date - bic_assignment_date) for active records. Identifies the slowest link in the workflow chain. [PMI PMBOK | High]
- **Status Dwell Time** (`ws-status-dwell`): Average time a record spends in each status before transitioning to the next state. Identifies which statuses are bottlenecks in the workflow. Formula: AVG(next_status_date - current_status_date) per status. [PMI PMBOK (process efficiency) | Medium]
- **Workflow Completion Rate** (`ws-workflow-complet`): Percentage of records that reach a terminal state (Closed, Approved, Complete) vs. remaining active or stalled. Formula: COUNT(terminal_status) / COUNT(total_created) over a time period. [PMI PMBOK (project closure) | High]
- **Escalation Rate** (`ws-escalation-rate`): Percentage of workflow items that require elevation to a higher authority because the assigned party failed to act within the allowed time. Formula: COUNT(escalated) / COUNT(total_actionable). Higher rate = more workflow friction. [PMI PMBOK (issue escalation) | None]

## Domain Relationships

How domains connect to each other — the primary relationships, bridge elements, and connection strength.

- **Financial Instruments → Documents & Communications** [Dense]: ORIGINATED_FROM, REFERENCES
  - Bridge: RFI→CE (origin_type = 'Rfi::Header'), Drawing→Submittal (spec_section)
  - RFIs generate 307K origin-linked CEs. Strongest document-to-financial bridge.
- **Financial Instruments → Quality & Safety Records** [Moderate]: ORIGINATED_FROM, COSTS_AGAINST
  - Bridge: Observation→CE (origin_type = 'Observations::Item'), Punch Item→Rework Cost (inferred chain), NCR→Backcharge
  - Observations are leading indicators (28-day lead on CEs). 20,238 observation-originated CEs across 727 cos.
- **Financial Instruments → Building Elements** [Dense]: MAPS_TO, CLASSIFIED_AS, COSTS_AGAINST
  - Bridge: Cost Code→MasterFormat Division→Building System, WBS Code→Element-level cost, CE/CCO Line Items→wbs_code_id
  - MasterFormat cost codes are the primary financial-to-physical mapping. wbs_code_id on line items enables element-level cost attribution.
- **Financial Instruments → Organizations** [Dense]: CONTRACTED_TO, COMMITTED_TO
  - Bridge: Commitment→Vendor (vendor_id), CCO→Vendor (via commitment)
  - Every commitment links to a vendor. Vendor performance measured via CO rate, invoice timing, and quality records.
- **Financial Instruments → Schedule** [Moderate]: DEPENDS_ON, IMPACTS
  - Bridge: Schedule Activity→Cost Loading, CE schedule_impact flag, Delay→Cost Impact
  - Schedule delays trigger cost changes. Cost-loaded schedules enable earned value. Cash flow tied to billing cycle.
- **Financial Instruments → Standards & Classifications** [Dense]: MAPS_TO, CLASSIFIED_AS
  - Bridge: Cost Code→MasterFormat Division, Budget Code→UniFormat Category, change_reason→structured enum
  - MasterFormat is the Rosetta Stone for cross-company cost normalization. change_reason is the primary CE/CCO categorization.
- **Financial Instruments → Field Operations** [Moderate]: TRIGGERED_BY, COSTS_AGAINST
  - Bridge: Daily Log Delay→Cost Impact, T&M Ticket→Direct Cost, Manpower→Labor Cost
  - Daily log delays trigger cost events. T&M entries become direct costs. Manpower hours feed cost tracking.
- **Financial Instruments → Contracts & Procurement** [Dense]: COMMITTED_TO, BUDGETED_FOR
  - Bridge: Commitment (Subcontract/PO)→Budget Line Items, Bid→Award→Commitment
  - Financial Instruments tracks money flow; Contracts & Procurement tracks commercial process. Subcontract/PO instruments shared.
- **Financial Instruments → Phases** [Moderate]: PRECEDES, DEPENDS_ON
  - Bridge: Billing cycle→Phase milestones, Retainage→Substantial Completion, Contingency→Construction phase
  - Contingency burned during construction. Retainage released at substantial/final completion. Billing follows phase milestones.
- **Financial Instruments → Risk** [Moderate]: IMPACTS, MITIGATED_BY, EXPOSES_TO
  - Bridge: Contingency→Risk Reserve, CE change_reason→Risk Category, CO Rate→Risk Indicator
  - Contingency burn rate is a leading financial risk indicator. Change order rate decomposed by change_reason reveals risk sources.
- **Financial Instruments → Locations** [Sparse]: LOCATED_AT, COSTS_AGAINST
  - Bridge: WBS Code→Location segment, Budget Line Item→Location allocation
  - WBS codes can segment cost by location. Not all companies use location-based WBS.
- **Financial Instruments → Roles** [Moderate]: MANAGED_BY, APPROVED_AS
  - Bridge: Cost Engineer→Budget, PM→Change Orders, Accountant→Invoices
  - Financial workflows require specific role approvals. Cost engineer, PM, and accounting roles drive financial process.
- **Quality & Safety Records → Documents & Communications** [Dense]: REFERENCES, ATTACHED_TO, LINKED_TO
  - Bridge: Observation→Drawing Reference, Punch Item→Photo, Inspection→Spec Section, Coordination Issue→RFI (rfi_header_id)
  - Photos attached to observations/punch items. Coordination issues link to RFIs (4,967 linked). Inspections reference spec sections.
- **Quality & Safety Records → Building Elements** [Moderate]: MAPS_TO, LOCATED_AT
  - Bridge: Observation.name→18 Issue Categories→Building System, Punch Item.name→18 Categories, Inspection Item→System
  - Keyword clustering on observation.name and punch_item.name maps to building systems. 12,556 unique cos in dual-signal model.
- **Quality & Safety Records → Organizations** [Dense]: ASSIGNED_TO, PERFORMED_BY, INSPECTED_BY
  - Bridge: Observation→vendor_id (80%), Punch Item→vendor_id, Inspection→responsible_contractor_id (48%)
  - Vendor assignment on observations and punch items enables trade-level quality attribution.
- **Quality & Safety Records → Field Operations** [Moderate]: DOCUMENTS, TRIGGERED_BY
  - Bridge: Daily Log Safety Violation→Safety Obs (conceptual), Accident Log→Incident, Daily Log Inspection→Inspection
  - Daily log entries feed formal quality/safety records. Safety violations and accidents link conceptually to incidents.
- **Quality & Safety Records → Standards & Classifications** [Dense]: COMPLIES_WITH, VIOLATES, CLASSIFIED_AS
  - Bridge: Observation→OSHA Hazard Category (hazard_name), Inspection→IBC/OSHA standard, NCR→Spec Section deviation
  - OSHA hazard categories are structured on safety observations. Inspections verify code compliance.
- **Quality & Safety Records → Locations** [Moderate]: LOCATED_AT
  - Bridge: Observation→location_id, Punch Item→location_id, Inspection→location
  - Location tracking on observations, punch items, and inspections enables spatial quality analysis.
- **Quality & Safety Records → Roles** [Moderate]: ASSIGNED_TO, INSPECTED_BY, MANAGED_BY
  - Bridge: Safety Manager→Safety Obs, QC Inspector→Inspections, PM→Punch Items
  - Safety managers drive safety observations. QC inspectors conduct inspections. PMs manage punch list closure.
- **Quality & Safety Records → Phases** [Moderate]: PRECEDES, DEPENDS_ON
  - Bridge: Observation→Construction phase, Punch Item→Closeout, Inspection→Pre-cover/Pre-pour gates
  - Observations peak during construction. Punch items concentrate in closeout. Inspections gate phase transitions.
- **Quality & Safety Records → Risk** [Dense]: EXPOSES_TO, LEADS, IMPACTS
  - Bridge: Safety Observation→Safety Risk, Quality Deficiency→Rework Risk, Hazard Recurrence→Systemic Risk
  - Quality/safety records are primary risk signals. Validated in insights #1, #4, #11.
- **Quality & Safety Records → Models & BIM** [Sparse]: LINKED_TO, ORIGINATED_FROM
  - Bridge: Coordination Issue→BIM Clash, Observation→Model Element (conceptual)
  - Coordination issues originate from BIM clash detection. Observations can reference model elements but linkage is weak.
- **Quality & Safety Records → Contracts & Procurement** [Sparse]: VIOLATES, COSTS_AGAINST
  - Bridge: Deficiency Notice→Contract cure provisions, NCR→Specification deviation, Backcharge→Subcontract
  - Deficiency notices invoke contractual cure provisions. NCRs trace to spec sections. Backcharges deduct from subcontracts.
- **Documents & Communications → Building Elements** [Dense]: REFERENCES, GOVERNS, SPECIFIES
  - Bridge: Drawing→Building System (discipline), Spec Section→MasterFormat Division→System, RFI predicted_topic→System
  - RFI predicted_topic (176 topics) maps directly to building systems. Spec sections organized by MasterFormat. Drawings organized by discipline.
- **Documents & Communications → Organizations** [Dense]: ASSIGNED_TO, RESPONDS_TO, DESIGNED_BY
  - Bridge: RFI→Architect/Engineer (assignee), Submittal→Reviewer, Correspondence→Parties
  - RFIs assigned to design team. Submittals routed through approval chains. Correspondence tracks inter-party communication.
- **Documents & Communications → Schedule** [Moderate]: REFERENCES, IMPACTS, PRECEDES
  - Bridge: RFI schedule_impact flag, Submittal→Procurement→Schedule, Drawing Revision→Schedule Activity
  - Overdue RFIs and submittals delay schedule activities. Drawing revisions may trigger schedule changes.
- **Documents & Communications → Field Operations** [Dense]: DOCUMENTS, ATTACHED_TO
  - Bridge: Daily Log Note→Field narrative, Photo→Observations/Daily Logs, Plan Revision→Drawing Receipt
  - Daily logs document field activity. Photos attach to nearly all field records. Plan revisions track drawing distribution.
- **Documents & Communications → Standards & Classifications** [Moderate]: REFERENCES, GOVERNS
  - Bridge: Spec Section→MasterFormat/ASTM, Drawing→NCS Standards, RFI→Code Reference
  - Spec sections reference MasterFormat and ASTM standards. Drawings follow NCS conventions.
- **Documents & Communications → Phases** [Moderate]: PRECEDES, DEPENDS_ON
  - Bridge: Addendum→Bidding, Shop Drawing→Fabrication, As-Built→Closeout, O&M Manual→Handover
  - Document types are phase-gated: addenda in preconstruction, shop drawings in procurement, as-builts in closeout.
- **Documents & Communications → Locations** [Sparse]: REFERENCES, LOCATED_AT
  - Bridge: Drawing Sheet→Location (floor/zone), Photo→location_id, Site Instruction→Work Area
  - Drawings reference locations by sheet content. Photos can be geotagged to locations.
- **Documents & Communications → Roles** [Moderate]: ASSIGNED_TO, MANAGED_BY
  - Bridge: RFI→Ball-in-Court (role), Submittal→Reviewer, Document Controller→Distribution
  - Ball-in-court tracking identifies responsible role. Document controller manages distribution.
- **Documents & Communications → Permits & Regulatory** [Moderate]: DOCUMENTS, DEPENDS_ON
  - Bridge: Permit Application→Drawings/Specs, COI→Vendor Insurance, Lien Waiver→Payment
  - Permit applications reference design documents. COIs and lien waivers are regulatory compliance documents.
- **Documents & Communications → Contracts & Procurement** [Dense]: REFERENCES, GOVERNS
  - Bridge: Contract→Drawings/Specs (contract docs), Bid Package→Drawings, Submittal→Spec Section
  - Design documents are part of the contract. Bid packages reference drawings and specs.
- **Documents & Communications → Models & BIM** [Moderate]: REPRESENTS, REFERENCES
  - Bridge: Drawing Sheet→2D from 3D Model, Coordination Issue→RFI (rfi_header_id), Shop Drawing→Model Element
  - Drawing sheets generated from BIM models. Coordination issues link to RFIs for resolution.
- **Documents & Communications → Risk** [Moderate]: IMPACTS, TRIGGERED_BY
  - Bridge: Late RFI→Schedule/Cost Risk, Drawing Revision Post-IFC→Change Risk, Overdue Submittal→Material Risk
  - Late documents are leading risk indicators. Post-IFC revisions signal design instability.
- **Standards & Classifications → Building Elements** [Dense]: MAPS_TO, CLASSIFIED_AS
  - Bridge: MasterFormat Division→Building System, UniFormat Category→Element, OmniClass→Entity
  - MasterFormat is the primary financial-to-physical bridge. UniFormat provides systems-level classification.
- **Standards & Classifications → Organizations** [Moderate]: COMPLIES_WITH, CLASSIFIED_AS
  - Bridge: OSHA→Safety Authority, IBC→Building Department, ADA→Accessibility requirements
  - Organizations comply with standards from regulatory authorities. Classification by role type.
- **Standards & Classifications → Permits & Regulatory** [Dense]: GOVERNS, COMPLIES_WITH
  - Bridge: IBC→Building Permit requirements, NFPA→Fire Marshal review, OSHA→Safety plan
  - Building codes govern permit requirements. Fire codes govern fire marshal review. OSHA governs safety compliance.
- **Standards & Classifications → Resources** [Moderate]: SPECIFIES, CLASSIFIED_AS
  - Bridge: Spec Section→Material requirements, MasterFormat→Trade classification
  - Specifications define material and installation requirements. MasterFormat divisions align with trade scopes.
- **Standards & Classifications → Models & BIM** [Moderate]: MAPS_TO, CLASSIFIED_AS
  - Bridge: IFC Classification→BIM Entity, LOD Specification→Model Completeness
  - IFC standards classify BIM entities. LOD specification defines model element maturity.
- **Standards & Classifications → Contracts & Procurement** [Moderate]: GOVERNS, REFERENCES
  - Bridge: AIA Contracts→Standard forms, Spec Sections→Scope definition
  - AIA standards govern contract forms. Spec sections define procurement scope.
- **Organizations → Roles** [Dense]: PLAYS_ROLE, BELONGS_TO
  - Bridge: Company→PM Role, Vendor→Trade Role, GC→Superintendent
  - Organizations employ people who play specific roles on projects. Same company, different roles across projects.
- **Organizations → Building Elements** [Moderate]: PERFORMED_BY, CONTRACTED_TO
  - Bridge: Subcontractor→Building System scope (via commitment), Trade→Element installation
  - Subcontractors are contracted for specific building system scopes. Vendor→commitment→cost code→system chain.
- **Organizations → Contracts & Procurement** [Dense]: CONTRACTED_TO, BONDED_BY
  - Bridge: Vendor→Subcontract, Surety→Bond, Insurance→COI
  - Organizations are the parties to contracts. Surety and insurance companies provide financial backing.
- **Organizations → Locations** [Sparse]: LOCATED_AT, ALLOCATED_TO
  - Bridge: Crew→Work Zone, Vendor→Project Site
  - Organizations are allocated to work zones on site. Less structured in Procore.
- **Organizations → Permits & Regulatory** [Moderate]: ISSUED_BY, COMPLIES_WITH
  - Bridge: Building Department→Permit, Fire Marshal→Review, OSHA→Citation
  - Regulatory authorities issue permits and citations. Contractors comply with regulatory requirements.
- **Roles → Schedule** [Moderate]: MANAGED_BY, ALLOCATED_TO
  - Bridge: Scheduler→Schedule Management, Superintendent→Field Coordination, PM→Progress Tracking
  - Roles drive schedule management. Scheduler maintains CPM, superintendent coordinates field work.
- **Roles → Field Operations** [Dense]: PERFORMED_BY, MANAGED_BY
  - Bridge: Superintendent→Daily Log, Safety Manager→Safety Violations, Foreman→Crew Management
  - Field operations are role-driven. Superintendent owns the daily log. Safety manager owns safety program.
- **Locations → Building Elements** [Dense]: CONTAINS, LOCATED_AT
  - Bridge: Floor/Level→MEP Systems, Zone→Interiors, Room→Fixtures
  - Building elements are installed at specific locations. Location hierarchy mirrors building decomposition.
- **Locations → Field Operations** [Moderate]: LOCATED_AT
  - Bridge: Daily Log→location context, Equipment→Work Area, Crew→Zone Assignment
  - Field operations happen at specific locations. Daily log entries can reference work areas.
- **Locations → Schedule** [Moderate]: LOCATED_AT, DEPENDS_ON
  - Bridge: Schedule Activity→Location, Work Zone→Sequence, Floor→Vertical progression
  - Schedule activities linked to locations enable 4D visualization. Vertical construction progresses floor by floor.
- **Locations → Models & BIM** [Moderate]: REPRESENTS, LOCATED_AT
  - Bridge: BIM Model→Spatial decomposition, Point Cloud→As-Built Location
  - BIM models represent spatial layout. Point clouds capture actual positions.
- **Phases → Schedule** [Dense]: CONTAINS, PRECEDES
  - Bridge: Phase→Summary Activities, Phase Gate→Milestone, Phase Duration→Schedule Segment
  - Phases contain schedule activities. Phase transitions are schedule milestones.
- **Phases → Workflows & Statuses** [Dense]: PRECEDES, DEPENDS_ON
  - Bridge: Phase Gate→Status Transition, Approval Chain→Phase-specific workflows
  - Workflow patterns are phase-specific. Financial approval chains differ from field workflows.
- **Phases → Building Elements** [Dense]: PRECEDES, CONCURRENT_WITH
  - Bridge: Structure phase→Structural Frame, Enclosure phase→Exterior, MEP phase→All MEP systems
  - Each construction phase activates specific building systems. Phase×System matrix defines this.
- **Phases → Resources** [Dense]: REQUIRES, ALLOCATED_TO
  - Bridge: Phase→Trade mobilization, Phase→Equipment deployment, Phase→Material procurement
  - Resource requirements vary by phase. System-resource matrix crossed with phase-system matrix.
- **Phases → Contracts & Procurement** [Moderate]: PRECEDES, DEPENDS_ON
  - Bridge: Bidding→Award (Preconstruction), Fabrication→Installation (Procurement), Closeout→Warranty
  - Procurement activities are phase-gated. Contract milestones align with phase transitions.
- **Phases → Permits & Regulatory** [Moderate]: DEPENDS_ON, PRECEDES
  - Bridge: Building Permit→Construction start, Inspections→Phase gates, CO→Occupancy
  - Permits gate construction start. Inspections gate phase transitions. CO enables occupancy.
- **Workflows & Statuses → Documents & Communications** [Dense]: RESOLVES_TO, APPROVED_AS
  - Bridge: RFI workflow, Submittal approval chain, Correspondence response chain, Lien waiver exchange
  - Workflows drive document processing. RFI lifecycle, submittal approval, invoice processing all follow defined workflows.
- **Workflows & Statuses → Financial Instruments** [Dense]: APPROVED_AS, RESOLVES_TO
  - Bridge: CE→Approved, CCO→Approved (96.7%), Pay App→Approved, Budget Mod→Posted
  - Financial instruments follow approval workflows. CE/CCO/Invoice/Budget Mod all have structured status progressions.
- **Workflows & Statuses → Quality & Safety Records** [Dense]: RESOLVES_TO, APPROVED_AS
  - Bridge: Observation→Closed, Punch Item→Closed, Incident→Closed, Inspection→Complete
  - Quality/safety records follow resolution workflows. Open→In Progress→Ready for Review→Closed.
- **Risk → Schedule** [Dense]: IMPACTS, TRIGGERED_BY
  - Bridge: Schedule Risk→Delay, Float Erosion→Risk Indicator, Critical Path→Risk Concentration
  - Schedule risk is one of the highest-impact risk categories. Float erosion is a leading indicator.
- **Risk → Contracts & Procurement** [Moderate]: MITIGATED_BY, EXPOSES_TO
  - Bridge: Surety Bond→Performance Risk, Insurance→Liability Risk, Contract Terms→Risk Allocation
  - Contracts allocate risk between parties. Bonds and insurance transfer risk to third parties.
- **Risk → Resources** [Moderate]: EXPOSES_TO, TRIGGERED_BY
  - Bridge: Labor Shortage→Schedule Risk, Single-Source Material→Supply Risk, Equipment Failure→Delay Risk
  - Resource constraints create risk exposure. Material shortages validated as structured signal (84K delay records).
- **Risk → Permits & Regulatory** [Moderate]: TRIGGERED_BY, IMPACTS
  - Bridge: Permit Delay→Schedule Risk, Code Violation→Regulatory Risk, Environmental Non-compliance→Fine Risk
  - Permit and regulatory issues trigger risk events. Non-compliance carries financial penalties.
- **Models & BIM → Building Elements** [Dense]: REPRESENTS, CLASHES_WITH
  - Bridge: BIM Model Element→Physical Element, Federated Model→System Coordination
  - BIM models represent building elements digitally. Clash detection finds spatial conflicts between systems.
- **Models & BIM → Schedule** [Moderate]: LINKED_TO, REPRESENTS
  - Bridge: 4D Model→Schedule Activity, 5D Model→Cost-loaded Schedule
  - 4D models link BIM to schedule for visualization. 5D adds cost dimension.
- **Models & BIM → Resources** [Moderate]: SPECIFIES, CONSUMES
  - Bridge: Quantity Takeoff→Material Quantities, Model→Bill of Materials
  - BIM enables quantity takeoff for material procurement. Model-based estimating.
- **Models & BIM → Locations** [Moderate]: REPRESENTS, CONTAINS
  - Bridge: BIM Model→Spatial Layout, Coordination Model→Floor/Zone breakdown
  - BIM models inherently contain spatial information. Model space maps to physical locations.
- **Contracts & Procurement → Resources** [Moderate]: SPECIFIES, COMMITTED_TO
  - Bridge: Subcontract→Trade scope, PO→Material, Insurance→Risk transfer
  - Contracts commit specific trade and material resources. POs procure materials.
- **Contracts & Procurement → Permits & Regulatory** [Sparse]: COMPLIES_WITH, DEPENDS_ON
  - Bridge: Prevailing Wage→Labor compliance, Bonding→Permit requirement, DBE→Diversity compliance
  - Contract compliance requirements include prevailing wage, bonding, and diversity goals.
- **Field Operations → Schedule** [Dense]: LINKED_TO, DOCUMENTS
  - Bridge: Daily Log Scheduled Work→schedule_task_id (FK), Delay Log→Schedule Impact, Manpower→Resource Loading
  - Procore's daily_log_scheduled_work_task links field data to CPM schedule. Unique capability — no P6 equivalent.
- **Field Operations → Building Elements** [Moderate]: MAPS_TO, LOCATED_AT
  - Bridge: Manpower trade_name→Trade→Building System, Equipment→System being served, Delivery→Material→System
  - Trade names on manpower logs map to building systems. Equipment usage indicates active systems.
- **Field Operations → Resources** [Dense]: DOCUMENTS, CONSUMES
  - Bridge: Manpower Log→Trade hours, Equipment Log→Equipment hours, Delivery Log→Material receipts
  - Field operations document actual resource consumption. Manpower, equipment, and delivery logs track trades, equipment, and materials.
- **Field Operations → Locations** [Sparse]: LOCATED_AT
  - Bridge: Work area→Location, Equipment→Location, Crew→Zone
  - Field operations happen at specific locations. Less structured than expected in current data.
- **Field Operations → Organizations** [Moderate]: PERFORMED_BY, MANAGED_BY
  - Bridge: Vendor→Manpower/Equipment entries, GC→Daily Log compilation
  - Vendors appear on daily log entries via vendor_name/vendor_id. GC compiles daily logs.
- **Field Operations → Phases** [Moderate]: DOCUMENTS
  - Bridge: Daily Log→Construction progress by phase, Delay Log→Phase-specific delays
  - Daily logs track progress within each construction phase.
- **Field Operations → Permits & Regulatory** [Sparse]: DOCUMENTS, COMPLIES_WITH
  - Bridge: Daily Log Safety→OSHA compliance, Weather Log→Environmental compliance
  - Safety violation logs and environmental logs support regulatory compliance documentation.
- **Resources → Building Elements** [Dense]: REQUIRES, CONSUMES, PERFORMED_BY
  - Bridge: Trade→Building System (system-resource matrix), Material→Element, Equipment→System served
  - System-resource matrix defines which trades, equipment, and materials each building system requires.
- **Resources → Locations** [Sparse]: ALLOCATED_TO, LOCATED_AT
  - Bridge: Crew→Zone, Equipment→Work Area, Material→Laydown/Staging
  - Resources allocated to specific locations during construction.
- **Project Attributes → Financial Instruments** [Dense]: SEGMENTED_BY, BENCHMARKED_AGAINST
  - Bridge: Project Type→Cost benchmarks, Value Band→Budget norms, Delivery Method→CO rate comparison
  - Project attributes are the primary segmentation dimensions for financial benchmarking.
- **Project Attributes → Quality & Safety Records** [Dense]: SEGMENTED_BY, BENCHMARKED_AGAINST
  - Bridge: Project Type→Defect patterns (3D hot sheet), Value Band→Safety metrics
  - 7 project types validated for quality/safety benchmarking with 99+ cos each.
- **Project Attributes → Schedule** [Moderate]: SEGMENTED_BY, BENCHMARKED_AGAINST
  - Bridge: Project Type→Duration norms, Complexity→Schedule risk, Delivery Method→Schedule approach
  - Project attributes drive schedule benchmarking dimensions.
- **Project Attributes → Building Elements** [Moderate]: CLASSIFIED_AS, CONTAINS
  - Bridge: Project Type→Expected systems, Building Area/Stories→Scope definition
  - Project type determines which building systems are relevant. Building attributes define scope.
- **Project Attributes → Organizations** [Moderate]: CLASSIFIED_AS, MANAGED_BY
  - Bridge: Owner Type→Owner organization, GC/CM→Contractor, Sub Count→Team size
  - Project attributes classify the organizational structure. Owner type, GC, and sub count.
- **Project Attributes → Risk** [Moderate]: EXPOSES_TO, SEGMENTED_BY
  - Bridge: Project Complexity→Risk Level, Fast-Track→Schedule Risk, Site Constraints→Execution Risk
  - Project attributes define inherent risk profiles. Complexity, delivery method, and constraints drive risk.
- **Project Attributes → Locations** [Moderate]: LOCATED_AT
  - Bridge: Address/City/State/Country→Geographic location, Climate Zone→Weather risk, Seismic Category→Structural requirements
  - Project attributes include geographic and environmental classification.
- **Project Attributes → Resources** [Sparse]: REQUIRES
  - Bridge: Peak Workforce→Labor demand, Construction Type→Material requirements, Area/Stories→Equipment needs
  - Project scale attributes indicate resource requirements.
- **Building Elements → Resources** [Dense]: REQUIRES, COMPOSED_OF
  - Bridge: System→Primary Trade, System→Materials, System→Equipment (system-resource matrix)
  - System-resource matrix defines which trades, equipment, and materials each building system requires.
- **Building Elements → Locations** [Dense]: LOCATED_AT, ADJACENT_TO
  - Bridge: System→Floor/Level, Element→Zone/Room, MEP routing→Ceiling Plenum
  - Building elements exist at specific locations. Spatial decomposition mirrors system hierarchy.
- **Building Elements → Standards & Classifications** [Dense]: CLASSIFIED_AS, MAPS_TO
  - Bridge: System→MasterFormat Division, Element→UniFormat Category, System→OmniClass
  - Building elements classified by industry standards. MasterFormat and UniFormat are the primary schemes.
- **Building Elements → Models & BIM** [Dense]: REPRESENTED_BY, CLASHES_WITH
  - Bridge: Physical Element→BIM Model Element, System conflict→Clash Detection
  - Every physical building element has a digital BIM representation. Clashes detected between systems.
- **Schedule → Financial Instruments** [Moderate]: COSTS_AGAINST, BUDGETED_FOR
  - Bridge: Activity→Cost Loading, Schedule Milestone→Billing Cycle, Float Erosion→Budget Risk
  - Cost-loaded schedules map activities to budget lines for earned value. Billing tied to schedule milestones.
- **Schedule → Field Operations** [Dense]: LINKED_TO, DOCUMENTS
  - Bridge: CPM Activity→Scheduled Work Log (schedule_task_id FK), Schedule→Daily Log progress
  - Procore's native schedule-to-field linkage via schedule_task_id. No P6 equivalent.
- **Schedule → Phases** [Dense]: CONTAINS, PRECEDES
  - Bridge: Summary Activities→Phase boundaries, Milestones→Phase gates
  - Schedule activities organized by phase. Milestones mark phase transitions.
- **Schedule → Building Elements** [Dense]: PRECEDES, CONCURRENT_WITH
  - Bridge: Activity→Building System installation sequence, MEP Rough-In concurrent across systems
  - Schedule sequences building system installation. Vertical progression floor-by-floor.
- **Schedule → Resources** [Moderate]: REQUIRES, ALLOCATED_TO
  - Bridge: Activity→Trade/Equipment/Material, Resource Loading→Schedule Activities
  - Resource-loaded schedules assign trades, equipment, and materials to activities.
- **Permits & Regulatory → Phases** [Dense]: ENABLES, DEPENDS_ON
  - Bridge: Building Permit→Construction start, CO→Occupancy, Inspections→Phase gates
  - Permits gate construction phases. No construction without permits.
- **Permits & Regulatory → Quality & Safety Records** [Dense]: COMPLIES_WITH, INSPECTED_BY
  - Bridge: AHJ Inspection→Code compliance, OSHA→Safety requirements, Special Inspection→Structural integrity
  - Regulatory inspections verify code compliance. OSHA governs safety requirements.
- **Permits & Regulatory → Organizations** [Moderate]: ISSUED_BY, COMPLIES_WITH
  - Bridge: Building Department→Permit, Fire Marshal→Review, OSHA→Citation, Insurance Broker→COI
  - Regulatory authorities issue permits. Contractors and vendors comply.
- **Permits & Regulatory → Documents & Communications** [Moderate]: DOCUMENTS, REFERENCES
  - Bridge: Permit Application→Drawing/Spec package, Safety Plan→OSHA compliance, SWPPP→Environmental compliance
  - Permit applications reference design documents. Safety and environmental plans are compliance documents.

## Element Relationships

Specific element-to-element connections with cardinality, lifecycle phase, and data join paths.

- Financial Instruments.Project Budget —[CONTAINS]→ Financial Instruments.Budget Line Item (1:many, High)
  - Join: `budget_line_items.project_id → projects.project_id`
  - A project budget is composed of individual budget line items that allocate dollars to specific cost codes.
- Financial Instruments.Budget Line Item —[CLASSIFIED_AS]→ Financial Instruments.Cost Code (many:1, High)
  - Join: `budget_line_items via wbs_codes.cost_code_id → cost_codes.cost_code_id`
  - Every budget line item maps to a cost code that classifies what type of work the money is for.
- Financial Instruments.Budget Line Item —[CLASSIFIED_AS]→ Financial Instruments.WBS Code (many:1, High)
  - Join: `budget_line_items via wbs_codes.wbs_code_id`
  - WBS codes add a second dimension (phase, location, or category) to cost code classification.
- Financial Instruments.Budget Line Item —[CLASSIFIED_AS]→ Financial Instruments.Budget Code (many:1, Medium)
  - Join: `budget_line_items.budget_code_id → budget_codes.budget_code_id`
  - Budget codes group budget lines for executive reporting (Structure, MEP, General Conditions).
- Financial Instruments.Budget Line Item —[ADJUSTED_BY]→ Financial Instruments.Budget Modification (1:many, High)
  - Join: `budget_modifications.wbs_code_id → budget_line_items (via wbs_codes)`
  - Budget modifications transfer money between budget lines. transfer_amount is the field (not amount).
- Financial Instruments.Commitment (Subcontract) —[COMMITTED_TO]→ Financial Instruments.Budget Line Item (many:many, High)
  - Join: `commitment_line_items.wbs_code_id → wbs_codes → budget_line_items`
  - Commitment line items map to budget lines via WBS codes. Committed cost = sum of commitment line items per cost code.
- Financial Instruments.Commitment (Subcontract) —[CONTAINS]→ Financial Instruments.Commitment Line Item (1:many, High)
  - Join: `commitment_line_items.commitment_id → commitments.commitment_id`
  - Each commitment breaks into line items that allocate to specific cost codes.
- Financial Instruments.Commitment (Subcontract) —[CONTRACTED_TO]→ Organizations.Subcontractor (Trade-Specific) (many:1, High)
  - Join: `commitments.vendor_id → project_vendors.vendor_id`
  - Every commitment links to a vendor. Vendor identity links financial to organizational domain.
- Financial Instruments.Commitment (Purchase Order) —[COMMITTED_TO]→ Financial Instruments.Budget Line Item (many:many, High)
  - Join: `commitment_line_items.wbs_code_id → wbs_codes → budget_line_items`
  - PO line items map to budget lines. Same mechanism as subcontracts.
- Financial Instruments.Commitment (Purchase Order) —[CONTRACTED_TO]→ Organizations.Material Supplier (many:1, High)
  - Join: `commitments.vendor_id → project_vendors.vendor_id`
  - POs link to material suppliers via vendor_id.
- Financial Instruments.Change Event (CE) —[ORIGINATED_FROM]→ Documents & Communications.Request for Information (RFI) (many:1, High)
  - Join: `change_events.origin_type = 'Rfi::Header' AND change_events.origin_id = rfis.rfi_header_id`
  - 307K CEs originated from RFIs — the strongest document-to-financial bridge in Procore.
- Financial Instruments.Change Event (CE) —[ORIGINATED_FROM]→ Quality & Safety Records.Observation (many:1, Medium)
  - Join: `change_events.origin_type = 'Observations::Item' AND change_events.origin_id = observations.observation_id`
  - 20,238 CEs originated from observations across 727 cos. Direct field-to-financial traced path.
- Financial Instruments.Change Event (CE) —[CLASSIFIED_AS]→ Standards & Classifications.MasterFormat (many:1, High)
  - Join: `change_events → change_event_line_items.wbs_code_id → wbs_codes.cost_code_id → cost_codes.code (MasterFormat prefix)`
  - CE cost lands on cost codes which map to MasterFormat divisions for building system attribution.
- Financial Instruments.Change Event (CE) —[CONTAINS]→ Financial Instruments.Change Event Line Item (1:many, High)
  - Join: `change_event_line_items.change_event_id → change_events.change_event_id`
  - CE line items carry cost-code-level detail with wbs_code_id and latest_cost_amount.
- Financial Instruments.Change Event (CE) —[BECOMES]→ Financial Instruments.Potential Change Order (CPCO) (1:many, High)
  - Join: `commitment_potential_change_orders.change_event_id`
  - A single CE may generate CPCOs for multiple affected subcontractors.
- Financial Instruments.Potential Change Order (CPCO) —[BECOMES]→ Financial Instruments.Commitment Change Order (CCO) (many:1, High)
  - Join: `commitment_potential_change_orders.commitment_change_order_id (89.5% populated)`
  - CPCOs bridge CEs to CCOs. 89.5% have a CCO link — the CE→CPCO→CCO lifecycle chain.
- Financial Instruments.Commitment Change Order (CCO) —[ADJUSTS]→ Financial Instruments.Commitment (Subcontract) (many:1, High)
  - Join: `commitment_change_orders.commitment_id → commitments.commitment_id`
  - CCOs modify commitment amounts. Approved CCOs (96.7%) change the committed dollar amount.
- Financial Instruments.Commitment Change Order (CCO) —[CONTAINS]→ Financial Instruments.CCO Line Item (1:many, High)
  - Join: `commitment_change_order_line_items.commitment_change_order_id`
  - CCO line items carry wbs_code_id and extended_amount for cost-code-level change attribution.
- Financial Instruments.CCO Line Item —[COSTS_AGAINST]→ Financial Instruments.Budget Line Item (many:1, High)
  - Join: `commitment_change_order_line_items.wbs_code_id → wbs_codes → budget_line_items`
  - CCO line item costs land on budget lines via WBS/cost code mapping.
- Financial Instruments.Change Event Line Item —[LINKED_TO]→ Financial Instruments.CCO Line Item (many:many, Medium)
  - Join: `change_event_line_items.commitment_potential_change_order_line_item_id → (CPCO LI table NOT in gold) → commitment_change_order_line_items.commitment_potential_change_order_id`
  - 40.8% of CE line items link to CPCO line items. CPCO line items table not in gold layer limits direct tracing.
- Financial Instruments.Direct Cost —[COSTS_AGAINST]→ Financial Instruments.Budget Line Item (many:many, High)
  - Join: `direct_cost_line_items.wbs_code_id → wbs_codes → budget_line_items`
  - Direct costs charge against budget lines but bypass commitment/invoice workflow.
- Financial Instruments.Direct Cost —[CONTAINS]→ Financial Instruments.Direct Cost Line Item (1:many, High)
  - Join: `direct_cost_line_items.direct_cost_id → direct_costs.direct_cost_id`
  - Direct cost line items provide cost-code-level granularity for non-commitment expenses.
- Financial Instruments.Owner Invoice / Pay Application —[BILLED_AGAINST]→ Financial Instruments.Commitment (Subcontract) (many:1, High)
  - Join: `owner_invoices → commitment billing (SOV-based)`
  - Pay applications bill against prime contract. Sub invoices bill against commitments.
- Financial Instruments.Subcontractor Invoice —[BILLED_AGAINST]→ Financial Instruments.Commitment (Subcontract) (many:1, High)
  - Join: `subcontractor_invoices.commitment_id → commitments.commitment_id`
  - Each sub invoice bills against a specific commitment for work completed that period.
- Financial Instruments.Lien Waiver —[FOLLOWS]→ Financial Instruments.Payment (many:1, High)
  - Join: `payments_lien_waivers → payments`
  - Lien waivers exchanged with each payment cycle. Required for final payment.
- Financial Instruments.Owner Change Order (Prime Contract CO) —[ADJUSTS]→ Contracts & Procurement.Prime Contract (many:1, Medium)
  - Join: `prime_contract_change_orders.prime_contract_id`
  - Owner COs modify the prime contract value. Revenue side of change management.
- Financial Instruments.Cost Code —[MAPS_TO]→ Standards & Classifications.MasterFormat (many:1, High)
  - Join: `cost_codes.code (first 2 digits = MasterFormat division prefix)`
  - Cost code → MasterFormat division is the primary cross-company cost normalization path.
- Financial Instruments.Cost Code —[MAPS_TO]→ Building Elements.All Building Systems (many:many, High)
  - Join: `cost_codes.code prefix: 02→Site & Earthwork, 03→Foundations, 05→Structural Frame, 07→Roofing, 09→Interiors, 14→Elevators, 22→Plumbing, 23→HVAC, 26→Electrical, 33→Site Utilities`
  - MasterFormat division prefixes on cost codes map directly to building system categories.
- Financial Instruments.WBS Code —[CLASSIFIED_AS]→ Financial Instruments.Cost Code (many:1, High)
  - Join: `wbs_codes.cost_code_id → cost_codes.cost_code_id`
  - WBS codes contain a cost_code_id that provides the building system mapping key.
- Documents & Communications.Request for Information (RFI) —[BECOMES]→ Financial Instruments.Change Event (CE) (many:many, High)
  - Join: `change_events.origin_type = 'Rfi::Header' AND change_events.origin_id = rfis.rfi_header_id`
  - RFIs become CEs when cost impact is confirmed. 307K CEs linked to RFIs.
- Documents & Communications.Request for Information (RFI) —[CLASSIFIED_AS]→ Building Elements.All Building Systems (many:1, High)
  - Join: `rfis.predicted_topic → 176 ML-classified topics mapping to building systems`
  - predicted_topic is the strongest structured signal for RFI-to-building-system classification. Zero NLP needed.
- Documents & Communications.Request for Information (RFI) —[REFERENCES]→ Documents & Communications.Drawing Sheet (many:many, Medium)
  - Join: `rfis.drawing_number → drawing_revision.number`
  - RFIs reference specific drawing sheets for clarification.
- Documents & Communications.Request for Information (RFI) —[ASSIGNED_TO]→ Organizations.Architect of Record (AOR) (many:1, High)
  - Join: `rfis.assignees / rfis.responsible_contractor → project_vendors / project_role_memberships`
  - RFIs assigned to design team members for response. Ball-in-court tracking.
- Documents & Communications.Request for Information (RFI) —[RESPONDS_TO]→ Documents & Communications.RFI Response (1:many, High)
  - Join: `rfi_responses.rfi_id → rfis.rfi_header_id`
  - Each RFI has one or more responses tracked with text, responder, and official status.
- Quality & Safety Records.Observation —[ORIGINATED_FROM]→ Financial Instruments.Change Event (CE) (many:1, Medium)
  - Join: `change_events.origin_type = 'Observations::Item' AND change_events.origin_id → observation_id`
  - Observations generate CEs when they reveal cost-impacting conditions. 20,238 CEs via this path.
- Quality & Safety Records.Observation —[LEADS]→ Quality & Safety Records.Punch Item (many:many, High)
  - Join: `Statistical — observations 28-day lead time before rework costs; 1.98x multiplier`
  - Observations are leading indicators of downstream punch items and rework. Validated in insight #1.
- Quality & Safety Records.Observation —[ASSIGNED_TO]→ Organizations.Subcontractor (Trade-Specific) (many:1, High)
  - Join: `observation.vendor_id → project_vendors.vendor_id (80% populated)`
  - Observations assigned to responsible vendors for corrective action.
- Quality & Safety Records.Observation —[CLASSIFIED_AS]→ Standards & Classifications.OSHA Hazard Categories (many:1, High)
  - Join: `observation.hazard_name (OSHA-aligned taxonomy: Fall, Struck By, Electrical, etc.)`
  - Safety observations classified by structured OSHA hazard taxonomy. 16 types with 50+ cos each.
- Quality & Safety Records.Observation —[LOCATED_AT]→ Locations.Room / Space (many:1, Medium)
  - Join: `observation.location_id → locations.location_id`
  - Observations reference specific project locations for spatial quality analysis.
- Quality & Safety Records.Observation —[MAPS_TO]→ Building Elements.All Building Systems (many:many, Medium)
  - Join: `observation.name keyword clustering → 18 issue categories → building systems`
  - Keyword clustering on observation.name maps to building systems (43% clustering rate).
- Quality & Safety Records.Punch Item —[ASSIGNED_TO]→ Organizations.Subcontractor (Trade-Specific) (many:1, High)
  - Join: `punch_item.vendor_id → project_vendors.vendor_id`
  - Punch items assigned to responsible vendors for correction before acceptance.
- Quality & Safety Records.Punch Item —[MAPS_TO]→ Building Elements.All Building Systems (many:many, High)
  - Join: `punch_item.name keyword clustering → 18 issue categories → building systems (74% clustering rate)`
  - Punch item name clustering is the strongest field-to-system mapping. Paint/Finish #1 universally.
- Quality & Safety Records.Punch Item —[LOCATED_AT]→ Locations.Room / Space (many:1, Medium)
  - Join: `punch_item.location_id → locations.location_id`
  - Punch items reference specific locations for spatial closeout tracking.
- Quality & Safety Records.Inspection —[CONTAINS]→ Quality & Safety Records.Inspection Item (1:many, High)
  - Join: `inspection_items.inspection_id → inspections.inspection_id`
  - Inspections contain checklist items. Deficiency rate 2-6% across 5,470 cos.
- Quality & Safety Records.Inspection Item —[VIOLATES]→ Standards & Classifications.International Building Code (IBC) (many:many, Medium)
  - Join: `inspection_items.status = 'Deficient' → spec/code deviation`
  - Deficient inspection items indicate code or specification non-conformance.
- Quality & Safety Records.Incident —[CONTAINS]→ Quality & Safety Records.Incident Record (1:many, High)
  - Join: `incident_record.incident_id → incident.incident_id`
  - One incident may have multiple records (injuries, damage, environmental release).
- Quality & Safety Records.Incident —[TRIGGERS]→ Quality & Safety Records.Corrective Action / Incident Action (1:many, High)
  - Join: `incident_action.incident_id → incident.incident_id`
  - Incidents trigger required corrective actions. Only 1.2% of observations have linked actions.
- Quality & Safety Records.Coordination Issue —[LINKED_TO]→ Documents & Communications.Request for Information (RFI) (many:1, Medium)
  - Join: `coordination_issue.rfi_header_id → rfis.rfi_header_id (4,967 linked across 204 cos)`
  - Coordination issues link to RFIs when design clarification is needed. Bridge to financial impact.
- Quality & Safety Records.Coordination Issue (Design-Related) —[BECOMES]→ Financial Instruments.Change Event (CE) (many:many, Medium)
  - Join: `coordination_issue.rfi_header_id → rfis → change_events.origin_type = 'Rfi::Header'`
  - Design coordination issues → RFI → CE chain traces design problems to cost impact.
- Field Operations.Delay Log Entry —[TRIGGERED_BY]→ Resources.All Materials (many:many, High)
  - Join: `daily_log_delay.delay_type = 'Material' (84K records, 4,351 cos, structured enum)`
  - Material delays are a structured signal — zero NLP needed. Primary signal for material shortage detection.
- Field Operations.Delay Log Entry —[IMPACTS]→ Schedule.Detail Activity (many:many, Medium)
  - Join: `daily_log_delay → schedule impact (inferred via date overlap with schedule activities)`
  - Delays impact schedule activities. Duration field (median 5.0 days for Material) quantifies impact.
- Field Operations.Daily Log Note —[DOCUMENTS]→ Quality & Safety Records.Observation (many:many, Low)
  - Join: `Conceptual — daily_log_note.comment keywords correlate with observation findings`
  - Daily log notes provide narrative context. NLP keywords (rework, shortage) supplement structured data.
- Field Operations.Scheduled Work Log Entry —[LINKED_TO]→ Schedule.Detail Activity (many:1, High)
  - Join: `daily_log_scheduled_work_task.schedule_task_id → schedule_task.schedule_task_id`
  - Procore's native field-to-schedule linkage. showed boolean = plan-vs-actual. No P6 equivalent.
- Field Operations.Manpower Log Entry —[PERFORMED_BY]→ Resources.All Trades (many:1, High)
  - Join: `daily_log_manpower.trade_name (direct trade identifier)`
  - trade_name is the most direct trade signal in Procore. Keyword normalization to canonical trades needed.
- Field Operations.Equipment Log Entry —[REQUIRES]→ Resources.All Equipment (many:1, Medium)
  - Join: `daily_log_equipment.equipment_name (free text, keyword classification to 12 types)`
  - Equipment names are free text requiring keyword classification into canonical equipment types.
- Field Operations.Delivery Log Entry —[CONSUMES]→ Resources.All Materials (many:1, Medium)
  - Join: `daily_log_delivery.contents (free text describing delivered materials)`
  - Delivery contents describe materials received on site. Free text — keyword matching needed.
- Field Operations.Weather Log Entry —[TRIGGERED_BY]→ Field Operations.Delay Log Entry (many:many, High)
  - Join: `daily_log_observed_weather_condition.is_weather_delay (boolean)`
  - Weather conditions trigger delay events. is_weather_delay is the primary weather-delay boolean.
- Documents & Communications.Submittal —[SPECIFIES]→ Resources.All Materials (many:1, High)
  - Join: `submittals.title (product/material description — strongest material signal in Procore)`
  - Submittal titles describe specific products. Every specified material requires a submittal.
- Documents & Communications.Submittal —[REFERENCES]→ Documents & Communications.Specification Section (many:1, Medium)
  - Join: `submittals.specification_section_id → specification_sections.specification_section_id`
  - Submittals organized by spec section. Adoption depends on whether team enters spec sections.
- Documents & Communications.Submittal —[PRECEDES]→ Resources.All Materials (many:1, High)
  - Join: `Submittal approval → procurement release → material fabrication/delivery`
  - Approved submittals trigger procurement. Overdue submittals → material delays.
- Documents & Communications.Submittal —[LEADS]→ Field Operations.Delay Log Entry (many:many, Medium)
  - Join: `submittals.overdue = true → downstream material delays (statistical)`
  - 718K overdue submittals. Overdue submittals are a leading indicator of material delays.
- Documents & Communications.Drawing Revision —[VERSIONED_AS]→ Documents & Communications.Drawing Sheet (many:1, High)
  - Join: `drawing_revision.drawing_id → drawings (revision tracking per sheet)`
  - Drawing revisions track successive versions of each sheet. current flag identifies latest.
- Documents & Communications.Drawing Revision —[SUPERSEDES]→ Documents & Communications.Drawing Revision (1:1, High)
  - Join: `drawing_revision.revision (sequential — newer supersedes older)`
  - Each revision supersedes the prior version. Revision clouds highlight changes.
- Documents & Communications.Specification Section —[GOVERNS]→ Resources.All Materials (1:many, Medium)
  - Join: `specification_sections.section_number → MasterFormat division → material requirements`
  - Spec sections define what materials must be. Part 2 (Products) specifies exact requirements.
- Documents & Communications.Specification Section —[MAPS_TO]→ Standards & Classifications.MasterFormat (many:1, High)
  - Join: `specification_sections.section_number (first 2 digits = MasterFormat division)`
  - Spec sections organized by MasterFormat. Division 05 12 00 = Structural Steel Framing.
- Documents & Communications.Correspondence —[ASSIGNED_TO]→ Roles.Project Manager (many:1, Medium)
  - Join: `correspondences.assignees → project_role_memberships`
  - Correspondence assigned to responsible parties for response via configurable types.
- Documents & Communications.Meeting —[CONTAINS]→ Documents & Communications.Meeting Minutes / Meeting Item (1:many, High)
  - Join: `meeting_item.meeting_id → meeting.meeting_id`
  - Meetings contain agenda/action items. Items carry forward across meetings.
- Documents & Communications.Meeting Minutes / Meeting Item —[ASSIGNED_TO]→ Roles.All Roles (many:1, High)
  - Join: `meeting_item_assignee.meeting_item_id → meeting_item`
  - Meeting action items assigned to specific people for follow-up.
- Documents & Communications.Action Plan —[CONTAINS]→ Documents & Communications.Action Plan Line Item (Task) (1:many, High)
  - Join: `action_plan_line_item.action_plan_id → action_plan.action_plan_id`
  - Action plans contain individually tracked tasks with assignees and due dates.
- Documents & Communications.Action Plan Line Item (Task) —[LINKED_TO]→ Quality & Safety Records.Observation (many:1, High)
  - Join: `action_plan_line_item_record → observation (cross-reference to source issue)`
  - Action plan tasks link back to source observations, punch items, or incidents.
- Documents & Communications.Action Plan Line Item (Task) —[LINKED_TO]→ Quality & Safety Records.Punch Item (many:1, High)
  - Join: `action_plan_line_item_record → punch_item (cross-reference to source issue)`
  - Action plan tasks created from punch items for structured closeout remediation.
- Documents & Communications.Photo —[ATTACHED_TO]→ Quality & Safety Records.Observation (many:1, High)
  - Join: `photo attachment → observation (via attachment tables)`
  - Photos are the visual evidence layer for observations. Very high volume.
- Documents & Communications.Photo —[ATTACHED_TO]→ Quality & Safety Records.Punch Item (many:1, High)
  - Join: `photo attachment → punch_item (via attachment tables)`
  - Punch item photos document deficiencies for trade correction.
- Documents & Communications.Photo —[ATTACHED_TO]→ Field Operations.Daily Log (Header) (many:1, High)
  - Join: `photo attachment → daily_log (via daily log note attachments)`
  - Daily log photos document site conditions and progress.
- Documents & Communications.Photo —[LOCATED_AT]→ Locations.All Location Levels (many:1, Medium)
  - Join: `photo.location_id → locations.location_id`
  - Photos can be geotagged to specific project locations.
- Standards & Classifications.MasterFormat —[MAPS_TO]→ Building Elements.All Building Systems (1:many, High)
  - Join: `MasterFormat division prefix → building system (02→Site, 03→Foundations, 05→Structure, etc.)`
  - MasterFormat is the Rosetta Stone — primary bridge from financial data to building systems.
- Standards & Classifications.UniFormat —[MAPS_TO]→ Building Elements.All Building Systems (1:many, Medium)
  - Join: `UniFormat category → building system (B→Shell, C→Interiors, D→Services)`
  - UniFormat provides systems-level classification. Less adopted than MasterFormat in Procore.
- Standards & Classifications.OSHA Hazard Categories —[CLASSIFIES]→ Quality & Safety Records.Safety Observation (1:many, High)
  - Join: `observation.hazard_name (Fall, Struck By, Electrical, Caught In/Between, etc.)`
  - 16 OSHA-aligned hazard types with 50+ cos each. Structured taxonomy — zero NLP needed.
- Standards & Classifications.Specification Section —[GOVERNS]→ Documents & Communications.Submittal (1:many, Medium)
  - Join: `submittals.specification_section_id → specification_sections`
  - Spec sections define submittal requirements. Each submittal maps to a spec section.
- Organizations.General Contractor (GC) —[MANAGES]→ All Domains.Project (1:many, High)
  - Join: `projects.company_id → companies.company_id`
  - GC is the primary project entity. All project data rolls up to the GC.
- Organizations.Subcontractor (Trade-Specific) —[CONTRACTED_TO]→ Financial Instruments.Commitment (Subcontract) (1:many, High)
  - Join: `commitments.vendor_id → project_vendors.vendor_id`
  - Subcontractors linked via vendor_id on commitments. Primary financial-to-organizational link.
- Organizations.Subcontractor (Trade-Specific) —[ASSIGNED_TO]→ Quality & Safety Records.Observation (1:many, High)
  - Join: `observation.vendor_id → project_vendors.vendor_id (80% populated)`
  - Vendors responsible for corrective action on observations.
- Organizations.Subcontractor (Trade-Specific) —[ASSIGNED_TO]→ Quality & Safety Records.Punch Item (1:many, High)
  - Join: `punch_item.vendor_id → project_vendors.vendor_id`
  - Vendors responsible for correcting punch list items.
- Organizations.Subcontractor (Trade-Specific) —[PERFORMED_BY]→ Field Operations.Manpower Log Entry (1:many, High)
  - Join: `daily_log_manpower.vendor_id → project_vendors.vendor_id`
  - Manpower entries track vendor workforce on site daily.
- Organizations.Architect of Record (AOR) —[DESIGNED_BY]→ Documents & Communications.Drawing Set (1:many, High)
  - Join: `project_role_memberships.role_name / group = 'design_team'`
  - Architect creates design documents. role_name or group='design_team' identifies design team members.
- Organizations.Architect of Record (AOR) —[RESPONDS_TO]→ Documents & Communications.Request for Information (RFI) (1:many, High)
  - Join: `rfis.assignees → project_role_memberships (design team)`
  - Design team responds to RFIs. Response time is a key metric.
- Organizations.MEP Engineer —[DESIGNED_BY]→ Building Elements.HVAC (1:many, Medium)
  - Join: `project_role_memberships.group = 'design_team' (engineering roles)`
  - MEP engineers design mechanical, electrical, and plumbing systems.
- Organizations.Special Inspection Agency —[INSPECTED_BY]→ Quality & Safety Records.Third-Party / Special Inspection (1:many, Medium)
  - Join: `Conceptual — inspections by third-party agencies. No direct FK to organization.`
  - Third-party inspection agencies conduct code-required inspections.
- Organizations.Surety / Bonding Company —[MITIGATES]→ Risk.Financial Risk (many:many, Medium)
  - Join: `vendor_insurances tables track bonding/insurance`
  - Surety bonds transfer performance risk. COI compliance tracked via vendor_insurances tables.
- Roles.Project Manager —[MANAGES]→ Financial Instruments.Change Event (CE) (1:many, High)
  - Join: `project_role_memberships.role_name = 'Project Manager' → project_id`
  - PM manages the change management process. Approves CEs, reviews CCOs.
- Roles.Project Manager —[MANAGES]→ Quality & Safety Records.Punch Item (1:many, High)
  - Join: `project_role_memberships.role_name = 'Project Manager' → project_id`
  - PM manages punch list closure process.
- Roles.Superintendent —[MANAGES]→ Field Operations.Daily Log (Header) (1:many, High)
  - Join: `project_role_memberships.role_name = 'Superintendent' → daily_log_completion.project_id`
  - Superintendent owns the daily log — the legal record of site activity.
- Roles.Safety Manager / Safety Director —[MANAGES]→ Quality & Safety Records.Safety Observation (1:many, Medium)
  - Join: `project_role_memberships.role_name = 'Safety Manager' (47.2% of safety obs projects)`
  - Safety managers drive safety observation programs. Not universal coverage.
- Roles.Quality Manager / QC Inspector —[INSPECTED_BY]→ Quality & Safety Records.Inspection (1:many, Medium)
  - Join: `inspection_assignees.user_id → users`
  - QC inspectors conduct formal inspections against checklists.
- Roles.Scheduler / Project Controls Manager —[MANAGES]→ Schedule.Detail Activity (1:many, Medium)
  - Join: `project_role_memberships.role_name → scheduling tools`
  - Scheduler maintains CPM schedule. Schedule updates and look-aheads.
- Roles.Document Controller —[MANAGES]→ Documents & Communications.Drawing Revision (1:many, Medium)
  - Join: `Conceptual — document controller manages drawing distribution`
  - Document controller ensures field teams have current drawings.
- Schedule.Detail Activity —[DEPENDS_ON]→ Schedule.Detail Activity (many:many, High)
  - Join: `scheduling_relationship.from_activity / to_activity + dependency_type (FS/SS/FF/SF) + lag`
  - Typed dependencies with lag values. Enables critical path analysis and logic quality checks.
- Schedule.Detail Activity —[LOCATED_AT]→ Locations.Floor / Level (many:1, Medium)
  - Join: `scheduling_activity.category_data (JSON) or custom_fields (area/zone)`
  - Schedule activities linked to locations via custom fields or category data.
- Schedule.Detail Activity —[REQUIRES]→ Resources.All Trades (many:many, Medium)
  - Join: `scheduling_activity.resource_data (JSON), vendor_id, vendor_name`
  - New scheduling tool carries resource data including trade/vendor assignment.
- Schedule.Detail Activity —[COSTS_AGAINST]→ Financial Instruments.Budget Line Item (many:many, Medium)
  - Join: `scheduling_activity → cost loading via cost_code alignment`
  - Cost-loaded schedules map activities to budget lines for earned value tracking.
- Schedule.Detail Activity —[LINKED_TO]→ Field Operations.Scheduled Work Task Link (many:1, High)
  - Join: `daily_log_scheduled_work_task.schedule_task_id → schedule_task.schedule_task_id`
  - Procore's native field-to-schedule FK. Unique capability.
- Schedule.Milestone —[DEPENDS_ON]→ Phases.All Phases (many:1, High)
  - Join: `scheduling_activity.milestone = true → phase-level milestones`
  - Milestones mark phase transitions. Substantial completion, final completion are key milestones.
- Schedule.Baseline Schedule —[VERSIONED_AS]→ Schedule.Schedule Update (1:many, High)
  - Join: `scheduling_type.parent_schedule_id (baseline linkage), is_active flag`
  - Schedule updates tracked against baseline. imported_data_date is the data date.
- Schedule.Schedule Change Tracking —[DOCUMENTS]→ Schedule.Detail Activity (many:1, High)
  - Join: `schedule_task_changes.schedule_task_id → schedule tasks (old/new dates, duration, percentage)`
  - Structured delta tracking with when_at timestamps. Unique audit trail.
- Schedule.Look-Ahead Schedule —[CONTAINS]→ Schedule.Detail Activity (1:many, High)
  - Join: `schedule_lookahead_task.schedule_task_id → schedule_task (FK to CPM)`
  - Look-ahead tasks link to CPM activities. Separate entity with richer field context.
- Locations.Project Site —[CONTAINS]→ Locations.Building (1:many, High)
  - Join: `Location hierarchy: Site→Building→Floor→Zone→Room`
  - Hierarchical spatial decomposition. Level 0→Level 5 nesting.
- Locations.Floor / Level —[CONTAINS]→ Locations.Zone / Wing (1:many, High)
  - Join: `Location hierarchy: Floor→Zone/Wing→Room/Space`
  - Floor contains zones and rooms. Primary spatial organizing level.
- Locations.Floor / Level —[CONTAINS]→ Building Elements.All Building Systems (1:many, Medium)
  - Join: `Building systems installed per floor. MEP rough-in, interiors, finishes are floor-specific.`
  - Building elements exist at specific floor levels during vertical construction.
- Risk.Design Risk —[TRIGGERED_BY]→ Documents & Communications.Request for Information (RFI) (many:many, High)
  - Join: `rfis → change_events (cost impact). RFI volume leads change order volume.`
  - Design risk manifests as RFIs that become change events. Validated in insight #31.
- Risk.Design Risk —[IMPACTS]→ Financial Instruments.Change Event (CE) (many:many, High)
  - Join: `change_events.change_reason = 'design_development' (354K CEs, 6,748 cos, $54.8B)`
  - Design changes = 26.4% median of CE cost. Largest single change category.
- Risk.Safety Risk —[TRIGGERED_BY]→ Quality & Safety Records.Safety Observation (many:many, High)
  - Join: `observation.category = 'Safety' + hazard_name recurrence detection`
  - Safety observations with recurring hazards signal systemic safety risk. Insight #11.
- Risk.Supply Chain Risk —[TRIGGERED_BY]→ Field Operations.Delay Log Entry (many:many, High)
  - Join: `daily_log_delay.delay_type = 'Material' (84K records, 4,351 cos)`
  - Material delays are structured signal for supply chain risk. Insight: Material Shortage Detection.
- Risk.Schedule Risk —[TRIGGERED_BY]→ Schedule.Detail Activity (many:many, Medium)
  - Join: `Float erosion on critical/near-critical activities. scheduling_activity.total_float trending toward 0.`
  - Float erosion is a leading schedule risk indicator. Critical path concentration = risk concentration.
- Risk.Financial Risk —[MITIGATED_BY]→ Financial Instruments.Contingency (many:1, Medium)
  - Join: `Contingency burn rate = (contingency used / original) / (% complete). Burn rate > 1.0 = red flag.`
  - Contingency reserves mitigate financial risk. Burn rate is a leading indicator of budget distress.
- Phases.Preconstruction —[PRECEDES]→ Phases.Procurement (1:1, High)
  - Join: `Sequential phase flow: Preconstruction→Procurement→Mobilization→Construction→Closeout`
  - Phases follow a defined sequence. Some overlap (fast-track).
- Phases.Construction (all sub-phases) —[REQUIRES]→ Building Elements.All Building Systems (many:many, High)
  - Join: `Phase×System activity matrix defines which systems are active during each construction phase`
  - System-resource matrix crossed with phase-system matrix defines full resource picture.
- Phases.Contract Closeout —[DEPENDS_ON]→ Quality & Safety Records.Punch Item (1:many, High)
  - Join: `Punch list closure required for substantial completion certificate`
  - Punch list must be closed before owner acceptance. Gate for retainage release.
- Phases.Contract Closeout —[DEPENDS_ON]→ Documents & Communications.As-Built Documentation (1:many, High)
  - Join: `As-built drawings required for final completion`
  - As-built documentation is a contractual closeout deliverable.
- Workflows & Statuses.Universal Lifecycle Statuses —[RESOLVES_TO]→ Documents & Communications.Request for Information (RFI) (many:1, High)
  - Join: `rfis.status (Draft→Open→Closed/Overdue)`
  - RFI follows universal lifecycle. Status transitions drive response time metrics.
- Workflows & Statuses.Approval & Review Statuses —[APPROVED_AS]→ Documents & Communications.Submittal (many:1, High)
  - Join: `submittals.status (Approved/Approved as Noted/Revise & Resubmit/Rejected)`
  - Submittal approval workflow gates procurement. Multiple reviewers in approval chain.
- Workflows & Statuses.Financial Workflow Stages —[APPROVED_AS]→ Financial Instruments.Commitment Change Order (CCO) (many:1, High)
  - Join: `commitment_change_orders.status (Draft→Pending→Approved, 96.7%)`
  - CCO approval workflow. 96.7% reach Approved status.
- Workflows & Statuses.Field Disposition Statuses —[RESOLVES_TO]→ Quality & Safety Records.Observation (many:1, High)
  - Join: `observation.status (Open→In Progress→Ready for Review→Closed)`
  - Observation resolution workflow. Status transitions track remediation progress.
- Workflows & Statuses.Field Disposition Statuses —[RESOLVES_TO]→ Quality & Safety Records.Punch Item (many:1, High)
  - Join: `punch_item.workflow_status (Open→In Progress→Ready for Review→Closed/Not Accepted)`
  - Punch item resolution workflow. Not Accepted items restart the cycle.
- Models & BIM.3D Building Information Model —[REPRESENTS]→ Building Elements.All Building Systems (1:many, High)
  - Join: `Conceptual — BIM model elements represent physical building systems`
  - BIM models contain digital representations of all building systems.
- Models & BIM.Clash Detection Result —[CLASHES_WITH]→ Building Elements.All Building Systems (many:many, Medium)
  - Join: `coordination_issue.issue_type = 'Clash' → affected systems`
  - Clash detection finds spatial conflicts between building system elements.
- Models & BIM.Coordination Issue —[LINKED_TO]→ Documents & Communications.Request for Information (RFI) (many:1, Medium)
  - Join: `coordination_issue.rfi_header_id → rfis.rfi_header_id`
  - 4,967 coordination issues linked to RFIs. Bridge from BIM to documents.
- Models & BIM.Drawing Sheet —[REPRESENTS]→ Models & BIM.3D Building Information Model (many:1, Medium)
  - Join: `Drawing sheets = 2D views from 3D models (discipline-organized)`
  - 2D drawing sheets generated from 3D BIM models. Sheet ↔ model element linkage.
- Models & BIM.Point Cloud / Laser Scan —[CAPTURED_BY]→ Building Elements.All Building Systems (many:many, Low)
  - Join: `Laser scan captures as-built conditions for comparison to design intent`
  - Reality capture validates construction against design. Growing adoption.
- Models & BIM.Quantity Takeoff —[CONSUMES]→ Resources.All Materials (1:many, Medium)
  - Join: `BIM model quantities → material quantities for procurement and estimating`
  - BIM-based quantity takeoff feeds material procurement and cost estimating.
- Contracts & Procurement.Subcontract —[COMMITTED_TO]→ Financial Instruments.Commitment (Subcontract) (1:1, High)
  - Join: `Same instrument — subcontract in Contracts domain = commitment in Financial domain`
  - Subcontract is the commercial instrument; commitment is the financial tracking. Same record.
- Contracts & Procurement.Purchase Order —[COMMITTED_TO]→ Financial Instruments.Commitment (Purchase Order) (1:1, High)
  - Join: `Same instrument — PO in Contracts domain = commitment (PO type) in Financial domain`
  - PO is the commercial instrument; commitment is the financial tracking. Same record.
- Contracts & Procurement.Bid Package —[PRECEDES]→ Contracts & Procurement.Subcontract (1:many, High)
  - Join: `Bid → evaluation → award → subcontract execution`
  - Bid packages lead to subcontract awards. Bidding process is preconstruction-gated.
- Contracts & Procurement.Warranty —[FOLLOWS]→ Phases.Contract Closeout (many:1, Medium)
  - Join: `Warranty period begins at substantial completion. 1-year general, 2-year MEP, 5-20 year roofing.`
  - Warranty obligations begin at closeout. Duration varies by building system.
- Contracts & Procurement.Insurance Certificate —[COMPLIES_WITH]→ Permits & Regulatory.Safety & Labor Compliance (many:many, High)
  - Join: `project_vendor_insurances / company_vendor_insurances → insurance tracking`
  - COI compliance tracked via vendor insurance tables. Structured data — High Procore coverage.
- Permits & Regulatory.Building Permit —[ENABLES]→ Phases.Construction (all sub-phases) (1:many, High)
  - Join: `Building permit must be issued before construction starts — critical path item`
  - No construction without a permit. Permit issuance is a schedule milestone.
- Permits & Regulatory.AHJ Inspection —[INSPECTED_BY]→ Quality & Safety Records.Third-Party / Special Inspection (many:many, Medium)
  - Join: `Regulatory inspections conducted by AHJ. Tracked via inspections module.`
  - AHJ inspections gate construction milestones. Pass required before covering work.
- Permits & Regulatory.Certificate of Occupancy —[DEPENDS_ON]→ Quality & Safety Records.Inspection (many:many, High)
  - Join: `All required inspections must pass before CO issuance`
  - CO requires all inspection approvals. Final regulatory gate for project completion.
- Permits & Regulatory.Certificate of Occupancy —[DEPENDS_ON]→ Quality & Safety Records.Punch Item (many:many, High)
  - Join: `Punch list closure required for CO (or TCO with open items)`
  - Punch list closure is a prerequisite for certificate of occupancy.
- Project Attributes.Project Type —[SEGMENTS]→ Financial Instruments.All Financial Instruments (1:many, High)
  - Join: `projects.project_type → project-level attribute for segmenting financial benchmarks`
  - Project type is the primary segmentation dimension for financial benchmarking.
- Project Attributes.Total Value Band —[SEGMENTS]→ Financial Instruments.All Financial Instruments (1:many, High)
  - Join: `projects.total_value → value band classification for cost normalization`
  - Value band segments projects for like-for-like cost comparison.
- Project Attributes.Project Type —[SEGMENTS]→ Quality & Safety Records.All Quality Records (1:many, High)
  - Join: `projects.project_type → segmentation for quality/safety benchmarks (7 types with 99+ cos)`
  - Project type drives the 3D hot sheet — issue distributions vary by type.
- Project Attributes.State / Region —[SEGMENTS]→ All Domains.All Elements (1:many, Medium)
  - Join: `projects.state_name (NOT state_code) → geographic segmentation`
  - Geographic segmentation for regional benchmarking. 20+ states with 30+ cos.
- Building Elements.HVAC —[COMPOSED_OF]→ Resources.Ductwork & HVAC Materials (1:many, High)
  - Join: `Building system composed of specific material assemblies. HVAC = ductwork + equipment + controls.`
  - Building systems are physically composed of materials and assemblies.
- Building Elements.Exterior Enclosure —[ADJACENT_TO]→ Building Elements.Structural Frame (many:many, High)
  - Join: `Exterior enclosure adjacent to structural frame at slab edges and connections.`
  - Adjacent systems require coordination. Curtain wall anchors to structural frame.
- Building Elements.Exterior Enclosure —[ADJACENT_TO]→ Building Elements.Roofing (many:many, High)
  - Join: `Roofing-to-wall transitions require coordination for weather-tightness.`
  - Interface between enclosure and roofing is a common defect location.
- Organizations.General Contractor (GC) —[OWNED_BY]→ Organizations.Private Developer (many:1, High)
  - Join: `projects.company_id → owner identification (project ownership)`
  - Project owned by developer/owner entity. GC contracted by owner to build.
- Organizations.Architect of Record (AOR) —[PARTICIPATES_IN]→ Documents & Communications.Meeting (many:many, High)
  - Join: `meeting_attendee.user_id → users → project_role_memberships (design team)`
  - Architects participate in OAC meetings. Attendance tracked via meeting_attendees.
- Roles.Superintendent —[REPORTS_TO]→ Roles.Project Manager (many:1, High)
  - Join: `Organizational hierarchy: Superintendent reports to PM on field matters.`
  - Standard construction reporting hierarchy. Superintendent handles field; PM handles overall project.
- Roles.Foreman / General Foreman —[REPORTS_TO]→ Roles.Superintendent (many:1, High)
  - Join: `Organizational hierarchy: Foreman reports to superintendent for field coordination.`
  - Foreman runs specific crews under superintendent direction.
- Documents & Communications.Submittal —[TYPED_AS]→ Documents & Communications.Shop Drawing (many:1, High)
  - Join: `submittals.type = 'Shop Drawing' — shop drawings are a TYPE of submittal.`
  - Shop drawings, product data, and samples are all types of submittals.
- Documents & Communications.Submittal —[TYPED_AS]→ Documents & Communications.Product Data Submittal (many:1, High)
  - Join: `submittals.type = 'Product Data' — product data is a TYPE of submittal.`
  - Product data submittals are the highest-volume submittal type.
- Financial Instruments.Commitment (Subcontract) —[TYPED_AS]→ Contracts & Procurement.Subcontract (1:1, High)
  - Join: `commitments.type = 'Subcontract' — type field distinguishes subcontract from PO.`
  - Subcontract is a type of commitment instrument.
- Project Attributes.Project Type —[COMPARABLE_TO]→ Project Attributes.Project Type (many:many, High)
  - Join: `Projects with same project_type are comparable for benchmarking.`
  - Projects of the same type support meaningful comparison.
- Project Attributes.Total Value Band —[COMPARABLE_TO]→ Project Attributes.Total Value Band (many:many, High)
  - Join: `Projects within the same value band are comparable for cost benchmarking.`
  - Value band enables like-for-like cost comparison.
- Financial Instruments.Budget Variance —[BENCHMARKED_AGAINST]→ Financial Instruments.Budget Variance (many:many, High)
  - Join: `Project budget variance benchmarked against portfolio/industry median.`
  - Budget variance by cost code division benchmarked across projects.

## Relationship Graph Summary

Total: 171 domain pairs, 8361 relationship edges

**building-elements**: resources (202), phases (99), financial-instruments (89), locations (86), schedule (80), quality-safety-records (79), field-operations (70), organizations (70), project-attributes (64), contracts-procurement (60), roles (60), building-elements (57), models-bim (51), documents-communications (50), permits-regulatory (50), risk (50), standards-classifications (50), workflows-statuses (45)
**contracts-procurement**: financial-instruments (80), documents-communications (70), organizations (70), field-operations (60), schedule (60), contracts-procurement (50), roles (50), quality-safety-records (40), workflows-statuses (40), risk (37), project-attributes (36), phases (35), standards-classifications (30), locations (20), models-bim (20), permits-regulatory (20), resources (12)
**documents-communications**: financial-instruments (99), organizations (95), phases (80), quality-safety-records (80), risk (69), documents-communications (60), roles (60), workflows-statuses (60), schedule (59), field-operations (55), permits-regulatory (50), standards-classifications (50), models-bim (45), project-attributes (38), locations (30), resources (19)
**field-operations**: locations (107), roles (86), schedule (80), organizations (60), quality-safety-records (60), phases (56), field-operations (50), financial-instruments (50), workflows-statuses (50), project-attributes (41), risk (40), permits-regulatory (35), standards-classifications (35), resources (24), models-bim (21)
**financial-instruments**: workflows-statuses (88), organizations (80), phases (70), quality-safety-records (70), risk (65), financial-instruments (62), schedule (50), project-attributes (42), roles (35), locations (34), standards-classifications (33), permits-regulatory (31), models-bim (23), resources (4)
**locations**: schedule (90), quality-safety-records (66), phases (50), resources (50), locations (46), organizations (35), roles (30), workflows-statuses (28), project-attributes (26), models-bim (25), permits-regulatory (25), risk (25), standards-classifications (20)
**models-bim**: phases (50), schedule (40), models-bim (38), quality-safety-records (35), project-attributes (33), resources (28), organizations (24), roles (24), risk (21), workflows-statuses (21), standards-classifications (19), permits-regulatory (16)
**organizations**: quality-safety-records (85), phases (70), resources (60), organizations (50), schedule (50), workflows-statuses (50), project-attributes (46), roles (45), risk (37), permits-regulatory (35), standards-classifications (25)
**permits-regulatory**: phases (85), quality-safety-records (58), permits-regulatory (40), schedule (40), project-attributes (39), roles (35), workflows-statuses (35), resources (33), risk (25), standards-classifications (25)
**phases**: resources (143), schedule (100), quality-safety-records (70), roles (70), phases (60), standards-classifications (50), workflows-statuses (50), risk (49), project-attributes (40)
**project-attributes**: project-attributes (40), resources (40), quality-safety-records (37), schedule (35), risk (32), roles (30), workflows-statuses (25), standards-classifications (24)
**quality-safety-records**: risk (84), schedule (60), workflows-statuses (60), quality-safety-records (50), standards-classifications (50), roles (44), resources (16)
**resources**: resources (56), schedule (50), roles (40), risk (35), standards-classifications (35), workflows-statuses (35)
**risk**: schedule (45), risk (40), roles (35), workflows-statuses (31), standards-classifications (25)
**roles**: roles (52), workflows-statuses (40), schedule (38), standards-classifications (25)
**schedule**: schedule (50), workflows-statuses (35), standards-classifications (25)
**standards-classifications**: standards-classifications (39), workflows-statuses (25)
**workflows-statuses**: workflows-statuses (40)

## Relationship Verbs

The verbs used to describe relationships between elements across domains:

Total: 3348 unique relationship verbs across 1440 verb families.

Key verb families (by frequency):
- **MEASURES** (33 variants): MEASURES, MEASURES ADOPTION OF, MEASURES AGAINST, ...
- **TRIGGERS** (25 variants): TRIGGERS, TRIGGERS AMENDMENT TO, TRIGGERS CHANGE IN, ...
- **TRACKS** (22 variants): TRACKS, TRACKS ACROSS PROJECTS, TRACKS AGAINST, ...
- **VERIFIES** (20 variants): VERIFIES, VERIFIES AGAINST, VERIFIES ALL CORRECTIVE ACTIONS CLOSED AT, ...
- **RECORDS** (19 variants): RECORDS, RECORDS ACTUAL DATES FOR, RECORDS ACTUALS IN, ...
- **VALIDATES** (18 variants): VALIDATES, VALIDATES ABSENCE OF, VALIDATES AGAINST, ...
- **LOGS** (17 variants): LOGS, LOGS ACCEPTANCE TEST VIA, LOGS ARRIVAL OF, ...
- **REQUIRES** (17 variants): REQUIRES, REQUIRES CLEARANCE FROM, REQUIRES COMPACTION TESTING BY, ...
- **TRACKED** (16 variants): TRACKED ACROSS, TRACKED AGAINST, TRACKED ALONGSIDE, ...
- **DOCUMENTS** (15 variants): DOCUMENTS, DOCUMENTS ACTIVITY OF, DOCUMENTS COMPLIANCE WITH, ...
- **FLAGGED** (15 variants): FLAGGED AGAINST, FLAGGED AS OPEN IN, FLAGGED AT, ...
- **ISSUED** (14 variants): ISSUED AFTER, ISSUED AGAINST, ISSUED AS, ...
- **VERIFIED** (14 variants): VERIFIED AGAINST, VERIFIED AT, VERIFIED BEFORE, ...
- **MEASURED** (13 variants): MEASURED ACROSS, MEASURED AGAINST, MEASURED AS, ...
- **SPECIFIES** (13 variants): SPECIFIES, SPECIFIES ASSEMBLIES FOR, SPECIFIES EQUIPMENT FOR, ...
- **TESTED** (13 variants): TESTED, TESTED AT, TESTED BY, ...
- **ASSESSED** (12 variants): ASSESSED ACROSS, ASSESSED AFTER, ASSESSED AGAINST, ...
- **CERTIFIES** (12 variants): CERTIFIES, CERTIFIES AGAINST, CERTIFIES AS, ...
- **DOCUMENTED** (12 variants): DOCUMENTED AGAINST, DOCUMENTED AS, DOCUMENTED AT, ...
- **PROVIDES** (12 variants): PROVIDES, PROVIDES CRANES FOR, PROVIDES DAILY SNAPSHOT FOR, ...
- **ASSIGNS** (11 variants): ASSIGNS, ASSIGNS ACCOUNTABILITY TO, ASSIGNS CORRECTION TO, ...
- **CERTIFIED** (11 variants): CERTIFIED AFTER, CERTIFIED AT, CERTIFIED BY, ...
- **CONFIRMS** (11 variants): CONFIRMS, CONFIRMS APPROVAL BY, CONFIRMS DELIVERY FOR, ...
- **DEFINES** (11 variants): DEFINES, DEFINES BOUNDARY FOR, DEFINES COMPLETENESS OF, ...
- **DIRECTS** (11 variants): DIRECTS, DIRECTS CHANGE TO, DIRECTS CHANGES DURING, ...
- **DRIVES** (11 variants): DRIVES, DRIVES COMPLEXITY OF, DRIVES CREW SIZING FOR, ...
- **GATES** (11 variants): GATES, GATES BILLING ON, GATES DELIVERY UNTIL APPROVED IN, ...
- **INSPECTED** (11 variants): INSPECTED AGAINST, INSPECTED AT, INSPECTED BEFORE BACKFILL AT, ...
- **INSPECTS** (11 variants): INSPECTS, INSPECTS AGAINST, INSPECTS AT, ...
- **RELEASED** (11 variants): RELEASED AFTER, RELEASED AT, RELEASED BY, ...
- **CLOSES** (10 variants): CLOSES, CLOSES AT, CLOSES ITEMS IN, ...
- **SCHEDULED** (10 variants): SCHEDULED AS, SCHEDULED AT, SCHEDULED BY, ...
- **SUBMITTED** (10 variants): SUBMITTED AFTER, SUBMITTED AS, SUBMITTED AT, ...
- **APPROVES** (9 variants): APPROVES, APPROVES DETAIL FOR, APPROVES FOR, ...
- **BILLED** (9 variants): BILLED AGAINST, BILLED AT, BILLED BACK TO, ...
- **BILLS** (9 variants): BILLS ADDED LABOR OF, BILLS EQUIPMENT TIME TO, BILLS INSTALLATION OF, ...
- **CLOSED** (9 variants): CLOSED AS OF, CLOSED AT, CLOSED BY, ...
- **DELIVERED** (9 variants): DELIVERED AT, DELIVERED BY, DELIVERED DURING, ...
- **DETAILS** (9 variants): DETAILS, DETAILS CONNECTIONS FOR, DETAILS FABRICATION FOR, ...
- **GOVERNS** (9 variants): GOVERNS, GOVERNS COMPLIANCE IN, GOVERNS ENGAGEMENT OF, ...
- **ITEMIZES** (9 variants): ITEMIZES EQUIPMENT IN, ITEMIZES EQUIPMENT ON, ITEMIZES LABOR IN, ...
- **REPORTED** (9 variants): REPORTED AS, REPORTED AT, REPORTED BY, ...
- **RESOLVES** (9 variants): RESOLVES, RESOLVES AS, RESOLVES CLASHES DURING, ...
- **SCHEDULES** (9 variants): SCHEDULES, SCHEDULES BY, SCHEDULES CUTOVER AT, ...
- **VALIDATED** (9 variants): VALIDATED AGAINST, VALIDATED BEFORE, VALIDATED BY, ...
- **ASSIGNED** (8 variants): ASSIGNED AS, ASSIGNED BACK TO, ASSIGNED BY, ...
- **BENCHMARKS** (8 variants): BENCHMARKS, BENCHMARKS AGAINST, BENCHMARKS COMPLETION AGAINST, ...
- **CLASSIFIES** (8 variants): CLASSIFIES, CLASSIFIES BY, CLASSIFIES COST OF, ...
- **CLEARS** (8 variants): CLEARS, CLEARS AT, CLEARS DEFICIENCIES FOR, ...
- **CODED** (8 variants): CODED AGAINST, CODED AS, CODED BY, ...

## Key Data Principles

### Financial Model
- **Budget = planned spend, NOT actual cost.** Actual cost comes from commitments, change orders, and direct costs.
- **CE→CCO deduplication:** Change Events and Commitment Change Orders represent the SAME change at different lifecycle stages. NEVER sum them — use GREATEST(CE total, CCO total).
- **Not all companies have financial tools.** Projects without financial modules should be excluded from cost benchmarks.
- **Cost code → MasterFormat → Building System** is the primary financial-to-physical mapping chain.

### Quality & Safety Signals
- **Observations are leading indicators** (during construction, 63% rework correlation, 28-day lead time).
- **Punch items are trailing indicators** (closeout, 17-day lag behind the issue).
- **Combined dual-signal model:** 12,556 unique companies across both observation and punch item data.
- **Keyword clustering on name fields** maps quality/safety records to 18 building system issue categories.

### Classification & Standards
- **MasterFormat (CSI)** is the Rosetta Stone for cross-company cost normalization — maps cost codes to building systems.
- **OSHA hazard categories** provide structured safety classification via observation.hazard_name.
- **RFI predicted_topic** is an ML-classified taxonomy of 176 topics mapping RFIs to building systems.

### Relationships
- **Relationship direction** is encoded by the verb, not by source/target position in edge triples.
- **Element IDs use domain prefixes:** be- (building elements), fi- (financial), qsr- (quality/safety), fo- (field ops), sch- (schedule), loc- (locations), cp- (contracts), org- (organizations), rl- (roles), rk- (risk), ph- (phases), ws- (workflows), res-/mat-/eq- (resources).
