# import modules
import matplotlib.pyplot as mp
import pandas as pd
import seaborn as sb

# load data
data = pd.read_csv("bestsellers.csv")

# plotting heatmap
sb.heatmap(data.corr(), annot=None, cbar_kws={'shrink': 0.6})

# displaying heatmap
mp.show()
