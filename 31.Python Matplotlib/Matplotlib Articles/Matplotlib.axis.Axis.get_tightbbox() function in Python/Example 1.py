# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
import numpy as np

X = np.arange(-10, 10, 0.5)
Y = np.arange(-10, 10, 0.5)
U, V = np.meshgrid(X, Y)

fig, ax = plt.subplots()
ax.quiver(X, Y, U, V)
ax.invert_xaxis()
w = Axis.get_tightbbox(ax.xaxis, fig.canvas.get_renderer())

print("Value Return :\n" + str(w))
ax.grid()

fig.suptitle("""matplotlib.axis.Axis.get_tightbbox() 
function Example\n""", fontweight="bold")

plt.show()
