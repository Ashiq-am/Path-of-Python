# Implementation of matplotlib function
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import numpy as np
import matplotlib.pyplot as plt

N_points = 100000
x = np.random.randn(N_points)
y = .4 * x + np.random.randn(100000) + 5

fig, ax = plt.subplots()
ax.hist2d(x, y, bins=100,
          norm=colors.LogNorm(),
          cmap="Greens")

w = list(ax.get_lines())
if len(w) == 0:
    ax.text(-2, 8.5,
            "No line contained by the Axes \n")
else:
    ax.text(-3, 8.5,
            "List of the lines contained by the Axes \n")
    x = 8.5
    for i in w:
        ax.text(-3, x - 0.5, str(i))
        x -= 0.5

fig.suptitle('matplotlib.axes.Axes.get_lines() \
function Example', fontweight="bold")

plt.show()
