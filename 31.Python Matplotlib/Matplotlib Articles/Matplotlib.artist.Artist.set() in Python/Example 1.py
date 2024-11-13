# Implementation of matplotlib function
from matplotlib.artist import Artist
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2, 0.001)
s = 1 + np.sin(8 * np.pi * t) * 0.4

fig, ax = plt.subplots()
ax.plot(t, s)

Artist.set(ax, xlabel='X-Axis', ylabel='Y-Axis',
           xlim=(0, 1.5), ylim=(0.5, 1.5),
           title='matplotlib.artist.Artist.set() function Example')

ax.grid()

plt.show()
