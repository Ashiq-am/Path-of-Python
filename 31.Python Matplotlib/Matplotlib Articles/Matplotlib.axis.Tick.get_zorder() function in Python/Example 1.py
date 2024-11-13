# Implementation of matplotlib function
from matplotlib.axis import Tick
import numpy as np
import matplotlib.pyplot as plt

d = np.arange(16).reshape(4, 4)
xx, yy = np.meshgrid(np.arange(5), np.arange(5))

fig, ax = plt.subplots()

ax.set_aspect(1)
ax.pcolormesh(xx, yy, d)

ax.text(1.4, 3.5, "Zorder Value : "
        + str(Tick.get_zorder(ax)),
        fontweight="bold")

fig.suptitle('matplotlib.axis.Tick.get_zorder() \
function Example', fontweight="bold")

plt.show()
