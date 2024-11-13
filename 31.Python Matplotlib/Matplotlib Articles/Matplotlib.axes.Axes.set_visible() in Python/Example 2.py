# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

X = np.arange(-20, 20, 0.5)
Y = np.arange(-20, 20, 0.5)
U, V = np.meshgrid(X, Y)

fig, ax = plt.subplots()
ax.quiver(X, Y, U, V)
w = ax.get_xaxis()
w.set_visible(False)

fig.suptitle('matplotlib.axes.Axes.set_visible() \
function Example\n', fontweight="bold")

plt.show()
