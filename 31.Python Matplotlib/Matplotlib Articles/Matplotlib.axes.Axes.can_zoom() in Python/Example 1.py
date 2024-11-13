# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.plot([1, 2, 3])

w = ax.can_zoom()

ax.text(0.45, 2.75, "Value return by function:",
        fontweight="bold")
ax.text(0.9, 2.6, w, fontweight="bold")

fig.suptitle('matplotlib.axes.Axes.can_zoom() function \
Example\n\n', fontweight="bold")

plt.show()
