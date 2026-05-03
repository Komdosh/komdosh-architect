# Komdosh Architect Marketplace

Codex marketplace repository for Komdosh architecture tools.
It currently exposes the `architecture-diagrammer` plugin.

## Install

```bash
codex plugin marketplace add https://github.com/Komdosh/komdosh-architect.git
```

The repository and marketplace name is `komdosh-architect`.
The plugin name remains `architecture-diagrammer`.

To enable the plugin explicitly in `~/.codex/config.toml`:

```toml
[plugins."architecture-diagrammer@komdosh-architect"]
enabled = true
```

Restart Codex after adding or updating the marketplace so the plugin skills are loaded into the session context.

## Plugin

The plugin package lives at [plugins/architecture-diagrammer](plugins/architecture-diagrammer).
