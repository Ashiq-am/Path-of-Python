# Sample larger dataset
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generate random data
np.random.seed(42)
large_data1 = pd.DataFrame({
    'x': np.random.rand(100),
    'y': np.random.rand(100),
    'dataset': ['set1'] * 100
})

large_data2 = pd.DataFrame({
    'x': np.random.rand(100),
    'y': np.random.rand(100),
    'dataset': ['set2'] * 100
})

# Combine the larger datasets
large_combined_data = pd.concat([large_data1, large_data2])

# Create the scatter plot with transparency
sns.scatterplot(data=large_combined_data, x='x', y='y', hue='dataset', alpha=0.5)
plt.show()
