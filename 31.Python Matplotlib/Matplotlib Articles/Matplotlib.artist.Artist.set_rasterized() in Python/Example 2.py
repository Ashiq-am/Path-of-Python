# Implementation of matplotlib function
from matplotlib.artist import Artist
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.gridspec as gridspec
import numpy as np

arr = np.arange(100).reshape((10, 10))
norm = mcolors.Normalize(vmin=0., vmax=100.)

pc_kwargs = {'cmap': 'plasma', 'norm': norm}

fig, ax = plt.subplots()

im = ax.pcolormesh(arr, **pc_kwargs)
fig.colorbar(im, ax=ax, shrink=0.6)
Artist.set_rasterized(im, False)

fig.suptitle('matplotlib.artist.Artist.set_rasterized()\
function Example', fontweight="bold")

plt.show()
