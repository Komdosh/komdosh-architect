---
name: diagram-layout-aligner
description: Align architecture diagram blocks so the flow reads top-bottom and left-right with minimal mental effort.
---

# Diagram Layout Aligner

## Purpose

Arrange blocks so a developer can read the diagram without needing the source text.

## Required Inputs

Before choosing layout, require:

- source text or the source-backed inventory from `$architecture-diagrammer:diagram-boundary-context`
- explicit assumptions that must stay visible in the diagram
- requested medium when Mermaid, DrawIO, or Excalidraw changes layout constraints
- target artifact path when the user asks to write a file

If the user invokes this skill without source text or a source-backed inventory, do not arrange a diagram. Ask for the missing source or route the user to `$architecture-diagrammer:architecture-diagrammer`.

## Reading Direction

Choose one primary reading direction:

- top-bottom for lifecycles, request handling, command processing, pipelines, and step order
- left-right for ownership boundaries, producer-to-consumer flows, actor-to-service interaction, and upstream-to-downstream dependency
- sequence diagram when the key value is call order rather than component structure

Use a secondary direction only for grouped details inside a lane.

## Placement Rules

- Put actors and external callers at the top or left edge.
- Put edge and gateway components before domain services.
- Put authoritative services and stores near the center.
- Put downstream projections, analytics, search, notifications, or consumers to the right or bottom.
- Put external providers at the far right or bottom edge.
- Keep components at the same abstraction level on the same row or lane.
- Prefer 3 to 7 major blocks per view; split the diagram when that limit breaks clarity.

For service or system views, prefer this reading order unless the source text needs another one:

1. actor or external provider
2. edge or gateway boundary
3. owning service or bounded context
4. authoritative store and event publication
5. downstream projection, search, analytics, notification, operational consumer, or external integration

## Alignment Rules

- Use consistent block sizes for comparable components.
- Keep lane titles short and stable.
- Avoid nested groups unless the hierarchy is necessary to understand ownership.
- Keep whitespace intentional: enough room for labels and connector paths, not enough to scatter the diagram.
- Treat connector labels as layout objects, not decoration that can be squeezed in later.
- Do not create decorative frames or empty groups.

## Label Clearance Spacing

Leave deliberate gaps between blocks when a labeled connector needs room to be readable.
Compactness means fast comprehension, not minimum distance between boxes.

- Reserve a clear label corridor between neighboring blocks before exporting.
- Prefer widening a lane, row, or group gutter when the label is source-backed and useful.
- Use tighter spacing only for unlabeled, very short, or obviously adjacent relationships.
- Keep more room around cross-boundary, async, callback, retry, and compensation labels because those labels usually carry architecture meaning.
- For DrawIO and Excalidraw, use explicit coordinates with enough horizontal or vertical distance for the full edge label; do not rely on auto-routing to find space after export.
- For Mermaid, spacing control is limited; reduce label density, group relationships, split the view, or choose DrawIO/Excalidraw when edge-label readability matters more than text-native compactness.
- Do not add fake architecture components just to force spacing. If a renderer requires layout help, use a non-semantic format feature or choose a better medium.

## Mermaid Guidance

- Use `flowchart TB` or `flowchart LR` deliberately.
- Use simple `subgraph` groups for boundaries.
- Avoid deep nested subgraphs when Mermaid rendering becomes fragile.
- Use stable ASCII node IDs and readable labels.
- Use one boundary level per subgraph when possible; prefer separate diagrams over fragile nesting.

## Output

Return the chosen layout direction, lane/group plan, and any split recommendation before export.
