import seaborn as sns
import matplotlib.pyplot as plt

# Load the example dataset
tips = sns.load_dataset("tips")

# Create a jointplot
g = sns.jointplot(x="total_bill", y="tip", data=tips)

# Adjust the aspect ratio
g.ax_joint.set_aspect(2)
plt.show()
