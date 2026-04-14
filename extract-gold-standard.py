#!/usr/bin/env python3
"""Extract gold standard data from construction-execution-force.html into pair JSON files.

Also overwrites the generated domain catalogs for phases, building-elements, resources
with the gold standard's curated IDs and category structure.
"""

import json
import re
import os

BASE = os.path.dirname(os.path.abspath(__file__))
HTML_PATH = os.path.join(BASE, 'construction-execution-force.html')
DOMAINS_DIR = os.path.join(BASE, 'data', 'domains')
PAIRS_DIR = os.path.join(BASE, 'data', 'pairs')

with open(HTML_PATH, 'r') as f:
    html = f.read()

# ── Extract phaseGroups ──
phase_match = re.search(r'const phaseGroups = \[(.*?)\];', html, re.DOTALL)
phase_text = phase_match.group(1)
# Parse: {cat:"name",items:[{id:"...",name:"..."},...]},
phases = []
for cat_match in re.finditer(r'\{cat:"([^"]+)",items:\[(.*?)\]\}', phase_text, re.DOTALL):
    cat_name = cat_match.group(1)
    items = []
    for item_match in re.finditer(r'\{id:"([^"]+)",name:"([^"]+)"\}', cat_match.group(2)):
        items.append({"id": item_match.group(1), "name": item_match.group(2)})
    phases.append({"name": cat_name, "color": "#ffb74d", "nodes": items})

# ── Extract graphNodes ──
nodes_match = re.search(r'const graphNodes = \[(.*?)\];', html, re.DOTALL)
nodes_text = nodes_match.group(1)
# Parse: {id:"...",name:"...",domain:"...",cat:"..."},
all_nodes = []
for m in re.finditer(r'\{id:"([^"]+)",name:"([^"]+)",domain:"([^"]+)",cat:"([^"]+)"\}', nodes_text):
    all_nodes.append({"id": m.group(1), "name": m.group(2), "domain": m.group(3), "cat": m.group(4)})

# Build element groups
element_cats = {}
resource_cats = {}
for n in all_nodes:
    if n["domain"] == "elements":
        element_cats.setdefault(n["cat"], []).append({"id": n["id"], "name": n["name"]})
    elif n["domain"] == "resources":
        resource_cats.setdefault(n["cat"], []).append({"id": n["id"], "name": n["name"]})

# Element category order and colors from gold standard
el_cat_order = ['Site & Earthwork','Foundations','Site Utilities','Structure','Enclosure',
    'Roofing','HVAC','Plumbing','Electrical','Fire Protection','Low Voltage','Interiors',
    'Conveying','Site Improvements']
el_color_map = {cat: '#66bb6a' for cat in el_cat_order}

res_cat_order = ['Trades','Equipment','Materials']
res_color_map = {'Trades': '#ce93d8', 'Equipment': '#4dd0e1', 'Materials': '#ff8a65'}

# ── Extract allEdges ──
edges_match = re.search(r'const allEdges = \[(.*?)\];', html, re.DOTALL)
edges_text = edges_match.group(1)
all_edges = []
for m in re.finditer(r'\["([^"]+)","([^"]+)","([^"]+)"\]', edges_text):
    all_edges.append([m.group(1), m.group(2), m.group(3)])

# ── Build node ID → domain mapping ──
node_domain = {}
for cat in phases:
    for n in cat["nodes"]:
        node_domain[n["id"]] = "phases"
for n in all_nodes:
    if n["domain"] == "elements":
        node_domain[n["id"]] = "building-elements"
    elif n["domain"] == "resources":
        node_domain[n["id"]] = "resources"

# ── Split edges into pairs ──
pair_edges = {}
verb_glossaries = {}
for src, tgt, verb in all_edges:
    src_dom = node_domain.get(src)
    tgt_dom = node_domain.get(tgt)
    if not src_dom or not tgt_dom:
        print(f"  WARN: unknown node {src} or {tgt}")
        continue
    # Canonical pair key: alphabetical order
    pair_key = '--'.join(sorted([src_dom, tgt_dom]))
    pair_edges.setdefault(pair_key, []).append([src, tgt, verb])
    verb_glossaries.setdefault(pair_key, set()).add(verb)

# ── Write pair files ──
os.makedirs(PAIRS_DIR, exist_ok=True)

for pair_key, edges in pair_edges.items():
    doms = pair_key.split('--')
    pair_file = {
        "source": doms[0],
        "target": doms[1],
        "edges": edges,
        "verbGlossary": {v: "" for v in sorted(verb_glossaries[pair_key])}
    }
    out_path = os.path.join(PAIRS_DIR, f"{pair_key}.json")
    with open(out_path, 'w') as f:
        json.dump(pair_file, f, indent=2)
    print(f"  {pair_key}: {len(edges)} edges, {len(pair_file['verbGlossary'])} verbs → {pair_key}.json")

# ── Write gold-standard domain catalogs ──
# Phases
phases_catalog = {
    "domain": "phases",
    "name": "Phases",
    "color": "#ffb74d",
    "categories": phases
}
with open(os.path.join(DOMAINS_DIR, 'phases.json'), 'w') as f:
    json.dump(phases_catalog, f, indent=2)
print(f"  Updated phases.json: {sum(len(c['nodes']) for c in phases)} nodes")

# Building Elements
be_cats = []
for cat_name in el_cat_order:
    if cat_name in element_cats:
        be_cats.append({"name": cat_name, "color": el_color_map[cat_name], "nodes": element_cats[cat_name]})
be_catalog = {
    "domain": "building-elements",
    "name": "Building Elements",
    "color": "#66bb6a",
    "categories": be_cats
}
with open(os.path.join(DOMAINS_DIR, 'building-elements.json'), 'w') as f:
    json.dump(be_catalog, f, indent=2)
print(f"  Updated building-elements.json: {sum(len(c['nodes']) for c in be_cats)} nodes")

# Resources
res_cats = []
for cat_name in res_cat_order:
    if cat_name in resource_cats:
        res_cats.append({"name": cat_name, "color": res_color_map[cat_name], "nodes": resource_cats[cat_name]})
res_catalog = {
    "domain": "resources",
    "name": "Resources",
    "color": "#ce93d8",
    "categories": res_cats
}
with open(os.path.join(DOMAINS_DIR, 'resources.json'), 'w') as f:
    json.dump(res_catalog, f, indent=2)
print(f"  Updated resources.json: {sum(len(c['nodes']) for c in res_cats)} nodes")

print(f"\nTotal: {len(all_edges)} edges split into {len(pair_edges)} pairs")
print(f"Gold standard domain catalogs updated for phases, building-elements, resources")
