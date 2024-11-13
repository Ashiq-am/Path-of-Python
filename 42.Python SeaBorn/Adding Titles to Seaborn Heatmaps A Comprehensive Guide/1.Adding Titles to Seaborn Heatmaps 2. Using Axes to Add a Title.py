import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = np.random.rand(10, 12)

# Create a figure and axis
fig, ax = plt.subplots()

# Create a heatmap
sns.heatmap(data, ax=ax)

# Add a title using the axes object
ax.set_title('Heatmap Title with Axes')
plt.show()
