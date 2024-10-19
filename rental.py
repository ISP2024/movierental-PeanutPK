import logging
from pricing import RegularPrice, NewRelease, ChildrensPrice


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    For simplicity of this application only days_rented is recorded.
    """
    # The types of movies (price_code).
    REGULAR = RegularPrice()
    NEW_RELEASE = NewRelease()
    CHILDREN = ChildrensPrice()

    def __init__(self, movie, days_rented, price_code):
        """Initialize a new movie rental object for
           a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented
        self.price_code = price_code

    def get_price(self):
        """Return a calculated price for a rental."""
        amount = 0
        try:
            amount = self.get_price_code().get_price(self.days_rented)
        except AttributeError:
            log = logging.getLogger()
            log.error(f"Movie {self} has unrecognized priceCode "
                      f"{self.get_price_code()}")
        return amount

    def get_price_code(self):
        # get the price code
        return self.price_code

    def get_rental_points(self):
        # compute the frequent renter points based on movie price code
        if self.get_price_code() == self.NEW_RELEASE:
            # New release earns 1 point per day rented
            return self.days_rented
        else:
            # Other rentals get only 1 point
            return 1

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented
