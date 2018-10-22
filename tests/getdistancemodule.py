import unittest
from src.railroad import Railroad
from tests import Kiwiland

class GetDistanceModuleTest(unittest.TestCase):
    def setUp(self):
        self.railroad = Kiwiland

    # Testing cases of railroad.get_distance
    def test_empty_route_should_return_no_such_route(self):
        self.assertEqual(self.railroad.get_distance(""), "NO SUCH ROUTE")

    def test_nonexistant_single_step_route_should_return_no_such_route(self):
        self.assertEqual(self.railroad.get_distance("A-C"), "NO SUCH ROUTE")

    def test_existing_single_step_route_should_return_distance(self):
        self.assertAlmostEqual(self.railroad.get_distance("A-B"), 5)

    def test_nonexistant_multiple_step_route_should_return_no_such_route(self):
        self.assertEqual(self.railroad.get_distance("A-B-D"), "NO SUCH ROUTE")

    def test_existing_multiple_step_route_should_return_distance(self):
        self.assertAlmostEqual(self.railroad.get_distance("A-B-C"), 9)

def suite():
    """
    Gather all the GetDistanceModuleTest tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(GetDistanceModuleTest))
    return test_suite
	
if __name__ == '__main__':
    #So you can run tests from this module individually.
    mySuit=suite()

    runner=unittest.TextTestRunner()
    runner.run(mySuit)