import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LogFormatterSciNotation


class CustomTicker(LogFormatterSciNotation):

	def __call__(self, x, pos = None):

		if x not in [0.1, 1, 10]:
			return LogFormatterSciNotation.__call__(self, x, pos = None)

		else:
			return "{x:g}".format(x = x)


fig = plt.figure(figsize =[7, 7])
ax = fig.add_subplot(111)

ax.set_yscale('log')
ax.set_xscale('log')

ax.plot(np.logspace(-4, 4), np.logspace(-4, 4))

ax.xaxis.set_major_formatter(CustomTicker())

plt.show()
