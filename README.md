# Komdosh Architect Marketplace

Codex marketplace repository for Komdosh architecture tools.
It currently exposes the `architecture-diagrammer`, `architecture-requirementer`, and `architecture-scope-bounder` plugins.

## Install

```bash
codex plugin marketplace add https://github.com/Komdosh/komdosh-architect.git
```

The repository and marketplace names are `komdosh-architect`.
Plugin names remain stable:

- `architecture-diagrammer`
- `architecture-requirementer`
- `architecture-scope-bounder`

To enable plugins explicitly in `~/.codex/config.toml`:

```toml
[plugins."architecture-diagrammer@komdosh-architect"]
enabled = true

[plugins."architecture-requirementer@komdosh-architect"]
enabled = true

[plugins."architecture-scope-bounder@komdosh-architect"]
enabled = true
```

Restart Codex after adding or updating the marketplace so the plugin skills are loaded into the session context.

## Plugins

- [plugins/architecture-diagrammer](plugins/architecture-diagrammer)
- [plugins/architecture-requirementer](plugins/architecture-requirementer)
- [plugins/architecture-scope-bounder](plugins/architecture-scope-bounder)
