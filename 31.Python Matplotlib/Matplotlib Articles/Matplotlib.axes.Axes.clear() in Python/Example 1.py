# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.plot([1, 2, 3])
ax.grid(True)
ax.clear()
ax.set_title('matplotlib.axes.Axes.clear() \
Example\n', fontsize=12, fontweight='bold')
plt.show()
