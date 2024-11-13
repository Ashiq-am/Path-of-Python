# import modules
import seaborn as sn
import matplotlib.pyplot as plt
import pandas as pd

# import data
data = pd.read_csv("C:\\Users\\Vanshi\\Desktop\\gfg\\bestsellers.csv")

# selcting required rows and columns
data = data.iloc[2:10, :]

# plotting a single line graph
sn.lineplot(x="Year", y="User Rating", data=data)

# displaying the plot
plt.show()
