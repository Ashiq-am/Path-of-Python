import numpy as np

# Generate sample data
data = np.random.randn(10, 10)

# Create a heatmap with a diverging palette
sns.heatmap(data, cmap=sns.diverging_palette(240, 10, as_cmap=True))
plt.show()
