import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")

# Scatter plot using Seaborn's FacetGrid
g = sns.FacetGrid(tips)
g.map(sns.scatterplot, "total_bill", "tip")

# Invert the X axis using the FacetGrid's axis object
g.set(xlim=g.ax.get_xlim()[::-1])
plt.show()
