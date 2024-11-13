# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
from numpy.random import rand

fig, ax = plt.subplots()
ax.plot(rand(100), rand(100), 'o')


def line_picker(line, mouseevent):
    if mouseevent.xdata is None:
        return False, dict()

    xdata = line.get_xdata()
    ydata = line.get_ydata()
    maxd = 0.05
    d = np.sqrt(
        (xdata - mouseevent.xdata) ** 2 + (ydata - mouseevent.ydata) ** 2)

    ind, = np.nonzero(d <= maxd)

    if len(ind):

        pickx = xdata[ind]
        picky = ydata[ind]
        props = dict(ind=ind, pickx=pickx,
                     picky=picky)
        return True, props

    else:
        return False, dict()


Axis.set_contains(ax, picker=line_picker)

ax.text(0.1, 0.8,
        "Value Return : "
        + str(Axis.get_contains(ax)),
        fontweight="bold", fontsize=10)

fig.suptitle("""matplotlib.axis.Axis.get_contains() 
function Example\n""", fontweight="bold")

plt.show()
