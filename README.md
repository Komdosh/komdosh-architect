# Komdosh Architect

<p align="center">
  <strong>Codex plugin marketplace for first-class software architecture design.</strong>
</p>

<p align="center">
  <img alt="Codex marketplace" src="https://img.shields.io/badge/Codex-plugin%20marketplace-111827">
  <img alt="Architecture workflow" src="https://img.shields.io/badge/workflow-architecture%20design-2563EB">
  <img alt="Human readable" src="https://img.shields.io/badge/output-human%20readable-16A34A">
  <img alt="Repository" src="https://img.shields.io/badge/repository-komdosh--architect-475569">
</p>

Komdosh Architect is a marketplace of focused Codex plugins for software architecture work.
Each plugin owns one design stage, keeps the output compact, and produces architecture context that the next stage can safely use.

The goal is simple: make architecture work easier to read, easier to review, and harder to turn into vague all-in-one design documents.

## What You Get

- a staged architecture workflow from product goals to implementation readiness
- focused plugins for requirements, scope, domain, service, data, load, integration, deployment, security, observability, decisions, risks, and diagrams
- compact, self-contained outputs written for humans first
- review gates that catch missing context, unclear decisions, drift, and premature implementation detail
- reusable Codex skill names that can be called directly in prompts

## Recommended Flow

Use the workflow in order when starting from a new product or large feature.
For existing systems, start with `architecture-decision-discoverer` so current ADRs and decision notes are visible before new design work.

| Step | Plugin | Main job |
|------|--------|----------|
| 0 | [`architecture-decision-discoverer`](plugins/architecture-decision-discoverer) | Find ADRs, decision notes, constraints, drift risks, and future ADR questions. |
| 1 | [`architecture-requirementer`](plugins/architecture-requirementer) | Turn product goals into architect-ready functional and non-functional requirements. |
| 2 | [`architecture-scope-bounder`](plugins/architecture-scope-bounder) | Define the system boundary, actors, external systems, and top-level use cases. |
| 3 | [`architecture-domain-modeler`](plugins/architecture-domain-modeler) | Model domain language, concepts, rules, lifecycles, commands, and events. |
| 4 | [`architecture-service-designer`](plugins/architecture-service-designer) | Define service or component responsibilities, ownership, collaboration, and consistency boundaries. |
| 5 | [`architecture-data-designer`](plugins/architecture-data-designer) | Design data ownership, flows, contracts, lifecycle, projections, migration, and privacy expectations. |
| 6 | [`architecture-load-estimator`](plugins/architecture-load-estimator) | Estimate workload, traffic, data growth, bottlenecks, and capacity pressure. |
| 7 | [`architecture-integration-designer`](plugins/architecture-integration-designer) | Design API-first integration contracts, events, webhooks, batch, resilience, and versioning. |
| 8 | [`architecture-deployment-designer`](plugins/architecture-deployment-designer) | Design runtime topology, environments, network boundaries, rollout, reliability, and DR. |
| 9 | [`architecture-security-designer`](plugins/architecture-security-designer) | Design trust boundaries, identity, authorization, data protection, abuse controls, secrets, and audit. |
| 10 | [`architecture-observability-designer`](plugins/architecture-observability-designer) | Design SLIs, SLOs, logs, metrics, traces, dashboards, alerts, diagnostics, and incident support. |
| 11 | [`architecture-risk-evaluator`](plugins/architecture-risk-evaluator) | Prioritize architecture risks, validation work, mitigations, owners, and go/no-go readiness. |
| Any | [`architecture-diagrammer`](plugins/architecture-diagrammer) | Create source-backed architecture diagrams from any stage output. |

## Install

Add the marketplace:

```bash
codex plugin marketplace add https://github.com/Komdosh/komdosh-architect.git
```

Restart Codex after adding or updating the marketplace so the plugin skills are loaded into the session context.

## Enable Plugins

Plugins can be enabled explicitly in `~/.codex/config.toml`:

```toml
[plugins."architecture-diagrammer@komdosh-architect"]
enabled = true

[plugins."architecture-requirementer@komdosh-architect"]
enabled = true

[plugins."architecture-scope-bounder@komdosh-architect"]
enabled = true

[plugins."architecture-domain-modeler@komdosh-architect"]
enabled = true

[plugins."architecture-service-designer@komdosh-architect"]
enabled = true

[plugins."architecture-data-designer@komdosh-architect"]
enabled = true

[plugins."architecture-load-estimator@komdosh-architect"]
enabled = true

[plugins."architecture-integration-designer@komdosh-architect"]
enabled = true

[plugins."architecture-deployment-designer@komdosh-architect"]
enabled = true

[plugins."architecture-security-designer@komdosh-architect"]
enabled = true

[plugins."architecture-observability-designer@komdosh-architect"]
enabled = true

[plugins."architecture-decision-discoverer@komdosh-architect"]
enabled = true

[plugins."architecture-risk-evaluator@komdosh-architect"]
enabled = true
```

## Prompt Examples

```text
Use $architecture-requirementer:architecture-requirementer to prepare architect-ready requirements for this product idea.
```

```text
Use $architecture-decision-discoverer:architecture-decision-discoverer to find ADRs and decision notes that constrain this design.
```

```text
Use $architecture-integration-designer:architecture-integration-designer to design API and integration contracts for this architecture.
```

```text
Use $architecture-risk-evaluator:architecture-risk-evaluator to evaluate implementation readiness and produce a compact risk register.
```

## Output Standard

All plugins must prefer readability over professional complexity.
Architecture documents should be compact, self-contained, and easy to scan.

- put the main idea or decision first
- use plain words before specialist terms
- highlight only important decisions, risks, assumptions, open questions, and next steps
- keep details close to the point they explain
- avoid long paragraphs and decorative wording
- explain necessary technical terms in place

## Plugin Catalog

| Plugin | Focus |
|--------|-------|
| [`architecture-diagrammer`](plugins/architecture-diagrammer) | Source-backed Mermaid, DrawIO, and Excalidraw architecture diagrams. |
| [`architecture-requirementer`](plugins/architecture-requirementer) | Product goals, functional requirements, non-functional requirements, assumptions, and handoff readiness. |
| [`architecture-scope-bounder`](plugins/architecture-scope-bounder) | System boundaries, actors, external systems, use cases, exception paths, and context diagrams. |
| [`architecture-domain-modeler`](plugins/architecture-domain-modeler) | Domain language, concepts, rules, invariants, lifecycles, capabilities, commands, and events. |
| [`architecture-service-designer`](plugins/architecture-service-designer) | Service candidates, responsibility boundaries, collaboration, consistency, dependencies, and adapters. |
| [`architecture-data-designer`](plugins/architecture-data-designer) | Data ownership, boundaries, flows, contracts, read models, retention, privacy, and migration planning. |
| [`architecture-load-estimator`](plugins/architecture-load-estimator) | Workload scenarios, traffic, concurrency, storage growth, resource pressure, and bottleneck risks. |
| [`architecture-integration-designer`](plugins/architecture-integration-designer) | API-first contracts, sync/async choices, events, webhooks, batch, resilience, and versioning. |
| [`architecture-deployment-designer`](plugins/architecture-deployment-designer) | Runtime topology, environments, network boundaries, stateful placement, scaling, rollout, reliability, and DR. |
| [`architecture-security-designer`](plugins/architecture-security-designer) | Trust boundaries, identity, authorization, data protection, abuse cases, secrets, audit, and compliance. |
| [`architecture-observability-designer`](plugins/architecture-observability-designer) | SLIs, SLOs, logs, metrics, traces, alerts, dashboards, diagnostics, incidents, and telemetry governance. |
| [`architecture-decision-discoverer`](plugins/architecture-decision-discoverer) | ADR and decision-note discovery, constraint extraction, drift detection, and decision-context briefs. |
| [`architecture-risk-evaluator`](plugins/architecture-risk-evaluator) | Architecture risks, assumptions, prioritization, validation spikes, mitigations, owners, and go/no-go readiness. |

## Repository Layout

```text
.
├── .agents/plugins/marketplace.json
├── plugins/
│   ├── architecture-diagrammer/
│   ├── architecture-requirementer/
│   ├── architecture-scope-bounder/
│   ├── architecture-domain-modeler/
│   ├── architecture-service-designer/
│   ├── architecture-data-designer/
│   ├── architecture-load-estimator/
│   ├── architecture-integration-designer/
│   ├── architecture-deployment-designer/
│   ├── architecture-security-designer/
│   ├── architecture-observability-designer/
│   ├── architecture-decision-discoverer/
│   └── architecture-risk-evaluator/
└── README.md
```

Each plugin keeps its manifest in `.codex-plugin/plugin.json` and its Codex skills under `skills/`.

## Naming

The marketplace and repository are named `komdosh-architect`.
Plugin names are stable and should remain unchanged unless there is a deliberate migration plan.

## Design Principles

- one plugin, one architecture stage
- read existing context before generating new output
- prefer compact decision-ready documents
- show assumptions and open questions explicitly
- avoid premature implementation detail
- keep diagrams source-backed
- keep review gates strict enough to catch weak architecture work
