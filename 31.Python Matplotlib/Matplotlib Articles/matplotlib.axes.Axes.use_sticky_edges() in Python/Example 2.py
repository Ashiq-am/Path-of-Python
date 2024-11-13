# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

y, x = np.mgrid[:6, 1:6]
poly_coords = [
    (0.25, 2.75), (3.25, 2.75),
    (2.25, 0.75), (0.25, 0.75)
]
fig, (ax1, ax2) = plt.subplots(nrows=2)

ax2.use_sticky_edges = False

for ax, status in zip((ax1, ax2),
                      ('Is', 'Is Not')):
    # sticky
    cells = ax.pcolor(x, y, x + y,
                      cmap='PuBuGn')
    ax.add_patch(
        plt.Polygon(poly_coords, color='green',
                    alpha=0.5)
    )  # not sticky
    ax.margins(x=0.1, y=0.05)
    ax.set_aspect('equal')
    ax.set_title('use_sticky_edges() function {} used'.format(status),
                 fontweight="bold")

fig.suptitle('matplotlib.axes.Axes.use_sticky_edges() function \
Example\n', fontweight="bold")
fig.canvas.draw()
plt.show()
