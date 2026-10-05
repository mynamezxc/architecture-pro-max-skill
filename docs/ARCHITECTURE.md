# Repository architecture

`skills/architecture-pro-max/` is the canonical Agent Skill. `tools/generate_adapters.py` produces platform-specific installation artifacts under `adapters/`. Platform wrappers must stay thin; architectural knowledge belongs in the canonical skill.

The split deliberately follows progressive disclosure:

- `SKILL.md`: workflow and output contract;
- `references/`: deep explanatory knowledge;
- `data/`: structured facts for scripts/tools;
- `scripts/`: deterministic helpers;
- `assets/`: files copied into user projects.

This structure prevents every AI client from carrying a different copy of architecture policy.
