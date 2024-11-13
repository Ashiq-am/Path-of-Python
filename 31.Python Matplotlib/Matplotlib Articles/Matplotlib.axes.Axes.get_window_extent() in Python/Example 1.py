# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

X = np.arange(-10, 10, 0.5)
Y = np.arange(-10, 10, 0.5)
U, V = np.meshgrid(X, Y)

fig, ax = plt.subplots()
ax.quiver(X, Y, U, V)
ax.invert_xaxis()
w = ax.get_window_extent()
print(str(w))

fig.suptitle('matplotlib.axes.Axes.get_window_extent()\
function Example', fontweight="bold")

plt.show()
