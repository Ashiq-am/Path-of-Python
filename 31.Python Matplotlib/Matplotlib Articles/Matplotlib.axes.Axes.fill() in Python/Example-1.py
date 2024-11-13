# Implementation of matplotlib function

import numpy as np
from matplotlib import patches
import matplotlib.pyplot as plt

x = np.array([1, 4, 1, 4])
y = np.array([1, 1, 4, 4])

fig, ax1 = plt.subplots()
ax1.fill(x, y, facecolor='green')
ax1.set_title('matplotlib.axes.Axes.fill Example 1')
plt.show()
