# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import MultipleLocator, ScalarFormatter

x = [0, 5, 9, 10, 15]
y = [0, 1, 2, 3, 4]

tick_spacing = 1

fig, ax = plt.subplots(1, 1)
ax.plot(x, y)

Axis.set_major_locator(ax.xaxis,
                       ticker.MultipleLocator(3))
Axis.set_minor_locator(ax.xaxis,
                       ticker.MultipleLocator(tick_spacing))
Axis.set_minor_formatter(ax.xaxis, ScalarFormatter())
ax.xaxis.remove_overlapping_locs

plt.title("Matplotlib.axis.Axis.remove_overlapping_locs \
Example", fontsize=12, fontweight='bold')

plt.show()
