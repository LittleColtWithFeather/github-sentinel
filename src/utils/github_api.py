import requests
from src.config import GITHUB_TOKEN

class GitHubAPI:
    def __init__(self):
        self.token = GITHUB_TOKEN
        self.headers = {"Authorization": f"token {self.token}"}

    def get_repo_updates(self, repo_url):
        response = requests.get(f"https://api.github.com/repos/{repo_url}/events", headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
