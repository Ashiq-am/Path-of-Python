import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")

g = sns.FacetGrid(tips)
g.map(sns.scatterplot, "total_bill", "tip")

# Accessing the Axes and inverting both X and Y axes
g.set(ylim=g.ax.get_ylim()[::-1], xlim=g.ax.get_xlim()[::-1])
plt.show()
