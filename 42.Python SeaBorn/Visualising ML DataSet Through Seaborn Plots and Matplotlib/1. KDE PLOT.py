# importing the modules and dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
dataset = pd.read_csv("Survival.csv")

# KDE plot
sns.kdeplot(dataset["Age"], color = "green",
			shade = True)
plt.show()
plt.figure()
