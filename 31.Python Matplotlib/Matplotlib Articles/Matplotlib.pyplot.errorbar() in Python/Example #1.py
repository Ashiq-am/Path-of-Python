# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

# example data
xval = np.arange(0.1, 4, 0.5)
yval = np.exp(-xval)

plt.errorbar(xval, yval, xerr = 0.4, yerr = 0.5)

plt.title('matplotlib.pyplot.errorbar() function Example')
plt.show()
