# importing packages
import seaborn
import matplotlib.pyplot as plt

# loading dataset
df = seaborn.load_dataset('tips')

# PairGrid object with hue
graph = seaborn.PairGrid(df)
# type of graph for non-diagonal(upper part)
graph = graph.map_upper(sns.scatterplot)
# type of graph for non-diagonal(lower part)
graph = graph.map_lower(sns.kdeplot)
# type of graph for diagonal
graph = graph.map_diag(sns.kdeplot, lw = 2)
# to show
plt.show()
