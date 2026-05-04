---
name: decision-source-map-diagrammer
description: Create simple source and constraint maps showing where ADRs and decision notes were found, which decisions constrain current work, and where source gaps remain.
---

# Decision Source Map Diagrammer

## Purpose

Visualize where decision context came from.
The diagram should help architects see source coverage, constraints, and gaps.

## Required Inputs

Require:

- searched source list
- relevant ADRs or decision notes
- extracted constraints or current architecture task

## Diagram Types

Use a source map when the goal is:

- local files, related repos, MCP/RAG, memory, and user-provided context

Use a constraint map when the goal is:

- decisions that constrain one architecture task

Use a drift map when the goal is:

- current design points that conflict with accepted decisions

## Diagram Rules

- Label each source with type and confidence.
- Mark confirmed ADRs differently from inferred or memory-derived context.
- Show decision status when known.
- Show source gaps explicitly.
- Do not turn the diagram into a new decision record.

## Output

Return:

- diagram purpose
- source map, constraint map, or drift map
- source-confidence note
- limits for future ADR authoring workflow
