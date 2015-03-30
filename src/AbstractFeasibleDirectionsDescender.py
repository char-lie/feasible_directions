from exceptions import NotImplementedError, ValueError

from numpy import add, multiply, divide
from numpy.linalg import norm

from AbstractFunction import AbstractFunction

class AbstractFeasibleDirectionsDescender:
  """
  Abstract class for feasible direction descend optimization method.
  """

  def __init__(self, function = None):
    """
    Initialize descender with differentialbe function R^n -> R
    and constraints.
    """
    if not isinstance(function, AbstractFunction):
      raise ValueError("Parameter {param} should be instance of {classname}," +
                       " but it has type {actual_type}".format(
                          param="function", classname="AbstractFunction",
                          actual_type=type(function)))
    self.function = function

  def _normalize(self, vector):
    """
    Normalize vector: divide it by its norm.
    """
    return divide(vector, norm(vector))

  def _point_fits_constraints(self, point):
    """
    Check wether point fits set constraints or not.
    """
    return self.constraints.point_fits_constraints(point)

  def get_start_point(self):
    """
    Get start point for descend algorithm.
    """
    raise NotImplementedError

  def get_descent_direction(self, current_x):
    """
    Determine feasible descent search direction from the point current_x.
    Direction is feasible if there is a scalar step > 0, such that
    f (x + t * direction ) fits constraints for all 0 < t <= step.
    """
    raise NotImplementedError

  def get_step_length(self, x, direction):
    """
    Determine step length for the next step of descend algorithm such that
    f(x + step * direction) < f(x) and
    self._fits_constraints(x + step * direction) is True
    """
    raise NotImplementedError

  def termination_criterion(self, x):
    """
    Check wether algorithm is needed to be terminated.
    """
    raise NotImplementedError

  def find_infimum(self):
    """
    Find infimum.
    Algorithm of feasible directions descend.
    """
    # Step 0 (Initialization)
    x = [self.get_start_point()]
    k = 0
    current_x = x[0]
    # Step 1 (Termination check)
    while not self.termination_criterion(x):
      # Step 2 (Direction determination)
      #direction = self._normalize(self.get_descent_direction(current_x))
      direction = self.get_descent_direction(current_x)
      # Step 3 (Step length determination)
      step_length = self.get_step_length(current_x, direction)
      # Step 4 (Update)
      #print current_x, x[-1], direction, step_length
      #print "x", current_x, "direction", direction, "step", step_length
      current_x = add(x[-1], multiply(direction, step_length)).tolist()
      x.append(current_x)
      k += 1
    # Output
    return x
