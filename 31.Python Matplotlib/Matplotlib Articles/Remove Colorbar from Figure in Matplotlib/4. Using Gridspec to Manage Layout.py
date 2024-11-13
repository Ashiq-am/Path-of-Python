import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

data = np.random.rand(10, 10)

fig = plt.figure()
gs = gridspec.GridSpec(1, 2, width_ratios=[1, 0.05])  # Set width_ratios here

# Create the main plot
ax = fig.add_subplot(gs[0])
cax = ax.imshow(data, cmap='viridis')

# Add a colorbar in the second column
colorbar_ax = fig.add_subplot(gs[1])
colorbar = fig.colorbar(cax, cax=colorbar_ax)

# Remove the colorbar by deleting its axes
fig.delaxes(colorbar.ax)

# Update the GridSpec layout to reclaim space
gs = gridspec.GridSpec(1, 1)  # Recreate GridSpec without the colorbar space
ax.set_position(gs[0].get_position(fig))  # Adjust the position of the main plot
ax.set_subplotspec(gs[0])  # Update the subplot spec

plt.show()
