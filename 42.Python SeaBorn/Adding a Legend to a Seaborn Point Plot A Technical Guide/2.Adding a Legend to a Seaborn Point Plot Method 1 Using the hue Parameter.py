import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset("tips")

# Creating a point plot with hue
sns.pointplot(x="day", y="total_bill", hue="sex", data=tips)
plt.show()
