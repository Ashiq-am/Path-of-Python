import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
# Generate example data
data = np.random.rand(10, 12)
# Create a subplot with specific size
fig, ax = plt.subplots(figsize=(12, 8))
# Create the heatmap
sns.heatmap(data, ax=ax,cmap="Blues")
plt.show()
