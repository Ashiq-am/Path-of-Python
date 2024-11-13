# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms


fig, ax = plt.subplots()
ax.plot(range(12, 24), range(12))
ax.set_yticks((2, 5, 7, 10))

w = ax.get_yticks()
ax.text(15, 9, "ytick values : "+str(w),
	fontweight ="bold")

fig.suptitle('matplotlib.axes.Axes.get_yticks() function Example\n\n', fontweight ="bold")
plt.show()
