import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

np.random.seed(0)
data = np.random.randn(100, 4)

# setting the Seaborn style to 'whitegrid'
sns.set_style('whitegrid')

# createing subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# plotting on each subplot
for i, ax in enumerate(axes.flat):
    sns.histplot(data[:, i], kde=True, ax=ax)
    ax.set_title(f'Subplot {i+1}')

plt.tight_layout()
plt.show()
