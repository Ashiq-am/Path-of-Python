# Implementation of matplotlib function
from matplotlib.artist import Artist
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import Subplot

fig = plt.figure()

ax = Subplot(fig, 111)
fig.add_subplot(ax)

ax.axis["left"].set_visible(False)
ax.axis["top"].set_visible(False)

Artist.set_snap(ax, True)

fig.suptitle('matplotlib.artist.Artist.set_snap()\
function Example', fontweight="bold")

plt.show()
