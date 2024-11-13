import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(10, 12)

# Define maximum value based on the 95th percentile
max_value = np.percentile(data, 95)

# Create a heatmap with the dynamic vmax
sns.heatmap(data, vmax=max_value, cmap="magma")
plt.show()
