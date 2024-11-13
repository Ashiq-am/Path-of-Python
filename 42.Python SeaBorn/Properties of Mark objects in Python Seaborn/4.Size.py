import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(0)
data = pd.DataFrame({
    'categories': ['A', 'B', 'C', 'D'],
    'values': np.random.randint(1, 100, 4),
    'sizes': np.random.randint(100, 500, 4)
})

sns.set(style="whitegrid", palette="Set2")

plt.figure(figsize=(8, 6))
sns.barplot(data=data, x='categories', y='values', hue='categories', palette="Set2",
            dodge=False, linewidth=2.5, edgecolor='black')

plt.title('GFG Plot')
plt.xlabel('Categories')
plt.ylabel('Values')

plt.legend(title='Categories', loc='upper right')
plt.show()
