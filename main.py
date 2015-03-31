from sys import argv

from src.FrankWolfe import FrankWolfe
from src.RosenbrockFunction import RosenbrockFunction
from src.HimmelblauFunction import HimmelblauFunction
from src.HolderTableFunction import HolderTableFunction

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.lines import Line2D
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt

functions = list()
functions.append(RosenbrockFunction([0, 3]))
functions.append(HimmelblauFunction([0, 0]))
functions.append(HolderTableFunction([0, 0]))

if __name__ == '__main__':

  function_number = 0
  accuracy = .25

  current_f = functions[function_number]

  try:
    if len(argv) > 1:
      function_number = int(argv[1])
      current_f = functions[function_number]
    if len(argv) > 2:
      accuracy = float(argv[2])
  except Exception:
    print "USAGE: {program} [0<=function_number<={last_func}] [acc]".format(
          program=argv[0], last_func=len(functions)-1, acc="accuracy")
    exit(1)

  current_f = functions[function_number]

  fw = FrankWolfe(current_f)
  res = fw.find_infimum()

  fig = plt.figure()
  ax = Axes3D(fig, azim = -29, elev = 49)
  X, Y, Z = current_f.get_mesh_XYZ(accuracy)
  #ax.plot_surface(X, Y, Z, rstride=1, cstride=1, norm=LogNorm(), cmap=cm.jet)
  ax.plot_wireframe(X, Y, Z, rstride=1, cstride=1, norm=LogNorm(), cmap=cm.jet)

  lines_x = list()
  lines_y = list()
  lines_z = list()
  for r in res:
    lines_x.append(r[0])
    lines_y.append(r[1])
    lines_z.append(current_f(r))
  plt.plot(lines_x, lines_y, lines_z, 'kD--', linewidth=2)

  start_point = res[0]
  finish_point = res[-1]
  ax.text(start_point[0], start_point[1], current_f(res[0]), "Start",
          fontsize=20)
  ax.text(finish_point[0], finish_point[1], current_f(res[-1]), "Finish",
          fontsize=20)

  plt.xlabel("x")
  plt.ylabel("y")
     
  plt.show()
