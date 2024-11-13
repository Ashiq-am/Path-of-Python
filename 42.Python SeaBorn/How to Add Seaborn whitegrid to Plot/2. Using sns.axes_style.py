import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris')

# Temporarily set the style to whitegrid
with sns.axes_style('whitegrid'):
    # Create a plot
    sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species')

plt.show()
