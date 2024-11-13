# Implementation of matplotlib function

import numpy as np
import matplotlib.pyplot as plt

test = np.arange(0.01, 30.0, 0.1)

# Create figure
fig, ax = plt.subplots()

# log x axis
ax.semilogx(test, np.sin(3 * np.pi * test))
ax.grid()

ax.set_title('matplotlib.axes.Axes.semilogx Example2')
plt.show()
