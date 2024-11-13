import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset("tips")

# Plot a bar chart with default error bars
sns.barplot(x="day", y="total_bill", data=tips)
plt.show()
