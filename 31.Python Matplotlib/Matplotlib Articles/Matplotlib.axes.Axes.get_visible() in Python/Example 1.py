# Implementation of matplotlib function
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import Subplot

fig, ax = plt.subplots()

ax.plot([1, 2, 34, 67, 43, 5, 8])

ax.set_title("Visibility : " + str(ax.get_visible()))

fig.suptitle('matplotlib.axes.Axes.get_visible()\
function Example\n', fontweight="bold")

plt.show()
