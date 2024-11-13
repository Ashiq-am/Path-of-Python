# Implementation of matplotlib function

import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

# create random data
xdata = np.random.random([2, 10])

# split the data into two parts
xdata1 = xdata[0, :]
xdata2 = xdata[1, :]

# sort the data so it makes clean curves
xdata1.sort()
xdata2.sort()

# create some y data points
ydata1 = xdata1 ** 2
ydata2 = 1 - xdata2 ** 3

# plot the data
plt.plot(xdata1, ydata1, color='tab:blue')
plt.plot(xdata2, ydata2, color='tab:orange')

# set the limits
plt.xlim([0, 1])
plt.ylim([0, 1])

plt.title('matplotlib.pyplot.plot() example 2')

# display the plot
plt.show()
