# Implementation of matplotlib function
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from mpl_toolkits.axisartist.axislines import Subplot
import numpy as np

fig = plt.figure()

ax = Subplot(fig, 111)
fig.add_subplot(ax)

w = fig.get_facecolor()
ax.text(0.3, 0.5,
        "Value Return by get_facecolor() :\n "
        + str(w),
        fontweight="bold")

fig.canvas.draw()
fig.suptitle('matplotlib.figure.Figure.get_facecolor() \
function Example', fontweight="bold")

plt.show()
