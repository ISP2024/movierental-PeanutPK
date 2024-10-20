import unittest
from rental import Rental
from movie import Movie, MovieCatalog


class RentalTest(unittest.TestCase):

    def setUp(self):
        catalog = MovieCatalog()
        self.new_movie = catalog.get_movie("Dune: Part Two")
        self.regular_movie = Movie("Air", 2023, ["Drama", "Sport"])
        self.children_movie = Movie("Frozen", 2013, ["Children", "Comedy"])

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of
        Movie"""
        m = Movie("Air", 2023, ["Drama", "Sport"])
        self.assertEqual("Air", m.get_title())
        self.assertEqual(2023, m.year)
        self.assertIn("Drama", m.genre)

    def test_rental_price(self):
        """test rental price for each movie attribute"""
        # New movies
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(), 15.0)
        # Regular movies
        rental = Rental(self.regular_movie, 1)
        self.assertEqual(rental.get_price(), 2.0)
        rental = Rental(self.regular_movie, 5)
        self.assertEqual(rental.get_price(), 6.5)
        # Children movies
        rental = Rental(self.children_movie, 1)
        self.assertEqual(rental.get_price(), 1.5)
        rental = Rental(self.children_movie, 5)
        self.assertEqual(rental.get_price(), 4.5)

    def test_rental_points(self):
        """test rental points for each movie type"""
        rental = Rental(self.regular_movie, 1)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.children_movie, 3)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_rental_points(), 5)

    def test_catalog(self):
        """Test for MovieCatalog class"""
        # SingleTon test
        catalog = MovieCatalog()
        catalog2 = MovieCatalog()
        self.assertEqual(catalog2, catalog)

        # load data test
        cinderella = catalog.get_movie("Cinderella")
        self.assertEqual(cinderella, catalog.get_movie("Cinderella"))
        self.assertEqual(cinderella.year, 1950)
        self.assertIn("Animation", cinderella.genre)
