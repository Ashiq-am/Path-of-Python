# Create the stripplot
ax = sns.stripplot(x='day', y='total_bill', data=tips)

# Calculate mean for each category
mean_values = tips.groupby('day')['total_bill'].mean()

# Add a customized mean line
for day in mean_values.index:
    plt.axhline(mean_values[day], color='blue', linestyle='-', linewidth=2)

plt.show()
