from unittest import TestCase, main

from numpy.linalg import norm

from src.AbstractFeasibleDirectionsDescender import *
from src.AbstractConstraints import AbstractConstraints

class TestFunctions(TestCase):

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_default_constructor(self):
    with self.assertRaises(ValueError):
      ffd = AbstractFeasibleDirectionsDescender()

  def test_constructor(self):
    function = lambda x: x
    constraints = AbstractConstraints()
    ffd = AbstractFeasibleDirectionsDescender(constraints, function)
    self.assertIsInstance(ffd, AbstractFeasibleDirectionsDescender)
    self.assertEqual(ffd.function, function)
    self.assertEqual(ffd.constraints, constraints)

  def test_normalize(self):
    ffd = AbstractFeasibleDirectionsDescender(AbstractConstraints())
    v = (1, 1)
    v_norm = norm(v)
    self.assertNotAlmostEqual(v_norm, 1)
    normalized_v = ffd._normalize(v)
    self.assertAlmostEqual(norm(normalized_v), 1)
    self.assertAlmostEqual(normalized_v[0] * v_norm, v[0])
    self.assertAlmostEqual(normalized_v[1] * v_norm, v[1])

  def test_not_implemented(self):
    ffd = AbstractFeasibleDirectionsDescender(AbstractConstraints())
    with self.assertRaises(NotImplementedError):
      ffd.get_start_point()
    with self.assertRaises(NotImplementedError):
      ffd.get_descent_direction((0, 0))
    with self.assertRaises(NotImplementedError):
      ffd.get_step_length((0,0), (0,0))
    with self.assertRaises(NotImplementedError):
      ffd.termination_criterion([(0,0)], 0)

if __name__ == '__main__':
  main()
