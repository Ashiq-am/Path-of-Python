# Implementation of matplotlib function
from matplotlib.artist import Artist
import numpy as np
import matplotlib.pyplot as plt

xx = np.random.rand(16, 30)

fig, (ax3, ax4) = plt.subplots(1, 2)

m = ax3.pcolor(xx)

ax3.set_title("No Zorder value ")

m = ax4.pcolor(xx)
Artist.set_zorder(m, -20)

ax4.set_title("Zorder Value : -20")

fig.suptitle('matplotlib.artist.Artist.set_zorder()\
function Example', fontweight="bold")

plt.show()
