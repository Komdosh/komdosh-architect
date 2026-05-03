---
name: architecture-data-designer
description: Design data architecture responsibilities from domain and service boundaries, covering ownership, source-of-truth, data boundaries, flows, read models, projections, lifecycle, privacy, migration, contracts, diagrams, assumptions, and handoff readiness.
---

# Architecture Data Designer

## Purpose

Turn service/component boundaries into data architecture responsibilities.
The result must help a system designer understand who owns authoritative data, how data moves, where derived views may exist, and which lifecycle, privacy, retention, audit, and migration concerns shape later storage and integration decisions.

Use this skill when the user asks for data architecture, data ownership, source-of-truth boundaries, data flows, read models, projections, reporting/search/analytics data, privacy/retention, migration/backfill, or data contract framing.

## Core Rule

Design data responsibility, not physical storage:

- define authoritative data ownership explicitly
- distinguish write models, read models, projections, caches, analytics views, and reference data
- identify data boundary candidates from service, domain, lifecycle, and invariant boundaries
- map data flows and freshness expectations
- define duplicated-data and stale-data rules
- capture lifecycle, retention, deletion, privacy, residency, and audit-history needs
- frame migration, backfill, reconciliation, and coexistence concerns
- define data contract ownership and compatibility expectations
- prepare inputs for later storage, API, integration, analytics, and infrastructure workflow plugins

## Required Inputs

Load the minimum needed context:

- service/component design when available
- domain model when available
- requirements and scope-boundary brief when available
- known external systems and data exchanges
- quality attributes that affect data, such as consistency, availability, latency, privacy, audit, retention, deletion, scale, and analytics needs
- existing architecture docs, ADRs, schemas, service docs, or code when the data design must align with a current system

If service design is missing, infer only a conservative first-pass ownership model and label assumptions.
Ask when missing source-of-truth or privacy facts would make the design misleading.

## Skill Flow

1. Use `$architecture-data-designer:data-ownership-bounder` to define authoritative ownership and source-of-truth boundaries.
2. Use `$architecture-data-designer:data-boundary-modeler` to identify write models, read models, derived data, and reference data.
3. Use `$architecture-data-designer:data-flow-mapper` to map data movement, freshness, consistency, and failure expectations.
4. Use `$architecture-data-designer:read-model-projection-planner` to frame projections, search, reporting, analytics, and cache responsibilities.
5. Use `$architecture-data-designer:lifecycle-retention-privacy-planner` to define lifecycle, retention, deletion, privacy, residency, and audit needs.
6. Use `$architecture-data-designer:migration-backfill-planner` to frame migration, backfill, reconciliation, and coexistence.
7. Use `$architecture-data-designer:data-contract-designer` to define data contract ownership and compatibility expectations.
8. Use `$architecture-data-designer:data-diagrammer` to create data ownership or data flow diagrams when useful.
9. Use `$architecture-data-designer:data-review-gate` before final delivery.

## Output Contract

Return a self-contained data-design brief with this structure unless the user asks for another format:

1. Data design purpose
2. Source context
3. Authoritative data ownership
4. Source-of-truth boundaries
5. Data boundary candidates
6. Write models, read models, and derived data
7. Data flows and freshness expectations
8. Consistency and duplication rules
9. Projection, search, reporting, and analytics candidates
10. Lifecycle, retention, deletion, privacy, residency, and audit requirements
11. Migration, backfill, coexistence, and reconciliation concerns
12. Data contract ownership and compatibility
13. Data diagrams
14. Data risks and alternatives
15. Assumptions
16. Open questions
17. Handoff checklist for later architecture steps

## Design Discipline

Do not turn this step into physical storage design:

- do not choose database engines, warehouse products, queue products, or cloud storage services
- do not write table schemas, index plans, collection schemas, or physical partitioning
- do not define final API payloads or event schemas
- do not normalize shared database access as integration
- do not treat analytics, search, caches, or projections as authoritative unless explicitly required

You may state data architecture decisions at the responsibility level:

- this service owns the authoritative lifecycle state
- this projection can be eventually consistent with a stated freshness target
- this reference data is copied from an external owner and must be reconciled
- this PII requires deletion and audit boundaries
- this migration requires backfill and dual-read or reconciliation planning later

## Stop Conditions

Stop and ask when:

- central source-of-truth ownership is unknown
- sensitive data categories are likely but privacy, retention, or deletion expectations are missing
- multiple services need to write the same authoritative data without an explicit reason
- migration from existing data is required but source data ownership is unclear
- the user asks for physical schema design while data ownership is unresolved
