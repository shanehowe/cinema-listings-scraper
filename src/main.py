import cinema_scraper
import mailer
import os
import logging

from dotenv import load_dotenv


def main():
    load_dotenv()
    logging.basicConfig(level=logging.INFO)

    logging.info("Getting cinema listings")
    cinema_soup = cinema_scraper.get_cinema_soup()
    cinema_listings = cinema_scraper.get_cinema_listings(cinema_soup)
    movies = cinema_scraper.create_movie_objects(cinema_listings)

    for movie in movies:
        title = movie.get_title()
        logging.info(f"Getting rating for {title}")
        rating = cinema_scraper.get_movie_rating(title)
        movie.set_rating(rating)

    logging.info("Trying to send email")
    server = mailer.get_smtp_server()
    email = mailer.build_html_email(movies)
    from_address = os.getenv("EMAIL")
    to_addresses = [os.getenv("SHANE"), os.getenv("GEORGINA")]

    try:
        server.sendmail(from_address, to_addresses, email.as_string())
    except Exception as e:
        logging.error(f"Email not sent.\n{e}")
    finally:
        server.quit()


if __name__ == "__main__":
    main()
