import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
# Set default figure size
plt.rcParams['figure.figsize'] = [12, 8]
# Generate example data
data = np.random.rand(10, 12)
# Create the heatmap
sns.heatmap(data, annot=True, cmap="Blues")
plt.show()
