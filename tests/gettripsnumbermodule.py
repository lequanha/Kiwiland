import unittest
from src.railroad import Railroad
from tests import Kiwiland

class GetTripsNumberModuleTest(unittest.TestCase):
    def setUp(self):
        self.railroad = Kiwiland

    # Testing cases of railroad.get_number_of_possible_trips
    def test_number_trips_max_stops_with_missing_connection_should_return_zero(self):
        self.assertEqual(self.railroad.get_number_of_possible_trips("A", "A", 3, Railroad.TripType.max_stops), 0)

    def test_number_trips_max_stops_with_valid_routes_should_return_number(self):
        self.assertEqual(self.railroad.get_number_of_possible_trips("E", "D", 5, Railroad.TripType.max_stops), 2)

    def test_number_trips_max_stops_with_too_small_stops_should_return_zero(self):
        self.assertEqual(self.railroad.get_number_of_possible_trips("E", "D", 2, Railroad.TripType.max_stops), 0)

    def test_number_trips_exact_stops_with_missing_connection_should_return_zero(self):
        self.assertEqual(self.railroad.get_number_of_possible_trips("A", "A", 3, Railroad.TripType.exact_stops), 0)

    def test_number_trips_exact_stops_with_valid_routes_should_return_number(self):
        self.assertEqual(self.railroad.get_number_of_possible_trips("A", "C", 2, Railroad.TripType.exact_stops), 2)

    def test_number_trips_exact_stops_with_no_matches_should_return_zero(self):
        self.assertEqual(self.railroad.get_number_of_possible_trips("E", "D", 4, Railroad.TripType.exact_stops), 0)

    # Testing cases of railroad.get_number_of_possible_trips_to_maximum_distance
    def test_num_routes_of_less_than_zero_distance_should_return_zero(self):
        self.assertEqual(self.railroad.get_number_of_possible_trips_to_maximum_distance("E", "B", 0), 0)

    def test_num_routes_to_unreachable_city_should_return_zero(self):
        self.assertEqual(self.railroad.get_number_of_possible_trips_to_maximum_distance("E", "A", 100), 0)

    def test_num_routes_of_complex_path_should_return_five(self):
        self.assertEqual(self.railroad.get_number_of_possible_trips_to_maximum_distance("A", "C", 19), 5)

def suite():
    """
    Gather all the GetTripsNumberModuleTest tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(GetTripsNumberModuleTest))
    return test_suite

if __name__ == '__main__':
    #So you can run tests from this module individually.
    mySuit=suite()

    runner=unittest.TextTestRunner()
    runner.run(mySuit)