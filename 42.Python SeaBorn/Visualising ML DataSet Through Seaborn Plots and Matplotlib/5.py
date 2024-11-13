# importing the modules and dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
dataset = pd.read_csv("Survival.csv")

# Histogram+Density Plot
sns.distplot(dataset["Age"], color = "green")
plt.show()
plt.figure()
