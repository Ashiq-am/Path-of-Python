# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

dx, dy = 0.015, 0.05
x = np.arange(-4.0, 4.0, dx)
y = np.arange(-4.0, 4.0, dy)
X, Y = np.meshgrid(x, y)

extent = np.min(x), np.max(x), np.min(y), np.max(y)

fig, ax = plt.subplots()

Z1 = np.add.outer(range(8), range(8)) % 2
ax.imshow(Z1, cmap="binary_r",
          interpolation='nearest',
          extent=extent, alpha=1)


def geeks(x, y):
    return (1 - x / 2 + x ** 5 + y ** 6) * np.exp(-(x ** 2 + y ** 2))


Z2 = geeks(X, Y)

ax.imshow(Z2, cmap="Greens", alpha=0.7,
          interpolation='bilinear',
          extent=extent)

print("List of the Axes images contained by the Axes \n",
      *list(ax.get_images()), sep="\n")

fig.suptitle('matplotlib.axes.Axes.get_images() function\
Example', fontweight="bold")
plt.show()
