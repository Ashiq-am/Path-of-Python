import seaborn as sns
import matplotlib.pyplot as plt

# Load the example dataset
tips = sns.load_dataset("tips")

# Create a jointplot
sns.jointplot(x="total_bill", y="tip", data=tips)
plt.show()
