# Implementation of matplotlib function
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
from matplotlib.patches import Rectangle
from matplotlib.text import Text
from numpy.random import rand

fig, ax2 = plt.subplots()

ax2.bar(range(10), rand(10), picker=True)

for label in ax2.get_xticklabels():
    label.set_picker(True)


def onpick1(event):
    if isinstance(event.artist, Line2D):
        thisline = event.artist
        xdata = thisline.get_xdata()
        ydata = thisline.get_ydata()
        ind = event.ind
        print('onpick1 line:',
              np.column_stack([xdata[ind],
                               ydata[ind]]))

    elif isinstance(event.artist, Rectangle):
        patch = event.artist
        print('onpick1 patch:', patch.get_path())

    elif isinstance(event.artist, Text):
        text = event.artist
        print('onpick1 text:', text.get_text())


ax2.set_contains(onpick1)

ax2.text(0.5, 0.9,
         "Value Return : " + str(ax2.get_contains()),
         fontweight="bold", fontsize=10)

fig.suptitle('matplotlib.axes.Axes.get_contains() function\
Example', fontweight="bold")

plt.show()
