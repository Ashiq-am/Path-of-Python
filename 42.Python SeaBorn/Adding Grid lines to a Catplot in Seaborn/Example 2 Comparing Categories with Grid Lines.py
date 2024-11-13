import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset("titanic")

# Create the catplot
g = sns.catplot(x="sex", y="survived", hue="class", kind="bar", data=titanic)

# Access the axes object
ax = g.ax

# Add light gray grid lines
ax.grid(True, axis="y", color="gray", alpha=0.5)
plt.show()
