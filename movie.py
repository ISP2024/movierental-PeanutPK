import csv
import logging
from typing import Collection, Optional
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


class MovieCatalog:
    """
    A movie catalog contains a collection of movies from csv files.
    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MovieCatalog, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.movies = []
        self.load_movies()

    def load_movies(self):
        with open('movies.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)

            for row in reader:
                if '#id' == row[0]:
                    continue
                try:
                    title = row[1]
                    year = int(row[2])
                    genre = row[3].split('|')
                except (IndexError, ValueError):
                    log = logging.getLogger('MovieCatalog')
                    log.error(f"Unrecognized format {row}")
                self.movies.append(Movie(title=title, year=year, genre=genre))

    def get_movie(self, title: str, year: Optional[int] = None) -> Movie:
        for movie in self.movies:
            if (movie.get_title().lower() == title.lower() and
                    (movie.year == year or year is None)):
                return movie

