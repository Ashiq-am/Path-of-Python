# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms


fig, ax = plt.subplots()
ax.plot(range(12, 24), range(12))
ax.set_yticks((2, 5, 7, 10))

fig.suptitle('matplotlib.axes.Axes.set_yticks() function Example\n\n', fontweight ="bold")
plt.show()
