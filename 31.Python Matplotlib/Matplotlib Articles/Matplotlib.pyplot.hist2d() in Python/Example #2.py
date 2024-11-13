# Implementation of matplotlib function
from matplotlib import colors
import numpy as np
from numpy.random import multivariate_normal
import matplotlib.pyplot as plt

result = np.vstack([
    multivariate_normal([10, 10],
                        [[3, 2], [2, 3]], size=1000000),
    multivariate_normal([30, 20],
                        [[2, 3], [1, 3]], size=100000)
])

plt.hist2d(result[:, 0],
           result[:, 1],
           bins=100,
           cmap="Greens",
           norm=colors.LogNorm())
plt.title('matplotlib.pyplot.hist2d function \
Example')
plt.show()

plt.hist2d(result[:, 0],
           result[:, 1],
           bins=100,
           cmap="RdYlGn_r",
           norm=colors.LogNorm())
plt.show()
