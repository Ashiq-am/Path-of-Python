# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

NUM = 200

ells = [Ellipse(xy=np.random.rand(2) * 10,
                width=np.random.rand(),
                height=np.random.rand(),
                angle=np.random.rand() * 360)
        for i in range(NUM)]

fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})

for e in ells:
    ax.add_artist(e)
    e.set_clip_box(ax.bbox)
    e.set_alpha(np.random.rand())
    e.set_facecolor(np.random.rand(4))

ax.set_xlim(3, 7)
ax.set_ylim(3, 7)

print("Value return by get_constrained_layout_pads() ")
w = list(fig.get_constrained_layout_pads())

print("w_pad :", w[0])
print("h_pad :", w[1])
print("wspace :", w[2])
print("hspace :", w[3])

fig.suptitle('matplotlib.figure.Figure.get_constrained_layout_pads() \
function Example\n\n', fontweight="bold")

plt.show()
