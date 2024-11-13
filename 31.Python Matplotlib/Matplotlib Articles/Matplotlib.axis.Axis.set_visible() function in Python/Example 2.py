# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
import numpy as np

X = np.arange(-20, 20, 0.5)
Y = np.arange(-20, 20, 0.5)
U, V = np.meshgrid(X, Y)

fig, ax = plt.subplots()
ax.quiver(X, Y, U, V)
w = ax.get_xaxis()

Axis.set_visible(w, False)

fig.suptitle('matplotlib.axis.Axis.set_visible() \
function Example\n', fontweight="bold")

plt.show()
