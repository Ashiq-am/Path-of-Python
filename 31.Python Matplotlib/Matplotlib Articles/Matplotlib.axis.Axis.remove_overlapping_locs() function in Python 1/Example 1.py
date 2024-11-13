# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, ScalarFormatter

fig, ax = plt.subplots()
ax.plot([0, 5, 10, 15, 20], [3, 2, 1, 2, 4])

Axis.set_minor_locator(ax.xaxis, MultipleLocator(1))
Axis.set_minor_formatter(ax.xaxis, ScalarFormatter())
Axis.set_major_locator(ax.xaxis, MultipleLocator(4))

ax.tick_params(axis='both', which='major',
               labelsize=14, pad=12,
               colors='g')

ax.tick_params(axis='both', which='minor',
               labelsize=8, colors='b')
ax.xaxis.remove_overlapping_locs

plt.title("Matplotlib.axis.Axis.remove_overlapping_locs \
Example", fontsize=12, fontweight='bold')

plt.show()
