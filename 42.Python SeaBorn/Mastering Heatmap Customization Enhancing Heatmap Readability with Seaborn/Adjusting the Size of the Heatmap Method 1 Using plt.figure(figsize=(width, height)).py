import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
# Generate sample data
data = np.random.rand(10, 12)
# Set the size of the figure
plt.figure(figsize=(12, 8))
# Create the heatmap
sns.heatmap(data, annot=True, cmap="Blues")
plt.show()
