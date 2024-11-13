import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
data = np.random.rand(10, 12)

# Create a heatmap without the color bar
sns.heatmap(data, cbar=False)

# Show the plot
plt.show()
