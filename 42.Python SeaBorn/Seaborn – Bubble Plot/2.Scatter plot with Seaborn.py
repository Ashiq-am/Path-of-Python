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

# depict scatterplot illustration
sns.set_context("talk", font_scale=1.1)
plt.figure(figsize=(8, 6))
sns.scatterplot(x="sepal.length",
				y="sepal.width",
				data=df)

# assign labels
plt.xlabel("Sepal.Length")
plt.ylabel("sepal.width")
