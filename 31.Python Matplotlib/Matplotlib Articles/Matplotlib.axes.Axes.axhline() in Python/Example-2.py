# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
import numpy as np

fig, ax = plt.subplots()
x = np.arange(0, 8 * np.pi, 0.01)
y = np.sin(x)
ax.plot(x, y, color ='black')

threshold = 0.35
ax.axhline(threshold, color ='green',
		lw = 3, alpha = 0.7)

ax.fill_between(x, 0, 1, where = y > threshold,
				color ='green', alpha = 0.8,
				transform = ax.get_xaxis_transform())

ax.set_title('matplotlib.axes.Axes.axhline() Example')
plt.show()
