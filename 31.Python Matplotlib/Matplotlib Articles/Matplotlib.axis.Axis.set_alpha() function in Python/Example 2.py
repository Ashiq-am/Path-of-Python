# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

NUM = 100

ells = [Ellipse(xy=np.random.rand(2) * 10,
                width=np.random.rand(),
                height=np.random.rand(),
                angle=np.random.rand() * 360)
        for i in range(NUM)]

fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})

for e in ells:
    ax.add_artist(e)
    e.set_clip_box(ax.bbox)
    Axis.set_alpha(e, np.random.rand())
    e.set_facecolor(np.random.rand(4))

ax.set_xlim(2, 8)
ax.set_ylim(2, 8)

fig.suptitle('matplotlib.axis.Axis.set_alpha() \
function Example\n', fontweight="bold")

plt.show()
