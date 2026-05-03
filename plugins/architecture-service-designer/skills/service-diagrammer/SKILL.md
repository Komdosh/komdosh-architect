---
name: service-diagrammer
description: Create architecture-level service, component, container, and collaboration diagrams from source-backed service design notes without low-level implementation detail.
---

# Service Diagrammer

## Purpose

Visualize the proposed structural design.
Diagrams should show responsibilities, ownership, and collaboration clearly enough for architecture review.

## Required Inputs

Require:

- structural units
- responsibilities
- collaborations
- external systems or adapters when relevant
- assumptions that must stay visible
- requested format when the user needs Mermaid, DrawIO, or another output

If service design inputs are missing, route back to `$architecture-service-designer:architecture-service-designer`.

## Diagram Types

Use a component diagram when the goal is:

- modules or components inside one deployable system
- responsibility boundaries
- internal dependency direction

Use a service/container diagram when the goal is:

- deployable services or major containers
- external systems
- public/internal boundaries
- source-of-truth ownership

Use a collaboration diagram when the goal is:

- command, query, event, or process flow across units
- sync versus async relationships
- adapter and anti-corruption boundaries

## Diagram Rules

- Keep diagrams architecture-level, not code-level.
- Show external systems outside the system boundary.
- Label edges with business interaction meaning.
- Mark sync versus async when it affects correctness.
- Mark source-of-truth owners when it prevents misunderstanding.
- Do not show tables, cloud resources, framework packages, or final API schemas.
- Keep diagrams consistent with the written service design.

## Output

Return:

- diagram purpose
- component, service/container, or collaboration diagram
- source-assumption note
- diagram limitations for later architecture steps
