# Requirements, Scope, and Domain

Use only the sections relevant to the request.

## Requirements

- Establish the outcome, users and stakeholders, success measures, constraints, and non-goals.
- Cover primary, alternate, negative, and recovery workflows; data, integration, access, support, and operational needs; and future change that materially affects today's design.
- Express important quality attributes as scenarios with a trigger, operating condition or load, expected response, and measurable threshold. Avoid words such as “fast,” “secure,” or “reliable” without a testable meaning.
- Give requirements stable identifiers only when traceability will be used. Map each material requirement to validation evidence or an unresolved question.
- Keep requirements separate from solution choices unless a technology or boundary is already a confirmed constraint.

## Scope and context

- Name one system of interest. State what is inside, outside, and adjacent, including ownership at each boundary.
- Include human and non-human actors, privileged/support roles, upstream and downstream systems, and the trust position of each.
- Capture top-level use cases, exceptional paths, information or control flows, and who owns retry, compensation, or manual recovery.
- Surface legacy coexistence, migration, policy ownership, and external constraints when they can move the boundary.

## Domain model

- Resolve ambiguous or overloaded terms before using them as boundaries.
- Identify core concepts, relationships, continuity/identity, ownership candidates, and source-of-truth candidates.
- Model important lifecycles: states, transitions, triggers, guards, terminal states, reversal, expiry, and recovery authority.
- State business rules, policies, invariants, and consistency expectations separately from technical validation.
- Use commands for requested change and events for business facts that occurred. Do not turn the domain model into classes, tables, APIs, or service decomposition.

## Review checks

- No actor, requirement, responsibility, data flow, or exception path is orphaned.
- Every assumption that can change a boundary or quality target is visible with a verification path.
- The proposed scope and domain vocabulary are consistent with current evidence; conflicts are explicit.
