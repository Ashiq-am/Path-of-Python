# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)

fig, ax = plt.subplots()

x, y, s, c = np.random.rand(4, 200)
s *= 200

ax.scatter(x, y, s, c)

Axis.set(ax, xlabel='X-Axis', ylabel='Y-Axis',
         xlim=(0, 0.5), ylim=(0, 0.5))

ax.grid()

fig.suptitle('matplotlib.axis.Axis.set() \
function Example\n', fontweight="bold")

plt.show()
