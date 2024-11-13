# importing libraries
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, ScalarFormatter

fig, ax = plt.subplots()
ax.plot([0, 10, 20, 30], [0, 2, 1, 2])

ax.xaxis.set_minor_locator(MultipleLocator(1))
ax.xaxis.set_minor_formatter(ScalarFormatter())

ax.tick_params(axis ='both', which ='major',
			labelsize = 16, pad = 12,
			colors ='r')

ax.tick_params(axis ='both', which ='minor',
			labelsize = 8, colors ='b')

plt.show()
