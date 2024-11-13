import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")

# Create histogram with log-scaled y-axis
sns.histplot(tips["total_bill"], log=True)
plt.show()
