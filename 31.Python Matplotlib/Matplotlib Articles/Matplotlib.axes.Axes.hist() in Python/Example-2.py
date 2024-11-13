# Implementation of matplotlib function
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10**7)
n_bins = 20
x = np.random.randn(10000, 3)

fig, [(ax0, ax1), (ax2, ax3)] = plt.subplots(nrows = 2,
											ncols = 2)


colors = ['green', 'blue', 'lime']

ax0.hist(x, n_bins, density = True,
		histtype ='bar',
		color = colors,
		label = colors)

ax0.legend(prop ={'size': 10})

ax1.hist(x, n_bins, density = True,
		histtype ='barstacked',
		stacked = True,
		color = colors)

ax2.hist(x, n_bins, histtype ='step',
		stacked = True,
		fill = False,
		color = colors)

x_multi = [np.random.randn(n) for n in [100000,
										80000,
										1000]]

ax3.hist(x_multi, n_bins,
		histtype ='stepfilled',
		color = colors)

plt.show()
