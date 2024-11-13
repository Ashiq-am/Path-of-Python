# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np
import matplotlib.pyplot as plt

d = np.arange(49).reshape(7, 7)
xx, yy = np.meshgrid(np.arange(8), np.arange(8))

fig, ax = plt.subplots()

ax.set_aspect(1)
m = ax.pcolormesh(xx, yy, d)
Axis.set_rasterized(m, True)

fig.suptitle('matplotlib.axis.Axis.set_rasterized() \
function Example\n', fontweight="bold")

plt.show()
