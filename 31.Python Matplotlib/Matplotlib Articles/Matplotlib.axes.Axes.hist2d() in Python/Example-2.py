# Implementation of matplotlib function
from matplotlib import colors
import numpy as np
from numpy.random import multivariate_normal
import matplotlib.pyplot as plt

result = np.vstack([
	multivariate_normal([10, 10],
			[[3, 2], [2, 3]], size = 100000),
	multivariate_normal([30, 20],
			[[2, 3], [1, 3]], size = 1000)
])

fig, [axes, axes1] = plt.subplots(nrows = 2, ncols = 1, sharex = True)

axes.hist2d(result[:, 0], result[:, 1],
			bins = 100, cmap ="GnBu",
			norm = colors.LogNorm())

axes1.hist2d(result[:, 0], result[:, 1],
			bins = 100, norm = colors.LogNorm())

axes.set_title('matplotlib.axes.Axes.hist2d() Example')

plt.show()
