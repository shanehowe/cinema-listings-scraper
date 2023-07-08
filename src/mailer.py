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
            <head>
                <style>
                    body {{
                        font-family: Arial, sans-serif;

                    }}
                    
                    h3 {{
                        color: #333333;
                        font-size: 18px;
                        text-align: center;
                    }}
                    
                    p {{
                        color: #777777;
                        font-size: 14px;
                        text-align: center;
                    }}
                    
                    .container {{
                        max-width: 600px;
                        margin: 0 auto;
                        padding: 20px;
                        background-color: #ffffff;
                        box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
                    }}
                </style>
            </head>
            <body>
                <p style="text-align: center;">🎬 Here's what's on in the cinema tonight 🎬</p>
                {movies_html_section}
            </body>
            </html>
    """
    part = MIMEText(html_content, "html")
    message.attach(part)
    return message
