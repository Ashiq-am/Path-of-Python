import seaborn as sns
import matplotlib.pyplot as plt

# Load the example dataset
tips = sns.load_dataset("tips")

# Create a non-square jointplot
g = sns.jointplot(x="total_bill", y="tip", data=tips, height=8, ratio=2)
plt.show()
