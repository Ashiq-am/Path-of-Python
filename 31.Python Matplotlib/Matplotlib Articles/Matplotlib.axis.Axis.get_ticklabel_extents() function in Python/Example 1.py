# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
import numpy as np

X = np.arange(-5, 5, 1)
Y = np.arange(-5, 5, 1)
U, V = np.meshgrid(X, Y)

fig, ax = plt.subplots()
ax.quiver(X, Y, U, V)
ax.invert_xaxis()
w = Axis.get_ticklabel_extents(ax.xaxis,
                               fig.canvas.get_renderer())

print("Value Return :\n" + str(w))
ax.grid()

fig.suptitle("""matplotlib.axis.Axis.get_ticklabel_extents() 
function Example\n""", fontweight="bold")

plt.show()
