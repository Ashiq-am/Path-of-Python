# Implementation of matplotlib function

import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.01, 20.0, 0.01)

# Create figure
fig, ax = plt.subplots()

# log x and y axis
ax.loglog(t, 20 * np.exp(-t / 10.0), basex=2)

ax.set_title('matplotlib.axes.Axes.loglog Example2')
plt.show()
