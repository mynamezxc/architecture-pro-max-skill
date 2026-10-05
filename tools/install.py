#!/usr/bin/env python3
"""Install Architecture Pro Max into a target repository. Standard library only."""
from pathlib import Path
import argparse, shutil, sys

ROOT = Path(__file__).resolve().parents[1]
CANON = ROOT / 'skills' / 'architecture-pro-max'

SKILL_PATHS = {
    'claude': '.claude/skills/architecture-pro-max',
    'cursor': '.cursor/skills/architecture-pro-max',
    'copilot': '.github/skills/architecture-pro-max',
    'kiro': '.kiro/skills/architecture-pro-max',
    'codex': '.agents/skills/architecture-pro-max',
    'qoder': '.qoder/skills/architecture-pro-max',
}

WINDSURF_RULE = """---\ntrigger: model_decision\ndescription: "Use Architecture Pro Max when designing or reviewing software architecture, multi-platform systems, module boundaries, databases, integrations, testing or major refactors."\n---\n\n# Architecture Pro Max\n\nRead `.agents/skills/architecture-pro-max/SKILL.md` when this rule applies. Load references progressively. Require alternatives, concise rationale, self-critique, simpler fallback, migration thresholds, tests and documentation rules.\n"""
ANTIGRAVITY_RULE = """---\ntrigger: model_decision\ndescription: "Deep software architecture analysis and multi-platform system design."\n---\n\nUse `.agents/skills/architecture-pro-max/SKILL.md` for architecture design, major refactors and system-boundary decisions.\n"""


def planned(platform, target):
    if platform in SKILL_PATHS:
        return [(CANON, target / SKILL_PATHS[platform], 'dir')]
    if platform == 'windsurf':
        return [
            (CANON, target / '.agents/skills/architecture-pro-max', 'dir'),
            (WINDSURF_RULE, target / '.windsurf/rules/architecture-pro-max.md', 'text'),
        ]
    if platform == 'antigravity':
        return [
            (CANON, target / '.agents/skills/architecture-pro-max', 'dir'),
            (ANTIGRAVITY_RULE, target / '.agents/rules/architecture-pro-max.md', 'text'),
        ]
    raise ValueError(platform)


def install_one(platform, target, dry):
    for src, dest, kind in planned(platform, target):
        print(f'[{platform}] {dest}')
        if dry: continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        if kind == 'dir':
            if dest.exists(): shutil.rmtree(dest)
            shutil.copytree(src, dest)
        else:
            dest.write_text(src, encoding='utf-8')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--platform', required=True, choices=list(SKILL_PATHS)+['windsurf','antigravity','all'])
    ap.add_argument('--target', required=True)
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()
    target = Path(args.target).expanduser().resolve()
    platforms = list(SKILL_PATHS) + ['windsurf','antigravity'] if args.platform == 'all' else [args.platform]
    for p in platforms: install_one(p, target, args.dry_run)
    if not args.dry_run:
        print('Install complete. Existing Architecture Pro Max skill files were replaced; unrelated files were untouched.')

if __name__ == '__main__':
    main()
