---
name: diagram-review-gate
description: Review an architecture diagram against the SCHEMA mnemonic for standalone comprehension, boundary correctness, layout, styling, connection clarity, and architect-ready presentation quality.
---

# Diagram Review Gate

## Purpose

Review the finished diagram before delivery.
Find diagram problems, not prose problems.

## Required Inputs

Before reviewing, require:

- source text or the source-backed inventory from `$architecture-diagrammer:diagram-boundary-context`
- the diagram artifact or exact diagram diff to review
- explicit assumptions that should appear in the diagram
- requested medium and target artifact path when reviewing a file

If the user invokes this skill without source text or a source-backed inventory, do not judge architecture correctness from the diagram alone. Ask for the missing source or route the user to `$architecture-diagrammer:architecture-diagrammer`.

## SCHEMA Review

Use this gate:

| Check | Question |
|-------|----------|
| `S` Scope | Does the diagram answer one clear architecture question for one audience? |
| `C` Components | Are all necessary components present, and are decorative elements absent? |
| `H` Hierarchy | Are ownership, trust, runtime, and abstraction boundaries visible and not mixed? |
| `E` Edges | Are connections directional, labeled, necessary, and untangled? |
| `M` Medium | Does the chosen format fit the complexity and styling needs? |
| `A` Alignment | Can the diagram be read top-bottom and left-right without backtracking? |

Also run architecture-fit checks:

| Check | Question |
|-------|----------|
| Scope fit | Does the diagram avoid presenting deferred, optional, or assumed capabilities as confirmed? |
| Source truth | Are diagrams supporting the authoritative text rather than replacing or contradicting it? |
| Constraints | Does the diagram preserve source-backed architecture constraints? |
| Format validity | Does the artifact parse and meet the validation rules for Mermaid, DrawIO, or Excalidraw? |

Then run format-specific checks:

| Format | Required checks |
|--------|-----------------|
| Mermaid | Fenced `mermaid` block, simple ASCII IDs, quoted complex labels, shallow subgraphs, and syntax likely to render in Markdown preview. |
| DrawIO | XML parses, root is `mxfile` or `mxGraphModel`, cells have stable IDs, edge cells reference intended source and target blocks or group anchors, and labels remain readable. |
| Excalidraw | JSON parses, `elements` is present, text elements are readable, arrows bind to intended elements when supported, and no malformed element breaks opening the file. |

Open or render the artifact when the local toolchain supports it without leaving the repository. If local validation can only parse the file, report the remaining manual open/render check.

Then run human-presentation checks:

| Check | Question |
|-------|----------|
| Architect-ready | Does the whole diagram look professional enough to show to an architect or stakeholder? |
| Text spacing | Is every node label, group title, and connection label readable with enough whitespace? |
| Group borders | Are all grouped items fully inside their group border with comfortable padding? |
| Group edges | Do group-level connections point to the group boundary or a named group anchor, not to the first child? |
| Endpoint correctness | Does each connector point to the intended item with the arrowhead and attachment side matching the flow? |
| Connector anchoring | Are connectors anchored to blocks, group frames, or named anchors when the format supports it? |
| Label clearance | Do labeled connectors have enough empty space, or should blocks be moved apart before delivery? |
| Visual balance | Does the diagram avoid cramped regions, awkward empty areas, and distracting edge tangles? |

## Readability Check

Treat readability as part of review quality:

- the diagram purpose is visible first
- wording is plain and compact
- labels and notes support nearby diagram elements instead of hiding the main view
- only important decisions, risks, assumptions, open questions, and next steps are highlighted
- necessary technical terms are explained in place

Mark as Major when professional complexity, long notes, or scattered details make the diagram hard to use.

## Findings

Classify issues:

- `Blocker`: the diagram contradicts or invents architecture meaning.
- `Major`: the diagram is hard to understand without source text.
- `Minor`: the diagram is understandable but can be cleaner.

## Fix Bias

When possible, fix the diagram directly.
Do not return a long critique when a small layout, label, or edge change solves the issue.

Treat these as blockers:

- invented source-of-truth ownership, stores, queues, protocols, or service boundaries
- scope expansion hidden inside the diagram
- cross-service database coupling shown as normal integration when the source text does not allow it
- downstream projection, search, analytics, or cache shown as authoritative
- unrenderable Mermaid in a Markdown deliverable
- malformed DrawIO XML or connector cells pointing to the wrong source or target
- malformed Excalidraw JSON or arrows that are not bound to the intended elements when bindings are available
- group-level edge attached to a random child instead of the group boundary or anchor
- connector attached to the wrong item, wrong group member, wrong boundary, or wrong side of the target
- connector drawn as a loose line near a block when the format supports anchoring it to that block
- group border cutting through grouped items, labels, or connectors
- connection labels overlapping or touching blocks, group borders, arrowheads, or other labels
- diagram too cramped, overlapped, or visually unpolished to show to a human reviewer

## Output

Return either:

```text
SCHEMA: pass
Architecture fit: pass
Presentation: pass
```

or:

```text
SCHEMA: needs changes
- Blocker/Major/Minor: <issue and fix>
```

Then provide the corrected diagram when the user asked for an artifact.
