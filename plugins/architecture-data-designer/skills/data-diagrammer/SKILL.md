---
name: data-diagrammer
description: Create architecture-level data ownership maps, data flow diagrams, read-model/projection diagrams, and lifecycle/retention views from source-backed data design notes.
---

# Data Diagrammer

## Purpose

Visualize data ownership and movement.
Diagrams should make source-of-truth, derived data, flows, and lifecycle concerns clear without becoming physical schema diagrams.

## Required Inputs

Require:

- data owners or data boundaries
- data flows or projections
- assumptions that must stay visible
- requested format when the user needs Mermaid, DrawIO, or another output

If data design inputs are missing, route back to `$architecture-data-designer:architecture-data-designer`.

## Diagram Types

Use a data ownership map when the goal is:

- authoritative owners
- derived copies
- external owners
- source-of-truth boundaries

Use a data flow diagram when the goal is:

- direction of data movement
- freshness and consistency expectations
- external systems and projections

Use a lifecycle/retention view when the goal is:

- creation, retention, deletion, audit, and privacy propagation
- sensitive data boundaries
- deletion or anonymization impact

## Diagram Rules

- Keep diagrams architecture-level, not physical schema-level.
- Show authoritative owners distinctly from read models, projections, caches, analytics, and exports.
- Label flows with business data subjects and freshness expectations when known.
- Show external systems outside the system boundary.
- Do not show tables, indexes, partitions, database products, or storage infrastructure.
- Keep diagrams consistent with the written data design.

## Output

Return:

- diagram purpose
- data ownership map, data flow diagram, or lifecycle/retention view
- source-assumption note
- diagram limitations for later architecture steps
