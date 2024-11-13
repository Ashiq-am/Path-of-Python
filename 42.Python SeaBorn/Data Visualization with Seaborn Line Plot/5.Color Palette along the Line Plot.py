import seaborn as sn
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("C:\\Users\\Vanshi\\Desktop\\gfg\\cumulative.csv")

data = data.iloc[2:10,:]

sn.lineplot(x = "kepid", y = "koi_period",data=data, hue="koi_score", palette="pastel")

plt.show()
