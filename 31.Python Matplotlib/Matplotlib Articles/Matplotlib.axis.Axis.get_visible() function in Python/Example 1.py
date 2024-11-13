# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import Subplot

fig, ax = plt.subplots()

ax.plot([11, 52, 4, 7, 13, 35, 81])

ax.set_title("Visibility : " + str(Axis.get_visible(ax)))

fig.suptitle('matplotlib.axis.Axis.get_visible() \
function Example\n', fontweight="bold")

plt.show()
