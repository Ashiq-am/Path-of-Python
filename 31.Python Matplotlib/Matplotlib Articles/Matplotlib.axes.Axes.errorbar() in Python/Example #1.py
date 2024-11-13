# Implementation of matplotlib function

import numpy as np
import matplotlib.pyplot as plt

# example data
xval = np.arange(0.1, 4, 0.5)
yval = np.exp(-xval)

fig, ax = plt.subplots()
ax.errorbar(xval, yval, xerr=0.4, yerr=0.5)
plt.show()
