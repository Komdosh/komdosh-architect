---
name: lifecycle-state-modeler
description: Model key domain lifecycles, states, transitions, triggers, guards, terminal states, reversal paths, exception states, and lifecycle ownership for architecture decisions.
---

# Lifecycle State Modeler

## Purpose

Understand how important domain concepts change over time.
Architecture decisions often depend on lifecycle authority, transition rules, and exception states.

## Required Inputs

Require:

- core domain concepts
- known workflows, use cases, or business rules

## Lifecycle Coverage

For each lifecycle-worthy concept, capture:

- initial state
- active states
- waiting or pending states
- failed, blocked, rejected, expired, cancelled, or suspended states
- terminal states
- allowed transitions
- transition triggers
- transition actor or system authority
- guards and preconditions
- reversal, retry, compensation, or correction paths
- audit and history needs

## Output

Return:

| Concept | State | Allowed next states | Trigger | Authority | Guard/invariant |
|---------|-------|---------------------|---------|-----------|-----------------|

Then provide:

- lifecycle narrative for critical concepts
- Mermaid `stateDiagram-v2` when useful
- lifecycle assumptions
- open lifecycle questions
