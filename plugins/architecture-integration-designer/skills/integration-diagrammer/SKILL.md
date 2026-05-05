---
name: integration-diagrammer
description: Create architecture-level integration context, sequence, event flow, webhook, batch, and collaboration diagrams from source-backed integration design notes.
---

# Integration Diagrammer

## Purpose

Visualize integration decisions.
Diagrams should clarify consumers, producers, contract direction, interaction style, trust boundaries, and failure semantics without becoming implementation schemas.

## Required Inputs

Require:

- integration surfaces
- consumers and producers
- interaction styles
- assumptions that must stay visible
- requested format when the user needs Mermaid, DrawIO, or another output

If integration inputs are missing, route back to `$architecture-integration-designer:integration-designer`.

## Diagram Types

Use an integration context diagram when the goal is:

- system, consumers, providers, and external systems
- public, partner, internal, and operational boundaries
- trust boundaries

Use a sequence or collaboration diagram when the goal is:

- request, callback, webhook, or command flow
- retries, idempotency, and compensation

Use an event flow diagram when the goal is:

- event producer and consumers
- ordering, replay, dead-letter, or backfill expectations

Use a batch/file diagram when the goal is:

- scheduled exchange
- validation, reconciliation, and reprocessing

## Diagram Rules

- Label edges with contract meaning and interaction style.
- Mark public and partner APIs distinctly from internal contracts.
- Show external systems outside the owned boundary.
- Show idempotency, retry, or versioning notes only when decision-relevant.
- Do not show final schemas, controllers, tables, or framework classes.

## Output

Return:

- diagram purpose
- integration context, sequence, event flow, or batch/file diagram
- source-assumption note
- diagram limitations for later detailed API/schema design
