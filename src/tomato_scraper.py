from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import cinema_scraper


def get_headless_browser() -> WebDriver:
    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Firefox(options=options)
    return browser


def get_tomato_score(web_driver: WebDriver, title: str) -> int | None:
    ENTER_KEY = "\ue007"
    web_driver.get("https://www.rottentomatoes.com/")
    search_box = web_driver.find_element(by=By.CLASS_NAME, value="search-text")
    search_box.send_keys(title)
    search_box.send_keys(ENTER_KEY)
    web_driver.implicitly_wait(6)
    shadow_host_elements = web_driver.find_elements(
        By.CSS_SELECTOR, '[data-qa="search-result"]'
    )
    if len(shadow_host_elements) < 2:
        return None
    shadow_root = shadow_host_elements[1]
    nested_shadow_root = shadow_root.find_element(
        By.CSS_SELECTOR, '[data-qa="data-row"]'
    )
    score = nested_shadow_root.get_attribute("tomatometerscore")
    if score is None or not score.isdigit():
        return None
    return int(score)


if __name__ == "__main__":
    cinema_soup = cinema_scraper.get_cinema_soup()
    cinema_listings = cinema_scraper.get_cinema_listings(cinema_soup)
    movies = cinema_scraper.create_movie_objects(cinema_listings)
    driver = get_headless_browser()
    for movie in movies:
        try:
            score = get_tomato_score(driver, movie.get_title())
            movie.set_rotten_tomato(score)
            print(movie)
        except Exception as e:
            print(e)
            continue
    driver.close()
