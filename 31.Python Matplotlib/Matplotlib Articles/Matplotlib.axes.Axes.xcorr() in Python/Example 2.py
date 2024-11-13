# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np


# Fixing random state for
# reproducibility
np.random.seed(10**7)
geeksx = np.random.randn(100)
geeksy = np.random.randn(100)

fig, ax = plt.subplots()
ax.xcorr(geeksx, geeksy, usevlines = True,
		normed = True, maxlags = 80,
		color ="green")

ax.grid(True)

ax.set_title('matplotlib.axes.Axes.xcorr() Example')

plt.show()
