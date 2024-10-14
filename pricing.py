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
