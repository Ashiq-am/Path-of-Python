import seaborn as sns
import matplotlib.pyplot as plt

# Load the example dataset
tips = sns.load_dataset("tips")

# Create a JointGrid
g = sns.JointGrid(x="total_bill", y="tip", data=tips)

# Plot the data
g = g.plot(sns.regplot, sns.histplot)

# Adjust the aspect ratio
g.ax_joint.set_aspect(2)
plt.show()
