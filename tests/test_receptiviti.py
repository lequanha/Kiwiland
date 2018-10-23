import unittest
from src.railroad import Railroad
from tests import Kiwiland

class ReceptivitiTest(unittest.TestCase):
    def setUp(self):
        self.railroad = Kiwiland

    # Default tests
    """
    1. The distance of the route A-B-C.
    2. The distance of the route A-D.
    3. The distance of the route A-D-C.
    4. The distance of the route A-E-B-C-D.
    5. The distance of the route A-E-D.
    6. The number of trips starting at C and ending at C with a maximum of 3 stops.  In the sample data below, there are two such trips: C-D-C (2 stops). and C-E-B-C (3 stops).
    7. The number of trips starting at A and ending at C with exactly 4 stops. In the sample data below, there are three such trips: A to C (via B,C,D); A to C (via D,C,D); and A to C (via D,E,B).
    8. The length of the shortest route (in terms of distance to travel) from A to C.
    9. The length of the shortest route (in terms of distance to travel) from B to B.
    10. The number of different routes from C to C with a distance of less than 30. In the sample data, the trips are: CDC, CEBC, CEBCDC, CDCEBC, CDEBC, CEBCEBC, CEBCEBCEBC.
    """
    def test_01(self):
        self.assertAlmostEqual(self.railroad.get_distance("A-B-C"), 9)

    def test_02(self):
        self.assertAlmostEqual(self.railroad.get_distance("A-D"), 5)

    def test_03(self):
        self.assertAlmostEqual(self.railroad.get_distance("A-D-C"), 13)

    def test_04(self):
        self.assertAlmostEqual(self.railroad.get_distance("A-E-B-C-D"), 22)

    def test_05(self):
        self.assertEqual(self.railroad.get_distance("A-E-D"), "NO SUCH ROUTE")

    def test_06(self):
        self.assertEqual(self.railroad.get_number_of_possible_trips("C", "C", 3, Railroad.TripType.max_stops), 2)

    def test_07(self):
        self.assertEqual(self.railroad.get_number_of_possible_trips("A", "C", 4, Railroad.TripType.exact_stops), 3)

    def test_08(self):
        self.assertEqual(self.railroad.get_shortest_distance("A", "C"), 9)

    def test_09(self):
        self.assertEqual(self.railroad.get_shortest_distance("B", "B"), 9)

    def test_10(self):
        self.assertEqual(self.railroad.get_number_of_possible_trips_to_maximum_distance("C", "C", 30), 7)

def suite():
    """
    Gather all the Insight Global tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(ReceptivitiTest))
    return test_suite

if __name__ == '__main__':
    #So you can run tests from this module individually.
    mySuit=suite()

    runner=unittest.TextTestRunner()
    runner.run(mySuit)
