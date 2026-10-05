import subprocess, sys, tempfile, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'tools/install.py'

class InstallTests(unittest.TestCase):
    def test_all_platform_install(self):
        with tempfile.TemporaryDirectory() as td:
            subprocess.check_call([sys.executable, str(SCRIPT), '--platform','all','--target',td])
            p = Path(td)
            required = [
                '.claude/skills/architecture-pro-max/SKILL.md',
                '.cursor/skills/architecture-pro-max/SKILL.md',
                '.github/skills/architecture-pro-max/SKILL.md',
                '.kiro/skills/architecture-pro-max/SKILL.md',
                '.qoder/skills/architecture-pro-max/SKILL.md',
                '.agents/skills/architecture-pro-max/SKILL.md',
                '.windsurf/rules/architecture-pro-max.md',
                '.agents/rules/architecture-pro-max.md',
            ]
            for rel in required:
                self.assertTrue((p/rel).exists(), rel)

if __name__ == '__main__': unittest.main()
