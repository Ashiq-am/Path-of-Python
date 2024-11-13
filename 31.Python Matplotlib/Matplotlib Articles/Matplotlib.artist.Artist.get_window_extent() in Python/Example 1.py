# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.artist import Artist


X = np.arange(-10, 10, 1.5)
Y = np.arange(-10, 10, 1.5)
U, V = np.meshgrid(X, Y)

fig, ax = plt.subplots()

ax.quiver(X, Y, U, V)

fig.canvas.draw()
renderer = fig.canvas.renderer

# use of get_window_extent() method
val = Artist.get_window_extent(ax, renderer)
print("Value Return by get_window_extent():")
print(val)

fig.suptitle('matplotlib.artist.Artist.get_window_extent() function Example', fontweight="bold")

plt.show()
