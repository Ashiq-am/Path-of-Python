import seaborn as sns
import matplotlib.pyplot as plt

# Create a swarm plot
sns.swarmplot(data=tips, x="day", y="total_bill")

# Display the plot
plt.show()
