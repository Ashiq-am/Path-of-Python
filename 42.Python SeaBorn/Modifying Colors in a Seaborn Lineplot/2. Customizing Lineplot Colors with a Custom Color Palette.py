import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = {
    'x': list(range(10)) * 3,
    'y': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 7, 9, 2, 6, 8, 2, 1, 9, 3, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 7],
    'category': ['A'] * 10 + ['B'] * 10 + ['C'] * 10
}
df = pd.DataFrame(data)

# Create a custom color palette
custom_palette = sns.color_palette(["#FF6347", "#4682B4", "#32CD32"])

# Create the line plot with a custom color palette
sns.lineplot(x='x', y='y', hue='category', data=df, palette=custom_palette)

plt.show()

# This code is contributed by Susobhan Akhuli
