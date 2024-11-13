# Implementation of matplotlib function
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.stem([0.3, 1.5, 2.7],
		[1, 3.6, 2.7],
		label ="stem test")

ax.legend()
ax.set_title('matplotlib.axes.Axes.stem Example')
plt.show()
