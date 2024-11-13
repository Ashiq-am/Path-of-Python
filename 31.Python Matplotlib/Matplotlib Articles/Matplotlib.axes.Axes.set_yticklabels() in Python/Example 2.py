# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
y2 = y + 0.2 * np.random.normal(size=x.shape)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.plot(x, y2)

ax.set_yticks([-1, 0, 1])

ax.spines['left'].set_bounds(-1, 1)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.set_yticklabels(("Val-1", "Val-2", "Val-3"))

fig.suptitle('matplotlib.axes.Axes.set_yticklabels()\
function Example\n\n', fontweight="bold")
fig.canvas.draw()
plt.show()
