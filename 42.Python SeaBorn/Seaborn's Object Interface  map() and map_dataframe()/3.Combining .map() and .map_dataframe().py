import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset("titanic")
g = sns.FacetGrid(titanic, col="class", row="sex")

# Use .map_dataframe() with custom function
g.map_dataframe(sns.histplot, x="age", bins=10, kde=True, color="green").set_titles("{row_name} - {col_name}")\
# Use .map() to add titles
g.map(plt.axhline, y=0, color="k", linestyle="--")
