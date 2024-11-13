# ImpleIn Reviewtation of matplotlib function
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.set_xscale("log")
ax1.set_yscale("log")
ax1.set_xlim(1e1, 1e3)
ax1.set_ylim(1e2, 1e3)
ax1.set_aspect(1)
ax1.set_title("Axes 1")

ax2.set_xscale("log")
ax2.set_yscale("log")
ax2.set_adjustable("datalim")
ax2.plot([1, 113, 10], [1, 119, 100], "o-")
ax2.set_xlim(1e-1, 1e2)
ax2.set_ylim(1e-1, 1e3)
ax2.set_aspect(1)
ax2.set_title("Axes 2")

w = ax1.get_adjustable()
w1 = ax2.get_adjustable()

ax1.text(20, 400,
		"	 Value return by\n get_adjustable() : " +str(w))
ax2.text(1, 200,
		" Value return by \nget_adjustable() : \n	 " +str(w1))

fig.suptitle('matplotlib.axes.Axes.get_adjustable() function Example\n',
			fontweight ="bold")
fig.canvas.draw()
plt.show()
