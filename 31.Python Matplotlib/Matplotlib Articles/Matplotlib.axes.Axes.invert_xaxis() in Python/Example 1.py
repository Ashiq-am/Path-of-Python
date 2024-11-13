# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

X = np.arange(-20, 20, 0.5)
Y = np.arange(-20, 20, 0.5)
U, V = np.meshgrid(X, Y)

fig, ax = plt.subplots()
ax.quiver(X, Y, U, V)
w = ax.invert_xaxis()
ax.set_title('matplotlib.axes.Axes.invert_xaxis() \
Example', fontsize=14, fontweight='bold')
plt.show()
