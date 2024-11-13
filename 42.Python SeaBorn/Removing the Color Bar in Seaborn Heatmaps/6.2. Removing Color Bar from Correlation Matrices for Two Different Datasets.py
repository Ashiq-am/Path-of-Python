import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

np.random.seed(0)
data1 = pd.DataFrame(np.random.rand(10, 10), columns=[f'Var{i}' for i in range(10)])
data2 = pd.DataFrame(np.random.rand(10, 10), columns=[f'Var{i}' for i in range(10)])
corr1 = data1.corr()
corr2 = data2.corr()

# Create a figure with subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,5))

# Create the first heatmap with a color bar
sns.heatmap(corr1, cmap='coolwarm', ax=ax1, annot=True, fmt=".2f", cbar=True, cbar_kws={'label': 'Correlation'})

# Create the second heatmap without a color bar
sns.heatmap(corr2, cmap='coolwarm', ax=ax2, annot=True, fmt=".2f", cbar=False)

# Customize the plots
ax1.set_title('Correlation Matrix with Color Bar')
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, horizontalalignment='right')
ax1.set_yticklabels(ax1.get_yticklabels(), rotation=0)

ax2.set_title('Correlation Matrix without Color Bar')
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, horizontalalignment='right')
ax2.set_yticklabels(ax2.get_yticklabels(), rotation=0)

# Adjust layout to prevent overlapping
plt.tight_layout()
plt.show()
