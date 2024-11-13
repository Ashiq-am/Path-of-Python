# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2, 0.001)
s = 1 + np.sin(4 * np.pi * t) * 0.2

fig, ax = plt.subplots()
ax.plot(t, s)

Tick.set(ax, xlabel='X-Axis', ylabel='Y-Axis',
         xlim=(0, 1.5), ylim=(0.5, 1.5))

ax.grid()

fig.suptitle('matplotlib.axis.Tick.set() \
function Example', fontweight="bold")

plt.show()
