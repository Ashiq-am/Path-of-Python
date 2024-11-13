import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 6))

data = np.random.rand(10, 10)

# Plot data and add a colorbar
for ax in axes.flat:
    im = ax.imshow(data, vmin=0, vmax=1, cmap='viridis')
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    plt.colorbar(im, cax=cax)

plt.show()
