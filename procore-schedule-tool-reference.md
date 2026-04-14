# Procore Schedule Tool Reference

Internal reference for Procore's schedule data model — legacy vs. new tool comparison, gap analysis vs. P6, and Procore-specific advantages. This is NOT part of the UCDM taxonomy (which is tool-agnostic). Source system mappings live in `taxonomy-data-mapping.csv`.

## Legacy Tool: schedule_task

The legacy schedule tool imports schedules from P6/MS Project as a read-only mirror. 30+ columns but limited CPM fidelity.

**Key tables:**
- `schedule_task` — Activity data (name, dates, duration, percentage, baseline dates, critical_path boolean, milestone boolean, WBS, resource_name)
- `schedule_task_changes` — Delta tracking (old/new values for start, finish, duration, percentage, name; reason free text; when_at timestamp)
- `schedule_task_requests` — Collaborative update requests (sub/field proposes changes for scheduler approval)
- `schedule_lookahead` + `schedule_lookahead_task` — Look-aheads as first-class entities with their own tasks, assignees, companies

**Legacy limitations:**
- Predecessors stored as comma-separated WBS strings — no relationship type (FS/SS/FF/SF) or lag values
- No float values (total or free)
- No constraint types or constraint dates
- No calendar assignments
- No activity codes or custom fields
- Single resource_name string (no structured resource data)

## New Tool: scheduling_activity / scheduling_relationship / scheduling_type

Full CPM-grade schedule data captured natively.

**Key tables:**
- `scheduling_activity` — Full activity data with float, constraints, calendars, resources, trade assignment
- `scheduling_activity_custom_fields` — Extensible activity code system (replaces P6 activity codes)
- `scheduling_relationship` — Typed dependencies (FS/SS/FF/SF) with lag values
- `scheduling_type` — Schedule metadata (type, data date, baseline linkage via parent_schedule_id)

## Gaps Closed by New Tool (7/7)

| Gap | Legacy | New | Impact |
|-----|--------|-----|--------|
| Relationship types | Comma-separated WBS strings | `dependency_type` (FS/SS/FF/SF) | Enables relationship ratio, logic quality |
| Lag values | None | `lag` + `lag_display_unit` | Enables lag analysis, negative lag detection |
| Float | None | `total_float` | Enables float distribution, critical path analysis |
| Constraints | None | `constraint_type` + `constraint_date` | Enables constraint ratio analysis |
| Calendars | None | `calendar_id` + `calendar_name` | Enables calendar validation |
| Activity codes | None | `category_data` (JSON) + custom_fields | Enables trade/area/phase filtering |
| Resources | Single `resource_name` string | `resource_data` (JSON) + `crew_size` + `vendor_id` | Enables resource and trade-level analysis |

**Result:** DCMA 14-point analysis, float distribution, constraint ratio, logic density, relationship ratio — all from Procore data alone.

## Remaining Gaps vs. P6

| Feature | Status | Notes |
|---------|--------|-------|
| Free float | Missing | Only `total_float` available |
| Late start / late finish | Missing | Only `start_date` / `finish_date` |
| Remaining duration | Derived | Must calculate from `duration` + `percent_done` |
| Multiple named baselines | Uncertain | `parent_schedule_id` may handle this |
| Resource hours / cost | Unknown | `resource_data` JSON structure not inspected |
| Activity steps | Missing | P6 feature for within-activity sequencing |
| Scheduling options | Missing | Retained logic vs. progress override setting |

**TODO:** Databricks queries to inspect `resource_data` JSON structure, `category_data` JSON structure, `scheduling_type.type` enum values, and `parent_schedule_id` baseline modeling.

## Procore-Specific Advantages (vs. P6 / MS Project)

These are things P6 and MS Project cannot do because they're standalone scheduling tools with no field data:

1. **Schedule-to-daily-log linkage** — CPM activities connected to what actually happened on site
2. **Field-initiated schedule updates** — Subs propose changes; scheduler approves/rejects (schedule_task_requests)
3. **Structured change audit** — Every delta timestamped with old/new values and reason (schedule_task_changes)
4. **Look-aheads as first-class entities** — Separate from CPM with their own tasks, assignees, and companies
5. **Trade assignment per activity** — vendor_id/vendor_name directly on scheduling_activity
6. **Cross-tool linkage** — Schedule connected to observations, RFIs, inspections, daily logs

P6 is an island — no native field data. Procore bridges planning to execution. This is the data moat for schedule analytics.
