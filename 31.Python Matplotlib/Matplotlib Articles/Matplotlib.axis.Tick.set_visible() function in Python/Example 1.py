# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import Subplot

fig = plt.figure()

ax = Subplot(fig, 111)
fig.add_subplot(ax)

Tick.set_visible(ax.axis["right"], False)
Tick.set_visible(ax.axis["top"], False)

fig.suptitle('matplotlib.axis.Tick.set_visible() \
function Example', fontweight="bold")

plt.show()
