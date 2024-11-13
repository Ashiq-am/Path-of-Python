# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.gridspec as gridspec
import numpy as np


arr = np.arange(100).reshape((10, 10))
norm = mcolors.Normalize(vmin = 0., vmax = 100.)

pc_kwargs = {'cmap': 'plasma', 'norm': norm}

fig, ax = plt.subplots( )

im = ax.pcolormesh(arr, **pc_kwargs)
fig.colorbar(im, ax = ax, shrink = 0.6)

ax.set_rasterized(False)

fig.suptitle('matplotlib.axes.Axes.set_rasterized() function Example', fontweight ="bold")

plt.show()
