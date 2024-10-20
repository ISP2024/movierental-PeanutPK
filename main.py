# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.
import logging

from movie import Movie, MovieCatalog
from rental import Rental
from customer import Customer


def make_movies():
    """Some sample movies."""
    catalog = MovieCatalog()
    movies = [
        Movie("Air", 2024, ["Drama", "Sport"]),
        catalog.get_movie("Oppenheimer"),
        Movie("Frozen", 2013, ["Comedy", "Children"]),
        catalog.get_movie("Bitconned"),
        catalog.get_movie("Particle Fever")
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        if movie:
            customer.add_rental(Rental(movie, days))
        else:
            log = logging.getLogger("MovieFinder")
            log.info("Movie not found")
        days = (days + 2) % 5 + 1
    print(customer.statement())
