# Implementation of matplotlib function
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
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


print("Value return by get_constrained_layout_pads() ")
w = list(fig.get_constrained_layout_pads())

print("w_pad :", w[0])
print("h_pad :", w[1])
print("wspace :", w[2])
print("hspace :", w[3])

fig.suptitle('matplotlib.figure.Figure.get_constrained_layout_pads() \
function Example\n\n', fontweight="bold")

plt.show()
