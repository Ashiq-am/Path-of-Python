import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")

# Create a swarm plot
sns.swarmplot(x="day", y="total_bill", data=tips)
plt.show()
