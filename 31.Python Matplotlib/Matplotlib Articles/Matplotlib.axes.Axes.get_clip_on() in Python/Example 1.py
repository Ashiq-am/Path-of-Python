# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

delta = 45.0

angles = np.arange(0, 360 + delta, delta)
ells = [Ellipse((2, 2), 5, 2, a) for a in angles]

fig, ax = plt.subplots()

for e in ells:
    e.set_alpha(0.1)
    ax.add_artist(e)

ax.set_xlim(-1, 5)
ax.set_ylim(-1, 5)

print("Value Return by get_clip_on() : ",
      ax.get_clip_on())

fig.suptitle('matplotlib.axes.Axes.get_clip_on()\
function Example\n\n', fontweight="bold")

plt.show()
