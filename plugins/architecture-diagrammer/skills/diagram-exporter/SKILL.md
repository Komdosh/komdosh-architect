---
name: diagram-exporter
description: "Choose and produce the right architecture diagram export format: Mermaid for simple cases, DrawIO for standard polished diagrams, or Excalidraw when explicitly requested."
---

# Diagram Exporter

## Purpose

Choose the diagram medium that fits the task instead of forcing every diagram into one format.

## Required Inputs

Before choosing or producing an export, require:

- source text or the source-backed inventory from `$architecture-diagrammer:diagram-boundary-context`
- explicit assumptions that must appear in the exported artifact
- requested medium, or enough delivery context to choose Mermaid, DrawIO, or Excalidraw
- target artifact path when the user asks to write a file

If the user invokes this skill without source text or a source-backed inventory, do not export a diagram. Ask for the missing source or route the user to `$architecture-diagrammer:architecture-diagrammer`.

## Format Decision

Use Mermaid when:

- the diagram is simple or medium complexity
- text-native Markdown is the delivery target
- precise manual alignment is not required
- the user needs quick review or version-control friendly output
- the artifact will live in architecture documentation as supporting Markdown

Use DrawIO when:

- the diagram is a standard architecture deliverable
- precise positioning, alignment, theme control, or export to image/PDF matters
- the diagram has many components or boundaries
- dark and light theme readability must be controlled explicitly
- stakeholders need a polished standalone image or PDF after architecture review

Use Excalidraw when:

- the developer explicitly asks for Excalidraw
- a sketch-like collaborative diagram is needed
- hatching, hand-drawn strokes, or quick visual ideation is the desired style

Suggest another format when the requested format would hide important architecture meaning.

## Mermaid Rules

- Emit a renderable fenced `mermaid` block.
- Use simple ASCII IDs and readable labels.
- Prefer `flowchart TB`, `flowchart LR`, `sequenceDiagram`, or `stateDiagram-v2` based on the architecture question.
- Keep style declarations short.
- Avoid renderer-fragile nesting, punctuation-heavy IDs, and edge syntax.
- Quote labels that contain punctuation, slashes, parentheses, arrows, or non-trivial symbols.
- Keep subgraphs shallow; split the diagram when nested boundaries become fragile.
- Do not rely on a diagram theme that only works in one Markdown viewer.

For Markdown files, Mermaid renderability is part of the artifact quality bar.
If a diagram may not render, simplify it before returning it.

## DrawIO Rules

- Prefer explicit fill, stroke, font color, and rounded rectangle settings.
- Keep blocks aligned to a clear grid.
- Space connected blocks far enough apart that edge labels fit between them without touching block borders.
- Use theme-safe colors that work on light and dark backgrounds.
- Group by ownership and boundary, not by decorative sections.
- If asked for a file, produce valid `.drawio` XML.
- For file output, the XML must parse and use a DrawIO-compatible root such as `mxfile` or `mxGraphModel`.
- Edges should reference source and target cells when the relationship endpoint is a block or group anchor.

## Excalidraw Rules

- Use restrained strokes and simple backgrounds.
- Use hatching or roughness only to separate groups or assumptions.
- Keep text readable and avoid hand-written density.
- Leave visible whitespace around arrow labels; increase block spacing before accepting label overlap.
- If asked for a file, produce valid `.excalidraw` JSON.
- For file output, the JSON must parse and include an `elements` array.
- Bind arrows to source and target elements when supported by the format.

## Artifact Validation

Before delivery:

- Mermaid: check that the fenced block uses renderable Mermaid syntax and simplify if the preview is likely to fail.
- DrawIO: parse the XML, confirm a DrawIO-compatible root, and check that connector cells do not point at arbitrary labels when source or target blocks exist.
- Excalidraw: parse the JSON, confirm an `elements` array, and check that arrows use bindings or clearly touch the intended elements.
- For any file artifact, open or render it when the local toolchain supports that without leaving the repository. If only parse validation is possible, say so briefly in the final note.

## Output

Start with:

```text
Format: Mermaid | DrawIO | Excalidraw
Reason: <one sentence>
```

Then provide the artifact.
When editing an existing Markdown file, preserve the surrounding document structure and keep the authoritative prose as the source of truth.
