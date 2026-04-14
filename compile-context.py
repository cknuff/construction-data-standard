#!/usr/bin/env python3
"""Compile the UCDM into a single LLM-consumable context file."""

import json
import csv
from pathlib import Path

UCDM_DIR = Path(__file__).parent
DATA_DIR = UCDM_DIR / "data"
DOMAINS_DIR = DATA_DIR / "domains"
PAIRS_DIR = DATA_DIR / "pairs"
OUTPUT = UCDM_DIR / "construction-data-standard.md"

def read_csv(path):
    """Read a CSV file and return list of dicts."""
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Skip section separator rows (start with ---)
            first_val = list(row.values())[0]
            if first_val and first_val.strip().startswith("---"):
                continue
            # Skip empty rows
            if not any(v.strip() for v in row.values() if v):
                continue
            rows.append(row)
    return rows

def read_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def build_domain_overview():
    """Build domain overview from taxonomy-domains.csv."""
    rows = read_csv(UCDM_DIR / "taxonomy-domains.csv")
    lines = []
    for row in rows:
        name = row.get("Domain", "").strip()
        desc = row.get("Description", "").strip()
        elements = row.get("Elements", "").strip()
        connections = row.get("Connections", "").strip()
        if name:
            lines.append(f"| {name} | {desc} | {connections} |")
    return lines

def build_domain_elements():
    """Build element listings from taxonomy CSVs (richer than JSON) with JSON IDs."""
    sections = []

    # Build an ID lookup from domain JSONs
    id_lookup = {}  # (domain_slug, element_name) -> id
    domain_files = sorted(DOMAINS_DIR.glob("*.json"))
    domain_name_map = {}  # slug -> display name
    for df in domain_files:
        data = read_json(df)
        slug = df.stem
        domain_name_map[slug] = data.get("name", slug)
        for cat in data.get("categories", []):
            for node in cat.get("nodes", []):
                id_lookup[node.get("name", "").lower()] = node.get("id", "")

    # Map CSV filenames to domain slugs
    csv_files = sorted(UCDM_DIR.glob("taxonomy-*.csv"))
    skip = {"taxonomy-domains.csv", "taxonomy-domain-relationships.csv",
            "taxonomy-element-relationships.csv", "taxonomy-data-mapping.csv",
            "taxonomy-system-resource-matrix.csv", "taxonomy-relationships.csv"}

    for cf in csv_files:
        if cf.name in skip:
            continue

        rows = read_csv(cf)
        if not rows:
            continue

        domain_slug = cf.stem.replace("taxonomy-", "")
        domain_name = domain_name_map.get(domain_slug, domain_slug.replace("-", " ").title())

        lines = [f"### {domain_name}"]
        current_category = None

        for row in rows:
            cat = row.get("Category", "").strip()
            elem = row.get("Element", "").strip()
            desc = row.get("Description", "").strip()
            standard = row.get("Industry Standard", "").strip()
            common = row.get("Common Values", "").strip()
            coverage = row.get("Procore Coverage", "").strip()
            benchmark = row.get("Benchmarking Use", "").strip()
            notes = row.get("Notes", "").strip()

            if not elem:
                continue

            if cat and cat != current_category:
                current_category = cat
                lines.append(f"\n**{cat}**")

            # Get element ID from JSON lookup
            eid = id_lookup.get(elem.lower(), "")
            id_str = f" (`{eid}`)" if eid else ""

            # Truncate description to ~250 chars at sentence boundary
            if len(desc) > 250:
                cut = desc[:250].rfind(". ")
                if cut > 100:
                    desc = desc[:cut+1]
                else:
                    desc = desc[:250] + "..."

            entry = f"- **{elem}**{id_str}: {desc}"

            # Add compact metadata on same line
            meta = []
            if standard:
                # Just the standard name, not the full description
                std_short = standard.split(";")[0].strip()[:80]
                meta.append(std_short)
            if coverage:
                cov_short = coverage.split("—")[0].strip()[:30]
                meta.append(cov_short)
            if common:
                cv_short = common.split(";")[0].strip()[:100]
                meta.append(cv_short)
            if meta:
                entry += f" [{' | '.join(meta)}]"

            # Add Notes as compact sub-bullet (analytical context)
            if notes:
                if len(notes) > 200:
                    cut = notes[:200].rfind(". ")
                    if cut > 80:
                        notes = notes[:cut+1]
                    else:
                        notes = notes[:200] + "..."
                entry += f"\n  - {notes}"

            lines.append(entry)

        if lines and len(lines) > 1:
            sections.append("\n".join(lines))

    return sections

def build_taxonomy_detail():
    """Build detailed taxonomy info from CSV files for each domain."""
    sections = []

    # Map domain names to CSV files
    csv_files = sorted(UCDM_DIR.glob("taxonomy-*.csv"))
    skip = {"taxonomy-domains.csv", "taxonomy-domain-relationships.csv",
            "taxonomy-element-relationships.csv", "taxonomy-data-mapping.csv",
            "taxonomy-system-resource-matrix.csv", "taxonomy-relationships.csv"}

    for cf in csv_files:
        if cf.name in skip:
            continue

        rows = read_csv(cf)
        if not rows:
            continue

        # Get domain name from filename
        domain_slug = cf.stem.replace("taxonomy-", "")
        domain_name = domain_slug.replace("-", " ").title()

        lines = []
        current_category = None

        for row in rows:
            cat = row.get("Category", "").strip()
            elem = row.get("Element", "").strip()
            desc = row.get("Description", "").strip()
            standard = row.get("Industry Standard", "").strip()
            coverage = row.get("Procore Coverage", "").strip()
            benchmark = row.get("Benchmarking Use", "").strip()

            if not elem:
                continue

            if cat and cat != current_category:
                current_category = cat
                lines.append(f"\n**{cat}**")

            # Build compact entry
            parts = [f"- **{elem}**: {desc[:200]}{'...' if len(desc) > 200 else ''}"]
            meta = []
            if standard:
                meta.append(f"Standard: {standard[:100]}")
            if coverage:
                meta.append(f"Coverage: {coverage[:60]}")
            if benchmark:
                meta.append(f"Benchmark: {benchmark[:100]}")
            if meta:
                parts.append(f"  - {' | '.join(meta)}")

            lines.append("\n".join(parts))

        if lines:
            sections.append((domain_name, "\n".join(lines)))

    return sections

def build_domain_relationships():
    """Build domain relationship table from CSV."""
    rows = read_csv(UCDM_DIR / "taxonomy-domain-relationships.csv")
    lines = []

    for row in rows:
        src = row.get("Source Domain", "").strip()
        tgt = row.get("Target Domain", "").strip()
        rels = row.get("Primary Relationships", "").strip()
        bridge = row.get("Bridge Elements", "").strip()
        strength = row.get("Connection Strength", "").strip()
        notes = row.get("Notes", "").strip()

        if not src or not tgt:
            continue

        lines.append(f"- **{src} → {tgt}** [{strength}]: {rels}")
        if bridge:
            lines.append(f"  - Bridge: {bridge[:200]}")
        if notes:
            lines.append(f"  - {notes[:200]}")

    return "\n".join(lines)

def build_element_relationships():
    """Build element relationship table from CSV."""
    rows = read_csv(UCDM_DIR / "taxonomy-element-relationships.csv")
    lines = []

    for row in rows:
        src_d = row.get("Source Domain", "").strip()
        src_e = row.get("Source Element", "").strip()
        rel = row.get("Relationship", "").strip()
        tgt_d = row.get("Target Domain", "").strip()
        tgt_e = row.get("Target Element", "").strip()
        card = row.get("Cardinality", "").strip()
        phase = row.get("Lifecycle Phase", "").strip()
        join = row.get("Procore Join Path", "").strip()
        strength = row.get("Strength", "").strip()
        desc = row.get("Description", "").strip()

        if not src_e or not tgt_e:
            continue

        line = f"- {src_d}.{src_e} —[{rel}]→ {tgt_d}.{tgt_e} ({card}, {strength})"
        if join:
            line += f"\n  - Join: `{join}`"
        if desc:
            line += f"\n  - {desc[:200]}"

        lines.append(line)

    return "\n".join(lines)

def build_pair_summary():
    """Build summary of relationship pairs from index.json."""
    index = read_json(DATA_DIR / "index.json")

    # Group by source domain
    pairs_by_source = {}
    for pair in index.get("pairs", []):
        src = pair["source"]
        tgt = pair["target"]
        edges = pair["edges"]
        if src not in pairs_by_source:
            pairs_by_source[src] = []
        pairs_by_source[src].append((tgt, edges))

    lines = []
    total = index.get("totalEdges", 0)
    count = index.get("pairCount", 0)
    lines.append(f"Total: {count} domain pairs, {total} relationship edges\n")

    for src in sorted(pairs_by_source.keys()):
        targets = pairs_by_source[src]
        targets.sort(key=lambda x: -x[1])
        parts = [f"{t} ({e})" for t, e in targets]
        lines.append(f"**{src}**: {', '.join(parts)}")

    return "\n".join(lines)

def build_pair_verbs():
    """Extract verb stems from pair files — grouped by category."""
    all_verbs = set()
    pair_files = sorted(PAIRS_DIR.glob("*.json"))

    for pf in pair_files:
        data = read_json(pf)
        glossary = data.get("verbGlossary", {})
        all_verbs.update(glossary.keys())

    # Group verbs by first word (stem) for compact display
    stems = {}
    for v in sorted(all_verbs):
        parts = v.split()
        stem = parts[0] if parts else v
        if stem not in stems:
            stems[stem] = []
        stems[stem].append(v)

    # Show stems with counts, plus examples for large groups
    lines = [f"Total: {len(all_verbs)} unique relationship verbs across {len(stems)} verb families.\n"]
    lines.append("Key verb families (by frequency):")
    for stem, verbs in sorted(stems.items(), key=lambda x: -len(x[1]))[:50]:
        if len(verbs) > 3:
            examples = ", ".join(verbs[:3])
            lines.append(f"- **{stem}** ({len(verbs)} variants): {examples}, ...")
        elif len(verbs) > 1:
            lines.append(f"- **{stem}** ({len(verbs)}): {', '.join(verbs)}")
        else:
            lines.append(f"- {verbs[0]}")

    return "\n".join(lines)

def main():
    out = []

    # Header
    out.append("# Construction Data Standard")
    out.append("")
    out.append("A unified data model for the construction industry covering 18 domains, 817 elements, and 8,361 relationships. This standard defines the entities, attributes, and connections that describe how construction projects are planned, executed, and tracked.")
    out.append("")

    # Domain overview
    out.append("## Domains Overview")
    out.append("")
    out.append("| Domain | Description | Connections |")
    out.append("|--------|-------------|-------------|")
    for line in build_domain_overview():
        out.append(line)
    out.append("")

    # Elements by domain (from JSON - more structured)
    out.append("## Domain Elements")
    out.append("")
    out.append("Each domain contains categorized elements representing the fundamental concepts in construction data.")
    out.append("")
    for section in build_domain_elements():
        out.append(section)
        out.append("")

    # Domain relationships
    out.append("## Domain Relationships")
    out.append("")
    out.append("How domains connect to each other — the primary relationships, bridge elements, and connection strength.")
    out.append("")
    out.append(build_domain_relationships())
    out.append("")

    # Element relationships (the gold — includes join paths)
    out.append("## Element Relationships")
    out.append("")
    out.append("Specific element-to-element connections with cardinality, lifecycle phase, and data join paths.")
    out.append("")
    out.append(build_element_relationships())
    out.append("")

    # Relationship graph summary
    out.append("## Relationship Graph Summary")
    out.append("")
    out.append(build_pair_summary())
    out.append("")

    # Verb glossary (compact)
    out.append("## Relationship Verbs")
    out.append("")
    out.append("The verbs used to describe relationships between elements across domains:")
    out.append("")
    out.append(build_pair_verbs())
    out.append("")

    # Key principles
    out.append("## Key Data Principles")
    out.append("")
    out.append("""### Financial Model
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
""")

    # Write output
    content = "\n".join(out)
    OUTPUT.write_text(content, encoding="utf-8")

    # Stats
    lines_count = content.count("\n")
    chars_count = len(content)
    words_count = len(content.split())
    print(f"Written to: {OUTPUT}")
    print(f"Lines: {lines_count:,}")
    print(f"Characters: {chars_count:,}")
    print(f"Words: {words_count:,}")
    print(f"Estimated tokens: ~{words_count * 4 // 3:,}")

if __name__ == "__main__":
    main()
