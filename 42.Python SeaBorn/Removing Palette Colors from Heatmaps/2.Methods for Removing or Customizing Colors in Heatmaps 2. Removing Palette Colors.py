import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

data = np.random.rand(10, 10)

# Define a custom colormap
colors = [(1, 1, 1), (0, 0, 0)]  # white to black
n_bins = 100  # Discretizes the interpolation into bins
cmap_name = 'my_colormap'
cm = LinearSegmentedColormap.from_list(cmap_name, colors, N=n_bins)

plt.imshow(data, cmap=cm)
plt.colorbar()
plt.show()
