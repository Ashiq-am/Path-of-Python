# Implementation of matplotlib function
from matplotlib.artist import Artist
import matplotlib.pyplot as plt
import numpy as np

values = np.array([
    0.015, 0.166, 0.133,
    0.159, 0.041, 0.024,
    0.195, 0.039, 0.161,
    0.018, 0.143, 0.056,
    0.125, 0.096, 0.094,
    0.051, 0.043, 0.021,
    0.138, 0.075, 0.109,
    0.195, 0.050, 0.074,
    0.079, 0.155, 0.020,
    0.010, 0.061, 0.008])

values[[3, 14]] += .8

fig, (ax, ax2) = plt.subplots(2, 1, sharex=True)

ax.plot(values, "o-", color="green")
ax2.plot(values, "o-", color="green")

ax.set_ylim(.78, 1.)
ax2.set_ylim(0, .22)

ax.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax.xaxis.tick_top()
ax.tick_params(labeltop=False)
ax2.xaxis.tick_bottom()

d = .005
kwargs = dict(transform=ax.transAxes,
              color='k', clip_on=False)

ax.plot((-d, +d), (-d, +d), **kwargs)
ax.plot((1 - d, 1 + d), (-d, +d), **kwargs)

kwargs.update(transform=ax2.transAxes)

ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)
ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)

Artist.set_sketch_params(ax, 1.0, 100.0, 22.0)
Artist.set_sketch_params(ax2, 1.0, 10.0, 22.0)

fig.suptitle('matplotlib.artist.Artist.set_sketch_params()\
function Example', fontweight="bold")

plt.show()
