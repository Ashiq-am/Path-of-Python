import matplotlib.pyplot as plt
import numpy as np

# Generating two datasets
data1 = np.random.normal(100, 10, 200)
data2 = np.random.normal(90, 15, 200)

# Creating a boxplot for both datasets
plt.boxplot([data1, data2], labels=['Data 1', 'Data 2'])

# Adding a title and labels
plt.title('Combined Boxplot of Two Datasets')
plt.ylabel('Values')

# Display the plot
plt.show()
