import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)

data1 = np.random.normal(loc=20, scale=5, size=100)
data2 = np.random.normal(loc=30, scale=10, size=100)
data3 = np.random.normal(loc=25, scale=7, size=100)

# Combine data into a list
data = [data1, data2, data3]

# Create a figure and axis
fig, ax = plt.subplots()
# Create the boxplot
box = ax.boxplot(data, patch_artist=True)
# Set labels for x-axis
ax.set_xticklabels(['Dataset 1', 'Dataset 2', 'Dataset 3'])

# Define colors for each dataset
colors = ['lightblue', 'lightgreen', 'lightcoral']

# Apply colors to each boxplot
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Create custom labels
labels = ['Dataset 1', 'Dataset 2', 'Dataset 3']

# Add a legend
ax.legend([box['boxes'][i] for i in range(len(colors))], labels)
plt.title('Boxplot with Legend for Multiple Datasets')
plt.show()
