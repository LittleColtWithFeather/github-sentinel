import unittest
from unittest.mock import patch
from src.notifier import Notifier

class TestNotifier(unittest.TestCase):
    @patch("src.utils.email_sender.EmailSender.send_email")
    def test_send_notifications(self, mock_send_email):
        notifier = Notifier()
        notifier.send_notifications("Test Report")
        mock_send_email.assert_called_once_with("GitHub Sentinel Report", "Test Report")

if __name__ == "__main__":
    unittest.main()
