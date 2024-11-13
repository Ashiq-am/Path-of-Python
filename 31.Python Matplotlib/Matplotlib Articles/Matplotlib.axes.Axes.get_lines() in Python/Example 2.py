# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, ax = plt.subplots()
x, y = 10 * np.random.rand(2, 1000)
ax.plot(x, y, 'go', alpha=0.2)

circ = mpatches.Circle((0.5, 0.5),
                       0.25,
                       transform=ax.transAxes,
                       facecolor='blue',
                       alpha=0.75)

ax.add_patch(circ)

w = list(ax.get_lines())

if len(w) == 0:
    ax.text(1, 8.5,
            "No line contained by the Axes \n")

else:
    ax.text(1, 8.5,
            "List of the lines contained by the Axes \n")
    x = 8.5

    for i in w:
        ax.text(1, x - 0.5, str(i))
        x -= 0.5

fig.suptitle('matplotlib.axes.Axes.get_lines() \
function Example', fontweight="bold")

plt.show()
