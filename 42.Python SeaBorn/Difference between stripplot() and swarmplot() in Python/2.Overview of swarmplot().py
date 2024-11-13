import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = sns.load_dataset("tips")

# Create a swarm plot
sns.swarmplot(x="day", y="total_bill", data=data)
plt.title("Swarm Plot of Total Bill by Day")
plt.show()
