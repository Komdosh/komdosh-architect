# Komdosh Architect Marketplace

Codex marketplace repository for Komdosh architecture tools.
It currently exposes the `architecture-diagrammer`, `architecture-requirementer`, `architecture-scope-bounder`, `architecture-domain-modeler`, `architecture-service-designer`, and `architecture-data-designer` plugins.

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
```

Restart Codex after adding or updating the marketplace so the plugin skills are loaded into the session context.

## Plugins

- [plugins/architecture-diagrammer](plugins/architecture-diagrammer)
- [plugins/architecture-requirementer](plugins/architecture-requirementer)
- [plugins/architecture-scope-bounder](plugins/architecture-scope-bounder)
- [plugins/architecture-domain-modeler](plugins/architecture-domain-modeler)
- [plugins/architecture-service-designer](plugins/architecture-service-designer)
- [plugins/architecture-data-designer](plugins/architecture-data-designer)
