# Implementation of matplotlib function
from mpl_toolkits.axes_grid1 import Size, Divider
import matplotlib.pyplot as plt


fig = plt.figure(1, (6, 6))

value1 = [Size.Fixed(2.), Size.Fixed(.8), Size.Fixed(1.2),
		Size.Fixed(.7)]
value2 = [Size.Fixed(1.2), Size.Fixed(.7), Size.Fixed(2.)]

polygon = (0.2, 0.2, 0.4, 0.4)
resultant = Divider(fig, polygon, value1,
					value2, aspect = False)

ax1 = fig.add_axes(polygon, label ="2")
ax2 = fig.add_axes(polygon, label ="3")
ax3 = fig.add_axes(polygon, label ="1")
ax4 = fig.add_axes(polygon, label ="4")

ax1.set_axes_locator(resultant.new_locator(nx = 0,
					ny = 0))
ax2.set_axes_locator(resultant.new_locator(nx = 0,
					ny = 2))
ax3.set_axes_locator(resultant.new_locator(nx = 3,
					ny = 2))
ax4.set_axes_locator(resultant.new_locator(nx = 3,
					nx1 = 4, ny = 0))

fig.suptitle('matplotlib.axes.Axes.set_axes_locator() function Example\n\n', fontweight ="bold")
plt.show()
