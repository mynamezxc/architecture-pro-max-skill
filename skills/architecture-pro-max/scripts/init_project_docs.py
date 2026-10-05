#!/usr/bin/env python3
"""Initialize the Architecture Pro Max project documentation contract."""
from pathlib import Path
import argparse, shutil, sys

SKILL = Path(__file__).resolve().parents[1]
TEMPLATE = SKILL / 'assets' / 'project-docs'


def copy_tree(src: Path, dest: Path, force: bool):
    created, skipped = [], []
    for item in src.rglob('*'):
        rel = item.relative_to(src)
        out = dest / rel
        if item.is_dir():
            out.mkdir(parents=True, exist_ok=True)
            continue
        out.parent.mkdir(parents=True, exist_ok=True)
        if out.exists() and not force:
            skipped.append(str(out))
            continue
        shutil.copy2(item, out)
        created.append(str(out))
    return created, skipped


def main():
    ap = argparse.ArgumentParser(description='Create docs/ architecture/product/testing/ai contract in a target project.')
    ap.add_argument('--target', default='.', help='Target project root')
    ap.add_argument('--force', action='store_true', help='Overwrite existing template files')
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()
    target = Path(args.target).expanduser().resolve() / 'docs'
    if args.dry_run:
        for item in TEMPLATE.rglob('*'):
            if item.is_file(): print(target / item.relative_to(TEMPLATE))
        return
    created, skipped = copy_tree(TEMPLATE, target, args.force)
    print(f'Project docs initialized: {len(created)} files written, {len(skipped)} existing files preserved.')
    if skipped:
        print('Preserved existing files:')
        for x in skipped: print('-', x)

if __name__ == '__main__':
    main()
