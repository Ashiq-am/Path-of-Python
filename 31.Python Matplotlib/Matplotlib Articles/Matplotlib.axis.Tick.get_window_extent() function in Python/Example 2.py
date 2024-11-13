# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib.pyplot as plt
import numpy as np

xx = np.random.rand(3, 4)

fig, ax = plt.subplots()

m = ax.pcolor(xx)
m.set_zorder(10)

fig.canvas.draw()
renderer = fig.canvas.renderer

# use of get_window_extent() method
val = Tick.get_window_extent(ax, renderer)
print("Value Return by get_window_extent():")
print(val)

fig.suptitle('matplotlib.axis.Tick.get_window_extent() \
function Example', fontweight="bold")

plt.show()
