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
        catalog.get_movie("Air"),
        catalog.get_movie("Oppenheimer"),
        catalog.get_movie("Frozen"),
        catalog.get_movie("Bitconned"),
        catalog.get_movie("Particle Fever")
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    index = 0
    price_code = [Rental.NEW_RELEASE, Rental.REGULAR, Rental.CHILDREN]
    for movie in make_movies():
        if movie:
            customer.add_rental(Rental(movie, days, price_code[index % 3]))
        else:
            log = logging.getLogger("MovieFinder")
            log.info("Movie not found")
        days = (days + 2) % 5 + 1
        index += 1
    print(customer.statement())
