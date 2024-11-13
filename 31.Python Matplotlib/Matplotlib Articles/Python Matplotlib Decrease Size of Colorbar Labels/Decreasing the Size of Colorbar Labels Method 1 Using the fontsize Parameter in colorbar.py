import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = np.random.rand(10, 10)

# Create plot
fig, ax = plt.subplots()
cax = ax.imshow(data, cmap='viridis')

# Add colorbar with fontsize parameter
cbar = fig.colorbar(cax, ax=ax)
cbar.ax.tick_params(labelsize=10)  # Set label size to 10

plt.show()
