# import modules
import matplotlib.pyplot as mp
import pandas as pd
import seaborn as sb
import numpy as np

# import file with data
data = pd.read_csv("C:\\Users\\Vanshi\\Desktop\\gfg\\bestsellers.csv")

# creating mask
mask = np.triu(np.ones_like(data.corr()))

# plotting a triangle correlation heatmap
dataplot = sb.heatmap(data.corr(), cmap="YlGnBu", annot=True, mask=mask)

# displaying heatmap
mp.show()
