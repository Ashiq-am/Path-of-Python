# Implementation of matplotlib function
from matplotlib.axis import Tick
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from matplotlib.path import Path
from matplotlib.patches import PathPatch

delta = 0.025

x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)

Z1 = np.exp(-X ** 2 - Y ** 2)
Z2 = np.exp(-(X - 1) ** 2 - (Y - 1) ** 2)
Z = (Z1 - Z2) * 2

path = Path([[0, 1], [1, 0], [0, -1],
             [-1, 0], [0, 1]])
patch = PathPatch(path, facecolor='none')

fig, ax = plt.subplots()
ax.add_patch(patch)

im = ax.imshow(Z, interpolation='bilinear',
               cmap=cm.gray,
               origin='lower',
               extent=[-3, 3, -3, 3],
               clip_path=patch, clip_on=True)

im.set_clip_path(patch)

Tick.set_snap(im, None)

fig.suptitle('matplotlib.axis.Tick.set_snap() \
function Example', fontweight="bold")

plt.show()
