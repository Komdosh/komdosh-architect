---
name: integration-surface-inventory
description: Identify integration surfaces, consumers, producers, contract owners, public/internal/partner status, lifecycle, support ownership, and integration risks.
---

# Integration Surface Inventory

## Purpose

List every surface where another actor or system depends on this architecture.
Integration design starts by knowing who consumes what and how painful change will be.

## Required Inputs

Require at least one of:

- service/component design
- external-system landscape
- data flow or contract notes
- existing API or integration inventory

## Surface Types

Consider:

- public APIs
- partner APIs
- internal service APIs
- admin/operator APIs
- events
- webhooks and callbacks
- batch imports and exports
- files and documents
- streams
- manual operational handoffs
- external provider adapters
- SDKs, clients, or generated contracts

## Output

Return:

| Surface | Producer/owner | Consumers | Status | Change risk | Support owner |
|---------|----------------|-----------|--------|-------------|---------------|

Then list:

- public or hard-to-change surfaces
- unstable internal surfaces
- external provider surfaces
- consumer assumptions
- open inventory questions
