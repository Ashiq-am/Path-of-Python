import matplotlib.pyplot as plt
import numpy as np

# Create a figure and a grid of subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 6))

data = np.random.rand(10, 10)
for ax in axes.flat:
    im = ax.imshow(data, vmin=0, vmax=1, cmap='viridis')

fig.subplots_adjust(right=0.8)
cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
fig.colorbar(im, cax=cbar_ax)

plt.show()
