import seaborn as sns
import matplotlib.pyplot as plt
iris = sns.load_dataset("iris")

# Create a strip plot with custom colors
sns.stripplot(x="species", y="sepal_length", data=iris, jitter=True, palette="Set2", edgecolor="black", linewidth=1)

# Overlay KDE plots with custom styles
for species in iris['species'].unique():
    subset = iris[iris['species'] == species]
    sns.kdeplot(subset['sepal_length'], label=species, bw_adjust=0.5, linestyle="--", linewidth=2)

plt.title("Customized Sepal Length Distribution by Species")
plt.xlabel("Species")
plt.ylabel("Sepal Length")
plt.legend(title='Species')
plt.show()
