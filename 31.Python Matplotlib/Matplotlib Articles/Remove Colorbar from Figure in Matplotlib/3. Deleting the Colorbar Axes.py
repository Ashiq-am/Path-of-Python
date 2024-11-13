import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(10, 10)

# Create a figure and axis
fig, ax = plt.subplots()
cax = ax.imshow(data, cmap='viridis')

# Add a colorbar
colorbar = fig.colorbar(cax)

# Remove the colorbar by deleting its axes
fig.delaxes(colorbar.ax)
plt.show()
