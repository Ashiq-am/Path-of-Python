import matplotlib.pyplot as plt
import numpy as np

# Plot an image
a = np.random.random((10, 20))
plt.imshow(a, cmap='gray')

# Calculate (height_of_image / width_of_image)
im_ratio = a.shape[0]/a.shape[1]

# Plot vertical colorbar
plt.colorbar(fraction=0.047*im_ratio)
plt.show()
