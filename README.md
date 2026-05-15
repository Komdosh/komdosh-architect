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
- focused plugins for requirements, scope, domain, service, data, load, integration, deployment, security, observability, decisions, risks, stakeholder acceptance, Jira handoff, and diagrams
- compact, self-contained outputs written for humans first
- review gates that catch missing context, unclear decisions, drift, and premature implementation detail
- reusable Codex skill names that can be called directly in prompts

## How To Choose

Start from the work you need to finish, not from the full plugin list.

| Need | Start with | Then add |
|------|------------|----------|
| New product or large feature | [`architecture-requirementer`](plugins/architecture-requirementer) | scope, domain, service, data, integration |
| Existing system with unknown constraints | [`architecture-decision-discoverer`](plugins/architecture-decision-discoverer) | risk, scope, service, diagram |
| Unclear ownership or boundaries | [`architecture-scope-bounder`](plugins/architecture-scope-bounder) | domain, service, data |
| API, events, webhooks, or external systems | [`architecture-integration-designer`](plugins/architecture-integration-designer) | security, observability, deployment |
| Runtime placement or production readiness | [`architecture-deployment-designer`](plugins/architecture-deployment-designer) | load, observability, security, risk |
| Architecture ready for stakeholder sign-off | [`architect-interviewer`](plugins/architect-interviewer) | risk, Jira tasker, diagrammer |
| Final implementation handoff | [`architecture-risk-evaluator`](plugins/architecture-risk-evaluator) | Jira tasker, diagrammer |

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
| 12 | [`architect-interviewer`](plugins/architect-interviewer) | Present completed architecture, interview stakeholders, and record acceptance or required revisions. |
| 13 | [`architecture-jira-tasker`](plugins/architecture-jira-tasker) | Create rich, self-contained Jira implementation tasks from completed architecture docs. |
| Any | [`architecture-diagrammer`](plugins/architecture-diagrammer) | Create source-backed architecture diagrams from any stage output. |

## Recommended Sets

For everyday use, enable only the plugins that match the team workflow.

| Set | Plugins | Best for |
|-----|---------|----------|
| Discovery | decision discoverer, requirementer, scope bounder, diagrammer | Early product or architecture discovery. |
| Design core | domain modeler, service designer, data designer, integration designer | Turning scope into system structure and contracts. |
| Production readiness | load estimator, deployment designer, security designer, observability designer, risk evaluator | Preparing architecture for real operation. |
| Acceptance | interviewer, risk evaluator, diagrammer | Presenting the architecture and confirming stakeholder acceptance. |
| Delivery handoff | risk evaluator, Jira tasker, diagrammer | Converting approved architecture into implementation work. |

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

[plugins."architect-interviewer@komdosh-architect"]
enabled = true

[plugins."architecture-jira-tasker@komdosh-architect"]
enabled = true
```

## Prompt Examples

```text
Use $architecture-requirementer:architecture-requirementer to prepare architect-ready requirements for this product idea.
```

```text
Use $architecture-decision-discoverer:decision-discoverer to find ADRs and decision notes that constrain this design.
```

```text
Use $architecture-integration-designer:integration-designer to design API and integration contracts for this architecture.
```

```text
Use $architecture-risk-evaluator:architecture-risk-evaluator to evaluate implementation readiness and produce a compact risk register.
```

```text
Use $architect-interviewer:architect-interviewer to present this service architecture and interview me for acceptance.
```

```text
Use $architecture-jira-tasker:architecture-jira-tasker to create a rich Jira task from completed architecture docs.
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
| [`architect-interviewer`](plugins/architect-interviewer) | Stakeholder-facing architecture presentation, requirements coverage interviews, acceptance decisions, and revision records. |
| [`architecture-jira-tasker`](plugins/architecture-jira-tasker) | Jira-ready AI-agent implementation tasks from completed architecture docs. |

## Suggested Plugins To Add Next

These are good marketplace candidates, but they should be added only when their scope is crisp enough to stay independent.

| Candidate | Why it belongs | Boundary |
|-----------|----------------|----------|
| `architecture-adr-writer` | The marketplace can discover and evaluate decisions, but it intentionally does not write or supersede ADRs. | Writes ADRs only after decision context is found and reviewed. |
| `architecture-api-contract-designer` | Integration design stops before final schemas; teams often need OpenAPI, event, webhook, and compatibility contract detail next. | Detailed contracts only, not service implementation. |
| `architecture-implementation-planner` | Jira tasker creates delivery tickets, but a repo-local implementation plan is useful before ticket creation. | Produces implementation sequence, file/module ownership, validation plan, and rollout notes. |
| `architecture-migration-planner` | Existing systems need coexistence, data backfill, contract migration, rollback, and cutover planning across several current plugins. | Migration strategy only, not migration scripts. |
| `architecture-cost-estimator` | Load and deployment plugins expose capacity pressure, but cost tradeoffs deserve a dedicated decision brief. | Estimates cost ranges and levers, not cloud billing automation. |
| `architecture-reviewer` | Each plugin has a local review gate; a final cross-stage reviewer would catch contradictions across the full design set. | Reviews completed architecture docs, does not rewrite them by default. |

The highest-value next additions are `architecture-adr-writer`, `architecture-api-contract-designer`, and `architecture-implementation-planner` because they cover clear gaps after the current discovery, integration, and Jira handoff stages.

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
│   ├── architecture-risk-evaluator/
│   ├── architect-interviewer/
│   └── architecture-jira-tasker/
├── scripts/
│   └── validate_marketplace.py
└── README.md
```

Each plugin keeps its manifest in `.codex-plugin/plugin.json` and its Codex skills under `skills/`.

## Maintaining The Marketplace

Update the marketplace as one change set so the install metadata, plugin docs, and landing page do not drift.

1. Add or update the plugin under `plugins/<plugin-name>/`.
2. Update `.agents/plugins/marketplace.json`.
3. Update the root `README.md` catalog, workflow guidance, enable snippet, and repository layout.
4. Check that namespaced prompt examples use runtime skill names from `SKILL.md` frontmatter.
5. Run validation before committing:

```bash
python3 scripts/validate_marketplace.py
python3 -m json.tool .agents/plugins/marketplace.json >/dev/null
git diff --check
```

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
