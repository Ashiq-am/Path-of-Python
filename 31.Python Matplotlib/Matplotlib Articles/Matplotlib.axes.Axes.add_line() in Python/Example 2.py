# Implementation of matplotlib function
import random
import matplotlib.lines as lines
import matplotlib.patches as patches
import matplotlib.text as text
import matplotlib.collections as collections
from basic_units import cm, inch
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.xaxis.set_units(cm)
ax.yaxis.set_units(cm)

# Fixing random state for reproducibility
np.random.seed(19680801)


if 0:
    # test a line collection
    # Not supported at present.
    verts = []
    for i in range(10):
        # a random line segment in inches
        verts.append(zip(*inch * 10 * np.random.rand(2,random.randint(2, 15))))
    lc = collections.LineCollection(verts, axes = ax)
    ax.add_collection(lc)

# test a plain-ol-line
line = lines.Line2D([0 * cm, 1.5 * cm],
					[0 * cm, 2.5 * cm],
					lw = 2, color ='green',
					axes = ax, alpha = 0.7)

ax.add_line(line)

ax.grid(True)

fig.suptitle('matplotlib.axes.Axes.add_line() function Example\n\n', fontweight ="bold")
plt.show()
