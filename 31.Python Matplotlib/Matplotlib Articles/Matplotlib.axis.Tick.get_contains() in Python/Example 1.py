# Implementation of matplotlib function
from matplotlib.axis import Tick
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


Tick.set_contains(ax2, picker=onpick1)

ax2.text(0.5, 0.8,
		"Value Return : "
		+ str(Tick.get_contains(ax2)),
		fontweight="bold", fontsize=10)

fig.suptitle("""matplotlib.axis.Tick.get_contains()
function Example\n""", fontweight="bold")

plt.show()
