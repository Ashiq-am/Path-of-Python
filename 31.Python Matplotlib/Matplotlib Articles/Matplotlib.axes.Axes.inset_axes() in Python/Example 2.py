# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np


def geeks():
	from matplotlib.cbook import get_sample_data
	import numpy as np
	f = get_sample_data("axes_grid / bivariate_normal.npy",
						asfileobj = False)
	z = np.load(f)
	return z, (-3, 4, -4, 3)

fig, ax = plt.subplots()

X, extent = geeks()
Z2 = np.zeros([150, 150], dtype ="g")
ny, nx = X.shape
Z2[30:30 + ny, 30:30 + nx] = X

ax.imshow(Z2, extent = extent,
		interpolation ="nearest",
		origin ="lower", cmap ="Greens")

axins = ax.inset_axes([0.5, 0.5, 0.47, 0.47])

axins.imshow(Z2, extent = extent,
			interpolation ="nearest",
			origin ="lower", cmap ="Greens")
x1, x2, y1, y2 = -1.5, -0.9, -2.5, -1.9
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)

ax.indicate_inset_zoom(axins)

ax.set_title('matplotlib.axes.Axes.inset_axes() Example',
			fontsize = 14, fontweight ='bold')
plt.show()
