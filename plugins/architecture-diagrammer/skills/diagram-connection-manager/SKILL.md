---
name: diagram-connection-manager
description: Manage architecture diagram connections so edges are necessary, directional, labeled, grouped when useful, and routed around blocks without visual clutter.
---

# Diagram Connection Manager

## Purpose

Keep relationships readable.
Connections must explain the solution, not cover the workspace.

## Required Inputs

Before selecting or routing edges, require:

- source text or the source-backed inventory from `$architecture-diagrammer:diagram-boundary-context`
- relationship facts with source evidence, or explicit assumptions when a relationship is undecided
- requested medium when connector anchoring or routing support differs by format
- target artifact path when the user asks to write a file

If the user invokes this skill without source text, a source-backed inventory, or source-backed relationship facts, do not generate edges. Ask for the missing source or route the user to `$architecture-diagrammer:architecture-diagrammer`.

## Edge Selection

Include a connection only when it communicates one of:

- user or system request path
- authoritative write or read dependency
- event publication or consumption
- callback, webhook, or external provider interaction
- ownership activation, state transition, or compensation path
- security, trust, or gateway crossing that changes behavior

Omit redundant edges when a grouped relationship or label communicates the same fact.

## Logical Grouping

Group blocks before drawing edges when several sibling components share the same relationship:

- connect to a named group when the edge applies to every member
- when an edge targets a group, attach it to the group boundary or a named group anchor, not to the first item inside the group
- keep individual edges when one member has a different protocol, direction, trust boundary, or source-of-truth role
- label the group by responsibility, not technology alone
- avoid hiding an exception inside a group; split the group or draw the exception separately
- prefer one group-level edge over repeated parallel edges to the same external system, store, queue, or consumer

Good group-level edges communicate concepts such as:

- one external actor calling several public endpoints through the same API boundary
- several services publishing to one event backbone
- one service updating a set of read models or projections
- several workers consuming one queue or topic family

## Group Boundary Rules

- All grouped items must be visually inside the group border.
- Keep enough inner padding for group title, child labels, child blocks, and internal connections.
- Group borders must not cut through text, child blocks, icons, or connectors.
- If a group-level edge needs a visible attachment point, add a small named boundary anchor such as `Group API`, `Group events`, or `Group boundary`.
- If the format cannot connect cleanly to a group frame, connect to the named boundary anchor instead of silently connecting to the first child.
- Reflow, resize, or split a group when its border becomes too tight to read.

## Connection Rules

Preserve source-backed architecture constraints when the source text touches them:

- use API, message, or event edges for service-to-service behavior unless shared storage is explicitly part of the design
- mark event publication and downstream projection consumption as async
- keep authoritative writes distinct from read models, search indexes, analytics, projections, and caches
- show idempotency-sensitive paths for retries, external callbacks, webhooks, and provider interactions when they affect correctness
- show state-transition triggers when they affect ownership, lifecycle, or downstream behavior
- split the diagram when one edge would hide different protocols, trust boundaries, or source-of-truth responsibilities

## Edge Labels

Use short labels:

- command or action name
- API shape such as `REST`, `WSS`, `gRPC`, or `Webhook`
- event name or event family
- data direction such as `read model`, `projection`, or `audit log`
- scope or condition such as `confirmed`, `deferred`, `optional`, or `fallback` only when it prevents misunderstanding

Avoid labels that repeat node names.

## Endpoint Selection

Choose the semantic endpoint before drawing the connector:

- connect to the exact source and target item named by the relationship, not the nearest visual block
- put the arrowhead on the target item and the tail on the source item
- use a group boundary or named group anchor only when the relationship applies to the whole group
- anchor connectors to the source and target blocks when the output format supports anchored connectors
- never connect to a label, icon, title, empty group interior, or arbitrary first child
- keep bidirectional relationships explicit with two labeled edges unless the source text truly means symmetric exchange
- after layout changes, re-check every connector endpoint because auto-routing can snap to the wrong item

Choose the right connection position on the item:

- attach incoming request or command edges to the side facing the caller lane
- attach outgoing calls, events, or callbacks to the side facing the destination lane
- attach store reads and writes to the side nearest the owning service or data-access path
- attach boundary-crossing edges at the boundary entry point, gateway, adapter, or named anchor
- avoid top or bottom attachment when a left or right side makes the flow direction clearer
- keep parallel edges on separate positions so arrowheads and labels remain distinguishable

Use anchored connectors where possible:

- prefer block-bound anchors or ports over free-floating line endpoints
- preserve connector binding when blocks are moved or resized
- use explicit anchor points only to improve readability, not to change the semantic endpoint
- if a connector cannot be anchored to a group frame, anchor it to a named group boundary node
- if the renderer has no real anchoring, make the edge reference the source and target node IDs directly

## Routing Rules

- Route along the chosen reading axis.
- Keep primary flow straight where possible.
- Route connections around blocks, group frames, and labels; do not let lines pass through nodes.
- Use connector waypoints, elbows, or curved paths when the output format supports them.
- Prefer smooth curves or orthogonal bends over diagonal lines that cut across unrelated blocks.
- Attach edges to the side of a block nearest the source or destination lane.
- Attach group-level edges to the group border or named group anchor.
- Reserve visual gutters between groups for cross-boundary edges.
- Put feedback, retries, and compensation on a secondary lane.
- Do not cross boundaries diagonally when a boundary entry point exists.
- Use one edge per concept, not one edge per implementation detail.
- Use a group-level edge when it removes duplicate parallel connections without changing meaning.
- Split the diagram when crossings become the dominant visual feature.

## Format-Specific Routing

- Mermaid: manual routing, curves, and explicit anchor ports are limited; connect node IDs directly and reduce crossings through grouping, layout direction, shallow subgraphs, and diagram splitting.
- Mermaid: when a group frame cannot be the true endpoint, add a small boundary anchor node inside the subgraph and connect to that anchor node.
- DrawIO: use anchored connectors with source and target cells, then add waypoints and curved or orthogonal routing so lines flow around blocks and group frames.
- DrawIO: attach group-level edges to the group container when possible; otherwise use a named boundary anchor cell inside the group.
- Excalidraw: bind arrow endpoints to the source and target shapes when supported, then use curved arrows and generous spacing for cross-lane relationships.
- Excalidraw: avoid coordinate-only arrows that merely touch or hover near a block when a bound arrow can be used.

## Text And Label Spacing

- Leave enough empty space for every edge label to be readable.
- Do not place connection labels on top of blocks, group borders, icons, or other labels.
- Put labels on the clearest segment of the connection; offset them when the renderer supports it.
- Shorten labels when they make routing cramped.
- If a label needs more detail than fits on the edge, move detail into a nearby note or split the relationship into clearer edges.

## Line Style Guidance

Use line styles only when the exporter supports them clearly:

- solid for synchronous calls
- dashed for async events or callbacks
- dotted for optional, administrative, or diagnostic paths

If the renderer makes line styles hard to read, prefer labels over extra styling.

## Output

Return a relationship list:

| From | To | Label | Sync/Async | Why it is necessary |
|------|----|-------|------------|---------------------|

`From` and `To` may be individual blocks, group boundaries, or named group anchors when the group-level edge is truthful.
Then generate only those edges, attach them to the correct endpoint position, and route them around blocks where the selected format allows it.
