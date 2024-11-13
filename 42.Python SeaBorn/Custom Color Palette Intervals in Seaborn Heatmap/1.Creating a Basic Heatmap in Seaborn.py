import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
data = np.random.rand(10, 10)

# Create the heatmap
sns.heatmap(data)
plt.show()
