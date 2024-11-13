# Implementation of matplotlib function

import numpy as np
from matplotlib import patches
import matplotlib.pyplot as plt

t = np.arange(0.0, 5.0, 0.1)
s = np.exp(-t) + np.cos(3 * np.pi * t) + np.sin(np.pi * t)
nse = np.random.normal(0.0, 0.8, t.shape) * s

fig, ax = plt.subplots()

ax.hlines(t, [0], s)
ax.set_xlabel('time (s)')
ax.hlines([1, 3, 5], -3, 5, color="lightgreen")
ax.set_title('matplotlib.axes.Axes.hlines Example')

plt.show()
