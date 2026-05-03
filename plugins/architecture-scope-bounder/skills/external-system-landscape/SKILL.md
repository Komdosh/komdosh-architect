---
name: external-system-landscape
description: Identify external systems, upstream and downstream dependencies, integration surfaces, ownership, interaction style, data exchange, failure ownership, and boundary assumptions.
---

# External System Landscape

## Purpose

Identify what is outside the system of interest and how the system may integrate with it.
External systems are part of the scope boundary even when they are not designed here.

## Required Inputs

Require:

- system of interest
- known product/domain context
- known integrations, or permission to infer likely external systems as assumptions

## External System Types

Consider:

- identity and access systems
- payment, billing, tax, fraud, or risk providers
- messaging, email, SMS, push, or notification providers
- search, analytics, experimentation, or recommendation platforms
- CRM, ERP, warehouse, catalog, inventory, fulfillment, or logistics systems
- file storage, media processing, document generation, or CDN systems
- regulatory, compliance, audit, KYC, AML, or reporting systems
- partner APIs, marketplaces, public APIs, or webhooks
- legacy systems, migration sources, and operational tools

## Integration Framing

For each external system, identify:

- ownership
- why it is needed
- interaction direction
- likely interaction style such as API, webhook, event, batch, file, or manual operation
- data exchanged at a high level
- consistency expectation
- latency sensitivity
- failure handling ownership
- idempotency, retry, timeout, or compensation needs
- trust and security boundary
- open integration decisions

## Output

Return:

| External system | Owner | Role in scope | Direction | Interaction style | Failure concern | Boundary note |
|-----------------|-------|---------------|-----------|-------------------|-----------------|---------------|

Then list integration assumptions, risks, and open questions.
