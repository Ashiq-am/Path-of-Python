# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


fig, ax = plt.subplots()
x, y = 10 * np.random.rand(2, 1000)
ax.plot(x, y, 'go', alpha = 0.2)

circ = mpatches.Circle((0.5, 0.5), 0.25,
					transform = ax.transAxes,
					facecolor ='blue',
					alpha = 0.75)
ax.add_patch(circ)

print("Value return : \n", *list(ax.findobj()),
	sep ="\n")

fig.suptitle('matplotlib.axes.Axes.findobj() function Example', fontweight ="bold")

plt.show()
