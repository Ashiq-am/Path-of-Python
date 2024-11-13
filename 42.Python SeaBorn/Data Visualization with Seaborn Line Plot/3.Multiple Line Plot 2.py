import seaborn as sn
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("C:\\Users\\Vanshi\\Desktop\\gfg\\cumulative.csv")

data = data.iloc[2:10, :]

# using just style
sn.lineplot(x="kepid", y="koi_period", data=data, size="koi_score")

plt.show()


# using style, size and hue
sn.lineplot(x="kepid", y="koi_period", data=data,
			size="koi_score", hue="koi_score", style="koi_score")

plt.show()
