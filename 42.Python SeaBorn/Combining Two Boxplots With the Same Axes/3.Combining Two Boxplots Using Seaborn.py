import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generating two datasets
data1 = np.random.normal(100, 10, 200)
data2 = np.random.normal(90, 15, 200)

# Creating a DataFrame for plotting
df = pd.DataFrame({
    'Values': np.concatenate([data1, data2]),
    'Group': ['Data 1'] * len(data1) + ['Data 2'] * len(data2)
})

# Plotting the combined boxplot
sns.boxplot(x='Group', y='Values', data=df)

# Adding title and labels
plt.title('Combined Boxplot of Two Datasets')
plt.show()
