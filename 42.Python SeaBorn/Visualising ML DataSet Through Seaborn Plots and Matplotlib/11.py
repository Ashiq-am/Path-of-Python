# importing the modules and dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
dataset = pd.read_csv("Survival.csv")

# Based On Fare There Are 3 Types Of Tickets
sns.catplot(x = "PassType", y = "Fare", data = dataset)
plt.show()
plt.figure()
