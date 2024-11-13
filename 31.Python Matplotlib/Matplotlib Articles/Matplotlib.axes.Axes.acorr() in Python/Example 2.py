# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np


# Fixing random state for reproducibility
np.random.seed(10**7)
geeks = np.random.randn(100)

fig, ax = plt.subplots()
ax.acorr(geeks, usevlines = True, normed = True,
		maxlags = 80, lw = 3)
ax.grid(True)

ax.set_title('matplotlib.axes.Axes.acorr() Example')

plt.show()
