import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np

# Plot image on axes ax
ax = plt.gca()
img = np.random.random((10, 20))
im = plt.imshow(img, cmap='gray')

# Divide existing axes and create new axes
# at bottom side of image
divider = make_axes_locatable(ax)
cax = divider.append_axes("bottom", size="5%", pad=0.25)

# Plot horizontal colorbar
plt.colorbar(im, orientation="horizontal", cax=cax)
plt.show()
