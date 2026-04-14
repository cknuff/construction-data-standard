#!/usr/bin/env python3
"""Parse 18 UCDM taxonomy CSVs → domain catalog JSON files in data/domains/"""

import csv
import json
import re
import os
from collections import OrderedDict

BASE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(BASE, 'data', 'domains')
os.makedirs(OUT_DIR, exist_ok=True)

DOMAIN_DEFS = {
    'taxonomy-building-elements':       ('building-elements',       'Building Elements',          '#66bb6a', 'be'),
    'taxonomy-resources':               ('resources',               'Resources',                  '#ce93d8', 'res'),
    'taxonomy-phases':                  ('phases',                  'Phases',                     '#ffb74d', 'ph'),
    'taxonomy-financial-instruments':   ('financial-instruments',   'Financial Instruments',      '#ef5350', 'fi'),
    'taxonomy-organizations':           ('organizations',           'Organizations',              '#42a5f5', 'org'),
    'taxonomy-roles':                   ('roles',                   'Roles',                      '#26c6da', 'rl'),
    'taxonomy-locations':               ('locations',               'Locations',                  '#8d6e63', 'loc'),
    'taxonomy-schedule':                ('schedule',                'Schedule',                   '#ff7043', 'sch'),
    'taxonomy-documents-communications':('documents-communications','Documents & Communications', '#5c6bc0', 'doc'),
    'taxonomy-quality-safety-records':  ('quality-safety-records',  'Quality & Safety Records',   '#d4e157', 'qsr'),
    'taxonomy-field-operations':        ('field-operations',        'Field Operations',           '#ffa726', 'fo'),
    'taxonomy-standards-classifications':('standards-classifications','Standards & Classifications','#78909c', 'sc'),
    'taxonomy-permits-regulatory':      ('permits-regulatory',      'Permits & Regulatory',       '#ec407a', 'pr'),
    'taxonomy-contracts-procurement':   ('contracts-procurement',   'Contracts & Procurement',    '#ab47bc', 'cp'),
    'taxonomy-workflows-statuses':      ('workflows-statuses',      'Workflows & Statuses',       '#29b6f6', 'ws'),
    'taxonomy-risk':                    ('risk',                    'Risk',                       '#f44336', 'rk'),
    'taxonomy-models-bim':              ('models-bim',              'Models & BIM',               '#26a69a', 'bim'),
    'taxonomy-project-attributes':      ('project-attributes',      'Project Attributes',         '#9ccc65', 'pa'),
}

# Abbreviation map for shorter IDs
ABBREVS = {
    'and': '', 'the': '', 'for': '', 'with': '',
    'construction': 'const', 'management': 'mgmt', 'professional': 'pro',
    'equipment': 'equip', 'electrical': 'elec', 'mechanical': 'mech',
    'structural': 'struct', 'environmental': 'enviro', 'inspection': 'insp',
    'documentation': 'docs', 'communication': 'comm', 'communications': 'comm',
    'installation': 'install', 'installer': 'inst', 'maintenance': 'maint',
    'certificate': 'cert', 'regulatory': 'reg', 'compliance': 'comp',
    'performance': 'perf', 'verification': 'verif', 'coordination': 'coord',
    'commissioning': 'cx', 'classification': 'class', 'modification': 'mod',
    'modification': 'mod', 'modifications': 'mods', 'improvement': 'improv',
    'improvements': 'improv', 'distribution': 'dist', 'protection': 'prot',
    'fabrication': 'fab', 'procurement': 'procure', 'technology': 'tech',
    'temporary': 'temp', 'utilities': 'util', 'instruments': 'instr',
    'organization': 'org', 'organizations': 'orgs', 'subcontractor': 'sub',
    'contractor': 'contr', 'superintendent': 'super', 'specialist': 'spec',
    'document': 'doc', 'information': 'info', 'request': 'req',
    'approval': 'appr', 'approvals': 'apprs', 'operational': 'ops',
    'operations': 'ops', 'standard': 'std', 'standards': 'stds',
    'materials': 'mat', 'material': 'mat', 'delivery': 'dlvy',
    'general': 'gen', 'conditions': 'cond', 'adjustment': 'adj',
    'potential': 'pot', 'commitment': 'commit', 'change': 'chg',
}


def make_short_id(prefix, name):
    """Generate a compact, readable ID like be-excav, fi-budget, ph-earthwork"""
    slug = re.sub(r'[^a-z0-9\s]+', ' ', name.lower()).strip()
    words = slug.split()
    # Remove filler words and apply abbreviations
    shortened = []
    for w in words:
        if w in ('and', 'the', 'for', 'with', 'a', 'an', 'of', 'in', 'on', 'to', 'by'):
            continue
        shortened.append(ABBREVS.get(w, w))
    # Filter empty strings
    shortened = [w for w in shortened if w]
    # Join with hyphens
    slug = '-'.join(shortened)
    # If still too long, take first 2-3 words max
    if len(slug) > 16:
        slug = '-'.join(shortened[:3])
    if len(slug) > 16:
        slug = '-'.join(shortened[:2])
    if len(slug) > 16:
        slug = slug[:16].rstrip('-')
    return f"{prefix}-{slug}"


def parse_csv(filepath):
    """Parse taxonomy CSV using --- separators as primary category grouping.
    Returns OrderedDict: category_name → [(element_name, description)]
    """
    categories = OrderedDict()
    current_section = "General"  # fallback if no separator before first element

    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cat_field = row.get('Category', '').strip()
            elem = row.get('Element', '').strip()

            # Category separator rows
            if cat_field.startswith('---'):
                m = re.match(r'^---\s*(.+?)(?::\s|---)', cat_field)
                if m:
                    current_section = m.group(1).strip().title()
                continue

            # Regular element row — use the Category column value as the sub-grouping
            if elem:
                # Use the CSV Category column as the category name
                cat_name = cat_field if cat_field else current_section
                if cat_name not in categories:
                    categories[cat_name] = []
                desc = row.get('Description', '').strip()
                categories[cat_name].append((elem, desc[:200] if desc else ''))

    return list(categories.items())


def generate_sub_colors(base_color, count):
    """Generate subtle variations of base color for subcategories"""
    if not base_color.startswith('#') or count == 0:
        return [base_color] * max(count, 1)
    r = int(base_color[1:3], 16)
    g = int(base_color[3:5], 16)
    b = int(base_color[5:7], 16)
    colors = []
    for i in range(count):
        shift = (i * 17) % 60 - 30
        nr = max(0, min(255, r + shift))
        ng = max(0, min(255, g - shift // 2))
        nb = max(0, min(255, b + shift // 3))
        colors.append(f"#{nr:02x}{ng:02x}{nb:02x}")
    return colors


def main():
    total_domains = 0
    total_elements = 0

    for csv_stem, (domain_slug, display_name, color, prefix) in DOMAIN_DEFS.items():
        csv_path = os.path.join(BASE, f"{csv_stem}.csv")
        if not os.path.exists(csv_path):
            print(f"  SKIP: {csv_path} not found")
            continue

        categories = parse_csv(csv_path)
        if not categories:
            print(f"  WARN: No categories found in {csv_stem}")
            continue

        sub_colors = generate_sub_colors(color, len(categories))
        used_ids = set()

        catalog = {
            "domain": domain_slug,
            "name": display_name,
            "color": color,
            "categories": []
        }

        elem_count = 0
        for idx, (cat_name, items) in enumerate(categories):
            cat_obj = {
                "name": cat_name,
                "color": sub_colors[idx] if idx < len(sub_colors) else color,
                "nodes": []
            }
            for elem_name, desc in items:
                short_id = make_short_id(prefix, elem_name)
                base_id = short_id
                counter = 2
                while short_id in used_ids:
                    short_id = f"{base_id}-{counter}"
                    counter += 1
                used_ids.add(short_id)
                cat_obj["nodes"].append({
                    "id": short_id,
                    "name": elem_name
                })
                elem_count += 1
            if cat_obj["nodes"]:
                catalog["categories"].append(cat_obj)

        out_path = os.path.join(OUT_DIR, f"{domain_slug}.json")
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump(catalog, f, indent=2, ensure_ascii=False)

        total_domains += 1
        total_elements += elem_count
        print(f"  {display_name}: {len(catalog['categories'])} cats, {elem_count} elements → {domain_slug}.json")

    print(f"\nDone: {total_domains} domains, {total_elements} total elements")


if __name__ == '__main__':
    main()
