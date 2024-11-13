import seaborn as sns
import matplotlib.pyplot as plt
iris = sns.load_dataset("iris")

# Create pairplot with black borders around markers for 'setosa'
sns.pairplot(iris, hue="species", markers=["o", "s", "D"],
             plot_kws={'edgecolor': 'black'})
plt.show()
