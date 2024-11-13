# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib.pyplot as plt
import numpy as np

X = np.arange(-4, 4, 0.5)
Y = np.arange(-4, 4, 0.5)
U, V = np.meshgrid(X ** 2, Y ** 2)

fig, ax = plt.subplots()
ax.quiver(X, Y, U, V)
w = ax.get_xaxis()

Tick.set_visible(w, False)

fig.suptitle('matplotlib.axis.Tick.set_visible() \
function Example', fontweight="bold")

plt.show()
