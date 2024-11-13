# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

d = np.arange(100).reshape(10, 10)
xx, yy = np.meshgrid(np.arange(11), np.arange(11))

fig, ax = plt.subplots()

ax.set_aspect(1)
m = ax.pcolormesh(xx, yy, d)
if m.get_rasterized() == None:
    m.set_rasterized(True)

fig.suptitle('matplotlib.axes.Axes.get_rasterized() \
function Example', fontweight="bold")

plt.show()
