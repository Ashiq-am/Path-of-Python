# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

X, Y = np.meshgrid(np.arange(0, 2 * np.pi, .2),
                   np.arange(0, 2 * np.pi, .2))
U = np.cos(X ** 2)
V = np.sin(Y ** 2)

fig, ax = plt.subplots()
ax.streamplot(X, Y, U, V, density=[0.5, 1])

ax.set_title('matplotlib.axes.Axes.streamplot()\
Example\n', fontsize=14, fontweight='bold')
plt.show()
