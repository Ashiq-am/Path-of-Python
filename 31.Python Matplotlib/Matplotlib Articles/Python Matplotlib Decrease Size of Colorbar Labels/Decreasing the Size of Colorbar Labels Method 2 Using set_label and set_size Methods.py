import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = np.random.rand(10, 10)

# Create plot
fig, ax = plt.subplots()
cax = ax.imshow(data, cmap='viridis')

# Add colorbar
cbar = fig.colorbar(cax, ax=ax)

# Manually adjust the label sizes
cbar.ax.yaxis.set_tick_params(labelsize=8)  # Set label size to 8

plt.show()
