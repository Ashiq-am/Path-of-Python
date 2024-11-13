# Import libraries
import matplotlib.pyplot as plt
import numpy as np

# Plot image
a = np.random.random((10, 10))
plt.imshow(a, cmap='gray')

# Plot vertical colorbar
cbar = plt.colorbar(
	orientation="vertical", fraction=0.050)

# Set ticklabels
labels = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6,
		0.7, 0.8, 0.9, 1]
cbar.set_ticks(labels)

# Rotate colorbar ticklabels by 30 degrees clockwise
cbar.ax.set_yticklabels(labels, rotation=-30)

plt.show()
