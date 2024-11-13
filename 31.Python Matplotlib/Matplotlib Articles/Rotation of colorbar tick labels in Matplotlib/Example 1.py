# Import libraries
import matplotlib.pyplot as plt
import numpy as np

# Plot image
a = np.random.random((10, 10))
plt.imshow(a, cmap='gray')

# Plot horizontal colorbar
cbar = plt.colorbar(
	orientation="horizontal", fraction=0.050)

# Set ticklabels
labels = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6,
		0.7, 0.8, 0.9, 1]
cbar.set_ticks(labels)

# Rotate colorbar ticklabels by 45 degrees
# anticlockwise
cbar.ax.set_xticklabels(labels, rotation=45)

plt.show()
