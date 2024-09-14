import unittest
from unittest.mock import patch
from src.update_fetcher import UpdateFetcher

class TestUpdateFetcher(unittest.TestCase):
    @patch("src.utils.github_api.GitHubAPI.get_repo_updates", return_value={"events": []})
    def test_fetch_updates(self, mock_get_repo_updates):
        fetcher = UpdateFetcher()
        subscriptions = ["example/repo"]
        updates = fetcher.fetch_updates(subscriptions)
        self.assertIn("example/repo", updates)

if __name__ == "__main__":
    unittest.main()
