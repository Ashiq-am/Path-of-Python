# import all important libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# load dataset
data = "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"

# convert to dataframe
df = pd.read_csv(data)

# display top most rows
df.head()

# depict scatter plot illustration
sns.set_context("talk", font_scale=1.1)
plt.figure(figsize=(10, 6))
sns.scatterplot(x="petal.length",
				y="petal.width",
				data=df)
# Put the legend out of the figure
plt.legend(bbox_to_anchor=(1.01, 1), borderaxespad=0)
plt.xlabel("petal.length")
plt.ylabel("petal.width")
plt.tight_layout()
plt.savefig("Bubble_plot_Seaborn_scatterplot.png",
			format='png', dpi=150)
