import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
tips = sns.load_dataset("tips")

# Create a figure with 2 subplots
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Plot 1: Basic Stripplot
sns.stripplot(x='day', y='total_bill', data=tips, ax=axes[0])
axes[0].set_title('Basic Stripplot')

# Plot 2: Stripplot with Mean Lines
sns.stripplot(x='day', y='total_bill', data=tips, ax=axes[1])
mean_values = tips.groupby('day')['total_bill'].mean()
for index, day in enumerate(mean_values.index):
    axes[1].axhline(mean_values[day], color='red', linestyle='--', label=f"Mean {day}" if index == 0 else "")

axes[1].set_title('Stripplot with Mean Lines')
axes[1].legend()

# Adjust layout
plt.tight_layout()
plt.show()
