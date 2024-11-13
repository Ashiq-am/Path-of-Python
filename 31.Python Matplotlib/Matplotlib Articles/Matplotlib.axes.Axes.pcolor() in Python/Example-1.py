# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

Z = np.random.rand(6, 30)

fig, ax0 = plt.subplots()

ax0.pcolor(Z)

ax0.set_title('matplotlib.axes.Axes.pcolor() Examples')
plt.show()
