# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import Subplot

fig = plt.figure()

ax = Subplot(fig, 111)
fig.add_subplot(ax)

Axis.set_visible(ax.axis["right"], False)
Axis.set_visible(ax.axis["top"], False)

fig.suptitle('matplotlib.axis.Axis.set_visible() \
function Example\n', fontweight="bold")

plt.show()
