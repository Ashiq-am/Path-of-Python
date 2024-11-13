import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = np.random.rand(10, 12)

# Create a heatmap with a custom colormap
sns.heatmap(data, cmap='coolwarm')
plt.show()
