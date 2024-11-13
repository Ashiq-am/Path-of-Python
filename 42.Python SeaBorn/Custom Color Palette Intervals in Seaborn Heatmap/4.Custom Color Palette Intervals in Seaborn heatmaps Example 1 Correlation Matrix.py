import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, BoundaryNorm

df = sns.load_dataset("iris")
df_numeric = df.select_dtypes(include=[np.number])
correlation_matrix = df_numeric.corr()

# Define data ranges and corresponding colors
bounds = [-1, -0.5, 0, 0.5, 1]
colors = ["#d73027", "#f46d43", "#fee08b", "#a6d96a", "#1a9850"]
custom_palette = LinearSegmentedColormap.from_list("custom_palette", colors)
norm = BoundaryNorm(bounds, custom_palette.N)

# Create the heatmap with custom intervals
sns.heatmap(correlation_matrix, cmap=custom_palette, norm=norm, annot=True)
plt.title("Correlation Matrix with Custom Color Palette Intervals")
plt.show()
