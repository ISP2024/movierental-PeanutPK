import re
import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class CustomerTest(unittest.TestCase):
    """ Tests of the Customer class"""

    def setUp(self):
        """Test fixture contains:

        c = a customer
        movies = list of some movies
        """
        self.c = Customer("Movie Mogul")
        self.new_movie = Movie("Mulan", Movie.NEW_RELEASE)
        self.regular_movie = Movie("CitizenFour", Movie.REGULAR)
        self.childrens_movie = Movie("Frozen", Movie.CHILDRENS)

    def test_billing(self):
        """test for computing total charges"""
        self.c.add_rental(Rental(self.new_movie, 5))
        self.c.add_rental(Rental(self.childrens_movie, 4))
        # new movie 15.0 + children 3.0
        self.assertEqual(self.c.get_billing(), 18.0)

        self.c.add_rental(Rental(self.new_movie, 5))
        self.c.add_rental(Rental(self.childrens_movie, 4))
        # new movie 15.0 + children 3.0 + old charges
        self.assertEqual(self.c.get_billing(), 36.0)

    def test_statement(self):
        stmt = self.c.statement()
        # get total charges from statement using a regex
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.match(pattern, stmt, flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])
        # add a rental
        self.c.add_rental(Rental(self.new_movie, 4))  # days
        stmt = self.c.statement()
        matches = re.match(pattern, stmt.replace('\n', ''), flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])
