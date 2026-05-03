---
name: contract-collaboration-designer
description: Frame high-level public and internal contracts, collaboration styles, command/query/event ownership, sync versus async choices, and interaction responsibilities without detailed API schemas.
---

# Contract Collaboration Designer

## Purpose

Define how structural units collaborate at an architecture level.
Contracts should describe responsibilities and interaction semantics, not final endpoint or message schemas.

## Required Inputs

Require:

- structural units and responsibilities
- use cases or capabilities
- external integration expectations when relevant

## Collaboration Styles

Choose and justify:

- synchronous request/response
- asynchronous event publication
- command handoff
- query/read-model access
- webhook or callback
- batch/file exchange
- manual operational process

## Contract Framing

For each collaboration, identify:

- initiator
- target owner
- business action or fact
- direction
- sync or async expectation
- authoritative owner
- failure expectation
- idempotency or retry expectation
- public versus internal contract status
- consumer impact

## Output

Return:

| From | To | Contract purpose | Style | Sync/Async | Authority | Failure concern |
|------|----|------------------|-------|------------|-----------|-----------------|

Then list:

- public contracts
- internal contracts
- event vocabulary
- command/query responsibilities
- collaboration assumptions
- low-level schema decisions deferred to later workflow
