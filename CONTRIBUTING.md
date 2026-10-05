# Contributing

1. Make changes in `skills/architecture-pro-max/` first.
2. Keep platform-specific behavior in `tools/generate_adapters.py`.
3. Add or update tests for every deterministic behavior change.
4. Regenerate adapters and ensure `--check` passes.
5. Keep recommendations technology-neutral unless a reference is explicitly stack-specific.
6. New architecture rules should include: problem, forces, when to use, when not to use, trade-offs, migration path and test implications.
