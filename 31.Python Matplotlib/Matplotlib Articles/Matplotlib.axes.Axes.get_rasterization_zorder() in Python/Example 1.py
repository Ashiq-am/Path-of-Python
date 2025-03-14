# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

d = np.arange(100).reshape(10, 10)
xx, yy = np.meshgrid(np.arange(11), np.arange(11))

fig, ax = plt.subplots()

ax.set_aspect(1)
m = ax.pcolormesh(xx, yy, d)
m.set_zorder(-15)
ax.set_rasterization_zorder(-5)

w = ax.get_rasterization_zorder()
ax.text(2, 9.5, "Rasterization Zorder Value : " + str(w))

fig.suptitle('matplotlib.axes.Axes.get_rasterization_zorder() \
function Example', fontweight="bold")

plt.show()
