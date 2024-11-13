import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np

# Plot image on axes ax
ax = plt.gca()
img = np.random.random((10, 20))
im = plt.imshow(img, cmap='gray')

# Divide existing axes and create
# new axes at right side of image
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.15)

# Plot vertical colorbar
plt.colorbar(im, cax=cax)
plt.show()
