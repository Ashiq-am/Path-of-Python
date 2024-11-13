# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
from matplotlib.ticker import LogFormatter
import numpy as np

fig, axes = plt.subplots(2)

dt = 0.01
t = np.arange(dt, 20.0, dt)

# first plot doesn't use a formatter
axes[0].semilogx(t, np.exp(-t / 5.0))
axes[0].grid()

xlims = [[0, 25], [0.2, 8], [0.6, 0.9]]

for ax, xlim in zip(axes[1:], xlims):
    ax.semilogx(t, np.exp(-t / 5.0))
    formatter = LogFormatter(labelOnlyBase=False,minor_thresholds=(2, 0.4))

    Axis.set_minor_formatter(ax.xaxis, formatter)
    ax.grid()

fig.suptitle("Matplotlib.axis.Axis.set_minor_formatter()\n\
Function Example", fontsize=12, fontweight='bold')

plt.show()
