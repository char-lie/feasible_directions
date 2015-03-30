from unittest import TestCase, main
from numpy import testing

from src.AbstractConstraints import AbstractConstraints
from src.FrankWolfe import FrankWolfe

from numpy import ndarray, array

class TestFunctions(TestCase):

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_gradient(self):
    fw = FrankWolfe(AbstractConstraints(), lambda x: x[0] + x[1])
    testing.assert_almost_equal(fw._calculate_gradient([0, 0]), [1, 1])

    rosenbrock_f = lambda x: ((1-x[0])**2 + 100*(x[1]-x[0]**2)**2)
    fw = FrankWolfe(AbstractConstraints(), rosenbrock_f)
    testing.assert_almost_equal(fw._calculate_gradient([0, 0]), [-2, 0])
    testing.assert_almost_equal(fw._calculate_gradient([1, 1]), [0, 0])

  def test_termination(self):
    fw = FrankWolfe(AbstractConstraints(), lambda x: x[0])
    self.assertFalse(fw.termination_criterion([(0,0), (1,0)]))
    self.assertTrue(fw.termination_criterion([(0,0), (0,0)]))

if __name__ == '__main__':
  main()
