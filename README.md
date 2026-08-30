# Komdosh Architect

Komdosh Architect is one compact [Codex plugin](plugins/komdosh-architect) for evidence-driven software architecture. It replaces the former marketplace of 15 stage-specific plugins and 137 micro-skills with one skill and seven references that are loaded only when relevant.

## What it covers

- requirements, scope, domain language, lifecycles, and invariants
- service/module boundaries, data ownership, APIs, events, webhooks, and batch flows
- load, deployment, reliability, operations, and observability
- security architecture, abuse cases, risk, and readiness
- ADR discovery, decision drift, and architecture review against actual code
- source-backed diagrams
- stakeholder acceptance and Jira/delivery handoff

The workflow is intentionally non-linear. Start at the user's problem and load only the matching reference.

## Install

Add this repository as a local marketplace, then install its single plugin:

```bash
codex plugin marketplace add /absolute/path/to/komdosh-architect
codex plugin add komdosh-architect@komdosh-architect
```

Start a new Codex task after installation or update so the new skill is loaded.

## Use

```text
Use $komdosh-architect:architecture to review this service architecture against the implementation.
```

```text
Use $komdosh-architect:architecture to decide the service, data, and integration boundaries for this feature.
```

```text
Use $komdosh-architect:architecture to produce a source-backed deployment diagram and readiness verdict.
```

The skill leads with the requested decision or verdict, labels assumptions, and keeps supporting detail proportional to the task.

## Migration from 0.2.x

This is a breaking packaging change. Every former plugin and namespaced micro-skill maps to the unified entrypoint:

```text
$komdosh-architect:architecture
```

Existing namespaced prompts for the former security designer, diagrammer, Jira tasker, and other stage plugins must be updated. The relevant domain checklists remain available through progressive-disclosure references inside the skill.

## Repository layout

```text
.
├── .agents/plugins/marketplace.json
├── plugins/komdosh-architect/
│   ├── .codex-plugin/plugin.json
│   └── skills/architecture/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       └── references/
└── scripts/validate_marketplace.py
```

## Validate

```bash
python3 scripts/validate_marketplace.py
python3 /path/to/plugin-creator/scripts/validate_plugin.py plugins/komdosh-architect
python3 /path/to/skill-creator/scripts/quick_validate.py plugins/komdosh-architect/skills/architecture
git diff --check
```

The repository validator checks marketplace policy, manifest identity and metadata, skill discovery, local references, namespaced invocations, and stale plugin directories.
