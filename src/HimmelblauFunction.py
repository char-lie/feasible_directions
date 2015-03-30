import numpy

from AbstractFunction import AbstractFunction
from SimpleConstraints import SimpleConstraints

class HimmelblauFunction(AbstractFunction):

  def __init__(self, start_point=[0, 0]):
    self.start_point = start_point
    self.constraints = SimpleConstraints([-6, -6], [6, 6])

  def get_start_point(self):
    return self.start_point

  def get_mesh_XYZ(self, accuracy):
    X = numpy.arange(-6, 6, accuracy)
    Y = numpy.arange(-6, 6, accuracy)
    X, Y = numpy.meshgrid(X, Y)
    Z = (X*X+Y-11)**2 + (X+Y*Y-7)**2
    return [X, Y, Z]

  def get_function(self):
    return lambda x: ((x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2)

