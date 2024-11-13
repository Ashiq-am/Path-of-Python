import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Plot 1: Histplot with legend
sns.histplot(data=iris, x="sepal_length", hue="species", multiple="stack", ax=axes[0])
axes[0].set_title('Histplot with Legend')

# Plot 2: Histplot and then remove legend using ax.get_legend().remove()
sns.histplot(data=iris, x="sepal_length", hue="species", multiple="stack", ax=axes[1])
axes[1].get_legend().remove()
axes[1].set_title('Histplot without Legend')

plt.tight_layout()
plt.show()
