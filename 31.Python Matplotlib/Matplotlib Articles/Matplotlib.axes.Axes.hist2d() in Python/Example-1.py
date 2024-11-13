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

ax.set_title('matplotlib.axes.Axes.\
hist2d() Example')

plt.show()
