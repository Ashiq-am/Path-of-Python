# Implementation of matplotlib function

import numpy as np
from matplotlib import patches
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.vlines([1, 2, 3, 4], 0, 1,
          color="green",
          transform=ax.get_xaxis_transform())

ax.set_title('matplotlib.axes.Axes.vlines Example')

plt.show()
