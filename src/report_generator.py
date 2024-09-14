class ReportGenerator:
    def generate_report(self, updates):
        report = "GitHub Sentinel Report:\n"
        for repo, update in updates.items():
            report += f"Repo: {repo}\nUpdates:\n{update}\n\n"
        return report
