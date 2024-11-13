# Implementation of matplotlib function
from matplotlib.axis import Tick
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)

fig, ax = plt.subplots()

x, y, s, c = np.random.rand(4, 100)
s *= 10000

ax.scatter(x ** 2, y ** 2, s, c ** 2)

Tick.set(ax, xlabel='X-Axis', ylabel='Y-Axis',
         xlim=(0, 0.5), ylim=(0, 0.5))

fig.suptitle('matplotlib.axis.Tick.set() \
function Example', fontweight="bold")

plt.show()
