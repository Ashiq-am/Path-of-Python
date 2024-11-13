import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

# Define a color palette for each variable
palette = sns.color_palette('husl', n_colors=len(tips['day'].unique()))

# Create a plot with multiple variables mapped to hue
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='day', palette=palette)

plt.show()
