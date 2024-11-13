# Implementation of matplotlib function
import matplotlib.pyplot as plt

fig, axs = plt.subplots()
axs.plot([1, 2, 3])
axs.remove()

fig.suptitle('matplotlib.axes.Axes.remove() function Example', fontweight ="bold")

plt.show()
