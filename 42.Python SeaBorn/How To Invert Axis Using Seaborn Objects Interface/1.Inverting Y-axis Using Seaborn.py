import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")

# Create the scatter plot using Seaborn's FacetGrid
g = sns.FacetGrid(tips)
g.map(sns.scatterplot, "total_bill", "tip")

# Invert the Y axis using the FacetGrid's axis object
g.set(ylim=g.ax.get_ylim()[::-1])
plt.show()
