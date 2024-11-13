# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
df = sns.load_dataset('tips')

# Create a figure with subplots (1 row, 2 columns)
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Create a basic swarm plot in the first subplot
sns.swarmplot(data=df, x='day', y='total_bill', ax=axs[0])
axs[0].set_title("Basic Swarm Plot")

# Create another swarm plot in the second subplot
ax2 = sns.swarmplot(data=df, x='day', y='total_bill', ax=axs[1])

# Adjust the x-position of the 'Fri' group in the second plot
for collection in ax2.collections:
    if collection.get_offsets()[0, 0] == 3:  # Assuming 'Fri' is at x=3
        offsets = collection.get_offsets()
        offsets[:, 0] += 0.2  # Shift 'Fri' group 0.2 units to the right
        collection.set_offsets(offsets)

axs[1].set_title("Swarm Plot with Shifted 'Fri' Group")

# Show the subplots
plt.tight_layout()
plt.show()
