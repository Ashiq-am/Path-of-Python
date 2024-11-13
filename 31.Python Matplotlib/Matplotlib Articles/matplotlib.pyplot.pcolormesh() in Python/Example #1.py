# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

Z = np.random.rand(25, 25)

plt.pcolormesh(Z)

plt.title('matplotlib.pyplot.pcolormesh() function Example', fontweight="bold")
plt.show()
