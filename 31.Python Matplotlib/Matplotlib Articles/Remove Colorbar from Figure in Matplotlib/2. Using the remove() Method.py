import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
data = np.random.rand(10, 10)

# Create a heatmap
heatmap = plt.imshow(data, cmap='viridis')

# Add a colorbar
colorbar = plt.colorbar(heatmap)

# Remove the colorbar
colorbar.remove()

plt.show()
