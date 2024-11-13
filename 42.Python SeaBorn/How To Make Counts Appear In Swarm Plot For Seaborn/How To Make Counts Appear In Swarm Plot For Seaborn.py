import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
tips = sns.load_dataset("tips")

# Create swarm plot
sns.set(style="whitegrid")
ax = sns.swarmplot(x="day", y="total_bill", data=tips)

# Calculate counts for each day
counts = tips['day'].value_counts().sort_index()

# Add counts as annotations
for i, count in enumerate(counts):
    ax.text(i, tips['total_bill'].max() + 2, f"Count: {count}",
            ha='center', size='medium', color='black', weight='semibold')

# Set plot title and labels
plt.title('Swarm Plot of Total Bill by Day')
plt.xlabel('Day')
plt.ylabel('Total Bill')

# Show plot
plt.show()
