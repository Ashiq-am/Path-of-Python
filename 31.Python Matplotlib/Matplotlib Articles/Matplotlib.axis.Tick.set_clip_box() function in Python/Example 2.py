# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

NUM = 200

ells = [Ellipse(xy=np.random.rand(2),
                width=np.random.rand(),
                height=np.random.rand(),
                angle=np.random.rand() * 360)
        for i in range(NUM)]

fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})

for e in ells:
    ax.add_artist(e)
    Tick.set_clip_box(e, ax.bbox)
    e.set_clip_box(ax.bbox)
    e.set_alpha(np.random.rand())
    e.set_facecolor(np.random.rand(4))

fig.suptitle('matplotlib.axis.Tick.set_clip_box() \
function Example', fontweight="bold")

plt.show()
