import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap, BoundaryNorm

# Generate some random data
data = np.random.rand(10, 10)

# Define custom colors
colors = ["#d73027", "#f46d43", "#fdae61", "#fee08b", "#ffffbf", "#d9ef8b", "#a6d96a", "#66bd63", "#1a9850", "#006837"]
cmap = LinearSegmentedColormap.from_list("custom", colors, N=100)

# Define boundaries and corresponding colors
boundaries = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
colors = ["#d73027", "#f46d43", "#fee08b", "#d9ef8b", "#66bd63"]
cmap = LinearSegmentedColormap.from_list("custom", colors, N=len(colors))
norm = BoundaryNorm(boundaries, cmap.N, clip=True)

# Create the heatmap with custom intervals
sns.heatmap(data, cmap=cmap, norm=norm)
plt.show()
