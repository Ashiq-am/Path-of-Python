# Implementation of matplotlib function
from matplotlib.artist import Artist
import matplotlib.pyplot as plt
import numpy as np

X = np.arange(-20, 20, 0.5)
Y = np.arange(-20, 20, 0.5)
U, V = np.meshgrid(X, Y)

fig, ax = plt.subplots()
ax.quiver(X, Y, U, V)
w = ax.get_xaxis()

Artist.set_visible(w, False)

fig.suptitle('matplotlib.artist.Artist.set_visible()\
function Example', fontweight="bold")

plt.show()
