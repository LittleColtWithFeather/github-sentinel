from src.utils.github_api import GitHubAPI

class UpdateFetcher:
    def __init__(self):
        self.github_api = GitHubAPI()

    def fetch_updates(self, subscriptions):
        updates = {}
        for repo in subscriptions:
            updates[repo] = self.github_api.get_repo_updates(repo)
        return updates
