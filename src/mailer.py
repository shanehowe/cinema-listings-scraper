from smtplib import SMTP
from dotenv import load_dotenv
import os


def get_smtp_server() -> SMTP:
    load_dotenv()
    server = SMTP("smtp-mail.outlook.com", 587)
    server.starttls()
    server.login(os.getenv("EMAIL"), os.getenv("PASSWORD"))
    return server


def send_mail_and_quit(server: SMTP) -> None:
    # TODO: send mail
    server.quit()