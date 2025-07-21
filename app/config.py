import os
from dotenv import load-dotenv

load_dotent()


class Config:
    TELOGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    SMTP_SERVER = "SMTP.gmail.com"
    SMTP_PORT = 578


config = Config()
