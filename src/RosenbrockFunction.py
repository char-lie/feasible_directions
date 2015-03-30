import numpy

from AbstractFunction import AbstractFunction
from SimpleConstraints import SimpleConstraints

class RosenbrockFunction(AbstractFunction):

  def __init__(self, start_point=[0, 0]):
    self.start_point = start_point
    self.constraints = SimpleConstraints([-3, -3], [3, 3])

  def get_start_point(self):
    return self.start_point

  def get_mesh_XYZ(self, accuracy):
    X = numpy.arange(-2, 2.+accuracy, accuracy)
    Y = numpy.arange(-1, 3.+accuracy, accuracy)
    X, Y = numpy.meshgrid(X, Y)
    Z = (1.-X)**2 + 100.*(Y-X*X)**2
    return [X, Y, Z]

  def get_function(self):
    return lambda x: ((1-x[0])**2 + 100*(x[1]-x[0]**2)**2)
