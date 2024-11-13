import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = {
    'x': list(range(10)) * 3,
    'y': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4],
    'category': ['A'] * 10 + ['B'] * 10 + ['C'] * 10
}
df = pd.DataFrame(data)

# Create the line plot with a predefined palette
sns.lineplot(x='x', y='y', hue='category', data=df, palette='dark')

plt.show()

# This code is contributed by Susobhan Akhuli
