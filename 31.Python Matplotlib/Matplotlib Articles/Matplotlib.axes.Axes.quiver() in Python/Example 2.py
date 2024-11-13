# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

X, Y = np.meshgrid(np.arange(0, 2 * np.pi, .2),
                   np.arange(0, 2 * np.pi, .2))
U = np.cos(X ** 2)
V = np.sin(Y ** 2)
C = U ** 2 + V ** 2

fig, ax = plt.subplots()
ax.quiver(X, Y, U, V, C, units='width')
ax.set_title('matplotlib.axes.Axes.quiver() \
Example', fontsize=14, fontweight='bold')
plt.show()
