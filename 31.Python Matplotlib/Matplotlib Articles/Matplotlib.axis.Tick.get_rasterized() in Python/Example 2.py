# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.gridspec as gridspec
import numpy as np


arr = np.arange(100).reshape((10, 10))
norm = mcolors.Normalize(vmin=0., vmax=100.)

pc_kwargs = {'cmap': 'PuBuGn', 'norm': norm}

fig, ax = plt.subplots()

m = ax.pcolormesh(arr, **pc_kwargs)
fig.colorbar(m, ax=ax, shrink=0.6)

if Tick.get_rasterized(m) == None:
	Tick.set_rasterized(m, True)

fig.suptitle("""matplotlib.axis.Tick.get_rasterized()
function Example\n""", fontweight="bold")

plt.show()
