import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
# Generate example data
data = np.random.rand(10, 12)
# Create the heatmap
ax = sns.heatmap(data, annot=True, cmap="Blues")
# Set the aspect ratio
ax.set_aspect("equal")
plt.show()
