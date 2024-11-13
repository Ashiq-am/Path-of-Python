import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris')

# Create a FacetGrid plot with multiple variables
g = sns.FacetGrid(iris, col='species', hue='species', col_wrap=2)
g.map_dataframe(sns.scatterplot, x='sepal_length', y='sepal_width')
g.add_legend()

plt.show()
