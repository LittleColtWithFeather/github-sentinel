import unittest
from src.subscription_manager import SubscriptionManager

class TestSubscriptionManager(unittest.TestCase):
    def test_add_subscription(self):
        manager = SubscriptionManager()
        manager.add_subscription("example/repo")
        self.assertIn("example/repo", manager.get_subscriptions())

    def test_remove_subscription(self):
        manager = SubscriptionManager()
        manager.add_subscription("example/repo")
        manager.remove_subscription("example/repo")
        self.assertNotIn("example/repo", manager.get_subscriptions())

if __name__ == "__main__":
    unittest.main()
