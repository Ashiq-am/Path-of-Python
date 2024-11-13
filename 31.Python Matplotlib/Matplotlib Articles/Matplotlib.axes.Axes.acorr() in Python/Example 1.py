# Implementation of matplotlib function

import matplotlib.pyplot as plt
import numpy as np

# Time series data
geeks = np.array([24.40, 110.25, 20.05,
				22.00, 61.90, 7.80,
				15.00, 22.80, 34.90,
				57.30])

# Plot autocorrelation
fig, ax = plt.subplots()
ax.acorr(geeks, maxlags = 9)

# Add labels to autocorrelation
# plotax.xlabel('X-axis')
ax.set_ylabel('Y-axis')

ax.set_title('matplotlib.axes.Axes.acorr() Example')

plt.show()
