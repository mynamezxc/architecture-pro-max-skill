import subprocess, sys, tempfile, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'skills/architecture-pro-max/scripts/architect.py'

class ReasonerTests(unittest.TestCase):
    def run_plan(self, *args):
        return subprocess.check_output([sys.executable, str(SCRIPT), *args], text=True)

    def test_crm_small_team_does_not_default_microservices(self):
        out = self.run_plan('--product','crm','--platform','web','mobile','desktop','--team-size','7','--domain-complexity','high','--integrations','6','--realtime','--offline','mobile','--multi-tenant')
        self.assertIn('Recommendation', out)
        recommendation = out.split('## 5. Recommendation',1)[1].split('## 6.',1)[0]
        self.assertNotIn('**Microservices**', recommendation)
        self.assertIn('Self-critique', out)
        self.assertIn('cross-platform', out.lower())

    def test_json_mode(self):
        out = self.run_plan('--product','saas','--json')
        self.assertIn('"pressures"', out)
        self.assertIn('"candidates"', out)

if __name__ == '__main__': unittest.main()
