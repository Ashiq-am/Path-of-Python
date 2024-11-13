# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

d = np.arange(100).reshape(10, 10)
xx, yy = np.meshgrid(np.arange(11), np.arange(11))

fig, ax = plt.subplots()

ax.set_aspect(1)
ax.pcolormesh(xx, yy, d)

ax.text(3, 9.5, "Zorder Value : "
        + str(ax.get_zorder()),
        fontweight="bold")

fig.suptitle('matplotlib.axes.Axes.get_zorder() \
function Example', fontweight="bold")

plt.show()
