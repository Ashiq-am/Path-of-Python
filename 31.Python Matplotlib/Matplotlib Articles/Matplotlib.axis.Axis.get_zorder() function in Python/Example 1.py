# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np
import matplotlib.pyplot as plt

d = np.arange(49).reshape(7, 7)
xx, yy = np.meshgrid(np.arange(8), np.arange(8))

fig, ax = plt.subplots()

ax.set_aspect(1)
ax.pcolormesh(xx, yy, d)

ax.text(2.4, 6.5, "Zorder Value : "
        + str(Axis.get_zorder(ax)),
        fontweight="bold")

fig.suptitle('matplotlib.axis.Axis.get_zorder() \
function Example\n', fontweight="bold")

plt.show()
