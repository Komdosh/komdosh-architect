---
name: integration-review-gate
description: Review integration design for API quality, consumer clarity, lifecycle readiness, versioning, resilience, security, supportability, diagram consistency, and stage discipline.
---

# Integration Review Gate

## Purpose

Review integration design before detailed API, schema, and implementation work.
Find unstable contracts, hidden consumers, missing versioning, vague failure semantics, and support gaps.

## Required Inputs

Require:

- integration-design brief or exact diff
- service/data/load context when available
- diagrams when produced

If only an integration brief is provided, review internal coherence and state that source alignment was not verified.

## APIWISE Review

Use `APIWISE`:

| Check | Question |
|-------|----------|
| `A` Audience | Are consumers, producers, owners, and support paths clear? |
| `P` Promise | Is each API or contract promise stable, intentional, and not leaking internals? |
| `I` Interaction | Is sync, async, event, webhook, batch, or file style justified? |
| `W` Workflow failure | Are idempotency, retries, timeouts, ordering, duplicates, and compensation explicit? |
| `I` Interface evolution | Are versioning, compatibility, deprecation, and migration rules defined? |
| `S` Security/support | Are auth, authorization, audit, observability, rate limits, diagnostics, and support ownership covered? |
| `E` Extensibility | Can the interface extend without breaking consumers or freezing unstable concepts? |

Also check:

- diagrams match written contracts
- public/partner/internal boundaries are clear
- detailed schema/code decisions are deferred when appropriate

## Readability Check

Treat readability as part of review quality:

- main ideas and decisions are visible first
- wording is plain and compact
- details support nearby points instead of hiding them
- only important decisions, risks, assumptions, open questions, and next steps are highlighted
- necessary technical terms are explained in place

Mark as Major when professional complexity, long prose, or scattered details make the document hard to use.

## Blockers

Treat these as blockers:

- public or partner API has no lifecycle/versioning policy
- consumer groups are unknown for a hard-to-change contract
- contract exposes unstable internal data or provider language
- idempotency or retry behavior is missing for commands, callbacks, or webhooks
- event semantics are unclear or technical-only
- security, authorization, or data exposure is undefined
- support and observability ownership is missing
- diagrams contradict written contract direction or ownership
- output jumps to final schema/code while contract strategy is unresolved

## Output

Return either:

```text
APIWISE: pass
Integration readiness: pass
```

or:

```text
APIWISE: needs changes
- Blocker/Major/Minor: <issue and fix>
```

When the user asks to improve the integration design, provide the corrected section or full revised integration-design brief.
