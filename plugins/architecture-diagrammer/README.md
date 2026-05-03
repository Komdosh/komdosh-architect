# Architecture Diagrammer

Architecture Diagrammer is a Codex plugin for diagram-only software architecture work.
It treats diagrams as mirrors of documented text: no invented architecture, no prose rewrite, and no diagram element without source evidence or an explicit assumption.

## Scope Fit

This plugin is useful for architecture documentation, ADRs, service designs, system maps, flow diagrams, and supporting visual artifacts.
It is not a runtime, deployment, validation, or autonomous implementation plugin.

Use it when the requested outcome is:

- a new or improved architecture diagram
- a Mermaid, DrawIO, or Excalidraw artifact
- a diagram-focused review of boundaries, components, flows, and layout
- a visual companion to an authoritative architecture document

Before drawing, the plugin must check that the diagram does not silently expand the requested scope or contradict source-backed architecture constraints such as ownership, source of truth, trust boundaries, idempotent callbacks, downstream projections, and API/event boundaries.

## Skill Grouping

- `$architecture-diagrammer:architecture-diagrammer`: orchestrates the full diagram pass.
- `$architecture-diagrammer:diagram-boundary-context`: finds the diagram scope, boundary, actors, components, stores, and external systems.
- `$architecture-diagrammer:diagram-layout-aligner`: arranges blocks for top-bottom and left-right reading.
- `$architecture-diagrammer:diagram-visual-styler`: keeps styling simple, readable, and theme-safe.
- `$architecture-diagrammer:diagram-connection-manager`: keeps relationships necessary, labeled, and untangled.
- `$architecture-diagrammer:diagram-exporter`: chooses Mermaid, DrawIO, or Excalidraw and writes the requested output.
- `$architecture-diagrammer:diagram-review-gate`: checks the finished diagram against the `SCHEMA` mnemonic.

Use the namespaced skill form above in Codex prompts. The short skill names are directory names, not the guaranteed runtime invocation names.

## Required Inputs

Every skill entrypoint requires source grounding:

- source text, source document path, or a source-backed boundary inventory
- explicit assumptions when scope, ownership, storage, protocol, or transport is undecided
- requested medium when the user needs Mermaid, DrawIO, or Excalidraw
- target artifact path when the user asks to write a file

If a subskill is invoked directly without source text or a source-backed inventory, it must ask for the missing source or route back to `$architecture-diagrammer:architecture-diagrammer`.

## Quality Bar

A good result is source-backed, compact, renderable, and standalone.
It should make the architecture easier to review without replacing the source document.

Reject or revise a diagram when it:

- invents services, stores, queues, protocols, or ownership
- presents deferred, optional, or assumed capabilities as confirmed scope
- treats caches, indexes, analytics, or projections as sources of truth unless the source text says so
- hides trust, ownership, or sync/async boundaries that affect correctness
- produces Mermaid that is likely to break in Markdown preview
- produces malformed DrawIO XML or Excalidraw JSON
- needs a long essay to explain what the diagram means

## Examples

Source-backed examples live under [examples/](examples/):

- source text and inventory
- expected Mermaid output
- expected DrawIO output
- expected Excalidraw output
- expected review-gate output

## SCHEMA Mnemonic

- `S` Scope: one purpose, one audience, one diagram level.
- `C` Components: only necessary actors, systems, services, stores, queues, and external dependencies.
- `H` Hierarchy: clear ownership, context, trust, and abstraction boundaries.
- `E` Edges: directional flows with useful labels and no duplicate or decorative connections.
- `M` Medium: Mermaid for simple text-native diagrams, DrawIO for standard polished diagrams, Excalidraw when explicitly requested.
- `A` Alignment: top-bottom and left-right reading order with compact lanes and minimal crossing.
