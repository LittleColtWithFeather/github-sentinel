import smtplib
from email.mime.text import MIMEText
from src.config import NOTIFICATION_EMAIL

class EmailSender:
    def __init__(self):
        self.sender_email = NOTIFICATION_EMAIL

    def send_email(self, subject, body):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.sender_email
        msg['To'] = self.sender_email

        with smtplib.SMTP('smtp.example.com') as server:
            server.sendmail(self.sender_email, [self.sender_email], msg.as_string())
