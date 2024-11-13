# Implementation of matplotlib function
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.set_yscale("log")
ax.set_adjustable("datalim")
ax.plot([1, 3, 10], [1, 9, 100], "o-",
		color ="green")

ax.set_ylim(1e-1, 1e3)
ax.set_aspect(1)
fig.suptitle('matplotlib.axes.Axes.set_yscale() function Example\n', fontweight ="bold")
plt.show()
