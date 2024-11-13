# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)

fig, ax = plt.subplots()
for color in [ 'tab:green', 'tab:blue',
			'tab:orange']:
	n = 70
	x, y = np.random.rand(2, n)
	scale = 1000.0 * np.random.rand(n)
	ax.scatter(x, y, c = color, s = scale,
			label = color,
			alpha = 0.35)

ax.legend()
ax.grid(True)
fig.suptitle('matplotlib.axes.Axes.legend() function Example\n', fontweight ="bold")

plt.show()
