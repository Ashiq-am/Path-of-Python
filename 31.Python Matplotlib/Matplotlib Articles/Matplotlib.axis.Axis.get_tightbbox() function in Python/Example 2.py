# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np
import matplotlib.pyplot as plt

xx = np.random.rand(8, 6)

fig, ax = plt.subplots()

m = ax.pcolor(xx)
m.set_zorder(-2)
w = Axis.get_tightbbox(ax.xaxis, fig.canvas.get_renderer())

print("Value Return :\n" + str(w))
ax.grid()

fig.suptitle("""matplotlib.axis.Axis.get_tightbbox() 
function Example\n""", fontweight="bold")

plt.show()
