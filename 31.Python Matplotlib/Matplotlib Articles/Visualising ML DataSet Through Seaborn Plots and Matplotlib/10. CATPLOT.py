# importing the modules and dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
dataset = pd.read_csv("Survival.csv")

# Plot a nested barplot to show survival for Siblings and Gender
g = sns.catplot(x = "Siblings", y = "Survived", hue = "Gender", data = dataset,
				height = 6, kind = "bar", palette = "muted")
g.despine("lef t = True")
g.set_ylabels("Survival Probability")
plt.show()
