import matplotlib.pyplot as plt
import numpy as np

# Plot an image
a = np.random.random((10, 20))
plt.imshow(a, cmap='gray')

# Calculate (width_of_image/height_of_image)
im_ratio = a.shape[1]/a.shape[0]

# Plot horizontal colorbar
plt.colorbar(orientation="horizontal", fraction=0.047*im_ratio)
plt.show()
