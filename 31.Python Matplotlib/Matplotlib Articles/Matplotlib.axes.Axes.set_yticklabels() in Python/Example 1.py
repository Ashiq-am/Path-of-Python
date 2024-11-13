# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms

fig, ax = plt.subplots()
ax.plot(range(12, 24), range(12))
ax.set_yticks((2, 5, 7, 10))
ax.set_yticklabels(("Label-1", "Label-2",
                    "Label-3", "Label-4"))

fig.suptitle('matplotlib.axes.Axes.set_yticklabels()\
function Example\n\n', fontweight="bold")
fig.canvas.draw()
plt.show()
