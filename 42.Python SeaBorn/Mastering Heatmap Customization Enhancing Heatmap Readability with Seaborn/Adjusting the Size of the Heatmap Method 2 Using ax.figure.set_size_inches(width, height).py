import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
# Generate example data
data = np.random.rand(10, 12)
# Create the heatmap
ax = sns.heatmap(data, annot=True, cmap="Blues")
# Set the size of the figure
ax.figure.set_size_inches(12, 8)
plt.show()
