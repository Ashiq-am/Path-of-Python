# Implementation of matplotlib function
from matplotlib.axis import Tick
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D
import matplotlib.transforms as mtransforms

fig, ax = plt.subplots()
l1, = ax.plot([0.1, 0.5, 0.9],
              [0.1, 0.9, 0.5],
              "go-")
l2, = ax.plot([0.1, 0.5, 0.9],
              [0.5, 0.2, 0.7],
              "yo-")

for l in [l1, l2]:
    xx = l.get_xdata()
    yy = l.get_ydata()

    shadow, = ax.plot(xx, yy)
    Tick.update_from(shadow, l)

    ot = mtransforms.offset_copy(l.get_transform(),
                                 ax.figure,
                                 x=4.0,
                                 y=-6.0,
                                 units='points')

    shadow.set_transform(ot)
ax.set_title('matplotlib.axis.Tick.update_from() \
function Example', fontweight="bold")

plt.show()
