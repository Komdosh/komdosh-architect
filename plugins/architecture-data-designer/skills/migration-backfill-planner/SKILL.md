---
name: migration-backfill-planner
description: Frame data migration, coexistence, backfill, reconciliation, cutover, rollback, and historical-data risks without designing implementation scripts.
---

# Migration Backfill Planner

## Purpose

Plan data transition concerns early.
Many architecture designs fail because existing data, backfill, reconciliation, and cutover are treated as implementation details too late.

## Required Inputs

Require at least one of:

- existing system or legacy data notes
- current ownership model
- target data ownership model
- migration requirement

If this is a greenfield system, state that no migration is known and still consider future import/export needs.

## Migration Concerns

Identify:

- source systems and data owners
- target owners
- data quality risks
- historical data needs
- backfill scope
- coexistence period
- dual-write, dual-read, import, export, or reconciliation expectations at a high level
- cutover and rollback concerns
- audit continuity
- privacy/deletion continuity
- support and manual correction needs

## Output

Return:

| Data area | Source | Target owner | Migration concern | Reconciliation need | Cutover risk |
|-----------|--------|--------------|-------------------|---------------------|--------------|

Then list:

- backfill assumptions
- coexistence risks
- rollback concerns
- open migration questions
