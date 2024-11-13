# Implementation of matplotlib function


import matplotlib.pyplot as plt
import numpy as np

X, Y = np.meshgrid(np.arange(0, 2 * np.pi, .2),
                   np.arange(0, 2 * np.pi, .2))
U = np.cos(X ** 2)
V = np.sin(Y ** 2)

fig, (ax, ax1) = plt.subplots(nrows=2, ncols=1)
ax.streamplot(X, Y, U, V, density=[0.5, 1],
              color=V * U, linewidth=2,
              cmap='autumn')
val = np.array([[2, 1, 0, 1, 2, 1],
                [2, 1, 0, 1, 2, 2]])

ax1.streamplot(X, Y, U, V, color=V * U, linewidth=2,
               cmap='autumn',
               start_points=val.T)

ax.set_title('matplotlib.axes.Axes.streamplot() \
Example\n', fontsize=14, fontweight='bold')
plt.show()
