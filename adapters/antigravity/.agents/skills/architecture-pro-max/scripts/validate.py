#!/usr/bin/env python3
from pathlib import Path
import json, sys, re

ROOT = Path(__file__).resolve().parents[3]
SKILL = ROOT / 'skills' / 'architecture-pro-max'
errors = []

skill_text = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
if not skill_text.startswith('---\n'):
    errors.append('SKILL.md must start with YAML frontmatter')
if 'name: architecture-pro-max' not in skill_text[:1000]:
    errors.append('SKILL.md name is missing or incorrect')
if 'description:' not in skill_text[:1500]:
    errors.append('SKILL.md description is missing')

for filename in ['architectures.json','product-profiles.json','platform-strategies.json','quality-attributes.json']:
    try:
        json.loads((SKILL / 'data' / filename).read_text(encoding='utf-8'))
    except Exception as e:
        errors.append(f'{filename}: {e}')

refs = re.findall(r'`(references/[^`]+\.md)`', skill_text)
for rel in sorted(set(refs)):
    if not (SKILL / rel).exists():
        errors.append(f'missing reference: {rel}')

required = [
    'references/architecture-decision-framework.md',
    'references/pattern-catalog.md',
    'references/multiplatform-strategy.md',
    'references/stack-selection.md',
    'references/database-integration.md',
    'references/project-structure-standard.md',
    'references/testing-quality-gates.md',
    'references/ai-maintenance-contract.md',
    'references/self-critique-checklist.md',
]
for rel in required:
    if not (SKILL / rel).exists(): errors.append(f'missing {rel}')

if errors:
    print('Validation failed:')
    for e in errors: print('-', e)
    sys.exit(1)
print('Architecture Pro Max skill validation: OK')
