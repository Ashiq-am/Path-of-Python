import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(10, 12)

# Create a heatmap with both minimum and maximum value for the color bar
sns.heatmap(data, vmin=0.2, vmax=0.8, cmap="viridis")
plt.show()
