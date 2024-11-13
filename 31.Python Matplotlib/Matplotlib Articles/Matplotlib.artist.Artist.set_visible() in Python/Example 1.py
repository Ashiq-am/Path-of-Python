# Implementation of matplotlib function
from matplotlib.artist import Artist
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import Subplot

fig = plt.figure()

ax = Subplot(fig, 111)
fig.add_subplot(ax)

Artist.set_visible(ax.axis["left"], False)
Artist.set_visible(ax.axis["top"], False)

fig.suptitle('matplotlib.artist.Artist.set_visible()\
function Example', fontweight="bold")

plt.show()
