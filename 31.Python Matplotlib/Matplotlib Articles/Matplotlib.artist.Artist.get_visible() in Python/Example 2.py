# Implementation of matplotlib function
from matplotlib.artist import Artist
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import Subplot

fig = plt.figure()

ax = Subplot(fig, 111)
fig.add_subplot(ax)

X = np.arange(-20, 20, 0.5)
Y = np.arange(-20, 20, 0.5)
U, V = np.meshgrid(X, Y)

ax.quiver(X, Y, U, V)

ax.axis["bottom"].set_visible(False)
ax.axis["top"].set_visible(False)

print("Visibilities of Axis")
print("Bottom :", Artist.get_visible(ax.axis["bottom"]),
      "\nTop :", Artist.get_visible(ax.axis["top"]),
      "\nLeft :", Artist.get_visible(ax.axis["left"]),
      "\nRight :", Artist.get_visible(ax.axis["right"]))

fig.suptitle('matplotlib.artist.Artist.get_visible()\
function Example', fontweight="bold")

plt.show()
