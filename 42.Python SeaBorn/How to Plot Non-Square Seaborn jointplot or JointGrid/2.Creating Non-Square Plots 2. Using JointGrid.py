import seaborn as sns
import matplotlib.pyplot as plt

# Load the example dataset
tips = sns.load_dataset("tips")

# Create a JointGrid with a non-square aspect ratio
g = sns.JointGrid(x="total_bill", y="tip", data=tips, height=8)
g = g.plot(sns.regplot, sns.histplot)
g.fig.set_figwidth(12)
plt.show()
