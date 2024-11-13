import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Sample data
data1 = np.random.rand(10, 12)
data2 = np.random.rand(10, 12)

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# Create heatmaps
sns.heatmap(data1, ax=ax1)
sns.heatmap(data2, ax=ax2)

# Add titles to each subplot
ax1.set_title('First Heatmap')
ax2.set_title('Second Heatmap')

plt.show()
