#!/usr/bin/env python3
from pathlib import Path
import argparse, shutil, sys

ROOT = Path(__file__).resolve().parents[1]
CANON = ROOT / 'skills' / 'architecture-pro-max'
ADAPTERS = ROOT / 'adapters'

PLATFORMS = {
    'claude': '.claude/skills/architecture-pro-max',
    'cursor': '.cursor/skills/architecture-pro-max',
    'copilot': '.github/skills/architecture-pro-max',
    'kiro': '.kiro/skills/architecture-pro-max',
    'codex': '.agents/skills/architecture-pro-max',
    'qoder': '.qoder/skills/architecture-pro-max',
}

WINDSURF_RULE = """---\ntrigger: model_decision\ndescription: "Use Architecture Pro Max when designing or reviewing software architecture, multi-platform systems, module boundaries, databases, integrations, testing or major refactors."\n---\n\n# Architecture Pro Max\n\nFor architecture/system-design tasks, read and follow `.agents/skills/architecture-pro-max/SKILL.md` from this adapter bundle. Load its referenced files only when relevant. Require explicit alternatives, decision rationale, self-critique, a simpler fallback, test strategy and project documentation/change rules.\n"""

ANTIGRAVITY_RULE = """---\ntrigger: model_decision\ndescription: "Deep software architecture analysis and multi-platform system design."\n---\n\nUse the portable skill at `.agents/skills/architecture-pro-max/SKILL.md` for architecture design, major refactors and system-boundary decisions.\n"""


def copy_skill(dest: Path):
    if dest.exists(): shutil.rmtree(dest)
    shutil.copytree(CANON, dest)


def build(target: Path):
    if target.exists(): shutil.rmtree(target)
    target.mkdir(parents=True)
    for platform, rel in PLATFORMS.items():
        copy_skill(target / platform / rel)
    # Windsurf keeps a rule wrapper plus a bundled canonical skill for portability.
    copy_skill(target / 'windsurf' / '.agents/skills/architecture-pro-max')
    rule = target / 'windsurf' / '.windsurf/rules/architecture-pro-max.md'
    rule.parent.mkdir(parents=True, exist_ok=True)
    rule.write_text(WINDSURF_RULE, encoding='utf-8')
    # Antigravity uses portable skill + scoped rule.
    copy_skill(target / 'antigravity' / '.agents/skills/architecture-pro-max')
    rule = target / 'antigravity' / '.agents/rules/architecture-pro-max.md'
    rule.parent.mkdir(parents=True, exist_ok=True)
    rule.write_text(ANTIGRAVITY_RULE, encoding='utf-8')


def compare_dirs(a: Path, b: Path):
    def files(p): return sorted(x.relative_to(p) for x in p.rglob('*') if x.is_file())
    fa, fb = files(a), files(b)
    if fa != fb: return False
    return all((a/x).read_bytes() == (b/x).read_bytes() for x in fa)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    args = ap.parse_args()
    if args.check:
        tmp = ROOT / '.adapter-check'
        build(tmp)
        ok = ADAPTERS.exists() and compare_dirs(tmp, ADAPTERS)
        shutil.rmtree(tmp, ignore_errors=True)
        if not ok:
            print('Generated adapters are out of date. Run: python tools/generate_adapters.py')
            sys.exit(1)
        print('Generated adapters: up to date')
    else:
        build(ADAPTERS)
        print(f'Generated adapters in {ADAPTERS}')

if __name__ == '__main__':
    main()
