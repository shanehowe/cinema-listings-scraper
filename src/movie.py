class Movie:
    def __init__(self, title: str, listing_times: list[str]) -> None:
        self._title = title
        self._times = listing_times
        self._rating: str | None = None

    def get_rating(self) -> str | None:
        return self._rating

    def set_rating(self, rating: str | None) -> None:
        self._rating = rating

    def get_title(self) -> str:
        return self._title

    def get_times(self) -> list[str]:
        return self._times

    def set_times(self, new_times: list[str]) -> None:
        self._times = new_times

    def to_html(self):
        listing_times = ", ".join(self._times)
        if self._rating is None:
            rating = "N/A"
        else:
            rating = self._rating

        html = f"""
            <div class="container">
                <h3>{self._title}</h3>
                <p>IMDB rating ⭐️: {rating}</p>
                <p>Listing Times ⏰: {listing_times}</p>
            </div>
        """
        return html

    def __repr__(self) -> str:
        return f"Movie(\ntitle={self._title}\ntimes={self._times}\n)"
