# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.gridspec as gridspec
import numpy as np

plt.rcParams['savefig.facecolor'] = "0.8"
plt.rcParams['figure.figsize'] = 6, 5

fig, ax = plt.subplots()

ax.plot([1, 2])

ax.locator_params("x", nbins=3)
ax.locator_params("y", nbins=5)

ax.set_xlabel('x-label')
ax.set_ylabel('y-label')

ax.text(0.2, 1.8, "Sketch Parameters : "
        + str(ax.get_sketch_params()),
        fontweight="bold")

fig.suptitle('matplotlib.axes.Axes.get_sketch_params() \
function Example\n\n', fontweight="bold")

plt.show()
