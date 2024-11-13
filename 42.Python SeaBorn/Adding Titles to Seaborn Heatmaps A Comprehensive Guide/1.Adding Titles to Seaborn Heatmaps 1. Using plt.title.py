import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = np.random.rand(10, 12)

# Create a heatmap
sns.heatmap(data)

# Add a title
plt.title('Sample Heatmap Title')
plt.show()
