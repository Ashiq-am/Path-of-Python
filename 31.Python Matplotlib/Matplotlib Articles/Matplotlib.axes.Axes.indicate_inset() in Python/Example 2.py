# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

def geeks():
	from matplotlib.cbook import get_sample_data
	import numpy as np
	f = get_sample_data("axes_grid/bivariate_normal.npy",
						asfileobj = False)

	z = np.load(f)
	return z, (-3, 4, -4, 3)

fig, ax = plt.subplots()
ax.plot(range(-3, 5), range(-4, 4))
X, extent = geeks()
Z2 = np.zeros([150, 150], dtype ="g")
ny, nx = X.shape
Z2[30:30 + ny, 30:30 + nx] = X

ax.imshow(Z2**3 + 100, extent = extent,
		interpolation ="nearest",
		origin ="lower", cmap ="Greens")

axins, axins1 = ax.indicate_inset([-1.5, -2.5, 0.8, 0.8])

ax.set_title('matplotlib.axes.Axes.indicate_inset() Example',
			fontsize = 14, fontweight ='bold')
plt.show()
