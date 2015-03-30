from AbstractConstraints import AbstractConstraints

class SimpleConstraints(AbstractConstraints):
  def __init__(self, lower, higher):
    self.lower = lower
    self.higher = higher

  def get_lower(self):
    return self.lower

  def get_higher(self):
    return self.higher
