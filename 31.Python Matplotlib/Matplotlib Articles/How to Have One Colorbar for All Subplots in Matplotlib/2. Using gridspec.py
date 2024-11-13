import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(8, 6))

# Create a GridSpec with space for a colorbar
gs = GridSpec(2, 3, figure=fig)
data = np.random.rand(10, 10)

ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[1, 0])
ax4 = fig.add_subplot(gs[1, 1])

im1 = ax1.imshow(data, vmin=0, vmax=1, cmap='viridis')
im2 = ax2.imshow(data, vmin=0, vmax=1, cmap='viridis')
im3 = ax3.imshow(data, vmin=0, vmax=1, cmap='viridis')
im4 = ax4.imshow(data, vmin=0, vmax=1, cmap='viridis')

# Add a colorbar
cbar_ax = fig.add_subplot(gs[:, 2])
fig.colorbar(im1, cax=cbar_ax)

plt.show()
