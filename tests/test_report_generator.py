import unittest
from src.report_generator import ReportGenerator

class TestReportGenerator(unittest.TestCase):
    def test_generate_report(self):
        generator = ReportGenerator()
        updates = {"example/repo": {"events": []}}
        report = generator.generate_report(updates)
        self.assertIn("example/repo", report)

if __name__ == "__main__":
    unittest.main()
