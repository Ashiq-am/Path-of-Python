# Implementation of matplotlib function
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import Subplot

fig = plt.figure()

ax = Subplot(fig, 111)
fig.add_subplot(ax)

ax.axis["left"].set_visible(False)
ax.axis["top"].set_visible(False)

ax.set_snap(True)

fig.suptitle('matplotlib.axes.Axes.set_snap() \
function Example\n', fontweight="bold")

plt.show()
