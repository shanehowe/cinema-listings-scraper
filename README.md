# Cinema Listings Scraper

The Cinema Listings Scraper is a Python project I developed to scrape cinema listings in my area, query an API for movie ratings, and send an email notification with the movie details to myself and my girlfriend. This project allows us to stay updated with movie times for our weekly cinema visits.

## Project Overview

- **Web scraping:** The project utilizes BeautifulSoup (bs4) to scrape cinema listings from a specific website.
- **API integration:** It queries an external API to fetch movie ratings for the scraped listings.
- **Email notification:** The project uses SMTP to send an email with the movie details to both me and my girlfriend.
- **Deployment:** The project is deployed as a cron job on Google Cloud, scheduled to run every weekend.

## Why?

I created this project because my girlfriend and I frequently visit the cinema on weekends, but we end up leaving it too late to book tickets. This project serves as a reminder and provides us with the cinema listings that we can easily book in advance.

## Features

- **Code formatting:** The project's code is formatted using `black` to ensure a consistent and readable coding style.
- **Type checking:** The project is fully type checked with `mypy` to catch potential type-related errors.
