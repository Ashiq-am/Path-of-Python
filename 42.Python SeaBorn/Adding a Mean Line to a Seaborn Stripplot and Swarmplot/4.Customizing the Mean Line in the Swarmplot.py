# Create the swarmplot
ax = sns.swarmplot(x='day', y='total_bill', data=tips)

# Calculate mean for each category
mean_values = tips.groupby('day')['total_bill'].mean()

# Add a customized mean line with transparency and label
for index, day in enumerate(mean_values.index):
    plt.axhline(mean_values[day], color='purple', linestyle='-', linewidth=3, alpha=0.5)

plt.show()
