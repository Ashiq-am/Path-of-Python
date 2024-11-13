# Implementation of matplotlib function
from matplotlib.artist import Artist
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import Subplot

fig, ax = plt.subplots()

ax.plot([1, 2, 34, 67, 43, 5, 8])

ax.set_title("Visibility : " + str(Artist.get_visible(ax)))

fig.suptitle('matplotlib.artist.Artist.get_visible()\
function Example', fontweight="bold")

plt.show()
