# Implementation of matplotlib function

import numpy as np
from matplotlib import patches
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.hlines([1, 3, 5], -3, 5, color="green")
ax.set_title('matplotlib.axes.Axes.hlines Example')

plt.show()
