class Movie:
    def __init__(self, title: str, listing_times: list[str]) -> None:
        self._title = title
        self._times = listing_times
        self._rotten_tomatoes: int | None = None

    def set_rotten_tomatoes(self, rotten_tom_score: int) -> None:
        self._rotten_tomatoes = rotten_tom_score
    
    def get_title(self) -> str:
        return self._title
    
    def get_times(self) -> list[str]:
        return self._times

    def __repr__(self) -> str:
        return f"Movie(title={self._title}\ntimes={self._times})"