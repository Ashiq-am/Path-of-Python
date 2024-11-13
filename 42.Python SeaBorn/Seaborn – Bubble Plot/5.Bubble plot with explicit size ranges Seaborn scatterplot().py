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

# depict bubble plot illustration
sns.set_context("talk", font_scale=1.2)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sepal.length',
				y='sepal.width',
				# size="body_mass_g",
				sizes=(20, 500),
				alpha=0.5,
				hue='variety',
				data=df)

# Put the legend out of the figure
plt.legend(bbox_to_anchor=(1.01, 1), borderaxespad=0)

# Put the legend out of the figure
plt.xlabel("sepal.length")
plt.ylabel("sepal.width")
plt.title("Bubble plot with Colors in Seaborn")
plt.tight_layout()
