# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.gridspec as gridspec
import numpy as np

arr = np.arange(20).reshape((4, 5))
norm = mcolors.Normalize(vmin=0., vmax=20.)

pc_kwargs = {'cmap': 'BuGn', 'norm': norm}

fig, ax = plt.subplots()

im = ax.pcolormesh(arr, **pc_kwargs)
fig.colorbar(im, ax=ax, shrink=0.7)
Axis.set_rasterized(im, False)

fig.suptitle('matplotlib.axis.Axis.set_rasterized() \
function Example\n', fontweight="bold")

plt.show()
