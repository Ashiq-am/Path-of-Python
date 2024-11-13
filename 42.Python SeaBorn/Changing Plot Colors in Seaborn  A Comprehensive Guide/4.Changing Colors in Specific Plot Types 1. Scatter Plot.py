import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
iris = sns.load_dataset('iris')

# Create a scatter plot with custom colors
sns.scatterplot(x='sepal_length', y='sepal_width', data=iris, hue='species', palette='viridis')
plt.show()
