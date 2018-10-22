import unittest
from src.railroad import Railroad
from tests import Kiwiland

class DijkstrasModuleTest(unittest.TestCase):
    def setUp(self):
        self.railroad = Kiwiland

    # Testing cases of railroad.get_shortest_distance
    def test_route_to_self_should_not_automatically_return_zero_distance(self):
        self.assertEqual(self.railroad.get_shortest_distance("D", "D"), 16)

    def test_shortest_dist_to_unreachable_destination_should_return_no_such_route(self):
        self.assertEqual(self.railroad.get_shortest_distance("C", "A"), "NO SUCH ROUTE")

    def test_direct_connection_shortest_should_return_direct_distance(self):
        self.assertEqual(self.railroad.get_shortest_distance("A", "B"), 5)

    def test_indirect_connection_shortest_should_return_indirect_distance(self):
        self.assertEqual(self.railroad.get_shortest_distance("A", "E"), 7)

    def test_two_routes_tie_should_return_correct_distance(self):
        self.assertEqual(self.railroad.get_shortest_distance("A", "C"), 9)

def suite():
    """
    Gather all the DijkstrasModuleTest tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(DijkstrasModuleTest))
    return test_suite

if __name__ == '__main__':
    #So you can run tests from this module individually.
    mySuit=suite()

    runner=unittest.TextTestRunner()
    runner.run(mySuit)