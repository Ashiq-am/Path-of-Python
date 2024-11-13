# Implementation of matplotlib function
from matplotlib.artist import Artist
import numpy as np
import matplotlib.pyplot as plt

xx = np.random.rand(16, 30)

fig, ax = plt.subplots()

ax.pcolor(xx)
ax.set_zorder(-20)

ax.set_title("Zorder Value : "
             + str(Artist.get_zorder(ax)),
             fontweight="bold")

fig.suptitle('matplotlib.artist.Artist.get_zorder()\
function Example', fontweight="bold")

plt.show()
