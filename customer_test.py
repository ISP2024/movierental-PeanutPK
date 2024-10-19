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
        self.new_movie = Movie("Mulan")
        self.regular_movie = Movie("CitizenFour")
        self.children_movie = Movie("Frozen")

    def test_billing(self):
        """test for computing total charges"""
        self.c.add_rental(Rental(self.new_movie, 5, Rental.NEW_RELEASE))
        self.c.add_rental(Rental(self.children_movie, 4, Rental.CHILDREN))
        # new movie 15.0 + children 3.0
        self.assertEqual(self.c.get_billing(), 18.0)

        self.c.add_rental(Rental(self.new_movie, 5, Rental.NEW_RELEASE))
        self.c.add_rental(Rental(self.children_movie, 4, Rental.CHILDREN))
        # new movie 15.0 + children 3.0 + old charges
        self.assertEqual(self.c.get_billing(), 36.0)

    def test_frequent_rental(self):
        """test for computing frequency of rental"""
        self.c.add_rental(Rental(self.new_movie, 5, Rental.NEW_RELEASE))
        self.c.add_rental(Rental(self.children_movie, 4, Rental.CHILDREN))
        self.c.add_rental(Rental(self.new_movie, 5, Rental.NEW_RELEASE))
        # 2 new movies rented for 5 days and one of the other categories
        self.assertEqual(self.c.get_rentals(), 11)

        self.c.add_rental(Rental(self.regular_movie, 5, Rental.REGULAR))
        self.c.add_rental(Rental(self.new_movie, 5, Rental.NEW_RELEASE))
        # 1 new movie and 1 regular movie
        self.assertEqual(self.c.get_rentals(), 17)

    def test_statement(self):
        stmt = self.c.statement()
        # get total charges from statement using a regex
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.match(pattern, stmt, flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])
        # add a rental
        self.c.add_rental(Rental(self.new_movie, 4, Rental.NEW_RELEASE))  # days
        stmt = self.c.statement()
        matches = re.match(pattern, stmt.replace('\n', ''), flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])
