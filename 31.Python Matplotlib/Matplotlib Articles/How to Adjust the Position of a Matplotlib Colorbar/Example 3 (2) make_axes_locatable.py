# import matplotlib packages
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np; np.random.seed(1)

fig, ax = plt.subplots(figsize = (4,4))
im = ax.imshow(np.random.rand(11,16))
ax.set_xlabel("x label")

# instance is used to divide axes
divider = make_axes_locatable(ax)
cax = divider.new_vertical(size = "5%",
						pad = 0.7,
						pack_start = True)
fig.add_axes(cax)

# creating colorbar
fig.colorbar(im, cax = cax, orientation = "horizontal")

plt.show()
