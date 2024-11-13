# ImpleIn Reviewtation of matplotlib function
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.set_xscale("log")
ax1.set_yscale("log")
ax1.set_adjustable("datalim")
ax1.plot([1, 3, 34, 4, 46, 3, 7, 45, 10],
		[1, 9, 27, 8, 29, 84, 78, 19, 48],
		"o-", color ="green")

ax1.set_xlim(1e-1, 1e2)
ax1.set_ylim(1, 1e2)

ax2.set_xscale("log")
ax2.set_yscale("log")
ax2.set_adjustable("datalim")
ax2.plot([1, 3, 34, 4, 46, 3, 7, 45, 10],
		[1, 9, 27, 8, 29, 84, 78, 19, 48],
		"o-", color ="green")

ax2.set_xlim(1e-1, 1e2)
ax2.set_ylim(1, 1e2)
ax2.set_aspect(2)

w = ax1.get_aspect()
w1 = ax2.get_aspect()

ax1.set_title("Axes 1\n Ratio : " +str(w))
ax2.set_title("Axes 2\n Ratio : " +str(w1))

fig.suptitle('matplotlib.axes.Axes.get_aspect() function Example\n\n', fontweight ="bold")
fig.canvas.draw()
plt.show()
