#!/usr/bin/env python3
"""Validate all pair edge files: check node IDs exist in domain catalogs, report stats."""

import json
import os
import glob

BASE = os.path.dirname(os.path.abspath(__file__))
DOMAINS_DIR = os.path.join(BASE, 'data', 'domains')
PAIRS_DIR = os.path.join(BASE, 'data', 'pairs')

# Load all domain catalogs and build node ID set
all_node_ids = set()
domain_nodes = {}  # domain_id → set of node IDs

for f in glob.glob(os.path.join(DOMAINS_DIR, '*.json')):
    with open(f) as fh:
        catalog = json.load(fh)
    domain_id = catalog['domain']
    ids = set()
    for cat in catalog['categories']:
        for node in cat['nodes']:
            ids.add(node['id'])
            all_node_ids.add(node['id'])
    domain_nodes[domain_id] = ids

print(f"Loaded {len(domain_nodes)} domain catalogs with {len(all_node_ids)} total node IDs\n")

# Validate each pair file
total_edges = 0
total_verbs = set()
issues = []
pair_stats = []

for f in sorted(glob.glob(os.path.join(PAIRS_DIR, '*.json'))):
    with open(f) as fh:
        try:
            pair = json.load(fh)
        except json.JSONDecodeError as e:
            issues.append(f"  JSON ERROR in {os.path.basename(f)}: {e}")
            continue

    fname = os.path.basename(f).replace('.json', '')
    domains = fname.split('--')
    edges = pair.get('edges', [])
    verbs = set()
    bad_ids = set()
    ontology_verbs = set()

    # Check each edge
    for edge in edges:
        if len(edge) != 3:
            issues.append(f"  {fname}: malformed edge {edge}")
            continue
        src, tgt, verb = edge
        if src not in all_node_ids:
            bad_ids.add(src)
        if tgt not in all_node_ids:
            bad_ids.add(tgt)
        verbs.add(verb)

        # Flag ontology verbs
        if verb.upper() in ('CONTAINS', 'MAPS_TO', 'CLASSIFIED_AS', 'HAS', 'IS_A', 'RELATES_TO', 'LINKED_TO'):
            ontology_verbs.add(verb)

    total_edges += len(edges)
    total_verbs.update(verbs)

    status = "OK"
    if bad_ids:
        status = f"BAD IDs: {', '.join(sorted(bad_ids)[:5])}"
        issues.append(f"  {fname}: {len(bad_ids)} invalid node IDs: {', '.join(sorted(bad_ids)[:10])}")
    if ontology_verbs:
        issues.append(f"  {fname}: ontology verbs detected: {', '.join(ontology_verbs)}")

    pair_stats.append({
        'key': fname,
        'edges': len(edges),
        'verbs': len(verbs),
        'bad_ids': len(bad_ids),
        'status': status
    })

    density = "Dense" if len(edges) >= 60 else "Moderate" if len(edges) >= 20 else "Sparse"
    print(f"  {fname}: {len(edges)} edges, {len(verbs)} verbs [{density}] — {status}")

print(f"\n{'='*60}")
print(f"Total: {len(pair_stats)} pairs, {total_edges} edges, {len(total_verbs)} unique verbs")

if issues:
    print(f"\nIssues ({len(issues)}):")
    for issue in issues:
        print(issue)
else:
    print("\nNo issues found!")

# Regenerate index.json
index_data = {
    "pairs": [
        {"key": p['key'], "edges": p['edges'], "verbs": p['verbs']}
        for p in pair_stats
    ]
}
index_path = os.path.join(BASE, 'data', 'index.json')
with open(index_path, 'w') as f:
    json.dump(index_data, f, indent=2)
print(f"\nUpdated data/index.json with {len(pair_stats)} pairs")
