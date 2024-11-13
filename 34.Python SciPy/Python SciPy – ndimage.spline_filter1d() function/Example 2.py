# importing spline filter with one dimension.
from scipy.ndimage import spline_filter1d

# importing matplot library for visualiation
import matplotlib.pyplot as plt

# importing munpy module
import numpy as np

# creating an image
geek_image = np.eye(80)

geek_image[40, :] = 1.0

# in axis=0
axis_0 = spline_filter1d(geek_image, axis=0)

# in axis=1
axis_1 = spline_filter1d(geek_image, axis=1)

f, ax = plt.subplots(1, 3, sharex=True)

for ind, data in enumerate([[geek_image, "geek_image original"],
                            [axis_0, "spline filter in axis 0"],
                            [axis_1, "spline filter in axis 1"]]):
    ax[ind].imshow(data[0], cmap='gray_r')

    # giving title
    ax[ind].set_title(data[1])

# orientation layout of our image
plt.tight_layout()

# to show image
plt.show()
