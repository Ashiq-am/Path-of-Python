# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import EllipseCollection

x = np.arange(5)
y = np.arange(7)
X, Y = np.meshgrid(x ** 2, y ** 3)

XY = np.column_stack((X.ravel(), Y.ravel()))

fig, ax = plt.subplots()

ec = EllipseCollection(5, 7, 5, units='y',
                       offsets=XY * 0.5,
                       transOffset=ax.transData,
                       cmap="plasma")

ec.set_array((X * Y + X * X).ravel())

ax.add_collection(ec)
ax.autoscale_view()

ax.set_xlabel('X')
ax.set_ylabel('y')

cbar = plt.colorbar(ec)
cbar.set_label('X + Y')

fig.suptitle('matplotlib.axis.Tick.set_label() \
function Example', fontweight="bold")

plt.show()
