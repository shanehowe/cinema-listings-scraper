from bs4 import BeautifulSoup, ResultSet, Tag
from movie import Movie
from pprint import pprint
import requests
import bs4


def get_cinema_soup() -> BeautifulSoup:
    """
    Fetch cinema web page
    :return: BeautifulSoup(web_page)
    """
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
    titles_and_times = filter(lambda x: len(x[1]) >= 0, zip(movie_titles, show_times))
    return list(titles_and_times)


def create_movie_objects(movie_titles_and_times: list[tuple[str, list]]) -> list[Movie]:
    """
    Creates a list of Movies()
    from the list passed in
    """
    movies: list[Movie] = []
    for movie_item in movie_titles_and_times:
        movie = Movie(movie_item[0], movie_item[1])
        movies.append(movie)
    return movies


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


if __name__ == "__main__":
    soup = get_cinema_soup()
    listings = get_cinema_listings(soup)
    movies = create_movie_objects(listings)
    pprint(movies)
