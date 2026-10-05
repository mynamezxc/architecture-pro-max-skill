# Platform compatibility

The project targets the open Agent Skills shape (`SKILL.md` + optional references/scripts/assets) wherever a client supports it. Vendor-specific rule wrappers are used only where needed.

| Platform | Primary mechanism | Repository target |
|---|---|---|
| Claude Code | Agent Skill | `.claude/skills/architecture-pro-max/` |
| Cursor | Agent Skill | `.cursor/skills/architecture-pro-max/` |
| Windsurf | Model-decision rule + portable skill | `.windsurf/rules/` + `.agents/skills/` |
| Antigravity | Agent rule + portable skill | `.agents/rules/` + `.agents/skills/` |
| GitHub Copilot | Agent Skill | `.github/skills/architecture-pro-max/` |
| Kiro | Agent Skill | `.kiro/skills/architecture-pro-max/` |
| Codex | Agent Skill / Agent Plugin | `.agents/skills/architecture-pro-max/` or root plugin |
| Qoder | Agent Skill | `.qoder/skills/architecture-pro-max/` |

When a vendor changes discovery syntax, update only the installer/generator and this compatibility document unless the Agent Skills format itself changes.
