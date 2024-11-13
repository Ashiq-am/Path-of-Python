# Create a figure with 2 subplots
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Plot 1: Basic Swarmplot
sns.swarmplot(x='day', y='total_bill', data=tips, ax=axes[0])
axes[0].set_title('Basic Swarmplot')

# Plot 2: Swarmplot with Mean Lines
sns.swarmplot(x='day', y='total_bill', data=tips, ax=axes[1])
mean_values = tips.groupby('day')['total_bill'].mean()
for day in mean_values.index:
    axes[1].axhline(mean_values[day], color='green', linestyle='--')

axes[1].set_title('Swarmplot with Mean Lines')

# Adjust layout
plt.tight_layout()
plt.show()
