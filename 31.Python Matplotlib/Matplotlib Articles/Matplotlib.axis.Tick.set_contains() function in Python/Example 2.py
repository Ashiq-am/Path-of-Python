# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
from matplotlib.text import Text
from matplotlib.image import AxesImage
import numpy as np
from numpy.random import rand


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
        props = dict(ind=ind, pickx=pickx, picky=picky)
        return True, props

    else:
        return False, dict()


def onpick2(event):
    print('Result :', event.pickx, event.picky)


fig, ax = plt.subplots()
ax.plot(rand(100), rand(100), 'o')

Tick.set_contains(ax, picker=line_picker)

fig.canvas.mpl_connect('pick_event', onpick2)

fig.suptitle('matplotlib.axis.Tick.set_contains() \
function Example', fontweight="bold")

plt.show()
