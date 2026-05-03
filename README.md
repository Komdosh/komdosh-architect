# Komdosh Architect Marketplace

Codex marketplace repository for Komdosh architecture tools.
It currently exposes the `architecture-diagrammer` and `architect-requirementer` plugins.

## Install

```bash
codex plugin marketplace add https://github.com/Komdosh/komdosh-architect.git
```

The repository and marketplace names are `komdosh-architect`.
Plugin names remain stable:

- `architecture-diagrammer`
- `architect-requirementer`

To enable plugins explicitly in `~/.codex/config.toml`:

```toml
[plugins."architecture-diagrammer@komdosh-architect"]
enabled = true

[plugins."architect-requirementer@komdosh-architect"]
enabled = true
```

Restart Codex after adding or updating the marketplace so the plugin skills are loaded into the session context.

## Plugins

- [plugins/architecture-diagrammer](plugins/architecture-diagrammer)
- [plugins/architect-requirementer](plugins/architect-requirementer)
