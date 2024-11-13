# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import Subplot

fig = plt.figure()

ax = Subplot(fig, 111)
fig.add_subplot(ax)

X = np.arange(-20, 20, 0.5)
Y = np.arange(-20, 20, 0.5)
U, V = np.meshgrid(X, Y)

ax.quiver(X, Y, U, V)

ax.axis["bottom"].set_visible(False)
ax.axis["top"].set_visible(False)

print("Visibilities of Axis")
print("Bottom :", ax.axis["bottom"].get_visible(),
      "\nTop :", ax.axis["top"].get_visible(),
      "\nLeft :", ax.axis["left"].get_visible(),
      "\nRight :", ax.axis["right"].get_visible())

fig.suptitle('matplotlib.axes.Axes.get_visible() \
function Example\n', fontweight="bold")

plt.show()
