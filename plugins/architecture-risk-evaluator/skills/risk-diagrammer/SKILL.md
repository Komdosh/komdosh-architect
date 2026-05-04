---
name: risk-diagrammer
description: Create architecture-level risk maps, heat maps, dependency-risk maps, assumption-risk maps, mitigation maps, and readiness diagrams from source-backed risk evaluation.
---

# Risk Diagrammer

## Purpose

Visualize risk when it helps decision making.
Diagrams should show priority, dependency, ownership, validation, or readiness clearly.

## Required Inputs

Require:

- risk register or prioritized risks
- source context or current architecture task
- requested format when the user needs Mermaid, DrawIO, or another output

If risk inputs are missing, route back to `$architecture-risk-evaluator:architecture-risk-evaluator`.

## Diagram Types

Use a risk heat map when the goal is:

- likelihood and impact overview

Use a dependency-risk map when the goal is:

- which components, integrations, data, or deployment areas carry risk

Use an assumption-risk map when the goal is:

- which assumptions need validation

Use a readiness diagram when the goal is:

- go/no-go blockers, conditions, and validation gates

## Diagram Rules

- Label risks with short names and priority.
- Show owners or validation gates only when useful.
- Keep the diagram compact and readable.
- Do not invent new risks not in the risk register.
- Do not turn the diagram into a project plan.

## Output

Return:

- diagram purpose
- risk heat map, dependency-risk map, assumption-risk map, mitigation map, or readiness diagram
- source-assumption note
- limits for later planning or implementation workflow
