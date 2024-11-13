# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np
import matplotlib.pyplot as plt

d = np.arange(25).reshape(5, 5)
xx, yy = np.meshgrid(np.arange(6), np.arange(6))

fig, ax = plt.subplots()

ax.set_aspect(1)
m = ax.pcolormesh(xx ** 2, yy ** 2, d ** 2)

Axis.set_zorder(m, -10)

plt.title('matplotlib.axis.Axis.set_zorder() \
function Example\n', fontweight="bold")

plt.show()
