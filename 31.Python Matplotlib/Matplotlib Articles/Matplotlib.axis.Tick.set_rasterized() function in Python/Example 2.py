# Implementation of matplotlib function
from matplotlib.axis import Tick
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
Tick.set_rasterized(im, False)

fig.suptitle('matplotlib.axis.Tick.set_rasterized() \
function Example', fontweight="bold")

plt.show()
