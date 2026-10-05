import subprocess, sys, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class ValidationTests(unittest.TestCase):
    def test_skill_validation(self):
        subprocess.check_call([sys.executable, str(ROOT/'skills/architecture-pro-max/scripts/validate.py')])
if __name__ == '__main__': unittest.main()
