# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

Z = np.random.rand(25, 25)

fig, ax0 = plt.subplots()

ax0.pcolormesh(Z)

ax0.set_title('matplotlib.axes.Axes.pcolormesh() Examples')
plt.show()
