# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms

fig, ax = plt.subplots()
l1, = ax.plot([0.1, 0.5, 0.9],
              [0.1, 0.9, 0.5],
              "bo-")
l2, = ax.plot([0.1, 0.5, 0.9],
              [0.5, 0.2, 0.7],
              "ro-")

for l in [l1, l2]:
    xx = l.get_xdata()
    yy = l.get_ydata()

    shadow, = ax.plot(xx, yy)
    shadow.update_from(l)

    ot = mtransforms.offset_copy(l.get_transform(),
                                 ax.figure,
                                 x=4.0,
                                 y=-6.0,
                                 units='points')

    shadow.set_transform(ot)

fig.suptitle('matplotlib.axes.Axes.update_from() \
function Example', fontweight="bold")

plt.show()
