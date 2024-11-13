# import all important libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# load dataset
data= "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"

# convert to dataframe
df = pd.read_csv(data)

# display top most rows
df.head()

# depict bubble plot illustration
sns.set_context("talk", font_scale=1.2)
plt.figure(figsize=(10,6))
sns.scatterplot(x='petal.length',
			y='petal.width',
			sizes=(20,500),
			alpha=0.5,
			data= df)
# Put the legend out of the figure
plt.legend(bbox_to_anchor=(1.01, 1),borderaxespad=0)

# assign labels
plt.xlabel("Sepal.length")
plt.ylabel("Sepal.width")

# assign title
plt.title("Bubble plot in Seaborn")

# adjust layout
plt.tight_layout()
