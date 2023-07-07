from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


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
