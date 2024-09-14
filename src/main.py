from src.subscription_manager import SubscriptionManager
from src.update_fetcher import UpdateFetcher
from src.notifier import Notifier
from src.report_generator import ReportGenerator

def main():
    subscription_manager = SubscriptionManager()
    update_fetcher = UpdateFetcher()
    notifier = Notifier()
    report_generator = ReportGenerator()

    subscriptions = subscription_manager.get_subscriptions()
    updates = update_fetcher.fetch_updates(subscriptions)
    report = report_generator.generate_report(updates)
    notifier.send_notifications(report)

if __name__ == "__main__":
    main()
