import logging
from abc import ABC, abstractmethod


class PriceStrategy(ABC):
    """Abstract base class for rental pricing."""
    _instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(PriceStrategy, cls).__new__(cls)
        return cls._instance

    @abstractmethod
    def get_price(self, days: int) -> float:
        """The price of this movie rental."""
        pass

    @abstractmethod
    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""
        pass


class RegularPrice(PriceStrategy):
    """
    Strategy for calculating the price of a regular movie rental.
    """

    def get_price(self, days):
        amount = 2.0
        if days > 2:
            amount += 1.5 * (days - 2)
        return amount

    def get_rental_points(self, days):
        return 1


class NewRelease(PriceStrategy):
    """
    Strategy for calculating the price of a new release movie rental.
    """

    def get_price(self, days):
        return 3 * days

    def get_rental_points(self, days):
        return days


# I don't know why the word Children have an s.
class ChildrensPrice(PriceStrategy):
    """
    Strategy for calculating the price of a children's movie rental.
    """

    def get_price(self, days):
        amount = 1.5
        if days > 3:
            amount += 1.5 * (days - 3)
        return amount

    def get_rental_points(self, days):
        return 1


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
