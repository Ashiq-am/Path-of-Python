import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
data = np.random.rand(10, 10)

# Create a heatmap
plt.imshow(data, cmap='viridis')

# No colorbar is added here
plt.show()
