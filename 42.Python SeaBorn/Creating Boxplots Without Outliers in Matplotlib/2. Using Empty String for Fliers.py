import matplotlib.pyplot as plt
import numpy as np

np.random.seed(123)
data = np.random.normal(0, 1, 100)

# Introduce outliers
outliers = np.array([5, 6, 7])  # Add some outliers
data_with_outliers = np.concatenate([data, outliers])

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Boxplot with outliers
axs[0].boxplot(data_with_outliers)
axs[0].set_title('Boxplot with Outliers')
axs[0].set_ylabel('Value')

# Boxplot without outliers using empty string for flier properties
axs[1].boxplot(data_with_outliers, flierprops=dict(markeredgecolor='none', markerfacecolor='none', markersize=0))
axs[1].set_title('Boxplot without Outliers')
axs[1].set_ylabel('Value')

plt.tight_layout()
plt.show()
