import seaborn as sns
import pandas as pd

# Sample dataset
data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [2, 3, 1, 5, 4],
    'category': ['A', 'B', 'A', 'B', 'A']
})

sns.set_hls_values(color='husl', h=0.6, l=0.6, s=0.8)

sns.scatterplot(x='x', y='y', hue='category', data=data)
