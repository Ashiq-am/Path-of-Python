# Implementation of matplotlib function
from matplotlib.axis import Axis
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

np.random.seed(19680801)

line = lines.Line2D([2 * cm, 8 * cm], [0 * cm, 2.5 * cm],
                    lw=2, color='green', axes=ax)
ax.add_line(line)

t = text.Text(3 * cm, 2.5 * cm,
              'Line 1',
              ha='left',
              va='bottom',
              axes=ax,
              color='red')
ax.add_artist(t)

ax.set_xlim(-1 * cm, 10 * cm)
ax.set_ylim(-1 * cm, 10 * cm)

ax.grid(True)

fig.suptitle("""matplotlib.axis.Axis.set_units() 
function Example\n""", fontweight="bold")

plt.show()
