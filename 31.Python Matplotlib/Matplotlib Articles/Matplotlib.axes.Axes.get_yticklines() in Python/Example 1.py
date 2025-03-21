# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms


fig, ax = plt.subplots()
ax.plot(range(12, 24), range(12))
ax.set_yticks((2, 5, 7, 10))
ax.set_yticklabels(("Label-1", "Label-2",
					"Label-3", "Label-4"))

w = ax.get_yticklines()
ax.text(16, 8, "yticklines values : ",
		fontweight ="bold")
xx = 8
for i in w:
	ax.text(17, xx-0.5, str(i), fontweight ="bold")
	xx-= 0.5

fig.suptitle('matplotlib.axes.Axes.get_yticklines() function Example\n\n', fontweight ="bold")
plt.show()
