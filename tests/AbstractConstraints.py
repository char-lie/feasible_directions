from unittest import TestCase, main

from numpy.linalg import norm

from src.AbstractConstraints import AbstractConstraints

class TestFunctions(TestCase):

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_constructor(self):
    constraints = AbstractConstraints()
    self.assertIsInstance(constraints, AbstractConstraints)

  def test_not_implemented(self):
    constraints = AbstractConstraints()
    with self.assertRaises(NotImplementedError):
      constraints.point_fits_constraints(None)

if __name__ == '__main__':
  main()
