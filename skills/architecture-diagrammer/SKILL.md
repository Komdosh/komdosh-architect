---
name: architecture-diagrammer
description: Create or improve architecture diagrams from documented architecture text. Use when the task is to think only about the diagram view, mirror the source document visually, and make the solution understandable without extra context.
---

# Architecture Diagrammer

## Purpose

Turn documented architecture text into a clear, standalone diagram for review.
The diagram is a mirror of the text, not a new architecture proposal.

Use this skill when the user asks for an architecture diagram, diagram review, Mermaid, DrawIO, Excalidraw, schema visualization, or a diagram-focused agent pass.

## Core Rule

Think only about the diagram view:

- include only architecture facts present in the source text or explicitly marked assumptions
- make the diagram understandable without reading surrounding prose
- keep the visual result compact enough for a developer to understand the solution quickly
- do not rewrite the architecture document unless the user separately asks for document editing

## Software Architecture Scope Fit

Before drawing, verify the diagram against the requested architecture scope:

- source documents, ADRs, tickets, or user-provided text remain authoritative; diagrams are supporting artifacts
- do not imply runnable services, deployments, tests, or infrastructure actions unless that is the requested task
- when a diagram touches release, feature, or capability scope, check the source text before marking something as in scope
- do not present deferred, optional, or assumed capabilities as confirmed unless the source text explicitly says so
- keep explicit assumptions visible when scope, ownership, storage, protocol, or transport is undecided

Do not silently contradict source-backed architecture constraints:

- source-of-truth ownership
- trust, security, or tenancy boundaries
- synchronous versus asynchronous integration semantics
- idempotency-sensitive paths such as retries, callbacks, or external webhooks
- cache, index, projection, analytics, or read-model status
- service boundaries and coupling rules

## Required Inputs

Load the minimum needed context:

- the target text or document
- adjacent README or index only when needed to resolve scope
- architecture defaults, domain scope, ADRs, standards, or constraints only when the diagram could contradict them
- explicit assumptions when source text leaves scope, ownership, storage, protocol, or transport undecided
- requested medium when the user needs a specific output format
- target artifact path when the user asks to write a Mermaid, DrawIO, or Excalidraw file

If a necessary fact is missing, either omit the element or label it as an assumption.

Every subskill in this plugin uses the same source-grounding contract. If a user invokes a subskill directly without source text or a source-backed boundary inventory, that subskill must stop and ask for the missing source or route the user back to `$architecture-diagrammer:architecture-diagrammer`.

## Skill Flow

1. Use `$architecture-diagrammer:diagram-boundary-context` to identify the boundary and component inventory.
2. Use `$architecture-diagrammer:diagram-layout-aligner` to choose the reading axis and block placement.
3. Use `$architecture-diagrammer:diagram-connection-manager` to reduce, label, and route relationships.
4. Use `$architecture-diagrammer:diagram-visual-styler` to apply simple readable styling.
5. Use `$architecture-diagrammer:diagram-exporter` to choose the output format.
6. Use `$architecture-diagrammer:diagram-review-gate` before final delivery, including scope-fit and format-validity checks.

## SCHEMA Mnemonic

Apply `SCHEMA` before exporting:

- `S` Scope: one purpose, one audience, one diagram level.
- `C` Components: all necessary components are on the desk, nothing decorative.
- `H` Hierarchy: ownership, trust, runtime, and abstraction boundaries are visible.
- `E` Edges: connections are directional, labeled, necessary, and not tangled.
- `M` Medium: Mermaid, DrawIO, or Excalidraw fits the requested use case.
- `A` Alignment: the flow reads top-bottom and left-right with consistent spacing.

## Output Contract

Return:

- a one-sentence diagram purpose
- the diagram artifact in the requested format
- a short source-assumption note only when assumptions were needed
- a short scope note when release, phase, or optional/deferred classification affects the diagram
- no long explanatory essay unless the user asks for rationale

## Stop Conditions

Stop and ask when:

- the requested diagram would require inventing source-of-truth ownership or integration decisions
- the user asks to change an accepted decision but only provided diagram instructions
- the source text contains contradictory boundaries that cannot be represented honestly
- the requested view would make a deferred or optional capability look like a confirmed dependency
