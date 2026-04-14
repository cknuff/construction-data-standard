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
- **Excavation & Shoring** (`be-excav`): Bulk and detailed excavation, sheeting, shoring, and underpinning. Typical trades: equipment operators, general laborers. Often the first major activity on site — schedule and cost overruns here cascade through the project. [MasterFormat 31 10 00 – 31 50 00 | Medium | Mass excavation, trench excavation, sheet piling, soldier pile and lagging, soil nailing]
  - Cost codes often combine all sitework. Daily logs are the best signal for earthwork activities.
- **Backfill & Grading** (`be-backfill`): Structural fill, fine grading, compaction, and subgrade preparation. Equipment-heavy — dozers, loaders, compactors. Quality depends on compaction testing (typically third-party geotechnical). [MasterFormat 31 20 00 – 31 23 00 | Medium | Structural fill, gravel, crushed stone, compaction to 95% Proctor]
  - Often combined with excavation in cost codes. Third-party test results live outside project management systems.
- **Dewatering** (`be-dewater`): Wellpoints, sump pumps, and groundwater control during construction. Triggered by water table conditions — not present on every project. Can become a major unplanned cost if unexpected. [MasterFormat 31 23 19 | Low | Wellpoint systems, sump pumps, deep wells]
  - Highly variable — some projects zero cost; others major budget item. Daily log delays (type: Existing Conditions) may capture water-related issues.
- **Erosion & Sediment Control**: Silt fence, construction entrances, inlet protection, and SWPPP compliance. Required by EPA/state permits — inspected regularly. Trades: general laborers. [MasterFormat 31 25 00 | Medium | Silt fence, erosion blankets, inlet protection, construction entrance]
  - Often in general conditions cost code. Environmental observations and inspections are the strongest signal for compliance issues.

**Foundations**
- **Deep Foundations** (`be-deep-fdn`): Driven piles, drilled shafts, caissons, micropiles, and helical piers. Requires specialized subcontractors and equipment. Production rates (piles per day) are a key schedule driver. Trades: pile drivers, equipment operators. [MasterFormat 31 62 00 – 31 66 00 | Medium | Steel H-piles, precast concrete piles, drilled shafts, micropiles, auger cast piles]
  - Daily log productivity records may capture pile counts. RFIs for pile capacity and obstructions are common.
- **Shallow Foundations** (`be-shallow-fdn`): Spread footings, strip footings, mat foundations, and pier pads. Concrete and formwork are the primary cost drivers. Trades: concrete workers, carpenters (formwork). Pour records track volume and placement. [MasterFormat 03 30 00 | Medium | Spread footings, strip footings, mat slab, pier pads]
  - Often grouped under general concrete cost code. Hard to separate from other concrete elements.
- **Foundation Walls** (`be-fdn-walls`): Cast-in-place or precast foundation walls and retaining walls. Formwork complexity drives cost. Waterproofing is a critical follow-on trade. Trades: concrete workers, carpenters. [MasterFormat 03 30 00 | Medium | CIP walls, precast foundation walls, retaining walls]
  - Rarely separated from footings in cost data. Daily log notes for wall pours help.
- **Grade Beams** (`be-grade-beams`): Reinforced concrete beams connecting foundation elements at or below grade. Transfer loads between piles/piers. Trades: concrete workers, carpenters. [MasterFormat 03 30 00 | Low | Grade beams, tie beams]
  - Rarely its own cost code. RFIs for reinforcing conflicts are common.
- **Slab on Grade** (`ph-slab`): Ground-supported concrete floor slabs with vapor barriers and joint sealants. Includes reinforcement (rebar, WWF, fiber). Quality depends on subgrade prep and finishing. Trades: concrete workers. [MasterFormat 03 30 00 | Medium | 4" SOG, 6" SOG, post-tensioned SOG, fiber-reinforced, vapor barrier]
  - Daily log pour records are a good signal. Observations capture flatness and cracking issues.
- **Below-Grade Waterproofing** (`be-bg-wp`): Foundation waterproofing membranes, dampproofing, underslab vapor barriers, and drainage boards. Failure leads to long-term moisture intrusion. Trades: specialty waterproofing applicators. [MasterFormat 07 10 00 – 07 16 00 | Medium | Fluid-applied membrane, sheet membrane, bentonite, drainage board, dampproofing]
  - Quality observations are a strong signal — waterproofing failures are a top rework driver.

**Site Utilities**
- **Water Main / Service**: Underground domestic and fire water supply piping from street to building. Requires coordination with municipality. Trades: plumbers/pipefitters, equipment operators. [MasterFormat 33 10 00 | Low | Ductile iron pipe, copper service, valves, meters]
  - Inspection records help when specific utility inspections exist. Municipality coordination adds schedule risk.
- **Sanitary Sewer** (`be-sanitary`): Underground sanitary waste piping from building to main, with manholes and cleanouts. Gravity-driven — slope is critical. Trades: plumbers/pipefitters, equipment operators. [MasterFormat 33 30 00 | Low | PVC pipe, concrete manholes, cleanouts, fittings]
  - Similar to water — often grouped in cost codes. Daily logs capture installation activities.
- **Storm Drainage** (`be-storm`): Underground storm water piping, catch basins, and retention/detention systems. Sized by hydrological analysis. Subject to local stormwater regulations. Trades: plumbers/pipefitters, equipment operators. [MasterFormat 33 40 00 | Low | HDPE/PVC pipe, concrete structures, catch basins, detention vaults]
  - Sometimes combined with sanitary in cost codes. Detention/retention system costs vary significantly by locality.
- **Gas Service** (`be-gas-svc`): Underground gas piping from meter to building. Small scope on most projects but requires specialty inspection. Trades: plumbers/pipefitters. [MasterFormat 33 50 00 | Low | Steel/PE gas pipe, fittings, valves, meter]
  - Inspection records for gas testing are a distinct signal when present.
- **Site Electrical & Telecom Ductbank**: Underground electrical and telecom conduit banks, manholes, and handholes. Coordinates with power company. Trades: electricians, equipment operators. [MasterFormat 33 70 00 – 33 80 00 | Low | PVC conduit, concrete encasement, handholes, manholes]
  - Less field data visibility than building MEP. Often utility company coordination delays.

**Structural Frame**
- **Columns** (`be-columns`): Steel or concrete vertical load-bearing members. Steel columns: W-shapes, HSS, pipe. Concrete columns: CIP with rebar cages, formwork. Trades: ironworkers (steel), concrete workers (concrete). Critical path activity. [MasterFormat 03 30 00 / 05 12 00 | Medium | W-shapes, HSS, CIP concrete, rebar cages]
  - Cost codes usually cover all structural concrete or all structural steel — not individual elements. RFI topics help differentiate.
- **Beams & Girders** (`be-beams`): Steel or concrete horizontal spanning members. Steel: W-shapes, built-up sections. Concrete: CIP or precast. Camber and deflection are key design parameters. Trades: ironworkers, concrete workers. [MasterFormat 03 30 00 / 05 12 00 | Medium | W-shapes, built-up sections, precast beams, CIP beams]
  - RFIs and observations provide element-level detail that cost codes don't separate.
- **Floor Slabs & Metal Deck**: Composite metal deck with concrete topping, post-tensioned slabs, or precast plank. Deck erection and concrete pours are major scheduling milestones. Trades: ironworkers (deck), concrete workers (topping). [MasterFormat 03 30 00 / 05 31 00 | Medium | 1.5" and 3" composite deck, lightweight concrete topping, PT slabs, precast hollow core]
  - Concrete pour records in daily logs are a strong signal. Deck erection tracked separately on some projects.
- **Roof Structure** (`be-roof-struct`): Steel or concrete roof framing — long-span joists, trusses, and moment frames. Trades: ironworkers. Often governs crane duration and pick sequence. [MasterFormat 05 12 00 / 05 21 00 | Low | Open-web steel joists, trusses, moment frames, long-span beams]
  - Usually under structural steel code. Joist and truss deliveries are scheduling milestones.
- **Structural Connections & Embeds**: Bolted and welded connections, embed plates, anchor bolts, and base plates. Connection design generates heavy RFI activity — a leading indicator of structural complexity. Trades: ironworkers. [MasterFormat 05 12 00 | Medium | High-strength bolts, weld rod, embed plates, base plates, shear studs]
  - RFIs are the strongest signal — structural connections generate heavy RFI activity.
- **Stairs & Ramps** (`be-stairs`): Cast-in-place or steel stairs and structural ramps, with handrails. Both temporary and permanent stairs. Punch items frequently reference stairs and railings. Trades: ironworkers, concrete workers. [MasterFormat 03 30 00 / 05 51 00 | Medium | Steel pan stairs, precast stairs, CIP stairs, structural ramps]
  - Often under misc metals or concrete code. Punch items are a good signal for stairs.
- **Miscellaneous Metals**: Lintels, loose angles, shelf angles, channels, bollards, and structural railings. Small scope individually but high coordination — nearly every other trade needs miscellaneous metals embedded. Trades: ironworkers. [MasterFormat 05 50 00 | Medium | Lintels, shelf angles, channels, bollards, railings, embed plates]
  - High coordination burden — lintels and shelf angles interact with masonry; embeds interact with concrete.

**Exterior Enclosure**
- **Curtain Wall** (`be-curtainwall`): Aluminum-framed glass curtain wall systems — unitized or stick-built. High RFI and coordination issue activity (MEP penetrations, structural anchors). Major submittal packages. Trades: glaziers, curtain wall installers. [MasterFormat 08 44 00 | High | Unitized curtain wall, stick-built, structural glazing, spider systems]
  - Coordination issues are common — MEP penetrations through curtain wall require early modeling.
- **Windows** (`be-windows`): Punched window units in opaque wall systems. Product submittals drive procurement timeline. Trades: glaziers. [MasterFormat 08 50 00 | Medium | Aluminum, vinyl, wood-clad windows]
  - Submittals are a strong signal — specific product approvals and lead times.
- **Exterior Doors & Entrances**: Entrance doors, storefronts, revolving doors, overhead doors, and service doors. Door hardware drives complexity. Trades: glaziers (storefronts), carpenters (hollow metal). Doors are one of the highest punch item categories. [MasterFormat 08 10 00 – 08 42 00 | High | Storefront entrances, revolving doors, hollow metal, overhead coiling, sliding glass]
  - Doors are one of the highest punch item categories across all project types.
- **Masonry Veneer / Backup Wall**: Brick veneer, stone veneer, and CMU backup walls with through-wall flashing and weep systems. Quality depends on mortar joints, flashing, and drainage. Trades: masons. [MasterFormat 04 20 00 – 04 40 00 | Medium | Brick veneer, natural stone, manufactured stone, CMU backup, cavity wall]
  - Quality observations for mortar joints and flashing failures are common signals.
- **Precast / Metal Panels** (`be-panels`): Architectural precast concrete, insulated metal panels (IMP), ACM panels, and terra cotta. Panel layout coordination with structure and MEP is critical. Trades: ironworkers (erection), specialty installers. [MasterFormat 03 45 00 / 07 42 00 | Medium | Architectural precast, insulated metal panels, ACM, fiber cement, terra cotta]
  - Coordination issues for panel layout vs. MEP penetrations and structural embed locations.
- **Air & Moisture Barrier** (`ph-barrier`): Fluid-applied or sheet membrane air/vapor barriers on exterior sheathing. Performance-critical — failures here cause long-term moisture damage. Third-party inspection is common. Trades: specialty applicators. [MasterFormat 07 25 00 – 07 27 00 | Medium | Fluid-applied membrane, self-adhered sheet, spray-applied, primers]
  - Critical quality item. Observation and inspection records are the strongest signal for failures.
- **Exterior Insulation** (`be-ext-insul`): Continuous insulation (CI) on exterior walls — mineral wool, rigid foam, or spray foam. Energy code compliance driver. Trades: specialty installers, general laborers. [MasterFormat 07 21 00 | Low | Rigid polyiso, mineral wool, EPS, XPS, spray foam]
  - Energy code compliance increasingly requires continuous insulation. Often bundled with air barrier work.

**Roofing**
- **Roof Membrane** (`be-roof-mem`): Single-ply (TPO, PVC, EPDM), built-up, or modified bitumen roofing membranes. Warranty is a key deliverable — manufacturer requirements drive installation quality. Trades: roofers. [MasterFormat 07 50 00 | High | TPO, PVC, EPDM, modified bitumen, built-up roofing]
  - Strong signal across observations and punch items. Submittals specify exact membrane product and warranty requirements.
- **Roof Insulation & Cover Board**: Rigid insulation and tapered systems for drainage, with cover boards. Tapered layout is a design coordination item. Trades: roofers. [MasterFormat 07 22 00 | Low | Polyiso, EPS, XPS, gypsum cover board, tapered crickets]
  - RFIs for roof assembly details and drainage design.
- **Flashing & Sheet Metal**: Roof edge metal, copings, counterflashing, reglets, gutters, and downspouts. Flashing failures are a top source of roof leaks. Trades: roofers, sheet metal workers. [MasterFormat 07 60 00 | Medium | Aluminum copings, galvanized gutters, copper flashing, stainless counterflashing]
  - Observations for flashing defects are a common quality signal. Sometimes its own code; sometimes under roofing.
- **Roof Drainage** (`be-roof-drain`): Interior roof drains, scuppers, overflow drains, and conductor piping. Cross-trade coordination — roofer installs drain bodies, plumber runs pipe. Design drives structural loads (ponding). [MasterFormat 07 63 00 / 22 14 00 | Low | Interior roof drains, scuppers, overflow drains, conductor pipe]
  - Cross-trade coordination between roofer and plumber. Coordination issues are the best signal.
- **Skylights & Roof Hatches**: Unit skylights, smoke vents, and roof access hatches. Small scope but high defect rate per unit — curb flashing is a common failure point. Trades: glaziers, specialty installers. [MasterFormat 08 62 00 / 07 72 00 | Low | Unit skylights, tubular skylights, smoke vents, roof hatches]
  - High defect rate per unit. Curb flashing around skylights is a frequent quality issue.

**HVAC**
- **Ductwork** (`be-ductwork`): Supply, return, and exhaust ductwork — sheet metal, flex, and fittings. Routing coordination with other MEP systems drives schedule. Trades: HVAC/sheet metal workers. [MasterFormat 23 31 00 | High | Sheet metal rectangular, round/spiral, flex duct, lined duct, fittings]
  - Strong signals across multiple field tools. Coordination issues between mechanical, electrical, and plumbing are a major schedule driver.
- **HVAC Piping** (`be-hvac-pipe`): Chilled water, hot water, condenser water, and refrigerant piping with insulation. Pipe sizing and routing are key RFI topics. Trades: pipefitters. [MasterFormat 23 21 00 | Medium | Steel, copper, CPVC pipe]
  - Observation and RFI signals help differentiate piping from general HVAC work.
- **Air Handling Equipment**: AHUs, RTUs, fan coil units, VAV boxes, and exhaust fans. Major submittals — equipment delivery is a key scheduling milestone. Trades: HVAC mechanics. [MasterFormat 23 73 00 – 23 74 00 | High | Rooftop units, AHUs, fan coil units, VAV boxes, exhaust fans]
  - Coordination issues for equipment clearances are common. Long lead items — procurement timing is critical.
- **Heating Equipment** (`be-heating`): Boilers, unit heaters, radiant heating, and heat exchangers. Seasonal dependency — heating system must be operational for winter work. Trades: HVAC mechanics. [MasterFormat 23 52 00 | Medium | Boilers (gas/electric), unit heaters, radiant panels, heat exchangers]
  - Temporary heat is often needed before permanent heating is operational — tracked in daily logs.
- **Cooling Equipment** (`be-cooling`): Chillers, cooling towers, condensing units, and split systems. Heaviest and most expensive MEP equipment — rigging and crane logistics are critical. Trades: HVAC mechanics. [MasterFormat 23 64 00 | Medium | Centrifugal chillers, air-cooled chillers, cooling towers, condensing units, VRF]
  - Major equipment — delivery logistics and rigging are schedule drivers.
- **Duct Insulation** (`be-duct-insul`): Thermal and acoustic insulation on ductwork. Required by energy code on exposed supply and return duct. Trades: insulators. [MasterFormat 23 07 00 | Low | Fiberglass wrap, elastomeric, foil-faced rigid, duct liner]
  - Punch items flag missing or damaged insulation. Often bundled with general HVAC code.
- **HVAC Controls & Thermostats**: DDC controls, thermostats, sensors, damper actuators, and building automation system (BAS) programming. Controls/commissioning generates heavy RFI and punch item activity. Trades: controls technicians, HVAC mechanics. [MasterFormat 23 09 00 / 25 00 00 | Medium | DDC controllers, thermostats, CO2 sensors, damper actuators, BAS software]
  - Controls sequences of operation generate heavy RFI activity. Late-project commissioning drives punch items.
- **Testing Adjusting & Balancing** (`ph-tab`): Air and water system balancing and commissioning verification. Late-project activity — results validate design assumptions. Trades: TAB contractors, commissioning agents. [MasterFormat 23 05 93 | Low | Air balancing, water balancing, sound testing, vibration testing]
  - Punch items and commissioning inspections are primary signals. Usually late-project activity.

**Plumbing**
- **Domestic Water Supply**: Hot and cold water distribution piping, valves, hangers, and insulation. Leak testing is a key milestone. Trades: plumbers/pipefitters. [MasterFormat 22 11 00 | Medium | Copper, PEX, CPVC, stainless steel pipe]
  - Observations for leaks are a strong signal. Pipe material choices vary by region and code.
- **Sanitary Waste & Vent**: DWV piping, cleanouts, floor drains, and traps. Gravity-driven — slope is critical and generates RFIs for routing in tight ceilings. Trades: plumbers/pipefitters. [MasterFormat 22 13 00 | Medium | Cast iron, PVC, ABS pipe]
  - RFIs for routing and slope are common. Cast iron vs. PVC is a cost and noise trade-off.
- **Interior Storm Drainage**: Interior roof drain leaders, area drains, and conductor piping. Connects roof drainage to underground storm system. Trades: plumbers/pipefitters. [MasterFormat 22 14 00 | Low | Cast iron, PVC conductor pipe]
  - Small scope. Often combined with sanitary plumbing in cost codes.
- **Gas Piping (Interior)**: Interior natural gas distribution to equipment — boilers, water heaters, kitchen equipment. Requires pressure testing and inspection. Trades: plumbers/pipefitters. [MasterFormat 22 11 00 | Low | Black steel pipe, fittings, valves, flex connectors, regulators]
  - Gas inspections are a distinct signal. Small scope on most projects.
- **Plumbing Fixtures** (`ph-plumb-fix`): Toilets, urinals, sinks, faucets, drinking fountains, and floor drains. High submittal activity (product approvals) and very high punch item rates — plumbing fixtures are a top punch category. Trades: plumbers. [MasterFormat 22 40 00 | High | Water closets, urinals, lavatories, kitchen sinks, drinking fountains, mop sinks]
  - Very high punch item rate — plumbing fixtures are a top punch category across all project types.
- **Water Heaters** (`be-water-htr`): Domestic water heating — tanks, tankless, and heat pump water heaters. Small scope but affects hot water distribution design. Trades: plumbers. [MasterFormat 22 33 00 | Low | Tank water heaters, tankless, heat pump, solar preheat]
  - Small scope. Submittal for specific unit selection.
- **Pipe Insulation** (`be-pipe-insul`): Thermal insulation on plumbing piping. Required by energy code on hot water and chilled supply lines. Trades: insulators. [MasterFormat 22 07 00 | Low | Fiberglass, elastomeric, phenolic pipe insulation]
  - Punch items flag missing insulation. Often bundled with general plumbing.

**Electrical**
- **Power Distribution** (`be-power-dist`): Main switchgear, distribution panels, transformers, bus duct, and feeders. Major submittals with long lead times — procurement timing is critical. Trades: electricians. [MasterFormat 26 24 00 – 26 28 00 | High | Switchgear, distribution panels, transformers, bus duct, feeders, metering]
  - Major submittals with long lead times. RFIs for panel sizing and circuit loading are common.
- **Branch Wiring & Devices**: Outlets, switches, junction boxes, home runs, and branch circuits. Highest-volume electrical work. Punch items for cover plates and device alignment are top closeout issues. Trades: electricians. [MasterFormat 26 27 00 | High | Wire (12 AWG, 10 AWG), boxes, receptacles, switches, cover plates, connectors]
  - Cover plates and device alignment are the highest-volume electrical punch items.
- **Conduit & Raceways** (`be-conduit`): EMT, rigid, PVC conduit, cable tray, and wireways. Routing coordination with other MEP systems is a major schedule driver. Trades: electricians. [MasterFormat 26 05 33 | Medium | EMT, rigid conduit, PVC conduit, cable tray, wireways, fittings]
  - Coordination issues for conduit routing are common — especially in tight ceiling spaces.
- **Lighting Fixtures & Controls**: Interior and exterior lighting fixtures, controls, occupancy sensors, and daylight harvesting systems. High submittal and punch item activity. Trades: electricians. [MasterFormat 26 50 00 – 26 56 00 | High | LED fixtures, controls, occupancy sensors, daylight sensors, dimming systems]
  - Lighting is a high-volume punch category. Submittal packages for fixture selections drive procurement schedule.
- **Emergency / Standby Power**: Emergency generators, automatic transfer switches (ATS), UPS systems, and emergency circuits. Code-required for life safety. Trades: electricians. [MasterFormat 26 32 00 – 26 36 00 | Medium | Diesel/gas generators, ATS, UPS, fuel tanks, emergency panels]
  - Code-required testing and inspection records are a distinct signal.
- **Grounding & Lightning Protection**: Building grounding system, lightning rods, and bonding. Code-required; tested during construction. Small scope. Trades: electricians. [MasterFormat 26 05 26 / 26 41 00 | Low | Copper ground wire, ground rods, lightning rods, bonding clamps]
  - Inspection records for grounding resistance tests are the primary signal.

**Fire Protection**
- **Sprinkler Mains & Branches**: Fire sprinkler distribution piping — mains, cross-mains, and branch lines with seismic bracing. Head layout coordination with ceilings and MEP is a top coordination issue. Trades: sprinkler fitters. [MasterFormat 21 13 00 | High | Black steel pipe, CPVC, fittings, hangers, seismic bracing]
  - Sprinkler head layout vs. ceiling layout vs. other MEP is a top coordination challenge.
- **Sprinkler Heads** (`be-sprink-head`): Pendant, upright, sidewall, and concealed sprinkler heads. Very high punch item rate — concealed head cover plates are a top closeout item. Trades: sprinkler fitters. [MasterFormat 21 13 00 | High | Pendant, upright, sidewall, concealed, ESFR heads]
  - Concealed head cover plates are consistently a top closeout punch item.
- **Standpipes & Hose Connections**: Standpipe risers, hose valves, and fire department connections (FDC). Required for buildings above certain heights. Flow testing is a code requirement. Trades: sprinkler fitters. [MasterFormat 21 12 00 | Low | Steel pipe, hose valves, FDC assemblies, check valves]
  - Inspections for flow tests are a distinct signal.
- **Fire Pump** (`be-fire-pump`): Fire pump, jockey pump, controller, and test header. Required when municipal water pressure is insufficient. Acceptance testing is code-required. Trades: sprinkler fitters, electricians. [MasterFormat 21 11 00 | Low | Electric/diesel fire pump, jockey pump, controller, test header]
  - Distinct equipment — submittal and acceptance testing signals. Not present on all projects.
- **Fire Alarm & Detection**: Fire alarm control panel (FACP), pull stations, smoke/heat detectors, notification appliances, and duct detectors. Code-required system with acceptance testing. Trades: electricians, low-voltage technicians. [MasterFormat 28 31 00 | High | FACP, smoke detectors, heat detectors, pull stations, horn/strobes, duct detectors]
  - Device alignment and labeling are common punch items. Acceptance testing inspections are a distinct signal. Usually its own cost code.

**Low Voltage & Technology**
- **Data / Telecom Cabling**: Cat6/fiber optic cabling, patch panels, racks, and telecom rooms. Pathway coordination with electrical. Trades: low-voltage technicians. [MasterFormat 27 10 00 – 27 15 00 | Medium | Cat6/6A, single-mode fiber, multi-mode fiber, patch panels, racks]
  - Punch items for labeling and testing. Sometimes bundled with general electrical.
- **Security Systems** (`be-security`): CCTV cameras, access control (card readers, controllers), and intrusion detection. Integrates with door hardware — coordination signal. Trades: low-voltage technicians. [MasterFormat 28 20 00 – 28 23 00 | Medium | IP cameras, card readers, controllers, door strikes, magnetic locks]
  - Access control integrates with door hardware (Division 08) — cross-trade coordination.
- **Audio / Visual Systems**: AV systems — displays, speakers, distributed audio, and conference room systems. Often owner-furnished / contractor-installed (OFCI). Trades: low-voltage technicians. [MasterFormat 27 40 00 | Low | Displays, projectors, speakers, amplifiers, control systems, cabling]
  - Often owner-furnished / contractor-installed — procurement responsibility varies.
- **Building Automation Devices & Wiring**: BAS field devices, sensors, actuators, and control wiring (not programming — see HVAC Controls). Different installer than the controls programmer. Trades: low-voltage technicians. [MasterFormat 25 10 00 | Low | Temperature sensors, humidity sensors, actuators, controllers, control wiring]
  - BAS programming vs. device installation are usually different subcontractors. Overlaps with HVAC Controls.
- **Specialty Systems** (`pa-specialty-system`): Nurse call, intercom, paging, distributed antenna (DAS), and clock systems. Project-type dependent — nurse call for healthcare, DAS for large buildings. Trades: low-voltage technicians. [MasterFormat 27 50 00 – 27 53 00 | Low | Nurse call, intercom, paging, DAS, master clock, mass notification]
  - Project-type dependent. DAS increasingly required by fire code in large buildings.

**Interiors**
- **Metal Stud Framing** (`ph-framing`): Interior metal stud partitions, soffits, and bulkhead framing with blocking. Layout accuracy drives downstream finish quality. Trades: drywall hangers. [MasterFormat 09 22 16 | Medium | 25-ga, 20-ga studs]
  - Usually combined with drywall in cost codes. Blocking for wall-mounted items is a common coordination issue.
- **Drywall / Gypsum Board**: Gypsum board installation, taping, and finishing — including specialty boards (moisture-resistant, fire-rated, abuse-resistant). Drywall damage and finish quality are top punch categories. Trades: drywall hangers, finishers. [MasterFormat 09 29 00 | High | Type X, moisture-resistant, abuse-resistant, shaft liner]
  - Strong observation and punch item signal. Drywall damage and finish quality are top punch categories.
- **Interior Doors Frames & Hardware**: Interior hollow metal and wood doors, frames, and finish hardware (hinges, closers, locks, pulls). Hardware sets are complex submittals. Doors/hardware is consistently a top 3 punch item category. Trades: carpenters. [MasterFormat 08 11 00 – 08 71 00 | High | Hollow metal, wood, FRP doors]
  - Consistently one of the top 3 punch item categories across all project types.
- **Acoustic Ceilings** (`be-act`): Suspended acoustic ceiling grid and tile systems. Layout coordination with lighting, sprinklers, and diffusers. Trades: ceiling installers. [MasterFormat 09 51 00 | High | 2x2, 2x4 tegular/lay-in tile]
  - Common punch item category — damaged tiles and grid alignment. RFIs for ceiling heights and clearances.
- **Drywall Ceilings Soffits & Bulkheads**: Drywall ceilings, soffits, bulkheads, and light coves — non-acoustic applications. More complex framing than walls. Trades: drywall hangers, finishers. [MasterFormat 09 29 00 | Medium | Flat ceilings, soffits, bulkheads, light coves, radius ceilings]
  - RFIs for dimensions and detailing. Lumped with general drywall in cost codes.
- **Paint & Wall Coatings** (`ph-paint`): Interior painting, primer, specialty coatings, stain, and clear finishes. Paint/finish is the #1 punch item category universally — touch-ups and color inconsistency dominate closeout. Trades: painters. [MasterFormat 09 91 00 | High | Latex paint, epoxy, urethane, stain, primer]
  - Paint/finish is the #1 punch item category universally. Extremely strong signal.
- **Wallcovering** (`be-wallcover`): Vinyl wallcovering, specialty wall finishes, and wall protection (corner guards, crash rails). Common in healthcare and hospitality. Trades: painters, specialty installers. [MasterFormat 09 72 00 / 10 26 00 | Low | Vinyl wallcovering, fabric wallcovering, corner guards, crash rails, chair rails]
  - Punch items for seams and adhesion failures. Project-type dependent.
- **Floor Tile & Stone**: Ceramic, porcelain, and natural stone tile for floors and walls — including setting materials and grout. Cracked tiles, grout, and lippage are common punch items. Trades: tile setters. [MasterFormat 09 30 00 | High | Ceramic, porcelain, marble, granite, limestone]
  - Strong punch item signal — cracked tiles and grout issues. Submittals specify exact tile product.
- **Carpet & Resilient Flooring**: Carpet (broadloom, tile), VCT, LVT, rubber, and sheet vinyl with resilient base. Seams, transitions, and base are frequent closeout items. Trades: floor installers. [MasterFormat 09 68 00 | High | Carpet tile, broadloom, LVT, VCT, rubber, sheet vinyl, resilient base]
  - Common punch item category. Seams and transitions are frequent closeout items.
- **Specialty Flooring** (`be-spec-floor`): Polished concrete, epoxy, terrazzo, and resinous flooring. Project-type dependent — common in industrial, healthcare, and education. Trades: specialty installers. [MasterFormat 03 35 00 / 09 67 00 | Medium | Polished concrete, epoxy, terrazzo, urethane, MMA]
  - Project-type dependent. Surface prep is critical — failures trace to poor subfloor preparation.
- **Casework & Millwork** (`ph-casework`): Cabinets, countertops, shelving, built-in furniture, and wood trim (base/crown molding). High punch item rate — scratches, chips, alignment, and door adjustment. Trades: carpenters. [MasterFormat 06 20 00 – 12 30 00 | High | Plastic laminate casework, wood veneer, solid surface counters, stone counters, wood trim]
  - High punch item rate — scratches, chips, alignment, and door adjustment are common closeout items.
- **Countertops** (`be-countertop`): Solid surface, stone, quartz, and plastic laminate countertops. Templated after casework installation — template-to-install cycle is a schedule constraint. Trades: specialty installers. [MasterFormat 12 36 00 | Medium | Quartz, granite, marble, solid surface, plastic laminate]
  - Submittals specify exact product and color. Template-to-fabrication lead time.
- **Toilet Accessories & Specialties**: Toilet partitions, accessories (paper holders, grab bars, soap dispensers), mirrors, and signage. High punch item rate — installation alignment, missing items, and damage. Trades: carpenters, general laborers. [MasterFormat 10 21 00 – 10 28 00 | High | Toilet partitions, grab bars, paper holders, soap dispensers, mirrors, dryers]
  - High punch item rate — installation alignment and missing items are common closeout issues.
- **Signage & Wayfinding**: Room signs, directional signs, code-required signs, and ADA signage. Late-project scope — often last items installed before occupancy. Trades: specialty installers. [MasterFormat 10 14 00 | Low | Room ID signs, directional, code-required exit signs, ADA tactile signs]
  - Usually late project. Punch items for incorrect or missing signs. ADA compliance is key.

**Elevators**
- **Elevator Car & Hoistway**: Passenger, service, and freight elevator cars — hoistway doors, cab finishes, and controls. Elevator installation is a major scheduling milestone. Long lead time item. Trades: elevator mechanics. [MasterFormat 14 20 00 | High | Traction passenger, hydraulic, MRL, service, freight elevators]
  - Elevator installation is a major scheduling milestone. Punch items for cab finishes and door operation.
- **Elevator Machinery & Controls**: Traction machines, hydraulic units, motor controllers, and dispatching systems. Acceptance testing/inspection by authority having jurisdiction (AHJ) is required. Trades: elevator mechanics. [MasterFormat 14 20 00 | Medium | Gearless traction, geared traction, hydraulic power unit, MRL drives, controllers]
  - Acceptance testing by AHJ is required before occupancy. Inspection records are a distinct signal.

**Site Improvements**
- **Paving** (`be-paving`): Asphalt and concrete paving for parking lots, access roads, and loading areas. Temperature-sensitive installation (asphalt). Trades: equipment operators, general laborers. [MasterFormat 32 12 00 – 32 13 00 | Medium | Asphalt, concrete paving, pervious concrete, pavers]
  - Daily log notes for paving activities. Temperature and weather dependencies.
- **Sidewalks & Curbs**: Concrete sidewalks, curbs, gutters, ADA ramps, and pavers. ADA compliance is a common observation and punch item trigger. Trades: concrete workers. [MasterFormat 32 16 00 | Medium | Concrete sidewalks, curb and gutter, ADA detectable warning pavers]
  - ADA compliance observations and punch items are a common signal.
- **Landscaping & Irrigation**: Trees, shrubs, ground cover, turf, and irrigation systems. Usually one of the last exterior scopes. Plant survival warranty (typically 1 year) extends beyond project completion. Trades: landscape contractors. [MasterFormat 32 90 00 | Medium | Trees, shrubs, sod, seed, mulch, irrigation pipe, drip, spray heads, controllers]
  - Punch items for plant survival and irrigation coverage. Warranty extends beyond project completion.
- **Site Lighting** (`be-site-light`): Parking lot and pathway lighting — poles, bollard lights, and site electrical. Coordinates with site electrical underground. Trades: electricians. [MasterFormat 26 56 00 / 32 00 00 | Low | Light poles, bollard fixtures, LED site lights, photocells]
  - Sometimes under electrical code; sometimes under sitework — inconsistent categorization.
- **Fencing & Gates**: Chain link, ornamental, and security fencing with gates and barriers. Small scope on most projects. Trades: fence contractors. [MasterFormat 32 31 00 | Low | Chain link, ornamental aluminum, steel picket, slide gates, swing gates]
  - Small scope. Usually under general sitework cost code.

**Standard Measures**
- **Cost per SF by System**: Total cost of each building system divided by gross building area (SF). The primary unit cost benchmark for comparing systems across projects. Calculation: system cost / gross SF. Source: budget line items, cost codes, building area. [AACE | Medium | $5-$50/SF depending on system (structure $15-35, MEP $30-60, finishes $10-25)]
  - Not all customers have financial tools. Exclude projects without cost data from benchmarks.
- **Punch Item Rate by Element Category**: Count of punch items per unit area (per 1000 SF) or per unit count (per door, per fixture) for each element category. Tracks closeout quality. Calculation: punch count / area or unit count. Source: punch items, building area. [N/A | High | 5-50 items per 1000 SF depending on element]
  - Validated 18-category keyword clustering on punch item names. 0% null on name field.
- **RFI Density by System**: Count of RFIs per system per million dollars of contract value. Tracks design coordination complexity. Calculation: RFI count / (contract value / $1M). Source: RFIs, contract value. [N/A | Medium | 10-100 RFIs per $1M depending on system]
  - ML-classified RFI topic taxonomy (176 topics) enables mapping to building systems without NLP.
- **Observation Rate by Element**: Count of quality/safety observations per unit area or per system. Tracks field issue frequency. Calculation: observation count / area. Source: observations, building area. [N/A | Medium | 1-20 observations per 1000 SF]
  - 18-category keyword clustering validated. Category filter (Quality vs. Safety) segments the data.
- **Submittal Cycle Time by System**: Average days from submittal creation to final approval for each system. Tracks procurement timeline performance. Calculation: avg(approval_date - created_date) by system. Source: submittals. [N/A | Medium | 14-60 days typical]
  - Overdue submittals (718K records) are a signal for procurement delays.
- **Coordination Issue Density** (`bim-coord-issue-2`): Count of coordination issues per system or trade per million dollars. Tracks MEP/architectural coordination complexity. Calculation: issue count / (contract value / $1M). Source: coordination issues, contract value. [N/A | Medium | 5-30 issues per $1M]
  - MEP-heavy. Issue types (Clash

### Contracts & Procurement

**Procurement Lifecycle**
- **Prequalification** (`cp-prequalification`): Vetting of a contractor or vendor's financial health, safety record, bonding capacity, and relevant experience BEFORE they are invited to bid. The gatekeeping step that determines who is eligible to compete for work. [AGC Prequalification Standards | None | Financial review, safety record (EMR < 1.0), bonding capacity, trade license verification, project r]
  - Procore Prequalification exists as a product but data is not yet in the analytics layer. TradeTapp and ISNetworld are major third-party platforms.
- **Bid Package** (`cp-bid-package`): A defined scope of work issued to qualified contractors for competitive pricing. Bundles drawings, specifications, schedule, and commercial terms into a single solicitation. The unit of procurement — one package per trade or work scope. [AIA A701 (Instructions to Bidders) | None | By trade: Concrete, Structural Steel, MEP, Drywall, Roofing, Elevators]
  - Bid packages are typically organized by CSI MasterFormat division. The number of packages varies by delivery method (hard bid = many, CM/GC = fewer, design-build = fewest).
- **Request for Qualification** (`cp-req-qualificatio`): Formal solicitation to assess contractor capabilities before inviting bids. Used on complex or specialized scopes where not all contractors can perform the work. Shortlists the field before pricing begins. [AIA | None | RFQ for structural steel erection, curtain wall, elevator, fire protection]
  - RFQs are most common on owner-driven projects and large GC programs. Design-build uses RFQs at the prime contract level.
- **Request for Proposal** (`cp-req-proposal`): Detailed solicitation requesting scope, approach, schedule, and price from qualified contractors. More comprehensive than a simple bid — evaluates methodology, not just price. Common on negotiated or best-value procurements. [AIA | None | Design-build RFP, CM-at-risk RFP, specialty trade RFP]
  - RFPs are the standard for design-build, CM/GC, and public best-value projects. Pure hard-bid projects skip RFPs and go straight to ITB.
- **Proposal / Bid** (`cp-proposal-bid`): A contractor's formal response to an ITB, RFQ, or RFP — includes pricing, scope clarifications, exclusions, alternates, and schedule. The document that becomes the basis for contract negotiation upon award. [AIA | None | Lump sum bid, unit price bid, GMP proposal, T&M proposal, design-build proposal]
  - Bid leveling (comparing proposals across bidders) is typically done in Excel. Number of bidders per package is a key market health indicator.
- **Bid Evaluation / Leveling** (`cp-bid-evaluation`): Comparative analysis of competing proposals — normalizing scope, pricing, qualifications, and exclusions to make an apples-to-apples recommendation. Identifies the apparent low bidder or best-value selection. [AIA | None | Price comparison, scope gap analysis, exclusion identification, reference checks, schedule evaluatio]
  - Bid leveling is one of the most Excel-dependent processes in construction. No PM system fully automates scope normalization.
- **Award / Notice to Proceed** (`cp-award-notice`): Formal notification to the selected contractor that they have won the work and are authorized to begin. Triggers mobilization, procurement, and insurance/bonding requirements. May precede the executed contract via a Letter of Intent. [AIA A101/A201 | Low | Award letter, Letter of Intent (LOI), Notice to Proceed (NTP), verbal authorization]
  - LOI vs. NTP vs. executed contract: many subs start work on an LOI before the contract is signed. This creates risk exposure for the GC.

**Contract Instruments**
- **Subcontract** (`cp-subcontract`): Executed agreement between a general contractor and a subcontractor for a defined scope of work at an agreed price. The primary commercial vehicle for trade work. Includes scope, price, schedule, insurance, and flow-down terms. [AIA A401 (Standard Subcontract) | High | Lump sum, GMP, unit price, T&M, cost-plus]
  - In Procore, subcontracts are stored as commitments with type classification. Financial detail (line items, COs, invoicing) lives in Financial Instruments domain.
- **Purchase Order** (`cp-purchase-order`): Agreement for material supply, equipment rental, or services at a specified price. Simpler than a subcontract — typically no labor/scope-of-work component. Tracks what was ordered, from whom, at what cost. [UCC (Uniform Commercial Code) | High | Material PO, equipment rental PO, service PO]
  - In Procore, POs are commitments with a different type classification. The workforce.materials_purchase_order table would add detailed PO data when ready.
- **Prime Contract** (`cp-prime-contract`): Agreement between the project owner and the general contractor or CM. The top-level commercial agreement that defines the overall project price, scope, schedule, and terms. All subcontracts flow down from this. [AIA A101/A102/A103 | Low | Lump sum, GMP, cost-plus, design-build, CM-at-risk, IPD]
  - Prime contract data in Procore is sparse. Most GCs track prime contract terms in their ERP or contract management system, not Procore.
- **Master Service Agreement** (`cp-master-service`): Standing agreement with a vendor or subcontractor that covers multiple projects or a defined time period. Sets standard terms so individual project work orders can be issued without full contract negotiation each time. [AGC | None | Annual MSA, multi-project MSA, vendor blanket PO]
  - MSAs are an enterprise procurement tool — most common on large programs or with repeat subcontractors. Procore's project-centric model doesn't support cross-project agreements.

**Contract Terms & Exhibits**
- **Scope of Work** (`cp-scope-work`): Detailed description of contracted work — defines what the subcontractor or vendor is responsible for delivering. May reference drawings, specifications, and schedule. The single most important exhibit to any construction contract. [AIA A201 | Low | Division-based scope (03 Concrete, 09 Finishes), activity-based scope, area-based scope]
  - Scope of work is almost always a PDF/Word attachment, not structured data. NLP on commitment descriptions is the best path to scope classification.
- **General Conditions** (`cp-gen-cond`): The standard legal and administrative terms that apply to all contracts on a project — defines roles, responsibilities, dispute resolution, insurance requirements, and procedural obligations. The 'rules of the game' for the project. [AIA A201 (General Conditions) | None | AIA A201, ConsensusDocs 200, modified/supplementary conditions, owner-specific]
  - GCs and owners negotiate supplementary conditions that modify the standard AIA or AGC terms. These modifications define the actual risk allocation.
- **Retainage Terms** (`cp-retainage-terms`): Contractual provision specifying the percentage of each payment withheld until substantial completion or final acceptance. Protects the owner/GC against incomplete or defective work. Typically 5-10% of contract value. [AIA A201 (9.3.1) | Medium | 5% standard, 10% on first 50% then 0%, graduated release, 0% (waived)]
  - Retainage rules vary by state law. Some states cap retainage at 5%. Financial detail (actual retainage amounts) lives in Financial Instruments domain.
- **Liquidated Damages** (`cp-liquidated-damag`): Pre-agreed daily or milestone-based financial penalty for late completion. Establishes the cost of delay without requiring the owner to prove actual damages. A critical risk term that drives schedule urgency. [AIA A201 (4.3) | None | $500-$50,000/day depending on project size and type. Milestone-based LDs for phased projects.]
  - LDs create strong incentive alignment but are almost never tracked in construction PM systems. LD exposure is computed from contract terms × schedule variance.
- **Allowance** (`fi-allowance`): A budgeted amount included in the contract for work that cannot be fully defined at contract execution. Spent against actual costs as scope is clarified. Commonly used for concealed conditions, owner selections, or design development items. [AIA A201 (3.8) | Medium | Owner selection allowance, concealed condition allowance, design development allowance, testing allo]
  - Allowances are a financial planning tool detailed in Financial Instruments. Listed here for the commercial/contractual context — they define where scope risk is allocated.

**Surety & Insurance**
- **Bid Bond** (`cp-bid-bond`): A surety bond submitted with a bid guaranteeing the bidder will enter into the contract at the bid price if awarded. Typically 5-10% of bid amount. Protects the owner against bidders who withdraw after bid opening. [Miller Act (federal) | None | 5% of bid amount (standard), 10% on public work]
  - Required on virtually all public work. Private owners may waive bid bonds for prequalified contractors.
- **Performance Bond** (`cp-perf-bond`): Surety guarantee that the contractor will complete the work per contract terms. If the contractor defaults, the surety must complete the work or compensate the owner. Typically 100% of contract value. [Miller Act | None | 100% of contract value (standard), partial bonds on private work]
  - Performance bonds are required on all federal projects >$150K and most public projects. Private owners increasingly require them on large projects.
- **Payment Bond** (`cp-payment-bond`): Surety guarantee that the contractor will pay subcontractors, suppliers, and laborers. Protects the project from mechanic's liens filed by unpaid parties. Typically 100% of contract value. [Miller Act | None | 100% of contract value (standard)]
  - Payment bonds replace mechanic's lien rights on public projects (where liens can't attach to government property). On private work, subs have both lien rights and bond claims.
- **Insurance Certificate** (`cp-insurance-cert`): Proof of insurance coverage — documents that the contractor carries required general liability, workers' comp, auto, umbrella, and builders risk coverage. Verified before work begins and tracked throughout the project. [ACORD forms (25, 28) | High | GL ($1M/$2M), WC (statutory), auto ($1M), umbrella ($5-10M), builders risk, professional liability]
  - Procore has structured insurance tracking with expiration dates, coverage amounts, and compliance status. One of the stronger procurement data sets in the platform.
- **Builders Risk** (`cp-builders-risk`): Insurance policy covering physical loss or damage to the building under construction. Typically carried by the owner or GC and covers all parties. Separate from the contractor's general liability. [AIA A201 (11.3) | None | Project value-based premium, named perils vs. all-risk, deductible structures]
  - Builders risk is a project-level policy, not per-contractor. Claims (fire, water damage, theft, weather) are major project risk events but tracked outside PM software.

**Warranty & Closeout**
- **Warranty** (`cp-warranty`): Post-construction guarantee that work will be free from defects for a specified period. Standard is 1 year from substantial completion; extended warranties apply to specific systems (roofing: 20 years, HVAC: 5 years, waterproofing: 10 years). [AIA A201 (3.5, 12.2) | Low | 1-year general, 2-year mechanical, 5-year HVAC, 10-year structural, 20-year roofing]
  - Warranty management is a major gap in construction PM systems — most tracking happens in facility management or spreadsheets after project closeout.
- **Substantial Completion** (`cp-substantial-comp`): The milestone when the project is sufficiently complete for the owner to occupy and use for its intended purpose. Triggers warranty start dates, retainage release, and final completion punchlist. A contractual — not just physical — milestone. [AIA A201 (9.8) | Medium | Certificate of Substantial Completion (AIA G704), punch list issuance, owner occupancy]
  - Substantial completion is the most important contractual milestone — it shifts risk, starts warranties, and triggers final payments. Often contested.
- **Final Completion** (`cp-final-completion`): The point at which ALL contract work is complete — all punch items resolved, all closeout documents delivered, all training completed. Triggers final retainage release and contract closeout. The true end of the project. [AIA A201 (9.10) | Medium | Final payment application, consent of surety, all closeout docs delivered]
  - The gap between substantial and final completion is often months. Long gaps signal poor closeout management and create retainage/lien exposure.

**Compliance Documents**
- **Prevailing Wage Certification** (`cp-prevailing-wage`): Documentation proving that workers on public projects are paid at or above the locally determined prevailing wage rate. Required on federal (Davis-Bacon) and most state public work. Submitted with each pay period. [Davis-Bacon Act | Medium | Certified payroll reports, WH-347 forms, apprenticeship ratios, fringe benefit statements]
  - Prevailing wage enforcement is increasing. Non-compliance results in fines, contract termination, and debarment. Procore tracks compliance docs but not payroll detail.
- **Diversity / DBE Certification** (`cp-diversity-dbe`): Documentation of participation by disadvantaged, minority, women-owned, veteran-owned, or small businesses. Required on most public projects and increasingly on private work. Tracked as percentage of contract value. [FAR (federal) | Low | DBE, MBE, WBE, SDVOSB, HUBZone, Section 3, local hire]
  - Diversity requirements are growing in both public and private sectors. Most tracking is manual — spreadsheets and compliance portals. Major automation opportunity.
- **Closeout Document Package** (`cp-closeout-doc`): The collection of documents required for project handover — as-builts, O&M manuals, warranties, training records, commissioning reports, and final lien waivers. The deliverable set that closes out the contract. [AIA A201 (9.10) | Medium | As-built drawings, O&M manuals, warranty letters, test reports, training records, attic stock, spare]
  - Closeout is universally hated in construction — it's administrative work after the exciting part is done. Completion tracking is the key metric.

**Standard Measures**
- **Bid Coverage Rate** (`cp-bid-coverage`): Percentage of project scope (by value) that was competitively bid vs. sole-sourced or negotiated. Formula: SUM(competitively_bid_contract_value) / total_contract_value. Higher rate = more price discovery. [AGC | None | 60-90% competitively bid on hard-bid projects, 40-70% on negotiated/CM projects]
  - Hard-bid projects approach 100% coverage. CM/GC and design-build projects have lower bid coverage because scopes are negotiated.
- **Average Bidders per Package** (`cp-average-bidders`): Mean number of competing proposals received per bid package. Formula: AVG(bidders_per_package). More bidders = more price competition and market depth. [AGC | None | 3-5 bidders typical, <3 signals tight market, >6 signals commodity scope]
  - Low bidder counts may indicate: market overheating, overly restrictive prequalification, unclear scope, or poor bid timing.
- **Award Cycle Time** (`cp-award-cycle-time`): Mean elapsed time from bid opening to contract execution. Formula: AVG(contract_date - bid_due_date). Shorter cycles get subs mobilized faster and reduce price escalation risk. [AGC | None | 2-4 weeks (simple), 4-8 weeks (complex/negotiated), 8-12+ weeks (public/federal)]
  - Long award cycles create risk: subcontractors may withdraw bids, material prices escalate, and schedule slips. Track from bid due date to NTP.
- **Insurance Compliance Rate** (`cp-insurance-comp`): Percentage of active subcontractors with current, compliant insurance certificates. Formula: COUNT(compliant_vendors) / COUNT(active_vendors). Below 100% = uninsured work exposure. [AIA A201 | High | 95-100% target, <90% is a red flag]
  - Procore has structured insurance data with expiration tracking. This is one of the most computable procurement metrics in the platform.
- **Change Order Rate** (`fi-chg-order-rate`): Ratio of total change order value to original contract value. Formula: SUM(CO_value) / original_contract_value. Higher rate = more scope change, design issues, or unforeseen conditions. [AACE | High | 5-10% typical, >15% signals problems, <3% may signal under-scoping]
  - This metric also appears in Financial Instruments (cost perspective). Here it's the contractual perspective — which contracts generate the most change.
- **Subcontractor Retention Rate** (`cp-sub-retention`): Percentage of subcontractors used on previous projects that are re-engaged on new projects. Formula: COUNT(repeat_subs) / COUNT(total_subs). Higher rate = stronger trade partner relationships. [AGC (partnering standards) | Medium | 40-60% typical for large GCs, >70% for relationship-focused builders]
  - Repeat subcontractors tend to have lower deficiency rates and fewer change orders. Cross-reference with quality and financial metrics.

### Documents & Communications

**Design & Construction Documents**
- **Drawing Set** (`doc-drawing-set`): Complete package of design documents issued for a project phase — architectural, structural, MEP, civil, landscape sheets organized by discipline and numbered by convention. Issued at milestones (SD, DD, CD, IFC, As-Built). [AIA E202 (BIM Protocol), AIA G702, NCS (National CAD Standard), US National BIM  | High | Schematic Design (SD), Design Development (DD), Construction Documents (CD), Issued for Construction]
  - Drawing sets are the primary REFERENCES target — RFIs, submittals, observations, and punch items all reference specific drawing sheets. VERSIONED_AS relationship tracks revision history.
- **Drawing Sheet** (`doc-drawing-sheet`): Individual sheet within a drawing set — identified by discipline prefix and sheet number (e.g., S-301, M-201, A-102). Contains plan views, sections, details, schedules, and notes for a specific scope. [NCS (sheet numbering convention), AIA CAD Layer Guidelines | High | Architectural (A-series), Structural (S-series), Mechanical (M-series), Electrical (E-series), Plumb]
  - Sheets are what RFIs reference (drawing_number field on rfis). Most granular unit of design documentation. ATTACHED_TO locations via plan markups.
- **Drawing Revision** (`doc-drawing-revision`): A new version of a drawing sheet issued to correct errors, incorporate changes, or add information. Tracked by revision number (Rev A, Rev B, or numeric) with a revision date and description of changes. Each revision supersedes the prior version. [AIA standard revision tracking, NCS revision block format | High | Rev 0 (original issue), Rev A/B/C or Rev 1/2/3, Addendum revisions, Bulletin revisions, ASI revision]
  - VERSIONED_AS relationship. Post-IFC revisions almost always generate change orders — high correlation with cost growth. ORIGINATED_FROM design changes, ASIs, or RFI responses.
- **Specification Section** (`sc-specification-se`): Written document defining material, product, and installation requirements for a specific scope of work — organized by CSI MasterFormat division and section number. Contains Part 1 (General), Part 2 (Products), Part 3 (Execution). [CSI MasterFormat (50 divisions), CSI SectionFormat (3-part structure), ASTM refe | Medium | Division 03 30 00 Cast-in-Place Concrete, Division 05 12 00 Structural Steel, Division 08 44 00 Curt]
  - GOVERNS materials and installation quality. Submittals are organized by spec section (specification_section_id on submittals). RFIs often reference spec sections.
- **Addendum** (`doc-addendum`): Formal modification to bidding or contract documents issued before contract execution — changes drawings, specs, or bid conditions. Numbered sequentially (Addendum 1, 2, 3). [AIA A701 (Instructions to Bidders), AIA A201 (General Conditions §1.1) | Low | Addendum 1, 2, 3]
  - SUPERSEDES prior bid document versions. Addenda volume during bidding indicates design completeness. High addendum count = design not ready for bidding. BECOMES contract document upon execution.
- **Bulletin / Architect's Supplemental Instruction (ASI)** (`doc-bulletin-archite`): Post-contract design clarification or minor change issued by the architect that does not change the contract sum or time. ASIs modify drawings or specs to clarify intent, correct minor errors, or adjust details. [AIA G710 (Architect's Supplemental Instructions) | Low | ASI-001, ASI-002]
  - Contentious document type: GCs argue ASIs that affect cost should be change orders. ORIGINATED_FROM design review or field conditions. TRIGGERS drawing revisions. Cost impact disputes are common.

**Requests & Clarifications**
- **Request for Information (RFI)** (`doc-req-info-rfi`): Formal question from the contractor to the design team requesting clarification on drawings, specs, or design intent. RFIs have a structured lifecycle: initiated → assigned → responded → closed/accepted. [AIA G716 (Request for Information), ConsensusDocs 200 | High | Open, Closed, Draft, Overdue]
  - The strongest structured document signal in Procore. predicted_topic enables zero-NLP topic classification. ORIGINATED_FROM design ambiguity or field conditions.
- **RFI Response** (`doc-rfi-response`): Formal answer to an RFI from the design team — provides the clarification, direction, or decision requested. May include supplementary sketches, revised details, or references to existing drawings. Response status (official vs. [AIA G716 | High | Official response, Preliminary response, Follow-up response]
  - RESPONDS_TO the RFI question. Response quality affects downstream work — vague responses generate follow-up RFIs. Late responses delay construction.
- **Request for Proposal (RFP) / Pricing Request** (`doc-req-proposal-rfp`): Formal request from GC to subcontractor or supplier for pricing on a change, additional work, or alternate scope. Not the same as a bid-phase RFP — this is a construction-phase pricing exercise. [No universal standard | Medium | RFP for change pricing, T&M request, Unit price request, Alternate pricing]
  - LINKED_TO change events. The response (quote) feeds into change event line items for cost estimation. ASSIGNED_TO subcontractors for their scope. Pricing velocity affects change management cycle time.

**Submittals & Approvals**
- **Submittal** (`doc-submittal`): Formal submission of product data, shop drawings, samples, or other documentation to the design team for review and approval before procurement or installation. Every specified material requires a submittal. [CSI standards, AIA A201 §3.12 (Shop Drawings, Product Data, Samples), spec secti | High | Approved, Approved as Noted, Revise and Resubmit, Rejected, Submitted, Under Review, Draft, Closed]
  - The primary material and product documentation pathway. Submittal titles are the strongest material signal in Procore — every material is specified through a submittal.
- **Submittal Response / Review** (`doc-submittal-respon`): The design team's review action on a submittal — approve, approve as noted, reject, or revise and resubmit. Reviewer markups on shop drawings are binding design modifications. [AIA A201 §4.2.7 (Review of Submittals) | High | Approved, Approved as Noted, Rejected, Revise and Resubmit, No Exception Taken, Make Corrections Not]
  - RESPONDS_TO the submittal. Review duration is a key schedule metric — slow reviews delay procurement. Multiple reviewer chains (sub → GC → architect → engineer) compound delay.
- **Shop Drawing** (`doc-shop-drawing`): A subcontractor-prepared or fabricator-prepared detailed drawing showing dimensions, connections, materials, and fabrication details for their specific scope — submitted for design team review. [AIA A201 §3.12, AISC Code of Standard Practice (steel), PCI (precast) | High | Structural steel connection details, Curtain wall anchor layouts, Precast panel elevations, Mechanic]
  - TYPED_AS a submittal. Shop drawings are where design errors surface — discrepancies between design drawings and shop drawings generate RFIs. Steel shop drawings are typically critical path.
- **Product Data Submittal** (`doc-product-data`): Manufacturer's published literature, cut sheets, performance data, and test reports submitted to demonstrate that a specific product meets specification requirements. [CSI submittals classification, ASTM/UL/FM test standards referenced in specs | High | Fixture cut sheets, Equipment performance data, Material safety data sheets (SDS), Manufacturer warr]
  - TYPED_AS a submittal. Product data drives the procurement pipeline — approved product data triggers purchase orders. SPECIFIES the exact product that will be installed.
- **Sample Submittal** (`doc-sample-submittal`): Physical material sample submitted for design team review and approval — colors, textures, finishes, and material quality. Includes mockup panels, paint samples, flooring tiles, stone selections, hardware finishes. [AIA A201 §3.12 (Samples) | Medium | Paint color samples, Flooring samples, Stone/tile samples, Hardware finish samples, Curtain wall moc]
  - TYPED_AS a submittal. Samples are the quality standard — field work is accepted or rejected based on approved sample. Mockup panels for exterior enclosure are expensive and schedule-critical.

**Correspondence & Notices**
- **Correspondence** (`doc-correspondence`): Formal written communication between project parties — letters, emails tracked as project records, and notices that require acknowledgment or response. Correspondence types are configurable per project (letters, notices, memos, transmittals). [AIA A201 (various notice provisions), contract-specific notice requirements | High | Letter, Notice, Memo, Transmittal, Email (tracked), Owner Directive, Claim Notice, Delay Notice, Cha]
  - Correspondence is the contractual communication backbone. Delay notices, claim notices, and change directives have legal significance. DOCUMENTS project decisions and directives.
- **Transmittal** (`doc-transmittal`): Cover document accompanying a package of drawings, specifications, submittals, or other documents sent between parties. Records what was sent, to whom, when, and for what purpose (for review, for approval, for information, for construction). [AIA G810 (Transmittal Letter) | Medium | For Review, For Approval, For Information, For Construction, For Record, As Requested]
  - CONTAINS document references. The metadata layer on document distribution. Being replaced by digital distribution (Procore's built-in document sharing) but still contractually required on many project...
- **Notice of Delay** (`doc-notice-delay`): Formal written notification that a delay event has occurred or is anticipated — required by most contracts within a specified timeframe (often 7-14 days) to preserve delay claim rights. [AIA A201 §15.1.6 (Claims for Additional Time), ConsensusDocs 200 §6.3 | Low | Weather delay notice, Material delay notice, Owner-caused delay notice, Design delay notice, Force m]
  - Contractually critical — late notice can waive claims. TRIGGERED_BY delay events (daily_log_delay). BECOMES basis for time extension requests and change orders.
- **Change Directive / Construction Change Directive (CCD)** (`doc-chg-directive`): Owner-issued directive requiring the contractor to proceed with changed work before the cost and time impact is agreed upon. Used when urgency prevents waiting for a negotiated change order. [AIA A201 §7.3 (Construction Change Directives), AIA G714 | Low | CCD-001, CCD-002]
  - Contentious document — contractor must comply but may dispute cost. TRIGGERS change events. ORIGINATED_FROM owner or design team. BECOMES negotiated change order when cost/time is agreed.

**Meeting Records**
- **Meeting** (`doc-meeting`): Formally scheduled project meeting with defined attendees, agenda, and documented outcomes. Meetings are the primary decision-making forum on construction projects. [No universal standard | High | OAC Meeting, Progress Meeting, Coordination Meeting, Safety Meeting, Preconstruction Meeting, Subcon]
  - Meetings are where DOCUMENTS relationship is strongest — meeting minutes document decisions, commitments, and action items. CONTAINS meeting items (agenda/action items).
- **Meeting Minutes / Meeting Item** (`doc-meeting-minutes`): Individual agenda item or action item within a meeting — captures topic, discussion, responsible party, due date, and status. Meeting items carry forward between meetings (rolling action item log). [AIA G712 (Project Meeting Minutes form) | High | Open, Closed, In Progress, Carried Forward]
  - ASSIGNED_TO responsible parties for action. Action items that stay open across multiple meetings signal blocked issues.

**Field Communications**
- **Daily Report / Daily Log** (`doc-daily-report`): Comprehensive daily site record compiled by the superintendent or project engineer — combines weather, manpower, equipment, deliveries, visitors, delays, notes, safety violations, and work performed into a single daily project narrative. [No universal standard | High | One report per project per day]
  - The richest daily data source in construction. DOCUMENTS field activity for every project day. daily_log_delay.delay_type is a structured enum (Weather, Material, Safety, etc.).
- **Daily Log Note** (`fo-daily-log-note`): Free-text field observation entered as part of the daily log — captures site conditions, work progress, issues, coordination problems, or any noteworthy event that doesn't fit structured log categories. Notes may be flagged as issue days. [No standard | High | Free-text observations]
  - Primary NLP signal source. Keywords in daily log notes identify rework (~130K records), material shortages (0.09% hit rate for 'shortage'), design issues, and schedule concerns.
- **Site Instruction** (`doc-site-instruction`): Written directive from the GC superintendent or project manager to a subcontractor or crew — directs specific field action. Site instructions address means and methods, sequence changes, safety corrections, or quality requirements. [No universal standard | Medium | Directive to correct work, Sequence change, Safety correction, Access restriction, Work area assignm]
  - ASSIGNED_TO subcontractors. ORIGINATED_FROM field conditions, safety concerns, or coordination issues. If a site instruction changes scope, it may TRIGGER a change event.
- **Phone Call Log** (`doc-phone-call-log`): Record of field phone calls tracked as part of the daily log — documents who called whom, subject, and outcome. Captures communications that don't have a formal paper trail. [No standard | Medium | Caller, recipient, subject, notes, date/time]
  - Declining in relevance as text/email replaces phone calls. Still used on some projects to document verbal directions. DOCUMENTS verbal communications that may have contractual significance.
- **Plan Revision Notice** (`doc-plan-revision`): Field-level record that a new drawing revision has been received and acknowledged on the jobsite. Ensures the construction team is working from current documents. [No standard | Medium | Drawing number, revision number, date received, distributed to]
  - LINKED_TO drawing_revision records. Ensures field teams are working from current documents. Late distribution of revised drawings is a common cause of rework. FOLLOWS the drawing revision event.

**Action Plans & Tasks**
- **Action Plan** (`qsr-action-plan`): Structured set of tasks with assignments, due dates, and completion tracking — used for punch list management, commissioning tasks, closeout activities, safety action items, or any coordinated work sequence. [No universal standard | High | Punch List Action Plan, Commissioning Action Plan, Safety Corrective Action Plan, Closeout Action Pl]
  - CONTAINS action plan line items. Action plans are the execution layer that converts identified issues (observations, punch items, inspection deficiencies) into tracked remediation work.
- **Action Plan Line Item (Task)** (`qsr-action-plan-line`): Individual task within an action plan — a specific work item assigned to a responsible party with a due date and status. [No standard | High | Not Started, In Progress, Complete, Blocked]
  - ASSIGNED_TO responsible parties. LINKED_TO source records (the observation, punch item, or deficiency that created the task). The task is the atomic unit of tracked remediation work.
- **Project Task** (`doc-project-task`): General-purpose task tracked at the project level — not tied to an action plan. Used for ad-hoc work items, reminders, and assignments that don't fit the formal action plan structure. Lighter weight than action plan tasks but less structured. [No standard | Medium | Open, Complete]
  - Simpler than action plan line items. Used for ad-hoc coordination. Less cross-referencing to other project records.

**Visual Documentation**
- **Photo** (`doc-photo`): Photograph documenting site conditions, work progress, quality issues, safety hazards, or installed work. Photos are attached to locations, observations, inspections, daily logs, and punch items. [No standard | High | Progress photos, Quality documentation, Safety hazard, Pre-existing condition, Punch item photo, Ins]
  - ATTACHED_TO nearly every other document type (observations, punch items, inspections, daily logs). Photos are the visual evidence layer — they prove conditions at a point in time.
- **Video** (`doc-video`): Video recording of site conditions, work-in-progress, or safety events. Increasingly used for progress documentation (time-lapse), drone flyovers, quality recording (concrete pours, waterproofing installation), and safety incident documentation. [No standard | Low | Progress time-lapse, Drone flyover, Work-in-progress recording, Safety event recording, Quality docu]
  - Growing in importance with drone and 360-camera adoption. DOCUMENTS conditions with richer context than photos. CAPTURED_BY drones, 360 cameras, or body cameras.

**Regulatory & Compliance Documents**
- **Permit Application / Building Permit Record** (`doc-permit-applicati`): Documentation submitted to and received from regulatory authorities — building permit applications, permit issuance records, permit conditions, and inspection cards. Tracks permit status from application through issuance. [IBC (International Building Code), local building codes, local permit applicatio | Low | Applied, Under Review, Approved, Issued, Conditional, Expired]
  - DEPENDS_ON design document completion. ENABLES construction activities. Permit conditions may restrict work hours, noise, traffic, or require specific inspections. GOVERNS what can be built.
- **Certificate of Insurance (COI)** (`doc-cert-insurance`): Proof of insurance coverage provided by a subcontractor, vendor, or other project party — verifies they meet the contractual insurance requirements (general liability, workers' comp, auto, umbrella, builders risk). [ACORD 25 (Certificate of Liability Insurance), ACORD 28 (Evidence of Property In | High | General Liability, Workers Compensation, Auto Liability, Umbrella/Excess, Builders Risk, Professiona]
  - REQUIRED_BY contract terms. COI compliance is a precondition for site access. LINKED_TO vendors/subcontractors.
- **Lien Waiver** (`fi-lien-waiver`): Legal document in which a contractor, subcontractor, or supplier waives their right to file a mechanic's lien against the property — exchanged with payment. [State-specific lien waiver statutes (e.g., California Civil Code §8132-8138), AI | High | Conditional Progress, Unconditional Progress, Conditional Final, Unconditional Final]
  - BILLED_AGAINST payments — exchanged with each payment cycle. Missing lien waivers can block final payment and retainage release. A major closeout bottleneck.
- **Safety Plan / Site Safety Documentation** (`doc-safety-plan-site`): Project-specific safety plan defining hazard controls, emergency procedures, PPE requirements, and safety protocols. Required by OSHA and most contracts. [OSHA 29 CFR 1926 (Construction Safety Standards), ANSI/ASSP Z590.3 (Prevention t | Low | Site-Specific Safety Plan, Job Hazard Analysis (JHA), Activity Hazard Analysis (AHA), Fall Protectio]
  - GOVERNS safety procedures. The safety plan is the standard against which safety observations and violations are measured. COMPLIES_WITH OSHA regulations.
- **SWPPP / Environmental Compliance Document** (`doc-swppp-enviro`): Stormwater Pollution Prevention Plan and related environmental compliance documentation — required by EPA and state environmental agencies for construction sites disturbing 1+ acre of soil. [EPA NPDES Construction General Permit, Clean Water Act §402, state stormwater pr | None | SWPPP, Erosion Control Plan, Spill Prevention Plan, Dust Control Plan, Dewatering Plan, Environmenta]
  - GOVERNS environmental compliance on site. COMPLIES_WITH EPA and state environmental regulations. Regular inspections required (typically weekly + after rain events).

**Closeout Documents**
- **Punch List (as Document)** (`doc-punch-list-as`): Formal list of deficiencies and incomplete work items that must be corrected before the owner accepts the project — compiled during substantial completion walkthrough. [AIA A201 §9.8 (Substantial Completion), AIA G704 (Certificate of Substantial Com | High | Combined punch list document]
  - The punch list document is a COMPILATION of individual punch item records. PRECEDES certificate of substantial completion. Punch list closure is a contract milestone.
- **As-Built Documentation** (`ph-asbuilt`): Marked-up drawings and records showing the actual constructed conditions — deviations from design documents, field modifications, and final installed locations of all systems. As-built documentation is a contractual closeout deliverable. [AIA A201 §3.11 (Documents at the Site), contract-specific as-built requirements | Low | As-built drawings (redline markups), Record drawings (architect-revised from as-builts), BIM as-buil]
  - As-built documentation is a major closeout bottleneck — subcontractors are slow to provide markups. DOCUMENTS final constructed conditions. VERSIONED_AS the final drawing revision.
- **O&M Manual (Operations & Maintenance)** (`doc-o-m-manual`): Compiled documentation of all installed equipment and systems — manufacturer manuals, maintenance schedules, warranty information, spare parts lists, and operating procedures. Required closeout deliverable for building handover. [AIA A201 §9.10 (Final Completion), spec section 01 78 00 (Closeout Submittals) | Medium | Equipment O&M manuals, Maintenance schedules, Warranty certificates, Spare parts lists, System opera]
  - TYPED_AS closeout submittals. O&M manuals are the owner's primary reference for facility operations. Incomplete O&M documentation is a common punchlist and retainage holdback item.
- **Warranty Documentation** (`doc-warranty-docs`): Written guarantees from manufacturers, subcontractors, and the GC covering defects in materials and workmanship for a specified period after substantial completion. [AIA A201 §3.5 (Warranty), spec section 01 78 36 (Warranties), manufacturer-speci | Low | 1-year general warranty, 2-year MEP warranty, 5-year roofing membrane warranty, 10-year structural w]
  - GOVERNS post-completion quality obligations. Warranty claims TRIGGERED_BY defects found during the warranty period. LINKED_TO building elements and equipment.

**Forms & Templates**
- **Form / ProForma Form** (`doc-form-proforma`): Configurable structured form for data collection — checklists, inspection templates, safety forms, quality records, or any project-specific data collection need. [No industry standard for form structure | High | Safety checklists, Quality inspection forms, Pre-task plans, Hot work permits, Concrete pour cards, ]
  - Forms are the extensibility layer — they capture structured data that doesn't fit standard tools. DOCUMENTS any field activity or compliance check.
- **Daily Log Template** (`doc-daily-log`): Configurable template defining which daily log sections are required for a project — determines which daily log tables are populated. [No standard | Medium | Required sections, Optional sections, Hidden sections]
  - GOVERNS daily log data collection. Template standardization is the key to consistent daily data — projects without standardized templates have sporadic data in optional sections.

**Standard Measures**
- **RFI Response Time** (`doc-rfi-response-2`): Average elapsed time from RFI issuance to final response — measures design team responsiveness and information flow efficiency. Formula: Response Date − Issue Date (in calendar or business days). [CII benchmarking metrics | High | Typical range: 3–14 calendar days]
  - Ball-in-court tracking (rfis_bic) provides granular view of where time is spent. Response time is affected by RFI quality — vague RFIs take longer.
- **RFI Volume Density** (`doc-rfi-volume`): Total RFI count relative to project size — measures design completeness and coordination quality. Formula: Total RFIs / Project Value (per $M) or Total RFIs / Project SF. High RFI density suggests incomplete design documents or poor coordination. [CII benchmarking | High | Typical: 50–300 RFIs per $100M project]
  - RFI predicted_topic (176 ML-classified topics) enables subject-matter breakdown without NLP. High RFI volume in a discipline signals design gaps in that system.
- **Submittal Cycle Time** (`doc-submittal-cycle`): Average elapsed time from submittal submission to final approval — measures the review and approval efficiency for product data and shop drawings. Formula: Approval Date − Submission Date (in business days). Includes resubmission cycles. [CSI Practice Guide for Submittals | High | Typical: 10–21 business days first review]
  - Overdue submittals (submittals.overdue flag) are a direct material delay risk signal. Cycle time × number of resubmissions = total approval duration.
- **Submittal Rejection Rate** (`doc-submittal-reject`): Percentage of submittals rejected or returned for revision on first review — measures submittal preparation quality and design coordination. Formula: (Rejected + Revise & Resubmit) / Total Submittals × 100. [CSI submittal review categories | High | Typical: 15–30% rejection/revision rate]
  - Rejection rate by trade reveals which subcontractors need submittal preparation support. Resubmission count per submittal tracks rework in the documentation process.
- **Drawing Revision Frequency** (`doc-drawing-revision-2`): Average number of revisions per drawing sheet — measures design stability and change volume. Formula: Total Revisions / Total Drawing Sheets. Late-stage revisions (post-IFC) are a stronger signal of design instability than early-stage revisions. [NCS revision numbering conventions | High | Typical: 2–5 revisions per sheet over project life]
  - Post-IFC revisions are the most impactful — they drive RFIs, change orders, and rework. Revision frequency by discipline reveals which systems have the most design churn.
- **Daily Log Completion Rate** (`fo-daily-log-2`): Percentage of working days with a completed daily log entry — measures field reporting consistency. Formula: Days with Daily Log / Total Working Days × 100. Consistent daily logging is a prerequisite for field data quality. [Company-specific daily reporting requirements | High | Typical target: 95–100% of working days]
  - Daily log completion is the foundation for all field analytics — workforce hours, weather delays, material deliveries, safety incidents.
- **Correspondence Response Time** (`doc-correspondence-r`): Average elapsed time from correspondence issuance to response — measures communication efficiency between project parties. Formula: Response Date − Issue Date (in business days). [Contract-specified response periods | High | Typical: 3–10 business days depending on correspondence type]
  - Correspondence types (via correspondence_types table) enable segmentation by communication category. High correspondence volume with slow response signals communication breakdown.

### Field Operations

**Daily Log Framework**
- **Daily Log (Header)** (`fo-daily-log-header`): The parent record for all daily field data — one per project per day. Acts as the container that links all log sections (manpower, equipment, weather, delays, notes, etc.) to a single date and project. [No universal standard | High | One header per project per day]
  - The foundation of field operations data. A project with low log completion rates has unreliable field data across ALL sections. completion rate is the single best metric for field data quality.
- **Daily Log Section Configuration** (`fo-daily-log`): The template configuration that defines which log sections are required, optional, or hidden for a project. [No standard | Medium | Required, Optional, Hidden per section]
  - Template standardization is the single biggest lever for field data quality. Companies that mandate all sections get 3-5x more data per project.

**Field Notes & Communications**
- **Daily Log Note** (`fo-daily-log-note`): Free-text narrative entry by field personnel documenting site conditions, work progress, issues, and events — the superintendent's daily diary. Multiple notes may be entered per day by different team members. [No universal standard | High | Free text narrative]
  - The primary free-text signal source for NLP-based analysis. Keyword extraction hits ~0.09% for specific topics like material shortages.
- **Phone Call Log Entry** (`fo-phone-call-log`): Record of field-related phone calls — caller, recipient, subject, and notes. Documents verbal communications for the project record. [No universal standard | Medium | One entry per call]
  - Low individual analytics value but call patterns reveal communication dynamics. Frequent architect calls may indicate design issues.
- **Plan Revision Receipt** (`fo-plan-revision`): Field record of updated drawing revisions received on site — which drawings were updated, to what revision, and when the field team received them. Critical for confirming that construction crews are working from current documents. [AIA A201 (document distribution) | Medium | One entry per revision received]
  - Tracks WHEN the field received updated drawings — not the drawing content itself. Long receipt lags mean the field may be building from outdated drawings.

**Workforce & Labor**
- **Manpower Log Entry** (`fo-manpower-log`): Daily record of workforce on site by trade and vendor — captures trade name, number of workers, hours per worker, total man-hours, and the vendor/subcontractor responsible. One entry per trade per vendor per day. [No universal standard | High | One entry per trade/vendor/day]
  - The strongest trade-level signal in Procore. trade_name is free text — needs keyword normalization to canonical trades (e.g., 'Electricians' → 'Electrician'). Not all companies fill it consistently.
- **Construction Report Entry** (`fo-const-report`): Certified payroll and workforce diversity reporting record — tracks hours by worker classification (apprentice, journeyman, foreman) and demographic category (minority, women, veteran, local) per trade and vendor. [Davis-Bacon Act (federal prevailing wage), state prevailing wage statutes, local | High | One entry per vendor/trade/day]
  - Critical for public projects. Prevailing wage violations carry heavy penalties. Diversity tracking (minority hours, women hours, veteran hours) increasingly required on private projects too.
- **Timecard Entry** (`fo-timecard-entry`): Structured record of individual worker hours — employee, date, hours worked, cost code, project, overtime classification. More granular than manpower log (individual workers vs. crew-level). [FLSA (Fair Labor Standards Act), state labor laws, union agreements for overtime | None (Not Ready) | One entry per worker per day]
  - NOT READY for import. When available, timecards will be the authoritative source for labor cost and productivity at the individual worker level.
- **Employee Record** (`fo-employee-record`): Master record for a field worker — name, role, job title, trade classification, certifications, company assignment. The identity record that timecards, crew memberships, and workforce planning reference. [No universal construction standard | None (Not Ready) | Employee ID, name, job_title, company_id, trade classification, certification status]
  - NOT READY. When available, employee-level trade classification will be more reliable than inferring trade from manpower log free text.
- **Crew / Crew Membership** (`fo-crew-crew`): Grouping of workers into a named crew assigned to a specific scope of work — crew name, members, lead/foreman, trade, and assignment. Crews are the operational unit of field labor management. [No standard | None (Not Ready) | Crew name, crew lead/foreman, member list, trade, assigned scope/area]
  - NOT READY. Crew-level workforce planning is how superintendents actually think about labor — not individual workers. When available, links to workforce planning (assignments, requests).

**Equipment**
- **Equipment Log Entry** (`fo-equip-log-entry`): Daily record of equipment on site — equipment name, hours operating, hours idle, and inspection status. One entry per piece of equipment per day. Captures both utilization (operating vs. idle) and safety compliance (inspected flag, inspection_time). [OSHA 29 CFR 1926 Subpart N (Cranes), Subpart O (Motor Vehicles), Subpart P (Exca | High | One entry per equipment per day]
  - equipment_name is free text — needs keyword classification into canonical types (12 categories per Resources taxonomy: crane, excavator, loader, aerial lift, forklift, scaffolding, etc.).
- **Equipment Master Record** (`fo-equip-master`): Catalog record for a piece of equipment — type, model, serial number, capacity, ownership/rental status, maintenance schedule. The identity record for equipment that field logs, timecards, and maintenance records reference. [No universal standard | None (Not Ready) | Equipment ID, name, type, model, serial number, capacity, owner (company or rental), maintenance sta]
  - NOT READY. Currently, equipment identification relies on free-text equipment_name in daily_log_equipment.
- **Equipment Timecard Entry** (`fo-equip-timecard`): Structured time record for individual equipment — hours by category (operating, idle, maintenance, travel), cost allocation, and operator assignment. More granular than the daily equipment log (includes cost allocation and maintenance time). [No universal standard | None (Not Ready) | Equipment ID, date, hours by category, cost code, operator, project]
  - NOT READY. Currently, daily_log_equipment provides operating and idle hours at the day level. Equipment timecards would add cost allocation and more precise utilization tracking.

**Materials & Deliveries**
- **Delivery Log Entry** (`fo-dlvy-log-entry`): Daily record of materials received on site — contents description, delivery source, tracking number, time, and comments. One entry per delivery event per day. The contents field is a free-text description of what was delivered. [No universal standard | High | One entry per delivery/day]
  - contents field is free text describing what was delivered — the most direct material receipt signal in field operations.
- **Material Shipment Record** (`fo-mat-shipment`): Structured tracking of material shipments from supplier/fabricator to jobsite — shipment date, expected arrival, contents, quantity, and carrier. Tracks the supply chain between purchase order and site delivery. [No universal standard | None (Not Ready) | Shipment ID, PO reference, contents, quantity, ship date, expected arrival, carrier, tracking number]
  - NOT READY. Currently, delivery tracking relies on daily_log_delivery (what arrived) and submittals with required_on_site_date (what was expected).
- **Material Receipt Record** (`fo-mat-receipt`): Formal acknowledgment that materials arrived on site matching the purchase order — quantity verification, condition inspection, and storage location. More structured than the delivery log (which is a field observation). [No universal standard | None (Not Ready) | Receipt ID, PO reference, item, quantity ordered, quantity received, condition, storage location, re]
  - NOT READY. The delivery log is currently the only signal for material arrival. Structured receipt data would enable quantity verification and damage tracking.

**Weather**
- **Weather Log Entry** (`fo-weather-log`): Daily record of observed weather conditions on the project site — temperature, precipitation, wind, sky conditions, humidity, ground conditions, and whether weather caused a delay. Multiple readings may be taken throughout the day. [No universal standard | High | One entry per day (or multiple time periods)]
  - Richest weather dataset in construction software. Dual signal: qualitative superintendent observations + quantitative measured values.

**Delays**
- **Delay Log Entry** (`fo-delay-log-entry`): Record of a delay event during construction — structured type, duration, start/end time, comments, and location. Delay entries document when work was stopped or significantly slowed and why. [AACE 29R-03 (Forensic Schedule Analysis), AIA A201 §15.1.6 (Claims for Additiona | High | delay_type values (structured enum): Weather, Existing Conditions, Material, Owner Directive, Non-Co]
  - The strongest structured delay signal in Procore — delay_type is a structured enum requiring zero NLP.

**Productivity & Quantities**
- **Productivity Log Entry** (`fo-productivity-log`): Daily record of quantities delivered and used/installed — tracks material flow from delivery to installation by vendor and commitment line item. Captures previously_delivered, previously_used, quantity_delivered (today), and quantity_used (today). [No universal standard | Low | One entry per vendor/item/day]
  - Extremely low adoption (622 cos) limits benchmarking value. When populated, provides the strongest earned-value signal in field operations — directly links installed quantities to commitments.
- **Quantity Log Entry** (`fo-quantity-log`): Daily record of installed quantities by cost code — quantity, unit of measure, description, and cost code. Distinct from productivity log (which tracks vendor-level delivery and installation). [No universal standard | Medium | One entry per cost code/day]
  - More adoption than daily_log_productivity but still sporadic. cost_code linkage is the key value — enables quantity-based percent complete by budget line item.

**Safety**
- **Safety Violation Log Entry** (`fo-safety-violation`): Daily log record of a safety violation observed during field walkthroughs — subject, comments, issued_to (person or company), compliance_due date, and safety_notice type. [OSHA 29 CFR 1926 (Construction Safety Standards), company safety programs | Medium | One entry per violation/day]
  - Validated as UNUSABLE for recurrence tracking (insight #11) — subject 66% null, mostly noise. vendor_name is free text with no FK, preventing reliable trade attribution.
- **Accident Log Entry** (`fo-accident-log`): Daily log record of an accident or safety event — involved person, involved company, time, comments, and location. [OSHA 29 CFR 1904 (Recording and Reporting), OSHA 300/300A/301 forms | Medium | One entry per event/day]
  - Lightweight first report — the formal incident system (incident, incident_record, incident_action) provides the detailed analysis data including injury type, body part, recordability, and corrective a...

**Inspections**
- **Daily Log Inspection Entry** (`fo-daily-log-insp`): Inspection event recorded as part of the daily log — inspecting entity, inspection type, inspector name, start/end time, and comments. [Building code inspection requirements, OSHA, project specifications | Medium | One entry per inspection event/day]
  - Records the OCCURRENCE of an inspection, not the detailed results. The formal inspections tool (inspections + inspection_items) provides structured pass/fail with checklist items.

**Visitors**
- **Visitor Log Entry** (`fo-visitor-log`): Daily record of non-project visitors on the construction site — visitor identity, purpose, arrival/departure times, and comments. Required for site security, safety compliance (visitors must be briefed on site hazards), and liability documentation. [OSHA general duty clause (site safety for visitors), company safety policies, co | Medium | One entry per visitor/day]
  - Visitor patterns reveal project dynamics — frequent owner visits during finishes indicate engaged clients. Architect visit frequency correlates with design issue volume.

**Waste & Environmental**
- **Waste Log Entry** (`fo-waste-log-entry`): Daily record of construction waste generated and removed — material type, quantity, disposal method, disposal location, and vendor. Tracks what waste was produced, how much, and where it went. [LEED MR Credit (Construction Waste Management), EPA RCRA (hazardous waste), loca | Medium | One entry per waste event/day]
  - Increasingly important for sustainability reporting. LEED MR credit requires 50-75% waste diversion. material field describes the waste type — enables diversion analysis.
- **Dumpster Log Entry** (`fo-dumpster-log`): Daily record of dumpster activity — dumpsters delivered and removed from the site. Tracks the containers, not the waste contents (that's the waste log). Dumpster management is a general conditions cost item. [No standard | Medium | One entry per dumpster event/day]
  - Operational metric. High dumpster turnover during demolition and interior rough-in. Dumpster rental and hauling is a significant general conditions line item — typically $500-1,500 per pull.

**Scheduled Work**
- **Scheduled Work Log Entry** (`fo-scheduled-work`): Daily record of subcontractors scheduled to work — whether they showed up, how many workers, hours, and what tasks they were assigned to. The 'showed' boolean is the simplest plan-vs-actual signal in field operations. [No universal standard | High | One entry per vendor/day]
  - The showed boolean is the Last Planner System's 'PPC' (Percent Plan Complete) equivalent — did the scheduled work happen? No-show rate by vendor is a reliability signal.
- **Scheduled Work Task Link** (`fo-scheduled-work-2`): Junction record linking a scheduled work entry to one or more CPM schedule tasks — the bridge between 'what was planned today' (daily log) and 'what the schedule says' (CPM). [No standard | High | One entry per task per scheduled work entry]
  - The critical bridge between field operations and schedule. schedule_task_id links directly to schedule_task (legacy) or scheduling_activity (new).

**Field Productivity Measurement**
- **Field Productivity Record** (`fo-field-productivi`): Structured measurement of field production — actual quantities produced vs. planned, by trade and activity. [No universal standard | None (Not Ready) | Crew, activity, planned quantity, actual quantity, unit, variance, notes]
  - NOT READY. Currently, productivity must be inferred from daily_log_manpower (man-hours) + daily_log_quantity (installed quantities) + daily_log_productivity (vendor quantities).
- **Actual Production Quantity** (`fo-actual-productio`): Recorded measurement of work actually completed — the 'actuals' side of earned value. Tracks what was installed in the field, by scope item, providing the physical percent complete that drives payment and forecasting. [PMI PMBOK (Earned Value Management), AACE | None (Not Ready) | Scope item, quantity completed, unit, measurement date, measured by]
  - NOT READY. When available, this is the authoritative 'what was actually built' signal. Currently, daily_log_quantity is the closest approximation.
- **Budgeted Production Quantity** (`fo-budgeted-product`): Planned quantity for a scope item — the 'budget' side of production tracking. Defines how much work is expected to be installed, creating the baseline for earned-value comparison. [PMI PMBOK, AACE | None (Not Ready) | Scope item, budgeted quantity, unit, source (estimate, schedule, budget)]
  - NOT READY. When available, budget vs. actual production quantities enable true earned value at the field measurement level.

**Time & Material Tracking**
- **T&M Ticket** (`fo-t-m-ticket`): Time and material ticket documenting extra work performed outside the base contract — captures labor hours, equipment hours, and materials used for change work or disputed scope. [AIA A201 §7.1.3 (for cost-plus changes), contract-specific T&M provisions | None (Not Ready) | One ticket per day per extra work item]
  - NOT READY. T&M tracking is a major pain point — disputed T&M tickets are a top source of claims. Currently tracked via paper, email, and Excel on most projects.
- **T&M Labor Entry** (`fo-t-m-labor-entry`): Labor portion of a T&M ticket — worker classification, hours, rate, and total labor cost. Multiple labor entries per ticket (different workers, different rates). [Contract schedule of rates, prevailing wage (if applicable) | None (Not Ready) | Worker, classification, hours (regular, OT, DT), rate, total, date]
  - NOT READY. Labor is typically the largest component of T&M costs.
- **T&M Equipment Entry** (`fo-t-m-equip-entry`): Equipment portion of a T&M ticket — equipment type, hours, rate, and total equipment cost. Equipment rates follow the contract schedule or industry published rates (Blue Book, FEMA). [Blue Book rental rates, FEMA equipment rates, contract-specific rates | None (Not Ready) | Equipment type, hours, rate, total, date]
  - NOT READY. Equipment rates are often disputed — Blue Book vs. actual rental cost.
- **T&M Material Entry** (`fo-t-m-mat-entry`): Material portion of a T&M ticket — material description, quantity, unit cost, and total material cost. Materials must be documented with receipts or invoices. Markup on materials is governed by contract terms (typically 10-15% overhead and profit). [Contract markup provisions | None (Not Ready) | Material, quantity, unit cost, total, receipt/invoice reference]
  - NOT READY. Material costs on T&M tickets require receipt documentation for audit.

**Workforce Planning**
- **Assignment** (`fo-assignment`): Allocation of a worker or crew to a specific project for a date range — the workforce planning layer above daily manpower logs. Assignments represent the planned labor allocation; manpower logs record the actual. [No standard | None (Not Ready) | Worker/crew, project, start date, end date, role, trade]
  - NOT READY. When available, planned vs. actual workforce comparison enables capacity planning and identifies understaffing/overstaffing.
- **Workforce Request** (`fo-workforce-req`): Request for additional workers or specific trades — submitted by field teams to the home office or labor pool. Tracks the demand signal for labor that may not yet be assigned. Request status (open, filled, unfilled) indicates workforce availability. [No standard | None (Not Ready) | Trade requested, quantity, project, date needed, urgency, status (open, filled, unfilled)]
  - NOT READY. Workforce requests are the leading indicator of labor shortages. Unfilled requests = constraint on schedule execution.

**Field Reporting & Distribution**
- **Daily Report Distribution** (`fo-daily-report`): The act of sending the completed daily log to stakeholders — tracks who received the compiled report, when it was distributed, and by whom. Distribution is a formal project management action — it makes the daily log an official project record. [Contract-specific distribution requirements | High | Distributed to: owner, architect, GC home office, project team]
  - Distribution rate is a project management discipline metric. Logs completed but not distributed have less contractual weight.

**Standard Measures**
- **Daily Log Completion Rate** (`fo-daily-log-2`): Percentage of project days with completed daily logs — completed logs / total project days × 100. The single best metric for field data quality across all sections. Projects below 80% completion rate have unreliable field data. [No universal standard | High | Expressed as percentage]
  - The data quality gatekeeper for all field operations analysis. Every insight that depends on field data should filter by log completion rate.
- **Daily Log Distribution Rate** (`fo-daily-log-dist`): Percentage of completed daily logs distributed to stakeholders — distributed / completed × 100. Distribution transforms the daily log from internal notes into an official project record with contractual weight. [Contract-specific distribution requirements | High | Expressed as percentage]
  - Completion without distribution = incomplete documentation. Cross-domain: distribution triggers stakeholder notification and creates the audit trail for claims.
- **Peak Daily Headcount** (`fo-peak-daily`): Maximum number of workers on site in a single day during the project — MAX(SUM(workers per trade per vendor) per day). Indicates project peak complexity and coordination burden. [OSHA staffing ratios | High | Typical peaks: 50-100 (small), 100-300 (mid), 300-800 (large), 800+ (mega). Usually occurs during ME]
  - Peak headcount defines the project's maximum coordination complexity. Cross-domain: feeds safety staffing ratios (Safety Manager per X workers) and site logistics planning.
- **Average Daily Headcount** (`fo-average-daily`): Average number of workers on site per active construction day — AVG(daily headcount) across construction days, excluding non-work days. Indicates sustained labor intensity throughout the project. [No universal standard | High | Typical averages: 20-50 (small), 50-150 (mid), 150-400 (large). Varies significantly by phase.]
  - More meaningful than peak for cost analysis — average × duration × loaded rate ≈ total labor cost. Cross-domain: feeds man-hours-per-million-dollars productivity metrics.
- **Equipment Utilization Rate** (`fo-equip-utilizatio`): Percentage of equipment time spent operating vs. idle — operating hours / (operating + idle hours) × 100. Calculated per equipment type and per project. Low utilization indicates over-provisioning or scheduling inefficiency. [No universal standard | High | Expressed as percentage]
  - equipment_name is free text — requires keyword classification into canonical types before meaningful benchmarking. Cross-domain: feeds equipment cost analysis (idle hours × daily rate = waste).
- **Plan Percent Complete (PPC)** (`fo-plan-percent`): Percentage of scheduled work that was actually performed — showed / total scheduled × 100. The Last Planner System's primary reliability metric. Measures whether the weekly or daily work plan was executed as planned. No-show rate = 1 - PPC. [Lean Construction Institute | High | Expressed as percentage]
  - PPC below 60% predicts schedule slippage. Vendor-level PPC identifies chronically unreliable trade partners. Cross-domain: strongest operational leading indicator for schedule performance.
- **Delay Frequency** (`fo-delay-frequency`): Number of recorded delay events per active project month, segmented by delay type — total delays / active months. Enables comparison of delay exposure across projects, geographies, and seasons. [AACE 29R-03 (Forensic Schedule Analysis) | High | Typical: 2-5 delay events per month (mid-size project). Varies heavily by geography (weather) and pr]
  - delay_type is a structured enum — zero NLP needed. Cross-domain: delay frequency × daily general conditions rate = delay cost estimate. Feeds schedule risk analysis and claims documentation.
- **Weather Delay Rate** (`fo-weather-delay`): Percentage of project days with weather-related delays — weather delay days / total project days × 100. Geographic and seasonal comparison metric. Combines weather observation data (conditions) with delay records (impact). [Contract-specific weather provisions | High | Expressed as percentage]
  - Two signals: weather log is_weather_delay flag and delay log weather entries. Cross-domain: feeds schedule contingency calculation and is primary evidence for excusable delay claims.
- **Waste Diversion Rate** (`fo-waste-diversion`): Percentage of construction waste recycled or diverted from landfill — recycled/diverted volume / total waste volume × 100. Required for LEED MR credit (50-75% target). Increasingly required by local ordinances and owner sustainability mandates. [LEED MR Credit (Construction Waste Management) | Medium | Expressed as percentage]
  - Requires method_of_disposal to distinguish recycling from landfill. Cross-domain: feeds sustainability reporting and environmental compliance documentation.

### Financial Instruments

**Budget & Cost Structure**
- **Project Budget** (`fi-project-budget`): The total approved budget for a project — the financial ceiling against which all costs are measured. Lifecycle: Created (preconstruction) → Approved → Active → Modified (via budget modifications) → Closed (at closeout). Original budget vs. [AACE 18R-97 (Cost Estimate Classification) | High | $500K–$500M+ depending on project type and delivery method]
  - Not all customers purchase financial tools. Projects without budget module should be excluded from cost benchmarks.
- **Budget Line Item** (`fi-budget-line-item`): An individual row in the project budget — allocates a specific dollar amount to a specific cost code or scope of work. Lifecycle: Created → Active → Modified (via budget modifications and change orders) → Closed. [CSI MasterFormat (cost code basis) | High | 10–500+ line items per project depending on complexity]
  - Budget line items are the bridge between money and work. Maps to building systems through cost code / WBS code — a budget line for '05 12 00 Structural Steel' maps to the Structural Frame system.
- **Cost Code** (`fi-cost-code`): A categorization code that classifies costs by type of work — typically based on MasterFormat divisions. The Rosetta Stone between financial data and building systems. Key properties: code number, description, MasterFormat division, standard vs. [CSI MasterFormat (50 divisions) | High | 02 Sitework, 03 Concrete, 05 Steel, 09 Finishes, 15 Mechanical, 26 Electrical]
  - Cost codes vary wildly between companies. Some use 3-level (division.section.subsection), others use flat codes. UCDM must normalize to MasterFormat for comparability.
- **WBS Code** (`fi-wbs-code`): Work Breakdown Structure code that adds a second dimension to cost classification — segments cost within a cost code by phase, location, or category. Example: cost code 03 30 00 (Cast-in-Place Concrete) + WBS 'Foundation' vs. WBS 'Elevated Slab'. [PMI PMBOK WBS (§5.4) | Medium | Phase-based, location-based, system-based, or hybrid segmentation]
  - WBS code adoption varies. Some companies use them extensively (5+ segments per cost code), others not at all. Budget codes serve a similar segmentation purpose.
- **Budget Code** (`fi-budget-code`): A grouping code applied to budget line items for reporting and categorization — distinct from cost codes. Key properties: code, description, project-specific or company-standard. Budget codes are a REPORTING overlay, not a transactional code. [Company-specific reporting hierarchies | Medium | Structure, Enclosure, MEP, General Conditions, Contingency, Site, Interiors]
  - Budget codes are the least standardized of the three code types. Highly company-specific. Useful for roll-up reporting but not for detailed cost analysis.

**Commitments**
- **Commitment (Subcontract)** (`fi-commit-subcontra`): A legally binding agreement between the GC and a subcontractor for a defined scope of work — the largest category of project spend. Lifecycle: Draft → Out for Signature → Executed → Active → Complete → Closed. [AIA A101/A201 (owner-contractor) | High | 25–40 subcontracts per project covering 70–85% of project cost]
  - Subcontracts are the primary financial instrument in construction. The vendor on a commitment links the financial domain to the Organizations domain.
- **Commitment (Purchase Order)** (`fi-commit-purchase`): An agreement to purchase materials, equipment, or services from a supplier — typically for materials not included in a subcontract scope. Lifecycle: Draft → Issued → Active → Complete → Closed. [UCC Article 2 (sale of goods) | High | $5K–$500K per PO]
  - POs are tracked in the same commitment system as subcontracts but with simpler workflows. Material PO delays are a primary schedule risk — connects to the Material Shortage insight.
- **Commitment Line Item** (`fi-commit-line-item`): A cost-code-level detail row within a commitment — breaks the total commitment into budget-aligned allocations. Key properties: cost code, WBS code, description, amount, commitment reference. [Follows parent commitment's standard/format | High | 5–500 line items per commitment depending on scope granularity]
  - Line item granularity varies by project and company. More granular = better cost tracking but more administrative burden. Direct cost-code-to-building-system mapping at the line item level.

**Change Management**
- **Change Event (CE)** (`fi-chg-event-ce`): Earliest financial signal of scope/cost change. change_reason values: design_development, owner_directive, unforeseen_conditions, value_engineering, scope_change, rework, allowance, regulatory, escalation. [AACE RP 10S-90 (Cost Engineering) | High | $1K–$5M per CE]
  - CEs are the earliest financial signal of a change. 6,748 companies have CEs with design-related change_reason. CE origin_type links back to the triggering document (RFI, observation).
- **Change Event Line Item** (`fi-chg-event-line`): A cost-code-level detail row within a change event — breaks the estimated change cost into budget-aligned allocations. [Follows parent CE standard/format | High | 1–50 line items per CE depending on scope breadth]
  - WBS codes on CE line items can identify specific elements (e.g., WBS 'Rework' within cost code '09 29 00 Gypsum Board'). latest_cost_amount is the current estimate — use this for cost totals.
- **Potential Change Order (CPCO)** (`fi-pot-chg-order`): An intermediate instrument that bridges a change event to a commitment change order — represents the GC's request to modify a specific subcontract based on an approved change. Lifecycle: Created (from CE) → Pending → Approved (becomes CCO) → Void. [AIA G709 (Proposal Request) | High | 1–5 CPCOs per CE depending on number of affected subs]
  - CPCOs are where changes get allocated to specific vendors. The CPCO is the bridge: CE identifies → CPCO formalizes against a commitment → CCO executes. Inherits building system mapping from parent CE.
- **Commitment Change Order (CCO)** (`fi-commit-chg-order`): Formal modification to a subcontract/PO that changes committed dollar amount. change_reason values (title case): Design Development, Owner Directive, Unforeseen Conditions, Value Engineering, Scope Change, Rework. Status: 96.7% Approved. [AIA G701 (Change Order) | High | $500–$2M per CCO]
  - 250K CCOs with design-related change_reason across 4,200 companies. $1.45B saved from CE/CCO deduplication in rework analysis. CCO grand_total is the cost column.
- **CCO Line Item** (`fi-cco-line-item`): A cost-code-level detail row within a commitment change order — modifies specific commitment line item amounts. [Follows parent CCO standard/format | High | 1–50 line items per CCO depending on scope breadth]
  - CCO line items are where committed cost changes actually land in the budget. Sum of CCO line items by cost code = net change to committed cost on corresponding budget lines.
- **Owner Change Order (Prime Contract CO)** (`fi-owner-chg-order`): A formal modification to the prime contract between owner and GC — changes the contract value and potentially the schedule. Lifecycle: Draft → Pending → Approved → Void. [AIA G701 (Change Order) | Medium | $5K–$10M per owner CO]
  - Not all projects track owner COs in construction software. Owner CO timing vs. commitment CO timing reveals cash flow risk — GC may commit to sub COs before owner approves the funding.
- **Budget Modification** (`fi-budget-mod`): REWORK SIGNAL: Modifications to rework-coded budget lines signal actual rework exceeding planned budget — 339 cos. Internal transfer between budget line items (moves money, does not change total budget). [Company-specific budget transfer policies | High | $1K–$1M per modification]
  - 339 companies have rework-coded budget modifications. Maps to building systems via cost codes on source and destination budget line items.

**Cost Tracking**
- **Direct Cost** (`fi-direct-cost`): A non-commitment expenditure — costs that don't flow through a subcontract or purchase order. Includes GC self-performed labor, small material purchases, equipment rental, T&M charges, reimbursables. Lifecycle: Created → Approved → Paid. [Company-specific cost tracking policies | High | $100–$500K per direct cost entry]
  - Companies that self-perform more have higher direct cost ratios and lower commitment ratios. Direct costs are the 'other' cost bucket — everything not covered by subcontracts or POs.
- **Direct Cost Line Item** (`fi-direct-cost-line`): A cost-code-level detail row within a direct cost — enables granular cost tracking for non-commitment expenses. Key properties: cost code, WBS code, description, amount, direct cost reference. [Follows parent direct cost format | High | 1–20 line items per direct cost entry]
  - Direct cost line item descriptions contain actionable keywords — 'rework', 'repair', 'correction', 'redo'. $500M in rework-related direct costs identified via NLP on line item descriptions.

**Billing & Payment**
- **Owner Invoice / Pay Application** (`fi-owner-invoice`): A periodic billing from the GC to the owner for work completed — the GC's request for payment under the prime contract. Lifecycle: Draft → Submitted → Under Review → Approved → Paid; also Rejected, Revised. [AIA G702/G703 (Application and Certificate for Payment) | High | Monthly billing cycle]
  - Monthly pay application cycle drives the financial rhythm of every project. Lender draws are often tied to pay app approval. Pay app line items correspond to SOV items mapping to cost codes.
- **Subcontractor Invoice** (`fi-sub-invoice`): A periodic billing from a subcontractor to the GC for work completed under a subcontract. Lifecycle: Draft → Submitted → Under Review → Approved → Paid; also Rejected, Revised. [AIA G702/G703 (adapted for sub billing) | High | Monthly billing]
  - Subcontractor invoice volume is high. Matching invoice amounts to approved work is a major administrative task. Invoice processing time is a key vendor relationship metric.
- **Retainage** (`fi-retainage`): Funds withheld from progress payments as security for completion of work — released at substantial completion or final completion. [State retainage statutes (vary by jurisdiction) | Medium | 5–10% of each progress payment]
  - Retainage is one of the most contentious financial instruments in construction. Subs view it as the GC holding their money. Some states cap retainage at 5%. Release delays strain vendor relationships.
- **Payment** (`fi-payment`): The actual transfer of funds between parties — the final step in the billing cycle. Lifecycle: Scheduled → Processed → Cleared. Key properties: amount, date, from party, to party, invoice reference, payment method. [Prompt Payment Acts (federal and state) | High | Net 30 to Net 60 payment terms]
  - Payment timing drives cash flow. Slow-paying owners cascade delays to sub payments. Construction lenders tie draws to pay app approval, adding another layer.
- **Lien Waiver** (`fi-lien-waiver`): A legal document in which a party waives their right to file a mechanic's lien against the property — exchanged with each payment. [State mechanic's lien statutes (vary by jurisdiction) | High | 4 types × number of subs × number of billing periods = hundreds per project]
  - Lien waiver collection is a major closeout task. Missing lien waivers can block final payment and retainage release. Some states have statutory lien waiver forms that must be used exactly.

**Financial Classification**
- **Schedule of Values (SOV)** (`fi-schedule-values`): A cost breakdown of a contract that defines the billing structure — line items represent discrete portions of work that can be billed as completed. Lifecycle: Created (with contract) → Active (updated each billing cycle) → Complete (100% billed). [AIA G703 (Continuation Sheet) | Medium | 10–500 SOV line items per contract depending on scope complexity]
  - SOV is one of the least standardized instruments. SOV lines often describe building elements in plain language ('Install curtain wall Level 3-5'), providing NLP-accessible links to building systems.
- **Allowance** (`fi-allowance`): A budget line item for work that cannot be precisely defined at contract time — price is estimated and reconciled to actual cost. Lifecycle: Established (in contract) → Active (as work performed) → Reconciled (actual vs. allowance). [AIA A201 §3.8 (Allowances) | Low | $10K–$2M per allowance]
  - Allowances are common in negotiated contracts (CM at Risk, design-build) and less common in hard bid. Typically tied to specific building systems — flooring, fixtures, lighting.
- **Contingency** (`fi-contingency`): A budget reserve for unforeseen costs — not allocated to any specific scope until needed. Lifecycle: Established (in budget) → Active (drawn down as changes occur) → Depleted or Returned. Key properties: contingency type (owner vs. GC vs. [AACE 10S-90 (Cost Engineering) | Low | 5–15% of construction cost depending on project complexity and delivery method]
  - Types: owner contingency (owner controls), GC contingency (GC controls), design contingency (for design-phase changes). GMP contracts define contingency explicitly. Burn rate > % complete = red flag.

**Earned Value & Forecasting**
- **Cost Forecast / Estimate at Completion (EAC)** (`fi-cost-forecast`): A projection of total project cost at completion — combines actual cost to date with estimated cost to complete. Updated monthly or more frequently on active projects. EAC = Actual Cost to Date + Estimated Cost to Complete. [AACE RP 10S-90 | Medium | Computed from: original budget + committed cost + actual cost + projected changes + cost to complete]
  - EAC is computed, not stored as a standalone instrument. Included here because it is the most important derived financial measure.
- **Cash Flow Projection** (`fi-cash-flow`): A time-phased projection of money in (owner payments) and money out (sub payments, direct costs) — shows when cash is needed. Updated monthly. Key properties: period, projected income, projected outflow, net cash position, cumulative cash position. [PMI PMBOK cash flow management | Low | Monthly or weekly time buckets]
  - Cash flow management is critical for GC financial health. Negative cash flow on a project means the GC is financing construction from other projects or credit lines.

**Standard Measures**
- **Budget Variance** (`fi-budget-variance`): The difference between budgeted cost and actual cost (committed + direct + approved changes) at any point in time. Formula: Budget Amount − (Committed Cost + Direct Cost + Approved Changes). [AACE cost variance analysis | High | Expressed as $ amount and as % of budget]
  - Variance by MasterFormat division enables cross-project comparison — 'are my concrete costs consistently over budget?' Budget variance at completion is the ultimate project financial outcome.
- **Cost Growth %** (`fi-cost-growth`): The percentage increase from original budget to final cost. Formula: (Final Cost − Original Budget) / Original Budget × 100. Measures total cost escalation including all changes, direct costs, and adjustments. [AACE 10S-90 | High | Typical range: 3–12% for well-managed projects]
  - delivery methods
- **Cost Performance Index (CPI)** (`fi-cost-perf-index`): The ratio of earned value to actual cost — measures cost efficiency. Formula: CPI = Earned Value / Actual Cost. CPI > 1.0 = under budget. CPI < 1.0 = over budget. CPI = 1.0 = on budget. Used as a multiplier in EAC forecasting. [ANSI/EIA-748 (EVMS) | Medium | CPI range: 0.70–1.30]
  - True EVMS is rare in commercial construction — more common on government/DOD projects. Simplified CPI (% complete × budget / actual cost) is more practical for benchmarking.
- **Committed Cost vs. Budget** (`fi-committed-cost`): The ratio of total committed cost (subcontracts + POs + approved changes) to budget. Formula: Total Committed / Budget × 100. Measures how much of the budget is locked into contracts. [AACE cost control | High | 0–100%+]
  - Commitment coverage < 70% late in the project = buying risk. Committed cost > budget = budget overrun before direct costs are even counted.
- **Change Order Rate** (`fi-chg-order-rate`): The number and value of change orders relative to original contract value. Formula: (Total CO Value / Original Contract Value) × 100. Can be computed separately for owner COs (revenue) and commitment COs (cost). [CII benchmarking metrics | High | By count: 20–100+ COs per project. By value: 5–15% of contract value is typical]
  - Separating CO rate by change_reason (design, owner, unforeseen, rework) reveals root causes. Design change rate + owner change rate + unforeseen change rate = total CO rate decomposition.
- **Contingency Burn Rate** (`fi-contingency-burn`): The rate at which contingency is consumed relative to project progress. Formula: (Contingency Used / Original Contingency) / (% Complete). Burn rate > 1.0 = contingency consumed faster than progress, indicating the project may exhaust reserves. [AACE contingency management | Low | Burn rate range: 0.5–2.0]
  - Contingency burn rate is one of the few LEADING financial indicators — it predicts future budget distress before it materializes. Most other financial metrics are lagging.
- **Invoice Processing Time** (`fi-invoice-processi`): The elapsed time from invoice submission to approval. Formula: Approval Date − Submission Date (in business days). Measures administrative efficiency and cash flow impact. [Prompt Payment Act benchmarks | High | Typical range: 5–30 business days]
  - Prompt Payment Acts in many states require payment within 30 days of invoice receipt. Invoice processing time directly affects sub cash flow and willingness to bid future work.
- **Cash Flow Variance** (`fi-cash-flow-2`): The difference between projected cash position and actual cash position at a point in time. Formula: Actual Cash Position − Projected Cash Position. Positive = more cash than expected. Negative = less cash than expected. [AACE cash flow analysis | Low | Expressed as $ amount]
  - Cash flow variance connects to payment timing — owner payment delays create negative variance that cascades to sub payments.
- **Estimate at Completion Variance** (`fi-estimate-at`): The difference between the projected final cost (EAC) and the original budget. Formula: EAC − Original Budget. Tracks how the projected final cost evolves over time. Early EAC variance is a leading indicator of final cost growth. [AACE 10S-90 | Medium | $ amount]
  - EAC variance at 25% complete is a strong predictor of final cost growth. Projects with high early EAC variance rarely recover. Track monthly EAC snapshots for trend analysis.

### Locations

**Site Level**
- **Project Site** (`loc-project-site`): The overall geographic boundary of a construction project — everything within the property line or limit of work. Top of the location hierarchy; every project has exactly one. Anchored by coordinates (lat/long or state plane). [OmniClass Table 13 | High | Single campus, city block, parcel, right-of-way corridor, multi-building campus]
  - Multi-building campuses are one site. The site boundary defines geographic extent. Level 0 in the hierarchy.
- **Building** (`loc-building`): A distinct structure within the project site — the primary vertical container for constructed space. Multi-building projects separate records by structure. Single-building projects still carry one Building node for hierarchy consistency. [OmniClass Table 13 | High | Building A/B, North Tower, South Tower, Parking Structure, Central Plant, Data Hall]
  - Building footprint defines horizontal boundary. Level 1 in hierarchy.
- **Exterior Zone** (`loc-exterior-zone`): A defined area outside the building envelope but within the project site — organized by function or orientation. Facade orientation zones (N/S/E/W) are critical for enclosure work as different exposures have different weather and solar conditions. [OmniClass Table 13 | Medium | North/South/East/West Facade, Courtyard, Plaza, Loading Dock, Parking Lot, Green Space, Entrance Dri]
  - Facade orientation zones connect enclosure scope to physical location. Level 1 in hierarchy.
- **Laydown / Staging Area** (`loc-laydown-staging`): Designated areas for material storage, prefabrication, and equipment staging. Shift as construction progresses — what was steel staging becomes curtain wall staging. Tight urban sites have minimal laydown, requiring just-in-time delivery. Leaf node. [OSHA 1926.250 (Materials Storage) | Medium | Main Laydown Yard, Steel Staging, Curtain Wall Staging, Dumpster Area, Concrete Washout, Crane Pad, ]
  - Laydown areas are dynamic and shift through the project. Urban vs. suburban site constraints drive logistics strategy. Level 1 leaf node.
- **Right-of-Way** (`loc-right-way`): Public or utility easement areas where project work occurs outside the property line. Governed by municipal permits with strict restoration requirements. Work windows may be restricted (night work, traffic hours). [MUTCD (Manual on Uniform Traffic Control Devices) | Low | Street Cut (Water Main), Sidewalk Reconstruction, Utility Ductbank, Curb Cut, Traffic Signal Work]
  - ROW work adds schedule risk from municipal coordination. Common on urban and infrastructure projects. Level 1 leaf node.
- **Temporary Facility** (`loc-temp-facility`): Contractor-provided temporary structures that support construction but are removed at completion. General conditions cost items. Location on site affects logistics. Removed before final site improvements. Leaf node. [OSHA 1926 Subpart F (Fire Protection) | Low | Job Trailer/Field Office, Temporary Parking, Guard Shack, Decontamination Unit, Temporary Restrooms,]
  - Temporary facilities are general conditions items not part of the permanent building. Level 1 leaf node.

**Building Vertical**
- **Floor / Level** (`loc-floor-level`): A horizontal plane within a building that divides it vertically — the primary vertical organizing unit. The most universally used location level. Most field records attach at floor level or below. [OmniClass Table 13 | High | Basement 2 (B2), Basement 1 (B1), Ground Floor (L1), Level 2-N, Mezzanine, Penthouse, Roof]
  - The universal organizing unit for field work. Level 2 in hierarchy.
- **Below-Grade Level** (`loc-below-grade`): Floors below ground level — basements, sub-basements, parking levels, underground mechanical spaces. Unique challenges: waterproofing, hydrostatic pressure, radon mitigation, garage ventilation, fire department access. [IBC Chapter 4 (special uses) | High | B1, B2, B3, Sub-Basement, Underground Parking P1/P2/P3]
  - Below-grade levels have distinct system profiles from above-grade. Waterproofing failures are a top rework driver. Level 2 in hierarchy.
- **Roof Level** (`loc-roof-level`): The top of the building including roof surface, mechanical penthouse, and rooftop equipment areas. Both an enclosure system (membrane, insulation, flashing) and a mechanical platform (RTUs, cooling towers, exhaust fans). [NRCA Roofing Manual | High | Main Roof, Low Roof, Mechanical Penthouse, Roof Terrace, Green Roof, Cooling Tower Platform]
  - Dual function — enclosure and mechanical platform. Fall protection observations are a leading safety signal. Level 2 in hierarchy.

**Floor Division**
- **Zone / Wing** (`loc-zone-wing`): A horizontal subdivision of a floor — used for phasing, scope separation, or building geometry. Project-specific designations defined by the team to organize work. A 50-story tower might define zones as quadrants per floor. [Project-specific | Medium | North/South/East/West Wing, Zone A/B/C, Phase 1/2 Area, Tower vs. Podium, Department]
  - Zones are project-specific — no universal standard. Level 3 in hierarchy.
- **Core / Shaft** (`loc-core-shaft`): Vertical penetrations that run through multiple floors — stairs, elevators, mechanical shafts, duct risers. Unique vertical elements that span the building height. [IBC Chapter 7 (fire-resistance-rated assemblies) | Medium | Stair A/B, Elevator Shaft 1-4, Mechanical Shaft, Electrical Riser, Plumbing Riser, Duct Shaft]
  - Vertical elements that span multiple floors — unique in the hierarchy. Firestopping is one of the most inspected items. Level 3.
- **Ceiling Plenum** (`loc-ceiling-plenum`): The space between the finished ceiling and the structural deck above — where most MEP distribution occurs. The most contested space in a building — 5+ trades working in the same 18-36 inch space. [IBC 717 (fire dampers in plenums) | Low | Typical Ceiling Plenum (per floor/zone), Return Air Plenum, Interstitial Space (healthcare)]
  - Above-ceiling inspection is the most critical quality hold point. Clash detection results often reference plenum space. Level 3 in hierarchy.

**Room & Space**
- **Room / Space** (`loc-room-space`): An individually identifiable enclosed space within a building — defined by walls, doors, and a room number. The unit of occupancy. Healthcare patient rooms may have 150+ punch items each. [OmniClass Table 13 | Medium | Office 301, Conference Room 205, Patient Room 412, Classroom 103, Hotel Room 1205, Apartment 8B, Lab]
  - Room-level tracking requires BIM or disciplined naming. Rooms bridge construction and operations. Level 4 in hierarchy.
- **Functional Area** (`loc-functional-area`): A space defined by its function rather than enclosure — may span rooms or be part of a larger space. Functional areas have specific code requirements: mechanical rooms (ventilation, fire separation), electrical rooms (clearances, access), data rooms ... [IBC Chapter 4 (special uses by function) | Medium | Lobby, Corridor, Elevator Lobby, Mechanical Room, Electrical Room, IDF/MDF, Kitchen, Server Room, Ma]
  - Code-driven spaces with specific inspection requirements regardless of project type. Level 4 in hierarchy.
- **Wet Area** (`loc-wet-area`): Spaces with plumbing fixtures and waterproofing requirements — bathrooms, kitchens, janitor closets, mechanical rooms with floor drains. Waterproofing testing (shower pan flood tests, floor drain tests) required before finishes. [IPC/UPC (plumbing codes) | Medium | Restroom M/F, Shower Room, Locker Room, Kitchen, Janitor Closet, Pool Area]
  - Waterproofing failures in wet areas are a major rework driver. ADA compliance is a primary inspection focus. Level 4 in hierarchy.

**Sub-Space**
- **Wall / Surface** (`loc-wall-surface`): An individual wall or surface within a room — identified by orientation or designation. Primarily BIM-driven and punch-item-driven. [OmniClass Table 13 | Low | North/South/East/West Wall, Column Line A, Soffit, Bulkhead]
  - Wall-level tracking requires BIM integration. Most valuable in repetitive programs (hotels, residential, healthcare). Level 5+ in hierarchy.
- **Equipment Location** (`loc-equip-location`): The specific location of a major piece of installed equipment — tracked for commissioning, maintenance, and warranty. Every major equipment piece gets a unique tag (AHU-1, CHL-1) that persists from design through 30+ years of operations. [ASHRAE Standard 202 (commissioning) | Low | AHU-1 (Mech Room B1), Chiller-1 (Central Plant), Panel LP-3A (Elec Room L2), VAV-3-01 (Plenum L3)]
  - Equipment tags bridge construction and operations lifecycle. Critical for facility management handover. Level 5+ in hierarchy.
- **Penetration / Opening** (`loc-penetration-open`): A specific penetration through a fire-rated or smoke-rated assembly — tracked for firestopping compliance. Every penetration through a rated assembly must be firestopped per a UL-listed system. [IBC 714 (penetrations) | Low | Electrical conduit through 2-hr wall, Plumbing riser sleeve, Duct penetration at stair wall]
  - Firestopping is one of the most inspected and most deficient items across all project types. Level 5+ in hierarchy.

**Cross-Cutting Overlay**
- **Fire / Smoke Compartment** (`loc-fire-smoke`): A code-defined area enclosed by fire-rated or smoke-rated construction — may span rooms or zones. A regulatory overlay on the physical layout that defines where fire barriers must be maintained, smoke dampers required, and rated doors installed. [IBC Chapters 7 & 7A | Low | Smoke Compartment A (L2 North), Fire Area 1, Fire Barrier at Grid 5, Horizontal Exit]
  - Fire compartments are a regulatory overlay not a physical construction element. Cross-cutting — spans multiple hierarchy levels.
- **Work Zone / Phase Area** (`loc-work-zone-phase`): A temporary designation that defines where active construction work is occurring — shifts as the project progresses. Dynamic — moves weekly or daily. Safety zones (crane radius, excavation, hot work) have specific regulatory requirements. [OSHA 1926 Subpart N (Cranes) | Medium | Active Pour Zone, Steel Erection Zone, Tower Crane Radius, Hot Work Area, Dust Control Zone, ICRA Zo]
  - Work zones are dynamic and temporary — they don't persist in the location hierarchy. Healthcare ICRA zones are heavily regulated.
- **Commissioning Zone** (`loc-cx-zone`): A grouping of spaces for the purpose of systems commissioning — may align with HVAC zones, floors, or functional groups. Groups equipment and spaces tested together. [ASHRAE Standard 202 (Commissioning) | Low | CxZone 1 (L1-L5 East), CxZone 2 (L1-L5 West), CxZone 3 (Penthouse Mech), CxZone 4 (Central Plant)]
  - Commissioning zones bridge location and system — organized by mechanical system boundaries. Cross-cutting.
- **Grid Line Intersection** (`loc-grid-line`): A coordinate location defined by the intersection of structural grid lines — the universal reference system for locating anything in a building. Every drawing references grid lines. Survey and layout is done to grid lines. [AIA A201 (drawing standards) | Low | Grid A/1, Grid B/3, Grid J/12, Column Line intersections]
  - Grid lines are the universal coordinate system of construction. Cross-cutting — applies at all hierarchy levels.

**Standard Measures**
- **Location Depth Utilization** (`loc-location-depth`): Measures how many levels of the location hierarchy a company uses in field records — from site-level only (depth 1) to room-level (depth 4+). Higher depth = more granular defect tracking. [None — operational maturity metric | High | Depth 1 (site only), Depth 2 (floor level), Depth 3 (zone level), Depth 4+ (room level)]
  - Low depth often indicates location setup was incomplete not that the project was simple.
- **Defect Density by Location Type** (`loc-defect-density`): Count of quality observations, punch items, and inspection deficiencies per location node — reveals where problems concentrate. Calculation: (observations + punch items + deficient inspections) / location count at each hierarchy level. [ISO 9001 (nonconformance tracking) | High | 5-15 punch items per room (typical), 20-50 per floor (commercial), 100+ per floor (healthcare)]
  - Normalize by location count or area to enable cross-project comparison.
- **Punch Items per Room** (`loc-punch-items-per`): Count of punch list items assigned to each room-level location — the primary closeout workload metric. Calculation: total punch items / total rooms. Segmented by room type for cross-project comparison. [AIA/AGC best practices for punchlist management | High | 3-8 per room (standard commercial), 10-20 per room (healthcare), 15-30 per room (hospitality)]
  - Requires room-level location setup. Projects without room locations can't benchmark at this level.
- **Floor Completion Rate** (`loc-floor-completion`): Percentage of punch items and observations closed per floor over time — tracks vertical closeout progress. Calculation: closed_items / total_items per floor measured weekly. [Lean Construction (last planner system) | High | 0-100% per floor]
  - Requires floor-level location setup. Sequence analysis reveals whether closeout follows schedule logic.
- **Location Coverage Rate** (`loc-location-coverag`): Percentage of defined locations that have at least one quality record (observation, inspection, or punch item) attached — measures inspection thoroughness. Calculation: locations_with_records / total_defined_locations. [ISO 19011 (audit sampling) | High | 60-80% typical]
  - Meaningful only when location hierarchy is fully set up. Low coverage is an actionable signal for quality managers.
- **Safety Incident Density by Zone** (`loc-safety-incident`): Count of safety observations and incidents per work zone or floor — identifies high-risk areas. Calculation: safety_observations / active_work_zones. [OSHA recordkeeping | Medium | 0-5 per zone per week (typical)]
  - Cross-domain with Safety. Location-based safety analysis requires location_id on safety observations.
- **Firestopping Deficiency Rate** (`loc-firestopping-def`): Percentage of inspected penetrations with firestopping deficiencies — a top quality metric for multi-story buildings. Calculation: deficient_penetrations / inspected_penetrations. Segmented by shaft type, rated assembly type, and floor. [IBC 714 | Medium | 5-15% first-pass deficiency rate (typical)]
  - Cross-domain with Building Elements (firestopping) and Quality (inspection deficiency). Highly regulated.

### Models & BIM

**BIM Authoring Models**
- **3D Building Information Model** (`bim-3d-building-info`): A parametric digital representation of the physical and functional characteristics of a building — the authoritative geometric and data source for design, construction coordination, and facility operations. [AIA E203 (BIM and Digital Data Protocol) | None | Architectural Model, Structural Model, Mechanical Model, Electrical Model, Plumbing Model, Fire Prot]
  - BIM models are the richest source of Building Element data — every element has type, material, dimensions, location, and spatial relationships.
- **Federated Model** (`bim-federated-model`): A combined multi-discipline model assembled from individual discipline models — the integrated view used for coordination, clash detection, and owner reviews. [AIA E203 (multi-discipline coordination) | None | Full federation (all disciplines), Partial federation (MEP only, structure + MEP), Trade-specific co]
  - Federation quality depends on model exchange format (IFC, NWC, RVT) and update cadence. Weekly federation with detection is standard; daily on fast-track projects.
- **4D Model (Schedule-Linked)** (`bim-4d-model`): A 3D model linked to the project schedule — visualizes construction sequence over time by associating model elements with schedule activities. Enables construction phasing visualization, logistics planning, and progress tracking. [BIM Execution Plan phasing requirements | None | Phase visualization, Logistics simulation, Progress comparison (planned vs. actual), Safety sequence]
  - 4D models bridge the Models & BIM domain to the Schedule domain. Most valuable on complex projects with phasing constraints. Adoption is growing but still limited to ~15-25% of major projects.
- **5D Model (Cost-Linked)** (`bim-5d-model-cost`): A 3D model linked to cost data — enables quantity-based estimating and cost visualization by associating model elements with cost information (cost codes, unit prices, assemblies). Quantities extracted from the model drive the estimate. [AACE cost estimating practices | None | Quantity takeoff from model, Assembly-based costing, Cost visualization by system, Value engineering]
  - 5D models bridge Models & BIM to Financial Instruments. Model quantities → cost estimates → budgets → actuals is the full financial lifecycle.
- **As-Built Model** (`bim-as-built-model`): A BIM model updated to reflect actual constructed conditions — incorporates field modifications, deviations from design, and final installed locations. [AIA E203 (as-built modeling requirements) | None | Updated architectural model, Updated structural model, Updated MEP models, Reality capture-verified ]
  - As-built models are a major closeout deliverable but adoption is inconsistent. Many projects still deliver 2D as-built drawings (redlines) rather than updated 3D models.

**Model Elements & Properties**
- **Model Element** (`bim-model-element`): An individual component within a BIM model — a wall, beam, column, pipe, duct, fixture, or any other discrete building component with geometry, type, material, and location properties. [IFC entity types (IfcWall, IfcBeam, IfcPipeSegment, etc.) | None | Walls, Columns, Beams, Slabs, Doors, Windows, Pipes, Ducts, Cable Trays, Fixtures, Equipment, Fittin]
  - Model elements are the bridge between the digital model and physical Building Elements. Each model element REPRESENTS a building element. IFC entity types provide the classification.
- **Level of Development (LOD)** (`bim-level-developmen`): A specification that defines the completeness and reliability of a model element at a given project phase — governs what information can be extracted from the model. [AIA E203 | None | LOD 100 (concept), LOD 200 (approx geometry), LOD 300 (precise geometry), LOD 350 (coordination), LO]
  - LOD 300/350 is the minimum for reliable coordination and clash detection. LOD 400 enables prefabrication. LOD requirements affect modeling cost and schedule.
- **Quantity Takeoff** (`bim-quantity-takeoff`): Material quantities extracted from model elements — counts, areas, volumes, lengths, and weights derived from model geometry and type properties. Quantities drive estimating (5D), procurement, and production tracking. [AACE quantity surveying practices | None | Element counts, Linear quantities (LF of pipe, duct, conduit), Area quantities (SF of wall, floor, c]
  - Quantity takeoff bridges Models & BIM to Financial Instruments (cost estimates) and Resources (material quantities). Takeoff accuracy depends on LOD — LOD 300+ needed for reliable quantities.
- **Model Properties & Parameters** (`bim-model-properties`): The non-geometric data attached to model elements — manufacturer, model number, fire rating, acoustic rating, energy performance, warranty period, maintenance requirements, and other attribute data. [COBie (Construction Operations Building Information Exchange) | None | Manufacturer, Model Number, Fire Rating, Acoustic Rating, U-Value, Finish, Color, Warranty Period, M]
  - Model properties are the data pipeline to facility management. Complete model properties at handover eliminate the need for the owner to manually catalog building assets.

**Coordination & Clash Detection**
- **Clash Detection Result** (`bim-clash-detection`): An identified spatial conflict between model elements from different disciplines — a pipe running through a beam, a duct intersecting a structural column, or conflicting MEP routes. [BIM Execution Plan clash detection protocols | None | Hard Clash (physical intersection), Soft Clash (clearance/tolerance violation), Workflow Clash (sequ]
  - Clash detection results are the input — coordination issues are the output. Not all clashes become coordination issues (many are resolved in the coordination meeting).
- **Coordination Issue** (`qsr-coord-issue`): A design or constructability problem identified during BIM coordination review — the actionable output of clash detection and model review. [AIA E203 | High | Clash, Coordination, Design Review, Constructability, Requirement Change, Existing Condition, Client]
  - coordination_issue.trade is free text, NOT standardized ('Plumbing' vs '22 Plumbing'). MEP-heavy.
- **BIM Coordination Meeting** (`bim-bim-coord`): A regular team meeting where designers, trade contractors, and the GC review the federated model, resolve clashes, and make coordination decisions. Typically weekly during design and early construction. [AIA E203 (BIM coordination requirements) | Medium | Weekly coordination meeting, Discipline-specific coordination (MEP-only, structure-MEP), Prefab coor]
  - Coordination meeting cadence and effectiveness directly predict field rework rates. Projects with weekly coordination have fewer field clashes than those with ad-hoc coordination.

**Reality Capture**
- **Point Cloud / Laser Scan** (`bim-point-cloud`): 3D spatial data captured by terrestrial or mobile laser scanning — represents existing conditions or as-built geometry as millions of measured points. [ASTM E57 (3D Imaging Data Exchange) | None | Terrestrial LiDAR scan, Mobile mapping scan, Handheld scan]
  - Point clouds bridge the physical site to the digital model. As-built verification via scan-to-model comparison reveals construction quality and dimensional accuracy.
- **360 Photo / Spherical Capture** (`bim-360-photo`): Spherical photographs taken at regular intervals throughout the project — creates an immersive, navigable visual record of site conditions over time. [No universal standard | Medium | Weekly capture, Milestone capture, Floor-by-floor documentation, Pre-cover documentation, Completion]
  - 360 photos are the fastest-growing reality capture method in construction — lower cost and faster than laser scanning. Linked to location (Locations domain) and time (Phases).
- **Drone Capture** (`bim-drone-capture`): Aerial photography, videography, photogrammetry, and LiDAR data captured by unmanned aerial vehicles (UAVs) — provides site-level documentation, earthwork volume calculations, progress monitoring, and safety surveillance. [FAA Part 107 (commercial drone operations) | Low | Orthomosaic (stitched aerial photo), 3D terrain model, Volumetric calculation (cut/fill), Progress p]
  - Drone captures are most valuable for site/earthwork projects (infrastructure, heavy civil) where volumetric tracking replaces manual survey.
- **Construction Photo** (`bim-const-photo`): A standard photograph documenting site conditions, progress, quality issues, safety observations, or completed work — the most fundamental visual record in construction. [Company documentation protocols | High | Progress photos (daily/weekly), Quality documentation, Safety documentation, Pre-cover photos, Compl]
  - Photos are the visual evidence layer for nearly all UCDM record types. A single observation or punch item may have 5–10 attached photos.

**Visualization & Communication**
- **Model-Based Drawing** (`bim-model-based`): A 2D drawing view generated from or linked to a 3D BIM model — plans, sections, elevations, and details extracted from the model rather than drawn independently. [NCS (National CAD Standard) | High | Plans, Sections, Elevations, Details, Schedules (door/window/finish), 3D views, Isometrics (MEP)]
  - Model-based drawings are the bridge between 3D models and 2D construction documents.
- **Digital Twin** (`bim-digital-twin`): A living digital representation of the building that combines the as-built BIM model with real-time sensor data, maintenance records, and operational information — the post-construction evolution of BIM. Updated continuously during operations. [ISO 23247 (Digital Twin Manufacturing) | None | Asset twin (equipment-level), Building twin (systems-level), Campus twin (portfolio-level)]
  - Digital twins are primarily an owner/facility management technology — construction's role is delivering the as-built model and data that feeds the twin.

**Standard Measures**
- **Coordination Issue Density** (`bim-coord-issue-2`): Number of coordination issues per million dollars of project value — measures the volume of BIM-identified spatial and design conflicts relative to project size. [No universal standard | High | Issues per $M]
  - Cross-domain: coordination issue density correlates with rework cost (Financial Instruments) and change event volume.
- **Coordination Issue Resolution Time** (`bim-coord-issue-3`): Average days from coordination issue creation to resolution — measures how quickly spatial and design conflicts are resolved. Faster resolution = less downstream delay. Segmented by issue_type (Clash vs. Design Review vs. [No universal standard | High | Days to resolution]
  - Long resolution times on Clash issues signal coordination bottlenecks. Design Review issues take longer by nature.
- **Clash Resolution Rate** (`bim-clash-resolution`): Percentage of identified clashes resolved before construction start — measures pre-construction coordination effectiveness. Higher rate = fewer field conflicts. [No universal standard | Medium | Percentage]
  - Unresolved pre-construction clashes predict field rework. Cross-domain: unresolved clashes → field conflicts → change events (Financial Instruments) → rework cost (insight #1).
- **Drawing Revision Frequency** (`doc-drawing-revision-2`): Number of drawing revisions issued per drawing set per month — measures design stability and churn. High revision frequency late in the project signals design instability and increases rework risk. [No universal standard | High | Revisions per drawing per month]
  - Late-stage revisions (post-IFC) are particularly costly — they often drive RFIs and change events. Cross-domain: drawing revisions trigger RFIs (Documents) and change events (Financial Instruments).
- **Photo Documentation Rate** (`bim-photo-docs-rate`): Number of construction photos documented per day or per million dollars — measures visual documentation discipline and thoroughness. Higher rates indicate more rigorous field documentation. [No universal standard | High | Photos per day]
  - Photo documentation rate correlates with quality record completeness — projects with high photo rates tend to have better observation and punch item documentation.
- **BIM Coordination Adoption Score** (`bim-bim-coord-2`): A composite measure of BIM coordination maturity based on: (1) whether coordination_issues exist, (2) issue volume relative to project size, (3) issue_type diversity (Clash + Design Review + Constructability), (4) resolution rate, (5) RFI linkage rat... [No universal standard | Medium | Score 0-100]
  - Composite score enables apples-to-apples comparison of BIM coordination usage. Companies with higher scores likely have lower rework rates.

### Organizations

**Owner / Developer**
- **Private Developer** (`org-private-develope`): Company or individual funding a project for profit — develops to sell, lease, or operate. Decision authority on scope, budget, and schedule. [State real estate licensing | Low | Developer]
  - Role polymorphism: a developer may self-perform CM services. Owner decisions drive cost and schedule more than any other party. Cross-domain: Financial Instruments (funding and change authorization).
- **Institutional Owner** (`org-institutional-ow`): Organization building for its own use — corporate campus, hospital, university, government facility. End user and operator of the facility. Defines program requirements, coordinates stakeholders, provides operations input, and plans occupancy. [Joint Commission (healthcare) | Low | Corporate real estate]
  - Institutional owners care about lifecycle cost, not just first cost. Internal facility teams often have strong opinions on systems and maintainability.
- **Public / Government Entity** (`org-public-governmen`): Federal, state, or local government agency procuring a public project. Regulated procurement authority with statutory constraints — competitive bidding, prevailing wage enforcement, ADA compliance, environmental review. [Miller Act (federal bonding) | Low | Federal agency]
  - Procurement rules severely constrain flexibility. Change orders require public documentation. Davis-Bacon prevailing wage on federal projects.

**Construction Management**
- **General Contractor (GC)** (`org-gen-contr-gc`): Company contracted to construct the project — holds risk for cost, schedule, and quality under lump sum or GMP contract. Single point of responsibility to the owner. Manages subcontractors, schedule, quality control, safety, and cost control. [AGC contract forms | High | GC]
  - cost growth
- **Construction Manager at Risk (CM at Risk)** (`org-const-manager-at`): CM engaged during design to provide preconstruction services (estimating, VE, constructability, scheduling), then transitions to GC role during construction under a GMP. Most common delivery method for large commercial projects. [AIA A133 (CM at Risk) | High | CM/GC]
  - GMP conversion is a key contractual milestone. Pre-construction services agreement → GMP amendment or separate construction contract.
- **Construction Manager Agency (CM Agency)** (`org-const-manager`): CM acts as owner's agent — manages project but does NOT hold trade contracts or bear construction cost risk. Provides schedule/budget management, trade coordination, quality oversight, and reporting. Owner holds direct contracts with trades. [AIA B132/B133 (CM services) | Medium | CM agent]
  - CM does not self-perform and does not hold subcontracts. Owner takes more risk but maintains direct trade relationships.
- **Design-Builder** (`org-design-builder`): Single entity responsible for both design and construction under one contract. Single point of responsibility for owner. Manages architect directly and self-coordinates design-construction overlap. [AIA A141 (design-build) | High | Design-builder]
  - Owner gives up some design control. Design-builder manages architect directly. Cross-domain: Phases (design and construction overlap significantly).
- **Program Manager** (`org-program-manager`): Firm managing a portfolio of related projects for an owner — multiple projects under one program. Provides portfolio-level schedule, budget, and risk management with standardization across projects. [CMAA (program management standards) | Medium | Program manager]
  - Provides consistency across projects. Cross-domain: Project Attributes (portfolio-level benchmarking).

**Design Team**
- **Architect of Record (AOR)** (`org-architect-record`): Licensed architecture firm responsible for building design and construction documents — stamp on architectural drawings. Performs construction administration (CA): submittal review, RFI response, field observation, punch list walk. [AIA B101 (design services) | Medium | Architect]
  - submittal review duration) across project types
- **Structural Engineer** (`org-struct-engineer`): Licensed engineering firm responsible for structural system design — foundation design, connection design, structural calculations. Stamp on structural drawings. Performs submittal review and RFI response for structural scope. [ASCE 7 (structural loads) | Medium | Structural engineer]
  - Shop drawing review is critical — especially steel connections and concrete reinforcing. Special inspections are often driven by structural requirements.
- **MEP Engineer** (`org-mep-engineer`): Licensed engineering firm(s) responsible for mechanical, electrical, and plumbing system design — HVAC, plumbing, electrical, fire protection. Energy code compliance, load calculations, equipment schedules. [ASHRAE (HVAC design) | Medium | MEP engineer]
  - MEP may be one firm or multiple specialists. Coordination issues during construction often trace back to design-phase decisions. Cross-domain: Building Elements (HVAC, Plumbing, Electrical).
- **Civil Engineer** (`org-civil-engineer`): Licensed engineering firm responsible for site design — grading, utilities, stormwater, roadways, erosion control. Stamp on civil drawings. Active from Preconstruction through Sitework. Subconsultant to architect or direct owner contract. [ASCE (civil engineering) | Low | Civil engineer]
  - Civil work is first constructed and last finished (site improvements). Utility conflicts between civil and structural are common. Cross-domain: Building Elements (Site & Earthwork, Site Utilities).
- **Fire Protection Engineer** (`org-fire-prot`): Licensed engineering firm responsible for fire protection and life safety system design — sprinkler design, fire alarm design, smoke control, egress analysis, fire code compliance. Active from Preconstruction through Commissioning. [NFPA 13 (sprinklers) | Low | Fire protection engineer]
  - Fire protection engineering is increasingly specialized. Smoke control on high-rises and atriums is complex. Fire marshal review is a critical permitting step.
- **Geotechnical Engineer** (`org-geotechnical-eng`): Licensed engineering firm investigating subsurface conditions and recommending foundation design — soil borings, lab testing, foundation recommendations, earthwork specs, dewatering recommendations. [ASTM D1586 (SPT) | Low | Geotechnical engineer]
  - Foundation type selection (spread footings vs. piles vs. caissons) driven by this report. Differing conditions claims reference it.
- **Landscape Architect** (`org-landscape-archit`): Licensed design firm responsible for exterior landscape, hardscape, irrigation, and site amenity design. Produces planting plans, irrigation plans, hardscape details. Active during Preconstruction and Site Improvements phase. [ASLA standards | Low | Landscape architect]
  - Landscape work is among the last site work completed. Plant material availability and seasonal planting windows affect schedule. Cross-domain: Building Elements (Site Improvements).

**Specialty Consultants**
- **Specifications Writer** (`org-specifications-w`): Firm or individual that writes the project manual (specifications) governing materials and installation methods. Product research, code cross-referencing, coordination with design team. Specifications are the legal backbone of construction quality. [CSI MasterFormat | Low | Spec writer]
  - Conflicts between specs and drawings generate RFIs. Many architects have in-house spec writers. Cross-domain: Documents (specifications, addenda).
- **Lighting Designer** (`org-lighting-designe`): Firm specializing in architectural and functional lighting design — lighting layout, fixture selection, controls design, daylighting analysis, energy code compliance. Bridges engineering and architecture. [IES (Illuminating Engineering Society) | Low | Lighting designer]
  - LED revolution has changed fixture selection. Controls complexity increasing (DALI, DMX, wireless). Cross-domain: Building Elements (Electrical — Lighting).
- **Acoustics Consultant** (`org-acoustics-consul`): Firm specializing in sound isolation, room acoustics, and noise control — STC/IIC ratings, room finish recommendations, mechanical noise criteria, environmental noise assessment. Critical for healthcare, education, residential, and performing arts. [ASTM E90/E413 (STC) | None | Acoustics consultant]
  - Speech privacy (healthcare), classroom acoustics (education), and impact isolation (residential) are the primary drivers. Cross-domain: Building Elements (Interiors — acoustical elements).
- **Building Envelope Consultant** (`org-building-envelop`): Firm specializing in design and performance of the building exterior skin — air/water/thermal barrier design, curtain wall engineering review, mock-up testing oversight, field quality inspection. [ASTM E2178/E2357 (air barrier) | Low | Envelope consultant]
  - Often independent from architect for objectivity. Cross-domain: Building Elements (Exterior Enclosure), Phases (Building Enclosure).
- **Sustainability / LEED Consultant** (`org-sustainability-l`): Firm managing green building certification and sustainability requirements — LEED/WELL credit tracking, energy modeling coordination, material documentation (EPDs, HPDs, VOC content), commissioning coordination. [LEED (USGBC) | Low | LEED consultant]
  - Material documentation (EPDs, HPDs, VOC content) is a major submittal effort across all trades. Cross-domain: Documents (certification documentation), Phases (Commissioning).
- **Code Consultant** (`org-code-consultant`): Firm specializing in building code interpretation and life safety compliance — code analysis, occupancy classification, egress analysis, fire resistance requirements, ADA compliance, variance applications. Critical for complex occupancies. [IBC/ICC (building code) | None | Code consultant]
  - Can save months in permitting by facilitating AHJ conversations. Critical for healthcare, high-rise, mixed-use. Cross-domain: Phases (Permitting & Approvals).

**Trade Contractors**
- **Subcontractor (Trade-Specific)** (`org-sub-trade`): Specialty contractor performing a specific trade scope of work under contract to the GC — self-performs trade work, manages own workforce, procures trade-specific materials, responsible for quality of installed work and safety of own crews. [State contractor licensing | High | Subcontractor]
  - safety incident rates
- **Self-Performing GC Division** (`org-self-performing`): GC's own workforce performing specific trade work — typically concrete, carpentry, general conditions, demolition. Same scope as subcontractor but with GC-employed labor. Costs tracked as direct costs rather than commitments. [State contractor licensing | Medium | GC self-perform]
  - carpentry)

**Suppliers & Fabricators**
- **Material Supplier** (`org-mat-supplier`): Company that sells construction materials — manufacturer or distributor. Supplies materials per purchase order, schedules deliveries, provides product documentation and warranties. Delivery reliability directly impacts schedule. [ASTM (material standards) | Medium | Supplier]
  - Material suppliers tracked via POs, not subcontracts. Material shortages are a top delay cause. Cross-domain: Resources (Materials), Phases (Procurement).
- **Fabricator** (`org-fabricator`): Company that manufactures custom construction components from approved shop drawings — steel fabricators, curtain wall fabricators, precast producers, custom casework shops. Fabrication per approved shop drawings with factory QC. [AISC (steel fabrication) | Medium | Fabricator]
  - Fabrication lead time is often critical path. Factory QC reports are key deliverables. Cross-domain: Phases (Fabrication & Long-Lead Items), Building Elements (by system).
- **Equipment Rental Company** (`org-equip-rental`): Company providing construction equipment on a rental basis — tower cranes, excavators, aerial lifts, temporary fencing, generators. Equipment mobilization, maintenance, and operator support (if provided). Active during Construction. [OSHA 29 CFR 1926 Subpart N (cranes) | Medium | Equipment rental]
  - Equipment costs are a significant general conditions line item. Tower crane planning dominates logistics on high-rise. Cross-domain: Resources (Equipment), Financial Instruments (Direct Costs).

**Testing & Inspection**
- **Special Inspection Agency** (`org-special-insp`): Independent testing firm performing code-required special inspections — structural steel connections, concrete testing, fireproofing thickness, welding inspection. Code requires independence from contractor. [IBC Chapter 17 (special inspections) | Medium | Special inspector]
  - Common inspections: structural connections, concrete cylinders, fireproofing thickness. Cross-domain: Phases (throughout Construction), Building Elements (Structural Frame).
- **Materials Testing Lab** (`org-mat-testing-lab`): Laboratory that tests construction materials for specification compliance — concrete cylinder testing (7-day and 28-day strength), soil compaction, steel tensile testing, asphalt testing, mortar testing. Active during Construction. [ASTM C31/C39 (concrete) | Low | Testing lab]
  - Concrete cylinder breaks are the most common test. Failing tests can require coring, load testing, or removal — expensive consequences.
- **Commissioning Agent (CxA)** (`rl-cx-agent-cxa`): Independent firm verifying building systems perform to design intent — pre-functional testing, functional performance testing, seasonal testing. Produces commissioning plan, checklists, test reports, deficiency lists, final commissioning report. [ASHRAE Guideline 0 (commissioning) | Low | Commissioning agent]
  - LEED and many jurisdictions now require independent CxA. Enhanced commissioning extends to envelope beyond MEP. Cross-domain: Phases (Commissioning), Building Elements (HVAC, Electrical).
- **Environmental Monitoring Firm** (`org-enviro-monitorin`): Firm monitoring environmental compliance during construction — air quality monitoring, noise monitoring, stormwater sampling, hazmat oversight, regulatory reporting. [EPA regulations | Low | Environmental consultant]
  - Cross-domain: Phases (Demolition & Site Clearing, Earthwork), Regulatory Authorities (EPA).

**Regulatory Authorities**
- **Building Department** (`org-building-departm`): Local government agency that reviews plans, issues building permits, performs progress inspections, and issues certificates of occupancy. Permit timeline varies from 2 weeks to 12+ months. Plan review comments generate design revisions. [IBC/ICC (building code) | Medium | Building department]
  - CO is the gate to occupancy. TCO is common when portions remain. Cross-domain: Phases (Permitting & Approvals, Final Inspections).
- **Fire Marshal / Fire Department** (`org-fire-marshal`): Fire authority having jurisdiction (AHJ) for fire and life safety compliance — fire protection plan review, fire alarm plan review, field inspections, acceptance testing, hydrant flow testing. Fire marshal sign-off is required for CO. [NFPA 1 (fire code) | Medium | Fire marshal]
  - Acceptance testing of fire alarm and sprinkler systems is witnessed by fire marshal. Fire watch may be required during construction. Cross-domain: Building Elements (Fire Protection).
- **Health Department** (`org-health-departmen`): Government agency regulating health-related construction — healthcare facilities, food service, pools, labs, childcare. Plan review for health-related spaces, field inspections, operational permits. Active from Preconstruction through Closeout. [FGI Guidelines (healthcare) | Low | Health inspector]
  - Required for hospitals, commercial kitchens, pools, childcare. Adds to closeout timeline.
- **Environmental / EPA Agency** (`org-enviro-epa`): Federal, state, or local environmental regulatory authority — environmental impact review, stormwater permit oversight, air quality compliance, hazmat oversight. NEPA review on federal projects can add years. [NEPA | Low | EPA]
  - SWPPP compliance monitored throughout construction. Contaminated site remediation adds significant cost and time. Cross-domain: Phases (Preconstruction, Earthwork).
- **OSHA / Safety Authority** (`org-osha-safety`): Federal or state occupational safety and health authority — workplace safety regulation, site inspections (scheduled and unscheduled), citation issuance, fatality investigation. [OSHA 29 CFR 1926 (construction safety) | Medium | OSHA]
  - OSHA can inspect any jobsite. Citations carry financial penalties and can shut down work. Cross-domain: Recurring Violations (insight #11), Resources (Safety Professional).
- **Zoning / Planning Authority** (`org-zoning-planning`): Local government agency controlling land use, density, setbacks, and project approvals — zoning compliance review, variance review, site plan approval, community review facilitation. Zoning approval is a prerequisite for building permit. [Local zoning codes | None | Zoning board]
  - Variances require public hearings. Conditions of approval can significantly affect project scope and cost. Cross-domain: Phases (Permitting & Approvals), Project Attributes (location).

**Financial Institutions**
- **Construction Lender** (`org-const-lender`): Bank or financial institution providing construction financing — construction loan funding, draw review, progress inspection (lender's inspector), compliance monitoring. Lender draws tied to percent complete — monthly pay applications scrutinized. [OCC (banking regulation) | Low | Construction lender]
  - Cost overruns can trigger loan covenant issues. Lender's inspector verifies progress independently. Cross-domain: Financial Instruments (Pay Applications, Retainage).
- **Surety / Bonding Company** (`org-surety-bonding`): Insurance company issuing performance and payment bonds guaranteeing contractor's obligations. Bonds protect owner (performance bond) and subcontractors (payment bond). [Miller Act (federal bonding) | Low | Surety]
  - Bond capacity limits how much work a GC can take on. Consent of surety required for final payment. Cross-domain: Financial Instruments (Contract Closeout).
- **Insurance Broker / Carrier** (`org-insurance-broker`): Companies providing construction insurance — general liability, workers' comp, builders risk, professional liability, umbrella, OCIP/CCIP wrap-up programs. Certificate of insurance collection is a major administrative task. Active across all phases. [State insurance regulations | Medium | Insurance broker]
  - Wrap-up (OCIP/CCIP) programs consolidate insurance under one policy. Builders risk covers property damage during construction.

**Utilities**
- **Electric Utility** (`org-electric-utility`): Local electric utility company providing permanent electrical service — service design review, transformer supply/placement, metering, permanent connection, energization. [NEC/NFPA 70 (service entrance) | Low | Electric utility]
  - Transformer location and service size affect design. Permanent power energization eliminates temporary power cost. Cross-domain: Phases (Electrical Rough-In), Building Elements (Electrical).
- **Gas Utility** (`org-gas-utility`): Local gas utility providing natural gas service — service design review, gas main extension (if required), meter installation, service connection. Gas service for HVAC, domestic hot water, commercial kitchen. [NFPA 54 (National Fuel Gas Code) | Low | Gas utility]
  - Gas service affects HVAC system type and kitchen design. Cross-domain: Building Elements (HVAC, Plumbing).
- **Water / Sewer Authority** (`org-water-sewer`): Municipal authority providing domestic water and sanitary sewer service — service size determination, tap/connection permits, meter installation, water quality testing. Water service affects fire protection (hydrant flow, fire pump supply). [International Plumbing Code | Low | Water authority]
  - Sanitary sewer capacity can limit project density. Fire protection water supply (hydrant flow) is a design driver. Cross-domain: Building Elements (Plumbing, Site Utilities).
- **Telecom / Internet Provider** (`org-telecom-internet`): Companies providing data, voice, and internet service — service design, conduit and fiber routing, equipment room requirements, service activation. Multiple carriers may serve the building. Active during Preconstruction and Construction. [TIA-568 (cabling standards) | Low | Telecom provider]
  - Conduit routing and telecom room sizing are design-phase decisions. Fiber-to-building availability varies by location. Cross-domain: Building Elements (Low Voltage & Technology).

**Standard Measures**
- **Subcontractor Count per Project** (`org-sub-count-per`): Total number of distinct subcontractors and suppliers engaged on a project — measured from awarded subcontracts and purchase orders. Indicates project complexity and coordination burden. [AGC (project complexity metrics) | High | Typical range: 15-25 (small), 25-40 (mid), 40-80 (large/complex)]
  - More subs = more coordination interfaces. Projects with 50+ subs have exponentially more coordination challenges.
- **Trade Coverage Rate** (`org-trade-coverage`): Percentage of project scope covered by contracted subcontractors vs. remaining unawarded scope — awarded value / estimated total value × 100. Tracks buyout progress during procurement. [AGC (procurement metrics) | High | Expressed as percentage]
  - Buyout gaps late in construction create budget risk. Cross-domain: Phases (Procurement — Bidding & Buyout), Financial Instruments (Commitments).
- **Vendor Insurance Compliance Rate** (`org-vendor-insurance`): Percentage of project vendors with current, compliant insurance certificates on file — compliant vendors / total vendors × 100. Tracks risk exposure from uninsured or underinsured trades. [AIA A201 (insurance requirements) | High | Expressed as percentage]
  - Insurance compliance is a contractual requirement. Non-compliant vendors create liability risk. Cross-domain: Financial Institutions (Insurance Broker).
- **Subcontractor Safety Incident Rate** (`org-sub-safety`): OSHA recordable incident rate per subcontractor — (number of recordable incidents × 200,000) / hours worked. Enables comparison of safety performance across trades and companies. [OSHA 29 CFR 1904 (recordkeeping) | Medium | TRIR typical: 0.5-3.0 (varies by trade)]
  - Cross-domain: Recurring Violations (insight #11 — safety observation patterns by vendor), Resources (Trades).
- **Design Team Responsiveness** (`org-design-team`): Average days for design team members to respond to RFIs and review submittals — measured from RFI creation to response and submittal submission to review completion. Indicates design team engagement quality. [AIA A201 (RFI and submittal timelines) | High | RFI response: typical 7-14 days contractual]
  - Slow RFI response cascades into schedule delays. Submittal review delays cascade into procurement and fabrication. Cross-domain: Documents (RFIs, Submittals), Phases (Procurement).
- **Change Order Dispute Rate by Trade** (`org-chg-order`): Percentage of change orders disputed or rejected by trade — disputed COs / total COs per trade × 100. Identifies which trade relationships generate the most commercial friction. [AIA A201 (change order process) | High | Expressed as percentage]
  - High dispute rates indicate scope definition problems or adversarial relationships. Cross-domain: Financial Instruments (Change Management), Resources (Trades).

### Permits & Regulatory

**Construction Permits**
- **Building Permit** (`pr-building-permit`): Primary authorization from the local building department to begin construction. Lifecycle: Application → Plan Review → Approval → Issuance → Active → Final Inspection → Closed. [IBC (International Building Code) | None | New Construction, Addition, Tenant Improvement, Shell & Core, Foundation Only, Partial Permit (early]
  - Critical path item — construction cannot legally start without an issued building permit. Most jurisdictions allow early-start or partial permits for foundations while full permit is pending.
- **Demolition Permit** (`pr-demolition-permi`): Authorization to demolish or remove existing structures. Lifecycle: Application → Hazmat Survey → Review → Approval → Issuance → Active → Completion Notification. [OSHA 29 CFR 1926 Subpart T (Demolition) | None | Full Demolition, Partial/Selective Demolition, Interior Demolition, Soft Strip]
  - Asbestos survey is typically a prerequisite — jurisdictions won't issue demo permits without a completed survey.
- **Renovation / Alteration Permit** (`pr-renovation-alter`): Authorization for modifications to existing structures — alterations / repairs / changes of use. Triggers when work exceeds substantial improvement thresholds defined by the jurisdiction (often 50% of building value). [IBC Chapter 34 (Existing Buildings) | None | Alteration Level 1/2/3, Change of Occupancy, Repair, Addition, Substantial Improvement]
  - Often more complex than new construction — requires code analysis of the existing building. The IEBC provides prescriptive (3 alteration levels) and performance paths.
- **Temporary Structures Permit** (`pr-temp-structures`): Authorization for temporary construction facilities — scaffolding / shoring / formwork / temporary enclosures / construction hoists. Required for structures affecting public safety or right-of-way. [OSHA 29 CFR 1926 Subpart L (Scaffolds) | None | Scaffold, Sidewalk Shed, Construction Fence, Tower Crane Foundation, Shoring, Temporary Enclosure, C]
  - In urban environments (NYC / Chicago / SF) sidewalk shed and scaffold permits are major cost drivers with annual renewal requirements. Tower crane permits may require FAA notification.
- **Trade Permit** (`pr-trade-permit`): Separate jurisdictional permits required for specific building system work — electrical / plumbing / mechanical / fire protection / elevator. [NEC (National Electrical Code) | None | Electrical, Plumbing, Mechanical/HVAC, Fire Protection (sprinkler), Fire Alarm, Elevator, Gas, Low V]
  - Trade permits are typically pulled by the responsible subcontractor (electrician pulls electrical permit) not the GC.

**Site & Environmental Permits**
- **Environmental Permit** (`pr-enviro-permit`): Regulatory authorizations for work affecting air quality / water resources / wetlands / hazardous materials. Issued by federal (EPA) / state / and local environmental agencies. [Clean Air Act | Low | Air Quality Permit, Wetlands Permit (Section 404), Hazardous Materials Permit, Noise Variance, Dust ]
  - Often the longest-lead regulatory item — wetlands permits can take 6-18 months. Projects near sensitive receptors (schools / hospitals / waterways) face stricter requirements.
- **Stormwater Permit / SWPPP** (`pr-stormwater-permi`): Stormwater Pollution Prevention Plan and associated permit required for sites disturbing one or more acres. Mandates erosion and sediment control (ESC) best management practices (BMPs). [Clean Water Act Section 402 | Low | Notice of Intent (NOI), Notice of Termination (NOT), BMP Inspection, Corrective Action, Turbidity Mo]
  - One of the most common regulatory violations on construction sites — EPA fines can exceed $50K/day. Many states have stricter requirements than federal CGP.
- **Street / Right-of-Way Permit** (`pr-street-right-way`): Authorization for construction activities within the public right-of-way — lane closures / sidewalk closures / utility cuts / material staging / crane operations over public streets. Issued by local transportation or public works departments. [MUTCD (Manual on Uniform Traffic Control Devices) | None | Lane Closure, Sidewalk Closure, Street Closure, Utility Cut, Crane Swing Over ROW, Material Staging,]
  - Urban projects may require multiple ROW permits throughout construction — each crane pick / concrete pour / or steel delivery that affects traffic may need separate authorization.
- **Utility Connection Permit** (`pr-utility-connecti`): Authorization to connect to or modify public utility infrastructure — water / sanitary sewer / storm sewer / gas / electric / telecommunications. Each utility provider has separate application processes and design review requirements. [Utility-specific standards (AWWA for water / NESC for electric) | None | Water Main Tap, Sewer Connection, Storm Drain Connection, Gas Service, Electrical Service, Telecom/F]
  - Utility connections require coordination with utility companies on THEIR schedules — the GC has limited control over timing.

**Zoning & Land Use**
- **Zoning Approval** (`pr-zoning-appr`): Land use authorization confirming that the proposed project complies with local zoning ordinances — permitted uses / setbacks / height limits / lot coverage / floor area ratio (FAR) / parking requirements / density. [Local zoning ordinances | None | By-Right (permitted use), Conditional Use Permit (CUP), Special Use Permit (SUP), Site Plan Approval]
  - Typically an owner/developer responsibility handled during preconstruction not by the GC.
- **Variance / Special Exception** (`pr-variance-special`): Formal relief from specific zoning requirements when strict compliance creates undue hardship. Lifecycle: Application → Staff Review → Public Hearing → Board Decision → Appeal Period. [State zoning enabling acts | None | Area Variance (setback / height / lot coverage), Use Variance, Special Exception, Nonconforming Use]
  - Use variances (allowing a prohibited use) are much harder to obtain than area variances (modifying dimensional requirements).

**Plan Review & Regulatory Approvals**
- **Building Department Plan Review** (`pr-building-departm`): Formal review of construction documents by the building department to verify code compliance before permit issuance. Covers structural / life safety / accessibility / energy / and building code requirements. [IBC | Low | First Review, Second Review, Third Review, Expedited Review, Deferred Submittal, Phased Review]
  - Many jurisdictions now accept or require electronic plan review (EPR). Third-party plan review firms supplement building department staff.
- **Fire Marshal Review** (`pr-fire-marshal`): Fire and life safety plan review and field approval by the fire marshal or fire prevention bureau. Covers fire sprinkler design / fire alarm systems / means of egress / fire-rated assemblies / hazardous materials storage / and fire access. [NFPA 1 (Fire Code) | Low | Fire Sprinkler Review, Fire Alarm Review, Means of Egress Review, Hazmat Review, Fire Access Review,]
  - Fire marshal and building department reviews are often independent — separate agencies with separate timelines.
- **Health Department Approval** (`pr-health-departmen`): Regulatory approval from the health department for projects involving food service / healthcare / pools / laboratories / or other health-regulated occupancies. [FDA Food Code | None | Food Service Review, Healthcare Plan Review, Pool/Spa Permit, Laboratory Safety Review, Child Care F]
  - Healthcare projects face the most complex health department requirements — infection control risk assessments (ICRA) / negative pressure room verification / medical gas system testing.

**Regulatory Inspections**
- **AHJ Inspection** (`pr-ahj-insp`): Field inspections performed by the Authority Having Jurisdiction (building department) at required construction milestones. Verifies that work in place complies with approved plans and applicable codes. [IBC Section 110 (Required Inspections) | Medium | Foundation, Slab/Deck, Rough Framing, Rough Electrical, Rough Plumbing, Rough Mechanical, Insulation]
  - The GC coordinates AHJ inspections — calling at the right time to avoid delays. A failed inspection can hold up subsequent work. Some jurisdictions have 24-48 hour scheduling lead times.
- **Special Inspection** (`pr-special-insp`): Code-required inspections performed by independent certified special inspectors (not the building department) for critical structural and life-safety work. Required where deficiencies would be concealed and could create structural failure. [IBC Chapter 17 (Special Inspections and Tests) | Medium | Structural Steel (bolting/welding), Concrete Placement, Reinforcing Steel, Masonry, Fireproofing, Sp]
  - The Statement of Special Inspections (SSI) from the design team lists all required special inspections — it's the compliance roadmap. Special inspectors must be certified (ICC / AWS / ACI).
- **Third-Party Testing** (`pr-third-party`): Independent materials testing and quality assurance performed by certified testing laboratories. Verifies that construction materials and installed systems meet specifications and code requirements. [ASTM standards (C39 concrete / D1557 soil / E1105 water infiltration) | Low | Concrete Cylinder Break, Soil Compaction (nuclear density), Steel Tensile Test, Weld Inspection (UT/]
  - Concrete cylinder breaks are the highest-volume test on most projects — 7-day and 28-day breaks are standard.

**Certificates & Occupancy**
- **Certificate of Occupancy** (`pr-cert-occupancy`): Final authorization from the building department to occupy and use a completed building for its permitted purpose. Confirms all code requirements met / all required inspections passed / all special inspection letters received. [IBC Section 111 (Certificate of Occupancy) | None | Full CO, Partial CO (by floor or area), Core & Shell CO, Amended CO (change of use)]
  - Often the contractual milestone triggering final payment / retainage release / warranty period start. Partial COs allow phased occupancy but may have conditions.
- **Temporary Certificate of Occupancy** (`pr-temp-cert`): Conditional occupancy approval when a building is safe to occupy but has outstanding items preventing full CO. Specifies conditions and deadline for completing remaining work. [IBC Section 111.3 (Temporary Occupancy) | None | 90-Day TCO, 120-Day TCO, 180-Day TCO, Renewed TCO, Conditional TCO]
  - Common on large commercial projects where full completion is impractical by move-in date. Multiple TCO renewals are a red flag for closeout problems.
- **Certificate of Completion** (`pr-cert-completion`): Regulatory sign-off confirming that construction work is complete and compliant — used for projects without occupancy (site work / infrastructure / demolition) or for trade-specific scope completion. [IBC Section 111.1 | None | Building Completion, Site Work Completion, Infrastructure Completion, Demolition Completion]
  - For public infrastructure projects (roads / bridges / utilities) the Certificate of Completion is the primary regulatory closeout instrument.
- **Letter of Compliance** (`pr-letter-comp`): Written confirmation from a regulatory agency / design professional / or special inspector that specific work or systems comply with applicable codes and standards. Lifecycle: Inspection/Testing → Report → Letter Issuance. [IBC Chapter 17 (Special Inspection letters) | None | Structural Compliance Letter, Fire Protection Sign-Off, Elevator Acceptance, Energy Compliance Certi]
  - Compliance letters are the connective tissue of closeout — each regulatory agency requires its own sign-off before releasing hold on the CO. A single missing letter can delay occupancy.

**Safety & Labor Compliance**
- **OSHA Notification** (`pr-osha-notificatio`): Required notifications to OSHA and activity-specific safety permits for hazardous construction operations. [OSHA 29 CFR 1926 (Construction Safety) | Low | Crane Notification, Confined Space Entry Permit, Excavation Permit, Hot Work Permit, Asbestos Notifi]
  - Hot work permits and confined space entry permits are managed internally by the GC's safety department not filed with OSHA. Crane notifications may require 24-48 hour advance notice.
- **Site Safety Plan** (`pr-site-safety-plan`): Project-specific safety documentation identifying hazards / control measures / emergency procedures / and safety responsibilities. [OSHA 29 CFR 1926 Subpart C (General Safety) | Low | Site-Specific Safety Plan (SSSP), Fall Protection Plan, Crane Lift Plan, Traffic Control Plan, Hazar]
  - A living document that should be updated as conditions change (new trades / new hazards / crane operations). Many owners/CMs require safety plan approval before GC mobilization.
- **Labor Compliance** (`pr-labor-comp`): Requirements for workforce compensation / documentation / and equal opportunity — particularly on public and federally funded projects. [Davis-Bacon Act (federal) | None | Prevailing Wage, Certified Payroll, Apprenticeship Ratio, DBE/MBE/WBE Goals, Section 3, Project Labo]
  - Prevailing wage applies to most public construction in the US. Violations can result in back pay / debarment from public work / contract termination.

**Permit Lifecycle & Tracking**
- **Permit Application** (`pr-permit-applicati`): The formal request to a regulatory agency for a permit / approval / or certificate. Includes project information / scope of work / applicable codes / required documents (plans / calculations / surveys) / and fees. [Local building department application requirements | Low | Building Permit Application, Trade Permit Application, Environmental Permit Application, ROW Permit ]
  - Incomplete applications are the #1 cause of permit delays — jurisdictions reject submissions missing required documents / calculations / or fees.
- **Permit Status** (`pr-permit-status`): The current state of a permit in its lifecycle — from application through issuance / active construction / and final closeout. Tracking status across all required permits is a critical path management activity. [No universal standard — each jurisdiction defines its own status terminology | Low | Applied, Under Review, Comments Issued, Approved, Issued, Active, Expired, Renewed, Suspended, Revok]
  - Most GCs maintain a permit tracking log — a spreadsheet listing all required permits / status / responsible party / and dates. Prime candidate for structured data capture.
- **Inspection Scheduling** (`pr-insp-scheduling`): The process of requesting / scheduling / and coordinating regulatory inspections with the AHJ / special inspectors / and testing labs. [IBC Section 110 | Medium | 24-Hour Request, 48-Hour Request, Same-Day, Online Scheduling, Phone Request, Batch Scheduling]
  - Failed inspections are a schedule killer — correction work and reinspection often lose 2-5+ days.

**Standard Measures**
- **Permit Cycle Time** (`pr-permit-cycle`): Elapsed time from permit application submission to permit issuance. Calculation: issuance date minus application date / optionally excluding resubmission periods. Segmented by permit type (building / trade / environmental) and jurisdiction. [No universal standard | Low | 2-4 weeks (simple trade permits), 4-12 weeks (building permits), 3-18 months (environmental/zoning)]
  - One of the most requested preconstruction metrics — owners want to know how long permits will take. Experienced teams budget for 2-3 review cycles.
- **Inspection Pass Rate** (`qsr-insp-pass-rate`): Percentage of regulatory inspections (AHJ and special) that pass on the first attempt. Calculation: passed inspections / total inspections × 100. [Industry benchmark: 85-95% first-pass rate for well-managed projects | Medium | 85-95% (well-managed), 70-84% (average), <70% (quality concerns)]
  - Failed inspections should be tracked by root cause — premature call (work not ready) vs. workmanship deficiency vs. code interpretation disagreement.
- **Regulatory Hold Duration** (`pr-reg-hold`): Total calendar days of construction delay caused by regulatory actions — stop-work orders / permit delays / failed inspections requiring correction / expired permits. [AACE delay classification | Low | 0-5 days (well-managed), 5-20 days (average), 20+ days (regulatory risk)]
  - Stop-work orders are the most severe regulatory action — they halt all construction and can take days to weeks to resolve.
- **Open Permit Aging** (`pr-open-permit`): Average elapsed days that permits remain in open/active status. Calculation: sum of (current date or closure date minus issuance date) / total permits. Tracks whether permits are being closed out in a timely manner. [No universal standard | None | 30-180 days (typical active period), 180+ days (aging concern), open at closeout (red flag)]
  - Open permits at project completion are a common problem — the GC moves on and forgets to close permits. Open permits can prevent CO issuance and create liability for the owner.
- **Compliance Document Completeness** (`pr-comp-doc`): Percentage of required regulatory and compliance documents received and verified. Calculation: received documents / total required documents × 100. [Owner/CM contract requirements | Medium | 100% (closeout ready), 90-99% (near complete), <90% (significant gaps)]
  - A structured compliance document checklist at project kickoff (listing all required letters / certificates / reports) is best practice.
- **Permit Renewal Rate** (`pr-permit-renewal`): Percentage of permits that require renewal or extension during the project — indicating original validity period was insufficient. Calculation: renewed permits / total permits × 100. [No universal standard | None | 0-5% (on-schedule), 5-15% (schedule pressure), 15%+ (significant delays)]
  - Permit renewal fees can be significant on large projects. Some jurisdictions require re-inspection or updated plans for renewal.

### Phases

**Preconstruction**
- **Programming & Feasibility** (`ph-program`): Owner defines project requirements and validates viability — needs assessment, site analysis, zoning review, pro forma development, and environmental studies. Gate: program approval / authorization to proceed with design. [ASTM E1557 (UNIFORMAT II) | None | Pro forma]
  - Cross-domain: Project Attributes (project type, location, total value defined here). Duration ranges from weeks to years depending on entitlement complexity.
- **Design Development** (`ph-design`): Architects and engineers develop the design from concept through construction documents — schematic design (SD), design development (DD), construction documents (CD), code review, structural/MEP engineering, energy modeling, specifications. [AIA B101 (design services) | Low | SD package]
  - Design RFIs between owner/architect/engineers are high volume. Coordination between disciplines starts here. Cross-domain: Building Elements (all systems defined on paper).
- **Estimating & Budgeting** (`ph-estimating`): Develop cost estimates from conceptual through detailed GMP or hard bid — quantity takeoff, unit pricing, subcontractor pricing, risk contingency, value engineering. Multiple estimate rounds: conceptual (SD), detailed (DD), final (CD). [AACE 18R-97 (cost estimate classification) | Medium | Conceptual estimate]
  - VE can significantly change scope. Cross-domain: Financial (budget line items and cost codes originate from estimates).
- **Permitting & Approvals** (`ph-permit`): Secure regulatory approvals required before construction — building permits, zoning variances, environmental permits, utility coordination, fire marshal review, DOT permits, stormwater permits. Gate: building permit issued / notice to proceed. [IBC/ICC (building code) | Low | Building permit]
  - Permit timelines vary wildly — 2 weeks to 12+ months depending on jurisdiction. Critical path item. Cross-domain: Project Attributes (location drives requirements).
- **Preconstruction Planning** (`ph-precon-plan`): GC develops execution strategy before breaking ground — baseline schedule, logistics plan, phasing strategy, safety plan, quality plan, procurement strategy, staffing plan. CM-at-Risk does this during design; design-bid-build GCs do it after award. [PMI PMBOK (scheduling) | Medium | Baseline schedule]
  - Baseline schedule is a key contractual deliverable. Cross-domain: Resources (staffing plan), Project Attributes (delivery method determines timing).

**Procurement**
- **Bidding & Buyout** (`ph-bidding`): Solicit bids from subcontractors and suppliers, level bids, negotiate scope, and award contracts — scope definition, bid solicitation, bid leveling, insurance/bonding verification, contract execution. [AIA A201 (general conditions) | Medium | Subcontracts]
  - Long-lead items (steel, curtain wall, elevators, switchgear) bid early. Cross-domain: Financial (subcontracts become commitments).
- **Submittals & Shop Drawings** (`ph-submittals`): Subcontractors prepare detailed fabrication and product documents for architect/engineer review — submittal preparation, review cycles, resubmittals, product substitution requests. Submittal log is a critical schedule driver. [CSI MasterFormat (section-based organization) | High | Approved submittals]
  - Curtain wall, structural steel, and elevator submittals typically have longest lead. Cross-domain: Building Elements (submittals organized by system).
- **Fabrication & Long-Lead Items**: Materials fabricated off-site with delivery schedules established — structural steel (8-16 wks), curtain wall (12-24 wks), elevators (16-30 wks), switchgear (12-20 wks), precast, HVAC equipment, custom casework. [AISC (steel fabrication) | Low | Fabricated materials]
  - These durations drive the critical path schedule. Cross-domain: Building Elements (Structural Frame, Exterior Enclosure, Elevators, Electrical).
- **Material Ordering & Delivery Coordination**: Standard materials ordered and delivery sequenced to match construction schedule — PO issuance, delivery scheduling, staging area planning, just-in-time coordination, material tracking. [CSI MasterFormat (material sections) | Medium | Purchase orders]
  - Staging space is a constant constraint on urban sites. Cross-domain: Resources (materials), Material Shortage (insight #2 — delay_type = Material is primary signal).

**Mobilization**
- **Site Setup** (`ph-site-setup`): Establish temporary facilities and infrastructure to support construction — temporary fencing, construction entrance, trailer placement, temporary utilities (power, water, sanitation), site signage, erosion control, tree protection. [OSHA 29 CFR 1926 (site safety) | Medium | Site logistics plan implemented]
  - SWPPP must be in place before disturbing soil. Temporary power is critical path for MEP startup. Cross-domain: Project Attributes (site logistics driven by location).
- **Safety & Environmental Orientation** (`ph-safety-orient`): Establish safety culture and environmental compliance from day one — site-specific safety orientation, toolbox talks, emergency action plan, hospital route, environmental awareness training, hazard communication. [OSHA 29 CFR 1926.21 (safety training) | Medium | Safety orientation records]
  - Sets the safety culture for the entire project. Cross-domain: Recurring Violations (insight #11 — safety observation patterns start here).

**Sitework & Foundations**
- **Demolition & Site Clearing** (`ph-demo`): Remove existing structures and vegetation to prepare for new construction — building demolition, selective demolition, clearing and grubbing, underground obstruction removal, hazmat abatement if required. Gate: site cleared and ready for earthwork. [OSHA 29 CFR 1926.850 (demolition safety) | Medium | Cleared site]
  - Hazmat abatement (asbestos, lead, contaminated soil) can be critical path. Unknown conditions are a common claims source.
- **Earthwork** (`ph-earthwork`): Excavate and prepare the ground for foundations — bulk excavation, rock removal, shoring/sheeting, dewatering, proof rolling, structural fill, compaction, fine grading. Differing site conditions are the #1 source of construction claims. [ASTM D698/D1557 (compaction testing) | Medium | Excavation complete]
  - Dewatering can run for months on high water table sites. Compaction testing is quality-critical. Cross-domain: Building Elements (Site & Earthwork).
- **Site Utilities** (`ph-site-util`): Install underground infrastructure before building foundations cover access — sanitary sewer, storm drainage, domestic and fire water, gas service, electrical and telecom ductbank, grease interceptors. Must complete before foundation/slab work. [International Plumbing Code | Medium | Utility installations tested]
  - Utility conflicts with foundations are common — as-built surveys critical for future reference. Cross-domain: Building Elements (Site Utilities).
- **Foundations** (`ph-foundations`): Construct below-grade structural support — pile driving or drilled shafts, spread footings, grade beams, foundation walls, waterproofing, backfill, underslab plumbing and electrical. Concrete testing (cylinders) is mandatory. [ACI 318 (concrete design) | Medium | Foundation as-built survey]
  - Underslab MEP rough-in must complete before slab pour — coordination milestone. Waterproofing inspection is a hold point. Cross-domain: Building Elements (Foundations).
- **Slab on Grade** (`ph-slab`): Pour ground-level concrete floor slab — vapor barrier, underslab insulation, rebar/WWF placement, embedded conduit, concrete placement, finishing, curing, control joint sawing. Large pours are major production events. [ACI 302.1R (floor slab construction) | Medium | Slab on grade complete]
  - FF/FL testing required for specified tolerances. Cure time (typically 28 days full strength) affects loading schedule. Cross-domain: Building Elements (Foundations).

**Structure**
- **Structural Steel Erection** (`ph-steel`): Erect the steel frame including columns, beams, girders, metal deck, and shear studs — connection bolting/welding, plumbing and aligning. Tower crane operations dominate logistics. Fall protection is the primary safety concern. [AISC 360 (steel design) | High | Steel erection complete per area]
  - Connection inspections (bolts and welds) are quality-critical hold points. Cross-domain: Building Elements (Structural Frame), Resources (ironworkers, cranes).
- **Elevated Concrete** (`ph-elev-conc`): Place concrete on metal deck or formwork for elevated floor slabs — deck prep, rebar/post-tensioning placement, embedded items, concrete pumping, finishing, curing, PT stressing. Follows deck erection floor-by-floor. [ACI 318 (concrete design) | Medium | Concrete test reports]
  - PT stressing has specific timing requirements. Slab edge forming at curtain wall line is coordination-critical. Duration included in structural steel.
- **Concrete Frame** (`ph-conc-frame`): For concrete-framed buildings: form and pour columns, beams, and slabs floor-by-floor — formwork erection, rebar placement, embedded items, concrete placement, form stripping, shoring/reshoring, curing. Formwork cycle time drives schedule. [ACI 318 (concrete design) | Medium | Concrete test reports]
  - Alternative to steel frame. Reshoring requirements affect lower floor loading and when MEP can start. Cross-domain: Building Elements (Structural Frame).
- **Stairs & Miscellaneous Metals**: Install permanent stairs, handrails, embed plates, lintels, shelf angles, bollards, and equipment supports. Shelf angles for masonry/exterior panels must be in place before enclosure starts. Stairs provide worker access between floors. [AISC (misc metals) | Medium | Stairs installed]
  - Shelf angles are coordination-critical — bridge between structure and enclosure phases. Duration included in structure. Cross-domain: Building Elements (Structural Frame, Exterior Enclosure).

**Building Enclosure**
- **Curtain Wall & Glazing** (`ph-curtainwall`): Install exterior glass and aluminum systems to enclose the building — curtain wall units (unitized or stick-built), windows, storefronts, structural silicone, perimeter sealant. [AAMA 501 (water testing) | High | Water test reports]
  - MEP penetration coordination through curtain wall is essential. Cross-domain: Building Elements (Exterior Enclosure), Procurement (longest fabrication lead).
- **Masonry & Cladding** (`ph-masonry`): Install opaque exterior wall systems — brick veneer, precast panels, metal panels, backup wall, through-wall flashing, weep systems, control joints. Weather-sensitive: masonry can't be laid below 40°F without protection. [TMS 402/602 (masonry) | High | Masonry completion per area]
  - Flashing and weep details critical for long-term water management — hidden work with major consequences. Cross-domain: Building Elements (Exterior Enclosure).
- **Air & Moisture Barrier** (`ph-barrier`): Establish continuous air and moisture barrier across the building envelope — fluid-applied or sheet membrane, transition detailing at openings, penetration sealing, inspection and testing. [ASTM E2178/E2357 (air barrier testing) | Medium | Air barrier inspection reports]
  - Many jurisdictions require third-party inspection. Failures cause long-term moisture damage. Cross-domain: Building Elements (Exterior Enclosure).
- **Roofing** (`ph-roofing`): Install roof membrane system to achieve weather-tight condition — roof insulation, cover board, membrane installation, flashing, sheet metal, roof drainage, penetration detailing. Dry-in is a major project milestone enabling interior work. [NRCA (roofing standards) | High | Roof completion certificate]
  - Dry-in is one of the most important project milestones — enables all interior work. Manufacturer rep on-site during install is typical for warranty. Cross-domain: Building Elements (Roofing).

**MEP Rough-In**
- **Above-Ceiling Coordination** (`ph-abv-ceil`): Resolve spatial conflicts between MEP systems before installation — 3D coordination / BIM clash detection, routing prioritization, trade coordination meetings, clearance verification. The difference between a smooth MEP install and chaos. [BIM Execution Plan (AGC/AIA) | Medium | Coordinated MEP drawings]
  - Trades that install without coordination cause rework. BIM coordination standard on $10M+ projects. Cross-domain: Building Elements (HVAC, Plumbing, Electrical, Fire Protection).
- **HVAC Distribution** (`ph-hvac-dist`): Install ductwork and hydronic piping — main duct and branch installation, HVAC piping (chilled/hot water), equipment pads, duct and pipe insulation, hanger installation. Ductwork is the largest spatial consumer in the ceiling. [SMACNA (duct construction) | High | HVAC rough-in complete per area]
  - Main duct runs installed first to establish routing priority. Insulation must be inspected before ceiling closes. Cross-domain: Building Elements (HVAC).
- **Plumbing Rough-In** (`ph-plumb-ri`): Install supply and waste piping — domestic water distribution, sanitary waste and vent, gas piping, pipe insulation, fire stopping at penetrations. Testing is a critical hold point: pressure test for supply, DWV test for waste. [International Plumbing Code (IPC) | High | Plumbing rough-in complete per area]
  - Fire stopping at penetrations is a code requirement and major punch item generator. Cross-domain: Building Elements (Plumbing).
- **Electrical Rough-In** (`ph-elec-ri`): Install conduit, wire, and power distribution — main conduit and feeder installation, branch circuits, wire pulling, panel and switchgear installation, transformer setting, cable tray, grounding. Permanent power energization is a major milestone. [NEC/NFPA 70 (electrical code) | High | Electrical rough-in complete per area]
  - Permanent power eliminates temporary power cost. Switchgear lead time often critical path. Cross-domain: Building Elements (Electrical), Procurement (switchgear).
- **Fire Protection** (`ph-fp-ri`): Install sprinkler mains, branches, standpipe risers, and fire pump — main and branch line installation, sprinkler head rough-in, seismic bracing, FDC installation. Sprinkler head layout drives ceiling coordination. Gate: system tested and tagged. [NFPA 13 (sprinklers) | High | Fire protection rough-in complete]
  - Head conflicts with lights, diffusers, and detectors are the most common coordination issue. Cross-domain: Building Elements (Fire Protection).
- **Low Voltage Rough-In** (`ph-lv-ri`): Install raceways and cabling for data, security, fire alarm, and AV — conduit and cable tray, backbone and horizontal cabling, fire alarm wiring, security wiring. Often the last trade into the ceiling space. Gate: cabling complete and tested. [TIA-568 (cabling) | Medium | Low voltage rough-in complete per area]
  - Data room buildout is a coordination milestone. Cable testing and certification required for warranty. Cross-domain: Building Elements (Low Voltage & Technology).

**Interior Rough-In**
- **Metal Stud Framing** (`ph-framing`): Frame interior partitions, soffits, and bulkheads — wall layout, metal stud framing, blocking for fixtures/casework, door frame setting, fire-rated assembly framing. Blocking for grab bars, casework, TV mounts must be coordinated with MEP. [ASTM C645/C754 (steel framing) | Medium | Framing complete per area]
  - Fire-rated wall framing inspection is a hold point. Missing blocking discovered during finish installation causes rework. Cross-domain: Building Elements (Interiors).
- **Drywall** (`ph-drywall`): Hang and finish gypsum board — drywall hanging, taping and finishing, sanding, specialty boards (moisture/abuse/fire-rated), patching around MEP. Above-ceiling inspection must happen BEFORE drywall closes the ceiling. [GA-216 (gypsum application) | High | Drywall complete per area]
  - Drywall damage from other trades is a constant issue and major punch item source. Cross-domain: Building Elements (Interiors), Quality Issues.
- **Ceiling Grid** (`ph-ceil-grid`): Install suspension system for acoustic ceilings — main tee and cross tee, hanger wire, seismic bracing, grid leveling, access panel framing. Grid installation signals all above-ceiling MEP work must be complete. [ASTM C635/C636 (ceiling suspension) | Medium | Ceiling grid installed and level per area]
  - Grid layout coordinates with light, sprinkler head, and diffuser locations. Last chance for above-ceiling inspection. Cross-domain: Building Elements (Interiors, HVAC, Electrical, Fire Protection).

**Finishes & MEP Trim**
- **Paint & Wall Coatings** (`ph-paint`): Apply primers, paint, and specialty coatings — primer, first coat, second coat, touch-up, specialty coatings, wall protection. Paint is the most common punch item across ALL project types. Typically the first finish in a space. [MPI (Master Painters Institute) | High | Paint complete per area]
  - Other trades damaging paint is a constant problem requiring multiple touch-up rounds. Cross-domain: Quality Issues (paint/finish is #1 punch category universally).
- **Flooring** (`ph-flooring`): Install floor finishes — tile (ceramic, porcelain, stone), carpet (broadloom, tile), resilient (LVT, VCT, rubber), specialty (epoxy, terrazzo, polished concrete), base, transitions. Sequence: tile before casework, carpet last. [TCNA Handbook (tile) | High | Flooring complete per area]
  - Floor protection critical after installation. Tile lippage and grout are common punch items. Cross-domain: Building Elements (Interiors), Quality Issues.
- **Ceilings** (`ph-ceilings`): Install acoustic ceiling tile and specialty ceiling finishes — acoustic tile, specialty ceilings (wood, metal, drywall), ceiling access panels, edge trim. One of the last overhead activities. Gate: ceilings complete. Duration: 1-2%. [ASTM E1264 (acoustical ceiling products) | Medium | Ceilings complete per area]
  - Damaged tiles from other trades working above are a frequent punch item. Cross-domain: Building Elements (Interiors).
- **Doors & Hardware** (`mat-doors`): Install door slabs and finish hardware — door hanging, hinges, closers, locksets, pulls, keying, access control coordination, fire-rated door labeling. Top-3 punch item category on every project type. Gate: all doors hung and hardware operational. [DHI (Door and Hardware Institute) | High | Doors and hardware complete]
  - Hardware schedule is one of the most detailed submittals. Access control integration adds complexity. Cross-domain: Quality Issues (top-3 punch category).
- **Casework & Millwork** (`ph-casework`): Install cabinets, countertops, trim, and built-in furnishings — cabinet installation, countertop templating and installation, trim and base molding, built-in shelving, toilet partitions and accessories. Gate: casework and accessories complete. [AWI (Architectural Woodwork Institute) | Medium | Casework and millwork complete per area]
  - Countertop templating happens after casework for exact dimensions. Toilet accessories typically one of the last installed items. Cross-domain: Building Elements (Interiors).
- **HVAC Trim & Controls** (`ph-hvac-trim`): Install visible HVAC devices and controls — diffusers, grilles, thermostats, VAV box controls, damper actuators, BAS device installation, final duct connections. Must be complete before TAB. Gate: HVAC devices complete — ready for commissioning. [ASHRAE (controls) | Medium | HVAC devices installed]
  - Controls programming often continues through commissioning. Thermostat/diffuser placement coordination with architect important. Cross-domain: Building Elements (HVAC).
- **Plumbing Fixtures** (`ph-plumb-fix`): Install visible plumbing fixtures — toilets, sinks, faucets, accessories, stop and waste valves, floor drain covers. Fixtures are damage-prone. Gate: plumbing fixtures complete and operational. Duration: 1-2%. [International Plumbing Code | High | Fixtures installed and operational]
  - High-volume punch item category. Cross-domain: Building Elements (Plumbing), Quality Issues.
- **Electrical Devices & Lighting** (`ph-elec-dev`): Install visible electrical devices and light fixtures — outlets, switches, cover plates, light fixtures, exit/emergency lighting, lighting controls, panel labeling. Major visual milestone. Gate: all devices and lighting operational. Duration: 2-3%. [NEC/NFPA 70 | High | Devices and lighting installed]
  - Cover plates and device alignment are high-volume punch items. Lighting control programming often continues into commissioning. Cross-domain: Building Elements (Electrical).
- **Fire Alarm & Detection Devices**: Install visible fire alarm devices — smoke/heat detectors, pull stations, horn/strobes, duct detectors, device addressing, panel programming. Device placement must match approved fire alarm drawings. [NFPA 72 (fire alarm code) | High | Fire alarm devices installed]
  - AHJ acceptance test is a required milestone. Strobe candela/placement per ADA is a common deficiency. Cross-domain: Building Elements (Fire Protection).
- **Low Voltage Devices** (`ph-lv-dev`): Install visible low voltage devices — data jacks, cameras, card readers, intercoms, paging, AV equipment. Cable labeling and testing required. Gate: devices complete and tested. Duration: 1-2%. [TIA-568 (cabling) | Medium | Devices installed]
  - Integration testing between security, access control, and fire alarm is complex. Late owner changes to AV/data layout are common. Cross-domain: Building Elements (Low Voltage & Technology).

**Commissioning**
- **Pre-Functional Testing** (`ph-prefunc`): Verify each system component is properly installed before energizing or flowing — equipment installation verification, valve/damper tag verification, motor rotation checks, control device calibration, breaker verification. [ASHRAE Guideline 0 (commissioning process) | Medium | Pre-functional checklists complete per system]
  - Many jurisdictions now require CxA. Catches installation errors before costly startup failures. Cross-domain: Building Elements (HVAC, Plumbing, Electrical, Fire Protection, Elevators).
- **Systems Startup** (`ph-startup`): Energize and start up individual systems for the first time — electrical energization sequence, boiler/chiller startup, pump/fan startup, fire pump acceptance test, elevator acceptance test, generator load bank test. [NETA (electrical testing) | Low | Startup reports per system]
  - Electrical energization must follow a specific safe sequence. Cross-domain: Building Elements (all MEP systems).
- **Testing Adjusting & Balancing** (`ph-tab`): Balance air and water systems to design flow rates — air system balancing (supply, return, exhaust), hydronic balancing (chilled, hot, condenser water), sound and vibration measurement. TAB contractor typically independent third party. [AABC (Associated Air Balance Council) | Low | TAB report]
  - Results affect occupant comfort directly. Re-balancing after tenant buildout is common. Cross-domain: Building Elements (HVAC).
- **Integrated Systems Testing** (`ph-integrated`): Verify systems work together correctly under various operating conditions — sequence of operations verification, failure mode testing, emergency power transfer, fire alarm integration, smoke control testing, elevator recall, BAS trending. [ASHRAE Guideline 0 | Low | Integrated test reports]
  - Tests systems interacting: fire alarm → elevator recall → smoke evacuation → emergency power. AHJ witnesses fire/life safety tests. Cross-domain: Building Elements (all systems).
- **Performance Verification** (`ph-perf-ver`): Confirm building performs to design intent under actual conditions — energy performance, thermal comfort, acoustics, lighting levels, indoor air quality, envelope performance. Some tests require seasonal conditions (heating vs. cooling season). [ASHRAE 90.1 (energy) | None | Performance verification report]
  - Required for LEED and WELL certification. Envelope commissioning increasingly required by code. Cross-domain: Project Attributes (sustainability rating).

**Closeout**
- **Punch List** (`ph-punch`): Identify and correct remaining deficiencies before owner acceptance — architect punchlist walk, owner punchlist walk, deficiency documentation, trade-by-trade correction, re-inspection, sign-off. Typical project: 500-5,000 punch items. [AIA A201 (substantial completion) | High | Punch list generated]
  - Most labor-intensive closeout activity. Multiple walks are normal. Cross-domain: Quality Issues (insight #4 — punch items are strongest quality signal).
- **Final Inspections & Approvals**: Secure regulatory sign-offs required for occupancy — fire marshal inspection, building department final, elevator inspection, health department, certificate of occupancy (CO), temporary CO (TCO). Gate: certificate of occupancy issued. Duration: 1-2%. [IBC/ICC (building code) | High | Certificate of occupancy (CO)]
  - TCO is common when portions of work remain. Each AHJ has unique requirements. Cross-domain: Project Attributes (location drives requirements).
- **As-Built Documentation** (`ph-asbuilt`): Compile record documents reflecting actual constructed conditions — as-built drawing markup, O&M manual compilation, warranty compilation, spare parts and attic stock delivery, equipment data sheets. [AIA A201 (record documents) | Medium | As-built drawings]
  - Quality varies enormously — digital O&M delivery increasingly expected. Cross-domain: Building Elements (all systems documented).
- **Owner Training** (`ph-training`): Train owner's facilities staff on building systems operation and maintenance — HVAC operations, BAS, fire alarm, elevator, security, electrical distribution, plumbing. Often rushed or skipped — leads to operational problems. [ASHRAE Guideline 0 (training requirements) | Low | Training sign-off sheets]
  - Quality of training directly affects warranty claim volume. Manufacturer reps typically conduct training. Cross-domain: Warranty & Operations.
- **Contract Closeout** (`ph-contract-close`): Complete commercial and legal close of all contracts — final change order reconciliation, final pay application, retainage release, lien waiver collection, consent of surety, final accounting, contract close letter. [AIA A201 (final payment, retainage) | High | Final pay application approved]
  - Retainage (typically 5-10% of contract value) is a major financial event. Lien waiver collection from all tiers can be complex. Cross-domain: Financial (all cost surfaces reconciled).

**Warranty & Operations**
- **Warranty Period** (`ph-warranty`): Contractor responsible for correcting defects discovered after substantial completion — warranty claim response, defect investigation, repair coordination, manufacturer warranty coordination, 11-month warranty walk. [AIA A201 (warranty provisions) | Low | Warranty claims resolved]
  - 11-month walk catches items before warranty expires. Cross-domain: Quality Issues (warranty claims correlate with construction deficiency rates).
- **Seasonal Commissioning** (`ph-seasonal-cx`): Verify HVAC performance across heating and cooling seasons not available during initial commissioning — heating season verification, cooling season verification, BAS setpoint optimization, energy monitoring review. [ASHRAE Guideline 0 (seasonal testing) | None | Seasonal commissioning reports]
  - First full year reveals actual performance across all conditions. Cross-domain: Building Elements (HVAC).
- **Facility Transition** (`ph-transition`): Transfer operational knowledge and responsibility from construction team to facilities team — maintenance schedule establishment, spare parts inventory, vendor contact transfer, BAS access transfer, service contract establishment. [IFMA (facility management) | None | Maintenance plan]
  - Quality of this transition determines decades of building maintenance. Poor transitions lead to deferred maintenance and premature failure. Cross-domain: all domains.

**Standard Measures**
- **Phase Duration Variance**: Actual phase duration compared to baseline schedule — (actual days - planned days) / planned days × 100. Positive = behind schedule. Measured per phase and sub-phase using schedule milestones and activity completion data. [PMI PMBOK (schedule management) | Medium | Expressed as percentage or days]
  - Most slippage occurs in procurement (long-lead items), enclosure (weather), and commissioning (integration complexity).
- **Schedule Performance Index** (`sch-schedule-perf`): Earned value metric: SPI = Earned Value / Planned Value. SPI < 1.0 = behind schedule, SPI > 1.0 = ahead. Calculated at project or phase level using weighted activity completion against the baseline schedule. [AACE RP 10S-90 (earned value) | Low | SPI typically 0.7-1.2]
  - Government/institutional projects most likely to use formal EVM. Commercial projects rely on milestone tracking instead.
- **Phase Milestone Compliance**: Percentage of phase transition milestones achieved on or before scheduled date — on-time milestones / total milestones × 100. Tracks critical path gates between phases. [PMI PMBOK (milestone management) | Medium | Expressed as percentage]
  - Dry-in, permanent power, and CO are the most commonly tracked milestones. Late milestones cascade downstream.
- **Phase Overlap Ratio**: Percentage of a phase's duration that overlaps with adjacent phases — overlap days / total phase days × 100. Higher overlap = more concurrent/fast-track execution. Normal for procurement to overlap with construction. [PMI PMBOK (fast tracking) | Low | Ranges 0% (sequential) to 80%+ (highly fast-tracked)]
  - Fast-tracking increases rework risk when upstream phases change. Cross-domain: Rework Cost (insight #1 — design changes during construction).
- **RFI Density by Phase**: RFIs generated during each phase, normalized by duration (RFIs per week) or project value (RFIs per $M). Indicates information gap intensity at each project stage. [CSI (RFI process) | High | Typical total: 200-2,000 RFIs per project]
  - RFI volume peaks during structure and MEP rough-in. predicted_topic enables classification without NLP. Cross-domain: Design Change Impact (insight #31).
- **Punch Item Density** (`qsr-punch-item-3`): Punch items per unit area (per 1,000 SF) or per trade during closeout — calculated from punch item creation dates and project gross area. Indicates construction quality and closeout efficiency. [AIA A201 (substantial completion criteria) | High | Typical: 0.5-5.0 items per 1,000 SF]
  - Cross-domain: Quality Issues (insight #4 — 18 keyword categories), Rework Cost (insight #1 — punch items are trailing indicator).
- **Submittal Cycle Time** (`doc-submittal-cycle`): Average days from submittal submission to final approval — calculated per submittal, then aggregated by trade, spec section, or phase. Longer cycles delay procurement and fabrication start. [CSI (submittal management) | High | Typical: 14-30 days per cycle]
  - 718K overdue submittals in 2-year window. Overdue submittals correlate with material delays. Cross-domain: Procurement (Submittals sub-phase).

### Project Attributes

**Project Identity**
- **Project Type** (`pa-project-type`): Primary functional use of the constructed facility — the single most impactful attribute for benchmarking. A $50M hospital and a $50M warehouse have completely different cost profiles, risk patterns, and trade compositions. [CSI UniFormat | High | Commercial Office, Retail, Healthcare (Hospital / Medical Office / Ambulatory), Education (K-12 / Hi]
  - Most impactful single attribute. Custom values are common — companies use their own naming. Normalization is essential for cross-company analysis.
- **Project Subtype** (`pa-project-subtype`): Further classification within primary project type — customer-defined refinement. Examples: 'Class A Office', 'Acute Care', 'Fulfillment Center', 'Garden-Style Apartments', 'Charter School'. [None — customer-defined | Low | Class A Office, Acute Care, Fulfillment Center, Garden-Style Apartments, Charter School, Strip Mall,]
  - No industry standard for subtypes. Only useful when a company has 20+ projects of the same subtype to enable meaningful comparison.
- **Sector** (`pa-sector`): Public vs. private funding and ownership — determines procurement rules, bonding requirements, prevailing wage, and compliance burden. Public projects have transparency requirements and standardized procurement. [Federal Acquisition Regulation (FAR) | Medium | Private, Public – Federal, Public – State, Public – Local / Municipal, Institutional, Non-Profit, Pu]
  - Public projects have prevailing wage, bonding, and procurement requirements that add 10-30% to labor cost. P3 is growing.
- **Work Type** (`pa-work-type`): New construction vs. renovation vs. addition — fundamentally different risk and cost profiles. Renovation projects have 2-3x the change order rate of new construction due to unknown existing conditions. [None — industry-standard categories | Medium | New Construction, Renovation / Remodel, Addition, Tenant Improvement / Fit-Out, Demolition, Historic]
  - Renovation projects have 2-3x change order rates. Existing conditions discovery is the #1 source of changes. Always filter by work type before benchmarking.
- **Program Type** (`pa-program-type`): Owner's capital program classification — groups projects by investment purpose across a portfolio. Useful for owners running rollout or prototype programs (retail chains, QSR, healthcare clinics) where standardized scope enables tight benchmarking. [None — customer-defined | Low | Capital Improvement, Maintenance & Repair, Expansion, Deferred Maintenance, Prototype Rollout, New M]
  - Rollout / prototype programs (retail, QSR, healthcare clinics) have distinct benchmarking needs. Standardized scope enables tighter comparison.

**Financial**
- **Estimated Value** (`pa-estimated-value`): Owner's initial budget or estimated total project cost at authorization — the 'what we thought it would cost' baseline. Set before contracts are awarded. Different from contract value (which is the GC agreement). [AACE Classification System (Class 1-5 Estimates) | High | $0 – $10B+ (wide range by type: $500K TI to $5B+ mega-project)]
  - Often the number used when the project is first created. May be a rough estimate (Class 5) or detailed estimate (Class 1). Precision matters for benchmarking.
- **Contract Value** (`pa-contract-value`): Contracted amount between owner and GC/CM — the GMP, lump sum, or negotiated target. This is the number subcontractors and the market see. Updated via change orders over the project lifecycle. Represents the GC's contractual obligation. [AIA A101/A133 (contract forms) | High | $0 – $10B+ (GMP, lump sum, or negotiated)]
  - GMP, lump sum, or negotiated. May differ significantly from estimated value. Change orders modify this over time.
- **Total Value Band** (`pa-total-value-band`): Bucketed range for benchmarking by project scale — log-scale bands work better than linear because construction costs, risks, and outcomes don't scale linearly. [ENR Project Cost Ranges | High | < $1M, $1M–$5M, $5M–$10M, $10M–$25M, $25M–$50M, $50M–$100M, $100M–$250M, $250M–$500M, $500M–$1B, > $]
  - Band thresholds should align with industry norms and data distribution. Log-scale bands work better than linear.
- **Cost per SF** (`pa-cost-per-sf`): Total project cost divided by gross building area — the most comparable unit cost metric across building projects. Only meaningful for building projects (not infrastructure). Varies enormously by type: warehouse $100-200/SF vs. [RS Means Square Foot Cost Data | Medium | $100–$1,500+/SF depending on type, region, and complexity]
  - Only meaningful for building projects. Varies enormously by type and region. Must normalize by type, region, and year.
- **Hard Cost** (`pa-hard-cost`): Direct construction cost excluding soft costs (design fees, permits, FF&E, land, financing). Typically 60-80% of total project cost. Isolates construction cost from owner's total investment. Essential for apples-to-apples cost benchmarking. [AACE Recommended Practice 10S-90 | Low | 60-80% of total project cost (varies by delivery method and owner cost structure)]
  - Hard cost vs. total cost distinction matters. Some customers track only hard cost; others include soft costs. Always clarify definition.
- **Contingency Budget** (`pa-contingency-budg`): Owner and/or GC contingency allowance at project start — the risk reserve. Owner contingency covers scope changes; GC contingency covers construction risks. How fast contingency burns is a leading indicator of project risk. [AACE Recommended Practice 40R-08 (Contingency Estimating) | Low | 3-10% of contract value (varies by project risk profile: 3% for simple, 10% for complex renovation)]
  - Separate owner contingency from GC contingency. Owner contingency covers scope; GC covers construction risk.
- **Final Cost at Completion** (`pa-final-cost-at`): Actual total cost when project is complete — includes all change orders, allowance adjustments, and final settlements. The gap between contract value and final cost is the most important financial performance indicator. [AACE Recommended Practice 10S-90 | Medium | $0 – $10B+ (final cost = contract value + all approved changes)]
  - Only available after project completion. Average cost growth is 4-8% for well-managed projects, 15-25% for poorly managed or complex renovations.

**Location**
- **Address** (`pa-address`): Street address of the project site — source for all derived geographic attributes. Geocoding converts address to latitude/longitude for distance, climate zone, and cost index calculations. [None — standard address format | High | Street address, city, state, ZIP]
  - Source for all derived geographic attributes. Quality of address data varies — some projects use office address instead of site address.
- **City** (`pa-city`): City or municipality where the project is located — enables local market analysis. Labor rates, material costs, and subcontractor availability vary significantly by metro area. [None — geographic standard | High | Any city name (top metros: New York, Los Angeles, Chicago, Houston, Phoenix, Dallas, etc.)]
  - City-level benchmarks useful for large metros with enough project volume. Suburban vs. urban within a metro also matters.
- **State / Province** (`pa-state-province`): State or province jurisdiction — major benchmarking dimension. State drives labor law (prevailing wage, right-to-work), building code edition, licensing requirements, and tax structure. Top 20 US states cover 80%+ of commercial construction volume. [None — ISO 3166-2 | High | US states, Canadian provinces, etc.]
  - State drives prevailing wage, right-to-work, building code edition, and licensing. Major benchmarking dimension.
- **Country** (`pa-country`): Country where the project is located — relevant for international benchmarking. Most construction data models are US-centric. International projects require currency normalization and different code/standard references. [ISO 3166-1 | High | US, Canada, UK, Australia, etc.]
  - Most construction analytics are US-centric. International expansion requires localized cost indices and code frameworks.
- **ZIP / Postal Code** (`pa-zip-postal-code`): Postal code of the project site — enables micro-market analysis and cost index application. RS Means and other cost databases use ZIP code for location cost factors. [USPS ZIP Code system | High | Standard postal format (US: 5-digit or ZIP+4)]
  - RS Means and other cost databases index by ZIP. Location cost factors range from 0.7 (rural South) to 1.4 (Manhattan).
- **Climate Zone** (`pa-climate-zone`): ASHRAE or IECC climate zone based on project location — drives envelope design, energy code compliance, and expected weather delay days. Zone 1 (hot-humid) to Zone 8 (subarctic) have fundamentally different design and construction requirements. [ASHRAE Standard 169 | None | Zone 1A through Zone 8 (ASHRAE 169)]
  - Climate zone drives envelope R-value, HVAC sizing, and expected weather delay days. Can be auto-derived from location.
- **Seismic Design Category** (`pa-seismic-design`): ASCE 7 seismic classification based on site soil conditions and proximity to faults. Higher SDC = more expensive structure and connections. [ASCE 7 | None | A (lowest), B, C, D0, D1, D2, E, F (highest). Most of California and Pacific NW = D or higher]
  - SDC D+ adds 5-15% to structural cost. Seismic bracing for MEP is an additional cost often missed in early estimates.
- **Region** (`pa-region`): Geographic region for market-level analysis — aggregates state-level data for regional trends. Region definitions vary by organization but should align with labor market and cost index boundaries. [ENR Regional Cost Data | Low | Northeast, Southeast, Midwest, Southwest, Mountain West, Pacific Northwest, Pacific Southwest, Gulf ]
  - Region definitions vary by organization. Should align with labor market boundaries and cost index regions.

**Schedule**
- **Planned Start Date** (`pa-planned-start`): Scheduled construction start date — typically Notice to Proceed (NTP) or mobilization date. The contractual baseline against which all schedule performance is measured. Some owners define this as first day of site work; others use NTP date. [AIA A201 | High | ISO 8601 date (YYYY-MM-DD)]
  - NTP is most common definition. Variance between planned and actual start captures pre-construction delays.
- **Actual Start Date** (`pa-actual-start`): Actual date construction work began on site — may differ from planned start due to permitting, financing, or design delays. The gap between planned and actual start captures pre-construction schedule risk. [None — project-specific | High | ISO 8601 date (YYYY-MM-DD)]
  - Variance between planned and actual start captures permitting, financing, and design delays.
- **Planned Completion Date** (`pa-planned-completi`): Contractual substantial completion date — when the owner can occupy the facility. Different from final completion (all punch items done, all contracts closed). Most contracts use substantial completion as the contractual milestone. [AIA A201 (Substantial Completion) | High | ISO 8601 date (YYYY-MM-DD)]
  - Substantial completion (owner can occupy) vs. final completion (all punch done, all contracts closed). Most contracts use substantial.
- **Actual Completion Date** (`pa-actual-completio`): Actual date of substantial completion — only available when the project reaches that milestone. The gap between contractual and actual completion is the core schedule performance metric. Average schedule growth is 10-20% for well-managed projects. [None — project-specific | Medium | ISO 8601 date (YYYY-MM-DD)]
  - Only available when project completes. Average schedule growth is 10-20%. Renovation projects have higher growth.
- **Planned Duration** (`pa-planned-duration`): Contractual construction duration in calendar days from NTP to substantial completion. Industry typically uses calendar days for overall duration (not working days). Excludes pre-construction. [PMI PMBOK Schedule Management | Medium | 2–60+ months (typical: 6-24 months for commercial, 24-48 for healthcare, 36-60 for infrastructure)]
  - Calendar days vs. working days must be specified. Industry uses calendar days for overall duration.
- **Actual Duration** (`pa-actual-duration`): Actual construction duration from start to substantial completion — compare to planned duration for schedule performance, compare to benchmarks by type/size for relative performance. [None — project-specific | Medium | 2–60+ months]
  - Compare to planned for growth. Compare to type/size benchmarks for relative performance.
- **Preconstruction Duration** (`pa-preconstruction`): Time from design authorization to NTP — often ignored but significantly affects construction outcomes. Design-build and CMAR compress this phase. DBB has the longest preconstruction. [AIA B101 (Design Services) | Low | 2–24+ months (DBB: 12-24, CMAR: 6-18, DB: 3-12)]
  - Design-build compresses preconstruction but shifts risk. Longer preconstruction often means fewer surprises in the field.
- **Season of Start** (`pa-season-start`): Season when construction begins — affects early work scope and weather delay risk. Winter starts in cold climates (ASHRAE zones 5-8) face frozen ground, concrete cold weather protection, and shorter daylight hours. [None — derived from start date | Medium | Spring (Mar-May), Summer (Jun-Aug), Fall (Sep-Nov), Winter (Dec-Feb)]
  - Winter starts in climate zones 5-8 face frozen ground, concrete protection, and shorter days. Can be auto-derived from start date.

**Procurement**
- **Delivery Method** (`pa-dlvy-method`): Project delivery system defining the design-construction relationship — one of the strongest predictors of project outcomes. DBB separates design and construction (owner bears coordination risk). [AIA A201 / A133 / A141 | Low | Design-Bid-Build (DBB), Construction Manager at Risk (CMAR / GMP), Design-Build (DB), CM as Agent (C]
  - CMAR/GMP most common for large commercial. DBB dominant in public. DB growing in infrastructure. IPD rare but lowest change rate.
- **Contract Type** (`pa-contract-type`): Compensation structure between owner and GC/CM — determines who bears cost risk. GMP: GC bears overrun risk above the guaranteed maximum. Lump Sum: GC bears all cost risk. Cost Plus: owner bears cost risk. [AIA A101 (Lump Sum) | Low | Lump Sum / Stipulated Sum, Guaranteed Maximum Price (GMP), Cost Plus Fixed Fee, Cost Plus Percentage]
  - GMP: GC bears overrun risk. Lump Sum: GC bears all risk. Cost Plus: owner bears risk. Dramatically affects financial benchmarks.
- **Bid Type** (`pa-bid-type`): How the contractor was selected — affects pricing competitiveness and project relationship dynamics. Open competitive typically yields lowest initial price but highest change order rate. [Federal Acquisition Regulation (FAR) | None | Competitive Bid (Open), Competitive Bid (Invited / Select), Negotiated, Sole Source / Direct Award, ]
  - Open competitive yields lowest bid but often highest final cost. Negotiated/QBS yields higher initial price but lower total cost.
- **Bonding Requirement** (`pa-bonding-requirem`): Whether performance and payment bonds are required — adds 1-3% to cost and limits the contractor pool to firms with adequate bonding capacity. Federal projects over $250K require bonds (Miller Act). [Miller Act (Federal) | None | Fully Bonded (Performance + Payment), Payment Bond Only, No Bond Required, Subcontractor Bonds Requi]
  - Public projects over $250K require bonds (Miller Act). Bonding capacity limits contractor pool. Bond cost passed to owner.
- **Prevailing Wage** (`pa-prevailing-wage`): Whether prevailing wage requirements apply — adds 10-30% to labor cost depending on market differential between prevailing and market rates. Federal (Davis-Bacon) and state prevailing wage laws apply to public projects. [Davis-Bacon Act (Federal) | None | Yes, No]
  - Federal and state prevailing wage laws apply to public projects. Some private projects trigger it through public incentives.
- **Union / Open Shop** (`pa-union-open-shop`): Labor agreement type on the project — affects labor rates, productivity assumptions, and trade jurisdiction rules. Union projects have higher hourly rates but potentially different productivity. [NLRA | None | Union (Closed Shop), Open Shop, Project Labor Agreement (PLA), Mixed]
  - Union projects have higher hourly rates. PLAs common on large public projects. Trade jurisdiction rules affect crew composition.

**Building**
- **Gross Building Area** (`pa-gross-building`): Total enclosed floor area including all floors — the primary size dimension for cost benchmarking. Gross area includes occupied, mechanical, circulation, and wall space. Different from rentable or usable area. [ASTM E1836 (Standard Classification for Building Floor Area) | Medium | 500 – 10M+ SF (typical commercial: 10K-500K SF)]
  - Definition matters: gross, net, rentable, usable are different numbers. Ensure apples-to-apples when benchmarking cost/SF.
- **Number of Stories Above Grade** (`pa-number-stories`): Count of floors above ground level — affects structural system, vertical transportation requirements, fire protection, and egress. [IBC Chapter 5 (Height and Area) | Medium | 1–100+ (low-rise: 1-3, mid-rise: 4-7, high-rise: 7+)]
  - High-rise (7+ stories / 75+ ft) requires different structural systems, fire protection, and egress. Each floor adds cost premium.
- **Number of Stories Below Grade** (`pa-number-stories-2`): Count of floors below ground level (basement levels) — below-grade construction costs 1.5-3x above-grade per SF due to excavation, shoring, waterproofing, and dewatering. Parking structures below grade are common in urban settings. [IBC | Low | 0–5+ (most common: 0-2)]
  - Below-grade space: excavation, shoring, waterproofing, dewatering. Underground parking is $50-80K/space.
- **Building Height** (`pa-building-height`): Height from grade to highest occupied floor or roof peak — triggers high-rise code requirements (typically 75+ ft). Determines crane type (tower vs. mobile), wind load design, and elevator requirements. [IBC Chapter 5 | Low | 10–2000+ ft (low-rise: <75 ft, high-rise: 75+)]
  - Height triggers high-rise code requirements at 75+ ft. Determines crane type. Affects wind load design.
- **Site Area** (`pa-site-area`): Total area of the project site — affects logistics, staging, and site improvement cost. Tight urban sites increase logistics cost due to limited staging, laydown, and equipment access. Large sites increase paving, utilities, and landscaping scope. [None — project-specific | Low | 0.1–1000+ acres (urban infill: 0.1-1, suburban: 1-20, campus: 20-100)]
  - Tight urban sites increase logistics cost. Large sites increase scope. Footprint-to-site ratio indicates density.
- **Structural System** (`pa-struct-system`): Primary structural framing system — the single biggest cost and schedule driver for any building. Steel frame: faster erection, lighter foundation. Concrete frame: potentially cheaper for regular grids, longer cycle time. [AISC | Low | Steel Frame, Concrete Frame (CIP), Precast Concrete, Wood Frame (Light), Mass Timber, Masonry Bearin]
  - Structural system is the single biggest cost driver. Steel vs. concrete vs. mass timber have fundamentally different cost and schedule profiles.
- **Foundation Type** (`pa-foundation-type`): Primary foundation system — driven by geotechnical conditions, not project type. Deep foundations (driven piles, drilled shafts) add $20-100/SF to substructure cost vs. shallow foundations (spread footings). [ASCE 7 | None | Spread Footings, Mat / Raft Foundation, Driven Piles, Drilled Shafts (Caissons), Micropiles / Helica]
  - Foundation type driven by geotechnical conditions. Deep foundations add $20-100/SF. Pile driving has noise/vibration impacts.
- **Number of Units** (`pa-number-units`): Count of individual units — apartments, hotel rooms, patient rooms, beds, or seats. Per-unit cost is the primary benchmark for residential, hospitality, and healthcare. Only applicable for certain building types. [None — type-specific unit definition | Low | 1–5000+ (apartments: 50-500, hotel rooms: 100-1000, hospital beds: 50-500)]
  - Only applicable for certain types: multi-family, hospitality, healthcare, education. Unit definition varies by type.
- **Parking Type** (`pa-parking-type`): Type of parking provided — parking structure can be 15-25% of total project cost. Underground parking is most expensive ($50-80K/space). Structured above-grade: $20-40K/space. Surface: $2-5K/space. [IBC | None | Surface Lot, Structured Garage (Above Grade), Underground Garage, Podium / Pedestal, No Parking, Mec]
  - Underground parking is the most expensive ($50-80K/space). Often 15-25% of total project cost.
- **Construction Type** (`pa-const-type`): IBC construction type classification — determines allowable building height and area, required fire-resistance ratings for structural elements, and material restrictions. [IBC Chapter 6 (Types of Construction) | None | Type I-A (Fire Resistive / Protected), Type I-B, Type II-A, Type II-B, Type III-A, Type III-B, Type ]
  - Type I-A is most expensive (full fire resistance). Type V-B is cheapest (no fire resistance). Type IV (mass timber) is emerging.
- **Occupancy Group** (`pa-occupancy-group`): IBC occupancy classification — drives code requirements for occupant load, egress, fire protection, accessibility, and special inspections. I-2 (hospitals) is the most demanding occupancy. [IBC Chapter 3 (Use and Occupancy) | None | A (Assembly), B (Business), E (Educational), F (Factory), H (High Hazard), I (Institutional), M (Mer]
  - I-2 (hospitals) is most demanding. Occupancy group determines sprinkler requirements, exit width, accessibility.
- **Building Code Edition** (`pa-building-code`): Edition of the building code adopted by the jurisdiction — affects energy, structural, and accessibility requirements. Jurisdictions adopt different editions on different timelines. Newer codes have stricter energy requirements. [IBC (2015 / 2018 / 2021 / 2024) | None | IBC 2015, IBC 2018, IBC 2021, IBC 2024, California Building Code, NYC Building Code, Local amendment]
  - Jurisdictions adopt different editions on different timelines. Local amendments can be significant (NYC, CA).
- **Fire Sprinkler Requirement** (`pa-fire-sprinkler`): Whether automatic fire sprinklers are required or provided — sprinkler cost is $3-8/SF but allows construction type trade-offs (increased height and area under IBC). Almost all new commercial and multi-family construction is now fully sprinklered. [NFPA 13 / 13R / 13D | None | Fully Sprinklered (NFPA 13), Partially Sprinklered, No Sprinkler Required, NFPA 13R (Residential), N]
  - Sprinklers allow increased height and area under IBC. Trade-off: sprinkler cost vs. structural savings.
- **Accessibility Standard** (`pa-accessibility-st`): Applicable accessibility standard — affects interior layout, restroom count, fixture selection, and door hardware. ADA applies to all commercial and public buildings. Fair Housing Act applies to multi-family (4+ units). [ADA | None | ADA (Federal), State Accessibility Code, Fair Housing Act (FHA), ADA + State (most common), Section ]
  - ADA applies to all commercial/public. FHA applies to multi-family (4+ units). State codes often exceed ADA.

**Standards**
- **LEED Certification** (`sc-leed-certificati`): LEED certification level targeted or achieved — the most widely recognized green building standard. LEED adds 2-8% to construction cost depending on level. Gold is the most common target for institutional and corporate projects. [USGBC LEED v4 / v4.1 | Low | None, LEED Certified, LEED Silver, LEED Gold, LEED Platinum, Pursuing (level TBD)]
  - LEED Gold is the most common target for institutional/corporate. Platinum adds most cost. Adds commissioning and documentation requirements.
- **WELL Certification** (`pa-well-certificati`): WELL Building Standard certification level — focuses on occupant health and wellness (air quality, water quality, light, fitness, comfort). Growing adoption in corporate office and multi-family. Adds operational requirements beyond construction. [International WELL Building Institute (IWBI) | None | None, WELL Silver, WELL Gold, WELL Platinum, Pursuing]
  - WELL focuses on air, water, light, fitness, comfort. Adds operational monitoring beyond construction.
- **Energy Code** (`pa-energy-code`): Energy code or standard the project must meet — becoming a bigger cost driver as standards tighten. Energy code determines insulation R-values, glazing performance, HVAC efficiency, and lighting power density. [ASHRAE 90.1 (2016/2019/2022) | None | ASHRAE 90.1-2019, ASHRAE 90.1-2022, IECC 2021, IECC 2024, Net Zero, Passive House, Local energy code]
  - Energy code is becoming a bigger cost driver as standards tighten. Net Zero adds 10-25% premium. Envelope and HVAC most affected.
- **Net Zero Target** (`pa-net-zero-target`): Whether the project targets net-zero energy consumption — requires on-site renewable energy (typically solar), high-performance envelope, and ultra-efficient MEP systems. Adds 10-25% to construction cost. [DOE Zero Energy Ready Home | None | Yes, No]
  - Net zero requires PV, high-performance envelope, and efficient MEP. Growing requirement from institutional owners.
- **Resilience Requirements** (`pa-resilience-requi`): Special requirements for disaster resilience — essential facilities (hospitals, fire stations, EOCs) must remain operational post-disaster. Requires enhanced structural, MEP, and envelope systems beyond standard code. [ASCE 7 (Risk Categories) | None | None, Flood Zone (FEMA), Hurricane / Wind Zone, Seismic (Above Code), Essential Facility (Post-Disas]
  - Essential facilities (hospitals, fire stations, EOCs) must remain operational post-disaster. Flood zone adds elevation and waterproofing cost.

**Organization**
- **Owner Type** (`pa-owner-type`): Type of entity that owns the project — drives procurement method, bonding requirements, and decision-making speed. Private developers prioritize speed and cost. Public owners have procurement rules and transparency requirements. [None — industry categories | Medium | Private Developer, Private Corporate (Owner-Occupied), Public – Federal, Public – State, Public – Lo]
  - Private developers move fast. Public owners have procurement rules. Institutional owners have long approval chains.
- **GC / CM Firm** (`pa-gc-cm-firm`): General contractor or construction manager firm name — enables contractor-level performance benchmarking across projects. With enough data: compare change order rates, schedule performance, safety records, and cost outcomes by contractor. [None — company name | High | Company name (ENR Top 400 contractors, regional firms, local builders)]
  - Contractor performance benchmarking requires 10+ projects per firm for statistical validity. ENR Top 400 provides industry context.
- **Architect of Record** (`pa-architect-record`): Architect responsible for design and construction administration — A/E firm performance significantly affects construction outcomes. Firms with higher document quality produce fewer RFIs and change orders. [None — company name | Medium | Company name (AIA member firms, regional and national)]
  - A/E firm performance significantly affects construction outcomes. Document quality correlates inversely with RFI and change order rates.
- **Number of Subcontractors** (`pa-number-subcontra`): Total count of subcontractor firms on the project — a proxy for project complexity. More subs = more coordination overhead, more meetings, more potential conflicts. A 100-sub project is fundamentally different from a 20-sub project. [None — derived from project data | High | 10–200+ (simple: 10-20, typical commercial: 30-60, complex healthcare: 80-200)]
  - Affected by self-perform strategy. GCs that self-perform more have fewer subs but more direct labor.
- **Peak Workforce** (`pa-peak-workforce`): Maximum number of workers on site during peak construction — a labor intensity metric. Peak workforce / SF indicates labor density. High peak on a constrained site creates safety and logistics challenges. [OSHA Multi-Employer Worksite Policy | Medium | 10–5000+ (typical commercial: 50-300, mega-project: 1000-5000)]
  - High peak on constrained site creates safety challenges. Peak timing typically aligns with MEP rough-in or finishes.
- **Self-Performed Work** (`pa-self-performed`): Percentage of work self-performed by the GC (not subcontracted) — affects risk profile and cost structure. Most GCs self-perform 5-15% (general conditions, concrete, carpentry). Trade-specific GCs may self-perform 40-60%. [AGC | None | 0%–60%+ (most GCs: 5-15%, specialty GCs: 40-60%)]
  - Most GCs self-perform 5-15% (GC, concrete, carpentry). Trade-specific GCs self-perform 40-60%.

**Scope**
- **New vs. Existing** (`pa-new-vs-existing`): Whether the project involves existing structures or is entirely new — renovation content fundamentally changes cost and risk. Existing conditions discovery is the #1 source of changes on renovation projects. [None — industry categories | Low | 100% New Construction, Primarily New with Minor Existing, Mixed New + Renovation, Primarily Renovati]
  - Renovation projects have 2-3x change order rates. Existing conditions discovery is the #1 source of changes.
- **Occupied During Construction** (`pa-occupied-during`): Whether the building or adjacent spaces are occupied during construction work — adds logistics constraints, safety requirements, work hour restrictions, noise/vibration limits, and security requirements. [OSHA Multi-Employer Worksite | None | Yes, No]
  - Adds 10-25% to schedule. Requires temporary partitions, phased shutdowns, and after-hours work. Healthcare ICRA requirements are especially demanding.
- **Phased Construction** (`pa-phased-const`): Whether the project is built in distinct phases with partial occupancy or turnover between phases. Each phase requires its own punch list, inspections, and turnover. [None — project-specific | None | Yes, No]
  - Each phase needs its own punch list and inspections. Temporary barriers and life safety between phases add cost.
- **Fast-Track** (`pa-fast-track`): Whether design and construction overlap — construction starts on early packages (sitework, foundations) while later packages (MEP, interiors) are still being designed. [CII Fast-Track Construction Research | None | Yes, No]
  - Fast-track means construction starts before design is complete. Higher RFI and change rate. Common with CMAR and DB delivery.
- **Site Constraints** (`pa-site-constraints`): Notable constraints on the construction site — multiple constraints compound and fundamentally change project complexity. [None — project-specific | None | Urban / Constrained Site, Adjacent Occupied Buildings, Environmental Contamination, High Water Table]
  - Multiple constraints compound. Environmental contamination adds remediation cost and schedule. Urban sites limit equipment and staging.
- **BIM Requirement** (`pa-bim-requirement`): Level of Building Information Modeling required on the project — BIM adoption level correlates with coordination quality and clash detection effectiveness. LOD 300-350 is becoming standard for commercial projects above $25M. LOD 400 for complex MEP. [AIA E203 (BIM Protocol) | None | None, LOD 200 (Design Coordination), LOD 300 (Construction Coordination), LOD 350 (Trade Coordinatio]
  - LOD 300-350 standard for commercial $25M+. LOD 400 for complex MEP. BIM investment reduces field coordination issues.
- **Modular / Prefab Content** (`pa-modular-prefab`): Percentage of construction using off-site prefabrication or modular methods — shifts labor from field to factory. Reduces on-site workforce peak but requires earlier procurement and more detailed coordination. [Modular Building Institute (MBI) | None | None, Light Prefab (<15%: MEP racks / wall panels), Moderate Prefab (15-40%: bathroom pods / headwal]
  - Shifts labor from field to factory. Reduces on-site peak but requires earlier procurement. Quality typically higher.
- **Specialty Systems** (`pa-specialty-system`): Notable specialty building systems that add cost, schedule, and coordination complexity — specialty systems often have proprietary vendors, long lead times, and complex commissioning requirements. [None — type-specific | None | Central Plant, Clean Room, Vivarium, Surgical Suite, Commercial Kitchen, Natatorium / Pool, Auditori]
  - A hospital with OR suites, labs, and clean rooms costs 3-5x per SF more than a standard office for MEP alone.

**Performance**
- **Project Status** (`pa-project-status`): Current state of the project in its lifecycle — determines what data is available and how the project should be treated in benchmarks. Only closed/archived projects have final cost and schedule data. Active projects have in-progress metrics. [PMI PMBOK Project Lifecycle | High | Pre-Construction, Active Construction, On Hold, Substantially Complete, Final Completion, Warranty P]
  - Only closed projects have final data. Active projects show in-progress metrics. Cancelled should be excluded from benchmarks.
- **Current Phase** (`pa-current-phase`): Current construction phase based on the phases taxonomy — enables phase-aware analytics and 'where should you be at this point' benchmarks. [None — derived from project activity patterns | Low | Preconstruction, Procurement, Mobilization, Sitework & Foundations, Structure, Building Enclosure, M]
  - Phase classification enables 'where should you be' benchmarks. Requires either manual tagging or inference from activity data.
- **Percent Complete** (`pa-percent-complete`): Overall project completion percentage — multiple methods: cost-based (earned value), milestone-based, or units-based. Cost-based is most common for overall project. [PMI PMBOK Earned Value Management | Medium | 0%–100%]
  - Method matters: cost-based, milestone-based, or units-based produce different numbers. Always specify method.
- **Earned Value — CPI** (`pa-earned-value-cpi`): Cost Performance Index — the most reliable predictor of final cost performance. Calculation: BCWP (Budgeted Cost of Work Performed) / ACWP (Actual Cost of Work Performed). CPI < 1.0 means over budget. [PMI PMBOK EVM | Low | 0.5–1.5 (1.0 = on budget, <1.0 = over budget, >1.0 = under budget)]
  - CPI rarely recovers after 20% complete. Industry-validated predictive metric. Requires disciplined cost and schedule tracking.
- **Earned Value — SPI** (`pa-earned-value-spi`): Schedule Performance Index — measures schedule efficiency. Calculation: BCWP (Budgeted Cost of Work Performed) / BCWS (Budgeted Cost of Work Scheduled). SPI < 1.0 means behind schedule. [PMI PMBOK EVM | Low | 0.5–1.5 (1.0 = on schedule, <1.0 = behind, >1.0 = ahead)]
  - SPI is less reliable than CPI as a predictor. Schedule recovery is more achievable through acceleration and overtime.

**Standard Measures**
- **Cost Growth** (`pa-cost-growth`): Percentage increase from contract value to final cost at completion — the most important financial performance metric in construction. Calculation: (Final Cost − Contract Value) / Contract Value × 100. [AACE Recommended Practice 10S-90 | Medium | 4-8% (well-managed), 10-15% (typical), 15-25% (complex renovation)]
  - Only available on completed projects. Must normalize by work type (new vs. renovation) and delivery method.
- **Schedule Growth** (`pa-schedule-growth`): Percentage increase from planned to actual duration — the core schedule performance metric. Calculation: (Actual Duration − Planned Duration) / Planned Duration × 100. Average is 10-20% for well-managed projects. [CII Benchmarking | Medium | 5-10% (well-managed), 10-20% (typical), 20-40% (complex renovation)]
  - Must normalize by work type and delivery method. Fast-track projects have compressed planned duration, affecting growth calculation.
- **Change Order Rate** (`fi-chg-order-rate`): Total approved change order value as percentage of original contract value — measures scope stability and document quality. Calculation: Total CO Value / Original Contract Value × 100. [AACE | High | 3-5% (simple new), 5-10% (typical new), 10-15% (complex new), 15-25% (renovation)]
  - Low CO rate may indicate suppressed changes (scope buried in allowances) rather than good performance.
- **RFI Density** (`pa-rfi-density`): Number of RFIs per $1M of contract value — measures document quality and design completeness. High RFI density correlates with incomplete documents, aggressive fast-track schedule, or complex design. [CII Document Quality Research | High | 10-20 RFIs/$1M (good documents), 20-40 (typical), 40+ (poor documents or fast-track)]
  - High RFI density = incomplete documents or complex design. DB typically has lower RFI density than DBB.
- **Safety Incident Rate (TRIR)** (`pa-safety-incident`): Total Recordable Incident Rate — OSHA-standard safety metric. Calculation: (Total Recordable Incidents × 200,000) / Total Labor Hours Worked. Industry average is 2.5-3.5 for commercial construction. Lower is better. [OSHA 300 Log | Medium | 0.5-1.0 (excellent), 1.0-2.5 (good), 2.5-3.5 (average), 3.5+ (poor)]
  - Observation frequency (leading indicator) predicts TRIR (lagging indicator). Projects with higher observation rates have lower TRIR.
- **Punch Item Density** (`qsr-punch-item-3`): Number of punch items per 1000 SF at substantial completion — measures overall quality of installed work. High density indicates quality issues during construction. Typical: 2-5 items per 1000 SF for well-managed projects. [None — industry practice | High | 1-2/1000 SF (excellent), 2-5 (typical), 5-10 (poor), 10+ (significant quality issues)]
  - Paint/finish is consistently #1 punch category across all project types. High punch density correlates with longer closeout duration.
- **Submittal Approval Rate** (`pa-submittal-appr`): Percentage of submittals approved on first submission — measures specification clarity, subcontractor preparation quality, and A/E review efficiency. Calculation: First-Submission Approvals / Total Submittals × 100. [None — industry practice | High | 70-80% first-pass (good), 60-70% (typical), <60% (poor specs or preparation)]
  - Re-submittals compound schedule delay — each re-sub adds 2-4 weeks. First-pass rate correlates with document quality.

### Quality & Safety Records

**Observations**
- **Observation** (`qsr-observation`): A documented finding from a site walk or inspection — captures conditions, hazards, deficiencies, or noteworthy items during active construction. The primary during-construction quality and safety signal. [OSHA 29 CFR 1926 (safety) | High | Quality, Safety, Environmental, Commissioning, Warranty, Work to Complete]
  - observation.name is the classification field for keyword clustering (18 validated issue categories). type_name is severity, NOT issue type. trade_id exists but has NO lookup table — dead end for V1.
- **Safety Observation** (`qsr-safety-observati`): An observation with category = 'Safety' — documents hazards, unsafe conditions, and safety compliance findings during site walks. [OSHA 29 CFR 1926 (Construction Safety) | High | Fall Protection, Struck By, Electrical, Caught In/Between, Housekeeping, PPE, Scaffolding, Excavatio]
  - hazard_name is 45.4% null — only 55% of safety obs have structured hazards. Corrective action linkage is sparse (1.2% via incident_action).
- **Quality Observation** (`qsr-quality-observat`): An observation with category = 'Quality' — documents workmanship deficiencies, material issues, and quality non-conformances during active construction. The strongest during-construction quality signal. [ISO 9001 §8.7 (Control of Nonconforming Outputs) | High | Corrective Action, Deficiency, Non-Conformance]
  - Quality observations + punch items form the dual-signal model for Common Quality Issues (insight #4). Observations are during-construction; punch items are closeout. Combined: 12,556 unique companies.
- **Environmental / Commissioning Observation** (`qsr-enviro-cx`): Observations with category = 'Environmental' or 'Commissioning' — documents environmental compliance findings (erosion control, dust, spills) and commissioning findings (system performance, functional testing results, equipment issues). [EPA NPDES (environmental) | Medium | Environmental: erosion, sediment, spill, dust, dewatering. Commissioning: functional test, performan]
  - Environmental and Commissioning observations follow the same data structure but serve different compliance purposes.

**Inspections**
- **Inspection** (`qsr-insp`): A formal structured examination of work against defined criteria — conducted by quality managers, safety officers, third-party inspectors, or regulatory authorities. [ISO 9001 §8.6 (Release of Products) | High | Safety, Quality, Commissioning, Pre-pour, Pre-cover, Structural, Electrical, Fire Protection, Enviro]
  - inspections.group values are lowercase ('quality', 'safety') but 93% null — nearly useless for categorization. Inspection type is the better filter.
- **Inspection Item** (`qsr-insp-item`): An individual line item within an inspection checklist — the atomic unit of conformance checking. Key properties: name (item description), status (structured, capitalized: 'Conforming', 'Deficient', 'Not Applicable', 'Uninspected', 'Neutral'). [ISO 9001 checklist requirements | High | Conforming, Deficient, Not Applicable, Uninspected, Neutral]
  - inspection_items.status values are CAPITALIZED ('Deficient' not 'deficient'). Recurring deficiency detection: same item name × project × inspection type.
- **Scheduled Inspection** (`qsr-scheduled-insp`): A recurring or planned inspection defined in advance — ensures systematic compliance checking on a regular cadence. Tracks inspection frequency, assigned inspector, and schedule compliance. [OSHA periodic inspection requirements | High | Daily safety walk, weekly quality audit, monthly fire protection check, pre-pour inspection, pre-cov]
  - Scheduled inspection adherence rate = actual inspections / scheduled inspections. Low adherence signals resource constraints or deprioritized quality/safety programs.
- **Third-Party / Special Inspection** (`qsr-third-party`): An inspection conducted by an independent testing or inspection agency — required by building codes for structural, fire protection, and other critical systems. [IBC §1704 (Special Inspections) | Medium | Structural steel (welding, bolting), concrete (pre-pour, placement, curing), fireproofing, sprinkler]
  - Third-party inspection failures often trigger re-work and schedule delays. Results connect to building elements (which system was inspected) and financial instruments (cost of retesting).

**Punch Items**
- **Punch Item** (`qsr-punch-item`): A documented deficiency or incomplete work item that must be corrected before the owner accepts the project — compiled during substantial completion walkthrough. The strongest closeout quality signal. [AIA A201 §9.8 (Substantial Completion) | High | Open, In Progress, Ready for Review, Closed, Not Accepted]
  - punch_item.name is the classification field (0% null). punch_item_type_name is severity/priority, NOT issue category.
- **Punch Item (by Issue Category)** (`qsr-punch-item-issue`): A categorized view of punch items grouped by the 18 validated issue categories derived from keyword clustering on name field. [No industry standard for issue categorization | High | Paint/Finish (#1 everywhere), Doors/Windows, Electrical, Plumbing/Piping, HVAC, Caulk/Sealant, Hardw]
  - 7 project types with 99–1,358 cos for punch items. 74% of punch items cluster into named categories. This is the core of insight #4 (Common Quality Issues).
- **Punch Item Resolution** (`qsr-punch-item-2`): The lifecycle tracking of a punch item from creation to closure — measures how quickly deficiencies are corrected and by whom. Key properties: workflow_status transitions (with timestamps), assignee response, resolution description, verification. [AIA A201 §9.8 | High | Resolution time typical: 7–30 days for individual items]
  - Resolution time by vendor reveals which subcontractors are responsive to punchlist items. Prolonged punch items block certificate of substantial completion and retainage release.

**Incidents**
- **Incident** (`qsr-incident`): A safety event that results in injury, illness, property damage, near-miss, or environmental release — the formal record of what happened. [OSHA 29 CFR 1904 (Recordkeeping) | High | Near Miss, First Aid, Medical Treatment, Restricted Duty, Lost Time, Fatality]
  - Incidents are the most serious safety signal. OSHA-recordable incidents drive TRIR (Total Recordable Incident Rate).
- **Incident Record** (`qsr-incident-record`): A detailed record within an incident — captures specific injury details, property damage details, or environmental release information. One incident may have multiple records (e.g., two people injured in the same event). [OSHA 29 CFR 1904.7 (General Recording Criteria) | High | Injury (body part, nature, cause), Property Damage (item, extent, cost), Environmental (release type]
  - nature) across trades and project types
- **Incident Witness Statement** (`qsr-incident-witness`): A documented account from a person who witnessed a safety event — captured as part of the incident investigation. Key properties: witness identity, statement text, date. Witness statements support root cause analysis and regulatory compliance. [OSHA investigation requirements | High | Free-text statement with witness identification, date, and signature]
  - Witness statements support incident investigation but are free-text — no structured data for analytics. Volume of witness statements per incident may indicate investigation thoroughness.
- **Corrective Action / Incident Action** (`qsr-corrective-actio`): A required remediation or preventive measure assigned in response to an incident or recurring safety observation. Key properties: action description, assignee, due date, status (Open, In Progress, Complete), linked incident or observation. [ISO 45001 §10.2 (Incident Investigation and Corrective Action) | High | Immediate corrective action, Root cause corrective action, Preventive action, Training, Engineering ]
  - Corrective action completion rate is a key safety program effectiveness metric. Sparse linkage to observations (1.2%) means most corrective actions flow through the incident pathway, not the observati...

**Formal Notices**
- **Safety Violation** (`qsr-safety-violation`): WARNING: daily_log_safety_violation is UNUSABLE for analytics — subject 66% null, vendor_name is free text (no FK). Use observation.category = 'Safety' with hazard_name for structured violation tracking instead. [OSHA 29 CFR 1926 (Construction Safety Standards) | Medium | OSHA Serious, OSHA Other-than-Serious, OSHA Willful, OSHA Repeat]
  - Daily log safety violations validated as UNUSABLE for recurrence tracking (insight #11) — too sparse and unstructured.
- **Non-Conformance Report (NCR)** (`qsr-non-conformance`): A formal documented deviation from specifications, drawings, or quality standards — triggers investigation and disposition (accept as-is, rework, reject/replace). [ISO 9001 §8.7 (Control of Nonconforming Outputs) | Medium | Accept as-is, Rework, Reject and Replace, Use as-is with concession]
  - NCRs bridge quality records to financial instruments — rework disposition drives cost (rework vs. replacement). NCR frequency by specification section identifies problematic design details.
- **Deficiency Notice** (`qsr-deficiency-notic`): A formal written notification to a subcontractor or vendor that their work does not meet contract requirements — triggers contractual obligations to correct. [AIA A201 §12.2 (Correction of Work) | Low | Written notice, Cure period (typically 7–14 days), Backcharge if uncured, Contract termination for r]
  - Deficiency notices connect quality records to financial instruments (backcharges) and organizations (vendor performance).

**Coordination Issues**
- **Coordination Issue** (`qsr-coord-issue`): A design or constructability problem identified during BIM coordination, drawing review, or field coordination — captures clashes, design conflicts, and constructability concerns before they become field problems. [BIM Execution Plan requirements | High | Clash, Coordination, Design Review, Constructability, Requirement Change, Existing Condition, Client]
  - coordination_issue.trade is free text, NOT standardized ('Plumbing' vs '22 Plumbing' vs '22 00 00 Plumbing'). MEP-heavy.
- **Coordination Issue (Design-Related)** (`qsr-coord-issue-2`): Coordination issues with issue_type in (Design Review, Constructability, Requirement Change) — the subset that signals design quality and completeness problems. [AGC BIMForum | High | Design Review, Constructability, Requirement Change]
  - 4,967 coordination issues linked to RFIs via rfi_header_id across 204 cos. Design-typed coordination issues are a V2 signal for insight #31 (Design-Related Change Impact).

**Test Reports**
- **Material Test Report** (`qsr-mat-test-report`): Results of material testing required by specifications and building codes — concrete cylinder breaks, soil compaction tests, steel mill certifications, fireproofing adhesion tests, waterproofing tests. Conducted by independent testing laboratories. [ASTM test standards (C39 concrete, D1557 soil, E119 fire) | Low | Concrete compressive strength, Soil compaction (Proctor), Steel tensile strength, Fireproofing thick]
  - Material test failures trigger rework (re-pour concrete, re-compact soil, replace steel).
- **System Performance Test** (`qsr-system-perf-test`): Results of functional testing for building systems — HVAC air balance, electrical load testing, fire alarm testing, plumbing pressure tests, elevator load tests, generator load bank tests. Conducted during commissioning phase. [ASHRAE standards (HVAC) | Low | HVAC air balance, Electrical load test, Fire alarm test, Plumbing pressure test, Elevator load test,]
  - System performance tests are the quality gate for building system handover. Failed tests trigger commissioning observations and corrective actions.

**Action Plans**
- **Action Plan** (`qsr-action-plan`): A structured set of tasks created in response to quality or safety findings — groups related corrective actions into a trackable plan with assignees, due dates, and approval workflows. [ISO 9001 §10.1 (Improvement) | High | Quality improvement plan, Safety corrective action plan, Environmental remediation plan, Commissioni]
  - Action plans are the management response layer — they organize individual findings into structured remediation.
- **Action Plan Line Item (Task)** (`qsr-action-plan-line`): An individual task within an action plan — the atomic unit of remediation work. Key properties: description, assignee, due date, status, linked record (the source observation, punch item, or incident that triggered this task). [Follows parent action plan standard/format | High | Task description, assignee, due date, status (Open, In Progress, Complete), priority, linked source ]
  - action_plan_line_item_record is the key linkage table — it connects remediation tasks back to the specific observation, punch item, or incident that triggered the action.

**Standard Measures**
- **Observation Density** (`qsr-observation-dens`): Total observations per unit of project size — measures the intensity of quality and safety monitoring. Formula: Total Observations / Project Value (per $M) or Total Observations / Project SF. Can be segmented by category (Quality vs. Safety). [Company-specific safety observation targets | High | Typical: varies widely]
  - Higher observation density correlates with better safety outcomes — proactive identification prevents incidents. Companies with < 10 observations per $M may have underreporting.
- **Deficiency Rate** (`qsr-deficiency-rate`): Percentage of inspection items found deficient — measures quality conformance. Formula: Deficient Items / Total Inspected Items × 100. Can be segmented by inspection type, building system, and trade. [ISO 9001 quality metrics | High | Typical: 2–6% deficiency rate by inspection type]
  - inspection_items.status values are CAPITALIZED. Deficiency rate by trade (via responsible_contractor_id, 48% populated) reveals which subcontractors have quality issues.
- **Punch Item Density** (`qsr-punch-item-3`): Total punch items per unit of project size at substantial completion — measures closeout quality. Formula: Punch Items / Gross SF or Punch Items / Unit Count. Lower density = cleaner handover. [Industry closeout benchmarks | High | Typical: 1–5 punch items per 1,000 SF depending on project type and quality standards]
  - Punch item density is the most widely available quality outcome metric in Procore due to massive adoption.
- **Total Recordable Incident Rate (TRIR)** (`qsr-total-recordable`): The number of OSHA-recordable incidents per 200,000 worker hours — the standard safety performance metric in construction. Formula: (Recordable Incidents × 200,000) / Total Worker Hours. [OSHA 29 CFR 1904 | Medium | Construction industry average: ~3.0]
  - TRIR depends on accurate worker hour tracking (daily_log_manpower) and incident classification. Companies that underreport incidents or overcount hours distort TRIR.
- **DART Rate** (`qsr-dart-rate`): Days Away, Restricted, or Transferred rate — incidents per 200,000 hours that result in days away from work, restricted duty, or job transfer. A subset of TRIR that measures more severe incidents. [OSHA 29 CFR 1904 | Medium | Construction industry average: ~1.5]
  - DART rate is a better predictor of safety program effectiveness than TRIR because it excludes minor first-aid incidents. Owner prequalification increasingly uses DART rate alongside TRIR.
- **Hazard Recurrence Rate** (`qsr-hazard-recurrenc`): Percentage of identified hazards that recur within the same project — measures safety program effectiveness at eliminating root causes. Formula: Recurring Hazards / Total Unique Hazards × 100. [ISO 45001 continual improvement metrics | Medium | Typical: 29–45% recurrence rate by hazard type across 1,296 cos]
  - Recurrence detection uses 14-day gap tolerance between consecutive observations. Fall Protection has highest volume; Infrastructure projects average 14.4 weeks of recurring hazards.
- **Rework Cost Percentage** (`qsr-rework-cost`): Rework-attributable cost as a percentage of total project cost — the financial impact of quality failures. Formula: Rework Cost / Total Project Cost × 100. [CII (Construction Industry Institute) rework benchmarks | Medium | Industry benchmark: 5–15% of project cost]
  - From insight #1 (Rework Cost). CE→CCO deduplication is CRITICAL — use GREATEST(CE, CCO), never sum. Four independent cost surfaces. 40,441 projects across all surfaces.
- **Observation Resolution Time** (`qsr-observation-reso`): Average elapsed time from observation creation to closure — measures how quickly quality and safety findings are addressed. Formula: Closed Date − Created Date (in business days). Can be segmented by category (Quality vs. [Company-specific SLA targets | High | Typical: 3–14 days for routine findings]
  - Resolution time by vendor reveals subcontractor responsiveness to quality/safety findings. Safety observations should resolve faster than quality observations due to hazard urgency.
- **Inspection Pass Rate** (`qsr-insp-pass-rate`): Percentage of inspections that pass on first attempt — measures work quality at the point of formal examination. Formula: Passed Inspections / Total Inspections × 100 (or at item level: Conforming Items / Total Items). [ISO 9001 first-pass yield | High | Typical: 85–95% first-pass rate]
  - First-pass yield by inspection type reveals which quality gates catch the most deficiencies. Pre-cover and pre-pour inspections with low pass rates signal workmanship issues in hidden work.
- **Near-Miss Ratio** (`qsr-near-miss-ratio`): Ratio of near-miss reports to actual incidents — measures safety culture and proactive reporting. Formula: Near-Miss Count / Incident Count. Higher ratio = better safety culture (more proactive identification). [Heinrich's Safety Triangle | Medium | Industry target: 10:1 near-miss-to-incident]
  - Near-miss reporting is voluntary — low ratios often indicate cultural barriers to reporting rather than safety. Companies that actively encourage near-miss reporting have better safety outcomes.
- **Corrective Action Closure Rate** (`qsr-corrective-actio-2`): Percentage of corrective actions completed by their due date — measures the effectiveness of the remediation loop. Formula: On-Time Closures / Total Corrective Actions × 100. Tracks whether identified problems actually get fixed. [ISO 45001 §10.2 | High | Target: > 90% on-time closure]
  - Closure rate by action type (immediate vs. root cause vs. preventive) reveals whether companies are doing quick fixes or addressing root causes.

### Resources

**General Labor**
- **General Laborer** (`res-laborer`): General construction labor across all project phases — site prep through closeout. Lifecycle: mobilize → work → demobilize. [OSHA 29 CFR 1926 | Medium | Site Laborer, Interior Laborer, Demolition Worker, Flagging, Material Handler]
  - Category-level entry. Sub-specialties rarely distinguished in data — usually reported as one headcount. Demolition workers may require separate licensing (hazmat, asbestos).
- **Carpenter** (`res-carpenter`): Rough and finish carpentry — one of the most versatile trades on any project. Rough carpenters build formwork, shoring, blocking, backing, and temporary structures during foundations and structural phases. [CSI MasterFormat 06 00 00 | Medium | Rough Carpenter, Finish Carpenter, Millworker, Form Carpenter]
  - One of the most common trades on daily logs. Rough and finish are often different subs but may share a cost code.
- **Concrete Worker** (`res-concrete`): All concrete forming, placing, and finishing — from foundations through elevated slabs. Sub-specialties: concrete finishers (screeding, finishing, curing flatwork), formwork carpenters (construction and stripping), and post-tension specialists (stran... [CSI MasterFormat 03 00 00 | Medium | Concrete Finisher, Formwork Carpenter, Post-Tension Specialist]
  - Overlaps with carpentry (formwork). Post-tension is a distinct specialty sub — present only on PT structures.

**Structural Trades**
- **Ironworker / Steel Erector**: Steel erection and reinforcing — structural steel columns, beams, and deck plus reinforcing bar placement. [CSI MasterFormat 05 00 00 | Medium | Structural Steel Erector, Welder, Rebar Installer, Rigger / Signal Person]
  - Riggers/signal persons required for all crane operations. Welder may be under ironworker crew or a separate specialty. Rebar sometimes called 'rodbusting' — may be a separate sub.
- **Mason** (`res-mason`): All unit masonry — brick, block, and stone. Sub-specialties: bricklayers (face brick, thin brick veneer), block layers (CMU walls, backup walls, elevator shafts), and stone masons (natural and manufactured stone for exterior veneer and interior lobbi... [CSI MasterFormat 04 00 00 | Medium | Bricklayer, Block Layer, Stone Mason]
  - Masonry is seasonal in cold climates — hot weather mortar and cold weather protection add cost. Stone is often a separate specialty sub from brick/block.

**Building Envelope**
- **Roofer** (`res-roofer`): All roofing work — membrane, metal, and built-up systems. Sub-specialties: membrane roofers (TPO, PVC, EPDM, BUR, modified bitumen) and metal roofers/sheet metal workers (standing seam, metal panels, copings, flashing). [CSI MasterFormat 07 50 00 – 07 60 00 | Medium | Membrane Roofer, Metal Roofer / Sheet Metal, Built-Up Roofer]
  - Metal roofer overlaps with sheet metal worker. Weather sensitivity means daily log delay records are especially useful for roofing benchmarks.
- **Glazier / Curtain Wall Installer**: All glass and curtain wall work — unitized and stick-built curtain wall systems, punch windows, storefronts, entrances, and skylights. Highly specialized — usually one sub for the full building envelope scope. [CSI MasterFormat 08 40 00 – 08 80 00 | Medium | Curtain Wall Installer, Window / Storefront Installer, Skylight Installer]
  - Often the same crew for the full envelope. Submittal turnaround is a leading indicator of schedule risk for glazing.
- **Waterproofer** (`res-waterproofer`): Below-grade and above-grade moisture protection — foundation membranes, air/vapor barriers, and joint sealants. [CSI MasterFormat 07 10 00 – 07 92 00 | Medium | Below-Grade Waterproofer, Air Barrier Installer, Caulker / Sealant Applicator]
  - Waterproofing failures are among the top rework drivers — observation data is a strong signal. Air barrier is increasingly a code requirement (IECC).

**Interior Finishes**
- **Drywall Hanger / Finisher**: Metal framing and gypsum board — one of the largest interior workforces. Sub-specialties: metal framers (light-gauge steel framing, furring, soffits), drywall hangers (board hanging, specialty boards for moisture/abuse/fire), tapers/finishers (joint ... [CSI MasterFormat 09 20 00 – 09 29 00 | Medium | Metal Framer, Drywall Hanger, Taper / Finisher, Plasterer]
  - Plasterer is specialty — not on every project. Metal framing and hanging are often the same sub but different crews. EIFS crosses into exterior work.
- **Painter** (`res-painter`): All painting and coating work — interior and exterior. Sub-specialties: interior painters (walls, ceilings, trim, doors), exterior painters (elastomeric, high-performance coatings), and specialty coatings applicators (epoxy floors, intumescent firepr... [CSI MasterFormat 09 90 00 – 09 97 00 | Medium | Interior Painter, Exterior Painter, Specialty Coatings Applicator]
  - Paint/finish is consistently among the top punch item categories across all project types. Exterior painting is weather-sensitive.
- **Floor Installer** (`res-floor`): All flooring installation — tile, carpet, resilient, hardwood, and specialty. Sub-specialties: tile setters (ceramic, porcelain, natural stone), carpet/resilient installers (carpet, LVT, VCT, sheet vinyl, rubber), and hardwood/specialty floor install... [CSI MasterFormat 09 30 00 – 09 68 00 | Medium | Tile Setter, Carpet / Resilient Installer, Hardwood / Specialty Floor Installer]
  - Moisture testing delays are common — concrete moisture content must meet ASTM F2170 before resilient flooring installation. Different sub for each flooring type on many projects.
- **Ceiling Installer** (`res-ceiling`): Ceiling systems — acoustic grid-and-tile and specialty ceilings. Sub-specialties: acoustic ceiling installers (grid, lay-in tile, tegular) and specialty ceiling installers (wood, metal, stretch, linear, cloud ceilings). [CSI MasterFormat 09 50 00 – 09 54 00 | Medium | Acoustic Ceiling Installer, Specialty Ceiling Installer]
  - Ceiling grid installation cannot begin until above-ceiling MEP is inspected and approved. Coordination delays are common.
- **Insulation Installer** (`res-insulator`): Thermal and acoustic insulation — building envelope and mechanical systems. Sub-specialties: building insulation (batt, rigid, spray foam, blown-in for walls and roof) and mechanical insulation (pipe and duct insulation, jacketing). [CSI MasterFormat 07 21 00 | Low | Building Insulation Installer, Mechanical Insulation Installer]
  - Building insulation increasingly drives energy code compliance. Mechanical insulation is a separate sub on larger projects.
- **Fireproofer** (`res-fireproofer`): Fire protection of structural elements and through-penetrations. Sub-specialties: spray fireproofers (SFRM on structural steel — follows steel erection, critical path) and firestoppers (through-penetration and perimeter fire barrier — inspection-crit... [CSI MasterFormat 07 81 00 – 07 84 00 | Medium | Spray Fireproofer (SFRM), Firestopper]
  - Spray fireproofing follows steel erection — critical path item. Firestopping deficiencies are among the most common inspection findings.

**MEP Trades**
- **Plumber / Pipefitter**: All plumbing and piping — domestic water, waste, vent, gas, and specialty process piping. Sub-specialties: plumbers (domestic water and DWV), steamfitters/HVAC pipefitters (chilled water, hot water, steam, refrigerant), medical gas installers (health... [CSI MasterFormat 22 00 00 | Medium | Plumber, Steamfitter / HVAC Pipefitter, Medical Gas Installer, Process Pipefitter]
  - Steamfitter may be under HVAC sub's scope — union distinction. Medical gas requires separate certification and testing.
- **HVAC / Sheet Metal Worker**: All HVAC ductwork and equipment — fabrication, installation, and commissioning. Sub-specialties: sheet metal workers (duct fabrication and installation), HVAC equipment installers (AHUs, RTUs, chillers, boilers, VRF), test and balance technicians (ai... [CSI MasterFormat 23 00 00 | Medium | Sheet Metal Worker, HVAC Equipment Installer, TAB Technician, Controls Technician]
  - Controls technician may be under HVAC sub or a separate controls sub. TAB and commissioning are late-project activities required for closeout.
- **Electrician** (`res-electrician`): All electrical work — power distribution, lighting, fire alarm, and site electrical. Sub-specialties: power electricians (service entrance, distribution, branch circuits, devices), lighting electricians (fixture installation, controls, emergency), fi... [CSI MasterFormat 26 00 00 | Medium | Power Electrician, Lighting Electrician, Fire Alarm Electrician, Site Electrician]
  - Fire alarm work may be under electrical sub or a separate FA specialty sub — varies by market. Electrical is typically on site the longest of any MEP trade.
- **Sprinkler Fitter** (`res-sprinkler`): All fire suppression piping — wet, dry, pre-action, deluge, and specialty systems. Sub-specialties: wet system installers (mains, branches, heads for standard wet pipe) and specialty system installers (dry, pre-action, deluge, clean agent, kitchen ho... [CSI MasterFormat 21 00 00 | Medium | Wet System Installer, Specialty System Installer]
  - Separate union and licensing from plumbing. Typically one sprinkler sub per project. NFPA 13 compliance is inspection-critical.
- **Elevator Mechanic** (`res-elevator`): All elevator and vertical transportation work — traction, hydraulic, MRL, escalators, and moving walks. Typically proprietary — one manufacturer's installer per project. Long lead time for equipment. [CSI MasterFormat 14 00 00 | Medium | Traction Elevator, Hydraulic Elevator, MRL Elevator, Escalator]
  - Proprietary trade — usually one sub per project. Temporary construction hoist is a distinct scope (see Equipment). Elevator inspection is jurisdictional.
- **Low Voltage Technician**: All low voltage and technology systems — data/telecom, security, AV, and fire alarm. Sub-specialties: data/telecom installers (structured cabling, fiber, racks), security installers (cameras, access control, intrusion), AV installers (audio, video, c... [CSI MasterFormat 27 00 00 – 28 00 00 | Medium | Data / Telecom Installer, Security Installer, AV Installer, Fire Alarm Installer]
  - Fire alarm installer overlaps with electrician — licensing varies by jurisdiction. AV is increasingly complex and a separate specialty sub.

**Site & Support**
- **Equipment Operator** (`res-operator`): Operation of construction equipment — earthmoving, cranes, and material handling. Sub-specialties: heavy equipment operators (excavators, dozers, loaders, graders, scrapers), crane operators (tower and mobile cranes — separately licensed), and forkli... [OSHA 1926 Subpart N/O/CC | Medium | Heavy Equipment Operator, Crane Operator, Forklift / Telehandler Operator]
  - Crane operators have separate licensing (NCCCO). Forklift/telehandler certification (OSHA) required for all operators.
- **Surveyor / Layout Technician**: Survey and layout — establishing control points, building layout, grade verification, and as-built documentation. Uses total stations, GPS/GNSS, robotic instruments, and increasingly drones for progress documentation. [CSI MasterFormat 01 71 23 | Low | Land Surveyor, Layout Technician, Drone/UAV Operator]
  - Drone/UAV surveys are increasingly common for progress photos, volumetric surveys, and thermal scans. Survey data lives outside PM systems.
- **Safety Professional** (`res-safety`): Safety management and compliance — hazard identification, incident investigation, OSHA compliance, and safety training. Typically a full-time role on projects above a threshold size. [OSHA 29 CFR 1926 | High | Site Safety Manager, Safety Engineer, Safety Officer]
  - Project role memberships identify safety professionals. Observation category = Safety is the primary data signal. Not all projects have a dedicated safety role.
- **Quality Control Inspector**: Quality assurance and testing — inspection of installed work, material testing coordination, and punch list management. May be a dedicated role or part of the superintendent's responsibilities. [ASTM testing standards | High | QC Manager, QC Inspector, Third-Party Testing Coordinator]
  - Quality observations and inspection items are the strongest signals. Third-party test results typically live outside PM systems.
- **Commissioning Agent** (`res-cxa`): Building systems commissioning — functional performance testing of MEP systems before owner occupancy. Increasingly required by code (IECC, ASHRAE 189.1) and LEED. Independent from installing contractors. [ASHRAE Guideline 0 | Low | Commissioning Authority (CxA), Retro-Commissioning Agent]
  - Distinct from TAB technician (HVAC-specific). Cx covers all MEP systems and building envelope. Growing requirement — increasingly a code mandate.

**Cranes**
- **Crane** (`res-crane`): Lifting equipment for vertical construction — tower cranes, mobile cranes, and overhead gantry systems. Tower cranes: hammerhead (fixed jib, high-rise), luffing (variable radius, tight urban sites), and self-erecting (low/mid-rise). [OSHA 1926 Subpart CC | Medium | Tower Crane — Hammerhead, Tower Crane — Luffing, Tower Crane — Self-Erecting, Mobile Crane — Truck, ]
  - Crane erection/dismantling noted in daily logs. Tower crane selection drives structural pour sequence. Multiple cranes on large sites require coordination.

**Earthmoving**
- **Earthmoving Equipment**: Excavation, grading, and site preparation equipment. Types: track excavators (primary dig — bulk and detail), mini excavators (confined spaces, utilities), long-reach excavators (deep cuts), wheel loaders (material handling, stockpile), skid steers (... [OSHA 1926 Subpart O | Medium | Track Excavator, Mini Excavator, Long Reach, Wheel Loader, Skid Steer, Backhoe, Dozer, Grader, Trenc]
  - GPS machine guidance reduces survey staking. Skid steers are the most versatile — used from earthwork through interior cleanup.

**Concrete Equipment**
- **Concrete Equipment**: Concrete placement and finishing equipment — pumps, mixers, vibrators, and saws. Boom pumps (truck-mounted, for elevated pours), line pumps (ground-level, for slabs and foundations), mixer trucks (ready-mix delivery), concrete vibrators (internal con... [ACI 304R | Medium | Boom Pump, Line Pump, Mixer Truck, Concrete Vibrator, Concrete Saw]
  - Boom pump vs line pump selection depends on reach and access. Concrete saw is also used for demo and modification work. Mixer truck count per pour is a productivity signal.

**Material Handling**
- **Material Handling Equipment**: Equipment for moving materials on site — forklifts, telehandlers, conveyors, and hoists. Rough terrain forklifts (outdoor material handling), warehouse forklifts (indoor staging), telehandlers (variable-reach telescopic handler — most common material... [OSHA 1926 Subpart N | Medium | Forklift — Rough Terrain, Forklift — Warehouse, Telehandler, Conveyor / Hoist]
  - Telehandler is the workhorse — present on virtually every project. Forklift certification (OSHA) required for all operators. Equipment rental vs ownership is a key cost decision.

**Access Equipment**
- **Access Equipment** (`res-access`): Equipment for elevated work access — boom lifts, scissor lifts, personnel hoists, and scaffolding. Boom lifts: articulating (around obstacles) and telescopic (maximum reach). [OSHA 1926 Subpart L (Scaffolds) | Medium | Boom Lift — Articulating, Boom Lift — Telescopic, Scissor Lift, Personnel Hoist, Scaffolding — Tubul]
  - Hoist availability directly affects productivity on high-rise — hoists are schedule-critical. Mast climbing platforms are replacing traditional scaffold on many projects.

**Compaction**
- **Compaction Equipment**: Soil and base compaction equipment — rollers, plate compactors, and rammers. Vibratory rollers (smooth drum or padfoot for large areas), plate compactors (walk-behind for trench backfill and confined areas), and pneumatic rollers (multi-tire for asph... [ASTM D698 | Low | Vibratory Roller, Plate Compactor, Pneumatic Roller, Rammer / Jumping Jack]
  - Third-party geotechnical testing results (density tests) are the real quality signal but live outside PM systems. Compaction failures cause schedule delays.

**Foundation Equipment**
- **Piling / Foundation Equipment**: Deep foundation equipment — pile drivers, drill rigs, and caisson drills. Impact and vibratory pile drivers (driven piles — steel H, precast concrete), drill rigs/auger equipment (drilled shafts, auger-cast piles), and caisson drills (large-diameter ... [ASTM D1143 | Low | Pile Driver — Impact, Pile Driver — Vibratory, Drill Rig / Auger, Caisson Drill]
  - Not present on every project — depends on soil conditions and structural loads. Pile driving logs and load test results are specialty data.

**Hauling**
- **Hauling Equipment**: Transport equipment — dump trucks, flatbeds, and water trucks. Dump trucks (on/off-site material hauling for earthwork and demo), flatbed trucks (material delivery and transport), and water trucks (dust control, compaction moisture). [DOT weight limits | Low | Dump Truck, Flatbed Truck, Water Truck, Articulated Hauler]
  - Water trucks are critical for dust control (EPA/local regulations) and compaction moisture. Articulated haulers for soft ground conditions. Haul distance is the primary cost variable.

**Temporary Utilities**
- **Temporary Utilities** (`res-temp-util`): Temporary site services during construction — power, compressed air, heating, lighting, and dewatering. [OSHA 1926 Subpart K | Medium | Generator, Air Compressor, Heater / Temp Heat, Light Tower, Dewatering Pump]
  - Dewatering is critical on waterfront and high-water-table projects — can be a major unplanned cost. Temp heat is a significant winter cost in cold climates. Duration drives cost.

**Welding & Fabrication**
- **Welding / Fabrication Equipment**: On-site welding and cutting equipment — arc welders and cutting tools. Arc welders (SMAW, GMAW, FCAW machines for structural and miscellaneous welding) and cutting equipment (oxy-fuel, plasma, saw cutting for steel modification and demolition). [AWS D1.1 | Low | Arc Welder (SMAW, GMAW, FCAW), Oxy-Fuel Torch, Plasma Cutter, Saw]
  - Welding procedure specifications (WPS) and welder qualification records (WPQ) are required documentation but rarely tracked in PM systems. NDT inspection results are external.

**Survey & Layout**
- **Survey / Layout Instruments**: Surveying and layout instruments — total stations, GPS/GNSS, lasers, and drones. Total stations (electronic survey instrument for precise layout), GPS/GNSS equipment (satellite positioning for grading and layout — enables machine guidance), laser lev... [ASCE Manual of Practice 98 | Low | Total Station, GPS / GNSS Receiver, Robotic Total Station, Laser Level, Drone / UAV]
  - Drones increasingly common — progress photos, LiDAR, volumetric surveys, thermal scans. GPS machine guidance integration reduces survey staking. Survey data typically lives in specialty platforms.

**Concrete**
- **Concrete** (`mat-concrete`): All cast-in-place and precast concrete — the most common structural material in construction. Types: ready-mix concrete (normal weight, lightweight, high-strength, SCC, fiber-reinforced), precast structural (hollow core plank, double tees, beams, col... [CSI MasterFormat 03 00 00 | Medium | Ready-Mix, Lightweight, High-Strength, SCC, Fiber-Reinforced, Precast Structural, Precast Architectu]
  - Mix design submittals are universal. Pour records in daily logs are a strong production signal. Precast requires shop drawing submittals.

**Reinforcing**
- **Rebar & Reinforcing**: All concrete reinforcement — deformed bars, welded wire, post-tensioning, and mechanical couplers. Rebar (#3 through #18 deformed bars, epoxy coated), welded wire fabric (WWF/WWR for slabs), post-tensioning (PT strand, anchors, ducts, grout — special... [CSI MasterFormat 03 20 00 | Medium | Rebar #3–#18, Epoxy-Coated, WWF/WWR, PT Strand, Mechanical Couplers]
  - Rebar shop drawings are standard submittals on every concrete project. Post-tensioning is a separate specialty sub with its own submittals. Seismic zones drive rebar density.

**Structural Metals**
- **Structural Steel & Metals**: All structural and miscellaneous steel and metal fabrications. Structural steel (wide flange, HSS, angles, channels, plates), steel deck (composite, non-composite, and roof deck), connection hardware (bolts, welds, base plates, shear studs), miscella... [CSI MasterFormat 05 00 00 | Medium | Wide Flange, HSS, Angles, Composite Deck, Roof Deck, Misc Metals, Stairs, Railings, Bollards, Orname]
  - Steel connection details generate heavy RFI activity — a leading indicator of structural complexity. Misc metals coordinate with nearly every other trade.

**Wood & Composites**
- **Lumber & Wood** (`mat-lumber`): All wood and composite products — dimensional lumber, engineered wood, and sheathing. Dimensional lumber (studs, joists, blocking, plates), engineered wood (LVL, glulam, TJI, CLT, PSL), and sheathing/panels (plywood, OSB, cementitious board). [CSI MasterFormat 06 00 00 – 06 17 00 | Medium | Dimensional Lumber, LVL, Glulam, CLT, PSL, TJI, Plywood, OSB, Cementitious Board]
  - CLT and mass timber are a growing structural system with distinct submittal and fire protection requirements. Conventional framing has less formal submittals.

**Masonry**
- **Masonry** (`mat-masonry`): All unit masonry — CMU, face brick, natural stone, manufactured stone, and accessories. CMU (standard, lightweight, split face, ground face), face brick (modular, queen, king, thin brick), natural stone (limestone, granite, marble, sandstone, slate),... [CSI MasterFormat 04 00 00 | Medium | CMU, Face Brick, Thin Brick, Limestone, Granite, Cast Stone, Cultured Stone, Mortar, Ties, Lintels]
  - Color and pattern submittals are critical for approval. Masonry is seasonal in cold climates. Natural stone is often a separate specialty sub from brick/block.

**Roofing**
- **Roofing** (`ph-roofing`): All roofing materials — membrane, metal, built-up, and accessories. Single-ply membrane (TPO, PVC, EPDM), built-up/modified bitumen (BUR, SBS, APP), metal roofing (standing seam, corrugated, architectural panels), insulation (polyiso, EPS, XPS, cover... [CSI MasterFormat 07 50 00 – 07 70 00 | Medium | TPO, PVC, EPDM, BUR, Modified Bitumen, Standing Seam, Polyiso, EPS, XPS]
  - Manufacturer warranty requirements dictate material specs and installer certification. Weather-sensitive installation — daily log delays frequently reference roofing holds.

**Waterproofing & Sealants**
- **Waterproofing & Sealants**: All moisture protection — below-grade waterproofing, air/vapor barriers, sealants, flashing, and expansion joints. [CSI MasterFormat 07 10 00 – 07 95 00 | Medium | Sheet Membrane, Fluid-Applied, Bentonite, Air Barrier, Silicone Sealant, Urethane, Flashing, Expansi]
  - Waterproofing failures are consistently among the top rework drivers. Air barrier is increasingly a code requirement (IECC). Observation data is a strong signal for envelope failures.

**Thermal & Fire Protection**
- **Thermal & Fire Protection**: Insulation and fireproofing materials — building insulation, spray fireproofing, and firestopping. Building insulation (batt, rigid board, spray foam, blown-in — energy code driven), spray fireproofing (SFRM — cementitious and intumescent on structur... [CSI MasterFormat 07 20 00 – 07 84 00 | Medium | Batt Insulation, Rigid Board, Spray Foam, SFRM (Cementitious), SFRM (Intumescent), Firestopping]
  - Firestopping deficiencies are among the most common inspection findings across all project types. Spray fireproofing thickness is a frequent inspection checkpoint.

**Doors Frames & Hardware**
- **Doors Frames & Hardware**: All door assemblies — hollow metal, wood, specialty doors, finish hardware, and overhead doors. Hollow metal doors and frames (steel), wood doors (flush, stile and rail, fire-rated), specialty doors (FRP, aluminum, sliding, folding, acoustic), finish... [CSI MasterFormat 08 10 00 – 08 71 00 | Medium | Hollow Metal Door, Wood Door, Specialty Door, Hinges, Locksets, Closers, Exit Devices, Overhead Door]
  - Hardware schedule is one of the most detailed and time-consuming submittals. ADA compliance drives hardware selection. Fire-rated assemblies require labeled components.

**Glass & Glazing**
- **Glass & Glazing** (`mat-glass`): All glass and glazing systems — curtain wall, windows, storefronts, skylights, and insulating glass units. [CSI MasterFormat 08 40 00 – 08 81 00 | Medium | Unitized Curtain Wall, Stick-Built CW, Aluminum Window, Storefront, Skylight, IGU (Low-E, Tempered, ]
  - Curtain wall is typically long lead — fabrication submittals are early and critical. Performance specs (thermal, structural, water) drive glazing selection.

**Interior Framing & Board**
- **Interior Framing & Gypsum**: Metal framing and gypsum board — the backbone of interior partitions. Metal studs and track (light-gauge steel framing, deflection track, furring), gypsum board (regular, moisture-resistant, fire-rated, abuse-resistant, shaftliner), and plaster/stucc... [CSI MasterFormat 09 20 00 – 09 29 00 | Medium | Metal Studs, Deflection Track, Regular Gypsum, Moisture-Resistant, Fire-Rated, Abuse-Resistant, Shaf]
  - Specialty board requirements drive cost — abuse-resistant and fire-rated boards cost significantly more than standard. EIFS crosses into exterior work.

**Ceilings**
- **Ceiling Materials** (`mat-ceiling`): All ceiling systems — acoustic grid-and-tile and specialty ceilings. Acoustic ceilings (suspension grid, lay-in tile, tegular) and specialty ceilings (wood, metal, stretch, linear, open cell, cloud ceilings). [CSI MasterFormat 09 50 00 – 09 54 00 | Medium | Grid, Lay-In Tile, Tegular, Wood Ceiling, Metal Ceiling, Stretch Ceiling, Linear, Cloud]
  - Ceiling grid installation is a coordination milestone — triggers MEP above-ceiling inspection. Specialty ceilings are significantly more expensive than standard acoustic tile.

**Flooring**
- **Flooring** (`ph-flooring`): All flooring materials — tile, carpet, resilient, hardwood, stone, and resinous/specialty. Ceramic/porcelain tile (floor and wall tile, mosaics), carpet (broadloom, modular tile), resilient flooring (LVT, VCT, sheet vinyl, rubber, linoleum), hardwood... [CSI MasterFormat 09 30 00 – 09 68 00 | Medium | Ceramic Tile, Porcelain, Carpet Tile, LVT, VCT, Rubber, Hardwood, Terrazzo, Epoxy, Polished Concrete]
  - Substrate moisture testing is a common delay driver — concrete moisture content must meet ASTM F2170. Multiple flooring subs per project is typical. Punch items frequently reference flooring.

**Paint & Coatings**
- **Paint & Coatings** (`be-paint`): All painting and coating products — interior paint, exterior coatings, specialty coatings, primers, and wall coverings. [CSI MasterFormat 09 72 00 – 09 97 00 | Medium | Latex, Acrylic, Elastomeric, Epoxy, Urethane, Anti-Graffiti, Vinyl Wall Covering, FRP]
  - Paint/finish is consistently the #1 punch item category across all project types. Color selection submittals are time-consuming. VOC compliance drives product selection.

**Specialties**
- **Specialties** (`mat-specialties`): Division 10 specialties — toilet accessories, signage, fire protection specialties, wall/corner protection, and lockers/storage. [CSI MasterFormat 10 00 00 | Medium | Toilet Partitions, Grab Bars, Dispensers, Mirrors, ADA Signs, Wayfinding, Extinguisher Cabinets, Cor]
  - Often supplied by GC directly or by multiple specialty suppliers. ADA compliance drives signage and accessory selection. Fire protection specialties are code-required.

**Casework & Millwork**
- **Casework & Millwork** (`ph-casework`): Cabinets, countertops, trim, and custom millwork. Plastic laminate casework (standard commercial cabinets), wood casework (stain-grade cabinets), countertops (solid surface, quartz, granite, laminate, stainless), and trim/millwork (base, crown, casin... [CSI MasterFormat 06 22 00 – 06 60 00 | Medium | Plastic Laminate, Wood Casework, Quartz Counter, Granite Counter, Solid Surface, Stainless, Base/Cro]
  - AWI quality grades (Economy, Custom, Premium) drive cost and specification detail. Long fabrication lead time — shop drawings are early critical path. Highly visible to end users — punch item driver.

**Plumbing**
- **Plumbing Materials** (`mat-plumbing`): All plumbing piping, fittings, and fixtures. Pipe: domestic water (copper, PEX, CPVC, stainless), waste/vent (cast iron, PVC, ABS, no-hub), valves and fittings (gate, ball, check, PRV, backflow preventers), and hangers/supports. [CSI MasterFormat 22 00 00 | Medium | Copper, PEX, CPVC, Cast Iron, PVC, Flush Valve, Tank Type, Wall-Hung, Undermount, Tankless Water Hea]
  - Plumbing fixture submittals are high-volume — every fixture by model number. Fixture count is a primary plumbing cost driver. Backflow preventer submittals are code-critical.

**HVAC Distribution**
- **HVAC Distribution** (`ph-hvac-dist`): All HVAC ductwork, piping, and insulation. Ductwork: sheet metal duct (rectangular, round, oval), flexible duct, duct fittings and accessories (elbows, tees, dampers, turning vanes, access doors), and diffusers/grilles/registers (supply, return, exha... [CSI MasterFormat 23 07 00 – 23 37 00 | Medium | Rectangular Duct, Round Duct, Flex Duct, Dampers, Diffusers, CHW Pipe, Refrigerant Pipe, Pipe Insula]
  - Duct fabrication is increasingly off-site (shop fab vs field fab). Above-ceiling coordination with other MEP trades is a major scheduling challenge. Terminal device submittals are high-volume.

**HVAC Equipment**
- **HVAC Equipment & Controls**: Major HVAC equipment and building automation controls. Equipment: air handling units (central station AHUs, make-up air), rooftop units (packaged RTUs, DX cooling), split systems/VRF/heat pumps, chillers (air-cooled, water-cooled), cooling towers, bo... [CSI MasterFormat 23 09 00 – 23 81 00 | Medium | AHU, RTU, VRF, Chiller, Cooling Tower, Boiler, VAV Box, Fan Coil, BAS Panel, DDC Controller]
  - Major HVAC equipment is long lead — submittal approval drives procurement schedule. Controls/BAS commissioning is a late-project critical path.

**Electrical Power**
- **Electrical Distribution & Wiring**: Power distribution equipment and wiring systems. Distribution: switchgear, transformers (dry-type, pad-mount), panelboards and breakers, disconnects and switches, motor starters/VFDs, and generators/UPS (permanent standby power). [CSI MasterFormat 26 05 00 – 26 32 00 | Medium | Switchgear, Transformer, Panel, VFD, Generator, UPS, THHN Wire, MC Cable, EMT, Rigid Conduit, Cable ]
  - Switchgear and transformer are long-lead items — submittal approval is early critical path. Generator sizing drives significant cost on mission-critical facilities (hospitals, data centers).

**Lighting**
- **Lighting** (`be-lighting`): All light fixtures and controls — interior, exterior, emergency, and controls. Interior fixtures (troffers, downlights, pendants, linear, decorative), exterior fixtures (site, facade, parking, landscape lighting), emergency and exit (emergency batter... [CSI MasterFormat 26 50 00 – 26 56 00 | Medium | Troffer, Downlight, Pendant, Linear, Decorative, Site Light, Emergency Battery, Exit Sign, Occupancy]
  - Lighting submittals are consistently the highest-volume submittal category. Energy code (IECC, ASHRAE 90.1) drives control requirements.

**Fire Protection**
- **Fire Protection Systems**: All fire suppression and fire alarm materials — sprinkler pipe, heads, pumps, detection devices, notification devices, and control panels. [CSI MasterFormat 21 00 00 / 28 31 00 | Medium | Wet Pipe, Dry Pipe, Pre-Action, Clean Agent, CPVC Pipe, Concealed Head, FACP, Smoke Detector, Strobe]
  - Fire suppression and fire alarm are increasingly separate subcontractors (separate unions and licensing). NFPA 13 compliance is inspection-critical.

**Low Voltage**
- **Low Voltage Systems**: Data/telecom, security, AV, and paging systems. Communications: structured cabling (Cat6, Cat6A, fiber optic), data outlets and patch panels, data racks and enclosures, AV equipment (displays, projectors, speakers, conferencing, control), and paging/... [CSI MasterFormat 27 00 00 – 28 00 00 | Medium | Cat6, Cat6A, Fiber Optic, Patch Panel, IP Camera, NVR, Card Reader, Maglocks, AV Display, Projector,]
  - Communications and security are often separate specialty subs. AV complexity has increased significantly — conference room technology is a major scope item.

**Site Materials**
- **Site & Utility Materials**: Sitework and infrastructure materials — soil/fill, utility pipe, manholes, geotextiles, paving, fencing, and landscaping. [CSI MasterFormat 31 00 00 – 33 00 00 | Medium | Structural Fill, Gravel, DI Pipe, PVC Pipe, HDPE, Precast Manhole, Silt Fence, Asphalt, Concrete Pav]
  - Soil/fill material is not typically in PM material tables — tracked via delivery logs and procurement. Paving and landscaping are late-project scopes.

**Vertical Transportation**
- **Elevator & Conveying**: All vertical transportation — traction elevators, hydraulic elevators, MRL (machine-room-less) elevators, escalators, moving walks, and cab finishes. [CSI MasterFormat 14 00 00 | Medium | Traction Elevator, Hydraulic Elevator, MRL Elevator, Escalator, Moving Walk, Cab Finishes]
  - Proprietary trade — limited submittal detail due to manufacturer IP. Elevator inspection is jurisdictional. MRL systems are gaining market share over traditional traction in mid-rise buildings.

**Standard Measures**
- **Labor Productivity Rate**: Output per labor hour for a given trade — the fundamental measure of workforce efficiency. Calculation: units installed ÷ total labor hours. Units vary by trade (CY for concrete, SF for drywall, tons for steel). [AACE RP 22R-01 | Medium | 0.5–2.0 SF/labor-hour (drywall), 0.3–1.0 CY/labor-hour (concrete), varies widely by trade]
  - Requires clean trade-to-output mapping — often not available in structured data. Weather, overtime, and learning curve all affect rates. Best measured at trade level, not aggregate.
- **Crew Size per Trade**: Average and peak headcount for a specific trade on a project. Calculation: sum of workers reported per trade per day from manpower logs. Tracking over time shows workforce loading curve — early ramp, peak, and demobilization. [OSHA recordkeeping | Medium | 5–15 (typical crew), 50–200+ (peak on large projects)]
  - Trade name normalization is essential — same trade may be logged under different names across companies. Headcount-based, not FTE-based.
- **Labor Cost per Unit**: Cost of labor per unit of output — combines productivity and wage rate. Calculation: total labor cost for trade ÷ total units installed. Requires cost code breakdown by trade and quantity tracking. [AACE Cost Engineering Terminology | Medium | $5–$15/SF (drywall), $50–$150/CY (concrete placement), varies by market]
  - Wage rates vary significantly by region and union status. Overtime premium distorts per-unit cost. Best used for relative comparison, not absolute targets.
- **Equipment Utilization Rate** (`fo-equip-utilizatio`): Percentage of available time that equipment is actively in use. Calculation: active operating hours ÷ total available hours on site. High utilization indicates right-sizing; low utilization suggests oversized fleet or scheduling gaps. [CII Equipment Management | Low | 60–85% (target utilization)]
  - Telematics provide the best utilization data but are rarely integrated into PM systems. Daily log equipment captures on-site presence, not active use.
- **Material Waste Rate**: Percentage of material ordered that is not installed — waste, damage, theft, or over-ordering. Calculation: (quantity ordered − quantity installed) ÷ quantity ordered × 100. Typical rates: 2–5% for steel, 5–10% for concrete, 10–15% for drywall. [WRAP (Waste & Resources Action Programme) | Low | 2–5% (steel), 5–10% (concrete), 10–15% (drywall/lumber), varies by material]
  - Waste tracking is increasingly important for LEED credits and ESG reporting. BIM-to-field quantity comparison is the emerging approach. Most companies track waste informally.
- **Submittal Turnaround Time**: Days from submittal submission to final approval — a leading indicator of schedule risk. Calculation: approval_date − submission_date for each submittal. [AIA A201 (standard review periods) | High | 7–14 days (typical target), 21–45 days (complex submittals)]
  - Long turnaround on critical-path submittals (steel shop drawings, curtain wall, major MEP equipment) is a leading schedule risk indicator. Re-submittals compound the delay.
- **Trade Count per Project**: Number of distinct trade categories active on a project — a proxy for project complexity. Calculation: count of unique trades from manpower logs. More trades = more coordination overhead. Typical: 15–25 trades on a mid-size commercial project. [CII Complexity Assessment | Medium | 8–12 (simple), 15–25 (typical commercial), 25–35 (complex healthcare/lab)]
  - Trade count is a useful complexity proxy but requires normalized trade names. More trades = more potential conflicts and coordination meetings.
- **Material Delivery On-Time Rate**: Percentage of material deliveries arriving on or before the scheduled date. Calculation: on-time deliveries ÷ total scheduled deliveries × 100. Late deliveries cause trade stacking and schedule compression. [CII Materials Management | Medium | 85–95% (target), varies by material and supply chain conditions]
  - Submittal overdue flags and required-on-site dates are the closest proxy for delivery schedule compliance. Actual delivery date tracking is sparse in most systems.
- **Labor Hours per $1M Project Value**: Total labor hours normalized by project value — an efficiency metric that enables cross-project comparison regardless of size. Calculation: total manpower hours ÷ (project total value ÷ $1M). [CII Benchmarking | Medium | 2000–5000 hours/$1M (new construction), 4000–8000 hours/$1M (renovation)]
  - Renovation projects are significantly more labor-intensive per dollar than new construction. Normalizing by value enables comparison across project sizes.

### Risk

**Risk Framework**
- **Risk** (`rk-risk`): An identified potential event or condition that could affect project objectives — the fundamental unit of risk management. Defined by source (what causes it), trigger (what signals it), consequence (what it affects), and owner (who manages it). [PMI PMBOK Risk Management | None | Design conflict, material shortage, permit delay, subcontractor default, weather event, unforeseen c]
  - Risk management in construction is overwhelmingly informal — spreadsheets, meeting discussions, and institutional knowledge.
- **Risk Register** (`rk-risk-register`): A project-level inventory of all identified risks — the master document that tracks risk identification, assessment, response, and status throughout the project lifecycle. Maintained from preconstruction through closeout. [PMI PMBOK 11.2 | None | 50–200 risks per major project]
  - Most GCs maintain risk registers in Excel. The opportunity is to auto-populate risk signals from Procore data into an external register — or build one natively.
- **Risk Category** (`rk-risk-category`): A classification that groups risks by their source or nature — the organizing principle for a risk register. Categories are typically defined at the company or program level and applied consistently across projects. [PMI PMBOK Risk Breakdown Structure (RBS) | None | Design, Construction, Financial, Schedule, Safety, Environmental, Regulatory, Market, Geotechnical, ]
  - Risk categories should map to the UCDM's cross-domain relationships: design risk → Documents & Communications (RFIs), financial risk → Financial Instruments (change orders), safety risk → Quality & Sa...
- **Risk Trigger** (`rk-risk-trigger`): An observable condition or event that signals a risk is materializing — the early warning system. Triggers convert abstract risks into actionable alerts. [PMI PMBOK 11.6 (Monitor Risks) | Low | RFI volume spike, submittal delay, weather forecast, change order rate increase, safety observation ]
  - Triggers are the bridge between reactive and proactive risk management. Procore's cross-domain data (RFIs + delays + observations + changes) is uniquely positioned to detect triggers that single-domai...
- **Risk Owner** (`rk-risk-owner`): The person or party responsible for monitoring a risk and executing the response plan — accountability for risk management. [PMI PMBOK 11.5 | None | Project Manager, Superintendent, Estimator, Architect, Owner's Rep, Subcontractor PM, Safety Manager]
  - Risk ownership often misaligns with contractual responsibility — the party best positioned to manage a risk is not always the party contractually responsible for it.

**Risk Assessment**
- **Likelihood Assessment** (`rk-likelihood-asses`): The evaluation of probability that a risk event will occur — qualitative (High/Medium/Low) or quantitative (percentage, frequency). [PMI PMBOK 11.3 | None | Very Low (<10%), Low (10-25%), Medium (25-50%), High (50-75%), Very High (>75%)]
  - Qualitative likelihood (H/M/L) is standard in construction. Quantitative likelihood is rare outside of large infrastructure projects where Monte Carlo simulation justifies the effort.
- **Impact Assessment** (`rk-impact-assessmen`): The evaluation of consequence severity if a risk materializes — measured across one or more dimensions: cost, schedule, quality, safety, reputation. [PMI PMBOK 11.3 | Low | Cost impact ($K–$M range)]
  - Impact assessment is most accurate when grounded in historical data from similar projects — exactly where Procore's cross-company benchmarking creates value.
- **Risk Score** (`rk-risk-score`): The combined measure of likelihood × impact that determines risk priority — the basis for triage and resource allocation. Typically displayed as a number (1–25 on a 5×5 matrix) or color (red/amber/green). [PMI PMBOK 11.3 | None | 1–5 (low) to 20–25 (critical) on 5×5 matrix]
  - Risk scores are only as good as the underlying likelihood and impact estimates. Procore data enables evidence-based scoring rather than gut-feel estimates.
- **Risk Matrix** (`rk-risk-matrix`): A visual grid that plots risks by likelihood (y-axis) and impact (x-axis) — the standard tool for risk prioritization. Typically 3×3 or 5×5 with color-coded zones (green = accept, amber = mitigate, red = escalate). [PMI PMBOK 11.3 | None | 3×3, 4×4, or 5×5 grid]
  - The risk matrix is the most widely recognized risk management artifact in construction — even teams without formal risk processes understand the red/amber/green framework.

**Risk Response**
- **Risk Response Type** (`rk-risk-response`): The strategic approach to managing an identified risk — the four fundamental options. Each risk in the register should have an assigned response type that determines the nature of the mitigation plan. [PMI PMBOK 11.5 | None | Avoid (eliminate the risk by changing plans), Mitigate (reduce likelihood or impact), Transfer (shif]
  - In construction, Transfer is the dominant strategy — subcontracting is fundamentally risk transfer. The GC transfers execution risk to subs while retaining coordination risk.
- **Mitigation Action** (`rk-mitigation-actio`): A specific planned action to reduce the likelihood or impact of an identified risk — the operational response. Mitigation actions have owners, due dates, status, and cost. [PMI PMBOK 11.5 | Low | Corrective action, preventive action, design modification, schedule acceleration, additional inspect]
  - Incident actions in Procore link to observations (observation_id) — this creates a closed-loop safety risk mitigation path. General risk mitigation has no equivalent tracking.
- **Contingency Reserve** (`rk-contingency-rese`): A budget allocation held in reserve for identified risks — financial buffer against cost uncertainty. Contingency is typically 3-10% of project cost depending on project complexity and phase (higher in early phases, drawn down as risks are resolved o... [AACE 40R-08 (Contingency Estimating) | Low | 3-5% for well-defined projects]
  - Contingency management is one of the least standardized practices in construction. Some owners hold contingency; some GCs hold it; some split it.
- **Schedule Buffer** (`rk-schedule-buffer`): Time reserves built into the project schedule to absorb schedule risk — the temporal equivalent of contingency reserve. Buffers may be explicit (milestone buffers between phases) or implicit (float in non-critical paths). [AACE 10S-90 | Low | 5-15% of activity duration as buffers]
  - In practice, schedule buffers are consumed silently — contractors use float without explicit tracking. Float erosion analysis from Procore schedule data can reveal hidden buffer consumption.
- **Residual Risk** (`rk-residual-risk`): The remaining risk exposure after mitigation actions are applied — the risk that persists despite response efforts. Residual risk may be accepted, monitored, or require additional response. [PMI PMBOK 11.5 | None | Re-scored risk after mitigation (lower likelihood and/or impact)]
  - Residual risk is rarely tracked formally in construction. Most teams re-assess risks qualitatively at milestone reviews rather than quantitatively re-scoring.

**Risk Categories**
- **Design Risk** (`rk-design-risk`): Risk arising from incomplete, conflicting, or evolving design — the most common source of change orders in construction. [AIA A201 (design liability) | Medium | Incomplete drawings, conflicting details, late design decisions, owner scope changes, code interpret]
  - Procore signals for design risk are strong: change_reason + RFI predicted_topic + coordination_issues provide three independent detection surfaces. See Insight #31 validation.
- **Construction Execution Risk** (`rk-const-execution`): Risk from means and methods, productivity, sequencing, and trade coordination — the risk of building it wrong or slow. [OSHA 29 CFR 1926 | Medium | Rework, out-of-sequence work, trade stacking, access conflicts, equipment failure, crew productivity]
  - Execution risk signals in Procore: observation.category='Quality' (5,923 cos), punch_item.name (11,722 cos), inspection_items.status='Deficient'. See Insights #1 and #4.
- **Financial Risk** (`rk-financial-risk`): Risk of cost overruns, cash flow problems, payment disputes, or contractor default — the money risks. Includes budget variance (actual > plan), cash flow gaps (invoices outpacing payments), subcontractor financial health (inability to complete), and ... [AACE 62R-11 | Medium | Budget overrun, change order disputes, payment delays, subcontractor default, material price escalat]
  - Financial risk detection in Procore relies on change order rate, budget variance, and invoice timing — all available but require computed metrics, not raw fields.
- **Schedule Risk** (`rk-schedule-risk`): Risk of delays and timeline overruns from any cause — weather, permits, material delivery, labor shortages, design changes, differing site conditions. [AACE 62R-11 | Medium | Weather delays, permit delays, material delivery delays, labor shortages, design change delays, diff]
  - Procore's delay log is one of the strongest schedule risk signals in the industry — structured delay_type with duration and comments. Most competitors have unstructured delay tracking.
- **Safety Risk** (`rk-safety-risk`): Risk of injuries, fatalities, and safety incidents — the most regulated and consequential risk category. Safety risk is measured by incident rates (TRIR, DART, EMR), managed through hazard identification and mitigation, and regulated by OSHA. [OSHA 29 CFR 1926 | High | Fall hazard, struck-by, electrical, caught-in/between, trenching/excavation, scaffolding, crane oper]
  - Safety is Procore's strongest risk data domain. Incident + observation + inspection create a three-layer safety risk detection system. See Insight #11 for recurrence patterns.
- **Environmental Risk** (`rk-enviro-risk`): Risk from contamination, hazardous materials, spills, weather events, and environmental compliance — both site-condition risk (what's already there) and operational risk (what the project creates). [EPA regulations | Medium | Soil contamination, asbestos/lead abatement, stormwater violations, spill events, endangered species]
  - Environmental risk is often the highest-consequence risk on renovation and industrial projects but has the lowest data maturity in construction software.
- **Regulatory and Permit Risk** (`rk-reg-permit-risk`): Risk from permitting delays, code changes, inspection failures, and regulatory enforcement — the risk that authorities block or delay work. [IBC | Low | Permit delay, failed inspection, code change mid-project, zoning variance denial, utility connection]
  - Permit risk is critical-path but data-poor in construction software. The data lives in municipal systems, not project management tools.
- **Supply Chain Risk** (`rk-supply-chain`): Risk from material shortages, delivery delays, price escalation, and sole-source dependencies — the risk that what you need isn't available when you need it. [AACE 62R-11 | Medium | Material shortage, delivery delay, price escalation, sole-source vulnerability, fabrication delay, s]
  - Procore's material delay signal (daily_log_delay) is structured and high-volume. Combined with submittal overdue tracking, it provides two independent supply chain risk indicators.
- **Geotechnical Risk** (`rk-geotechnical-ris`): Risk from unforeseen subsurface conditions — the most unpredictable risk in construction. Includes unexpected soil conditions, groundwater, contamination, underground utilities, and rock. [ASCE 21 (Geotechnical Baseline Reports) | None | Unexpected rock, high water table, contaminated soil, unknown utilities, settlement, unstable slopes]
  - Geotechnical risk is the classic 'unknown unknown' — by definition, the data doesn't exist until discovery. Pre-construction geotech reports are typically PDFs outside construction software.
- **Labor Risk** (`rk-labor-risk`): Risk from workforce availability, productivity variance, jurisdictional disputes, and labor relations — the people risk. [Bureau of Labor Statistics | Low | Skilled labor shortage, productivity loss, jurisdictional dispute, union work rules, absenteeism, ke]
  - Labor risk is the #1 concern for US contractors but the least digitized risk category. Most labor data lives in timekeeping systems separate from project management.
- **Coordination Risk** (`rk-coord-risk`): Risk from trade interference, design conflicts, and inadequate planning — the risk that parallel workstreams collide. [BIM Execution Plan | Low | Trade stacking, spatial conflicts, above-ceiling congestion, MEP coordination failures, design-field]
  - Coordination risk increases nonlinearly with project complexity. MEP-heavy projects (hospitals, data centers, labs) have the highest coordination risk.

**Risk Transfer & Allocation**
- **Insurance Requirement** (`rk-insurance-requir`): The contractual obligation for project participants to carry specific insurance coverages — the financial backstop for risk transfer. [AIA A201 (insurance provisions) | High | General Liability, Workers' Comp, Umbrella/Excess, Builders Risk, Professional Liability, Pollution,]
  - Procore's insurance tracking is one of the most complete risk transfer data sets in the platform — structured types, amounts, dates, and compliance status.
- **Surety Bond** (`rk-surety-bond`): A three-party guarantee that a contractor will fulfill contractual obligations — bid bonds (guarantee bid price), performance bonds (guarantee completion), and payment bonds (guarantee subcontractor/supplier payment). [Miller Act (federal) | None | Bid bond (5-10% of bid), Performance bond (100% of contract), Payment bond (100% of contract), Maint]
  - Bonds are a critical risk transfer mechanism but poorly tracked in project management software. Most bond data lives in contract documents and surety company systems.
- **Risk Allocation** (`rk-risk-allocation`): The contractual assignment of specific risks to parties — who bears the consequence when a risk materializes. Risk allocation is defined in contract terms and varies by delivery method. [AIA A201 | None | Owner-retained risks (permitting, financing, code changes), Contractor-retained risks (means/methods]
  - Risk allocation is the most consequential and least digitized aspect of risk management. It determines who pays when things go wrong — and it's all in contract prose.

**Standard Measures**
- **Risk Exposure Value** (`rk-risk-exposure`): Total financial exposure from identified risks — sum of (likelihood × cost impact) across all risks in the register. Provides a single number representing the project's aggregate risk in dollar terms. [AACE 40R-08 | None | Typically 5-15% of project value for active risk exposure]
- **Contingency Burn Rate** (`fi-contingency-burn`): Rate at which contingency reserve is consumed over project duration — actual contingency usage divided by elapsed project time. A leading indicator: fast burn early signals cost risk. [AACE 40R-08 | Low | Below 0.5 (healthy), 0.5-1.0 (monitor), above 1.0 (at risk)]
- **Incident Rate (TRIR)** (`rk-incident-rate`): Total Recordable Incident Rate — the standard OSHA safety metric. Formula: (number of recordable incidents × 200,000) / total hours worked. Measures overall safety risk realization. [OSHA 29 CFR 1904 | High | Construction industry avg TRIR: 2.5-3.0]
  - TRIR is the single most important risk metric in construction. Procore has recordable flag and severity data; the gap is hours worked (denominator), which comes from timekeeping systems.
- **Risk Mitigation Completion Rate** (`rk-risk-mitigation`): Percentage of planned mitigation actions completed on time — measures the effectiveness of risk response execution. Formula: completed actions / total planned actions. Tracks whether the team is actually doing what they planned to manage risk. [PMI PMBOK 11.6 | Low | Above 80% (strong risk management), 60-80% (adequate), below 60% (risk management breakdown)]
- **Change Order Rate** (`fi-chg-order-rate`): Percentage of original contract value added through change orders — a proxy for scope and design risk realization. Formula: total approved change order value / original contract value. Higher rates indicate more realized risk. [AACE 62R-11 | High | 5-10% (well-managed), 10-15% (typical), 15-25% (high risk realized), >25% (distressed)]
- **Schedule Float Erosion** (`rk-schedule-float`): Rate at which total float is consumed across the project schedule — a leading indicator of schedule risk. Formula: (baseline total float - current total float) / baseline total float. [AACE 10S-90 | Low | 0-20% consumed (healthy), 20-50% (monitor), >50% (critical)]

### Roles

**Project Leadership**
- **Owner's Representative** (`rl-owner-s`): Owner's on-site or dedicated agent who makes decisions on the owner's behalf — design review, scope decisions, change authorization, acceptance of work, dispute resolution, stakeholder management. [CMAA (owner representation standards) | Medium | Owner's rep]
  - Scope of authority varies by contract — some can authorize changes up to a threshold, others must escalate. Critical gatekeeper.
- **Project Executive** (`rl-project-executiv`): Senior leader overseeing a project or group of projects for the GC or CM — portfolio oversight, client relationship, risk escalation, financial performance, resource allocation, contract negotiations. [PMI PMP/PgMP | Low | Project exec]
  - Typically manages 2-5 projects simultaneously. The PE is the GC's senior relationship with the owner. Gets involved for major decisions and problem resolution.
- **Project Manager** (`rl-project-manager`): Day-to-day leader of the project — owns schedule, budget, and subcontractor management. Consumes daily reports, budget/schedule updates, RFIs, submittals, change events, pay applications. [PMI PMP | High | PM]
  - schedule variance) across project types
- **Assistant Project Manager** (`rl-assistant-projec`): Supports PM with day-to-day management — often assigned specific scope areas or administrative functions. Manages submittal tracking, RFI coordination, subcontract administration, insurance tracking, meeting coordination, document control. [PMI CAPM | Medium | APM]
  - Career progression: APM → PM → PE. The APM role is where most people learn construction management. Typically assigned specific trades.
- **Design Manager** (`rl-design-manager`): Manages the design process and design team coordination for the GC or owner — design review, constructability review, design schedule management, value engineering. Primarily a design-build or CM at Risk role. [AIA (design phase standards) | Low | Design manager]
  - Bridges the gap between design intent and construction reality. Manages the A/E team on behalf of the GC. Cross-domain: Organizations (Design Team), Phases (Design Development).

**Field Operations**
- **Superintendent** (`rl-super`): Senior field leader responsible for day-to-day construction operations — trade coordination, schedule enforcement, quality oversight, safety enforcement, site logistics, daily reporting. [OSHA 29 CFR 1926 (competent person requirements) | High | Superintendent]
  - The superintendent owns the field — everything on site flows through the super. Typically the most experienced person on the project.
- **Assistant Superintendent** (`rl-assistant-super`): Supports superintendent with field coordination — often assigned to specific building areas or trades. Manages area-specific trade coordination, daily documentation, inspection coordination, material tracking, quality walks. [OSHA 29 CFR 1926 | Medium | Assistant super]
  - Often assigned specific floors, areas, or trade groups. Career path to superintendent. May have 1-3 areas depending on project size.
- **Project Engineer** (`rl-project-engineer`): Technical field support — manages engineering and documentation aspects of field work. Drafts RFIs, coordinates submittals, tracks as-builts, reviews shop drawings, tracks quantities, solves technical problems. [PMI | Medium | PE (field)]
  - Often the first to identify technical conflicts. Strong career development role. Cross-domain: Documents (RFIs, submittals), Building Elements (technical issues).
- **Field Engineer** (`rl-field-engineer`): Entry-level field position focused on surveying, layout, and construction documentation — concrete placement monitoring, quantity verification, material receiving, photo documentation. Starting point for most construction careers. [OSHA 10/30 (safety training) | Low | Field engineer]
  - Gets hands dirty — learns how buildings actually go together. Transitions to PE or assistant super. Cross-domain: Field Operations (daily documentation).
- **Foreman / General Foreman** (`rl-foreman-gen`): Trade-specific field leader who manages a crew of 4-20 workers on a daily basis — daily work assignments, material coordination, quality of installed work, safety compliance, productivity. The link between management and craft workers. [OSHA 29 CFR 1926 (competent person) | Medium | Foreman]
  - A good foreman maximizes crew productivity. Cross-domain: Resources (Trades), Field Operations (manpower tracking).
- **Journeyman / Craft Worker** (`rl-journeyman-craft`): Skilled tradesperson who performs the physical construction work — licensed or certified in their trade. Installs trade-specific work per drawings and specs, maintains quality workmanship, complies with safety procedures. [State licensing (electricians, plumbers) | Medium | Journeyman]
  - Licensed electricians, plumbers, ironworkers, operators, etc. Union or non-union. Apprenticeship programs feed the pipeline. Cross-domain: Resources (Trades).
- **Apprentice** (`rl-apprentice`): Trades worker in training — learning under journeyman supervision as part of a formal 3-5 year program. Performs assigned tasks, attends trade school, progresses toward journeyman status. Active during Construction. [DOL (Department of Labor — registered apprenticeship) | Medium | Apprentice]
  - Formal apprenticeship programs are the primary skilled labor pipeline. Required on many public projects with workforce development mandates. Cross-domain: Resources (Trades).

**Safety & Quality**
- **Safety Manager / Safety Director** (`rl-safety-manager`): Dedicated safety professional responsible for the project's or company's safety program — site inspections, incident investigation, OSHA compliance, safety training, subcontractor safety oversight. [OSHA 29 CFR 1926 | Medium | Safety manager]
  - On large projects, full-time dedicated. On smaller projects, superintendent may double as safety. Third-party consultants common.
- **Safety Officer / Safety Coordinator** (`rl-safety-officer`): Field-level safety personnel conducting daily site safety activities — safety walks, toolbox talks, new worker orientation, PPE compliance, housekeeping inspections, near-miss documentation. Boots-on-the-ground safety presence. [OSHA 29 CFR 1926 | Low | Safety officer]
  - Multiple safety officers on large projects. Subcontractor safety officers supplement GC staff. Cross-domain: Quality & Safety Records (observations).
- **Quality Manager / QC Inspector** (`rl-quality-manager`): Dedicated quality professional responsible for QA/QC across the project — inspection coordination, deficiency tracking, specification compliance, material testing coordination, non-conformance management. [ISO 9001 (quality management) | Medium | QC manager]
  - Dedicated QC roles more common on large/complex projects (healthcare, data centers, federal). On typical commercial, quality falls to super and PE. Cross-domain: Quality & Safety Records.

**Preconstruction & Estimating**
- **Estimator / Chief Estimator** (`rl-estimator-chief`): Develops cost estimates from conceptual through detailed pricing — quantity takeoff, unit pricing, subcontractor bid solicitation and leveling, risk pricing, GMP development, value engineering. [AACE CEP (certified estimating professional) | Medium | Estimator]
  - Estimating is where projects are won or lost. Accuracy depends on experience and historical data. Conceptual ±20%, detailed ±5%. Cross-domain: Financial Instruments (budget origination).
- **Preconstruction Manager** (`rl-preconstruction`): Leads the preconstruction effort — coordinates estimating, scheduling, constructability, client presentations, GMP negotiation, value engineering facilitation, risk assessment, subcontractor prequalification. Active during Preconstruction. [CMAA | Low | Precon manager]
  - The GC's lead during the pre-award phase. Win rate depends on ability to build trust with owner and architect. Cross-domain: Organizations (CM at Risk), Phases (Preconstruction).

**Project Controls**
- **Scheduler / Project Controls Manager** (`rl-scheduler-projec`): Manages the project schedule and schedule-related analytics — schedule development, updates, critical path analysis, delay analysis, resource loading, earned value management, schedule risk assessment. [AACE PSP (planning and scheduling professional) | Medium | Scheduler]
  - Schedule management ranges from basic bar charts (small) to full P6 with EVM (large). Delay analysis expertise is critical for claims.
- **Document Controller** (`rl-doc-controller`): Manages the project document management system — document numbering, drawing distribution, revision control, submittal routing, RFI routing, transmittal management, archiving. Active across all phases. [CSI (document management standards) | Medium | Document controller]
  - On large projects, a full-time role. On smaller projects, the APM handles it. Discipline (or lack thereof) affects every other role. Cross-domain: Documents & Communications (all elements).
- **Cost Engineer / Cost Analyst** (`rl-cost-engineer`): Tracks and forecasts project costs — cost tracking, forecast updates, change order impact analysis, cash flow projections, earned value analysis, budget variance reporting. More common on large projects ($50M+). [AACE CCE (certified cost engineer) | Medium | Cost engineer]
  - Cost engineering and scheduling increasingly converge in project controls. On smaller projects, the PM handles cost management directly. Cross-domain: Financial Instruments (all cost surfaces).

**BIM & Technology**
- **BIM Manager / VDC Coordinator** (`rl-bim-manager-vdc`): Manages the building information model and virtual design and construction processes — BIM execution plan, model management, clash detection, trade coordination, 4D scheduling, quantity extraction, reality capture management. [AIA E203 (BIM protocol) | Medium | BIM manager]
  - BIM/VDC roles are standard on projects over $20M. LOD specification governs model reliability. Cross-domain: Phases (Above-Ceiling Coordination), Building Elements (all systems).
- **Technology Manager** (`rl-tech-manager`): Manages project technology infrastructure — software deployment, mobile device management, network infrastructure, system integration, data management, user training. Increasingly important as construction becomes more technology-dependent. [CompTIA | Low | IT manager]
  - Field tablets, drones, 360 cameras, IoT sensors all require technology management. Cross-domain: all domains (technology enables data capture across every domain).

**Procurement & Contracts**
- **Procurement Manager** (`rl-procure-manager`): Manages the procurement process from bid solicitation through contract execution — bid package development, bid solicitation, bid leveling, scope review, contract negotiation, insurance and bonding verification. [ISM (Institute for Supply Management) | Medium | Procurement manager]
  - On large projects, a dedicated role. On smaller projects, PM handles procurement. Early procurement of long-lead items is schedule-critical.
- **Contract Administrator** (`rl-contract-adminis`): Manages contract compliance and commercial processes after execution — change order processing, pay application review, lien waiver collection, insurance certificate tracking, retainage management. Active from Construction through Closeout. [AIA A201 (contract administration) | Medium | Contract admin]
  - Often combined with APM role on mid-size projects. The commercial backbone of the project. Cross-domain: Financial Instruments (all commercial instruments), Organizations (Trade Contractors).

**Commissioning & Startup**
- **Commissioning Agent (CxA)** (`rl-cx-agent-cxa`): Independent professional who verifies building systems perform as designed — commissioning plan development, pre-functional testing, functional performance testing, deficiency tracking, seasonal testing, final report. [ASHRAE Guideline 0 | Low | CxA]
  - CxA independence is key — represents owner's interest in system performance. LEED requires CxA. Enhanced CxA extends to envelope. Cross-domain: Organizations (CxA firm), Phases (Commissioning).
- **TAB Technician** (`rl-tab-technician`): Testing, Adjusting, and Balancing technician who measures and adjusts air and water flow rates to design values — air system balancing, hydronic balancing, sound and vibration measurement. [AABC (certification) | None | TAB technician]
  - TAB data is foundational — HVAC commissioning depends on balanced systems. Results directly affect occupant comfort. Cross-domain: Phases (Testing Adjusting & Balancing), Building Elements (HVAC).

**Office & Administrative**
- **Office Manager / Project Admin** (`rl-office-manager`): Manages the project office and administrative operations — office operations, filing, correspondence management, meeting scheduling, visitor management, event coordination. Active across all phases. [No specific industry standard — general office management | Low | Office manager]
  - On large projects, a dedicated role managing a trailer with 10-30 people. On smaller projects, admin tasks fall to APM or PE.
- **Accountant / Financial Analyst** (`rl-accountant-finan`): Manages project financial transactions and reporting — invoice processing, pay application processing, job cost tracking, financial reporting, audit support, tax compliance. Company-level role supporting multiple projects. Active across all phases. [AICPA | Medium | Project accountant]
  - On large projects, may have dedicated project accountant. Financial close each month drives reporting cadence. Cross-domain: Financial Instruments (billing and payment).

**Standard Measures**
- **Staffing Ratio** (`rl-staffing-ratio`): Ratio of management staff (PM, super, PE, APM) to project value or subcontractor count — indicates project resourcing adequacy. Calculated as management headcount / project value band or management headcount / active subcontractor count. [PMI PMBOK (resource management) | High | Typical: 1 PM per $20-50M]
  - Under-staffed projects correlate with higher deficiency rates, slower RFI response, and more schedule slippage.
- **Role Coverage Rate** (`rl-role-coverage`): Percentage of key project roles filled at any point in the project timeline — filled roles / required roles × 100. Tracks gaps in project team staffing that create risk. [PMI PMBOK | High | Expressed as percentage]
  - Safety manager and QC roles are the most commonly vacant on mid-size projects. Cross-domain: Organizations (staffing responsibility).
- **PM Workload Index** (`rl-pm-workload`): Number of active projects per project manager — indicates workload balance and risk of attention dilution. Calculated from PM role assignments across the active project portfolio. [PMI (resource management) | High | Typical: 1-2 projects (large/complex)]
  - schedule variance)
- **Superintendent Span of Control** (`rl-super-span`): Number of active subcontractors and direct reports managed by a single superintendent — indicates field coordination burden. Calculated from active vendor count and crew headcount per superintendent. [AGC (field management staffing) | High | Typical: 8-15 active subs per super (manageable)]
  - High span of control correlates with lower daily log compliance, more safety incidents, and more punch items. Cross-domain: Field Operations, Quality & Safety Records.
- **Safety Staffing Ratio** (`rl-safety-staffing`): Ratio of dedicated safety personnel to total workforce — safety staff headcount / peak daily workforce × 100. Indicates safety program investment and correlates with incident rates. [OSHA recommendations | Medium | Typical: 1 safety person per 50-100 workers]
  - Higher safety staffing ratios consistently correlate with lower incident rates. Cross-domain: Quality & Safety Records, Recurring Violations (insight #11).

### Schedule

**Activity Structure**
- **Detail Activity** (`sch-detail-activity`): The lowest-level schedulable work item — has its own duration, logic ties, resources, and cost assignment. The fundamental unit of CPM scheduling. Typical duration 5-20 working days; activities exceeding 20 days indicate insufficient detail. [AACE 10S-90 | High | 5-20 working day duration (typical)]
  - Activities > 40 working days are a red flag in most specifications. LOE activities should not be on the critical path.
- **Summary Activity & WBS** (`sch-summary-activity`): Roll-up activity that aggregates child activities into a single bar — no independent duration or resources. Used for Work Breakdown Structure nodes, phase summaries, and area roll-ups. [AACE 10S-90 | Medium | WBS summary, phase summary, area summary, hammock (duration-driven span)]
  - Summary activities should not have logic ties in most specifications. Hammocks are useful for measuring elapsed time of a phase.
- **Milestone** (`sch-milestone`): Zero-duration marker representing a key event — start milestone or finish milestone. Contractual milestones carry liquidated damages. [AACE 10S-90 | High | Start milestones, finish milestones, contractual milestones, interim milestones, procurement milesto]
  - Contractual milestones with liquidated damages are the highest-consequence schedule elements.
- **Activity Identification** (`sch-activity-identif`): The naming and coding conventions that make activities findable, filterable, and analyzable. Activity ID follows a coding convention encoding phase/area/trade (e.g., A1000, 03-EL-0100). [AACE 10S-90 | High | ID format varies by contractor]
  - Good IDs encode WBS level, trade, and sequence. Good names include what work, where, by whom. Quality varies enormously across contractors.
- **Duration & Progress** (`sch-duration-progres`): The time dimension of an activity — original duration (planned at baseline), remaining duration (days left from data date), actual start/finish dates, and percent complete. [AACE 10S-90 | High | Original 5-20 working days]
  - Remaining duration creep (remaining > original) is a leading indicator of schedule slip. Physical % from field measurement is most accurate.
- **Activity Codes** (`sch-activity-codes`): Classification codes assigned to activities for grouping, filtering, sorting, and reporting — the dimensional analysis framework for schedule data. [AACE 10S-90 | Medium | Trade, area/zone, phase, responsibility, CSI division, building system, crew]
  - Custom field framework replaces rigid activity code structures with extensible fields. Enables trade, area, phase, and responsibility analysis.

**Logic & Dependencies**
- **Relationship Type** (`sch-relationship-typ`): The logical connection between two activities that drives the CPM calculation. Four types: Finish-to-Start (FS, most common, ~80-90% of ties), Start-to-Start (SS, overlapping work), Finish-to-Finish (FF, activities ending together), Start-to-Finish (... [AACE 10S-90 | High | FS (~80-90% of ties), SS (often paired with FF), FF (paired with SS), SF (<1% — often error)]
  - Heavy SS/FF without pairing can obscure the critical path. SF ties should be flagged for review. DCMA 14-point check #4.
- **Lag & Lead Time** (`sch-lag-lead-time`): Time offset on a logical relationship — positive lag represents waiting time (concrete cure 7-28 days, submittal review 14-21 days, coating dry 1-3 days). Negative lag (lead) represents overlap — many specifications prohibit entirely. [AACE 10S-90 | High | Concrete cure 7-28 days]
  - Best practice: use SS relationships instead of negative lag on FS ties. Lag >20 days should document what's being waited for. DCMA checks #2 and #3.
- **Dependency Classification** (`sch-dependency-class`): Categorization of why two activities are linked — determines which relationships can change during delay analysis. Mandatory (hard logic): physical or contractual requirement (foundation before structure). [AACE 10S-90 | Low | Mandatory (physical sequence), Discretionary (preferred order), External (third-party driven)]
  - P6 and MS Project don't natively distinguish hard from soft logic. This classification exists in scheduler judgment and delay analysis documentation.
- **Open Ends** (`sch-open-ends`): Activities missing predecessors (open start) or successors (open finish) — logic gaps that distort CPM calculations. Only the project start and finish milestones should have open ends. Open starts can begin on the data date regardless of logic. [AACE 10S-90 | Medium | Open starts = missing predecessor]
  - The most fundamental schedule quality issue. One of the DCMA 14-point checks. Open ends invalidate float calculations.
- **Logic Density & Redundancy** (`sch-logic-density`): Schedule connectedness measured by relationship-to-activity ratio. Logic density healthy range: 1.5-2.5 relationships per activity. Below 1.2 means loosely connected (CPM unreliable). Above 3.0 may indicate over-constraining. [AACE 10S-90 | Medium | Density 1.5-2.5 (healthy)]
  - Low density means CPM calculation is unreliable — activities float freely without proper logic connections.

**Time Management**
- **Work Calendar** (`sch-work-calendar`): Definition of working days and hours that drives duration-to-date conversion in the CPM. Standard 5-day (Mon-Fri, default), 6-day (adds Saturday, +17% capacity), 7-day (continuous — for cure time and critical path compression), weather-adjusted (anti... [AACE 10S-90 | Medium | 5-day (default), 6-day (compressed), 7-day (cure/continuous), weather (regional), holiday (contractu]
  - Concrete cure on a 5-day calendar is a common error. Weather calendar thresholds per month define excusable delay for time extensions.
- **Schedule Constraint** (`sch-schedule-constra`): Date override on an activity that restricts CPM calculation — from permissive (ASAP, the default) to absolute (Must Start/Finish On). Every non-default constraint should have documented justification. [AACE 10S-90 | Medium | ASAP (default), SNET (start no earlier than), SNLT (start no later than), FNLT (finish no later than]
  - Must constraints break CPM logic entirely. FNLT on the last activity typically sets the contractual completion date. Negative float against FNLT = projected late.
- **Calculated Dates** (`sch-calculated-dates`): Dates produced by the CPM forward and backward pass calculations. Early Start/Early Finish: earliest possible dates from forward pass through logic and calendars. Late Start/Late Finish: latest dates from backward pass without delaying the project. [AACE 10S-90 | Medium | Early Start (ES), Early Finish (EF), Late Start (LS), Late Finish (LF)]
  - Forward pass: ES = max(predecessor EF + lag). Backward pass: LF = min(successor LS - lag). Critical path = where ES = LS.
- **Data Date** (`sch-data-date`): The status date of the schedule update — divides past from future. All progress is recorded as-of the data date. Activities with actual start after the data date or remaining work before it are out-of-sequence. [AACE 10S-90 | Medium | Month-end or contractual cut-off]
  - Data date currency (how recently updated) is itself a schedule management quality signal. Stale data dates indicate neglected schedules.
- **Baseline Dates** (`sch-baseline-dates`): The approved planned dates from the baseline schedule — the 'as-planned' reference against which all performance is measured. Original baseline (BL0) is the contractual reference submitted 30-90 days after NTP. [AACE 10S-90 | Medium | BL0 = original plan, BL1/BL2 = re-baselines after approved changes]
  - BL0 is sacrosanct — modifications require formal owner approval. Too-frequent re-baselining obscures true performance.

**Schedule Analysis**
- **Float / Slack** (`sch-float-slack`): Calendar days an activity can be delayed without downstream or project-level impact. Total Float: delay without delaying project completion (LF-EF). Free Float: delay without delaying any immediate successor. [AACE 10S-90 | High | Critical: TF=0]
  - Artificial constraints can inflate or deflate float. Negative float triggers recovery schedule requirement in most contracts. DCMA checks #6, #7.
- **Critical Path** (`sch-critical-path`): The longest continuous chain of activities and relationships determining minimum project duration — zero or least total float. Typically 10-15% of activities are critical on a well-built schedule. [AACE 10S-90 | High | Critical: TF ≤ 0]
  - >40% near-critical means schedule is fragile — almost no recovery room. Critical path shift analysis reveals actual project progression vs. plan.
- **Path Analysis Methods** (`sch-path-analysis`): Advanced techniques for tracing schedule logic beyond simple total float. Longest Path: traces driving relationships backward from project finish — more reliable than TF=0 when constraints distort float. [AACE 10S-90 | Low | Longest path algorithm (P6), driving relationship identification, path convergence analysis]
  - P6's Longest Path algorithm is more accurate than TF=0 when constraints inflate/deflate float. MS Project has limited path analysis capability.
- **Earned Schedule** (`sch-earned-schedule`): Time-based earned value method — measures schedule performance in time units instead of cost units. ES = the time at which current earned value should have been achieved per baseline. SPI(t) = ES / Actual Time. [AACE recommended practice | Low | SPI(t) >1.0 = ahead]
  - Traditional cost-based SPI is unreliable for schedule measurement. ES requires disciplined baseline and progress tracking.

**Schedule Lifecycle**
- **Baseline Schedule** (`sch-baseline-schedul`): The approved planned schedule against which all performance is measured — the contractual 'as-planned' reference. Original Baseline (BL0) submitted 30-90 days after NTP per typical specifications with 2-4 review cycles. [AACE 10S-90 | Medium | BL0 = original, BL1/BL2 = re-baselines]
  - BL0 is sacrosanct — modifications require formal owner approval. What-if analysis should always work on a copy, never the live schedule.
- **Schedule Update** (`sch-schedule-update`): The periodic progress recording and schedule recalculation cycle — the primary schedule management process. Monthly standard (bi-weekly on fast-track). [AACE 10S-90 | Medium | Monthly (standard) or bi-weekly (fast-track)]
  - Out-of-sequence progress means field is working in different order than schedule logic. P6 offers Retained Logic (safer) vs. Progress Override (aggressive).
- **Look-Ahead Schedule** (`sch-look-ahead`): Rolling short-term schedule showing daily/weekly detail for the next 3-6 weeks — the superintendent's primary planning tool. Three-week: daily detail for crew assignments, material deliveries, inspections. [Common practice | High | 3-week (daily detail, weekly update), 6-week (weekly detail, coordination focus)]
  - Look-aheads as a first-class entity with their own tasks and assignees is a differentiated capability vs. P6/MS Project filtered views.
- **Recovery Schedule** (`sch-recovery-schedul`): Plan to recover lost time and return to the contractual completion date after a delay. Required when negative float exceeds a contract threshold (often 10-20 days). [AACE 10S-90 | Low | Triggered by negative float >10-20 days]
  - Must show specific recovery actions, not just compressed durations. A common contractual remedy when the project falls behind.
- **As-Built Schedule** (`sch-as-built`): Final schedule reflecting actual dates for all activities — the factual record of how construction actually progressed. All activities have actual start and actual finish with no remaining duration. [AACE 10S-90 | Low | All activities 100% complete with actual dates]
  - If monthly updates were poor, the as-built is unreliable. Procore field data (daily logs, observations) can independently validate actual dates.

**Resource & Cost Loading**
- **Labor Loading** (`sch-labor-loading`): Trade-specific labor hours assigned to schedule activities — drives manpower histograms, workforce planning, and crew optimization. Shows when each trade peaks and valleys over the project. [AACE 10S-90 | Medium | Electrician-hours, carpenter-hours, ironworker-hours per activity]
  - Daily manpower logs can validate planned vs. actual labor — a feedback loop standalone scheduling tools cannot provide.
- **Equipment Loading** (`sch-equip-loading`): Major equipment utilization assigned to schedule activities — identifies mobilization timing, utilization gaps, and equipment-driven constraints. Tower crane is the most impactful — crane time allocation drives structural and enclosure sequences. [AACE 10S-90 | Medium | Tower crane-days, pump truck-hours, excavator-days, hoist-hours per activity]
  - Tower crane availability is often the single biggest schedule constraint on high-rise projects.
- **Cost Loading & Cash Flow** (`sch-cost-loading`): Dollar values distributed across schedule activities for earned value measurement and cash flow projection. Activity cost = labor + material + equipment + subcontract. Produces the S-curve (cumulative planned vs. [AACE 10S-90 | Low | Planned Value (PV), Earned Value (EV), Actual Cost (AC)]
  - Cost-loaded schedule connects the time model to the financial model. Misalignment between scheduled cost and actual billing is a warning sign.
- **Resource Leveling** (`sch-resource-levelin`): Adjusting activity timing within available float to smooth resource demand — avoid peaks and valleys without extending the project. [AACE 10S-90 | None | Peak-to-average ratio]
  - Auto-leveling in P6/MS Project can produce illogical sequences. Best practice: use float to manually smooth peaks. Never level the critical path.

**Delay & Claims**
- **Delay Classification** (`sch-delay-class`): Categorization of delays by cause and remedy — determines entitlement to time extension and/or compensation. Excusable Compensable: owner-caused, time + money (design errors, late owner items). [AACE 29R-03 | Medium | Excusable Compensable (owner-caused), Excusable Non-Compensable (weather/force majeure), Non-Excusab]
  - Concurrent delay has no universal rule — jurisdictions differ on apportionment. Procore daily delay logs capture weather and material delays with structured type field.
- **Time Impact Analysis** (`sch-time-impact`): The gold standard prospective delay analysis method — inserts a fragnet (delay event network of 3-20 activities) into the updated schedule at the time of impact and compares before/after CPM results. [AACE 29R-03 | Low | Fragnet: 3-20 activities representing the delay]
  - A well-built fragnet accurately represents the delay event. Expert judgment required. Quality depends on having valid contemporaneous schedule updates.
- **Retrospective Delay Analysis** (`sch-retrospective-de`): After-the-fact methods comparing planned vs. actual schedules. As-Planned vs. As-Built: simplest, compares BL0 to actual dates, shows variance but not causation. [AACE 29R-03 | Low | As-Planned vs. As-Built (simplest), Collapsed As-Built/But-For (claimant-favored), Windows Analysis ]
  - Windows Analysis requires good schedule updates for each period. As-Planned vs. As-Built doesn't handle concurrent delay. Method selection is often contested.
- **Time Extension Request** (`sch-time-extension`): Formal written request for additional contract time due to an excusable delay event. Must be submitted within the contract notice period (typically 7-21 days). [Contract specifications | Medium | Submitted within 7-21 day notice period]
  - Timely notice is critical — many contracts bar claims submitted after the notice period. Change events are the primary instrument for formal time extensions.
- **Acceleration** (`sch-acceleration`): Direction (explicit or constructive) to complete work faster than the adjusted contractual schedule. Explicit: written owner directive with cost reimbursement. [AACE | Low | Explicit (written directive with cost), Constructive (denied time extension + enforced date)]
  - Constructive acceleration occurs when the owner denies a valid time extension but insists on the original date. Documentation of denial and resulting cost is critical.

**Schedule Quality**
- **DCMA 14-Point Assessment** (`sch-dcma-14-point`): Defense Contract Management Agency schedule assessment framework — 14 checks covering logic, durations, float, constraints, relationships, resources, and critical path. [DCMA 14-Point Assessment | Medium | 14 checks: open ends, leads, lags (<5%), relationship types (<5% non-FS), constraints (<5%), high fl]
  - Not all 14 points apply equally to every project. Commercial construction typically focuses on checks 1-9 and CPLI.
- **Specification Compliance** (`sch-specification-co`): Contract-specific schedule requirements that must be met for baseline approval and ongoing updates. Activity duration limits (typically 15-20 working day max), relationship type ratios (FS >80-90%), calendar assignment rules (cure on 7-day, work on 5... [Contract specifications | Medium | Max duration 15-20 working days]
  - Specs vary by owner and contract. Activities exceeding duration limits must be broken down. Wrong calendar assignment distorts durations.
- **Critical Path Length Index** (`sch-critical-path-2`): (Critical path remaining duration + total float) / critical path remaining duration — a single-number predictor of schedule outcome. CPLI > 1.0: buffer exists. CPLI = 1.0: no buffer. CPLI < 1.0: project will finish late without recovery. [DCMA 14-Point Assessment (check #13) | Medium | CPLI >1.0 = buffer]
  - One of the most powerful schedule metrics. Simple enough for non-schedulers to understand. Trend over time reveals schedule trajectory.

**Schedule Integration**
- **Schedule Levels** (`sch-schedule-levels`): The hierarchy of schedule detail — from executive summary to daily work plan. Master/Summary: 50-200 activities, phase milestones, the owner's view. [AACE 10S-90 | High | Master (50-200 activities), Detailed CPM (500-5000+), Daily Work Plan (crew-level)]
  - Disconnect between schedule levels is a common problem. Daily work plans that link to CPM tasks close the gap between planning and execution.
- **CPM Tool Integration** (`sch-cpm-tool`): Importing the detailed schedule from the authoring tool (P6, MS Project, Asta) into the project management platform. The schedule is authored externally and consumed broadly. Import via XER/XML/MPP format. [Common practice | High | Import formats: XER (P6), XML, MPP (MS Project)]
  - Most GCs author schedules in P6 or MS Project but manage projects on a broader platform. Activity ID mapping is the bridge.
- **Schedule-to-Field Linkage** (`sch-schedule-field`): Connecting CPM activities to field data — daily logs, inspections, RFIs — to validate progress and identify discrepancies between planned and actual execution. The gap between CPM and field reality is the central problem in construction scheduling. [Emerging best practice | High | Actual dates validated by daily logs]
  - P6 has no field data. Native field-to-schedule linkage is a differentiated capability for project management platforms vs. standalone scheduling tools.
- **Schedule Change Tracking** (`sch-schedule-chg`): Timestamped record of every change to every schedule activity — capturing old values, new values, author, timestamp, and reason. Critical evidence in delay disputes: who changed what and when. Change frequency per activity identifies unstable areas. [AACE 10S-90 (change documentation) | High | Old/new for start, finish, duration, percentage, name]
  - Structured change tracking is more detailed than P6's Schedule Log. Field-initiated update requests add collaborative dimension. Reason field quality varies.

**Lean & Alternative**
- **Last Planner System** (`sch-last-planner`): Collaborative scheduling methodology where the people doing the work make reliable promises. Pull Planning: trades work backward from milestones to identify handoffs and constraints. [Lean Construction Institute (LCI) | Medium | PPC >80% = healthy, >85% = world-class]
  - PPC measures workflow reliability, not schedule progress. A project can be on schedule with low PPC (luck) or behind with high PPC (reliable but slow).
- **Takt Time Planning** (`sch-takt-time`): Fixed-rhythm scheduling where each trade moves through zones at the same pace — manufacturing flow applied to construction. Takt time = available time / number of zones. All trades match the same rhythm. [Lean Construction Institute | Low | Zone duration (takt) = available time / zones]
  - Growing adoption in repetitive construction (multi-family, hotels, hospitals). Reduces WIP and improves flow.
- **Linear Scheduling** (`sch-linear-schedulin`): Scheduling methods for repetitive or linear work where location is the primary axis. Line of Balance (LOB): graphical method showing production rate across identical units — each trade plotted as a line with slope = production rate. [AACE | None | LOB: Y-axis=location, X-axis=time, slope=production rate]
  - P6 and MS Project cannot natively produce LOB or time-distance diagrams. Tilos is the industry standard for linear projects.
- **4D/5D BIM Scheduling** (`sch-4d-5d-bim`): Linking 3D BIM model elements to CPM schedule activities for visual construction sequence simulation (4D) and adding cost data for time-phased cost visualization (5D). Animation shows construction progression over time. [AACE | Low | 4D = model + schedule (sequence animation)]
  - Requires: accurate 3D model, maintained element-to-activity links, regular re-sync. 5D adds cost-loaded elements for visual earned value.

**Standard Measures**
- **Schedule Performance Index** (`sch-schedule-perf`): Earned value / planned value — the primary schedule efficiency metric. Traditional SPI = EV/PV (cost-based, converges to 1.0 at project end, masking late delivery). Earned Schedule SPI(t) = ES/AT (time-based, remains accurate throughout). [PMI PMBOK | Low | SPI = 1.0 on schedule]
  - Duration-based SPI is more meaningful for construction than cost-based. SPI(t) using Earned Schedule doesn't converge to 1.0.
- **Baseline Execution Index** (`sch-baseline-executi`): Activities completed on or before baseline finish date / total activities completed in the period — measures execution discipline. Simpler and more intuitive than SPI. [AACE recommended practice | Medium | BEI = 1.0 all on time]
  - More intuitive than SPI for non-schedule audiences. Requires baseline dates. DCMA 14-Point check #14.
- **Float Erosion Rate** (`sch-float-erosion`): Rate of total float decrease across schedule updates — reveals whether the schedule is tightening faster than planned work completion. Calculation: average TF change per update period or % of activities losing float period-over-period. [AACE 10S-90 | Medium | Stable: avg TF change ≤ -2 days/update]
  - Normal float erosion occurs as a project progresses. Abnormal erosion (faster than planned work completion) signals emerging risk.
- **Milestone Adherence Rate** (`sch-milestone-adhere`): Milestones completed on or before their baseline date / total milestones due to date — a high-level schedule health KPI. Focuses on key events rather than all activities. More meaningful to owners and executives than SPI or float analysis. [Custom metric | Medium | Healthy: >80%]
  - Contractual milestones vs. interim milestones should be tracked separately. Contractual misses may trigger liquidated damages.
- **Critical Activity Ratio** (`sch-critical-activit`): Percentage of remaining activities that are critical (TF ≤ 0) — measures how much of the schedule is at risk of delay. Calculation: critical activities / total remaining activities. [AACE 10S-90 | High | Healthy: 10-15%]
  - >40% critical means almost no recovery room. The ratio naturally increases toward project end.
- **Percent Plan Complete** (`sch-percent-plan`): Percentage of weekly commitments completed as planned — the core lean scheduling metric from the Last Planner System. Calculation: PPC = tasks completed as committed / tasks committed. Measures workflow reliability, not schedule progress. [Lean Construction Institute | High | PPC >80% = healthy]
  - Showed boolean on daily scheduled work is a direct PPC input. One of the few metrics capturing field execution reliability.
- **Out-of-Sequence Rate** (`sch-out-sequence`): Activities with progress that violates their logical predecessors / total in-progress activities — indicates schedule-to-field alignment. Calculation: out-of-sequence activities / total in-progress. [AACE 10S-90 | Low | Target: <5%]
  - P6 handles with Retained Logic (safer) or Progress Override (aggressive). Most specs require Retained Logic.
- **Schedule Health Score** (`sch-schedule-health`): Composite metric aggregating multiple quality indicators into a single score — typically based on DCMA 14-Point Assessment. Each check is binary pass/fail; total pass count produces the health score. [DCMA 14-Point Assessment | Medium | 14 checks, each pass/fail]
  - Automated health scoring from imported schedule data is a high-value analytics feature. Not all checks automatable from imported data.

### Standards & Classifications

**Cost & Work Classifications**
- **MasterFormat** (`sc-masterformat`): The 50-division classification system published by CSI/CSC that organizes construction costs and specifications by type of work. The single most important standard for cross-company financial data comparison. [CSI MasterFormat 2018 (50 divisions) | High | Div 02 Existing Conditions, 03 Concrete, 05 Metals, 07 Thermal/Moisture, 08 Openings, 09 Finishes, 2]
  - Cost codes vary wildly between companies — some follow MasterFormat strictly, others use proprietary numbering. The first 2 digits of a MasterFormat code reliably map to building systems.
- **Specification Section** (`sc-specification-se`): A numbered section within a project's technical specifications organized by MasterFormat — defines quality standards, materials, methods, and acceptance criteria for a specific scope of work. [CSI MasterFormat (section numbering) | Medium | Part 1 General (scope, references, submittals), Part 2 Products (materials, manufacturers, standards]
  - Specification sections link to submittals (specification_section_id on submittals table — sparse but high-value) and to RFIs (spec reference in question).
- **Standard Cost Code List** (`sc-std-cost-code`): A company-standard or industry-standard template of cost codes used to set up new projects — ensures consistency across an organization's project portfolio. Companies may maintain multiple lists for different project types. [Company-specific | High | 3-level hierarchies (division.section.subsection), flat code lists, project-type-specific lists]
  - Standard cost code lists are the prerequisite for cross-project financial comparison. Companies without standard lists have inconsistent cost codes across projects — making benchmarking unreliable.
- **WBS Code Structure** (`sc-wbs-code`): Work Breakdown Structure code templates that provide a second dimension of cost classification beyond cost codes — segments costs by phase, location, category, or other company-defined dimension. [PMI PMBOK WBS (§5.4) | Medium | Phase-based (Design, Construction, Closeout), Location-based (Building A, Level 3), Category-based (]
  - WBS 'Rework' and 'Warranty' segments are high-confidence signals for rework cost detection (validated in insight #1). Budget codes serve a similar reporting purpose but are less standardized.
- **Budget Code Structure** (`sc-budget-code`): Company-specific grouping codes applied to budget line items for executive reporting — distinct from cost codes (transactional) and WBS codes (segmentation). [Company-specific | Medium | Structure, Enclosure, MEP, General Conditions, Contingency, Site, Interiors, Overhead, Fee]
  - Budget codes with values like 'Rework' or 'Warranty' are rework cost detection signals (339 cos validated).

**Building & Element Classifications**
- **UniFormat** (`sc-uniformat`): A building element classification system that organizes construction by functional systems rather than by product type — the complement to MasterFormat. [ASTM E1557 (UniFormat) | Low | A Substructure (A10 Foundations, A20 Basement), B Shell (B10 Superstructure, B20 Exterior Enclosure,]
  - UniFormat is the natural classification for the UCDM Building Elements domain. The taxonomy-building-elements.csv categories (Foundations, Structural Frame, Exterior Enclosure, etc.) align with UniFor...
- **OmniClass** (`sc-omniclass`): A comprehensive classification system covering ALL construction entities — buildings, spaces, elements, products, phases, disciplines, and more. [ASTM E2271 (OmniClass) | None | Table 11 Construction Entities, Table 13 Spaces, Table 21 Elements (UniFormat-based), Table 22 Work ]
  - OmniClass is the most comprehensive classification but the least adopted in practice.
- **IFC Classification (buildingSMART)** (`sc-ifc-class`): Industry Foundation Classes — an open data standard for BIM that defines entity types, properties, and relationships for all building elements. [ISO 16739 (IFC) | None | IfcWall, IfcSlab, IfcBeam, IfcColumn, IfcDoor, IfcWindow, IfcDuctSegment, IfcPipeSegment, IfcCableSe]
  - IFC is the bridge between BIM and construction management data. Mapping IFC entities to UCDM building elements enables automated classification of model elements into the taxonomy.

**Safety & Hazard Classifications**
- **OSHA Hazard Categories** (`sc-osha-hazard`): Standardized safety hazard types defined by OSHA for construction — the Focus Four hazards (Fall, Struck By, Electrical, Caught In/Between) plus additional categories. [OSHA 29 CFR 1926 (Construction Safety Standards) | High | Fall Protection, Struck By, Electrical, Caught In/Between, Housekeeping, PPE, Scaffolding, Excavatio]
  - OSHA hazard categories are validated as the primary safety classification in the UCDM (insight #11). hazard_name is 45% null — enrichment opportunity. Recurrence rates range 29–45% by hazard type.
- **OSHA Recordkeeping Classification** (`sc-osha-recordkeepi`): The OSHA system for classifying workplace injuries and illnesses by severity — determines which incidents are 'recordable' and drive TRIR and DART rate calculations. [OSHA 29 CFR 1904 (Recording and Reporting) | Medium | First Aid Only (not recordable), Medical Treatment, Restricted Duty, Days Away, Transfer, Fatality]
  - OSHA recordkeeping classification is the foundation for TRIR and DART metrics. Accurate classification requires trained safety professionals.
- **ANSI Injury Classification** (`sc-ansi-injury`): The ANSI/BLS system for classifying injuries by nature (laceration, fracture, sprain), body part (hand, back, knee), and cause (fall, struck by, overexertion) — provides detailed injury taxonomy for pattern analysis. [ANSI Z16.1 (Injury Classification) | Medium | Nature: laceration, contusion, fracture, sprain/strain, burn. Body part: hand/finger, back, knee, he]
  - Injury classification enables trade-specific prevention: fall-related hand/wrist injuries in steel erection, back injuries in concrete, eye injuries in welding.

**Building Codes & Regulatory**
- **International Building Code (IBC)** (`sc-international-bu`): The model building code adopted (with local amendments) by most US jurisdictions — governs structural design, fire safety, egress, accessibility, and building system requirements. [ICC International Building Code (IBC 2021, 2024) | Low | Construction Type: I-A, I-B, II-A, II-B, III-A, III-B, IV-A through IV-C, V-A, V-B. Occupancy: Assem]
  - IBC construction type directly affects cost — Type I-A (most fire resistant) costs significantly more than Type V-B (least). Occupancy group affects egress, sprinkler, and fire alarm requirements.
- **NFPA Standards** (`sc-nfpa-stds`): National Fire Protection Association standards governing fire protection, life safety, and electrical systems — the technical basis for fire code requirements. [NFPA 13 (Sprinkler Systems), NFPA 72 (Fire Alarm), NFPA 101 (Life Safety Code),  | Low | Sprinkler system design (ordinary/extra hazard), Fire alarm system type (addressable/conventional), ]
  - NFPA standards drive significant cost in fire protection building elements. NFPA 13 sprinkler requirements vary by occupancy and construction type.
- **ADA / Accessibility Standards** (`sc-ada-accessibilit`): Americans with Disabilities Act Accessibility Guidelines (ADAAG) and ICC A117.1 — govern accessible design requirements for public and commercial buildings. [ADA/ADAAG (federal) | Low | Accessible route (36" min clear), Door clearance (32" min), Ramp slope (1:12 max), Accessible restro]
  - Accessibility violations are a common source of punch items and rework — particularly in restrooms, door hardware, and signage.
- **Energy Code Standards** (`sc-energy-code-stds`): Energy conservation codes (IECC, ASHRAE 90.1) and above-code programs — govern building envelope performance, HVAC efficiency, lighting power density, and renewable energy requirements. [IECC (International Energy Conservation Code) | Low | Climate zones 1–8, Envelope U-values, SHGC requirements, Lighting power density (LPD), HVAC efficien]
  - Energy code stringency varies dramatically by jurisdiction (California Title 24 vs. minimum IECC states). Code-driven system requirements affect HVAC, envelope, and lighting building element costs.

**Sustainability & Certification**
- **LEED Certification** (`sc-leed-certificati`): Leadership in Energy and Environmental Design — the most widely recognized green building certification system. [USGBC LEED v4.1 (BD+C, ID+C, O+M) | Low | Certified, Silver, Gold, Platinum]
  - LEED projects require specific documentation that maps to UCDM domains: waste diversion (Field Operations), commissioning (Quality & Safety), material submittals (Documents), energy modeling (Building...
- **WELL Building Standard** (`sc-well-building`): A performance-based standard focused on occupant health and wellness — covers air, water, nourishment, light, fitness, comfort, and mind. Less common than LEED but growing rapidly, especially in commercial office and healthcare. [IWBI WELL Building Standard v2 | None | Silver, Gold, Platinum]
  - WELL is gaining traction in commercial office, healthcare, and education. Requirements overlap with LEED (air quality, materials) but add occupant-focused performance testing.
- **Resilience & Net Zero Standards** (`sc-resilience-net`): Emerging standards for climate resilience (RELi, FORTIFIED) and net-zero energy/carbon performance — increasingly required by institutional owners and government agencies. Resilience standards address flood, wind, seismic, and wildfire hazards. [RELi 2.0 (Resilience) | None | Net Zero Energy, Net Zero Carbon, Net Zero Water]
  - Resilience requirements are jurisdiction-specific (coastal flood zones, hurricane regions, wildfire-urban interface).

**Contract & Delivery Standards**
- **AIA Contract Documents** (`sc-aia-contract`): The American Institute of Architects standard contract document series — the most widely used contract forms in US construction. [AIA A101, A201, A401, B101 (Owner-Architect), G-series (G701, G702, G703, G704,  | Low | A101 Stipulated Sum, A102 Cost Plus Fee, A133 CM at Risk, A141 Design-Build]
  - AIA documents define the workflows modeled in the UCDM — change order flow (G701 → Financial Instruments), pay application flow (G702/G703 → Billing & Payment), substantial completion (G704 → Phases)....
- **Delivery Method Classification** (`sc-dlvy-method`): The taxonomy of project delivery methods that determines how design, construction, and risk are allocated between parties. Each delivery method creates different document flows, change order patterns, and financial instrument relationships. [AIA delivery method documents (A-series) | Low | Design-Bid-Build (traditional), CM at Risk (GMP), Design-Build, Integrated Project Delivery (IPD), M]
  - schedule growth
- **AACE Cost Engineering Standards** (`sc-aace-cost`): The Association for the Advancement of Cost Engineering recommended practices — define cost estimating, scheduling, and project controls methodologies. Key standards: 18R-97 (Cost Estimate Classification), 10S-90 (Cost Engineering), EVMS practices. [AACE International Recommended Practices: 18R-97 (Estimate Classification), 10S- | Low | Estimate Class 1 (definitive, ±5-10%), Class 2 (detailed, ±10-15%), Class 3 (budget, ±15-25%), Class]
  - AACE estimate classes map to project phases — Class 5 at feasibility, Class 1 at IFC. Tracking how estimate accuracy improves through phases benchmarks the estimating process.

**Standard Measures**
- **Cost Code Standardization Rate** (`sc-cost-code`): Percentage of a company's projects using a consistent standard cost code list — measures data readiness for cross-project benchmarking. Formula: Projects with Standard Cost Codes / Total Projects × 100. [Company-specific quality target | High | Target: > 80% standardization]
  - Cost code standardization is the #1 data quality factor for financial benchmarking. Companies with standardized codes can compare costs across projects; those without cannot.
- **MasterFormat Mapping Coverage** (`sc-masterformat-map`): Percentage of a company's cost codes that map to recognized MasterFormat divisions — measures the degree to which company codes can be normalized for cross-company comparison. [CSI MasterFormat mapping conventions | Medium | Target: > 70% of cost codes mappable to MasterFormat divisions]
  - MasterFormat mapping is the bridge from company-specific financial data to UCDM building system cost comparison. standard_cost_code field provides the mapping when populated.
- **Specification Section Coverage** (`sc-specification-se-2`): Percentage of project specification sections entered as structured data vs. remaining as PDF uploads — measures the quality of specification cross-referencing for submittals and RFIs. [CSI section count norms by project type | Medium | Typical project: 50–200 spec sections]
  - Specification section coverage directly affects the quality of submittal-to-spec and RFI-to-spec cross-referencing. Projects with 0 structured sections lose all spec-based analytics.
- **Safety Classification Completeness** (`sc-safety-class`): Percentage of safety observations with a structured hazard_name classification — measures the quality of safety data for OSHA hazard analysis. Formula: Observations with hazard_name / Total Safety Observations × 100. [OSHA hazard category standards | High | Current: 55% populated]
  - Safety classification completeness directly affects the reliability of hazard recurrence analysis (insight #11).
- **WBS Adoption Rate** (`sc-wbs-adoption`): Percentage of projects or companies using WBS codes for cost segmentation — measures the depth of financial data granularity available for building-element-level benchmarking. Formula: Projects with WBS Codes / Total Financial Projects × 100. [PMI WBS methodology adoption | Medium | Varies: some companies use extensively (5+ segments per cost code), others not at all]
  - WBS adoption is the key differentiator for deep financial benchmarking. Companies with WBS codes can track costs at the building-element level within a cost code (e.g., rework vs. original scope).
- **Certification Adoption Rate** (`sc-certification-ad`): Percentage of projects pursuing third-party certification (LEED, WELL, FORTIFIED, etc.) — measures the market penetration of green building and performance standards. Formula: Certified or Pursuing Projects / Total Projects × 100. [USGBC adoption reports | Low | LEED: ~30% of new commercial]
  - Certification adoption is driven by owner requirements — government and institutional owners have higher LEED rates than private developers.

### Workflows & Statuses

**Universal Lifecycle Statuses**
- **Open** (`ws-open`): Record is active and available for action — the entry point for most construction records. Indicates the item has been created and is part of the active workflow. Every record type has some version of 'open' as its initial actionable state. [PMI PMBOK | High | Open, Active, New]
  - Some systems use 'Active' or 'New' instead of 'Open'. UCDM should normalize to 'Open' as the universal starting state.
- **In Progress** (`ws-progress`): Work has begun on the record but is not yet complete. Indicates active effort by a responsible party — distinguishes items being worked on from those sitting idle. Common on tasks, action plans, inspections, and punch items. [PMI PMBOK | High | In Progress, Active, Working]
  - Not all record types use 'In Progress' — RFIs and submittals typically go Submitted → Under Review. Map carefully per record type.
- **Draft** (`ws-draft`): Record exists but has not been formally issued into the workflow. Editable, not yet visible to reviewers or counterparties. The pre-submission holding state where the creator refines before committing. [AIA A201 (document submission protocols) | High | Draft, Preliminary, Not Issued]
  - Draft items should be excluded from cycle time calculations. Only count from submission forward.
- **Closed** (`ws-closed`): Record has completed its lifecycle — no further action required. Terminal state indicating the workflow has run its course, whether resolved successfully or not. Distinct from Void (cancelled) and Approved (decision). [PMI PMBOK | High | Closed, Complete, Resolved, Done]
  - Some systems use 'Complete' or 'Resolved'. Normalize to 'Closed' for lifecycle analysis. Check whether closed items had a resolution or were just abandoned.
- **Void** (`ws-void`): Record has been invalidated or cancelled — the work was never completed, just abandoned. Distinct from Closed (completed lifecycle). Voided records should be excluded from most metrics but tracked as a signal of rework or process waste. [AACE 10S-90 (cost engineering terminology) | High | Void, Cancelled, Withdrawn, Deleted]
  - Voided CEs use mapped_to_status != 'void' filter. Voided CCOs use status = 'Void'. Always exclude from cost aggregations.
- **On Hold** (`ws-hold`): Record is paused, awaiting external input, owner decision, or other blocking condition. Not cancelled — expected to resume. Common when waiting for design clarification, material delivery, or client direction. [PMI PMBOK (risk response: accept) | Medium | On Hold, Suspended, Waiting, Deferred]
  - On Hold is often used inconsistently — some teams use it for 'I don't know what to do with this'. Consider tracking hold reason for meaningful analysis.
- **Overdue** (`ws-overdue`): Record has passed its due date without reaching its expected next state. A computed status based on comparing due_date to current_date and record status. Indicates workflow stall requiring attention. [PMI PMBOK (schedule variance) | High | Overdue, Past Due, Late]
  - Procore has a native 'overdue' boolean on submittals and due_date_variance on RFIs. For other records, overdue must be computed from due_date + status.

**Approval & Review Statuses**
- **Pending** (`ws-pending`): Awaiting action from the next responsible party. The record has entered the workflow but the reviewer has not yet begun evaluation. Pre-action holding state that starts the response time clock. [AIA A201 (submittal review) | High | Pending, Awaiting Review, Queued]
  - Pending vs. Submitted distinction matters: Pending = in queue but not picked up. Submitted = formally sent. Some systems conflate these.
- **Submitted** (`ws-submitted`): Formally sent to the reviewer or approver — the official handoff point. Clock starts on contractual response time. The creator has completed their work and is waiting for a decision. [AIA A201 (submittal procedures) | High | Submitted, Issued, Sent for Review]
  - Track submitted_date as the official workflow start for cycle time calculations.
- **Under Review** (`ws-under-review`): Actively being evaluated by the responsible party. Between submitted and decision. Some systems track this explicitly, others infer it from ball-in-court assignment. [AIA A201 | Medium | Under Review, In Review, Being Reviewed]
  - Not universally tracked as a distinct status. Many systems jump from Submitted → Approved/Rejected without explicit review state.
- **Approved** (`ws-approved`): Accepted without conditions — authorizes the associated work, cost, or material to proceed. The positive terminal decision in an approval workflow. On financial records, triggers commitment of funds. [AIA A201 | High | Approved, Accepted, Authorized]
  - CCOs are 96.7% approved in Procore — rejection is rare once a CCO is created. CEs have more status variety.
- **Approved as Noted** (`ws-approved-as`): Accepted with conditions, corrections, or minor modifications. Common on submittals — fabrication may proceed but noted changes must be incorporated. The 'yes, but' decision that avoids full rejection. [AIA A201 (submittal review actions) | High | Approved as Noted, Approved with Comments, Conditional Approval]
  - Approved as Noted should be counted as approved for throughput metrics but flagged for quality metrics — it signals rework potential.
- **Rejected** (`ws-rejected`): Not accepted — requires rework before resubmission. A hard stop that sends the record back to the originator. Resets the workflow cycle. Should always include rejection reason for tracking. [AIA A201 | High | Rejected, Not Approved, Returned, Denied]
  - Rejection reason is critical for root cause analysis but often unstructured free text. Cross-reference with spec section for pattern detection.
- **Revise and Resubmit** (`ws-revise-resubmit`): Similar to rejected but with specific revision guidance — the reviewer has identified what needs to change. Softer than rejection, implies the approach is correct but execution needs refinement. Common on submittals. [AIA A201 (submittal actions) | High | Revise and Resubmit, Revise & Resubmit, Resubmit]
  - Track revision count per submittal. More than 2 cycles signals a breakdown in pre-submission coordination.

**Field Disposition Statuses**
- **Ready for Review** (`ws-ready-review`): Field work is complete and awaiting quality inspection, superintendent sign-off, or third-party verification. The handoff point between field crews and quality/management teams. [ISO 19650 (information handover) | Medium | Ready for Review, Ready for Inspection, Complete — Pending QC]
  - In Procore, this maps to specific workflow_status values on punch items. Not all record types have this state.
- **Conforming** (`ws-conforming`): Inspection item meets the specified requirements — pass disposition. The field evaluator has verified the work complies with plans, specs, or standards. Moves the item toward closure. [ISO 9001 (conformity assessment) | High | Conforming, Pass, Satisfactory, Meets Requirements]
  - In Procore, inspection_items.status values are capitalized: 'Conforming' (not 'conforming'). Deficiency rate across all inspections is typically 2-6%.
- **Deficient** (`ws-deficient`): Inspection item fails to meet requirements — requires corrective action. A formal finding that the installed work does not comply with plans, specifications, or applicable codes. Triggers rework cycle. [ISO 9001 | High | Deficient, Fail, Non-Conforming, Does Not Meet Requirements]
  - In Procore, 'Deficient' (capitalized). Track deficiency-to-resolution cycle time. Also see observation.type_name for severity classification.
- **Not Applicable** (`ws-not-applicable`): Record or inspection item does not apply in this context — excluded from evaluation. Used when an inspection checklist item is irrelevant to the specific work being inspected. [ISO 9001 (scope exclusion) | High | Not Applicable, N/A, Excluded, Not Inspected]
  - 'Not Applicable' and 'Uninspected' are distinct in Procore. N/A = doesn't apply. Uninspected = applies but wasn't checked. 'Neutral' also exists as a non-disposition.

**Workflow Components**
- **Workflow Step** (`ws-workflow-step`): An individual stage in a multi-step approval or review process. Defines who must act, what action is required, and the sequence position. The atomic unit of workflow configuration. [PMI PMBOK (process groups) | Medium | Step 1: PM Review → Step 2: Architect Review → Step 3: Owner Approval]
  - Procore has *_workflow_steps tables for budget changes, commitments, COs, owner/sub invoices. Most are NOT ready (N) in gold layer except owner_invoice.
- **Approval Chain** (`ws-appr-chain`): Ordered sequence of reviewers and approvers that a record must pass through before reaching a terminal state. Defines the review hierarchy, required vs. optional reviewers, and fallback rules. [AIA A201 (submittal review requirements) | Medium | Linear chain, parallel reviewers, hybrid (parallel then sequential)]
  - In Procore, submittal_approvers defines the approval chain with sequence and response tracking. Most other record types have simpler single-approver patterns.
- **Ball in Court** (`ws-ball-court`): The party currently responsible for taking the next action on a record. Construction-specific accountability term — at any moment, someone 'has the ball'. Changes as the record moves through workflow steps. [AGC (project management practices) | High | Architect, GC PM, Subcontractor, Owner, Engineer]
  - In Procore, BIC is tracked via dedicated tables (rfis_bic, submittal_ball_in_courts) and inline fields. DocuSign overlay adds docusign_ball_in_court_status.
- **Distribution List** (`ws-dist-list`): Set of parties notified when a record is created, changes status, or receives a response. Ensures relevant stakeholders stay informed without being in the approval chain. Notification, not action. [AIA A201 (distribution requirements) | High | PM, Superintendent, Owner Rep, Architect, Sub Foreman]
  - Distribution groups can be configured at company level (reusable) or project level (custom). Both table types exist in Procore.
- **Workflow Response** (`ws-workflow-respons`): A reviewer's formal action at a workflow step — approve, reject, forward, return, or comment. The decision record that advances (or returns) the workflow. Timestamped for cycle time calculation. [PMI | Medium | Approve, Reject, Forward, Return, Comment, No Response Required]
  - Procore has *_workflow_responses tables for budget changes, commitments, COs, invoices. Most NOT ready in gold layer except owner_invoice.
- **Due Date** (`ws-due-date`): The date by which action must be completed on a record or workflow step. Contractually significant — missed due dates can trigger liquidated damages, delay claims, or escalation. [AIA A201 (response time requirements) | High | 7-day RFI response, 14-day submittal review, 30-day CO approval]
  - RFI due_date_variance and submittal overdue flag are native Procore fields. For other records, compare due_date to action_date.
- **Response Time** (`ws-response-time`): The elapsed time between submission and response — either the contractual allowance or the actual measured duration. Critical for project pacing — slow responses cascade into schedule delays. [AIA A201 (14-day default) | Medium | 7 days (RFI), 14 days (submittal), 21 days (complex submittal), 30 days (CO)]
  - Must be computed: response_date - submitted_date. Filter out weekends/holidays for business days. Cross-reference with contract-specified allowances.
- **Escalation** (`ws-escalation`): Elevation of a stalled workflow item to a higher authority when the responsible party fails to act within the allowed response time. The safety valve for stuck workflows. [PMI PMBOK (issue escalation) | None | Auto-escalate after 7 days, notify PM after 3 days, alert exec after 14 days]
  - Procore does not have native escalation. This is a gap — most enterprise PM systems include configurable escalation rules.
- **Delegation** (`ws-delegation`): Temporary or permanent transfer of approval authority from one party to another. Required when the primary reviewer is unavailable — prevents workflow stalls during vacations, role changes, or emergencies. [PMI PMBOK | None | Out-of-office delegation, role-based delegation, proxy approval]
  - Procore lacks formal delegation. Teams work around this by manually changing BIC or having admins act on behalf of others.

**Workflow Patterns**
- **Sequential Approval** (`ws-sequential-appr`): Approvers review in a defined order — each must act before the next receives the item. Ensures layered review (PM → Architect → Owner). Most formal and slowest pattern. [AIA A201 (review sequence) | Medium | Budget change: PM → Controller → Exec. CO: PM → Owner.]
  - In Procore, sequential approval is configured per record type. The number of steps varies by company configuration.
- **Parallel Review** (`ws-parallel-review`): Multiple reviewers evaluate simultaneously — all must respond before the workflow advances. Faster than sequential but requires all parties to be available. Common on design submittals with multiple discipline reviewers. [AIA A201 (simultaneous review) | Medium | Structural + MEP + Architectural review on shop drawings]
  - submittal_approvers tracks individual reviewer responses. Parallel patterns can be inferred when multiple approvers have the same sequence position.
- **Submit and Approve** (`ws-submit-approve`): Single submission followed by one or more approval decisions. The simplest and most common construction workflow pattern — the creator sends, the reviewer decides. [AIA A201 | High | Submittal → Approved. CO → Approved. Invoice → Paid.]
  - This is the default pattern. More complex patterns (sequential, parallel) are variations on this base.
- **Review and Respond** (`ws-review-respond`): A question or information request requiring a formal written response. The RFI pattern — question asked, answer provided, response becomes part of the project record. Response may have cost/schedule impact. [AIA A201 (RFI procedures) | High | RFI: Question → Response → Closed. Correspondence: Sent → Replied → Archived.]
  - RFIs are the most structured Review & Respond implementation. Correspondences follow a similar pattern with less structure.
- **Inspect and Disposition** (`ws-inspect-disposit`): Field evaluation of installed work against defined criteria, resulting in a conforming/deficient judgment. The quality assurance pattern — inspector walks the work, checks each item, renders a disposition. [ISO 9001 | High | Inspection: Uninspected → Conforming/Deficient. Observation: Open → Closed.]
  - The inspect-and-disposition pattern generates the richest quality signal when combined with keyword analysis on item names.
- **Create and Close** (`ws-create-close`): Simplest lifecycle: an item is created, worked on, and closed. No formal approval chain — the responsible party resolves and closes. The punch list and field finding pattern. [AIA A201 (punch list procedures) | High | Punch: Open → In Progress → Closed. Observation: Open → Ready for Review → Closed.]
  - Simple but high-volume. Punch items (~22.3M records) and observations (~1.3M) generate massive workflow data for benchmarking.
- **Multi-Stage Financial Review** (`ws-multi-stage`): A change progresses through independent budget, cost, and revenue stages — each with its own approval status. The change management pattern where a single event triggers parallel financial workflows across different ledgers. [AACE 10S-90 | High | Budget stage: Open → Approved → Closed. Cost stage: Pending → Approved. Revenue stage: Active → Comp]
  - Three independent stage statuses on each CE line item. Some stages may be skipped (e.g., no revenue stage if not billing T&M).

**Financial Workflow Stages**
- **Budget Stage** (`ws-budget-stage`): The budget approval phase of a change event — tracks whether the budget impact has been formally recognized and approved. First stage in the three-stage financial workflow. Controls whether the project budget is adjusted. [AACE 10S-90 | High | Open, Approved, Closed]
  - budget_stage_in_status_since tracks dwell time. Budget stage can be approved while cost/revenue stages remain pending.
- **Cost Stage** (`ws-cost-stage`): The cost commitment phase of a change — tracks whether costs have been formally committed to subcontractors or vendors via change orders. Second stage. Controls whether the commitment is updated. [AACE 10S-90 | High | Pending, Approved, Rejected]
  - cost_stage_in_status_since tracks dwell time. The CE→CPCO→CCO chain is the Procore path from cost stage to executed change order.
- **Revenue Stage** (`ws-revenue-stage`): The owner billing phase of a change — tracks whether the approved change has been incorporated into owner invoicing. Third and final stage. Controls whether the GC bills the owner for the change. [AACE 10S-90 | High | Active, Complete]
  - revenue_stage_in_status_since tracks dwell time. Not all changes have a revenue component (e.g., backcharges deducted, not billed).
- **Change Event Lifecycle** (`ws-chg-event`): The end-to-end progression of a change from identification through budget recognition, cost commitment, and revenue billing. The composite view across all three financial stages for a single change event. [AACE 10S-90 | High | Identified → Budget Approved → Cost Committed → Revenue Billed → Closed]
  - mapped_to_status normalizes domain-specific statuses for cross-record comparison. Use mapped_to_status != 'void' to exclude voided changes.
- **Mapped Status** (`ws-mapped-status`): A standardized status field that normalizes domain-specific statuses into a common vocabulary for cross-record comparison. Allows consistent filtering and aggregation across record types that use different status taxonomies. [Internal normalization (not an industry standard) | Medium | Open, Pending, Approved, Closed, Void]
  - Procore-specific normalization field. Other systems achieve this through status mapping configurations. Essential for UCDM analytics that span record types.

**Electronic Signature Workflows**
- **E-Signature Request** (`ws-e-signature-req`): A digital signing request sent through an integrated e-signature platform (e.g., DocuSign). Overlays the standard approval workflow — the record's internal status and the e-signature status track independently. [ESIGN Act | Medium | Sent, Delivered, Viewed, Signed, Completed, Declined, Voided]
  - docusign_status tracks the e-sign lifecycle independently from the record's approval status. Both must be 'complete' for full execution.
- **E-Signature Ball in Court** (`ws-e-signature-ball`): The signer currently expected to act on a digital signature request. Mirrors the construction ball-in-court concept within the e-signature workflow — identifies who is holding up execution. [ESIGN Act | Medium | Sent (awaiting view), Delivered (viewed, not signed), Completed (signed)]
  - Separate from the main BIC tracking. A record can have ball-in-court with an architect for review while simultaneously having e-signature BIC with an owner for execution.

**Standard Measures**
- **Average Approval Cycle Time** (`ws-average-appr`): Mean elapsed time from formal submission to final approval decision. The primary workflow efficiency metric. Formula: AVG(approval_date - submitted_date) in business days. Segment by record type, reviewer, and project phase. [PMI PMBOK (schedule performance) | High | RFIs: 7-14 days. Submittals: 14-21 days. COs: 14-30 days.]
  - Exclude Draft and Void records. Use business days (exclude weekends). Filter by ball-in-court party for accountability attribution.
- **Overdue Rate** (`ws-overdue-rate`): Percentage of records that exceed their due date before reaching the expected next state. Formula: COUNT(overdue_records) / COUNT(records_with_due_dates). Segment by record type and responsible party. [PMI PMBOK (schedule variance) | High | RFIs: 10-25% overdue typical. Submittals: 15-30% overdue typical.]
  - Use native overdue boolean on submittals. For RFIs, use due_date_variance > 0. For other records, compute from due_date vs. status transition date.
- **First-Pass Approval Rate** (`ws-first-pass-appr`): Percentage of submissions approved on first review without requiring revision or resubmission. Formula: COUNT(approved_first_pass) / COUNT(total_submissions). Higher rate = better pre-submission quality. [ISO 9001 (first-pass yield) | Medium | Submittals: 60-80% first-pass typical. COs: 85-95%.]
  - Requires identifying the first submission vs. resubmissions. On submittals, revision number tracks this. On other records, may need to count status transitions.
- **Resubmission Rate** (`ws-resubmission-rat`): Percentage of submissions that are rejected or returned for revision before eventual approval. Formula: COUNT(rejected_or_returned) / COUNT(total_submissions). The inverse complement of first-pass approval. [ISO 9001 | Medium | Submittals: 20-40% resubmission typical. High-complexity: 30-50%.]
  - Track not just rate but resubmission count per item. 1 resubmission = normal. 3+ = systemic coordination failure. Cross-reference with CSI division.
- **Ball-in-Court Aging** (`ws-ball-court-aging`): Average time a record sits with the current responsible party before action is taken. Formula: AVG(current_date - bic_assignment_date) for active records. Identifies the slowest link in the workflow chain. [PMI PMBOK | High | Architect: 5-10 days avg. GC PM: 2-5 days avg. Owner: 7-14 days avg.]
  - Compute from BIC assignment timestamp to response/transition timestamp. Current active BIC aging = current_date - last_bic_change.
- **Status Dwell Time** (`ws-status-dwell`): Average time a record spends in each status before transitioning to the next state. Identifies which statuses are bottlenecks in the workflow. Formula: AVG(next_status_date - current_status_date) per status. [PMI PMBOK (process efficiency) | Medium | Draft: 2-5 days. Pending: 3-7 days. Under Review: 5-14 days.]
  - Financial records have *_in_status_since columns (e.g., budget_stage_in_status_since). Other records require changelog analysis.
- **Workflow Completion Rate** (`ws-workflow-complet`): Percentage of records that reach a terminal state (Closed, Approved, Complete) vs. remaining active or stalled. Formula: COUNT(terminal_status) / COUNT(total_created) over a time period. [PMI PMBOK (project closure) | High | Punch items: 85-95% close rate. RFIs: 90-98%. Submittals: 80-90%.]
  - Filter by creation date cohort to track completion curves over time. Exclude Void from numerator but include in denominator.
- **Escalation Rate** (`ws-escalation-rate`): Percentage of workflow items that require elevation to a higher authority because the assigned party failed to act within the allowed time. Formula: COUNT(escalated) / COUNT(total_actionable). Higher rate = more workflow friction. [PMI PMBOK (issue escalation) | None | 5-15% escalation rate typical on well-run projects. >25% signals systemic problems.]
  - Since Procore lacks native escalation, approximate by identifying BIC reassignments that occur after the due date has passed.

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
