# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
from matplotlib.text import Text
from matplotlib.image import AxesImage
import numpy as np
from numpy.random import rand

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.set_ylabel('ylabel', picker=True,
               bbox=dict(facecolor='red'))

line, = ax1.plot(rand(100), 'go-')

ax2.bar(range(10), rand(10), picker=True)

for label in ax2.get_xticklabels():
    label.set_picker(True)


def onpick1(event):
    if isinstance(event.artist, Line2D):
        thisline = event.artist
        xdata = thisline.get_xdata()
        ydata = thisline.get_ydata()
        ind = event.ind
        print('onpick1 line:', np.column_stack([xdata[ind],
                                                ydata[ind]]))

    elif isinstance(event.artist, Rectangle):
        patch = event.artist
        print('onpick1 patch:', patch.get_path())

    elif isinstance(event.artist, Text):
        text = event.artist
        print('onpick1 text:', text.get_text())


Axis.set_contains(ax2, picker=onpick1)
fig.canvas.mpl_connect('pick_event', onpick1)

fig.suptitle('matplotlib.axis.Axis.set_contains() \
function Example\n', fontweight="bold")

plt.show()
