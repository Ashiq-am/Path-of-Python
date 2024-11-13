# Implementation of matplotlib.pyplot.acorr()
# function

import matplotlib.pyplot as plt
import numpy as np


# Fixing random state for reproducibility
np.random.seed(10**7)

geeks = np.random.randn(51 )

plt.title("Autocorrelation Example")
plt.acorr(geeks, usevlines = True,
		normed = True, maxlags = 50,
		lw = 2)

plt.grid(True)
plt.show()
