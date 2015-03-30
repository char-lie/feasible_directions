class AbstractConstraints:
  """
  Abstract class for representing constraints.
  """

  def __init__(self):
    """
    Init constraints.
    """
    pass

  def point_fits_constraints(self, point):
    """
    Check wether point fits constraints or not.
    """
    raise NotImplementedError
