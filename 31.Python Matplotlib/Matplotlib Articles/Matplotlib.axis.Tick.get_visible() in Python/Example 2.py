# Implementation of matplotlib function
from matplotlib.axis import Tick
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import Subplot


fig = plt.figure()

ax = Subplot(fig, 111)
fig.add_subplot(ax)

X = np.arange(-40, 40, 0.5)
Y = np.arange(-40, 40, 0.5)
U, V = np.meshgrid(X, Y)

ax.quiver(X, Y, U, V)

ax.axis["right"].set_visible(False)
ax.axis["top"].set_visible(False)

print("Visibilities of Axis")
print("Bottom :", Tick.get_visible(ax.axis["bottom"]),
	"\nTop :", Tick.get_visible(ax.axis["top"]),
	"\nLeft :", Tick.get_visible(ax.axis["left"]),
	"\nRight :", Tick.get_visible(ax.axis["right"]))

fig.suptitle('matplotlib.axis.Tick.get_visible() \
function Example\n', fontweight="bold")

plt.show()
