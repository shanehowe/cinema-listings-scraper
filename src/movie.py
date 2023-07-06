class Movie:
    def __init__(self, title: str, listing_times: list[str]) -> None:
        self._title = title
        self._times = listing_times
        self._rotten_tomatoes: int | None = None

    def get_rotten_tomato(self) -> int | None:
        return self._rotten_tomatoes

    def set_rotten_tomato(self, rotten_tom_score: int | None) -> None:
        self._rotten_tomatoes = rotten_tom_score

    def get_title(self) -> str:
        return self._title

    def get_times(self) -> list[str]:
        return self._times

    def set_times(self, new_times: list[str]) -> None:
        self._times = new_times

    def to_html(self):
        rotten_tomato_score = (
            self._rotten_tomatoes if self._rotten_tomatoes is not None else "N/A"
        )
        listing_times = "<br>".join(self._times)

        html = f"""
            <div>
                <h2>{self._title}</h2>
                <p>Rotten Tomatoes Score: {rotten_tomato_score}</p>
                <p>Listing Times:<br>{listing_times}</p>
            </div>
        """
        return html

    def __repr__(self) -> str:
        return f"Movie(\ntitle={self._title}\ntimes={self._times}\n🍅={self._rotten_tomatoes}\n)"
