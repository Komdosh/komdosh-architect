# Architecture Data Designer

Architecture Data Designer is a Codex plugin for the data architecture responsibility step of software architecture work.
It comes after service/component design and before physical storage, detailed schema, API, analytics, and infrastructure design.

## Scope Fit

Use this plugin when the requested outcome is:

- authoritative data ownership by service, component, or module
- source-of-truth boundaries
- data boundary and aggregate/data-cluster candidates
- write model versus read model responsibilities
- duplicated data, reference data, and derived data rules
- data flows between components and external systems
- consistency, freshness, retention, and lifecycle expectations
- projection, reporting, search, and analytics data needs
- audit, history, privacy, deletion, residency, and PII boundaries
- migration, backfill, coexistence, and data contract concerns
- data ownership maps, data flow diagrams, or lifecycle/retention views

This plugin should design data responsibilities, not physical data storage.
It may state architecture implications, but it must not choose database engines, table schemas, index design, warehouse topology, or low-level serialization formats unless the user explicitly asks for a later-stage design.

## Human-Readable Output

Prefer readability over professional complexity.
Outputs should be compact, self-contained, and easy to scan.

- put the main idea or decision first
- use plain words before specialist terms
- highlight only important decisions, risks, assumptions, open questions, and next steps
- keep details close to the point they explain
- avoid long paragraphs and decorative wording
- explain necessary technical terms in place

## Skill Grouping

- `$architecture-data-designer:architecture-data-designer`: orchestrates the full data-design pass.
- `$architecture-data-designer:data-ownership-bounder`: defines authoritative ownership, source-of-truth boundaries, and duplicated-data rules.
- `$architecture-data-designer:data-boundary-modeler`: identifies data boundary candidates, write models, read models, reference data, and derived data.
- `$architecture-data-designer:data-flow-mapper`: maps data movement, direction, freshness, consistency, and failure expectations.
- `$architecture-data-designer:read-model-projection-planner`: frames read models, projections, search, reporting, analytics, and cache responsibilities.
- `$architecture-data-designer:lifecycle-retention-privacy-planner`: defines lifecycle, retention, deletion, privacy, residency, PII, and audit-history expectations.
- `$architecture-data-designer:migration-backfill-planner`: frames migration, coexistence, backfill, reconciliation, and cutover concerns.
- `$architecture-data-designer:data-contract-designer`: frames data contract ownership, compatibility, versioning, and consumer impact.
- `$architecture-data-designer:data-diagrammer`: creates data ownership maps, data flow diagrams, and lifecycle/retention views.
- `$architecture-data-designer:data-review-gate`: reviews the data architecture for ownership clarity and design-stage discipline.

Use the namespaced skill form above in Codex prompts.
The short skill names are directory names, not the guaranteed runtime invocation names.

## Quality Bar

A good output is ownership-explicit, privacy-aware, lifecycle-aware, and ready for later storage and integration design.
It should prevent shared database coupling and unclear source-of-truth responsibilities.

Reject or revise a data design when it:

- hides authoritative ownership of central data
- treats read models, caches, projections, or analytics stores as authoritative by default
- allows shared database access as normal service integration
- omits data retention, deletion, privacy, or audit expectations for sensitive domains
- ignores duplicated, stale, missing, or conflicting data risks
- omits migration or backfill for existing systems
- jumps to physical database schemas or storage products too early

## Required Output Shape

The main output should be a data-design brief with:

- data design purpose and source context
- authoritative data ownership map
- source-of-truth boundaries
- data boundary candidates
- write model and read model responsibilities
- data duplication and reference data rules
- data flows and freshness expectations
- projection, search, reporting, and analytics candidates
- lifecycle, retention, deletion, privacy, residency, and audit requirements
- migration, backfill, reconciliation, and coexistence concerns
- data contract ownership and compatibility expectations
- data diagrams
- assumptions and open questions
- handoff checklist for later architecture workflow steps
