from collections import Collection
from dataclasses import dataclass


@dataclass(frozen=True)
class Movie:
    """
    A movie available for rent.
    """
    title: str
    year: int
    genre: Collection[str]

    def is_genre(self, genre: str) -> bool:
        return genre.lower() in self.genre

    def get_title(self):
        return self.title

    def __str__(self):
        return f"{self.title} ({self.year})"
