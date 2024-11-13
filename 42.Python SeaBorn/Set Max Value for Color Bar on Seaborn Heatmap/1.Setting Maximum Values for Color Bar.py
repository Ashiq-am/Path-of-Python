import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
data = np.random.rand(10, 12) * 100

# Create a heatmap with a specific maximum value for the color bar
sns.heatmap(data, vmax=50)
plt.show()
