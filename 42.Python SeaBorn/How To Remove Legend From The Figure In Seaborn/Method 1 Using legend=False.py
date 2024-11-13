import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = sns.load_dataset("iris")

# Create a figure with two subplots side by side
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Plot 1: Histplot with legend
sns.histplot(data=iris, x="sepal_length", hue="species", multiple="stack",ax=axes[0])
axes[0].set_title('Histplot with Legend')
# Plot 2: Histplot without legend using legend=False
sns.histplot(data=iris, x="sepal_length", hue="species", multiple="stack", legend=False, ax=axes[1])
axes[1].set_title('Histplot without Legend')

plt.tight_layout()
plt.show()
