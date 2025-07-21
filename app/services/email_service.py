import smtplib
from email.mime.text import MIMEText
from app.config import config


def send_email(to_email: str, subject: str, body: str):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = config.EMAIL_ADDRESS
    msg['To'] = to_email

    with smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT) as server:
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.EMAIL_PASSWORD)
        server.send_message(msg)

