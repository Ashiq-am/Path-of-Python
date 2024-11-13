# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

fig, (ax, ax1) = plt.subplots(1, 2)
ax.plot([1, 2, 3])
ax.grid()

ax1.plot([1, 2, 3])
ax1.grid()
ax.set_navigate(False)

ax.set_title("Axes 1")
ax1.set_title("Axes 2")

w = ax.get_navigate()
ax.text(0.25, 2, "Value Return : " + str(w),
        fontweight="bold")

w = ax1.get_navigate()
ax1.text(0.25, 2, "Value Return : " + str(w),
         fontweight="bold")

fig.suptitle('matplotlib.axes.Axes.get_navigate()\
function Example\n\n', fontweight="bold")

plt.show()
