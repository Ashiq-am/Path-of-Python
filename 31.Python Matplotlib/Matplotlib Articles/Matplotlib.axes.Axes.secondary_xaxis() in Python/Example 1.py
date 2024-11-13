# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.plot([1, 2, 3])

ax.set_xlabel('X-Axis')
ax.set_ylabel('Y-Axis')

secax = ax.secondary_xaxis('top')
secax.set_xlabel('Secondary-X-Axis')
ax.set_title('matplotlib.axes.Axes.secondary_xaxis() Example',
             fontsize=14, fontweight='bold')
plt.show()
