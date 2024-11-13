# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import Subplot


fig, ax = plt.subplots()

ax.plot([11, 2, 4, 7, 3, 5, 1])

ax.set_title("Visibility : " + str(Tick.get_visible(ax)))

fig.suptitle('matplotlib.axis.Tick.get_visible() \
function Example\n', fontweight="bold")

plt.show()
