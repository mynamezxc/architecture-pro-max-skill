# Maintenance

## Update checklist

1. Edit canonical files under `skills/architecture-pro-max/`.
2. Run canonical validation.
3. Regenerate adapters.
4. Run unit tests.
5. Test installer in a temporary directory for all platforms.
6. Update platform compatibility notes when vendor discovery behavior changes.

## Instruction budget

Do not move large reference material into always-on platform rules. Keep wrappers small and let the agent load `SKILL.md`/references on demand.

## Versioning

Use semantic versioning:
- patch: wording/data fixes with same workflow contract;
- minor: new references/rules/scripts, backward compatible;
- major: skill activation/output contract or installation layout breaks.
