import logging
from pricing import RegularPrice, NewRelease, ChildrensPrice


class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code). 
    REGULAR = RegularPrice()
    NEW_RELEASE = NewRelease()
    CHILDRENS = ChildrensPrice()

    def __init__(self, title, price_code):
        # Initialize a new movie. 
        self.title = title
        self.price_code = price_code

    def get_rental_points(self, days):
        if self.get_price_code() == self.NEW_RELEASE:
            # New release earns 1 point per day rented
            return days
        else:
            # Other rentals get only 1 point
            return 1

    def get_price(self, days):
        """Return a calculated price for a rental."""
        amount = 0
        try:
            amount = self.get_price_code().get_price(days)
        except AttributeError:
            log = logging.getLogger()
            log.error(
                f"Movie {self} has unrecognized priceCode {self.get_price_code()}")
        return amount

    def get_price_code(self):
        # get the price code
        return self.price_code

    def get_title(self):
        return self.title

    def __str__(self):
        return self.title
