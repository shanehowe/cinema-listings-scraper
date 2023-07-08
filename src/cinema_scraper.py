import os
from datetime import datetime
from bs4 import BeautifulSoup, ResultSet, Tag
from movie import Movie
import requests


def get_cinema_soup() -> BeautifulSoup:
    url = "https://omniplex.ie/cinema/killarney"
    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.content, "html.parser")


def get_cinema_listings(soup_object: BeautifulSoup) -> list[tuple[str, list]]:
    event_wrappers: ResultSet[Tag] = soup_object.find_all("div", class_="rightHolder")
    movie_titles = []
    show_times = []
    for wrapper in event_wrappers:
        title = wrapper.find("h3", class_="OMP_inlineBlock")
        if type(title) == Tag:
            movie_titles.append(title.text)
        times = wrapper.find("div", class_="OMP_list2D")
        show_times.append(__parse_times(str(times)))
    titles_and_times = filter(lambda x: len(x[1]) > 0, zip(movie_titles, show_times))
    return list(titles_and_times)


def create_movie_objects(movie_titles_and_times: list[tuple[str, list]]) -> list[Movie]:
    movies = __filter_movies_before_six_pm(
        [Movie(m[0], m[1]) for m in movie_titles_and_times]
    )
    return movies


def get_movie_rating(title: str) -> str | None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise Exception("API_KEY not set.")

    # Just assume it was released this year
    year = datetime.now().year
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={title}&y={year}"
    response = requests.get(url=url)

    json_response = response.json()
    if type(json_response) != dict:
        return None

    rating = json_response.get("imdbRating")
    return rating


def __parse_times(times_html_string: str) -> list[str]:
    """
    Helper function. Extracts movie times from div.
    """
    time_parser = BeautifulSoup(times_html_string, "html.parser")
    results: ResultSet[Tag] = time_parser.find_all("a", class_="OMP_buttonSelection")
    parsed_times: list[str] = []
    for item in results:
        parsed_time_tag = item.findChild("strong")
        if type(parsed_time_tag) == Tag:
            parsed_times.append(parsed_time_tag.text)
    return parsed_times


def __filter_movies_before_six_pm(movies: list[Movie]) -> list[Movie]:
    filtered_movies = []
    for movie in movies:
        times = movie.get_times()
        new_times: list[str] = []
        for time in times:
            hours, _ = time.split(":")
            if int(hours) > 18:
                new_times.append(time)
        if len(new_times) > 0:
            movie.set_times(new_times)
            filtered_movies.append(movie)
    return filtered_movies
