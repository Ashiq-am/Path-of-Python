import seaborn as sns
import numpy as np


np.random.seed(0)

# generates random values
data = np.random.rand(12, 12)

# creating a colormap
colormap = sns.color_palette("Greens")

# creating a heatmap using the colormap
ax = sns.heatmap(data, cmap=colormap)
