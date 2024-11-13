import seaborn as sns
import matplotlib.pyplot as plt

# Load the penguins dataset
data = sns.load_dataset("penguins")

# Create a FacetGrid
g = sns.FacetGrid(data, col="species", hue="sex", height=4, aspect=1)
g.map(sns.pointplot, "island", "body_mass_g")
g.add_legend(title='Sex')

plt.show()
