import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'x': range(10),
    'y': [5, 4, 6, 7, 8, 5, 6, 7, 8, 9]
})

plot = sns.relplot(data=data, x='x', y='y', hue='category', style='category', s=100)
plot.add_legend()

# Move and customize the legend
sns.move_legend(plot, "upper left", bbox_to_anchor=(1, 1), ncol=2, title='Categories', frameon=False)
plt.subplots_adjust(right=0.75)
plt.show()
