import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
data_sequential = np.array([[10, 20], [20, 30]])
data_diverging = np.array([[1, -1], [-2, 2]])
data_qualitative = np.array([[0, 1], [2, 3]])

# Set up the matplotlib figure
plt.figure(figsize=(12, 10))

# Plot a heatmap using a sequential color palette
plt.subplot(311)  # 3 rows, 1 column, 1st subplot
sns.heatmap(data_sequential, cmap='Blues', annot=True)
plt.title('Sequential Color Palette')

# Plot a heatmap using a diverging color palette
plt.subplot(312)  # 3 rows, 1 column, 2nd subplot
sns.heatmap(data_diverging, cmap='coolwarm', annot=True, center=0)
plt.title('Diverging Color Palette')

# Plot a heatmap using a qualitative color palette
plt.subplot(313)  # 3 rows, 1 column, 3rd subplot
sns.heatmap(data_qualitative, cmap='Set1', annot=True)
plt.title('Qualitative Color Palette')

# Display the plots
plt.tight_layout()
plt.show()
