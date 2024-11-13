import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Plot 1: Scatter plot with legend
sns.scatterplot(data=iris, x="sepal_length", y="sepal_width", hue="species", ax=axes[0])
axes[0].set_title('Scatter Plot with Legend')

# Plot 2: Scatter plot without legend
sns.scatterplot(data=iris, x="sepal_length", y="sepal_width", hue="species", ax=axes[1])
plt.legend().remove()  # Remove the legend
axes[1].set_title('Scatter Plot without Legend')

plt.tight_layout()
plt.show()
