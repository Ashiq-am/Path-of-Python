import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load example dataset
tips = sns.load_dataset("tips")

# Create a figure with two subplots
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Subplot 1: Default overlay without adjustments (shows overlapping issue)
sns.boxplot(ax=axes[0], x="day", y="total_bill", data=tips, whis=np.inf)
sns.swarmplot(ax=axes[0], x="day", y="total_bill", data=tips, color=".2")
axes[0].set_title('Without Adjustments')

# Subplot 2: Overlay with adjustments to handle overlapping
sns.boxplot(ax=axes[1], x="day", y="total_bill", data=tips, whis=np.inf, zorder=1)
sns.swarmplot(ax=axes[1], x="day", y="total_bill", data=tips, color=".2", zorder=2, alpha=0.7)
axes[1].set_title('With Adjustments')

# Display the plots
plt.tight_layout()
plt.show()
