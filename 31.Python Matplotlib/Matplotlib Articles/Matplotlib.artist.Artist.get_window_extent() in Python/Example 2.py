# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.artist import Artist


xx = np.random.rand(10, 10)

fig, ax = plt.subplots()

m = ax.pcolor(xx)
m.set_zorder(-20)

fig.canvas.draw()
renderer = fig.canvas.renderer

# use of get_window_extent() method
val = Artist.get_window_extent(ax, renderer)
print("Value Return by get_window_extent():")
print(val)

fig.suptitle('matplotlib.artist.Artist.get_window_extent() function Example', fontweight="bold")

plt.show()
