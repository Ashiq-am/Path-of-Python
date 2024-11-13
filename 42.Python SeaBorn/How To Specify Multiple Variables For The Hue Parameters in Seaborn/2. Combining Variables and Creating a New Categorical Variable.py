import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Create a DataFrame with multiple variables
data = {'x': [1, 2, 3, 4], 'y': [10, 15, 20, 25], 'group1': ['A', 'A', 'B', 'B'], 'group2': ['C', 'D', 'C', 'D']}
df = pd.DataFrame(data)

# Create a new categorical variable combining group1 and group2
df['combined_group'] = df['group1'] + '-' + df['group2']

# Create a plot with the combined variable mapped to hue
sns.scatterplot(data=df, x='x', y='y', hue='combined_group')

plt.show()
