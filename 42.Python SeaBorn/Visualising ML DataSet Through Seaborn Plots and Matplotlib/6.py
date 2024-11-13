# importing the modules and dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
dataset = pd.read_csv("Survival.csv")

# Adding Two Plots In One
sns.kdeplot(dataset[dataset.Gender == 'Female']['Age'],
			color = "blue")
sns.kdeplot(dataset[dataset.Gender == 'Male']['Age'],
			color = "orange", shade = True)
plt.show()
plt.figure()
