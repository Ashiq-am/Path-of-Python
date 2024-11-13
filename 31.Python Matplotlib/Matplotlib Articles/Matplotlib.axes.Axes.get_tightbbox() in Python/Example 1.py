# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

X = np.arange(-10, 10, 0.5)
Y = np.arange(-10, 10, 0.5)
U, V = np.meshgrid(X, Y)

fig, ax = plt.subplots()
ax.quiver(X, Y, U, V)
ax.invert_xaxis()
w = ax.get_tightbbox(fig.canvas.get_renderer(),
                     call_axes_locator=True,
                     bbox_extra_artists=None)

ax.set_title("Value Return :\n" + str(w),
             fontsize=10)

fig.suptitle('matplotlib.axes.Axes.get_tightbbox()\
function Example', fontweight="bold")

plt.show()
