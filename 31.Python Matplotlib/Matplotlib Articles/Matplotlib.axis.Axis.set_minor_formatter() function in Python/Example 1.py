# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, ScalarFormatter

fig, ax = plt.subplots()
ax.plot([0, 5, 10, 15, 20], [3, 2, 1, 2, 4])

Axis.set_minor_locator(ax.xaxis, MultipleLocator(1))
Axis.set_minor_formatter(ax.xaxis, ScalarFormatter())

ax.tick_params(axis='both', which='major',
               labelsize=14, pad=12,
               colors='g')

ax.tick_params(axis='both', which='minor',
               labelsize=8, colors='b')

plt.title("Matplotlib.axis.Axis.set_minor_formatter()\n\
Function Example", fontsize=12, fontweight='bold')

plt.show()
