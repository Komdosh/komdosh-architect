# Decisions and Review

## Decision discovery

- Search the current repository's code and configuration, then decision records and architecture docs; expand to related repositories, available retrieval tools, and memory only when the scope requires it.
- Search common ADR locations and naming variants. Record source path, status, scope, date when available, and relevance.
- Treat executable code and runtime configuration as evidence of current behavior. Treat accepted ADRs and decision records as intended constraints. Neither silently overrides the other: a mismatch is drift.
- Separate confirmed decisions, observed implementation, inferred implications, memory-derived context, and open questions. Mark potentially stale sources.
- Extract hard constraints, preferred defaults, rejected paths, ownership rules, consequences, assumptions, and revisit triggers.
- Compare the proposed or current design with each applicable decision and report aligned, drifted, superseded, ambiguous, and unimplemented items.
- Do not write, update, supersede, or accept an ADR unless the user asks for that mutation. A temporary note must be clearly non-authoritative.

## Architecture review

- Confirm the implementation or document revision being reviewed and its comparison base when a diff is involved.
- Review actual code and configuration for boundaries, ownership, data flow, coupling, consistency, failures, security, performance, operability, and migration behavior. Comments, docstrings, tickets, and PR prose are context, not proof of behavior.
- Report only concrete findings with severity, source location, triggering condition, and impact. Do not add filler or hypothetical concerns without a plausible path from the evidence.
- Distinguish defects in implementation, drift from a decision, missing decisions, and optional improvements.
- When the request is review-only, do not edit the artifact. When changes are requested, make the smallest coherent correction and verify the affected behavior.

A compact decision brief normally needs context, the decision or observed state, alternatives that actually matter, consequences, status, owners, and revisit triggers—not a fixed template for every case.
