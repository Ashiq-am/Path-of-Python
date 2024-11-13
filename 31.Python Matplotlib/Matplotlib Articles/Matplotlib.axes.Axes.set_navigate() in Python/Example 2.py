# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

fig, (ax, ax1) = plt.subplots(1, 2)

ax.plot([1, 2, 3])
ax.grid()

ax1.plot([1, 2, 3])
ax1.grid()

ax.set_navigate(False)
ax1.set_navigate(True)

ax.set_title(" set_navigate with False")
ax1.set_title(" set_navigate with True")

fig.suptitle('matplotlib.axes.Axes.set_navigate() function Example\n\n', fontweight="bold")

plt.show()
