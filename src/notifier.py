from src.utils.email_sender import EmailSender

class Notifier:
    def __init__(self):
        self.email_sender = EmailSender()

    def send_notifications(self, report):
        self.email_sender.send_email("GitHub Sentinel Report", report)
