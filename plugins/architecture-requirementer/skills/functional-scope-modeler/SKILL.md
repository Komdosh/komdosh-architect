---
name: functional-scope-modeler
description: Convert product goals into functional software requirements, workflows, data needs, boundaries, integrations, and release scope for architecture handoff.
---

# Functional Scope Modeler

## Purpose

Define what the system must do.
Functional requirements should be complete enough for architecture planning and concrete enough to test or review.

## Required Inputs

Require:

- product goal or goal-discovery output
- known users or actors
- known scope constraints, or explicit assumptions when scope is unknown

## Functional Requirement Areas

Cover the relevant areas:

- user-facing capabilities
- administrative and back-office capabilities
- onboarding, identity, access, and permissions
- core workflows and state transitions
- content, catalog, inventory, transaction, communication, or domain-specific flows
- search, filtering, recommendations, discovery, or navigation
- notifications, messages, exports, reports, or analytics
- configuration, policy, rules, moderation, approvals, and exceptions
- data capture, validation, correction, import, export, and deletion
- integrations, callbacks, webhooks, files, external providers, and third-party systems
- audit, history, traceability, and dispute or support workflows
- failure, cancellation, retry, timeout, compensation, and recovery paths

## Scope Rules

- State in-scope and out-of-scope items explicitly.
- Separate MVP requirements from later expansion when timing matters.
- Mark optional capabilities as `Could`, not `Must`.
- Do not hide a business-critical requirement as a future enhancement.
- Include negative paths and operator workflows when they affect architecture.

## Output

Return:

- actor list
- in-scope and out-of-scope boundaries
- functional requirements table with IDs, priority, description, and validation note
- key workflows with preconditions, trigger, main path, alternate paths, and resulting state
- data and lifecycle requirements
- integration requirements
- unresolved functional questions
