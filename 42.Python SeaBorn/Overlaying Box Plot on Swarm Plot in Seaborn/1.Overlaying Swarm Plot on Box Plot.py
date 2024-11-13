import seaborn as sns
import matplotlib.pyplot as plt

# Load example dataset
tips = sns.load_dataset("tips")
# Create box plot
sns.boxplot(x="day", y="total_bill", data=tips, whis=np.inf)

# Overlay swarm plot
sns.swarmplot(x="day", y="total_bill", data=tips, color=".2")

plt.show()
