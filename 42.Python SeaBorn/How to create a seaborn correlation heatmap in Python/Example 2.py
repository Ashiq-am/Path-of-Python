# import modules
import matplotlib.pyplot as mp
import pandas as pd
import seaborn as sb

# import file with data
data=pd.read_csv("C:\\Users\\Vanshi\\Desktop\\cumulative.csv")

# plotting correlation heatmap
dataplot=sb.heatmap(data.corr())

# displaying heatmap
mp.show()
