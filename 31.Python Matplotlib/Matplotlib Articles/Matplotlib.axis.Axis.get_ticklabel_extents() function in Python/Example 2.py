# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np
import matplotlib.pyplot as plt

xx = np.random.rand(10, 5)

fig, ax = plt.subplots()

m = ax.pcolor(xx)
m.set_zorder(-2)

w = Axis.get_ticklabel_extents(ax.xaxis, fig.canvas.get_renderer())

print("Value Return :\n" + str(w))
ax.grid()

fig.suptitle("""matplotlib.axis.Axis.get_ticklabel_extents() 
function Example\n""", fontweight="bold")

plt.show()
