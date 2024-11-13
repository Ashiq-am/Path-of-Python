# Implementation of matplotlib function
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from mpl_toolkits.axisartist.axislines import Subplot
import numpy as np

fig = plt.figure(edgecolor="green")

ax = Subplot(fig, 111)
fig.add_subplot(ax)

w = fig.get_edgecolor()
ax.text(0.2, 0.5, "Value Return by get_edgecolor() :\n"
        + str(w),
        fontweight="bold")

fig.canvas.draw()
fig.suptitle('matplotlib.figure.Figure.get_edgecolor() \
function Example', fontweight="bold")

plt.show()
