class SubscriptionManager:
    def __init__(self):
        self.subscriptions = []

    def get_subscriptions(self):
        return self.subscriptions

    def add_subscription(self, repo_url):
        self.subscriptions.append(repo_url)

    def remove_subscription(self, repo_url):
        self.subscriptions.remove(repo_url)
