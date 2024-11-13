# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.axes_divider import HBoxDivider
import mpl_toolkits.axes_grid1.axes_size as Size

arr1 = np.arange(40).reshape((8, 5))
arr2 = np.arange(12).reshape((3, 4))

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(arr1)
ax2.imshow(arr2)

rect = 111
pad = 1
for ax in [ax1, ax2]:
	ax.locator_params(nbins = 1)
	ax.xaxis.set_visible(False)
	ax.yaxis.set_visible(False)

h1, v1 = Size.AxesX(ax1), Size.AxesY(ax1)
h2, v2 = Size.AxesX(ax2), Size.AxesY(ax2)

pad_v = Size.Scaled(1)
pad_h = Size.Fixed(pad)

my_divider = HBoxDivider(fig, rect,
						horizontal =[h1, pad_h, h2],
						vertical =[v1, pad_v, v2])

ax1.set_axes_locator(my_divider.new_locator(0))
ax2.set_axes_locator(my_divider.new_locator(2))

ax3 = plt.axes([0.4, 0.5, 0.001, 0.001], frameon = False)
ax3.xaxis.set_visible(False)
ax3.yaxis.set_visible(False)
ax3.annotate("GeeksforGeeks\n matplotlib module \n Axes class",
			(1, 0.5),
			xycoords ="axes fraction",
			va ="center", ha ="center",
			bbox = dict(boxstyle ="round, pad = 1", fc ="w"))

w1 = ax1.get_axes_locator()
w2 = ax2.get_axes_locator()
w3 = ax3.get_axes_locator()


fig.suptitle('matplotlib.axes.Axes.get_axes_locator() function Example\n\n'+str(w1)+'\n'+str(w2)+'\n'+str(w3)+'\n\n\n\n')
plt.show()
