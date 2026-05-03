---
name: diagram-boundary-context
description: Identify the scope, boundary context, and necessary components before drawing an architecture diagram.
---

# Diagram Boundary Context

## Purpose

Put all necessary components on the desk before layout begins.
This skill decides what belongs in the diagram and what must stay out.

## Required Inputs

Before producing an inventory, require:

- source text, source document path, or user-provided architecture facts
- requested diagram purpose and audience when the source text supports multiple views
- explicit assumptions when scope, ownership, storage, protocol, or transport is undecided
- requested medium when the output format constrains what can be shown
- target artifact path when the user asks to write a diagram file later in the flow

If source text or source-backed facts are missing, do not invent the inventory. Ask for the missing source or route the user to `$architecture-diagrammer:architecture-diagrammer` for the full source-grounded flow.

## Component Inventory

Extract only source-backed elements:

- users, operators, systems, or external actors
- owning service, bounded context, module, or runtime container
- authoritative data stores and non-authoritative caches or projections
- event streams, queues, schedulers, and async consumers
- external providers, callbacks, webhooks, and platform dependencies
- gateways, edge boundaries, trust boundaries, and internal APIs when relevant

When release or capability scope matters, also record whether each capability is confirmed, deferred, optional, or unknown.

## Boundary Rules

Make boundaries visible when they affect understanding:

- domain, feature, or business capability boundary
- service ownership boundary
- trust or security boundary
- synchronous versus asynchronous boundary
- source-of-truth versus projection boundary
- internal versus external system boundary
- confirmed versus deferred or optional scope boundary

## Exclusion Rules

Do not include:

- implementation details that do not affect the solution definition
- observability, CI, deployment, or platform blocks unless they are part of the documented solution
- every table, endpoint, or event when a grouped component communicates the same idea more clearly
- invented stores, queues, services, or protocols
- deferred or optional ideas in a confirmed-scope diagram unless explicitly marked

## Architecture Constraint Checks

Before handing off to layout, check whether the diagram touches any source-backed constraint that must not be contradicted:

- source-of-truth ownership
- tenancy, trust, security, or data-classification boundaries
- authoritative writes versus read models, caches, indexes, projections, or analytics
- sync versus async integration
- idempotency-sensitive callbacks, retries, or external provider interactions
- cross-service coupling rules

## Output

Produce a compact inventory:

| Element | Type | Boundary | Scope | Why it is needed | Source evidence |
|---------|------|----------|-------|------------------|-----------------|

Use this inventory as the source of truth for later diagram steps.
