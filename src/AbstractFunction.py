from exceptions import NotImplementedError

class AbstractFunction:

  def __init__(self, start_point=None):
    self.start_point = start_point
    self.constraints = None

  def get_start_point(self):
    return self.start_point

  def get_mesh_XYZ(self):
    raise NotImplementedError()

  def get_function(self):
    raise NotImplementedError()

  def __call__(self, x):
    return self.get_function()(x)

  def get_constraints(self):
    return self.constraints

  def get_lower_constraints(self):
    return self.get_constraints().get_lower()

  def get_higher_constraints(self):
    return self.get_constraints().get_higher()
