import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie("Dune: Part Two")
        self.regular_movie = Movie("Air")
        self.children_movie = Movie("Frozen")

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of
        Movie"""
        m = Movie("Air")
        self.assertEqual("Air", m.get_title())

    def test_rental_price(self):
        """test rental price for each movie attribute"""
        # New movies
        rental = Rental(self.new_movie, 1, Rental.NEW_RELEASE)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5, Rental.NEW_RELEASE)
        self.assertEqual(rental.get_price(), 15.0)
        # Regular movies
        rental = Rental(self.regular_movie, 1, Rental.REGULAR)
        self.assertEqual(rental.get_price(), 2.0)
        rental = Rental(self.regular_movie, 5, Rental.REGULAR)
        self.assertEqual(rental.get_price(), 6.5)
        # Children movies
        rental = Rental(self.children_movie, 1, Rental.CHILDREN)
        self.assertEqual(rental.get_price(), 1.5)
        rental = Rental(self.children_movie, 5, Rental.CHILDREN)
        self.assertEqual(rental.get_price(), 4.5)

    def test_rental_points(self):
        """test rental points for each movie type"""
        rental = Rental(self.regular_movie, 1, Rental.REGULAR)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.children_movie, 3, Rental.CHILDREN)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.new_movie, 5, Rental.NEW_RELEASE)
        self.assertEqual(rental.get_rental_points(), 5)
