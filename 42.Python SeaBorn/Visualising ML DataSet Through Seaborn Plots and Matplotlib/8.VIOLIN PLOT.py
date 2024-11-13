# importing the modules and dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
dataset = pd.read_csv("Survival.csv")

sns.violinplot(x = 'Survived', y = 'Age', data = dataset,
			palette = {0 : "yellow", 1 : "orange"});
plt.show()
plt.figure()
