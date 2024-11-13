# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

Z = np.random.rand(30, 30)

fig, ax0 = plt.subplots()

ax0.pcolorfast(Z)

ax0.set_title('matplotlib.axes.Axes.pcolorfast() Examples')
plt.show()
