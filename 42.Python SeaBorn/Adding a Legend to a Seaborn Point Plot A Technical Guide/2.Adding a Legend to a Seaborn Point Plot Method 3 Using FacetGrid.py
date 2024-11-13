import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("penguins")

# Creating a FacetGrid
g = sns.FacetGrid(data, col="species", hue="sex", height=4, aspect=1)
g.map(sns.pointplot, "island", "body_mass_g")
g.add_legend(title='Sex')
plt.show()
