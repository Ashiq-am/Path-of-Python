# Implementation of matplotlib function
from matplotlib.axis import Tick
import numpy as np
import matplotlib.pyplot as plt

d = np.arange(16).reshape(4, 4)
xx, yy = np.meshgrid(np.arange(5), np.arange(5))

fig, ax = plt.subplots()

ax.set_aspect(1)
m = ax.pcolormesh(xx, yy, d)
Tick.set_rasterized(m, True)

fig.suptitle('matplotlib.axis.Tick.set_rasterized() \
function Example', fontweight="bold")

plt.show()
