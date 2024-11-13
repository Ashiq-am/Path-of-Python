# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.plot([1, 2, 3])

ax.set_xlabel('X-Axis')
ax.set_ylabel('Y-Axis')

secax = ax.secondary_yaxis('right')
secax.set_ylabel('Secondary-Y-Axis')
ax.set_title('matplotlib.axes.Axes.secondary_yaxis() Example',
             fontsize=14, fontweight='bold')
plt.show()
