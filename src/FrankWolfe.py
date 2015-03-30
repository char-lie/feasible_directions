from src.AbstractFeasibleDirectionsDescender import *

from scipy.misc import derivative
from scipy.optimize import line_search

from numpy import subtract, ndarray, array, add
from numpy.linalg import norm

from pulp import *


class FrankWolfe(AbstractFeasibleDirectionsDescender):
  EPSILON = 1E-5

  def _get_gradient_function(self):
    def grad(x):
      try:
        x = x.tolist()
      except:
        pass
      result = list()
      for i in range(len(x)):
        df = lambda y: self.function(x[:i] + [y] + x[i+1:])
        result.append(derivative(df, x[i], 1e-8))
      return result
    return grad

  def _calculate_gradient(self, x):
    return self._get_gradient_function()(x)
  
  def get_start_point(self):
    """
    Get start point for descend algorithm.
    """
    return self.function.get_start_point()

  def get_descent_direction(self, current_x):
    """
    Determine feasible descent search direction from the point current_x.
    Direction is feasible if there is a scalar step > 0, such that
    f (x + t * direction ) fits constraints for all 0 < t <= step.
    """
    grad = self._calculate_gradient(current_x)
    y = list()
    for i in range(len(current_x)):
      y.append(LpVariable("y"+str(i), self.function.get_lower_constraints()[i],
                                      self.function.get_higher_constraints()[i]))
    prob = LpProblem("problem", LpMinimize)
    for i in range(len(current_x)):
      prob += y[i]>=self.function.get_lower_constraints()[i]
    prob += (y[0]-current_x[0]) * grad[0] + (y[1]-current_x[1]) * grad[1]

    status = prob.solve(GLPK(msg=0))
    LpStatus[status]

    return [value(y[0])-current_x[0], value(y[1])-current_x[1]]

  def get_step_length(self, x, direction):
    """
    Determine step length for the next step of descend algorithm such that
    f(x + step * direction) < f(x) and
    self._fits_constraints(x + step * direction) is True
    """
    iterations_number = 1000
    current_pair = (self.function(x), x, 0)
    min_pair = (self.function(x), x, 0)
    for alpha in range(iterations_number):
      cur_x = add(x, multiply(direction, (alpha+1.0)/iterations_number)).tolist()
      cur_f = self.function(cur_x)
      if cur_f < min_pair[0]:
        min_pair = (cur_f, cur_x, alpha+1)
    return (min_pair[2]*1.0)/iterations_number

  def termination_criterion(self, x):
    """
    Check wether algorithm is needed to be terminated.
    """
    if len(x) < 2:
      return False
    else:
      return norm(subtract(x[-1], x[-2])) < self.EPSILON
