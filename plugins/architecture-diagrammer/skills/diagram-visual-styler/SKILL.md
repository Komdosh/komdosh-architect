---
name: diagram-visual-styler
description: Apply simple, readable, high-contrast diagram styling that works in light and dark themes.
---

# Diagram Visual Styler

## Purpose

Make the diagram easy to read, not visually impressive.
Style must support fast comprehension.

## Required Inputs

Before styling, require:

- source text or the source-backed inventory from `$architecture-diagrammer:diagram-boundary-context`
- explicit assumptions that need visual treatment
- requested medium, because Mermaid, DrawIO, and Excalidraw have different style controls
- target artifact path when the user asks to write a file

If the user invokes this skill without source text or a source-backed diagram/inventory, do not style an invented diagram. Ask for the missing source or route the user to `$architecture-diagrammer:architecture-diagrammer`.

## Style Principles

- Use one consistent font family or the renderer default.
- Keep labels short and sentence-case.
- Use strong contrast between text and background.
- Avoid complex gradients, shadows, 3D effects, heavy borders, tiny text, and decorative icons.
- Use color to encode meaning, not decoration.
- Keep the palette small and mixed; do not let the diagram become one hue.
- Keep architecture diagrams practical and review-focused, not marketing-style or decorative.

## Clean Palette

Use plain colors with readable text:

| Meaning | Fill | Stroke | Text |
|---------|------|--------|------|
| Actor or client | `#E0F2FE` sky blue | `#0284C7` | `#0F172A` |
| Domain service | `#DCFCE7` grass green | `#16A34A` | `#052E16` |
| Data store | `#FFEDD5` light orange | `#F97316` | `#431407` |
| Event or queue | `#EDE9FE` light violet | `#7C3AED` | `#2E1065` |
| External system | `#F1F5F9` slate | `#64748B` | `#0F172A` |
| Risk or unresolved assumption | `#FEF3C7` amber | `#D97706` | `#422006` |

## Dark And Light Theme Rules

- Do not rely on transparent fill for important blocks.
- Do not use pure black text on dark backgrounds or pure white text on light fills.
- For DrawIO, set explicit fill, stroke, and font colors.
- For Mermaid, prefer `theme: base` plus explicit `themeVariables` only when the renderer supports it.
- For Excalidraw, use high-contrast strokes and restrained hatching.
- If theme safety conflicts with simplicity, choose fewer colors with stronger labels over more style declarations.

## Label Rules

- Each block label should name the role, not just the technology.
- Add technology in a second line only when it changes the architecture meaning.
- Avoid paragraphs inside nodes.
- Put uncertainty in a note or assumption block, not in every label.

## Output

Return the style key and renderer-specific style declarations needed by the export format.
