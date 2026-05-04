# Komdosh Architect Marketplace

Codex marketplace repository for Komdosh architecture tools.
It currently exposes the `architecture-diagrammer`, `architecture-requirementer`, `architecture-scope-bounder`, `architecture-domain-modeler`, `architecture-service-designer`, `architecture-data-designer`, `architecture-load-estimator`, `architecture-integration-designer`, `architecture-deployment-designer`, `architecture-security-designer`, `architecture-observability-designer`, `architecture-decision-discoverer`, and `architecture-risk-evaluator` plugins.

## Install

```bash
codex plugin marketplace add https://github.com/Komdosh/komdosh-architect.git
```

The repository and marketplace names are `komdosh-architect`.
Plugin names remain stable:

- `architecture-diagrammer`
- `architecture-requirementer`
- `architecture-scope-bounder`
- `architecture-domain-modeler`
- `architecture-service-designer`
- `architecture-data-designer`
- `architecture-load-estimator`
- `architecture-integration-designer`
- `architecture-deployment-designer`
- `architecture-security-designer`
- `architecture-observability-designer`
- `architecture-decision-discoverer`
- `architecture-risk-evaluator`

To enable plugins explicitly in `~/.codex/config.toml`:

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

Restart Codex after adding or updating the marketplace so the plugin skills are loaded into the session context.

## Human-Readable Outputs

All plugins must prefer readability over professional complexity.
Architecture documents should be compact, self-contained, and easy to scan.

- put the main idea or decision first
- use plain words before specialist terms
- highlight only important decisions, risks, assumptions, open questions, and next steps
- keep details close to the point they explain
- avoid long paragraphs and decorative wording
- explain necessary technical terms in place

## Plugins

- [plugins/architecture-diagrammer](plugins/architecture-diagrammer)
- [plugins/architecture-requirementer](plugins/architecture-requirementer)
- [plugins/architecture-scope-bounder](plugins/architecture-scope-bounder)
- [plugins/architecture-domain-modeler](plugins/architecture-domain-modeler)
- [plugins/architecture-service-designer](plugins/architecture-service-designer)
- [plugins/architecture-data-designer](plugins/architecture-data-designer)
- [plugins/architecture-load-estimator](plugins/architecture-load-estimator)
- [plugins/architecture-integration-designer](plugins/architecture-integration-designer)
- [plugins/architecture-deployment-designer](plugins/architecture-deployment-designer)
- [plugins/architecture-security-designer](plugins/architecture-security-designer)
- [plugins/architecture-observability-designer](plugins/architecture-observability-designer)
- [plugins/architecture-decision-discoverer](plugins/architecture-decision-discoverer)
- [plugins/architecture-risk-evaluator](plugins/architecture-risk-evaluator)
