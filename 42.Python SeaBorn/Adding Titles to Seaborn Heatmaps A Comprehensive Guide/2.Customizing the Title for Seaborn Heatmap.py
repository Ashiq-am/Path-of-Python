import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = np.random.rand(10, 12)

# Create a heatmap
sns.heatmap(data)

# Add a customized title
plt.title('Customized Heatmap Title', fontsize=16, color='blue', loc='left')
plt.show()
