import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset("tips")

# Creating a basic point plot
sns.pointplot(x="day", y="total_bill", data=tips)
plt.show()
