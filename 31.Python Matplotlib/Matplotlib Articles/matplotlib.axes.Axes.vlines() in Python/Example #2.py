# Implementation of matplotlib function

import numpy as np
from matplotlib import patches
import matplotlib.pyplot as plt

t = np.arange(0.0, 5.0, 0.1)
s = np.exp(-t) + np.cos(3 * np.pi * t) + np.sin(np.pi * t)
nse = np.random.normal(0.0, 0.8, t.shape) * s

fig, ax = plt.subplots()

ax.vlines(t, [0], s)
ax.vlines([1, 2], 0, 1, color="lightgreen",
          transform=ax.get_xaxis_transform())

ax.set_xlabel('time (s)')
ax.set_title('matplotlib.axes.Axes.vlines Example')

plt.show()
