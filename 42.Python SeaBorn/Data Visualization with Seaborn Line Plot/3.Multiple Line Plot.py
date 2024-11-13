# import modules
import seaborn as sn
import matplotlib.pyplot as plt
import pandas as pd

# import data
data = pd.read_csv("C:\\Users\\Vanshi\\Desktop\\gfg\\cumulative.csv")

# select required data
data = data.iloc[2:10, :]

# plot data with different color scheme
sn.lineplot(x="kepid", y="koi_period", data=data, hue="koi_score")

# display plot
plt.show()
