# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

X = np.arange(-10, 10, 0.5)
Y = np.arange(-10, 10, 0.5)
U, V = np.meshgrid(X, Y)

fig, ax = plt.subplots()
ax.quiver(X, Y, U, V)
ax.invert_xaxis()

w = plt.get_current_fig_manager()

print("Value Return by get_current_fig_manager():")
print(w)

fig.suptitle('matplotlib.pyplot.get_current_fig_manager() \
function Example', fontweight="bold")

plt.show()
