from src.FrankWolfe import FrankWolfe
from src.AbstractConstraints import AbstractConstraints

rosenbrock_f = lambda x: ((1-x[0])**2 + 100*(x[1]-x[0]**2)**2)
fw = FrankWolfe(AbstractConstraints(), rosenbrock_f)

print "Output:", fw.find_infimum()
