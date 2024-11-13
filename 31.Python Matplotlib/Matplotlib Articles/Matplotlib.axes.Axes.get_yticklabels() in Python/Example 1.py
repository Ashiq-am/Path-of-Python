# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms


fig, ax = plt.subplots()
ax.plot(range(12, 24), range(12))
ax.set_yticks((2, 5, 7, 10))
ax.set_yticklabels(("Label-1", "Label-2",
					"Label-3", "Label-4"))

w = ax.get_yticklabels()
ax.text(16, 10, "yticklabels values : ",
	fontweight ="bold")
x = 10
for i in list(w):
	ax.text(16, x-1, str(i), fontweight ="bold")
	x-= 1

fig.suptitle('matplotlib.axes.Axes.get_yticklabels() function Example\n\n', fontweight ="bold")
plt.show()
