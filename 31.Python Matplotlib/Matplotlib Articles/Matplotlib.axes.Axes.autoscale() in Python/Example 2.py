# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import EllipseCollection

x = np.arange(10)
y = np.arange(15)
X, Y = np.meshgrid(x, y)

XY = np.column_stack((X.ravel(), Y.ravel()))

fig, ax = plt.subplots()

ec = EllipseCollection(10, 10, 5, units ='y',
					offsets = XY * 0.5,
					transOffset = ax.transData,
					cmap ="inferno")

ec.set_array((X * Y).ravel())
ax.add_collection(ec)
ax.autoscale_view()
ax.set_xlabel('X')
ax.set_ylabel('y')
cbar = plt.colorbar(ec)
cbar.set_label('X + Y')

fig.suptitle('matplotlib.axes.Axes.autoscale() function Example\n', fontweight ="bold")
fig.canvas.draw()
plt.show()
