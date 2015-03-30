from unittest import TestCase, main
from numpy import testing

from src.AbstractFunction import AbstractFunction
from src.RosenbrockFunction import RosenbrockFunction
from src.FrankWolfe import FrankWolfe

from numpy import ndarray, array

class TestFunctions(TestCase):

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_gradient(self):
    class LineFunction(AbstractFunction):
      def get_function(self):
        return lambda x: x[0] + x[1]
    fw = FrankWolfe(LineFunction())
    testing.assert_almost_equal(fw._calculate_gradient([0, 0]), [1, 1])

    fw = FrankWolfe(RosenbrockFunction())
    testing.assert_almost_equal(fw._calculate_gradient([0, 0]), [-2, 0])
    testing.assert_almost_equal(fw._calculate_gradient([1, 1]), [0, 0])

  def test_termination(self):
    class SimpleFunction(AbstractFunction):
      def get_function(self):
        return lambda x: x[0]
    fw = FrankWolfe(SimpleFunction())
    self.assertFalse(fw.termination_criterion([(0,0), (1,0)]))
    self.assertTrue(fw.termination_criterion([(0,0), (0,0)]))

if __name__ == '__main__':
  main()
