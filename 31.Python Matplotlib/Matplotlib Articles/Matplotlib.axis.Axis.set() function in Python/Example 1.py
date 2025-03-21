# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2, 0.001)
s = 1 + np.sin(8 * np.pi * t) * 0.4

fig, ax = plt.subplots()
ax.plot(t, s)

Axis.set(ax, xlabel='X-Axis', ylabel='Y-Axis',
         xlim=(0, 1.5), ylim=(0.5, 1.5))

ax.grid()

fig.suptitle('matplotlib.axis.Axis.set() \
function Example\n', fontweight="bold")

plt.show()
