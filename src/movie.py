class Movie:
    def __init__(self, title: str, listing_times: list[str]) -> None:
        self._title = title
        self._times = listing_times

    def get_title(self) -> str:
        return self._title

    def get_times(self) -> list[str]:
        return self._times

    def set_times(self, new_times: list[str]) -> None:
        self._times = new_times

    def to_html(self):
        listing_times = ", ".join(self._times)

        html = f"""
            <div>
                <h3>{self._title}</h3>
                <p>Listing Times ⏰: {listing_times}</p>
            </div>
        """
        return html

    def __repr__(self) -> str:
        return f"Movie(\ntitle={self._title}\ntimes={self._times}\n)"
