from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from movie import Movie
import os

load_dotenv()


def get_smtp_server() -> SMTP:
    server = SMTP("smtp-mail.outlook.com", 587)
    server.starttls()

    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    if not email or not password:
        raise Exception("No email and/or password found in environment variables.")

    server.login(email, password)
    return server


def build_html_email(movies: list[Movie]) -> MIMEMultipart:
    message = MIMEMultipart("alternative")
    message["subject"] = "Cinema Listings 🍿"
    message["from"] = os.getenv("EMAIL")
    message["to"] = f"{os.getenv('SHANE')}, {os.getenv('GEORGINA')}"

    movies_html_section = ""
    for movie in movies:
        movies_html_section += movie.to_html()

    html_content = f"""
        <html>
            <head></head>
            <body>
                {movies_html_section}
            </body>
        </html>
    """
    part = MIMEText(html_content, "html")
    message.attach(part)
    return message
