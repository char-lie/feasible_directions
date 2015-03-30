import numpy
import math

from AbstractFunction import AbstractFunction
from SimpleConstraints import SimpleConstraints

class HolderTableFunction(AbstractFunction):

  def __init__(self, start_point=[0, 0]):
    self.start_point = start_point
    self.constraints = SimpleConstraints([-10, -10], [10, 10])

  def get_start_point(self):
    return self.start_point

  def get_mesh_XYZ(self, accuracy):
    X = numpy.arange(-10, 10, accuracy)
    Y = numpy.arange(-10, 10, accuracy)
    X, Y = numpy.meshgrid(X, Y)
    Z = - numpy.abs(numpy.sin(X)*numpy.cos(Y)*
                    numpy.exp(numpy.abs(1-numpy.sqrt(X**2+Y**2)/numpy.pi)))
    return [X, Y, Z]

  def get_function(self):
    return lambda x: - abs(math.sin(x[0])*math.cos(x[1])*
                           math.exp(abs(1-math.sqrt(x[0]**2+x[1]**2)/math.pi)))

