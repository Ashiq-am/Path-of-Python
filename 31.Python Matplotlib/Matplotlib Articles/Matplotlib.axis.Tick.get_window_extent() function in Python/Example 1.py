# Implementation of matplotlib function
from matplotlib.axis import Tick
import numpy as np
import matplotlib.pyplot as plt

X = np.arange(0, 5, .5)
Y = np.arange(0, 5, .5)
U, V = np.meshgrid(X, Y)

fig, ax = plt.subplots()

ax.quiver(X, Y, U, V)

fig.canvas.draw()
renderer = fig.canvas.renderer

# use of get_window_extent() method
val = Tick.get_window_extent(ax, renderer)
print("Value Return by get_window_extent():")
print(val)

fig.suptitle('matplotlib.axis.Tick.get_window_extent() \
function Example', fontweight="bold")

plt.show()
