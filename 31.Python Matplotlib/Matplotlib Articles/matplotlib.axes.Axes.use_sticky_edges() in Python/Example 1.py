# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

y, x = np.mgrid[:6, 1:6]
poly_coords = [
	(0.25, 2.75), (3.25, 2.75),
	(2.25, 0.75), (0.25, 0.75)
]
fig, ax = plt.subplots()

ax.use_sticky_edges = False

ax.pcolor(x, y, y + 20 * x, cmap ='Greens')

ax.margins(x = 0.1, y = 0.05)
ax.set_aspect('equal')

fig.suptitle('matplotlib.axes.Axes.use_sticky_edges() function Example\n', fontweight ="bold")
fig.canvas.draw()
plt.show()
