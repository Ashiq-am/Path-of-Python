# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.gridspec as gridspec
import numpy as np


arr = np.arange(100).reshape((10, 10))
norm = mcolors.Normalize(vmin = 0., vmax = 100.)

pc_kwargs = {'rasterized': True, 'cmap': 'viridis',
			'norm': norm}

fig, (ax, ax1) = plt.subplots(1, 2)

im = ax.pcolormesh(arr, **pc_kwargs)
fig.colorbar(im, ax = ax, shrink = 0.6)

im1 = ax1.pcolormesh(arr, **pc_kwargs)
ax1.locator_params(nbins = 3)
fig.colorbar(im1, ax = ax1, shrink = 0.6)

ax.set_title("Without locator_params()")
ax1.set_title("With locator_params()")

fig.suptitle('matplotlib.axes.Axes.locator_params() function Example\n\n', fontweight ="bold")
plt.show()
