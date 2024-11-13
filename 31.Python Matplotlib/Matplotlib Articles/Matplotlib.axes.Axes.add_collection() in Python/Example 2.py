# Implementation of matplotlib function
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib import colors as mcolors
import numpy as np

N = 50
x = np.arange(N)

ys = [i/(x + 1) for i in x]

fig, ax = plt.subplots()
ax.set_xlim(0, 20)
ax.set_ylim(0, 20)

line_segments = LineCollection([np.column_stack([x, y]) for y in ys],
							linewidths =(0.5, 1, 1.5, 2),
							linestyles ='dashed',
							color ="# eeffdd")
line_segments.set_array(x**2)
ax.add_collection(line_segments)

fig.suptitle('matplotlib.axes.Axes.add_collection() function Example\n\n', fontweight ="bold")
plt.show()
