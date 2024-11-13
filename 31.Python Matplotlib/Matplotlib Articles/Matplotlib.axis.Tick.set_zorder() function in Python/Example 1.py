# Implementation of matplotlib function
from matplotlib.axis import Tick
import numpy as np
import matplotlib.pyplot as plt

d = np.arange(49).reshape(7, 7)
xx, yy = np.meshgrid(np.arange(8), np.arange(8))

fig, ax = plt.subplots()

ax.set_aspect(1)
m = ax.pcolormesh(xx ** 2, yy ** 2, d ** 2)

Tick.set_zorder(m, -5)

ax.set_title('matplotlib.axis.Tick.set_zorder() \
function Example', fontweight="bold")

plt.show()
