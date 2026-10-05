import subprocess, sys, tempfile, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'skills/architecture-pro-max/scripts/init_project_docs.py'

class ProjectDocsTests(unittest.TestCase):
    def test_scaffold_and_preserve_existing(self):
        with tempfile.TemporaryDirectory() as td:
            subprocess.check_call([sys.executable, str(SCRIPT), '--target', td])
            root = Path(td)
            index = root/'docs/ai/INDEX.md'
            self.assertTrue(index.exists())
            custom = '# custom content\n'
            index.write_text(custom, encoding='utf-8')
            subprocess.check_call([sys.executable, str(SCRIPT), '--target', td])
            self.assertEqual(index.read_text(encoding='utf-8'), custom)
            self.assertTrue((root/'docs/testing/results/cross-platform/.gitkeep').exists())

if __name__ == '__main__': unittest.main()
