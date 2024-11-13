# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

NUM = 100

ells = [Ellipse(xy=np.random.rand(2),
                width=np.random.rand(),
                height=np.random.rand(),
                angle=np.random.rand() * 360)
        for i in range(NUM)]

fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})

for e in ells:
    ax.add_artist(e)
    e.set_clip_box(ax.bbox)
    e.set_facecolor(np.random.rand(4))
    Tick.set_alpha(e, 0.2)

fig.suptitle('matplotlib.axis.Tick.set_alpha() \
function Example', fontweight="bold")

plt.show()
