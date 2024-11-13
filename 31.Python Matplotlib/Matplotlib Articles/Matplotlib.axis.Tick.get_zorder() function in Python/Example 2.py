# Implementation of matplotlib function
from matplotlib.axis import Tick
import numpy as np
import matplotlib.pyplot as plt

xx = np.random.rand(3, 4)

fig, ax = plt.subplots()

ax.pcolor(xx)
ax.set_zorder(3)

ax.set_title("Zorder Value : "
             + str(Tick.get_zorder(ax)),
             fontweight="bold")

fig.suptitle('matplotlib.axis.Tick.get_zorder() \
function Example', fontweight="bold")

plt.show()
