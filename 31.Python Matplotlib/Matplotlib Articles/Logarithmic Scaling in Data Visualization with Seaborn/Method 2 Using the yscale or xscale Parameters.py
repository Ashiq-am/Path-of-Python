import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")

# Create scatterplot with log-scaled x-axis and y-axis
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.xscale('log')
plt.yscale('log')
plt.show()
