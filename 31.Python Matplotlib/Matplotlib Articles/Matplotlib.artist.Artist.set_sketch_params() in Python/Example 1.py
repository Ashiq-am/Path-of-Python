# Implementation of matplotlib function
from matplotlib.artist import Artist
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

Artist.set_sketch_params(ax, 100, 100, 20)

fig.suptitle('matplotlib.artist.Artist.set_sketch_params()\
function Example', fontweight="bold")

plt.show()
