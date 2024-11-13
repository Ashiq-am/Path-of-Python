# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.plot([1, 2, 3])

w = ax.can_pan()
# print(w)

ax.text(0.4, 2.75, "Value return by can_pan() function:",
        fontweight="bold")
ax.text(0.9, 2.6, w, fontweight="bold")

fig.suptitle('matplotlib.axes.Axes.can_pan() function \
Example\n\n', fontweight="bold")

plt.show()
