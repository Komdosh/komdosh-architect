---
name: context-landscape-diagrammer
description: Create source-backed context diagrams and system landscape diagrams from a bounded architecture scope, showing actors, the system of interest, external systems, and top-level interactions.
---

# Context Landscape Diagrammer

## Purpose

Visualize the bounded scope.
The diagram should make the system of interest, actors, external systems, and top-level interactions understandable without detailed design.

## Required Inputs

Require:

- system of interest
- actors
- external systems
- high-level interactions or use cases
- assumptions that must stay visible
- requested format when the user needs Mermaid, DrawIO, or another output

If the boundary inventory is missing, route back to `$architecture-scope-bounder:architecture-scope-bounder`.

## Diagram Types

Use a context diagram when the goal is:

- one system of interest
- external actors and external systems around it
- top-level interactions and trust/integration boundaries

Use a system landscape diagram when the goal is:

- several adjacent systems
- ownership groups or domains
- upstream and downstream relationships
- coexistence with legacy, partner, operational, or platform systems

## Diagram Rules

- Put the system of interest at the center.
- Put human actors on the left or top.
- Put external systems around the boundary by ownership or interaction direction.
- Label interactions with short business actions, not implementation details.
- Mark assumptions and unresolved ownership clearly.
- Avoid detailed internal components unless one internal block is necessary to explain the boundary.
- Keep diagrams consistent with the written scope brief.
- Prefer Mermaid for lightweight text-native output and DrawIO for polished stakeholder handoff.

## Mermaid Guidance

- Use `flowchart LR` or `flowchart TB`.
- Use simple ASCII node IDs.
- Use one clear subgraph for the system of interest when helpful.
- Keep external systems outside the subgraph.
- Use labels such as `uses`, `submits`, `notifies`, `syncs`, `exports`, `webhook`, or `batch` when those are known.

## Output

Return:

- diagram purpose
- context diagram
- system landscape diagram when useful
- source-assumption note
- diagram limitations that later architecture plugins should resolve
