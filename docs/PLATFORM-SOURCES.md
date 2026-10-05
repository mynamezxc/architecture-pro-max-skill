# Platform source notes

Compatibility should be re-verified periodically because AI coding clients change discovery paths and plugin formats quickly. The project was checked against the following public documentation on 2026-10-05:

- Claude Code extension/skills overview: https://code.claude.com/docs/
- Cursor Agent Skills: https://cursor.com/docs/skills
- GitHub Copilot agent skills: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills
- Kiro Agent Skills: https://kiro.dev/docs/skills/
- OpenAI/Codex skills and plugins: https://developers.openai.com/plugins/build/skills and https://developers.openai.com/plugins/build/plugins
- Qoder Skills: https://docs.qoder.com/extensions/skills
- Google Antigravity rules/plugins: https://www.antigravity.google/docs/rules/ and https://www.antigravity.google/docs/plugins
- Windsurf rules/customizations: https://docs.windsurf.com/ and https://github.com/Windsurf-Samples/cascade-customizations-catalog

The canonical skill follows the portable Agent Skills shape wherever supported. Vendor-specific wrappers should remain thin.
