# Implementation of matplotlib function
from matplotlib.artist import Artist
import numpy as np
import matplotlib.pyplot as plt

d = np.arange(100).reshape(10, 10)
xx, yy = np.meshgrid(np.arange(11), np.arange(11))

fig, ax = plt.subplots()

ax.set_aspect(1)
m = ax.pcolormesh(xx, yy, d)

Artist.set_zorder(m, -15)

fig.suptitle('matplotlib.artist.Artist.set_zorder()\
function Example', fontweight="bold")

plt.show()
