---
name: domain-diagrammer
description: Create architecture-level domain diagrams such as concept maps, lifecycle diagrams, and capability maps from source-backed domain modeling notes.
---

# Domain Diagrammer

## Purpose

Visualize the domain shape.
Domain diagrams should help architects reason about concepts, relationships, lifecycles, capabilities, and rules without becoming implementation diagrams.

## Required Inputs

Require:

- glossary or concept list
- relationships or lifecycle facts
- assumptions that must stay visible
- requested format when the user needs Mermaid, DrawIO, or another output

If domain inputs are missing, route back to `$architecture-domain-modeler:architecture-domain-modeler`.

## Diagram Types

Use a concept map when the goal is:

- core domain concepts
- relationships
- source-of-truth candidates
- external concepts
- ambiguous ownership

Use a lifecycle diagram when the goal is:

- states
- transitions
- guards
- terminal states
- exception and recovery paths

Use a capability map when the goal is:

- business capabilities
- commands
- events
- rule clusters
- read concerns

## Diagram Rules

- Keep diagrams architecture-level, not code-level.
- Label relationship meaning, not just association.
- Do not show tables, classes, packages, or infrastructure.
- Mark assumptions or unresolved ownership clearly.
- Keep diagrams consistent with the written domain model.
- Prefer Mermaid for lightweight text-native output and DrawIO for polished handoff.

## Output

Return:

- diagram purpose
- concept map, lifecycle diagram, or capability map
- source-assumption note
- diagram limitations for later architecture steps
