# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms


fig, ax = plt.subplots()
ax.plot(range(12, 24), range(12))
ax.set_yticks((2, 5, 7, 10))
ax.set_yticklabels(("Label-1", "Label-2",
					"Label-3", "Label-4"))

w = ax.get_yminorticklabels()
ax.text(15, 8, "yminorticklabels values : " + str(list(w)),
		fontweight ="bold")

fig.suptitle('matplotlib.axes.Axes.get_yminorticklabels() function Example\n\n', fontweight ="bold")
plt.show()
