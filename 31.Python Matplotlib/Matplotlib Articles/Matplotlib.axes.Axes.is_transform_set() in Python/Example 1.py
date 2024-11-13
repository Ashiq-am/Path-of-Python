# Implementation of matplotlib function
import matplotlib.pyplot as plt

fig, axs = plt.subplots()
axs.plot([1, 2, 3])

axs.set_title("Is artist is explicitly set transform : "
			+str(axs.is_transform_set()))

fig.suptitle('matplotlib.axes.Axes.is_transform_set() function Example', fontweight ="bold")

plt.show()
