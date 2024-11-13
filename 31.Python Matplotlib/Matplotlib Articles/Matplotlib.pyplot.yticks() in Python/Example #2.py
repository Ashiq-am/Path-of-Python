#Implementation of matplotlib.pyplot.yticks()
# function

import matplotlib.pyplot as plt

from mpl_toolkits.axes_grid1.inset_locator import inset_axes, zoomed_inset_axes


def get_demo_image():
	from matplotlib.cbook import get_sample_data
	import numpy as np
	f = get_sample_data("axes_grid/bivariate_normal.npy",
						asfileobj=False)
	z = np.load(f)
	# z is a numpy array of 15x15
	return z, (3, 19, 4, 13)


fig, ax = plt.subplots(figsize=[5, 4])

Z, extent = get_demo_image()

ax.set(aspect=1,
	xlim=(0, 65),
	ylim=(0, 50))


axins = zoomed_inset_axes(ax, zoom=2, loc='upper right')
im = axins.imshow(Z, extent=extent, interpolation="nearest",
				origin="upper")

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.yticks(visible=False)


plt.show()
