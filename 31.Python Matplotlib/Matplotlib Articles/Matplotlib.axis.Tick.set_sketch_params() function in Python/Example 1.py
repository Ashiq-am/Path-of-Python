# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.gridspec as gridspec
import numpy as np

plt.rcParams['savefig.facecolor'] = "0.8"
plt.rcParams['figure.figsize'] = 6, 5

fig, ax = plt.subplots()

ax.plot([1, 2, 3, 4, 5], [2, 3, 6, 2, 5])

ax.locator_params("x", nbins=3)
ax.locator_params("y", nbins=5)

ax.set_xlabel('x-label')
ax.set_ylabel('y-label')

Tick.set_sketch_params(ax, 50, 50, 10)

fig.suptitle('matplotlib.axis.Tick.set_sketch_params() \
function Example', fontweight="bold")

plt.show()
